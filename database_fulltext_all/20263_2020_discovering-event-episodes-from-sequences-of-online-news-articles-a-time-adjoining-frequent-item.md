---
otero_id: 20263
otero_key: "9PHR7YS2"
title: "Discovering event episodes from sequences of online news articles: A time-adjoining frequent itemset-based clustering method"
authors: "Yen-Hsien Lee; Paul Jen-Hwa Hu; Hongquan Zhu; Hsin-Wei Chen"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103348"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Discovering event episodes from sequences of online news articles: A timeadjoining frequent itemset-based clustering method

![](/api/attachments/9PHR7YS2/fulltext/images/f381a0e7a185d0752de9ea108306d3f3b85aeef82f131cccc46b21bf44a7b7f1.jpg)

Yen-Hsien Lee<sup>a,</sup>\*, Paul Jen-Hwa Hu<sup>b</sup>, Hongquan Zhu<sup>c</sup>, Hsin-Wei Chen<sup>d</sup>

<sup>a</sup> Department of Management Information Systems, National Chiayi University, Taiwan

<sup>b</sup> Department of Operations and Information Systems, David Eccles School of Business, University of Utah, USA

<sup>c</sup> Department of Finance, School of Economics and Management, Southwest Jiaotong University, China

<sup>d</sup> AdvancedTEK International Corp., Taiwan

## A R T I C L E I N F O

Keywords: Event episode discovery Retrospective event detection Event evolution Temporal frequent itemset-based clustering

## A B S T R A C T

Firms perform environmental surveillance to identify important events and their developments. To alleviate the stringent information processing and analysis requirements, automated methods are needed to discover from online news articles distinct episodes (stages) of an important event. We propose a time-adjoining frequent itemset-based method that incorporates essential temporal characteristics of news articles for event episode discovery. With a corpus of 1468 news articles that pertain to 248 episodes of 53 diferent events, we empirically evaluate the proposed method and include several prevalent techniques as benchmarks. The results show that our method outperforms the benchmark techniques consistently and significantly, attaining the cluster recall, cluster precision, and F-measure values at 0.706, 0.593, and 0.584, respectively.

## 1. Introduction

Firms’ ability to identify and monitor essential changes in the environment and incorporate such information in strategy formulations, decision making, and business actions is crucial to their performance and competitiveness [1–4]. Many firms continuously surveil the busi ness environment to identify important events concerning customers, competitors, industry, technology, broad economic conditions, and government policies and regulations [5,6]. Because of the increasing prevalence of the Internet, online news articles represent a common and critical source for firms’ environmental surveillance [7–10]. As Haase and Franco [11] note, these voluminous news articles can be rapidly created, globally disseminated, conveniently accessed, and easily processed with increasing efectiveness and eficiency. Yet, the fastgrowing quantity of online news articles that pertain to various events now poses a fundamental challenge to firms that strive to stay abreast of the emerging events as they develop [12,13].

Event evolution patterns (EEPs) are central to firms' environmental surveillance and can support their market predictions, business deci sions, scenario analyses, and dialog system designs [12,14,15]. Firms seek to unfold EEPs that depict the general (overall) evolvement of a particular event type over time (e.g., merge and acquisition), so that they can be aware of and get prepared for monitoring such events in the near future [15,16]. In essence, EEPs produce high-level depictions of the evolution of diferent event types (categories), such as Initial Public Oferings warranting firms’ attention and surveillance [12,13,17], by discovering from sequences of news articles (or documents) a common evolution pattern for distinct events of the same type, together with their temporal relationships [12,14,18–20].

Typically, news stories reveal diferent episodes. Previous research has adopted diferent event structures or taxonomies. For example, [17,18] employ Story→Event→Topic; [21] adopt Story→Simple Event→Complex Event; [22] utilize Story→Component Event→Event; and [12] use Story→Episode→Event. These studies also use diferent concepts and terminologies. Specifically, “Topic” in [17,18] is identical to “Event” in [12,22] or “Complex Event” in [21], while “Event” refers to a distinct development stage of an event and is highly similar to “Simple Event” in [21], “Component Event” in [22], or “Episode” in [12].

In this study, we follow the Story→Episode→Event event structure [12]. As we illustrate in Fig. 1, one or more news stories describe a particular earthquake event, with each article denoting a distinct development stage or subevent of the focal event [12]. As shown, a common evolution pattern for earthquake events involves multiple episodes (development stages), such as epicenter and magnitude, casualties and damages, rescue actions, and rebuilding and restoration eforts. Supported by efective EEP discovery, firms can identify distinct stages of an emerging event, which they otherwise might overlook, and thereby can adapt better to the changing environment with agility and appropriate responses [23–26]. All else being equal, the common evolution pattern of a specific event type, if efectively identified and tracked, enables firms to anticipate and respond better to subsequent developments of diferent events of that type [27].

![](/api/attachments/9PHR7YS2/fulltext/images/da53b9f844ee116ee824a76b6406ba1e879797b8f2524cc78ad8dfc9202c9653.jpg)  
Fig. 1. Example of Relationships among Events, Event Episodes, and News Stories.

A critical precursor to EEP discovery is identifying distinct episodes of an event from a sequence of news articles (documents) that pertain to that event, by grouping the articles that describe each episode [12,17–19,28,29]. The enormous quantity of online news articles available on the Internet makes the traditional, manual approach to event episode discovery inefective, if feasible at all [30]. Previous EEP discovery research assumes the availability (existence) of diferent episodes of an event to be analyzed [21,22], then takes a conventional document clustering approach to discover episodes from a sequence of news articles pertinent to an event, without considering their temporal relationships [14,19,31–33], or extends existing document clustering techniques by considering characteristics specific to event-based documents [17,18]. For example, Nallapati, Feng, Peng, and Allan [17] incorporate temporal locality by applying a time-decaying function to adjust the similarity of two news articles. In general, news articles that describe a particular event often are temporally proximate; the greater the temporal diference between two articles, the lower their similarity.

Although empirical evidence indicates temporal diference-based clustering more efective for detecting events than traditional featurebased clustering [30], the use of a document-based time-decaying function may not be appropriate for event episode discovery, mainly because distinct episodes can have diferent temporal patterns. Typically, a time-decaying function tends to lower the similarity between news articles that are temporally distant and may not recognize persistent episodes of an event, which could vary in their time interval, such that the separation of diferent episodes becomes dificult. Also, distinct episodes of an event may be temporally adjacent or even overlap to some extent [30]. Even if the episodes are distinct, they remain interrelated and cannot be separated efectively by a linear time penalty function or an exponential time-decaying function. In addition, the features (terms) appearing in news articles describing the same event often share a considerable similarity, which often makes conventional feature-based document clustering less efective for grouping these articles according to feature similarity [30]. In either case then, the efectiveness of a document-based time-decaying function may be diminished.

This study addresses the limitations of conventional document based event episode discovery techniques by incorporating essential temporal characteristics of news articles about a focal event in featurelevel analyses. The rationale is that temporally proximate features (terms) should be more representative of the underlying episodes than temporally proximate news articles (documents). These temporally proximate features also should be more important than features that are farther apart temporally. We identify and select temporally proximate features and then use them to represent distinct episodes to be discovered, rather than relying on feature similarity for discovery. Some important temporal characteristics of features in distinct but related episodes of an event are incorporated in the proposed time-adjoining frequent itemset-based event-episode discovery (TAFIED) method. Overall, our method extends frequent itemset-based hierarchical clustering (FIHC) by incorporating temporal locality, according to the fit between a cluster and a document. Unlike typical FIHC that uses frequent items to group documents (features appearing frequently in news articles), our measure instead assesses the fit of documents within a cluster and estimates the temporal adjacency of diferent features intuitively. We target event episode discovery and seek to identify different subevents of a focal event to support EEP discovery.

The organization of the remaining paper is as follows. Section 2 provides an overview of retrospective event detection and event epi sode discovery, reviews representative studies of FIHC, and highlight the gaps that motivate our study. In Section 3, we elaborate the proposed method and its overall processing. We describe our data and evaluation design in Section 4, followed by data analyses and important results in Section 5. We conclude with a summary of the study and its contributions, together with several future research directions, in Section 6.

## 2. Literature review and motivation

Several streams of research closely relate to our study, including retrospective event detection and event episode discovery as well as FIHC. Herein, we review these streams of extant literature to indicate the gaps that we seek to address.

## 2.1. Retrospective event detection and event episode discovery

Previous research has examined retrospective event detection [34–38]. In general, retrospective event detection partitions or clusters a corpus of news articles into distinct topics or events; it shares several characteristics with event episode discovery but difers in both the unit and the granularity of analysis. Typical retrospective event detection techniques discover events from a stream of news articles; they target an event-based classification by clustering a sequence of chronologically ordered news articles, available in diferent sources or languages, to identify a set of coherent topics (events) inherent to the news articles [39,40].

Event episode discovery explicitly aims at discovering an event as it evolves through diferent development stages and identifying news articles that pertain to each stage. That is, retrospective event detection may reveal distinct events (e.g., Indian Ocean tsunami, the trade war between the United States and China, and Tesla going private) and find news articles associated with each event; event episode discovery instead seeks to identify the diferent development stages of these events over time and find news articles pertinent to each stage. Overall, event episode discovery identifies distinct episodes of an event from a sequence of news articles pertinent to that event, whereas retrospective event detection identifies events from a stream of articles by segmenting the diferent events described by these articles. As a result, event episode discovery tends to perform analyses at a finer-grained level than retrospective event detection.

