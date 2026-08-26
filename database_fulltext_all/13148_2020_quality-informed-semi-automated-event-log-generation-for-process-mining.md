---
otero_id: 13148
otero_key: "J4QQ7WGE"
title: "Quality-informed semi-automated event log generation for process mining"
authors: "R. Andrews; C.G.J. van Dun; M.T. Wynn; W. Kratsch; M.K.E. Röglinger; A.H.M. ter Hofstede"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113265"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Quality-informed semi-automated event log generation for process mining

R. Andrews<sup>a,∗</sup>, C.G.J. van Dun<sup>c,∗</sup>, M.T. Wynn<sup>a</sup>, W. Kratsch<sup>b</sup>, M.K.E. Röglinger<sup>c</sup>, A.H.M. ter Hofstede<sup>a</sup>

![](/api/attachments/J4QQ7WGE/fulltext/images/70c606b1a714935e000e0e5951363b4030b743788b43f8c3b6ae56e66d1207af.jpg)

<sup>a</sup> Queensland University of Technology, Brisbane, Australia

<sup>b</sup> FIM Research Center, University of Augsburg, Augsburg, Germany

<sup>c</sup> FIM Research Center, University of Bayreuth, Bayreuth, Germany

## A R T I C L E I N F O

Keywords: Process mining Data quality Event log Log extraction

## A B S T R A C T

Process mining, as with any form of data analysis, relies heavily on the quality of input data to generate accurate and reliable results. A fit-for-purpose event log nearly always requires time-consuming, manual pre-processing to extract events from source data, with data quality dependent on the analyst's domain knowledge and skills. Despite much being written about data quality in general, a generalisable framework for analysing event data quality issues when extracting logs for process mining remains unrealised. Following the DSR paradigm, we present RDB2Log, a quality-aware, semi-automated approach for extracting event logs from relational data. We validated RDB2Log's design against design objectives extracted from literature and competing artifacts, evaluated its design and performance with process mining experts, implemented a prototype with a defined set of quality metrics, and applied it in laboratory settings and in a real-world case study. The evaluation shows that RDB2Log is understandable, of relevance in current research, and supports process mining in practice.

## 1. Introduction

In recent years, process mining as a set of techniques for analysing business processes [1] has seen substantial uptake in research and in practice. While current research focuses on the application of process mining and on identifying appropriate use cases [2], three key limitations hinder an even faster adoption in practice: (i) Most recent process mining approaches assume high-quality event logs, without describing how such logs can be extracted from non-process-aware information systems [3-7]; (ii) As event data is typically stored in relational databases, references to cases and events are only implicitly available and have to be identified in, and extracted from, source data as well as converted into flat event logs [8]; (iii) As with all other forms of data analysis, the accuracy and reliability of process mining results is de pendent on the quality of the input data (called event log). As stated in Ref. [9], data quality issues can arise while preparing event logs, e.g. inaccurate timestamps or ambiguous activity labels. These issues can lead to discovered models that do not match the real execution of the process. See Ref. [10] for further examples on the impact of data quality.

While the topic of data quality in process mining is being discussed in literature and in practice and some niche solutions have been devised (e.g. Ref. [11]), a generalised approach for dealing with quality issues in process mining is far from being realised. Most of today's quality analyses are subjective, ad-hoc or even ex-post, manual and specific to a certain application domain (e.g. Ref. [12]). Similarly, pre-processing source data and extracting event logs for process mining are still considered mostly manual tasks [13]. Data pre-processing has been shown to take up to 60% of the efort invested into any data mining project [14]. To the best of our knowledge, there is only a handful of approaches (or tools) available to support process analysts in extracting event logs in a systematic manner, including ProM plugins [15, 16], object-centric [17], redo log-based [8] or ontology-based approaches [18]. Each has limitations, and – as we show in this paper – none address quality issues of the source data.

To fill these gaps, this paper presents RDB2Log, a semi-automated, quality-informed approach to event log generation from relational databases. RDB2Log takes, as input, a relational data set and generates an assessment of its quality based on common data quality dimensions. Using this assessment and the database key constraints, decisions regarding the data's suitability for process mining can be made. RDB2Log supports the mapping of data columns to event log attributes and generation of the event log. The artifact proposed in this paper is envisioned as a step towards a process data quality lifecycle: systematic detection, repair and tracking of data quality issues.

To design and evaluate RDB2Log, we follow the precepts of the Design Science Research (DSR) methodology [19, 20] but, in complying with the design-evaluate-construct-evaluate pattern advocated in Ref. [21], we did not traverse DSR phases strictly iteratively, but switched between the design and develop as well as the demonstration and evaluation phases.

We deal with DSR phases as: (i) for problem identification, we justified the need for considering an integrated approach for qualityinformed event log generation in this section; (ii) design objectives will be derived from literature in Section 2; (iii) in the design and development phase, we conceive the design specifications for RDB2Log (Section 3); (iv) the results of our evaluation (including an expert survey as well as the instantiation and testing of our approach as a software prototype) are reported in Section 4. The paper concludes in Section 5 with implications, limitations and starting points for future research.

## 2. Background

## 2.1. Process mining and data quality

Process mining extracts knowledge about business processes by analysing event logs — digital recordings of event executions in information systems [1]. Information systems (generally) capture process-related data in relational databases and do not necessarily output process data in standard event log format. As such, references to events, cases and relating timestamps have to be extracted from source data and converted into flat event logs [8]. Each event record represents a single step in the execution of a process and has attributes representing the process instance (case ID), the process step (activity), and includes information on execution time (timestamp) and (optionally) the resource responsible for the step, and may include other auxiliary data [22].

Process mining, like any form of data analysis, sufers from crucial data quality problems [9, 10, 23]. Data quality plays an important role in evaluating whether available data can actually answer the questions that stakeholders have. Thus, according to the IEEE Task Force on Process Mining [22], the quality of data is an important principle on which successful process mining is built.

In Ref. [24], the authors review several process mining methodologies and conclude that existing methodologies note the importance of data quality but (i) do not provide concrete support for assessing data quality, and (ii) do not consider how data quality can be exploited in the data extraction and log generation phases. In Ref. [10], the authors consider the impact of some of the 27 event log quality issues they describe on process mining analyses. Here, the impact assessment is based on having already identified the presence of the quality issues in an existing log.

To close this gap, a first design objective (DO) for RDB2Log states:

DO 1 A quality-informed log extraction approach should cater for data quality.

## 2.2. Measuring data quality

Data quality is described as a multidimensional concept [25]. A full assessment of data quality involves examining multiple dimensions. Relevant dimensions have been defined exhaustively in literature (e.g., Refs. [25-28]). Based on a review of existing literature, widely used and cited dimensions were clustered based on synonymous or similar defi nitions, i.e. dimensions referencing the same or similar data quality issues are in the same cluster (see Appendix A). To assess the quality of source data, we first select from this list a set of dimensions that are (i) relevant to process mining event logs, and (ii) can be quantified. Dimensions are relevant if they deliver valuable information on the applicability of the underlying data to generate event logs. For example, while the precision or privacy of the data is highly relevant when building event logs from relational data [4, 29], the eficiency (use of memory) of the DBMS is not as relevant. A dimension is quantifiable if there exists at least one metric that impacts on this dimension. In ou work, we have extracted 12 quality dimensions from literature which are both quantifiable and relevant in the area of process mining. We focus on the prominent dimensions of precision, completeness and uniqueness as these are explicitly relevant for process mining.

Precision describes the level of detail encoded by data [30]. Completeness can be generically defined as “the extent to which data are of suficient breadth, depth and scope for the task at hand” [28]. The dimension of uniqueness prescribes that no entity exists more than once within the data set [31, 32].

Metrics present a formal way of measuring and quantifying data quality dimensions [33-36]. Depending on the context, metrics and dimensions generally difer in their degree of automation [37, 38] and in their importance and can therefore impact overall data quality more or less strongly [39]. A high degree of automation describes metrics which can be computed without requiring external information (such as domain knowledge). In the context of process mining, importance is dependent on the role a data attribute will play in an event log. For instance, for a timestamp data attribute being considered for use as the completed time of an activity in an event log, the importance would be placed on the value of the uniqueness dimension being low AND (ideally) the value of the precision dimension being high (thus maximising the chances that events are properly ordered). The same combination of dimension values is likely to be undesirable for a data attribute being considered for use as the case identifier attribute. From all this, we infer the following design objective:

DO 2 A quality-informed log extraction approach should assess the quality of the source data. An ex-ante assessment (i.e. before an event log is generated) is sensible. The importance of quality dimensions should depend on the log attribute that is to be assigned to the data attribute.

## 2.3. Event log extraction