Nallapati, Feng, Peng, and Allan [17] and Wei and Chang [12] attempt event episode discovery by applying a hierarchical agglomerative clustering (HAC) algorithm [41] to identify distinct episodes of an event from sequences of news articles. Nallapati, Feng, Peng, and Allan [17] describe an event structure as interconnected, threading subjects, and apply a Story→Event→Topic event taxonomy. To discern diferent episodes of an event, they leverage the temporal localization of news stories, using a time-decaying function to estimate the similarity between two news stories and applying a penalty to news story pairs that are temporally distant. Empirical results confirm that the use of a timedecaying function improves the efectiveness of an existing event episode discovery technique [17,30]. Wei and Chang [12] instead propose a Story→Episode→Event taxonomy, which emphasizes essential intraand intersequence episode relationships and aims to capture the event evolution by unfolding the temporal patterns of the respective episodes of an event. However, this taxonomy does not consider temporal localization of news stories, because the goal is to generalize episodes across diferent events and discover frequent event episodes in the underlying temporal relationships, that is, event evolution patterns.

## 2.2. Frequent itemset-based hierarchical clustering

FIHC leverages association rule mining by considering the documents as transactions and the features of a document as items [42]. In general, FIHC selects features (items) with a document frequency greater than the prespecified minimum $\left( g _ { f } \right)$ threshold and uses the identified frequent features (items) as cluster centroids to group documents. That ${ \mathrm { i } } s ,$ the identified frequent features serve as cluster labels; a document $d _ { j }$ is initially assigned a set of candidate clusters, on the basis of its own frequent items, so that the most appropriate cluster for the document can be determined according to the goodness of fit that in dicates the score of retaining document d in the cluster $c _ { x } .$ . The score can be calculated as

$$
\begin{array}{c} S c o r e (c _ {x} \longleftarrow d _ {j}) = [ \sum_ {i} (n (t _ {i}) \times C l u s t e r \_ S u p p o r t (t _ {i})) ] \\ - [ \sum_ {i} (n (t _ {i} ^ {\prime}) \times G l o b a l \_ S u p p o r t (t _ {i} ^ {\prime})) ] \end{array}\tag{1}
$$

where t represents a global frequent item in document $d _ { j }$ and is also a frequent item in cluster $c _ { x } , t _ { i } ^ { \prime }$ denotes a global frequent item in $d _ { j }$ but not a frequent item in $c _ { x } , n ( t _ { i } )$ indicates the weight of t in $d _ { j } ,$ , n(t ’) is the weight of $t _ { i } ^ { \phantom { \dagger } }$ in $d _ { j } ,$ Cluster\_Support(t ) reveals the percentage of the documents in $c _ { x }$ that contain $t _ { i } ,$ and Global\_Support(t ’) depicts the per centage of the entire documents that contain $t _ { i } ^ { \prime } .$

Next, FIHC retains each document in the cluster with the highest goodness-of-fit score, such that each document belongs to one and only one cluster, and empty clusters get removed. To avoid the possibility that documents describe the same topic (event) but get assigned to multiple clusters, FIHC uses an intercluster similarity measure and collapses any cluster whose similarity exceeds the prespecified threshold. Furthermore, FIHC can generate a natural topic hierarchy, with increasing ease of browsing and cluster accuracy. For example, it may measure intercluster similarity by assessing the viability of merging cluster $c _ { y }$ with $c _ { x }$ by aggregating all the documents in $c _ { y }$ into a document, then consolidating the goodness of fit of the merging cluster $c _ { x }$ with $c _ { y }$ by aggregating all the documents in $c _ { x }$ into a document, calculated by Eq. (2). The score for merging cluster $c _ { y }$ with $c _ { x }$ then would be defined as in Eq. (3).

$$
\text { Inter\_Sim } (c _ {x} \leftrightarrow c _ {y}) = \sqrt {\text { Sim } (c _ {x} \longleftarrow c _ {y}) \times \text { Sim } (c _ {y} \longleftarrow c _ {x})}\tag{2}
$$

and

$$
S i m (c _ {x} \longleftarrow c _ {y}) = \frac {S c o r e (c _ {x} \longleftarrow d o c (c _ {y}))}{\sum n (t _ {i}) + \sum n (t _ {i} ^ {\prime})} + 1\tag{3}
$$