In an extensive literature review, we have identified existing approaches (as well as reference processes, discussions, or meta models) for extracting event logs from relational databases or similar data sources (see Appendix B). We categorise these approaches by the concept used for extracting the log and the type of source data used. Concepts range from artifact-centric (focusing on activities revolving around the life cycle of business artifacts, cf. Ref. [40]) to data- or object-centric approaches. In this context, we define an approach as concept-independent if its extraction is not based on a specific paradigm. After examining and evaluating strengths and weaknesses of existing approaches, we infer a design objective that relates to the event log generation process in general:

DO 3 A quality-informed log extraction approach should use as input a relational database as these are commonly used in practice as well as in existing log extraction approaches. It should be concept-independent, i.e. events can be extracted from databases irrespective of the concept of event representation in the database. The approach should output the event log in a standard format for process mining toolsets (e.g. XES).

## 2.4. Classical process mining challenges

In addition to the design objectives listed above, we focus on the applicability and ease-of-use of RDB2Log. Among the most important challenges that need to be addressed in process mining is the improvement of usability and understandability for non-experts [22].

![](/api/attachments/J4QQ7WGE/fulltext/images/475670e5530e67c24dbabe1e8f5cf75d488269ce509bc90a3e7b70206c9388fc.jpg)  
Fig. 1. RDB2Log — quality-informed event log generation.

Users should not need programming skills or extensive knowledge of relational database concepts. Typical remedies for this are the use of well-structured and systematic analysis processes and the implementation of intuitive interfaces that hide sophisticated algorithms and provide automated parameter settings and analysis. A recent analysis of addressed challenges from van der Aalst [22] shows that of 15 contributions addressing usability and understandability in process mining none focus on the log extraction phase [2]. In order to change this, the following design objective is formulated:

DO 4 A quality-informed log extraction approach should (i) guide the user through the log generation process, (ii) be semi-automated, and (iii) ofer decision support to the user when selecting the data for the log.

## 3. Generating quality-informed event logs

Fig. 1 illustrates our RDB2Log approach to extracting event logs from relational data. Our approach exploits database constraints and data quality assessments to support the semi-automated extraction of event records. Section 3.1 contains an explanation of how case and event data may be represented in tables participating in primary key –foreign key relationships. A description of the metrics-based concept of data quality assessment is shown in Section 3.2 with Section 3.3 providing examples of how metric results and their impact on process mining analyses may be interpreted. In Section 3.4 the notion of event constructors as mappings of database columns to log attributes is explained. The mappings are (i) table by table, (ii) user-selected, and (iii) quality-informed. That is, each database column is assessed against several quality dimensions for each event log attribute role assignment while taking into account acceptance criteria based on one or more quality dimensions and threshold values.

## 3.1. Database relationship assessment

RDB2Log caters for (i) process-related event data generated by non process-aware information systems, (ii) stored in relational form, (iii) that needs to be transformed into an event log for process mining. To ensure that a meaningful event log can be extracted, certain requirements (RQs) must be met:

RQ 1 There exists column(s) with a Unique or Primary Key constraint. RQ 2 Some tables have Foreign Key constraints defined. RQ 3 There is timestamp information recorded.

In this formulation, each Unique/Primary Key can be considered as a potential case identifier and each non-key column in the same table can be a case attribute. Tables which contain a Foreign Key referencing the Unique/Primary Key participate in a many-to-1 relationship with the referenced table. So long as these tables contain at least one timestamp column, each record in the table can be considered as event data where various columns may be mapped to event attributes such as activity or resource (see Section 3.4).

## 3.2. Data quality quantification

Our artifact incorporates 12 data quality dimensions that have been deemed quantifiable and relevant for process mining (Appendix Table A1). To retain clarity, we focus on three dimensions which are exceptionally relevant for process mining (precision, uniqueness, completeness). The operationalisation of the dimensions is not specific to RDB2Log and can be modified. Most metrics can be computed on a data column level and can therefore inform quality dimensions on an attribute level as well as at an overall log level. Others contribute to only log level assessment. Metrics have been normalized so that a value of 0 is considered “low-quality” while 1 is considered “high-quality”. A list of all 25 metrics (including sources, descriptions and their impact on the dimensions) which are included in the artifact can be found in a separate report<sup>1</sup>.

Let data column $c = ( \nu _ { 1 } , . . . . , \nu _ { n } )$ be a vector of n values. The three metrics described in detail in this work (timestamp precision $m _ { \mathrm { t p r e } } ( c ) ,$ missing values $m _ { \mathrm { m i s s } } ( c ) _ { \mathrm { : } }$ , and non-unique values $m _ { \mathrm { n u n i } } ( c ) )$ ) and their impact on the three dimensions is shown below. We consider the selected dimensions to be an indicative, but not a complete set of all possible relevant and quantifiable dimensions.

## 3.2.1. Timestamp precision [41]

This metric computes the average as well as minimum and maximum granularity of values in timestamp columns. Granularity is de fined as the smallest time unit available in a timestamp value and represents the exactness with which time is recorded. Therefore, the metric impacts the dimension of precision.

Let datepart(t,v) be a function returning 1 if time unit t of datetime value v is not 0, and 0 otherwise. The metric for timestamp precision follows:

$$
m _ {\mathrm{tpre}} (c) = \frac {1}{n} \sum_ {i = 1} ^ {n} f _ {\text { gran }} (v _ {i}) \text {   with   } f _ {\text { gran }} (v _ {i}) \left\{ \begin{array}{l l} 1, & \text { if   } d a t e p a r t (m s, v _ {i}) \neq 0 \\ 0. 7 5, & \text { else   if   } d a t e p a r t (s e c, v _ {i}) \neq 0 \\ 0. 5, & \text { else   if   } d a t e p a r t (m i n, v _ {i}) \neq 0 \\ 0. 2 5, & \text { else   if   } d a t e p a r t (h r, v _ {i}) \neq 0 \\ 0, & \text { otherwise } \end{array} \right.\tag{1}
$$

## 3.2.2. Missing values [32, 34]

This metric returns the proportion of missing values in a data column (including NULLs, empty cells, other keywords or default values that could be considered as missing values). M is defined as the set of all representations of missing values. The metric impacts the completeness dimension.

$$
m _ {\mathrm{miss}} (c) = \frac {1}{n} \sum_ {i = 1} ^ {n} f _ {\mathrm{miss}} (v _ {i}), \text {with} f _ {\mathrm{miss}} (v _ {i}) = \left\{ \begin{array}{l l} 1, & \text {if} v _ {i} \in M \\ 0, & \text {otherwise} \end{array} \right.\tag{2}
$$

## 3.2.3. Non-unique values [32]

This metric computes the proportion of non-unique values in a column. Non-unique values are values that occur more than once within a column. The ratio of non-unique values gives an indication of the richness of column values and impacts the dimension of uniqueness. Let $c ^ { * }$ be the set of distinct values in c.

$$
m _ {\mathrm{nuni}} (c) = 1 - \frac {| c ^ {*} |}{n}\tag{3}
$$

## 3.3. Interpreting data quality metrics

The metrics-based quality assessment approach described in this paper allows users to anticipate consequences of data quality issues for process mining from two perspectives: Can the data be adequately prepared as an event log for a process mining analysis, and can the ensuing analysis produce meaningful results? Therefore, this subsection provides exemplary interpretations of metric results and their impact on process mining preparation and results.

## 3.3.1. Interpreting the timestamp precision metric

The precision metric is particularly relevant to datetime columns that are candidates for mapping to event timestamp attributes and directly impacts process discovery, process conformance and performance analysis. Critically, if the value of the $m _ { \mathrm { t p r e } } ( c )$ precision metric indicates that the granularity of recorded timestamps is coarser than the actual interval between occurrence of events (in the same case), it is clear that event ordering issues will be encountered leading to paral lelism instead of sequence in the discovered model (see Table 1).

Coarser granularity also afects performance due to the resulting temporal flattening. If lifecycle transitions are taken into account, the efects on performance analysis are shown in Table 2.

## 3.3.2. Interpreting the missing values metric

In general, anything but very low values of $m _ { \mathrm { m i s s } } ( c )$ for database columns intended to be mapped to critical (mandatory) event log attributes such as case identifier, activity label or timestamp are undesirable. Missing case identifier values means that events cannot be assigned to the correct (or any) case. Depending on the database management system in use, missing values in a (string, char, varchar) column intended to be mapped to the event activity label attribute may be represented as a literal ‘NULL’ and a missing value in a datetime column may be exported as a default datetime value, usually the default datetime the system can represent, e.g. ‘1900-01-01 00:00:00.000’ in the case of MS SQL Server, which will introduce event ordering issues.

Table 2  
Performance issues — coarse granularity timestamps.

<table><tr><td>Relationship</td><td>Lifecycles</td><td>Performance implication</td></tr><tr><td>Same event</td><td>Start/complete</td><td>Activity duration = 0</td></tr><tr><td>Sequential events</td><td>Complete/complete</td><td>Sojourn time = 0</td></tr><tr><td>Sequential events</td><td>Start/complete</td><td>Wait time = 0</td></tr></table>

## 3.3.3. Interpreting the non-unique values metric

The $m _ { \mathrm { n u n i } } ( c )$ metric ofers insights into a number of diferent po tential column→ event log attribute mappings. For datetime columns that may be considered as an event log timestamp attribute, it is desirable that $m _ { \mathrm { n u n i } } ( c )$ indicates a low level of non-unique values as this means event ordering will be possible. If $m _ { \mathrm { n u n i } } ( c )$ indicates a significant number of non-unique (timestamp) values, further investigation should be carried out to determine whether the non-unique values occur intracase, inter-case, or both. If non-unique values do not exist intra-case, but do occur inter-case, event ordering may not be afected (but it is likely that so-called “batching” of activities is taking place).

The $m _ { \mathrm { n u n i } } ( c )$ value can also be applied to database columns under consideration for use as case identifier attribute. Ideally, the $m _ { \mathrm { n u n i } } ( c )$ value should be neither close to 0 (all unique), nor close to 1 (all the same). In fact the $m _ { \mathrm { n u n i } } ( c )$ value for a database column that is a candidate for use as a case identifier can provide insights into the success or otherwise of record merging where event data has been collected from multiple sources. The $m _ { \mathrm { n u n i } } ( c )$ can be used to estimate the number of cases that will occur in the log which can then be compared to the expected number of cases. As an example, consider a hospital admittance system (that records patient ID as identifier) and an emergency room system (that records presentation ID as identifier). If these two record sets were aggregated with a view to investigating hospital processes, it is possible that patients who first attend the emergency room and are subsequently admitted to hospital will result in two separate cases in the event log, i.e. the emergency room presentation and the (related) hospital admittance for the same patient, rather than a single case for the overall hospital encounter.

In a similar vein, the $m _ { \mathrm { n u n i } } ( c )$ value for a database column under consideration for use as the activity label event log attribute should be neither close to 0 (all unique), nor close to 1 (all the same). Here, a low value for $m _ { \mathrm { n u n i } } ( c )$ can be interpreted as indicating a wide range of activity labels (with possibly multiple syntactically diferent, but semantically similar values) which would manifest as unnecessarily complex discovered process models.

Table 1  
Event ordering issues — coarse granularity timestamps.

<table><tr><td></td><td>Event A</td><td>Event B</td><td>Modelled as</td><td>δ (A, B)</td></tr><tr><td>Actual</td><td>2019-08-07 11:05:10.55</td><td>2019-08-07 11:25:34.75</td><td></td><td>0:20:29.20</td></tr><tr><td>Recorded</td><td>2019-08-07 11:00:00.00</td><td>2019-08-07 11:00:00.00</td><td></td><td>0:00:00.00</td></tr></table>

![](/api/attachments/J4QQ7WGE/fulltext/images/453f833131050233ff48565e1345e8c4a5bf7c45d1574f18c8084f492d0ba40a.jpg)  
Fig. 2. Event and Timestamp event constructors.

We note that this column-based metric can only be a preliminary analysis. While it is useful in gaining insights into the distribution of values in a column and their suitability for process mining (see examples above), it cannot identify as (potential) duplicates values such as ‘John Smith’ and ‘J. Smith’, and it cannot provide insights into the uniqueness of data entries spanning multiple columns (e.g., multiple tasks being executed by the same resource at the same time). Thus, we acknowledge that single-column assessments can lead to the identifi cation of false positives, e.g. by discovering and listing duplicate values as issues within a column which, from a multi-column perspective, can be accepted as correct. This can skew the data quality assessment to the negative.

## 3.4. Event log attribute assignment

RDB2Log requires process-related data as a relational database for which unique key (UK)–foreign key (FK) (1: n) relationships have been defined in the database schema. We propose the notion of event constructors as mappings from database columns to event log attributes. The mappings are (i) table at a time, (ii) user-selected, and (iii) qualityinformed (the data quality of each column in the database is assessed against quality dimensions and each event log attribute role assignment has an acceptance criterion based on one or more quality dimensions and threshold values).

Event data can be encoded in multiple fashions in relational data and any database column with a datetime datatype points to event data. This paper focuses on two possibilities that are common in our experience. Firstly, events can be represented as a datetime (or similar) datatype column in the referenced table (containing the unique key used as case ID). The value of the datetime column is used as event timestamp and the name of the column as activity name (see Event constructor in Fig. 2). Secondly, events can be stored in a referencing table (referencing the case ID as foreign key). The activity name and timestamp are selected from the child table attributes and matched to each other (see Timestamp constructor in Fig. 2).<sup>2</sup> For each selected event representation in the source data, a constructor defining the necessary attributes (case identifier, activity label, timestamp and optional case/event data) is created, as shown in Fig. 2. The set of event log rows is then extracted.

Here, we define the diferent event constructors (each as a mapping from a relational database table to the event log table). Firstly, let be a universe of attribute names. Let T be a database table and Schema T( ) be the set of column names of table T. For each A Schema T( ), <sup>T</sup> is the domain (datatype) of A in table T. Let Inst(T) be the set of rows of table T. For all t ∈ Inst(T), t : Schema(T)↦Ω, a universe of values where t A( ) <sup>T</sup> for all A ∈ Schema(T). Unique(T,A) where A ⊆ Schema(T) denotes that the set of columns A is a key in table T and ForeignKey(R,B,T,A) where B ⊆ Schema(R) and A ⊆ Schema(T) and Unique(T,A) denotes that the set of columns B in table R is a foreign key referencing the set of columns A of table T. Let LC = {assign,schedule,start,complete,…} be a set of lifecycle transitions.

The Event constructor type is associated with the case table, i.e. the table with the unique key that is referenced through foreign key relationships. Let U be a (case) table and let Mapping : Schema U caseid timestamp casedata activity LC( ) { , , } ({ } )× with the requirements that {caseid,timestamp}⊆ ran(Mapping ) and there is at least one l ∈ LC such that (activity,l) ∈ ran(Mapping ). Let $X _ { 1 } , \cdots , X _ { n } \in$ Schema(U) be such that = datetime <sub>X</sub><sup>U</sup> for all 1 ≤ i ≤ n and Mapping (X ) = (activity,l ) where l ∈ LC.

Let ( )U be the event log table and Schema U( ( )) = { , , , } { Schema( )|Mapping ( )caseid activity timestamp transition A U A = casedata}. Furthermore, Unique(U,caseid). The Event constructor maps rows in the case table to rows in the event log table as follows. For all 1 ≤ i ≤ n, for all s ∈ Inst(U), an instance e Inst U( ( ))<sup>s</sup> exists such that:

• e caseid s Y ( ) ( ) = <sup>s</sup> where Y ∈ Schema(U) such that Mapping (Y) = caseid,

• e activity X ( ) = <sup>s</sup> i,

• e transition l i ( ) = <sup>s</sup> i,

$e _ { i } ^ { s } ( t i m e s t a m p ) = s ( X _ { i } ) _ { \cdot }$ , and

• e Y s Y ( ) ( ) = <sup>s</sup> if Y ∈ Schema(U) and Mapping (Y) = casedata.

No other instances of this form are in Inst U( ( )).

The Timestamp constructor is associated with the event table(s). That is, the table(s) with a foreign key that references a unique key (in the case table). Let R be an (event) table and let Mapping : Schema(R)↦ {caseid,activity,eventdata} ({ } )timestamp LC× with the requirements that {caseid,activity}⊆ ran(Mapping ) and there is at least one $l \in L C$ such that (timestamp,l) ∈ ran(Mapping ). Let $X _ { 1 } , \cdots , X _ { n }$ ∈ Schema(R) be such that $\mathcal { D } _ { X _ { i } } ^ { R } = d a t e t i m e$ for all $\begin{array} { r l r l r l } { { 1 } } & { { } \le { } } & { i } & { { } \le { } } & { n } \end{array}$ and Mapping (X ) = (timestamp,l ) where $l _ { i } \in L C$

Let ${ \mathcal { T } } ( R )$ be the event log table and Schema $\mathcal { T } ( R ) ) =$ { , , , } {caseid activity timestamp transition A Schema R Mapping A( )| ( ) = eventdata}. Furthermore, ForeignKey(R,caseid,U,caseid) where U is the referenced case table and Unique(U,caseid). The Timestamp constructor maps rows in an event table to rows in the event log table as follows. For all $1 \leq i \leq n ,$ for all s ∈ Inst(R), an instance f Inst R<sup>s</sup> ( ( )) exists such that:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- $f_i^s$ (caseid) = s(Y) where Y ∈ Schema(R) such that Mapping$_R$ (Y) = caseid,
- $f_i^s$ (activity) = s(X) if Mapping$_R$ (X) = activity,
- $f_i^s$ (timestamp) = X$_i$,
- $f_i^s$ (transition) = l$_i$, and
- $f_i^s$ (Y) = s(Y) if Y ∈ Schema(R) and Mapping$_R$ (Y) = eventdata.
</div>

No other instances of this form are in Inst $\left( \mathcal { T } ( R ) \right)$

Here we show how the metric-based concept of quality dimension assessment can be applied as the basis for the quality-informed as signment of event log attributes on a column level (as described in Section 3.4).

Let $Q = \{ q _ { 1 } , q _ { 2 } , q _ { 3 } , . . . q _ { n } \}$ be a set of quality dimensions. Let $\mathcal { A }$ be a universe of attribute names. Let T be a database table and C: Schema $( T ) \subset { \mathcal { A } }$ be the set of column names of table T. Let $m _ { q } ( c )$ $M \times C \to [ 0 . . . 1 ]$ be a function that computes the quality value for any q ∈ Q and $c \in C .$

Let ℒ be the event log table and L = Schema(ℒ) be the set of column names in the event log table, i.e. L = {caseid,activity, timestamp,transition,…}. For any $l \in L , S _ { l } \subseteq Q$ is the set of quality dimensions that impact on the suitability of assigning any column $c \in C$ to event log attribute l. Define lower : Q × L → [0…1) and upper : $Q \times L \to$ (0…1] as lower and upper bounds respectively of a range that determines acceptable values for $m _ { q } ( c )$ for which it is suitable to map column c to event log attribute l.

For each data column $c \in C ,$ , calculate $m _ { q } ( c )$ for each quality di mension $q \in Q .$ For each event log attribute set upper and lower bounds on each of the quality dimensions that inform the attribute. Then so long as lowe $\begin{array} { r } { r ( q , l ) \le m _ { q } ( c ) \le u p p e r { ( q , l ) } } \end{array}$ for all $q \in S _ { l } ,$ the mapping of database column c to event log attribute l can be made.

In summary, RDB2Log allows users to flexibly generate high-quality event logs from relational databases on the basis of a tailored data quality assessment.

## 4. Evaluation

## 4.1. Evaluation strategy

The DSR evaluation framework proposed by Sonnenberg and Vom Brocke [21] comprises four activities (EVAL1 to EVAL4). EVAL1 aims to justify the research problem. It also requires deriving design objectives from existing knowledge, which we have done in Sections 1 and 2. EVAL2 evaluates the artifact's design specification by discussing its features against competing artifacts as well as challenging its understandability and real-world fidelity with process mining experts from industry and academia (Section 4.2). EVAL3 strives for validated instantiations. Thus, RDB2Log has been implemented as a software prototype and applied to two data sets in a laboratory setting (Section 4.3). In accordance with Sonnenberg and Vom Brocke [21], we validate our approach regarding feasibility and suitability and can give a rough indication of its ease-of-use and robustness. EVAL4 requires validating the instantiation's applicability in naturalistic settings. Thus, we applied the prototype to real-world data of a medium-sized manufacturing company and evaluated the results as well as discussed them in collaboration with the company (Section 4.4).

While we have presented three quality dimensions and three metrics in detail in Section $^ { 3 , }$ our artifact comprises of 12 dimensions and 25 metrics which have all been included in this evaluation and implemented in the prototype.

## 4.2. Evaluation of design specification (EVAL2)

EVAL2 was carried out in an artificial and a naturalistic setting. For artificial evaluation, we conducted a feature comparison discussing its design against the DOs and competing artifacts. As competing artifacts, we selected artifacts ofering guidance on log generation. We acknowledge that this sample does not include all extant artifacts (as compared to Appendix B), but are confident that it covers the most important developments. See Table 3 for the analysis results.

While all artifacts cover typical steps of event log extraction, no approach provides a data quality assessment detailed enough to gen erate insights into the applicability of the data for process mining. Although approaches in Refs. [17, 18] have been designed recently, they either are not concept-independent or source-independent or do not provide logs in standard formats. Existing approaches do not focus on applicability for laymen. Therefore, in our opinion, no other approach addresses the design objectives as comprehensively as RDB2Log.

As a naturalistic validation of RDB2Log, we presented the design to process mining experts and gathered their feedback in a survey. This activity helps validate the understandability and real-world fidelity of the designed artifact [21]. Parts of the survey address EVAL4 and will be presented in Section 4.4.

As a pretest for this survey, semi-structured interviews were conducted with four BPM researchers. They all have experience with extracting process logs or other data sets from source data, cleaning the data and deriving insights into business processes. We also conducted interviews with employees of four companies which use process mining on a daily basis. All practitioners have experience with manually extracting process logs from information systems. The survey was subsequently refined and distributed to researchers and practitioners working with process mining on a regular basis. We gathered 28 utilisable responses to this survey, containing 15 responses by researchers and 13 by practitioners. Typical researcher positions include doctoral candidates, post-docs or professors, while typical professional roles are consultants or business intelligence analysts. Because of a tight survey distribution circle including only people with high reputation in their respective fields, we can consider their responses valuable and trust worthy. The majority of respondents have one to five years of experience with data analysis in general or process mining in particular, with the mean at more than two years but less than five years. The mean respondent has extracted as well as analysed two to five event logs, a majority (over 80% of respondents) use relational SQL databases as source data and have experience with tools such as Disco. Interestingly, 15 respondents declared that their current data preparation processe

Feature comparison. Table 3

<table><tr><td colspan="5">Feature comparison.</td></tr><tr><td>Artifact</td><td>DO 1</td><td>DO 2</td><td>DO 3</td><td>DO 4</td></tr><tr><td>Günther and van der Aalst [15]</td><td>Presents a basic log extraction toolbox supporting a multitude of source systems.</td><td>Only considers data anonymisation issues in the log extraction phase.</td><td>Can extract events via a data-centric perspective. Uses the outdated MXML format.</td><td>Manual mapping of data attributes to event log attributes is necessary.</td></tr><tr><td>Verbeek et al. [16]</td><td>Presents a basic log extraction toolbox for ProM.</td><td>Does not consider data quality issues in the log extraction phase.</td><td>Can extract events via a data-centric perspective.</td><td>Manual mapping of data attributes to event log attributes is necessary.</td></tr><tr><td>van der Aalst [8]</td><td>Presents an approach to map redo logs to event logs based on the concept of events leaving “footprints by changing the underlying database”.</td><td>Does not consider data quality issues in the log extraction phase.</td><td>Object-centric perspective: Only changes to the database are considered as events. Static database content is ignored.</td><td>In-depth knowledge of complex database structures is required.</td></tr><tr><td>Calvanese et al. [18]</td><td>Provides an ontology-based mapping from database to event log based on OBDA (ontology-based data access).</td><td>Does not consider data quality issues in the log extraction phase.</td><td>Allows for multiple representational concepts such as database content (data-centric) and database changes (object-centric).</td><td>Queries for extraction are generated automatically from the ontology-based mapping.</td></tr><tr><td>Li et al. [17]</td><td>Presents XOC (eXtensible Object-Centric) event logs, an extension to XES which caters for object-centric data.</td><td>Does not consider data quality issues in the log extraction phase.</td><td>Only changes to the database are considered as events. Static database content is ignored. XOC is used instead of XES.</td><td>In-depth knowledge of complex database structures is required.</td></tr><tr><td>RDB2Log</td><td>Supports the extraction of logs from relational databases. Provides decision support based on data quality information generated by metrics-based source data analysis. Outputs an XES-formatted log file.</td><td>Data quality information is generated before extracting the log. Data quality information is weighted depending on the user&#x27;s choice of event log attribute.</td><td>RDB2Log is able to extract events from a multitude of different representational concepts existing in relational databases. As output, the standard XES format is used.</td><td>RDB2Log is designed to lead the user through simple steps and requires little to no prior knowledge of process mining concepts. Automation is suggested where possible.</td></tr></table>

include only manual or no data quality checks at all.

The respondents were first shown a video explaining RDB2Log in detail<sup>3</sup>. Subsequently, participants had to assess a set of 11 statements regarding the understandability (S1–5) and real-world fidelity (S6–11) of RDB2Log on a Likert scale with values between 1: “strongly disagree” and 7: “strongly agree”. We outline the mean and standard deviations of the experts' assessments of the evaluation criteria mentioned above in Table 4.

The mean respondent agrees that RDB2Log is understandable, with a strong focus on the log extraction component. However, the respondents only somewhat agree to the understandability of the compilation of data quality dimensions. The same holds for S6–11: The mean respondent agrees or strongly agrees to the real-world fidelity of RDB2Log's components. Only the feasibility of data quality approximation via metrics is seen somewhat more sceptically. We link this to our discussion on the availability of domain knowledge and its impact on the explanatory power of data quality metrics. In summary, however, the respondents support the design of our artifact. In addition, Wilcoxon Signed-Rank tests show that the samples for all questions difer significantly (p < 0.05) from the neutral response (Likert value of 4).

Table 5 shows a full summary of optional qualitative statements made by the experts in answering open-ended questions. Statements with similar or identical content have been merged. The numbers in parentheses behind the statements denote their frequency of occurrence and determine the ordering in the table.

Topics for future work were also extracted from the interviews and the survey. For example, the interviewees suggested focusing on developing a more complete set of event constructors, on the one hand, and developing a more sophisticated framework for incorporating domain knowledge, on the other. Most practitioners suggested expanding the design to support input from data sources such as change logs and to integrate more decision support and automation.

We agree with the feedback expressed by the interviewees and conclude with confidence that the design of RDB2Log is valid and fills a gap in literature.

## 4.3. Prototype evaluation (EVAL3)

We have implemented an instantiation of RDB2Log, available publicly<sup>4</sup>, as a software prototype and evaluate it by applying it in artificial and naturalistic settings. Its user interface (Fig. 3) is implemented in Java to ensure portability while the backend is based on the DBMS provided by Microsoft SQL Server. In a first computational step, the selected data quality metrics are applied to the database and their results are aggregated to generate an evaluation of the selected quality dimensions for each of the data columns. The metric implementations have been extensively tested by comparing computational results with manually computed metrics to allow for robust and reproducible results. When clicking on a dimension score, a detail window opens and lists all data entries that have been identified as issues by the metrics in this dimension. For example, the detail window for uniqueness lists identified non-unique entries for the user to investigate further<sup>5</sup>. Future work will include a white-listing option.

We validate our artifact in terms of feasibility (proof of concept) and suitability by applying the prototype in a laboratory setting to two realworld data sets extracted from two diferent application domains. The first data set (MIMIC<sup>6</sup>) is an openly available data set comprising desensitised health data associated with \~40,000 critical care patients. It includes demographics, vital signs, laboratory tests, medications, and

Table 4  
Mean/SD of answers reg. understandability and real-world fidelity.

<table><tr><td>ID</td><td>Statement</td><td>Mean</td><td>SD</td></tr><tr><td>S1</td><td>RDB2Log is presented in an understandable way.</td><td>5.62</td><td>0.85</td></tr><tr><td>S2</td><td>The individual data quality dimensions are understandable and their compilation is comprehensible.</td><td>5.46</td><td>0.88</td></tr><tr><td>S3</td><td>The separation into metrics with/without domain knowledge is understandable.</td><td>5.92</td><td>0.95</td></tr><tr><td>S4</td><td>The approach to extracting events from a relational database is understandable.</td><td>6.24</td><td>0.88</td></tr><tr><td>S5</td><td>The decision support based on the data quality of the individual data attributes is understandable.</td><td>6.04</td><td>0.84</td></tr><tr><td>S6</td><td>RDB2Log solves a real problem that process analysts are currently confronted with.</td><td>6.08</td><td>0.98</td></tr><tr><td>S7</td><td>RDB2Log is transferable to other use cases (e.g. other data sets, other IT systems).</td><td>6.35</td><td>0.98</td></tr><tr><td>S8</td><td>The individual dimensions are relevant in the field of process data.</td><td>5.71</td><td>0.91</td></tr><tr><td>S9</td><td>The evaluation of data quality on the basis of metrics is sensible.</td><td>5.92</td><td>1.00</td></tr><tr><td>S10</td><td>The data quality of a data set can be easily approximated by calculating metrics.</td><td>4.72</td><td>1.14</td></tr><tr><td>S11</td><td>It is realistic to assume that different event roles (e.g. case ID, timestamp) have different data quality requirements.</td><td>6.52</td><td>0.71</td></tr></table>

<table><tr><td>Positive</td><td>Negative</td></tr><tr><td>• Available tools turn a blind eye to data quality issues in the source data (3)</td><td>• Domain knowledge might be unavailable (4)</td></tr><tr><td>• Concept of event constructors is elegant (3)</td><td>• Many more event constructors possible and necessary (4)</td></tr><tr><td>• RDB2Log is well-structured and novel (1)</td><td>• Not feasible to only extract high-quality logs due to bad data quality (3)</td></tr><tr><td>• Ex-ante data quality assessment is more efficient than ex-post assessment (1)</td><td>• Generality of the designed artifact is sometimes not helpful compared to tools designed for a specific source system (1)</td></tr></table>

![](/api/attachments/J4QQ7WGE/fulltext/images/3d148b8eb1f78725d037b1ed68fca5da5d2a39eb1255d2f4cbf2302c890d15be.jpg)  
Fig. 3. Example screenshot of the event log attribute selection.

more. A more detailed description can be found in Ref. [42] while an analysis of the data set's quality can be found in Ref. [12]. The second data set is in the domain of Compulsory Third Party (CTP) insurance. The Motor Accident Insurance Commission, established by the Queensland (Australia) State Government, manages the CTP scheme covering liability to drivers who are deemed to have been responsible for causing personal injury to other persons involved in a road trafic crash. The test data sets difer heavily not only in their domain, but also in the characteristics of their data schema: While the MIMIC data set contains 26 tables connected via multiple relationships, the (de-identified) CTP data consists of only five tables that have been merged from various sources. Timestamps in the MIMIC data have been randomly ofset into the future to anonymise the healthcare records. ID attributes in the CTP tables cannot be fully matched because of their difering source files.

Applying the prototype yielded favorable results with both data sets.

Table 6  
Mean/SD of answers reg. ease-of-use and usefulness.

<table><tr><td>ID</td><td>Statement</td><td>Mean</td><td>SD</td></tr><tr><td>S12</td><td>The prototype is easy and intuitive to use.</td><td>5.88</td><td>0.85</td></tr><tr><td>S13</td><td>A user with a basic understanding of Process Mining is able to use this tool.</td><td>5.17</td><td>1.13</td></tr><tr><td>S14</td><td>The prototype represents a typical working step of a process mining user (i.e. extract data from IT systems).</td><td>6.21</td><td>1.02</td></tr><tr><td>S15</td><td>In my opinion, this typical working step of a process mining user (i.e. extract data from IT systems) is important.</td><td>6.46</td><td>0.59</td></tr></table>

The described data quality problems in both data sets were identified by the prototype, with MIMIC attributes often being assigned a low currency value and some CTP IDs listed as incomplete. Project researchers were able to construct several diferent (XES format) event logs, from diferent case perspectives (by selecting diferent Unique-Foreign key trees) that were ready to be used for process analysis. All logs could be imported to standard process mining tools (e.g. ProM, Disco) without errors. Either (i), the logs did not display the detected quality issues as users were able to deselect attributes with low data quality in the attribute selection process, or, (ii) the users included attributes with low data quality while being aware of, and therefore able to react to detected quality issues, e.g. by challenging the resulting process mining outputs.

We conclude from this that the operationalisation of RDB2Log's design specification as a software prototype is feasible and that it is suitable for application in the problem domain. Participating researchers were able to use the tool themselves and can subjectively state that the prototype is easy to use. The use of two diferent data sets also allows us to give a rough indication of the RDB2Log's robustness to diferent inputs.

## 4.4. Evaluation of applicability (EVAL4)

To demonstrate RDB2Log in a laboratory and in practice, and to evaluate its applicability and usefulness in a real-world setting, we undertook two separate evaluation activities: (i) we conducted a case study with real data from a German electronics manufacturing services company to demonstrate applicability of our artifact, and (ii) we showed a screencast of our prototype to the EVAL2 survey participant and asked questions about its usefulness and ease-of-use.

The German manufacturer specialises in engineering, testing, and final assembly of complete devices as well as modules and has approximately 1000 employees. For our research purpose, we were granted access to a relational data set in the form of a MySQL DDL script. The data records contain process data from the factory floors that is distributed in more than 100 tables and describes manufacturing processes. After adding some missing foreign key relationships manu ally and migrating the data to SQL Server, the RDB2Log prototype was able to access the data set. Using RDB2Log and Disco, we conducted a simple end-to-end process discovery together with the process stakeholders within the company. The prototype was able to assess the quality of the data set and extract selected events automatically. As output, we obtained several XES event logs that could be imported into process mining tools. The findings and experiences of the case study were then discussed in an extensive workshop. To cover both the technical and the business perspective, the workshop was attended by the head of production engineering, an internal software enginee covering data engineering and data analytics topics, and a process analytics consultant who had already manually extracted an event log from the same data source. In their opinion, the prototype is particularly useful for a first contact with the data. Since it displays data quality metrics for all available database columns, users can quickly assess whether it makes sense to generate an event log from the data. This was highly appreciated by the company's internal process analysts who confirmed having to answer this exact question often. The process analytics consultant confirmed the meaningfulness of the discovered process models, and also highlighted the tool's usefulness in extracting the logs and the time saved, compared to their manual extraction. The feedback has shown that the quality metrics provide helpful insights into the data. In summary, the participants of the workshop confirmed the applicability and usefulness of our prototype as well as the meaningfulness of the process models discovered.

Secondly, we presented a screencast demonstrating the prototype in action to our survey participants and asked them to assess four statements (S12–S15) on the usefulness and ease-of-use of our prototype (Table 6). The survey participants agreed that the prototype is intuitive to use and that it generally helps process mining users in their daily business. S13 was rated among the statements with the highest standard deviations. This indicates that, when further developing the prototype, greater attention should be paid to comprehensibility for users having only a basic technical understanding of process mining, although some participants have already assessed this statement quite positively.

In open-ended survey questions, respondents contributed suggestions for enhancements to the prototype: (i) adding tooltips, legends and other documentation to make it self-explanatory, (ii) making the event log extraction repeatable by allowing for SQL code export, and (iii) adding more data quality metrics.

In summary, the real-world evaluation confirmed that RDB2Log is applicable in real-world settings and can be a useful tool for extracting high-quality event logs from relational data. Since survey participants have only had access to the prototype via video, their assessment of the ease-of-use – however positive it is – needs to be treated with caution. Additionally, the applicability of RDB2Log in assessing quality dimensions such as accuracy depends, of course, on the underlying case. In the case study, we were able to assess accuracy based on several domain knowledge inputs (e.g., distribution of values, typical value ranges, exemplary measurements for value ambiguity). While our prototype implements a systematic way to compute a measurement for accuracy based on the available domain knowledge, a further examination based on diferent cases should be considered. Nevertheless, after conducting EVAL 1–4, we are confident that RDB2Log adequately supports users in assessing data quality, mapping relational data attributes to log attributes, and extracting a usable event log. Thus, it helps close the gap between distributed relational databases and high-quality event logs which has been identified in Section 1.

## 5. Conclusion

## 5.1. Summary and contribution

This paper proposes RDB2Log, an approach towards semi-automatically generating quality-informed event logs from relational data. RDB2Log requires as input a relational data set and supports the user in selecting event log attributes from the available data columns by providing information on data quality and data constraints. As output, an XES event log is provided.

We have validated RDB2Log by providing evidence of the research gap and of its novel functionality. In a second step, we have shown that its design specification addresses the design objectives derived from the literature. We have discussed the design specification with experts from academia and practice to show its understandability and real-world fidelity. Finally, we have presented an instantiation as a software pro totype and tested its functionalities on real-world data in artificial and naturalistic settings to provide proof of concept and demonstrate its applicability and usefulness. We conclude that RDB2Log advances a long-neglected data quality perspective to the extraction of event logs. The implementation provides users with an integrated log generation tool replacing the laborious, time-consuming, and error-prone manual process.

## 5.2. Limitations and future research

We have identified, from research and the evaluation, several areas where RDB2Log can be extended. First of all, we currently use a subset of possible data quality dimensions and corresponding metrics. More precisely, we only use quantifiable quality dimensions and metrics which can only be applied to singular data columns. As RDB2Log is modular, we encourage the addition of new data quality information to provide users with broader and deeper insights into the quality of the underlying data. Secondly, our current event constructors implement the most obvious types of event representations in relational data and we limit RDB2Log to exploiting only one level of key relationships in constructing events. Event constructors should be added for events that may be extracted by following more complex relationships in the source data. Such an extension would, for example, allow for the identification of whole sub-processes. Additionally, case or event attributes may be extracted from lookup tables (other parent tables referenced in a child table). Further, more complex events should be extractable (e.g. where event attributes occur in diferent tables). Furthermore, a reference process for quality-informed event log extraction from source data might be a valuable contribution for researchers and practitioners.

It is worth noting that assessing quality dimensions such as accu racy, with its requirement of comparing stored values with a value considered to be the corresponding real-world value, presents challenges not only for RDB2Log, but for all applications attempting to assess data quality or accuracy in particular. Real-world values may not be available, or, if available, be prohibitively costly or time-consuming to obtain. For this reason, RDB2Log provides a set of metrics for the accuracy dimension (outlier detection, pre-defined range of values, value ambiguity, and distance to real-world value). The metrics require varying degrees of domain knowledge, with one metric (outlier detection) requiring no domain knowledge, thus being assessable in all cases. Each metric is calculated depending on availability of input data and values aggregated to score the accuracy dimension. Taken together, the metrics will provide an assessment of the accuracy dimension whose quality will depend on the availability of domain knowledge. Our evaluation of the applicability of RDB2Log (Section 4.4) is, of course, influenced by the characteristics of the underlying case and, specifi cally, the availability of domain knowledge for measuring accuracy. More and diferent cases could therefore strengthen our argument of applicability.

Lastly, we plan on extending our work to include tracking and repairing of quality issues detected in the log, i.e. to deal with process data provenance. The goal of research in event log data quality should be an integrated toolchain covering the event log lifecycle end-to-end, including log extraction (RDB2Log), log analysis and repair (using interactive log forensics), and log data provenance (based on XES extensions saving data quality information directly in the log).

## CRediT authorship contribution statement

R. Andrews: Conceptualization, Methodology, Software, Data curation, Investigation, Writing - original draft. C.G.J. van Dun: Conceptualization, Methodology, Software, Data curation, Investigation, Writing - original draft. M.T. Wynn: Conceptualization, Methodology, Writing - review & editing. W. Kratsch: Conceptualization, Methodology, Investigation, Writing - original draft. M.K.E. Röglinger: Conceptualization, Methodology, Writing - review & editing. A.H.M. ter Hofstede: Conceptualization, Methodology, Writing - review & editing.

## Acknowledgments

Much of the work in this paper was supported through an Australian Research Council Discovery Grant DP150103356. We would like to thank Queensland's Motor Accident Insurance Commission for allowing us access to the CTP insurance data set.

## Appendix A. Clustered data quality dimensions from literature

List of dimension clusters (bold: included in the artifact) based on a literature review in the databases AISeL, EBSCOhost, JSTOR, ScienceDirect, Scopus, and Web of Science following established guidelines, sorted on the number of articles that mention the respective dimension cluster (N). Title search string: “(Assess\* OR Evaluat\* OR Criteri\* OR Dimension\* OR Measur\*) AND (“Data Ouality" OR “Log Ouality" OR “Information Ouality")”

<table><tr><td>ID</td><td>N</td><td>Representative name</td><td>Clusters</td></tr><tr><td>1</td><td>52</td><td>Currency</td><td>Age, timeliness</td></tr><tr><td>2</td><td>48</td><td>Accuracy</td><td>Correctness, validity</td></tr><tr><td>3</td><td>44</td><td>Consistency</td><td>Null value repres., comparability, format</td></tr><tr><td>4</td><td>44</td><td>Believability</td><td>Credibility, reputation</td></tr><tr><td>5</td><td>41</td><td>Reliability</td><td></td></tr><tr><td>6</td><td>40</td><td>Relevance</td><td>Appropriateness, importance, usefulness</td></tr><tr><td>7</td><td>40</td><td>Completeness</td><td></td></tr><tr><td>8</td><td>25</td><td>Availability</td><td>Responsiveness</td></tr><tr><td>9</td><td>25</td><td>Interpretability</td><td>Clarity, understandability, meaningfulness</td></tr><tr><td>10</td><td>20</td><td>Privacy</td><td>Anonymity, security</td></tr><tr><td>11</td><td>20</td><td>Objectivity</td><td>Freedom from bias</td></tr><tr><td>12</td><td>19</td><td>Sufficiency</td><td>Amount of data</td></tr><tr><td>13</td><td>17</td><td>Conciseness</td><td></td></tr><tr><td>14</td><td>12</td><td>Accessibility</td><td></td></tr><tr><td>15</td><td>11</td><td>Value-added</td><td></td></tr><tr><td>16</td><td>9</td><td>Volatility</td><td></td></tr><tr><td>17</td><td>6</td><td>Integrity</td><td></td></tr><tr><td>18</td><td>4</td><td>Precision</td><td>Level of detail, unambiguousness</td></tr><tr><td>19</td><td>4</td><td>Efficiency</td><td>Efficient use of memory</td></tr><tr><td>20</td><td>3</td><td>Flexibility</td><td>Portability</td></tr><tr><td>21</td><td>3</td><td>Informativeness</td><td>Disaggregation, variety</td></tr><tr><td>22</td><td>3</td><td>Uniqueness</td><td></td></tr><tr><td>23</td><td>1</td><td>Content</td><td></td></tr></table>

Appendix B. Existing approaches to event log extraction  
Existing publications incl. their prominent features. Type of research: A = Approach, D = Discussion, M = Meta model, R = Ref. Proc. Extraction concept: AC = Artifact-centric, OC = Object-centric, O = Ontology, T = Transactions Data source: ERP = Enterprise Resource Planning, Elogs = Event Logs, PAIS = Process-aware Information Systems, RDB = Relational Database, RLogs = Redo Logs, Trans = Transactions.

<table><tr><td>Type of research</td><td>Extraction concept</td><td>Data source</td><td>Publications</td></tr><tr><td>M</td><td>AC</td><td>ERP</td><td>Pajic and Becejski [43]</td></tr><tr><td>A</td><td>AC</td><td>RDB</td><td>Fahland et al. [44]</td></tr><tr><td></td><td></td><td></td><td>Nooijen et al. [13]</td></tr><tr><td></td><td></td><td></td><td>Popova et al. [45]</td></tr><tr><td>A</td><td>AC</td><td>ERP</td><td>Lu et al. [46]</td></tr><tr><td></td><td></td><td></td><td>Simovic et al. [47]</td></tr><tr><td>A</td><td>OC</td><td>RDB</td><td>van der Aalst et al. [48]</td></tr><tr><td></td><td></td><td></td><td>Li et al. [49]</td></tr><tr><td></td><td></td><td></td><td>Li et al. [17]</td></tr><tr><td>A</td><td>OC</td><td>Trans</td><td>Ingvaldsen and Gulla [50]</td></tr><tr><td>A</td><td>OC</td><td>ERP</td><td>Roest [51]</td></tr><tr><td>A</td><td>O</td><td>ELogs</td><td>Deokar and Tao [52]</td></tr><tr><td>A</td><td>O</td><td>RDB</td><td>Calvanese et al. [18]</td></tr><tr><td></td><td></td><td></td><td>Calvanese et al. [53]</td></tr><tr><td>D</td><td>T</td><td>RLogs</td><td>de Murillas et al. [54]</td></tr><tr><td>A</td><td>T</td><td>RLogs</td><td>de Murillas et al. [55]</td></tr><tr><td></td><td></td><td></td><td>van der Aalst [8]</td></tr><tr><td>R</td><td>-</td><td>RDB</td><td>Jans et al. [56]</td></tr><tr><td></td><td></td><td></td><td>Jans and Soffer [57]</td></tr><tr><td>M</td><td>-</td><td>RDB</td><td>de Murillas et al. [58]</td></tr><tr><td></td><td></td><td></td><td>de Murillas [59]</td></tr><tr><td>A</td><td>-</td><td>PAIS</td><td>Günther and van der Aalst [15]</td></tr><tr><td>A</td><td>-</td><td>ERP</td><td>Buijs [60]</td></tr><tr><td>A</td><td>-</td><td>EDI</td><td>Engel et al. [61]</td></tr><tr><td>A</td><td>-</td><td>RDB</td><td>Yano et al. [62]</td></tr><tr><td></td><td></td><td></td><td>Pérez-Castillo et al. [63]</td></tr><tr><td>A</td><td>-</td><td>ELogs</td><td>Mannhardt et al. [64]</td></tr></table>

## References

[1] W. van der Aalst, Process Mining: Data Science in Action, Springer, Berlin, Heidelberg, 2016.

[2] H. R’bigui, C. Cho, The state-of-the-art of business process mining challenges, International Journal of Business Process Integration and Management 8 (4) (2017 285-303.

[3] W. Kratsch, J. Manderscheid, D. Reißner, M. Röglinger, Data-driven process prioritization in process networks, Decision Support Systems 100 (2017) 27–40

[4] S. Suriadi, M.T. Wynn, J. Xu, W. van der Aalst, A.H.M. ter Hofstede, Discovering work prioritisation patterns from event logs, Decision Support Systems 100 (2017) 77-92.

[5] J. Evermann, J.-R. Rehse, P. Fettke, Predicting process behaviour using deep learning, Decision Support Systems 100 (2017) 129–140

[6] N. Martin, M. Swennen, B. Depaire, M. Jans, A. Caris, K. Vanhoof, Retrieving batch organisation of work insights from event logs, Decision Support Systems 100 (2017) 119-128.

[7] M.T. Wynn, E. Poppe, J. Xu, A.H.M. ter Hofstede, et al., ProcessProfiler3D: a visualisation framework for log-based process performance comparison, Decision Support Systems 100 (2017) 93–108

[8] W. van der Aalst, Extracting event data from databases to unleash process mining, BPM — Driving Innovation in a Digital World, Springer, Cham, 2015, pp. 105–128.

[9] S. Suriadi, R. Andrews, A.H.M. ter Hofstede, M.T. Wynn, Event log imperfection patterns for process mining: towards a systematic approach to cleaning event logs, Information Systems 64 (2017).132-150

[10] R. Bose, R. Mans, W. van der Aalst, Wanna improve process mining results? It‘s high time we consider data quality issues seriously, 2013 IEEE Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2013, pp. 127–134.

[11] F. Fox, V.R. Aggarwal, H. Whelton, O. Johnson, A data quality framework for process mining of electronic health record data, 2018 IEEE International Conference on Healthcare Informatics (ICHI), IEEE, 2018, pp. 12–21.

[12] A.P. Kurniati, E. Rojas, et al., The assessment of data quality issues for process mining in healthcare using MIMIC II. Health Informatics Journal 25 (4) (2018) 1878-1893.

[13] E. Nooijen, B. van Dongen, D. Fahland, Automatic discovery of data-centric and artifact-centric processes, International Conference on Business Process Management, Springer, 2012, pp. 316–327.

[14] P. Cabena, P. Hadjinian, R. Stadler, J. Verhees, A. Zanasi, Discovering Data Mining: From Concept to Implementation, Prentice-Hall, 1998

[15] C.W. Günther, W. van der Aalst, A generic import framework for process event logs, International Conference on Business Process Management, Springer, 2006, pp. 81-92.

[16] H.M.W. Verbeek, J.C. Buijs, B.F. Van Dongen, W.M. van der Aalst, XES, XESame, and ProM 6, International Conference on Advanced Information Systems Engineering, Springer, 2010, pp. 60–75.

[17] G. Li, E.G.L de Murillas, R.M de Carvalho, W. van der Aalst, Extracting objectcentric event logs to support process mining on databases, International Conference on Advanced Information Systems Engineering, Springer, 2018, pp. 182–199.

[18] D. Calvanese, M. Montali, A. Syamsiyah, W. van der Aalst, Ontology-driven ex traction of event logs from relational databases. International Conference or Business Process Management, Springer, 2016, pp. 140–153.

[19] K. Pefers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science research methodology for IS research, Journal of Management Information Systems 24 (3) (2007) 45–77.

[20] A.R. Heyner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–105.

[21] C. Sonnenberg, J. Vom Brocke, Evaluations in the science of the artificial — reconsidering the build-evaluate pattern in design science research, International Conference on Design Science Research in Information Systems, Springer, 2012, pp. 381-397.

[22] W. van der Aalst. et al.. Process mining manifesto. International Conference on Business Process Management. Springer. 2012, pp. 169–194.

[23] R.S. Mans, W. van der Aalst, R.J.B. Vanwersch, A.J. Moleman, Process mining in healthcare: data challenges when answering frequently posed questions, Process Support and Knowledge Representation in Health Care, Springer, 2012, pp. 140-153.

[24] R. Andrews, M.T. Wynn. K. Vallmuur, A.H.M. ter Hofstede. E. Bosley, M. Elcock. S. Rashford. Leveraging data quality to better prepare for process mining International Journal of Environmental Research and Public Health 16 (7) (2019 1138.

[25] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological foundations, Communications of the ACM 39 (11) (1996) 86–95.

[26] C. Batini, M. Scannapieco, Data and Information Quality: Dimensions, Principles and Techniques, Springer, 2016

[27] T.C. Redman, A. Blanton, Data Quality for the Information Age, Artech House,

1997.

[28] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4) (1996) 5–33.

[29] F. Mannhardt, S.A. Petersen, M.F. Oliveira, Privacy challenges for process mining in human-centered industrial environments. 14th International Conference or Intelligent Environments, IEEE, 2018, pp. 64–71.

[30] C. Fox, A. Levitin, T. Redman, The notion of data and its quality dimensions, Information Processing and Management 30 (1) (1994) 9–19.

[31] D. Loshin, Chapter 5 — data quality and MDM, in: D. Loshin (Ed.), Master Data Management, Morgan Kaufmann, Boston, 2009, pp. 87–103.

[32] C. Batini, C. Cappiello, C. Francalanci, A. Maurino, Methodologies for data qualit assessment and improvement, ACM Computing Surveys (CSUR) 41 (3) (2009) 1–52.

[33] L.L. Pipino, Y.W. Lee, R.Y. Wang, Data quality assessment, Communications of th ACM 45 (4) (2002) 211–218

[34] Q. Görz, M. Kaiser, An indicator function for insuficient data quality — a contribution to data accuracy, Mediterranean Conference on Information Systems, Springer, 2012, pp. 169–184

[35] B. Heinrich, M. Klier, A. Schiller, G. Wagner, Assessing data quality: a probabilitybased metric for semantic consistency. Decision Support Systems 110 (2018) 1–41.

[36] B. Heinrich, M. Klier, Metric-based data quality assessment: developing and eval uating a probability-based currency metric, Decision Support Systems 72 (2015) 82–96.

[37] M. Kaiser, M. Klier, B. Heinrich, How to measure data quality? A metric-based approach, International Conference on Information Systems 2007 Proceedings, Association for Information Systems, 2007, pp. 1–15.

[38] A. Even, G. Shankaranaravanan, Utility-driven assessment of data quality, ACM SIGMIS Database: Database for Advances in Information Systems 38 (2) (2007) 75–93.

[39] D.M. Strong, Y.W. Lee, R.Y. Wang, Data quality in context, Communications of the ACM 40 (5) (1997) 103–110

[40] D. Cohn, R. Hull, Business artifacts: a data-centric approach to modeling business operations & processes, IEEE Data Engineering Bulletin 32 (3) (2009) 3–9.

[41] P.M. Dixit, S. Suriadi, R. Andrews, M.T. Wynn, A.H.M. ter Hofstede, J.C. Buijs, W. van der Aalst, Detection and interactive repair of event ordering imperfection in process logs, International Conference on Advanced Information Systems Engineering, Springer, 2018, pp. 274–290.

[42] A.E. Johnson, D.J. Stone, L.A. Celi, T.J. Pollard. The MIMIC code repository. Journal of the American Medical Informatics Association 25 (1) (2018) 32–39

[43] A. Pajić, D. Bečejski, Metamodel of the artifact-centric approach to event log ex traction from ERP systems. International Journal of Decision Support Systems Technology 8 (2) (2016) 18–28.

[44] D. Fahland, M. De Leoni, B.F. Van Dongen, W. van der Aalst, Behavioral con formance of artifact-centric process models, International Conference on Business Information Systems, Springer, 2011, pp. 37–49.

[45] V. Popova, D. Fahland, M. Dumas, Artifact lifecycle discovery, International Journal Cooperative Information Systems 24 (2013) 1550001.

[46] X. Lu, M. Nagelkerke, D. van de Wiel, D. Fahland, Discovering interacting artifacts from ERP systems, IEEE Transactions on Services Computing 8 (6) (2015) 861–873.

[47] A. Simović, S. Babarogić, O. Pantelić, A domain-specific language for supporting log extraction from ERP systems, 7th International Conference on Computers Communications and Control (ICCCC). 2018, pp. 12–16.

[48] W. van der Aalst. A. Artale. M. Montali. S. Tritini. Obiect-centric behavioral con: straints: integrating data and declarative process modelling. Description Logics. 2017. pp. 1-12.

[49] G. Li, R. de Carvalho, W. van der Aalst, Automatic discovery of object-centric behavioral constraint models. International Conference on Business Information Systems, Springer, 2017, pp. 43–58

[50] J.E. Ingvaldsen, J.A. Gulla, Preprocessing support for large scale process mining of SAP transactions, International Conference on Business Process Management. Springer, 2008, pp. 30–41.

[51] A. Roest, A Practitioner's Guide for Process Mining on ERP Systems: The Case of SAP Order-to-Cash. Master's thesis TU Eindhoven, 2012.

[52] A.V. Deokar, J. Tao, Semantics-based event log aggregation for process mining and analytics, Information Systems Frontiers 17 (6) (2015) 1209–1226.

[53] D. Calvanese, T.E. Kalayci, M. Montali, S. Tinella, Ontology-based data access for extracting event logs from legacy data: the onprom tool and methodology, International Conference on Business Information Systems, Springer, 2017, pp. 220-236.

[54] E.G.L de Murillas, G.E. Hoogendoorn, H.A. Reijers, Redo log process mining in real life: data challenges & opportunities, International Conference on Business Process Management, Springer, 2018, pp. 573–587.

[55] E.G.L de Murillas, W. van der Aalst, H.A. Reijers, Process mining on databases: unearthing historical data from redo logs, International Conference on Business Process Management, Springer, 2015, pp. 367–385.

[56] M. Jans, P. Sofer, T. Jouck, Building a valuable event log for process mining: an experimental exploration of a guided process, Enterprise Information Systems 13 (5) (2019) 601–630.

[57] M. Jans, P. Sofer, From relational database to event log: decisions with quality impact, International Conference on Business Process Management, Springer, 2017, pp. 588–599.

[58] E.G.L. de Murillas, H.A. Reijers, W. van der Aalst, Connecting databases with pro cess mining: a meta model and toolset, Software and Systems Modeling (2018) 1–39.

[59] E.G.L de Murillas, Process Mining on Databases: Extracting Event Data from Rea Life Data Sources, Tech.Rep. 2019 TU/e.

[60] J.C.A.M. Buijs, Mapping Data Sources to XES in a Generic Way, Master's thesis Department of Mathematics and Computer Science, TU/e, 2010.

[61] R. Engel, W. van der Aalst, M. Zapletal, C. Pichler, H. Werthner, Mining inter-organizational business process models from EDI messages, International Conferenc on Advanced Information Systems Engineering, Springer, 2012, pp. 222–237.

[62] K. Yano, Y. Nomura, T. Kanai, A practical approach to automated business process discovery, 17th IEEE International Enterprise Distributed Object Computing Conference Workshops, IEEE, 2013, pp. 53–62.

[63] R. Pérez-Castillo, B. Weber, I.G.R. de Guzmán, M. Piattini, J. Pinggera, Assessing event correlation in non-process-aware information systems, Software and Systems Modeling 13 (3) (2014) 1117–1139.

[64] F. Mannhardt, M de Leoni, H.A. Reijers, W. van der Aalst, P.J. Toussaint, From low level events to activities — a pattern-based approach, International Conference on Business Process Management, Springer, 2016, pp. 125–141.

![](/api/attachments/J4QQ7WGE/fulltext/images/1e4a790e69aa452db44da0d0bb0d4ce78feef0d5806fadfe358e7791cce78f67.jpg)  
Dr. Robert Andrews is a Senior Lecturer in the BPM Group of the School of Information Systems, Queensland University of Technology. His research interests includ process mining, data mining and machine learning with a particular focus on data quality.

![](/api/attachments/J4QQ7WGE/fulltext/images/8ea27027319f870eef904c34a8adaa015dd66203c0930ee4145c8ea6267e8f5e.jpg)

Christopher van Dun studied Computer Science (B.Sc.) at the University of Erlangen-Nuremberg as well as Finance & Information Management (M.Sc. with Honours) at the Technical University Munich as well as the Universities of Augsburg and Bayreuth. Since Summer 2018, Christopher is a doctoral candidate with the Research Center Finance & Information Management (FIM) in the area of business process management (BPM). His focus lies on process mining.

![](/api/attachments/J4QQ7WGE/fulltext/images/d6d15cb3f5effeb314a0df5792d375096efac510e5093485f41a4cad70139e69.jpg)

Professor Moe T. Wynn leads the Business Process Management (BPM) group within the School of Information Systems at Queensland University of Technology. Her research interests include process mining, process automation, comparative process analytics and robotic process automation. She has published over 80 refereed research papers. Her work appeared in well-known journals in the field including Information Systems, Decision Support Systems, Information Sciences, Data and Knowledge Engineering, Information and Software Technology, Formal Aspects of Computing, Journal of Computer and System Sciences, and Transactions on Petri Nets and Other Models of Concurrency.

![](/api/attachments/J4QQ7WGE/fulltext/images/5587bd736b75ef59698d33e95e6a2071dfb17b09740587b1ca07162a8b1516f5.jpg)

![](/api/attachments/J4QQ7WGE/fulltext/images/62a29bf4613c75cb3b0ad68453af8fcf1699ab5358e32ec079d8f3f3f605cf6c.jpg)

Wolfgang Kratsch studied Information Systems (B.A.) as well as Computer Science and Information Management (M.Sc.) at the University of Augsburg. Since Summer 2015, Wolfgang is a doctoral candidate with the Research Center Finance & Information Management (FIM) in the area of business process management (BPM). His focus lies on datadriven process analytics.

Maximilian Roeglinger is a Professor of Information Systems at the University of Bayreuth. Maximilian serves as Deputy Academic Director of the Research Center Finance & Information Management (FIM), where he heads the business process management (BPM) group. Maximilian also works with the Project Group Business & Information Systems Engineering of the Fraunhofer FIT. Most of Maximilian's work centers around BPM, customer relationship management, and digital transformation.

![](/api/attachments/J4QQ7WGE/fulltext/images/549810d74c0c209acd9c96affe911a1ccd4af171afe71c4b48ae145831569eeb.jpg)

Arthur ter Hofstede is a Professor in, and Head of, the School of Information Systems in the Science and Engineering Faculty, Queensland University of Technology, Brisbane, Australia. His research interests are in the areas of business process automation and process mining.