where $c _ { x }$ and $c _ { y }$ represent two clusters, doc(c ) is the aggregation of all the documents in cluster $c _ { y } ,$ t denotes a global frequent item in $d o c ( c _ { y } )$ and a frequent item in cluster $c _ { x } , t _ { i } ^ { \prime }$ indicates a global frequent item in doc $( c _ { y } )$ but not a frequent item in $c _ { x } , n ( t _ { i } )$ is the weight of $t _ { i }$ in $d o c ( c _ { y } ) ,$ and n(t<sub>i</sub>') is the weight of $t _ { i } ^ { \prime }$ in doc(c<sub>y</sub>).

## 2.3. Gap analysis and motivation

Retrospective event detection identifies diferent events that exist in a sequence of news articles and then groups them accordingly. Diferent news events might not be temporally adjacent and could vary sub stantially in content. In contrast, event episode discovery unfolds distinct (development) stages of a focal event from the related news articles. News articles that pertain to the focal event might have similar content, themes (main storyline), and wording. Retrospective event detection applies to the entire corpus of documents, whereas event episode discovery groups only those news articles specific to an episode of the focal event. As a result, existing retrospective event detection techniques may not be efective for event episode discovery.

Most existing event episode discovery techniques adopt a conventional document clustering approach and address the temporal locality of news articles by using a time-decaying function to adjust the probability that diferent news stories belong to the same episode. News articles pertinent to an event episode in principle should be temporally adjacent; yet, existing techniques overlook the likelihood that distinct episodes may develop concurrently, such as when multiple distinct episodes occur within a time period, with some degree of overlap among them.

To be efective, event episode discovery should properly consider two issues: news articles describing diferent episodes of a particular event have similar content, and diferent episodes could emerge concurrently within a time window. Existing techniques for event episode discovery or retrospective event detection may not identify event episodes from sequences of news articles efectively, even with the inclusion of a document-based time-decaying function. Event episode discovery instead should proceed at the feature level, rather than the document level, to analyze whether diferent news articles pertain to the same episode. Although articles about an event may have similar descriptions and wordings, they tend to vary in focus (main storyline) and have specific features (terms) that difer from those frequently appearing in the related news articles. For example, regarding a particular earthquake event, an initial episode may focus on the date and time, location, and magnitude of the quake; subsequent episodes could relate to casualties and damages, rescue operations, logistic support and survivor placement, and rebuilding and restoration eforts. Although these news articles would have similar content, their focus (theme) difers noticeably. We thus propose a novel time-adjoining frequent itemset-based method for event episode discovery, as we elaborate about this proposal in the next section.

## 3. Proposed method

The proposed TAFIED method extends FIHC, in an attempt to increase its ability to cope with the burst characteristic of features for event episode discovery. Our method can address the limitations of document-based time-decaying functions that often constrain existing document clustering techniques by considering several essential characteristics of online news articles: burst, new terms and develop ments, and the temporal adjacency of features. TAFIED groups news articles (documents) by using frequent items as cluster centroids; it addresses the temporal adjacency of documents in a cluster to ensure goodness of fit between a cluster and a document by properly weighing the adjacency of the respective time stamps of diferent news articles that belong to the same cluster (event episode). Thus, TAFIED can create clusters in which documents are temporally adjacent and share features that frequently appear in a stream of news articles. As we depict in Fig. 2, the input for the proposed method is a sequence of news articles about an event. which are used to discover a set of distinct episodes. The overall processing of our method consists of document preprocessing, cluster initialization, cluster distinction, and cluster adjust ment.

![](/api/attachments/9PHR7YS2/fulltext/images/3164ea512e20b47073ee1d0a439f5982f9e415cbf02a05b6bc628ee2cba8510b.jpg)  
Relevant Event Episodes  
Fig. 2. Proposed TAFIED Method.

In document preprocessing, TAFIED extracts meaningful terms (e.g., nouns, noun phrases, and verbs) from each news article, applies a rule based part-of-speech tagger to tag each word in the article [43], then uses a parser to select nouns, noun phrases, and verbs from the article. Stop words such as nonsemantic-bearing words get removed, and the remaining words are stemmed into their respective original forms.

For cluster initialization, TAFIED constructs a set of initial clusters and assigns each news article to candidate clusters according to its own frequent items. Frequent items (terms) are first identified from the entire corpus of news articles under analysis. Term t is a frequent item if the ratio between its document frequency (number of news articles with term t) and the total number of news articles exceeds the pre. specified minimum global support $g _ { t ^ { * } }$ . By viewing each frequent item as a class label, our method can create a set of initial clusters; each news article gets assigned to candidate clusters on the basis of its own frequent items (class labels). We may have as many clusters as the number of frequent items identified, and a news article can be labeled as a member of multiple clusters. For an illustration, assume that we have ten news articles, identified frequent items, with $g _ { t } = 0 . 4 ,$ and their respective term frequencies in each document, as shown in Table 1.

Table 1  
Example of Term Frequency of Frequent Items in Each Document.

<table><tr><td></td><td> $t_1$ </td><td> $t_2$ </td><td> $t_3$ </td><td> $t_4$ </td><td> $t_5$ </td></tr><tr><td> $d_1$ </td><td>3</td><td>-</td><td>2</td><td>-</td><td>-</td></tr><tr><td> $d_2$ </td><td>5</td><td>-</td><td>2</td><td>2</td><td>-</td></tr><tr><td> $d_3$ </td><td>7</td><td>-</td><td>-</td><td>3</td><td>4</td></tr><tr><td> $d_4$ </td><td>1</td><td>-</td><td>1</td><td>4</td><td>-</td></tr><tr><td> $d_5$ </td><td>2</td><td>-</td><td>-</td><td>5</td><td>-</td></tr><tr><td> $d_6$ </td><td>-</td><td>2</td><td>-</td><td>-</td><td>2</td></tr><tr><td> $d_7$ </td><td>-</td><td>3</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_8$ </td><td>-</td><td>1</td><td>16</td><td>-</td><td>2</td></tr><tr><td> $d_9$ </td><td>-</td><td>1</td><td>-</td><td>-</td><td>1</td></tr><tr><td> $d_{10}$ </td><td>2</td><td>-</td><td>12</td><td>-</td><td>-</td></tr></table>

The cluster initialization creates five initial clusters, with five identified frequent items $( t _ { 1 }$ to $t _ { 5 } )$ as cluster labels. Then a news document gets assigned repeatedly to the corresponding clusters, according to its own frequent items. For example, document $d _ { 1 }$ is assigned to clusters $c _ { t I }$ and $c _ { t 3 } ;$ document $d _ { 2 }$ is assigned to clusters $c _ { t l } , c _ { t 3 } ,$ and $c _ { t 4 } .$ As a result, we have a set of initial clusters with their respective member documents, as shown in Table 2.

After cluster initialization, each news document has been assigned to at least one candidate cluster. We assume that each news article pertains to one and only one event episode, so in cluster distinction, TAFIED assesses the fit between a document and each candidate cluster, selects the most appropriate cluster, and generates a final set of clusters. We develop a fitness function to measure the likelihood that a document $d _ { j }$ belongs to a cluster $c _ { x } .$ Because we consider the temporal characteristics of a sequence of news articles, any features (terms) of news articles that describe the same event episode in principle should exhibit essential temporal characteristics (burst, new terms and developments, and temporal proximity) and share more important features than others. That is, a news article describing a specific event episode should share features of high appearance frequency and temporal adjacency with articles about that same episode, compared with articles pertaining to another episode. Formally, the fitness function between a document $d _ { j }$ and a cluster $c _ { x }$ is as follows:

$$
\text { Fitness } (c _ {x} \longleftarrow d _ {j}) = \sum_ {i = 1} ^ {| T |} (\alpha \times C S (t _ {i}, c _ {x}) \times T F I D F (t _ {i}, d _ {j}) \times T P (c _ {x}))\tag{4}
$$

where T is a set of frequent items, t denotes a frequent item, $C S ( t _ { i } , c _ { x } )$ is the cluster support calculated as the percentage of documents in $c _ { x }$ that contain $t _ { i } ,$ α is a parameter to control the impact direction of $t _ { i } , T F I D F ( t _ { i } ,$ d ) represents the within-document term frequency × inverted document frequency for t appearing in $d _ { j } ,$ and $T P ( c _ { x } )$ is a temporal proximity (TP) function for measuring the temporal adjacency of documents when $d _ { j }$ is assigned to $c _ { x }$

For TAFIED, we employ the $\mathrm { T F } \times \mathrm { I D F }$ measure to evaluate the novelty of feature $t _ { i }$ in the entire corpus of news articles; lower document frequency should produce a higher $\mathrm { T F } \times \mathrm { I D F }$ value. Furthermore, the frequent item t is essential to cluster $c _ { x }$ if it appears frequently in many documents of $c _ { x } ,$ because a document that shares more important features with other documents in the same cluster should have a higher likelihood of belonging to that cluster. Inversely, the probability may decrease if a document shares fewer important features with the documents in ${ c _ { x } } ^ { 2 }$ We thus use a parameter (α) to control the efect direction of frequent item t ; specifically, α is set to -1 if the cluster support of $t _ { i } , \ C S ( t _ { i } , \ c _ { x } )$ , is lower than a prespecified significance threshold $s _ { t } \left( \mathrm { i . e . , } \right.$ , frequent item in $d _ { j }$ not satisfying the minimum cluster support of $c _ { x } ) _ { i }$ , or to 1 otherwise.

Table 2  
Example Initial Clusters and Their Respective Member Documents.

<table><tr><td>Initial Set of Clusters</td><td>Member Documents</td></tr><tr><td> $c_{t1}$ </td><td> $d_1, d_2, d_3, d_4, d_5, d_{10}$ </td></tr><tr><td> $c_{t2}$ </td><td> $d_6, d_7, d_8, d_9$ </td></tr><tr><td> $c_{t3}$ </td><td> $d_1, d_2, d_4, d_8, d_{10}$ </td></tr><tr><td> $c_{t4}$ </td><td> $d_2, d_3, d_4, d_5$ </td></tr><tr><td> $c_{t5}$ </td><td> $d_3, d_6, d_8, d_9$ </td></tr></table>

Previous event episode discovery research considers temporal characteristics of news articles (or documents) by incorporating a linea time-penalty function or a nonlinear time-decaying function in the content-similarity measure to adjust the similarity between pairs of articles and then employing the adjusted similarity to group articles with a traditional document clustering algorithm. The underlying assumption is that the probability of two news articles pertaining to the same event episode would become lower if they are temporally distant; i.e., a large time interval between their published time. In this study, we instead approach event episode discovery from a diferent perspective by considering important characteristics of news articles that belong to an event episode. Specifically, news documents pertaining to an event episode contain similar content and often are published in close tem poral adjacency (proximity). Unlike previous research that directly employs temporal distance to adjust interdocument similarity, we develop a TP function to measure the temporal adjacency of news articles in a cluster to determine the soundness of grouping them together; i.e., belonging to a specific event episode. The TP function, a criterion for our fitness measure, essentially considers that the articles in a cluster should be published in close temporal adjacency.

When assigning document $d _ { j }$ to a cluster, the fitness function con siders the temporal adjacency of the documents in cluster $c _ { x } .$ The fitness score decreases if assigning document $d _ { j }$ to a cluster $c _ { x }$ is likely to increase the temporal diference among documents in that cluster. We develop a TP function $T P ( c _ { x } )$ . defined as $\frac { e ^ { \lambda - \theta } } { 1 + e ^ { \lambda - \theta } }$ if $\vert c _ { x } \vert > 1$ and 0.5 otherwise, where $\lambda \ : = \ : ( | c _ { x } | \cdot 1 ) \times w ^ { 2 }$ is the theoretically maximal temporal diference allowed between two time-ordered documents in cluster $c _ { x } ,$ w is a parameter denoting the tolerant temporal diference of two time-ordered documents in $c _ { x } ,$ and $\begin{array} { r } { \theta \ = \ \sum _ { k = 1 } ^ { | c _ { x } | - 1 } | t ( d _ { k } ) - t ( d _ { k + 1 } ) | ^ { 2 } } \end{array}$ represents the sum of the squared actual temporal diference between two time-ordered documents in $c _ { x } ,$ with $t ( d _ { k } )$ being the time stamp of document $d _ { k }$ in cluster $c _ { x } .$ The value of $T P ( c _ { x } )$ ranges between 0 and 1. A smaller temporal diference between the documents in $c _ { x }$ implies that documents are in temporal adjacency (i.e., proximity), thus resulting in a higher value of $T P ( c _ { x } )$ . Furthermore, the value of $T P ( c _ { x } )$ gradually decreases as θ increases from 0 and decreases sharply as θ exceeds a threshold value. The proposed TP function can accommodate news articles pertinent to an event episode that are published in a later time period, so that the relevance between these news articles would not be unduly discounted by their temporal distance. Specifically, our TP function incorporates a parameter ( w) to account for the tolerance in temporal diference between two time-ordered documents within a cluster. Thus, two articles are considered as relevant (pertaining to an event episode) if they are published within the tolerant temporal dif ference. As we illustrate in Fig. 3, with a cluster of five documents and w set to $^ { 2 , }$ so tha $\lambda = 1 6$ , the variance of $T P ( c _ { x } )$ increases with $\theta ;$ the TP $( c _ { x } )$ value decreases gradually as $\theta$ increases from 0 to 12, then decreases sharply as θ increases further. The value of $T P ( c _ { x } )$ reaches 0.5 when $\theta = 1 6$ , such that $\theta = \lambda$

![](/api/attachments/9PHR7YS2/fulltext/images/0df08ce5f57979d8e05af9858ffc53f719bc1a0169efba2801f6f9b7450643d0.jpg)  
Fig. 3. Variance of Temporal Proximity Function.

To illustrate how we calculate the fitness score, we continue with the example of an initial set of clusters in Table 2. We set the significance threshold $s _ { t }$ to 0.3 and the tolerant time gap w to 2, then calculate the fitness score for document $d _ { 3 }$ to each of its candidate clusters as follows:

Fitness $\begin{array} { r } { ( c _ { t 1 } \longleftarrow d _ { 3 } ) = ( ( 1 \times \frac { 6 } { 6 } \times 7 \times \log _ { 2 } \frac { 1 0 } { 6 } ) + ( 1 \times \frac { 4 } { 6 } \times 3 \times \log _ { 2 } \frac { 1 0 } { 4 } ) + ( - 1 \times \frac { 1 } { 6 } \times 3 \times \log _ { 2 } \frac { 1 0 } { 6 } ) ) = 0 . } \end{array}$ $\begin{array} { r } { 4 \times \log _ { 2 } \frac { 1 0 } { 4 } ) ) \times \frac { e ^ { 2 0 - 2 9 } } { 1 + e ^ { 2 0 - 2 9 } } = 0 . 0 0 1 , } \end{array}$

where $\begin{array} { c c l } { \lambda _ { t 1 } } & { = } & { \left| 6 - 1 \right| \times 2 ^ { 2 } = 2 0 } \end{array}$ and $\begin{array} { c c l } { \theta _ { t l } } & { = } & { \left| 2 - 1 \right| ^ { 2 } + \left| 3 - 2 \right| ^ { 2 } + } \end{array}$ $| 4 - 3 | ^ { 2 } + | 5 - 4 | ^ { 2 } + | 1 0 - 5 | ^ { 2 } = 2 9 .$

$$
\begin{array}{r} F i t n e s s (c _ {t 4} \longleftarrow d _ {3}) = ((1 \times \frac {4}{4} \times 7 \times \log_ {2} \frac {1 0}{6}) + (1 \times \frac {4}{4} \times 3 \times \log_ {2} \frac {1 0}{4}) \\ + (- 1 \times \frac {1}{4} \times 4 \times \log_ {2} \frac {1 0}{4})) \times \frac {e ^ {1 2 - 3}}{1 + e ^ {1 2 - 3}} = 7. 8 0 2 \end{array}
$$

$$
\begin{array}{l} \text {where} \lambda_ {t 4} = | 4 - 1 | \times 2 ^ {2} = 1 2 \quad \text {and} \theta_ {t 4} = | 3 - 2 | ^ {2} + | 4 - 3 | ^ {2} + \\ | 5 - 4 | ^ {2} = 3. \end{array}
$$

$$
\begin{array}{c} \text {Fitness} (c _ {t 5} \longleftarrow d _ {3}) = ((- 1 \times \frac {1}{4} \times 7 \times \log_ {2} \frac {1 0}{6}) + (- 1 \times \frac {1}{4} \times 3 \times \log_ {2} \frac {1 0}{4}) \\ + (1 \times \frac {4}{4} \times 4 \times \log_ {2} \frac {1 0}{4})) \times \frac {e ^ {1 2 - 1 4}}{1 + e ^ {1 2 - 1 4}} = 0. 3 5 8, \end{array}
$$

where $\begin{array} { l l l } { { \lambda _ { t 5 } } } & { { = } } & { { \left| { 4 - 1 } \right| \times 2 ^ { 2 } = 1 2 } } \end{array}$ and $\begin{array} { r c l } { \theta _ { t S } } & { = } & { \left| 6 - 3 \right| ^ { 2 } + \left| 8 - 6 \right| ^ { 2 } + } \end{array}$ $| 9 - 8 | ^ { 2 } = 1 4 .$

The fitness scores of $d _ { 3 }$ with respect to candidate clusters $c _ { t 1 } , c _ { t 4 } ,$ and $c _ { t 5 }$ thus are 0.001, 7.802, and 0.358, respectively. Thus, document $d _ { 3 }$ remains in cluster $c _ { t 4 }$

The use of frequent items as the base to cluster articles could lead to news articles that describe the same event episode scattered across multiple clusters after cluster distinction. For example, an episode, like cluster $c _ { t 3 }$ in Table 3 mainly related to frequent items{t1, t3} and documents that primarily contain frequent items{t1, t3, t4} form another cluster $c _ { t 4 } .$ Intuitively, the documents in cluster $c _ { t 4 }$ are a subset of those in cluster $c _ { t 3 } .$ However, in this example, they are separated to form another cluster after cluster distinction. As a remedy, we assess the need to merge two clusters in the cluster adjustment step. To perform cluster adjustment, TAFIED merges the clusters that contain highly similar or relevant documents. A combined cohesion measure evaluates the appropriateness of merging two clusters, and the combined cohesion of two clusters $c _ { x }$ and $c _ { y }$ is calculated as follows:

$$
\begin{array}{l} \text { Combined - Cohesion } (c _ {x} \longleftarrow c _ {y}) \\ = \sqrt {\text { Cohesion } (c _ {x} \longleftarrow c _ {y}) \times \text { Cohesion } (c _ {y} \longleftarrow c _ {x})} \times T P (c _ {x} \leftrightarrow c _ {y}) \end{array}\tag{5}
$$

Therefore, TAFIED might merge two clusters if their combined cohesion score exceeds a specified merging threshold $\eta .$ To measure the cohesion of two clusters, the cluster to be merged $( \mathrm { e } . { \bf g } . , c _ { y } )$ serves as the document, for which the fitness with respect to the other cluster (e.g., $c _ { x } )$ can be calculated. The cohesion function extends the fitness function to assess the fit of a document and a cluster (in the cluster distinction phase), and it normalizes the output value to between 0 and 2, to avoid any negative values. Formally, the cohesion function is defined as:

Table 4  
Table 3  
Distinct Clusters and Respective Member Documents.

<table><tr><td>Distinct Set of Clusters</td><td>Member Documents</td></tr><tr><td> $c_{t2}$ </td><td> $d_6, d_7, d_9$ </td></tr><tr><td> $c_{t3}$ </td><td> $d_1, d_8, d_{10}$ </td></tr><tr><td> $c_{t4}$ </td><td> $d_2, d_3, d_4, d_5$ </td></tr></table>

$$
\text { Cohesion } (c _ {x} \longleftarrow c _ {y}) = \frac {\sum_ {i = 1} ^ {| F |} (\alpha \times C S (f _ {i} , c _ {x})) \times \sum_ {d _ {j} \in c _ {y}} T F I D F (f _ {i} , d _ {j})}{\sum_ {i = 1} ^ {| F |} \sum_ {d _ {j} \in c _ {y}} T F I D F (f _ {i} , d _ {j})} + 1\tag{6}
$$

where $c _ { x }$ and $c _ { y }$ are clusters to be considered for merging, $\textstyle \sum _ { d _ { j } \in c _ { y } } T F I D F ( f _ { i } , d _ { j } )$ is the sum of the $\mathrm { T F } \times \mathrm { I D F }$ values of $f _ { i }$ in each document $d _ { j }$ in cluster $c _ { y } ,$ and $\begin{array} { r } { \sum _ { i = 1 } ^ { | F | } \sum _ { d _ { j } \in c _ { y } } T F I D F ( f _ { i } , d _ { j } ) } \end{array}$ is the sum of the $\mathrm { T F } \times \mathrm { I D F }$ values of all frequent items in each document in cluster $c _ { y } .$ . We next calculate the combined cohesion score of merging clusters $c _ { t 3 }$ and $c _ { t 4 }$ for the example in Table 3:

frequent itemset and its inclusion provides a base for the proposed TAFIED method. With this benchmark technique, we can evaluate the use of conventional frequent itemset-based clustering for event episode discovery. In line with previous research that applies feature-based clustering to discover event episodes, we also included HAC as a benchmark; this feature-based document clustering technique can support event episode discovery [12] and retrospective event detection [34], with promising efectiveness. Finally, we augmented HAC with the time-decaying function [17], such that $\mathrm { H A C } + \mathrm { T D }$ can adjust the similarity of diferent news articles according to their temporal distance. The time-decaying similarity function is defined as $s i m _ { t i m \epsilon }$ -decaying $( d _ { i } , d _ { j } ) = \bar { s i m } ( d _ { i } , d _ { j } ) \times \exp ( - \frac { t ( d _ { j } ) - t ( d _ { i } ) } { T } )$ , where $s i m ( d _ { i } , \ d _ { j } )$ is the cosine similarity between d and $d _ { j } , t ( d _ { i } ) _ { i }$ , which indicates the timestamp of the ith document, and T is the time interval between the first and last document in the time-ordered sequence of documents pertinent to the focal event, $t ( d _ { | S | } ) \cdot t ( d _ { 1 } ) ,$ , in which |S| is the total number of documents describing that event. Overall, these benchmarks represent prevalent techniques for event episode discovery.

$$
\text {Cohesion} \left(\mathrm{c} _ {\mathrm{t} 3} \leftarrow \mathrm{c} _ {\mathrm{t} 4}\right) = 1. 3 2 1 = \frac {\left(\frac {2}{3} \times (5 + 7 + 1 + 2) \times \log \frac {1 0}{6} \times 1\right) + \left(\frac {3}{3} \times (2 + 1) \times \log \frac {1 0}{5} \times 1\right) + \left(\frac {0}{3} \times (2 + 3 + 4 + 5) \times \log \frac {1 0}{4} \times (- 1)\right) + \left(\frac {1}{3} \times (4) \times \log \frac {1 0}{4} \times 1\right)}{(5 + 7 + 1 + 2) \times \log \frac {1 0}{6} + (2 + 1) \times \log \frac {1 0}{5} + (2 + 3 + 4 + 5) \times \log \frac {1 0}{4} + (4) \times \log \frac {1 0}{4}} + 1
$$

$$
\text {Cohesion} \left(\mathrm{c} _ {\mathrm{t} 4} \longleftarrow \mathrm{c} _ {\mathrm{t} 3}\right) = 1. 4 7 8 = \frac {\left(\frac {4}{4} \times (3 + 2) \times \log \frac {1 0}{6} \times 1\right) + \left(\frac {0}{4} \times (1) \times \log \frac {1 0}{4} \times (- 1)\right) + \left(\frac {2}{4} \times (2 + 1 6 + 1 2) \times \log \frac {1 0}{5} \times 1\right) + \left(\frac {1}{4} \times (2) \times \log \frac {1 0}{4} \times (- 1)\right)}{(3 + 2) \times \log \frac {1 0}{6} + (1) \times \log \frac {1 0}{4} + (2 + 1 6 + 1 2) \times \log \frac {1 0}{5} + (2) \times \log \frac {1 0}{4}} + 1
$$

Combined-Cohesion $( \mathsf { c } _ { \mathsf { t 3 } }  \mathsf { c } _ { \mathsf { t 4 } } ) = \sqrt { 1 . 3 2 1 \times 1 . 4 7 8 } \times \frac { e ^ { 2 4 - 1 7 } } { 1 + e ^ { 2 4 - 1 7 } } = 1 . 3 9 6$

## 4. Data and evaluation design

We empirically evaluated the proposed method, including several prevalent techniques as benchmarks. In this section, we describe the corpus of articles used in the evaluation and detail the benchmark techniques, performance measures, and parameter tuning analyses.

## 4.1. Document collection

We used the event corpus from Nallapati, Feng, Peng, and Allan [17], which contains 248 event episodes associated with 53 distinct events described by 1468 related news articles (stories), selected from TDT2 and TDT3 corpora. In this sample, the news articles are relatively balanced across the 53 events, and each event consists of a relatively modest number of news articles. The length of news documents averages 64.2 words, and the average number of features identified for each event. after feature extraction. is 520. In Table 4. we summarize the event corpus.

## 4.2. Benchmark techniques

Three prevalent techniques served as performance benchmarks: FIHC, HAC, and HAC augmented with a time-decaying function (HAC + TD). FIHC partitions (clusters) documents on the basis of the

Summary of Event Corpus.

<table><tr><td></td><td>Average</td><td>Minimum</td><td>Maximum</td></tr><tr><td>Number of stories per event</td><td>27.7</td><td>16</td><td>30</td></tr><tr><td>Number of stories per episode</td><td>5.92</td><td>1</td><td>25</td></tr><tr><td>Number of episodes per event</td><td>4.68</td><td>2</td><td>8</td></tr><tr><td>Duration of episode (Days)</td><td>8.32</td><td>1</td><td>103</td></tr><tr><td>Duration of event (Days)</td><td>31.55</td><td>2</td><td>138</td></tr></table>

## 4.3. Performance measures

We used cluster recall and cluster precision to measure the performance of each technique for event episode discovery. Both measures reflect the association of documents in the same cluster (episode) and represent crucial performance measures for document clustering [44]. Given each event in the corpus of news articles, we considered known event episodes as the true (correct) episodes of the target event. The cluster recall (CR) and cluster precision (CP) of the target event are $\begin{array} { r } { C R = \frac { | C A | } { | T A | } } \end{array}$ and $\begin{array} { r } { C P = \frac { | C A | } { | G A | } } \end{array}$ , where TA refers to the set of associations of documents in the true event episodes, GA denotes the set of associations of documents in the event episodes generated by a technique under evaluation, and CA is the set of associations of documents that exists in both the true and generated event episodes.

As an illustration, consider a sequence of documents $S = < d _ { 1 } , d _ { 2 } ,$ $d _ { 3 } , d _ { 4 } , d _ { 5 } , d _ { 6 , d _ { 7 } } >$ pertaining to an event, such that S can be classified into three true event episodes, $E P _ { 1 } , E P _ { 2 } ,$ and $E P _ { 3 } ,$ where $E P _ { 1 } = \{ d _ { 1 } , d _ { 2 } \} _ { ; }$ $E P _ { 2 } ~ = ~ \{ d _ { 3 } , ~ d _ { 4 } , ~ d _ { 5 } , ~ d _ { 6 } \}$ , and $E P _ { 3 } \ = \ \{ d _ { 7 } \}$ . Thus, seven associations of documents exist: $\{ ( d _ { 1 } , d _ { 2 } ) , ( d _ { 3 } , d _ { 4 } ) , ( d _ { 3 } , d _ { 5 } ) , ( d _ { 3 } , d _ { 6 } ) , ( d _ { 4 } , d _ { 5 } ) , ( d _ { 4 } , d _ { 6 } ) ,$ $( d _ { 5 } , d _ { 6 } ) \}$ }. Alternatively, we could let the event episodes identified by an investigated technique be $G _ { 1 }$ and $G _ { 2 } ,$ where $G _ { 1 } = \{ d _ { 1 } , d _ { 2 } , d _ { 3 } \}$ and $G _ { 2 } =$ $\{ d _ { 4 } , d _ { 5 } , d _ { 6 } , d _ { 7 } \}$ . Then nine associations of documents, including {(d , $d _ { 2 } ) , ( d _ { 1 } , d _ { 3 } ) , ( d _ { 2 } , d _ { 3 } ) , ( d _ { 4 } , d _ { 5 } ) , ( d _ { 4 } , d _ { 6 } ) , ( d _ { 4 } , d _ { 7 } ) , ( d _ { 5 } , d _ { 6 } ) , ( d _ { 5 } , d _ { 7 } ) , ( d _ { 6 } , d _ { 7 } ) \}$ would exist in the generated event episodes. In this case, four associations of documents, $\{ ( d _ { 1 } , d _ { 2 } ) , ( d _ { 4 } , d _ { 5 } ) , ( d _ { 4 } , d _ { 6 } ) , ( d _ { 5 } , d _ { 6 } ) \}$ , are consistent in both the true and generated event episodes, so $C R = 4 / 7$ and $C P = 4 / 9$

Using the cluster recall and cluster precision attained for each event in the corpus of news articles, we apply a weighted average method to measure overall efectiveness across all events. To assess the trade-of between cluster precision and recall, we used the precision/recall tradeof (PRT) curve [45] to reveal the efectiveness of a technique with respect to diferent merging threshold values, such as the intercluster similarity threshold for HAC and the cluster merging threshold for FIHC and TAFIED. For HAC, we examined merging thresholds between 0 and 1, in increments of 0.02. For both FIHC and TAFIED, the value of combined cohesion ranged from 0 to 2, and two clusters would be merged if the value exceeded 1. In general, PRT curves close to the upper right corner are more desirable than those near the point of origin.

![](/api/attachments/9PHR7YS2/fulltext/images/1e52e1b22afaa90120360ef483987e5ed1a610cfba388dc5db43ee53a3f0421c.jpg)

![](/api/attachments/9PHR7YS2/fulltext/images/651f98f9d68c52a2be5d1dacba2eb35911703115098abddb48d04a32925edf18.jpg)  
0.10.2 0.3 0.4 0.5 0.6 →0.7—0.80.9 1.0

![](/api/attachments/9PHR7YS2/fulltext/images/493fc216c2ca91472ec4089764289c25200a830ff34a160fd037f7e431c071dd.jpg)  
Fig. 4. (a) Minimum Global Support (g ) of TAFIED Parameter Tuning. (b) Significance Threshold for Cluster Support (s ) of TAFIED Parameter Tuning. (c) Tolerant Time Gap (w) of TAFIED Parameter Tuning.

## 4.4. Parameter tuning analyses

We collected a sample of news articles pertaining to 10 events and performed a series of parameter tuning experiments to determine appropriate values of the parameters essential to each investigated tech nique. In particular, several parameter values are important to TAFIED: minimum global support (g ), the significance threshold for cluster support (s ), and the tolerant time gap (w). We first evaluated g over the range of 0.02, 0.05, 0.1, and 0.5 (in increments of 0.1 between 0.1 and 0.5) with the default setting of $s _ { t } = 0 . 2$ and $w = 2 . 0$ . As we show in Fig. 4a, TAFIED appears efective with $g _ { t }$ set to 0.02.

We then assessed the efect of s (between 0.1 and 1.0, in increments of 0.1) on clustering efectiveness, with $g _ { t } = 0 . 0 2$ and $w = 2 . 0$ . As Fig. 4b indicates, the performance of TAFIED has a tradeof between recall and precision when $s _ { t } = 0 . 1 ,  \ 0 . 2 ,$ , and 0.3. According to the overall results, we set $s _ { t } = 0 . 2$ as the average performance.

Next, we examined the efectiveness of TAFIED with w ranging from 1.5 to 4, in increments of 0.5. As Fig. 4c shows, we also observe a trade of between $w = 2 . 0$ and 2.5. Overall, TAFIED achieves better results when $w = 2 . 0$ , and appears most efective when $g _ { t } = 0 . 0 2 , s _ { t } = 0 . 2$ , and $w = 2 . 0$ . We therefore adopted these parameter values to perform the subsequent evaluation.

For FIHC, we need to determine the minimum global support (g<sub>f</sub>) and the significance threshold for cluster support $( s _ { f } )$ . We followed the same procedure to tune essential parameters by fixing the value of $s _ { f }$ and then assessing values of $g _ { f }$ over the range of 0.02, 0.05, 0.1, to 0.5 (in increments of 0.1 between 0.1 and 0.5). As we show in Fig. 5a, the smaller the value minimum global support, the greater efectiveness FIHC achieves. We set g to 0.02 according to the performance tuning results.

We then set g to 0.02 to examine the efect of $s _ { f }$ (between 0.1 and 1.0, in increments of 0.1) on clustering efectiveness. As we indicate in Fig. 5b, FIHC achieved the best performance when $g _ { f } \ = \ 0 . 0 2$ and $s _ { f } = 0 . 8$

Because HAC uses TF × IDF as the feature selection metric, we need to determine two important parameters: the number of features (k ) and the document representation scheme $\left( r _ { h } \right)$ . We examined the efects of $k _ { h }$ over the range between 50 and 250 (in increments of 50). As shown in Fig. 6a, setting $k _ { h }$ to 150 appeared most appropriate.

We also examined the efects of document representation scheme $\left( r _ { h } \right)$ on the efectiveness of HAC, using the binary and TF × IDF schemes. According to the results shown in Fig. 6b, we chose a binary scheme for $r _ { h } .$

Finally, the parameters that need to be turned for $\mathrm { H A C } + \mathrm { T D }$ are identical to those of $\mathrm { H A C } ;$ we therefore followed the same procedure for HAC + TD and set the number of features to 150 and adopted $\mathrm { T F } \times \mathrm { I D F }$ as the document representation scheme.

## 5. Results and discussion

## 5.1. Comparative evaluation results

According to our comparative assessment of the efectiveness of TAFIED and three benchmark techniques (FIHC, HAC, and $\mathrm { H A C } + \mathrm { T D } ) _ { \mathrm { : } }$ as we show in Fig. 7, TAFIED is consistently more efective for event episode discovery than any other benchmark techniques across the diferent merging thresholds we consider. The traditional feature-based HAC, which does not consider essential temporal characteristics of news articles, appears least efective; $\mathrm { F I H C } ,$ which uses frequent items to cluster news articles and considers the burst of features (terms) in the same event episodes to some degree, groups (clusters) articles that share more features and thus results in better performance than the feature-based HAC. Finally. HAC + TD. which considers temporal localization by using a time-decaying function to adjust the similarity between news articles, outperforms both HAC and FIHC, neither of which considers this temporal characteristic. This result is in line with previous research that suggests the use of a time-decaying function to improve the efectiveness of HAC for discovering event episodes [17]. Overall, the comparative results show our proposed method, which considers the frequent term set (burst and new terms) and temporal characteristics of news articles, capable of identifying diferent event episodes more efectively than the benchmarks.

Because of the trade-of between cluster recall and cluster precision, we performed a best-versus-best comparison by examining the best Fmeasure values achieved by the respective techniques for each of the 53 discovered events.<sup>3</sup> As Table 5 summarizes, TAFIED attains a F-measure value higher than that of any benchmark technique, in congruence with its lower cluster recall and the higher cluster precision values.

In addition, we assessed the statistical significance of efectiveness diferentials of the respective techniques across the 53 events. Specifically, we conducted the Wilcoxon signed-rank test to examine the statistical significance of the efectiveness diferences between pairs of F-measure values. The Wilcoxon signed-rank test, a nonparametric statistical hypothesis test, represents a legitimate alternative to the paired t-test when the distribution of the diference between two samples' means cannot be assumed to be normally distributed.⁴ As we show in Table 6, the F-measure value attained by TAFIED is higher than those attained by HAC, FIHC, and HAC + TD significant at the 0.01, 0.05, and 0.1 level, respectively, while the F-measure values of the benchmark techniques were not significantly diferent. The results suggest TAFIED significantly more efective for discovering event episodes than the benchmark techniques.

![](/api/attachments/9PHR7YS2/fulltext/images/63bc0ac3ad78ef05e6283f72b638be659b997f31dbd61591d5eb377bd8dbf52f.jpg)

![](/api/attachments/9PHR7YS2/fulltext/images/f401b372bb5e29ea58351a2d62f84f14a2c73aa0e976b59d15f78d289d889cdd.jpg)  
Fig. 5. (a) Minimum Global Support (g ) of FIHC Parameter Tuning. (b) Significance Threshold for Cluster Support (s ) of FIHC Parameter Tuning.

## 5.2. Efect of temporal proximity on TAFIED performance

According to the evaluation results, TAFIED is more efective for discovering event episodes than either HAC or FIHC. To analyze the performance enhancement achieved by including the temporal characteristics of news articles, we examined its efect by removing the TP function from the proposed method and then re-evaluating its effectiveness. As we show in Fig. 8, the efectiveness of TAFIED without the TP function decreased substantially. This result explicitly indicates the value of TP function and reinforces the significance of considering temporal characteristics of news articles when clustering them for event episode discovery.

## 5.3. Importance of temporal characteristic for event episode discovery

Because the clustering process of FIHC is similar to that of TAFIED, we incorporated the TP function with FIHC to create FIHC + TP, which considers the temporal diferences of the news documents within a cluster to measure the goodness-of-fit score for document assignments to clusters and cluster merge evaluation in the cluster distinction and cluster aggregation steps. We followed the same procedure to tune important parameters for FIHC + TP, including the parameter values for the tolerant time gap (w), the minimum global support (g ), and the significance threshold for cluster support (s ). The performance-tuning analyses suggested setting values of 0.1, 0.3, and 2 for the minimum global support, significance threshold for cluster support, and tolerant time gap for FIHC + TP, respectively.

![](/api/attachments/9PHR7YS2/fulltext/images/d85d0f2a117aa23bd1f0429eb5767770b5354237c23ac9b16dcb48e3b42063d1.jpg)

![](/api/attachments/9PHR7YS2/fulltext/images/87968161fdaaea30ac9ce2af550c14306c599559a18da82e8b592684579dbabc.jpg)  
Fig. 6. (a) Number of Features (k<sub>h</sub>) of HAC Parameter Tuning. (b) Document Representation Scheme (r<sub>h</sub>) of HAC Parameter Tuning.

![](/api/attachments/9PHR7YS2/fulltext/images/c3accbfc534ee9e546c81ebc72f1b22b78b5bd016abacf0188e908b0cb26a38f.jpg)  
Fig. 7. Comparative Evaluation Results.

As we illustrate in Fig. 9, TAFIED remains more efective than FIHC + TP or HAC + TD. partially because it considers the essential frequent term set and temporal characteristics of news articles to discover event episodes. As noted, HAC + TD considers temporal locali zation by using a time-decaying function to adjust the similarity between news articles, and outperforms HAC and FIHC, neither of which takes this temporal characteristic into account. These comparative results reinforce the value of a time-decaying function to improve the efectiveness of HAC for event episode discovery. The performance of FIHC + TP is lower than that of HAC + TD but notably not better than that of FIHC. Together, these results suggest a relatively limited value of

Table 5  
Best F-Measure Values with Associated Cluster Recall and Cluster Precision Values.

<table><tr><td></td><td>Cluster Recall</td><td>Cluster Precision</td><td>F-measure</td></tr><tr><td>TAFIED</td><td>0.706</td><td>0.593</td><td>0.584</td></tr><tr><td>FIHC</td><td>0.724</td><td>0.498</td><td>0.543</td></tr><tr><td>HAC</td><td>0.741</td><td>0.472</td><td>0.533</td></tr><tr><td>HAC + TD</td><td>0.740</td><td>0.520</td><td>0.567</td></tr></table>

TAFIED FIHC FIHC+TP HAC →HAC+TD  
Table 6  
Wilcoxon Signed-Rank Test on F-Measure Values of Investigated Methods.

<table><tr><td></td><td>FIHC</td><td>HAC</td><td>HAC + TD</td></tr><tr><td>TAFIED</td><td>0.017**</td><td>0.002***</td><td>0.072*</td></tr><tr><td>FIHC</td><td>—</td><td>0.642</td><td>0.108</td></tr><tr><td>HAC</td><td>—</td><td>—</td><td>0.101</td></tr></table>

\* p-value < 0.1.  
\*\* p-value < 0.05 and.  
\*\*\* p-value < 0.01.

![](/api/attachments/9PHR7YS2/fulltext/images/c61c18ca28f6ac7ab1705159d4febed94e5170785fd8e1d846fc7587be968573.jpg)  
Fig. 8. Efects of Temporal Proximity on TAFIED Technique.

![](/api/attachments/9PHR7YS2/fulltext/images/3b5361f96384ce812354438175489426de7931a60ba4937233c5d2396d7baafc.jpg)  
Fig. 9. Efects of Temporal Characteristics on Event Episode Discovery Techniques.

TP function to FIHC, possibly because FIHC depends on frequent terms for document clustering, yet the number of frequent terms in news articles pertinent to an event episode may not be small, and the articles describing diferent episodes of an event likely share similar frequent terms. These frequent terms then become less representative of the diferent event episodes and FIHC groups articles pertinent to distinct, temporally adjacent episodes in a cluster, thereby hindering its performance.

We also consider the computational processing requirements of the respective techniques. Overall, HAC is least computationally eficient; it performs the similarity analysis at the document level and exhaustively combines articles or article clusters that share the greatest similarity. In contrast, both FIHC and TAFIED determine a set of frequent terms, use these terms to cluster (group) news articles, and then make cluster assignments, distinctions, and merging decisions. The computational efficiency and scalability of HAC rely on the quality of news articles; those of FIHC or TAFIED depend on the number of initial clusters. When the number of initial clusters is smaller than the number of news articles, FIHC and TAFIED are more eficient than HAC. The incorporation of essential temporal characteristics, such as using a TP or time-decaying function, is not likely to afect computational eficiency significantly, because these functions are based on the temporal diference between documents.

## 6. Discussion and implications

The evaluation results reveal the criticality of frequent terms and temporal characteristics of news articles for event episode discovery. Existing techniques that cluster documents on the basis of feature similarity of pairwise documents cannot efectively identify distinct episodes from a news corpus, because the important features (terms) appearing in the documents about a specific event often highly overlap. As revealed in our analyses, methods that follow the frequent termbased approach (TAFIED and FIHC) outperform techniques using the feature-based similarity approach (HAC). As noted, the TAFIED groups documents on the basis of the set of frequent terms to gradually differentiate the documents pertaining to distinct episodes. The findings imply that the use of a set of frequent terms is both viable and ad vantageous to discover event episodes from a news corpus. By devel oping a method that is built on the use of frequent terms, we extend the event episode discovery research by highlighting another promising clustering strategy that groups news documents that pertain to a focal event into episodes, according to their frequent terms rather than the similarity of their feature sets.

Furthermore, temporal characteristics of news articles also are crucial to event episode discovery, particularly when considering various sources capable of publishing (releasing) a vast quantity of online news articles within a short time frame. As the evaluation results show, methods that consider temporal characteristics can support event episode discovery more efectively than prevalent techniques that do not consider such characteristics. Unlike the common use of a linear timepenalty function or a nonlinear time-decaying function to measure the temporal diference between pairs of documents and adjust their similarity, the proposed TAFIED method considers temporal characteristics by incorporating a TP function to measure the temporal adjacency of news articles and determine the soundness of grouping them in a cluster (the same episode), and is shown more efective for event epi sode discovery. This finding implies that a TP function that considers temporal tolerance to group news documents is more efective and flexible for identifying event episodes, because these episodes tend to vary in the length of their temporal intervals, which in turn indicates the need to properly measure temporal adjacency and further analyze its efects on event episode discovery.

After observing the proposed method’s greater efectiveness, we also explored the existence of conditions that would favor our method or a benchmark technique. Because of the infeasibility of exhaustively considering all the diferent conditions across the 53 news events, we instead concentrated on the article distribution of the event that our method attains the highest F-measure value (0.908) while HAC + TD (best-performing benchmark) has a value of 0.731 as well as the article distribution of the event that HAC + TD achieves the highest F-measure value (0.905) while the proposed TAFIED has a value of 0.771. Fig. 10 illustrates the distribution of articles for two events, with x-axis being the publishing time, and the size of the triangle or circle indicating the number of articles published in the same day. As shown, both events have three episodes and their first article is published at x = 0. In the event that TAFIED performs the best, Super Bowl XXXII between Denver and Green Bay (shown in the upper panel), we note a noticeable overlap in publishing time of the articles pertinent to Episode #2 and #3, with some articles of Episode#1 published in a small time difer ence and within the tolerance interval between articles (w). For the event that HAC + TD performs the best, a murder trial of two New Jersey teenagers accused of killing their newborn son (shown in the lower panel), articles that belong to distinct episodes are published in diferent time periods and those pertaining to the same episode are published in close temporal adjacency. As described, the proposed method considers two issues: news articles that describe diferent episodes of an event and have similar content, and diferent episodes that could emerge concurrently within a time window. According to the analysis results, our method achieves better performance when articles about diferent episodes of an event are published in an overlapped manner (temporal concurrency), which is common to the development and reporting of many events. On the other hand, conventional clustering techniques that rely on the temporal distance of the publishing time between articles for adjusting the inter-article similarity seem to perform well when diferent episodes of the event are separated by obvious time intervals.

![](/api/attachments/9PHR7YS2/fulltext/images/a81bdfb90ca9364e0fa10854c72814664620ea5b64d4dcc92e4dd634b5ac2aec.jpg)  
Fig. 10. Article Distribution of Event TAFIED and HAC + TD Shows Highest Fmeasure Value.

Finally, the proposed TAFIED is more efective than benchmark techniques for discovering diferent episodes of an event from sequences of news articles. Our method can advance firms’ practices by supporting automatic processing and analyses of online news article (documents) for event evolution pattern discovery, so that firms can unfold distinct episodes of important events as they develop over time. By efectively clustering news articles into appropriate episodes, the proposed method enables firms to better predict important trends and changes in the environment for increased competitiveness. Additionally, the proposed method groups documents on the basis of their frequent items, which could be considered for labeling event episodes; i.e., suggesting appropriate labels for diferent event episodes. We use the news articles regarding “Hurricane Mitch” in our evaluation data set as an illustration. As shown in Fig. 11, this event comprises five episodes: “emergence of tropical storm Mitch,” “hurricane Mitch up grade,” “path and impact forecasts,” “damage estimations and precau tionary measures,” and “update and warning before landing,” respec tively. For episode labeling, we presented the frequent items identified by our method to a researcher knowledgeable about the events in the data set, who then selected those appropriate to label each episode. For example, frequent items such as “tropical storm Mitch,” “Atlantic ocean,” and “Jamaica” are selected as labels for “Emergence of tropica storm Mitch” episode. Example labels for “hurricane Mitch upgrade” episode include “watch,” “strengthen,” and “Hurricane warning.”

## 7. Conclusion and future research directions

When performing environmental surveillance, companies may en counter multiple events and topics related to customers, market, com petitors, industry, technology, or government regulations. Online news articles represent a common but crucial source for monitoring and tracking such events. To mitigate information overload and tedious processing required to monitor and track important events, firms need automated event episode discovery methods to classify and organize news articles about the same event that pertain to diferent episodes (subevents). We propose TAFIED and empirically examine its efectiveness, in comparison with feature-based HAC, HAC augmented with a time-decaying function, and FIHC. The evaluation results confirm that TAFIED outperforms the benchmark techniques as manifested by significantly better cluster recall and cluster precision values. In addition, incorporating a TP function can increase event episode discovery effectiveness.

This study contributes to extant literature in several ways. First, our novel TAFIED method can discover event episodes embedded in se quences of news articles that pertain to a specific news event. The evaluation results afirm that TAFIED is capable of automatically identifying distinct episodes of an event from news articles to enable subsequent event evolution pattern discovery. Second, most existing document clustering techniques, which rely on the similarity of important features in news articles to determine whether those articles belong to the same event episode, are not appropriate for event episode discovery, because articles pertinent to the same event likely have similar content (feature), except for the portion that is specific to its diferent episodes. We therefore stress the frequent itemset and consider features (terms) associated with diferent episodes to cluster news articles, which can group articles specific to an episode. In this efort, our method extends FIHC by considering essential temporal characteristics of news articles and thereby specifying distinct episodes from among sequences of news articles. The proposed TAFIED method emerges as more efective for discovering diferent episodes of an event than any benchmark techniques. Third, though previous research has cited temporal diferences to assess the similarity of news articles and used a linear time-penalty function or nonlinear time-decaying function to adjust similarity accordingly, this approach is not efective for persistent episodes, because it ofers limited temporal tolerance. For example, the similarity of two news articles, published one day apart, could be unduly discounted, which is inefective for discovering longer episodes (e.g., reducing the similarity of news articles describing an episode with a 10-day duration by 10% or more). Our proposed method addresse the temporal tolerance issue and provides a TP function to evaluate the similarity of diferent news articles according to their temporal relationships. The evaluation results afirm that the incorporation of the TP function enhances the performance of the proposed TAFIED method for event episode discovery.

This proposed method can also support other applications. For example, distinct events could be categorized; events of the same category (type) might follow a defined progression pattern that consists of different episodes that occur in a temporal or causal sequence [12]. By discovering episodes of separate events of the same category (type), we can generalize the underlying event evolution patterns, through the identified episodes and their associations with respect to the focal event category, and thus better support event tracking by firms [12,14,18,19]. Furthermore, we consider temporal adjacency in the context of event episode discovery, which ofers an important temporal characteristic of essential features that exist in other application domains. For example, discussion threads in an online forum have similar features, and discussions pertinent to a topic can be clustered according to their diferent subtopics, which should aid in managing the content in the forum [46].

![](/api/attachments/9PHR7YS2/fulltext/images/2de2ce9a82941e9175126ae3237ef4f141ed12176ccdd100f8879a9dad313593.jpg)  
Fig. 11. Subset of Frequent Items in Each Episode of Event “Hurricane Mitch”.

This study can be extended in several promising directions. First, the news articles collected from TDT2 and TDT3 that are used in the eva luation include 53 events, each comprised of a relatively small number of episodes that range from 2 to 8 episodes. To produce more generalizable and robust results, additional sequences of news articles that describe more distinct, complex events should be included to evaluate the proposed method. Second, we assume that a news article pertains to one and only one episode; additional studies could relax this assump tion by extending the proposed method to multi-episode analyses. Conceivably, a news article pertains to multiple episodes of an event, such as one that describes several event developments. Third, event episode discovery is crucial to multi-document summaries, so a promising extension would detail episode-based, multi-document summarization, as is essential for many application domains. Fourth, this study focuses on developing an efective method to discover episodes from news articles associated with an event. Although our results suggest its efectiveness, the proposed method’s value and utility need further evaluations, including the use of additional sequences of realworld news articles in extrinsic evaluations. Last but not least, label choices for diferent episodes (from their respective frequent items) by targeted practitioners also deserve future research attention, so that the chosen labels are meaningful and appropriate for their practices. Although we observe that a researcher’s selecting labels from the identified frequent items appears straight-forward (without any dificulty), we nevertheless acknowledge the subjectivity of label choices and recognize the need to assess the selected (suggested) labels’ appropriateness by targeted practitioners using qualitative interview and case study methods.

## CRediT authorship contribution statement

Yen-Hsien Lee: Conceptualization, Methodology, Writing - original draft, Writing - review & editing. Paul Jen-Hwa Hu: Validation, Formal analysis, Writing - original draft, Writing - review & editing. Hongquan Zhu: Validation, Formal analysis. Hsin-Wei Chen: Software, Investigation, Visualization.

## Acknowledgment

This work was partially supported by the Ministry of Science Technology of the Republic of China (Taiwan) under Grants 99-2410-H-415-019-MY2 and 107-2410-H-415-011-MY3.

## References

[1] C.W. Choo, Environmental scanning as information seeking and organizational learning, Inf. Res. 7 (2001) 1–14.

[2] C.V. Robinson, J.E.L. Simmons, Organising environmental scanning: exploring information source, mode and the impact of firm size, Long Range Plann. (2017).

[3] R.Y.K. Lau, S.S.Y. Liao, K.F. Wong, D.K.W. Chiu, Web 2.0 environmental scanning and adaptive decision support for business mergers and acquisitions, Mis Q. 36 (2012) 1239–1268.

[4] X.M. Xu, G.R. Kaye, Y. Duan, UK executives’ vision on business environment for information scanning: a cross industry study, Inf. Manag. 40 (2003) 381–389.

[5] R.L. Daft, J. Sormunen, D. Parks, Chief executive scanning, environmental characteristics and company performance: an empirical study, Strateg. Manage. J. 9 (1988) 123–140.

[6] K.J. Sund, Scanning, perceived uncertainty, and the interpretation of trends: a study of hotel director's interpretation of demographic change, Int. J. Hosp, Manag. 33 (2013) 294–303.

[7] S.C. Jain, Environmental scanning in U.S. corporations, Long Range Plann. 17 (1984) 117–128

[8] G. Jogaratnam, R. Law, Environmental scanning and information source utilization: exploring the behavior of Hong Kong Hotel and tourism executives, J. Hosp. Tour. Res, 30 (2006) 170–190.

[9] A.S.A. du Toit, Using environmental scanning to collect strategic information: a South African survey, Int. J. Inf. Manage. 36 (2016) 16–24.

[10] S. Tan, H.H. Teo, B. Tan, K. Wei, Environmental scanning on the internet,

International Conference on Information Systems, Helsinki, 1998, pp. 76–87.

[11] H. Haase, M. Franco, Information sources for environmental scanning: do industry and firm size matter? Manage, Decis. 49 (2011) 1642–1657

[12] C.P. Wei, Y.S. Chang, Discovering event evolution patterns from document sequences, IEEE Trans. Syst. Man Cybern. A. Syst. Hum. 37 (2007) 273–283.

[13] D.C. Luckham, Event Processing for Business: Organizing the Real-Time Enterprise, Wiley, 2011.

[14] Z. Li, S. Zhao, X. Ding, T. Liu, EEG: Knowledge Base for Event Evolutionary Principles and Patterns, Springer Singapore, Singapore, 2017, pp. 40–52.

[15] D.-R. Liu, M.-J. Shih, C.-J. Liau, C.-H. Lai, Mining the change of event trends fo decision support in environmental scanning, Expert Syst. Appl. 36 (2009) 972–984.

[16] J. Yang, J. McAuley, J. Leskovec, P. LePendu, N. Shah, Finding progression stages in time-evolving event sequences, The 23th International World Wide Web Conference, ACM, Seoul, Korea, 2014

[17] R.M. Nallapati, A. Feng, F. Peng, J. Allan, Event threading within news topics, Thirteenth ACM Conference on Information and Knowledge Management, Washington, D.C., 2004, pp. 425–432.

[18] C.C. Yang, X. Shi, C.P. Wei, Discovering event evolution graphs from news corpora, JEEE Trans, Syst, Man Cybern, A. Syst, Hum, 39 (2009) 850–863

[19] S. Guo, K. Xu, R. Zhao, D. Gotz, H. Zha, N. Cao, EventThread: visual summarization and stage analysis of event sequence data, IEEE Trans. Vis. Comput. Graph. 24 (2018) 56–65.

[20] M. Ubaidullah Bokhari, K. Adhami, Event Evolution Modeling for Eficient New Search, (2015)

[21] X. Li, Y. Zheng, Y. Dong, Discovering evolution of complex event based on correlations between events, 11th Web Information System and Application Conference Tianjin, China, 2014, pp. 47–50.

[22] Y. Cai, Q. Li, H. Xie, T. Wang, H. Min, Event relationship analysis for temporal event search, in: W. Meng, L. Feng, S. Bressan, W. Winiwarter, W. Song (Eds.), Database Systems for Advanced Applications, Springer Berlin Heidelberg, Berlin, Heidelberg, 2013, pp. 179–193.

[23] R.L. Liu, Collaborative multiagent adaptation for business environmental scanning through the Internet, Appl. Intell. 20 (2004) 119–133.

[24] C.P. Wei, Y.H. Lee, Event detection from online news documents for supporting environmental scanning, Decis. Support Syst. 36 (2004) 385–401.

[25] J. Granat, Event mining based on observations of the system, J. Telecommun. Inf. Technol. 3 (2005) 87–90.

[26] L. Fahed, A. Brun, A. Bover, DEER: Distant and essential episode rules for early prediction, Expert Syst, Appl, 93 (2018) 283–298.

[27] Y. Ning, S. Muthiah, H. Rangwala, N. Ramakrishnan, Modeling precursors for event forecasting via nested multi-instance learning, Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, San Francisco, California, USA, 2016, pp. 1095–1104.

[28] R. Ahirrao, S. Patel, An overview on event evolution technique, Int. J. Comput. Appl. 77 (2013) 7–11.

[29] L. Kong, R. Yan, H. Jiang, Y. Zhang, Y. Gao, L. Fu, Mining event temporal bound aries from news corpora through evolution phase discovery, in: H. Wang, S. Li S. Oyama, X. Hu, T. Qian (Eds.), International Conference on Web-Age Information Management, Springer, Berlin, Heidelberg, Wuhan, China, 2011, pp. 554–565.

[30] C.P. Wei, Y.H. Lee, Y. Chiang, C. Chen, C.C. Yang, Exploiting temporal characteristics of features for efectively discovering event episodes from news corpora, J. Assoc, Inf, Sci, Technol, 65 (2014) 621–634.

[31] D. Huang, S. Hu, Y. Cai, H. Min, Discovering event evolution graphs based on News articles relationships. 2014 JEEE 11th International Conference on e-Business en: gineering (2014) 246–251.

[32] A. Wen, W. Lin, Y. Ma, H. Xie, G. Zhang, News event evolution model based on the reading willingness and modified TF-IDF formula, J. High Speed Networks 23 (2017) 33–47.

[33] P. Zhou. B. Wu. Z. Cao. EMMBTT: a novel event evolution model based on TFxIEF and TDC in tracking News streams, 2017 IEEE Second International Conference on Data Science in Cyberspace (DSC) (2017) 102–107

[34] Y. Yang, T. Pierce, J.G. Carbonell. A study on retrospective and on-line event de: tection. 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Melbourne, Australia, ACM Press, 1998, pp. 28–36.

[35] G. Kumaran, J. Allan, Text classification and named entities for new event detec tion 27th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Shefield, United Kingdom, ACM Press, 2004.

[36] G. Kumaran, J. Allan, Using names and topics for new event detection, Conferenc on Human Language Technology and Empirical Methods in Natural Language Processing, Association for Computational Linguistics, Vancouver, British Columbia, Canada, 2005, pp. 121–128.

[37] K. Zhang, J.Z. Li, G. Wu, New event detection based on indexing-tree and named entity, 30th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Amsterdam, Netherlands, 2007, pp.

[38] Q.H. Ramadan, M. Mohd, A review of retrospective news event detection, International Conference on Semantic Technology and Information Retrieval Putrajaya, Malaysia, 2011, pp. 209–214.

[39] J. Allan, V. Lavrenko, R. Swan, Explorations within topic tracking and detection, in: J. Allan (Ed.), Topic Detection and Tracking: Event-Based Information Organization, Kluwer Academic Publishers, 2002, pp. 197–224.

[40] J. Allan, S. Harding, D. Fisher, A. Bolivar, S. Guzman-Lara, P. Amstutz, Taking topic detection from evaluation to practice, 32th Annual Hawaii International Conference on System Sciences. Big Island. Hawaji, 2005.

[41] E.M. Voorhees, Implementing agglomerative hierarchical clustering algorithms for use in document retrieval, Inf. Process. Manag. 22 (1986) 465–476.

[42] B. Fung, K. Wang, M. Ester, Hierarchical document clustering using frequent itemsets. SIAM International Conference on Data Mining (2003) 59–70

[43] E. Brill, Some advances in rule-based part of speech tagging, 12th National Conference on Artificial Intelligence (AAAI-94), AAAI Press, Seattle, WA, 1994, pp. 722–727.

[44] D.G. Roussinov, H. Chen, Document clustering for electronic meetings: an experimental comparison of two techniques, Decis. Support Syst. 27 (1999) 67–79.

[45] M. Gordon, M. Kochen, Recall‐precision trade‐of: a derivation, J. Am. Soc. Inf. Sci. 40 (1989) 145–151.

[46] P.K. Srijith, M. Hepple, K. Bontcheva, D. Preotiuc-Pietro, Sub-story detection in Twitter with hierarchical Dirichlet processes, Inf. Process. Manag. 53 (2017) 989–1003.

Yen-Hsien Lee received his Ph.D. in Information Management from National Sun Yat-Sen University in Taiwan. He is currently an associate professor of the Department of Management Information Systems at the National Chiayi University in Taiwan. He was a visiting scholar at University of Utah in Fall 2002 and at University of Florida in Fall 2016. His papers have appeared in Journal of Management Information Systems, Journal of Organizational Computing and Electronic Commerce, ACM Transactions on Management Information Systems, Artificial Intelligence in Medicine, Journal of the American Society for Information Science and Technology, IEEE Transactions on Systems, Man and Cybernetics, and Decision Support Systems. His current research interests include knowledge discovery and data mining, knowledge management, information retrieval, text mining, and web mining.

Paul Jen-Hwa Hu is David Eccles Chair Professor at the David Eccles School of Business, the University of Utah. He has a Ph.D. in Management Information Systems from the University of Arizona. His current research interests include information technology in health care, technology implementation management, business analytics, e-commerce and digital government, technology-enabled innovation, human-computer interactions, and knowledge management. Hu has published papers in Management Information Systems Quarterly; Information Systems Research; Journal of Management Information Systems; Decision Sciences; Decision Support Systems; Journal of Association for Information Systems; Journal of Information Systems (AAA); Journal of Service Research; Journal of Busines Research; and various ACM and IEEE journals and transactions.

Hongquan Zhuis a professor at the School of Economics and Management, the Southwest Jiaotong University. He had a Ph.D. in Management Science and Engineering from the Academy of Mathematics and Systems Science, Chinese Academy of Science in 2001. His current research interests include financial markets and institutions and empirical asset pricing. He was a visiting scholar at the University of Utah in Spring 2013 and Fall 2015. Zhu has published papers in Journal of Banking and Finance; Journal of International Accounting Research; and International Review of Economics and Finance.

Hsin-Wei Chen received an MBA in Management Information Systems from National Chiayi University, Taiwan. He is currently a senior consultant in the AdvancedTEK International Corporation, Taiwan. His research interests include data mining, text mining, and knowledge management.
