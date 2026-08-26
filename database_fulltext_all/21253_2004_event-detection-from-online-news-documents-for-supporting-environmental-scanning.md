---
otero_id: 21253
otero_key: "9H3BCQMV"
title: "Event detection from online news documents for supporting environmental scanning"
authors: "Chih-Ping Wei; Yen-Hsien Lee"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00028-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Event detection from online news documents for supporting environmental scanning

Chih-Ping Wei\*, Yen-Hsien Lee

Department of Information Management, College of Management, National Sun Yat-Sen University, Kaohsiung, Taiwan, ROC

## Abstract

Environmental scanning, the acquisition and use of the information about events, trends, and relationships in an organization’s external environment, permits an organization to adapt to its environment and to develop effective responses to secure or improve the organization’s position in the future. Event detection technique that identifies the onset of new events from streams of news stories would facilitate the process of organization’s environmental scanning. However, traditional event detection techniques generally adopted the feature co-occurrence approach that identifies whether a news story contains an unseen event by comparing the similarity of features between the new story and past news stories. Such feature-based event detection techniques greatly suffer from the word mismatch and inconsistent orientation problems and do not directly support event categorization and news stories filtering. In this study, we developed an information extraction-based event detection (NEED) technique that combines information extraction and text categorization techniques to address the problems inherent to traditional feature-based event detection techniques. Using a traditional feature-based event detection technique (i.e., INCR) as benchmarks, the empirical evaluation results showed that the proposed NEED technique improved the effectiveness of event detection measured by the tradeoff between miss and false alarm rates. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Event detection; Environmental scanning; Information extraction; Text categorization; Event tracking

## 1. Introduction

As an organization’s environment becomes more complex and dynamic, uncertainty faced by the organization increases. Environmental scanning is the first link in the chain of perceptions and actions that permit an organization to adapt to its environment and subsequently to develop effective responses to secure or improve its position in the future [10,19,21]. As defined by Refs. [2,10], environmental scanning refers to ‘‘the acquisition and use of information about events, trends and relationships in an organization’s external environment, the knowledge of which would assist management in planning the organization’s future course of action.’’ Empirical research results suggest that environmental scanning is linked with improved organizational performance. For instance, Daft et al. [15] found that chief executives of highperforming firms scanned the environment more frequently and broadly than their counterparts in low-performing firms. Similarly, the empirical study conducted by Ahituv et al. [3] indicated significant differences in the level of environmental scanning and in the use of information systems between firms that were more successful in introducing new products into the market and firms that were less successful. As a result, scanning the external business environment for events, trends, and relationships from news services and websites has become a critical information activity of chief executive officers for planning their firms.

One of the major sources for environmental scanning is online news websites [9]. However, the proliferation of WWW, which improves the information circulation and increases the information source, has made the amount of scanning information exploded. However, the increases in scope and complexity of business environments make the interval between scanning efforts needed shorten. As a result, environmental scanning becomes more difficult to handle and has been a burden to managers. Thus, an information system that facilitates organizational scanning of external environments is essential. Specifically, the system needs to support detecting the onset of new events from news documents and tracking subsequent news stories that discuss an event of interest. In this study, we will mainly focus on event detection for environment scanning and leave event tracking as our future work.

Event detection is to identify the onset of new events from streams of news stories [4,43,44]. Practically, an event is referred to something happening in a certain place at a certain time [4,43,44]. An event (e.g., SPSS acquiring NetGenesis) is an instance of a specific event topic (e.g., business merger). Traditional event detection techniques generally adopted the feature co-occurrence approach that identifies whether a news story contains an unseen event by comparing the similarity of features between the news story and past news stories. Because news stories discussing the same event tend to be temporally proximate, a combined measure of lexical similarity and temporal proximity as a criterion for event detection was often employed [43,44]. Moreover, since a time gap between bursts of topically similar stories is often an indication of different events, the incorporation of a time window for event scoping was also commonly adopted [43,44].

Nevertheless, traditional feature-based event detection techniques incur several problems. First, there exist vocabulary discrepancies between reporters even when they describe the same event. For example, some may use ‘‘merger’’ or ‘‘purchase’’ to describe a business merger event, while others may use ‘‘acquisition’’ for the same event. Moreover, two news stories discussing the same event may be oriented from different angles, resulting in differences in features. Such word mismatch and inconsistent orientation problems limit the detection effectiveness of feature-based event detection techniques. Secondly, two news stories for different events may contain very similar feature sets since the events belong to the same event topic. For example, in the event topic of computer virus, the features ‘‘virus,’’ ‘‘computer,’’ ‘‘worm,’’ and ‘‘infection’’ may appear in every virus news story. In this case, the feature sets of these news stories will be similar, even though they discuss two different computer viruses. Finally, it would be essential to not only detecting whether a news story contains an unseen event, but also classifying the news story into an appropriate event topic. With the event categorization, filtering of news stories that are not of interest to a specific user can easily be supported. However, traditional event detection techniques do not directly support the described event categorization.

To overcome the problems inherent to traditional event detection techniques, limited form of story understanding is necessary. A news story about an event typically specifies the following event properties: when the event occurred, who was involved, where it took place, how it happened, and the impact, significance, or consequence of the event on the intended audience [26]. Understanding of news stories can be achieved by classifying a news story into an appropriate event topic and subsequently extracting from the news story the event properties relevant to the event topic to which the news story belongs. Consequently, two news stories are assumed to discuss different events if they are assigned to different event topics, or some of the event properties are different, regardless whether the features in the two news stories are highly similar. On the other hand, two news stories are assumed to discuss the same event if they belong to the same event topic and their event properties are the same or similar. Thus, the first and second problems of traditional feature-based event detection techniques can be solved by performing event detection based on event properties extracted from news stories rather than features appearing in news stories. Since the event topics can serve as the categories for classifying or filtering new news stories, the third problem inherent to traditional event detection techniques can be addressed as well.

Motivating by the need for improving the event detection accuracy and supporting event categorization, the goal of this research is to develop an event detection technique based on the information extraction approach, called information extraction-based event detection (NEED) technique. The proposed technique will empirically be evaluated using a traditional event detection technique as benchmarks. The rest of the paper is organized as follows. Section 2 reviews literatures relevant to this research, including feature-based event detection, text categorization, and information extraction techniques. The development of the information extraction-based event detection (NEED) technique will be depicted in Section 3. An empirical evaluation using news stories collected from a news website will be conducted and summarized in Section 4. Finally, the contributions of this study as well as future research directions will be summarized in Section 5.

## 2. Literature review

This section reviews traditional feature-based event detection techniques. As mentioned, to address the disadvantages of traditional feature-based event detection techniques, we will propose a new event detection technique that employs a text categorization technique and an information extraction method as a basis for event detection. Thus, the literature on text categorization and information extraction will also be summarized in this section.

## 2.1. Feature-based event detection techniques

The objective of event detection is to identify stories in several continuous news streams that pertain to new or previously unidentified events [43]. Event detection is subdivided into two forms: retrospective detection and online detection [4,43,44]. The former entails the discovery of previously unidentified events in a chronologically ordered accumulation of documents (stories), and the latter strives to identify the onset of new events from live news feeds in real time. Both forms of detection intentionally lack prior knowledge of novel events but do have access to unlabeled historical news stories for use as contrast sets.

Most of the proposed event detection algorithms, retrospective or online, were developed based on the document clustering approach. Yang et al. [43,44] implemented two clustering methods for event detection: GAC and INCR. GAC, operating in a strict retrospective detection setting, performs agglomerative clustering for producing hierarchically organized document clusters. GAC employed the conventional vector space model to represent documents and clusters. Each document is represented using a vector of weighted terms, based on the $\mathrm { T F } \times \mathrm { I D F }$ scheme:

$$
w (t, d) = \left(\frac {(1 + \log_ {2} \mathrm{tf} (t , d)) \mathrm{idf} (t)}{\| \overrightarrow {d} \|}\right)\tag{1}
$$

where $w ( t , d )$ is the weight of term t in document $d ,$ tf $[ t , d )$ is the within-document term frequency (TF), ${ \mathrm { i d f } } ( t ) = \log _ { 2 } ( N / n _ { t } )$ is the inverse document frequency (IDF) of term t, N is the number of the training documents used to compute the IDF, $n _ { t }$ is the number of training documents where t appears, and $\| { \overrightarrow { d } } \| =$ $\sqrt { \sum _ { t } w ( t , d ) ^ { 2 } }$ is the two-norm of vector $\stackrel {  } { d . }$

For cluster representation, the normalized vectors of documents in a cluster are summed and the k most significant terms called the prototype or centroid of the cluster are selected to represent the cluster [43,44]. GAC is an agglomerative group-average clustering algorithm that maximizes the average similarity between document pairs in the resulting clusters and merges clusters in a greedy, bottom-up fashion. To improve the computation efficiency and to preserve the characteristics that events tend to appear in news bursts, GAC adopted a divide-and-conquer strategy that grows clusters iteratively. In each iteration, the current pool of clusters is divided according to their order in time into evenly sized buckets. Subsequently, group-average clustering is applied to each bucket locally, merging smaller clusters into larger ones. Periodically, the stories within each of the top-level clusters are reclustered. Reclustering is useful when events straddle the initial temporal-bucket boundaries or when the bucketing causes undesirable groupings of stories about different events.

On the other hand, INCR, designed for both retrospective and online detection, is a single-pass incremental clustering algorithm that produces nonhierarchical clusters incrementally [43,44]. For retrospective detection, the $\mathrm { T F } \times \mathrm { I D F }$ scheme was adopted to represent documents or clusters. However, to deal with the problem of continuously incoming documents that might affect term weighting and vector normalization during online detection, the incremental IDF was employed by INCR:

$$
\operatorname{idf} (t, p) = \log_ {2} \left(\frac {N (p)}{n (t , p)}\right)\tag{2}
$$

where $p$ is the current time point, $N ( p )$ is the number of documents accumulated up to the current point (including the retrospective corpus if used), and $n ( t , ~ p )$ is the document frequency of term t at time $p .$

Moreover, INCR incorporated a time penalty when calculating the similarity between a news document x and any cluster c in the past. The time penalty can be a uniformly weighted time window (i.e., a time window of w documents before x is imposed) or a linear decaying-weight function (shown as below).

$$
\operatorname{sim} (x, c) = \left\{ \begin{array}{l l} \left(1 - \frac {i}{w}\right) \times \operatorname{sim} (x, c) & \text { if   } c \text {   has   any   member   documents   in   the   time   window } \\ 0 & \text { otherwise } \end{array} \right.\tag{3}
$$

where i is the number of news documents between x and the most recent member document in c and w is the time window measured in number of documents before x.

For retrospective detection, INCR sequentially processes news documents. A document is absorbed by the most similar cluster in the past if the similarity between the document and the cluster is greater than a preselected clustering threshold $( t _ { \mathrm { c } } ) ;$ ; otherwise, the document becomes the seed of a new cluster. For online detection, the novelty threshold $\left( t _ { \mathrm { n } } \right)$ was introduced. If the maximal similarity between the current document and any cluster in the past is no less than $t _ { \mathrm { n } } ,$ the document is flagged as containing an old event.

## 2.2. Text categorization

Text categorization refers to the assignment of textual documents, on the basis of their contents, to one or more predefined categories [5,14,16,42]. Central to text categorization is automatic learning of text categorization patterns, based on a set of preclassified training documents. Broadly, automatic learning of text categorization patterns is comprised of three main phases [5,37]: feature extraction and selection, document representation, and induction.

The feature extraction and selection phase is undertaken to determine one or multiple feature sets (referred to as the universal dictionary or local dictionaries) that will be used for representing the training documents. The universal dictionary is created for all categories, while each local dictionary is created for a particular category. Typically, feature extraction commences with the parsing of each training document to produce a list of nouns or noun phrases commonly referred to as features. In most cases, features exclude a set of specified stop words that are nonsemantic bearing words. After feature extraction, feature selection is initiated to condense the size of the universal dictionary or each local dictionary, a process that not only improves learning efficiency, but also increases the learning effectiveness [16]. Several feature selection methods have been proposed in the literature [16,22,24,29,33,34], including TF, $\mathrm { T F } \times \mathrm { I D F } ,$ correlation coefficient, mutual information, and $\chi ^ { 2 }$ metric. The top k features with the highest feature selection metric score are selected as features for representing documents.

In the document representation phase, each training document is represented using the features in the dictionary (universal or local) generated in the previous phase and is labeled to indicate its category membership. A document is assigned a value for each feature in the dictionary of choice, where the values can be either Boolean (e.g., indicating whether or not the feature appears in the document) or numerical (e.g., frequency of occurrence in the document). Different document representation methods have been proposed [42], including binary, TF, and TF  IDF.

The induction phase is designed to automatically discover text categorization patterns that distinguish categories from one another, based on the set of preclassified training documents. The learning strategies for automatic learning of text categorization patterns can essentially be subdivided into several types, including decision tree induction [38]; decision rule induction [5,13,14]; k-nearest neighbor classification [20,23,25,41]; neural network [29,40]; Naı¨ve

Bayes probabilistic classification [1,6,23,24,27]; and statistical approach [42]. For interested readers, a more detailed summary and empirical comparisons can be found in Ref. [45].

## 2.3. Information extraction

Information extraction is concerned with extracting relevant data from semistructured or unstructured documents and transforming them into structured representations [32]. Information extraction systems do not attempt in-depth understanding of text in documents. Rather, they analyze those portions of documents that contain information relevant to a prespecified template that defines types of information to be extracted. Examples of template representation include case frames consisting of a set of slots [32] and ontologies based on a semantic data model [18].

A key element of an information extraction system is its set of extraction rules used to extract from a document the information relevant to a particular extraction task [28]. Extraction rules are typically based on a combination of syntactic (i.e., syntactic relations between words) and semantic (i.e., semantic classes of words) constraints that help identify the relevant information within a document. For example, extraction rules of WHISK [35] are based on regular expression patterns that identify the context of relevant phrases and the exact delimiters of those phrases. Fig. 1 shows a WHISK rule for extracting the number of bedrooms and price from rental advertisements.

The wildcard ‘‘\*’’ means to skip any number of characters until the next occurrence of the following term in an extraction rule. Digit and Number are special semantic classes that are default to WHISK. Parentheses indicate a phrase to be extracted. The phrase within the first set of parentheses is bound to the slot \$1 in the output portion of the rule, the second to the slot \$2, and so forth. In the rule shown in Fig. 1, the first ‘‘\*’’ means skip over in a rental advertisement any input characters until the first digit immediately followed by the literal ‘BR’ is found. This digit is extracted as the number of bedrooms. The pattern matching continues, finding a literal ‘‘\$’’ immediately followed by a number. This number is then bound to the price slot for the rental case frame.

Extraction rules can be manually coded or generated from training examples by using inductive learning techniques. Several information extraction learning systems have been proposed in the literature. For example, WHISK adopted the top-down induction approach for learning extraction rules [35]. WHISK begins with an empty rule and then extends the rule by adding terms. Terms are added to a rule one at a time until the errors are reduced to zero or a prepruning criterion has been satisfied. The process is repeated until all possible extractions from the training documents are covered, at which time postpruning is conducted to remove insignificant rules to prevent from overfitting. For interested readers, a survey of different information extraction learning systems can be found in Refs. [17,28,35].

## 3. Information extraction-based event detection (NEED) technique

As mentioned, the proposed information extractionbased event detection (NEED) technique employs an information extraction method and a text categorization technique as a basis for event detection. The use of the information extraction turns event detection from feature-based to event property-based. This shift has the potential to improving the event detection accuracy and facilitating subsequent event tracking. On the other hand, the use of text categorization facilitates information extraction at the event topic level and supports event categorization and filtering. Accordingly, the NEED technique comprises two main processes: learning and detection. From a set of news stories with known event topics (called training news stories), the learning process is to induce event categorization patterns that distinguish event topics from one another. When a new news story arrives, the detection process is then applied to identify to which event topic the news story should belong and whether the news story discusses a new event.

## 3.1. Learning process

The learning process of the NEED technique is to induce event categorization patterns from a set of precategorized news documents. As with text categorization techniques reviewed in the previous section, the learning process (as shown in Fig. 2) consists of three steps, including feature extraction and selection, document representation, and induction.

## 3.1.1. Feature extraction and selection

When performing feature extraction, NEED extracts from the training news documents a set of representative features (i.e., nouns and noun phrases) that will be used for representing the training news documents. We adopted the rule-based part-of-speech tagger developed by Brill [7,8] to syntactically tag each word in these news documents. Subsequently, we employed the approach proposed by Voutilainen [36] to implement a noun-phrase parser for extracting noun phrases from each syntactically tagged document. Using the correlation coefficient or $\mathrm { T F } \times \mathrm { I D F }$ feature selection method, multiple (local) dictionaries were constructed, each of which was tailored to a particular event topic. Choice of local dictionaries over a universal dictionary was made primarily because of their effectiveness in retaining representative features of each event topic [5].

## 3.1.2. Document representation

For each event topic, all training news stories are represented by its respective dictionary and are labeled to indicate whether they belong to this event topic. Specifically, we selected the binary and TF schemes as alternative document representation schemes in this study.

## 3.1.3. Induction

The induction step induces for each event topic the event categorization patterns that will be used by the detection process of the NEED technique to categorize future news stories into appropriate event topics. As mentioned in Section 2, several learning strategies for automatic learning of event categorization patterns have been commonly adopted by prior research. In this study, the decision tree and the decision rule induction approaches were adopted as the induction techniques. Specifically, we incorporated C4.5 [30,31] and CN2 [11,12] as alternative induction algorithms in the learning process of the NEED technique. Fig. 3 illustrates a decision tree used to represent the event categorization patterns for the ‘‘Business Merger’’ event topic. For example, as shown in the leftmost path in Fig. 3, if a news story does not contain the feature ‘‘merger’’ but contains the feature ‘‘acquisition,’’ the news story will be assigned to the ‘‘Business Merger’’ event topic.

## 3.2. Detection process

The detection process of the NEED technique is to identify to which event topic a newly arrived news story belongs and to detect whether the news story discusses a new event. To achieve this, the detection process consists of three steps: event topic reasoning, event property extraction, and similarity comparison, as shown in Fig. 4.

![](/api/attachments/9H3BCQMV/fulltext/images/f1af408d4a317a2e565867bf5ccee52c013d95c2db7e8b6125afa3da9c1ea483.jpg)  
Fig. 2. Learning process of NEED technique.

![](/api/attachments/9H3BCQMV/fulltext/images/8629801cd1af278f53242f84c95e0d7845a525ed8b4121d7687c26392030fe18.jpg)  
Fig. 3. Example of event categorization patterns for ‘‘Business Merger’’ event topic.

## 3.2.1. Event topic reasoning

Based on the event categorization patterns induced previously in the learning process, the event topic reasoning step is to categorize the new news story into an appropriate event topic. Each new news story should first be represented by the feature set (i.e., local dictionary) pertaining to each event topic, using either the binary or the TF representation scheme. Accordingly, the reasoning with the event categorization patterns is performed. In this study, we assumed that a news story could belong to at most one event topic. Since the decision on whether the news story belongs to each event topic is made independently, two special cases arise; that is, the news story may be classified into more than one event topics or cannot be classified into any event topic. In the first case, conflict resolution is needed and proceeds as follows. For each event topic with a positive decision, the net support ratio is calculated as the number of training documents that satisfies the condition(s) of the fired rule(s) minus the number of training documents that satisfies the condition(s) but does not satisfy the decision of the fired rule(s), divided by the total number of training documents. For example, suppose a news story $n _ { i }$ can be classified into the event topics A and B, based on the event categorization patterns induced from 20 training documents. For the event topic A, assume that 6 training documents satisfy the condition(s) of the fired rule(s) and none of them has a decision contradicting to the fired rule(s). Furthermore, for the event topic B, assume 7 training documents support the condition(s) of the fired rule(s) but 2 of them do not support the decision of the fired rule(s). Thus, the net support ratio for the event topic A is $( 6 - 0 ) / 2 0 = 0 . 3$ and $( 7 - 2 ) /$ $2 0 = 0 . 2 5$ for the event topic B. As a result, the news story $n _ { i }$ will be classified into the event topic with the highest net support ratio (i.e., the event topic A in this example).

![](/api/attachments/9H3BCQMV/fulltext/images/b241cc11ecb117bdc4565ae8649e50c2c0b59bdbf51b98eb96e85c422871e7fd.jpg)  
Fig. 4. Detection process of NEED technique.

In the second case when the new news story cannot be classified into any event topics, the detection process of the NEED technique could stop further processing and suggest that this news story is not belonging to any known event topics. Alternatively, the detection process could consider the event topic for this news story undecided. In this view, this news story will be processed in every event topic in subsequent steps, and the decision on whether this news story contains an unseen event will be made across all event topics (to be detailed later).

## 3.2.2. Event property extraction

Once the new news story is classified into an event topic, the event property extraction step commences to create an event instantiation by extracting event properties from the news story based on the event ontology associated with the event topic. If the event topic for the news story is undecided in the previous step, an event instantiation for the news story will be created for every event topic. As with an information extraction system described in Section 2.3, each event ontology consists of a template defining event properties to be extracted and a set of extraction rules defining how event properties are extracted from a news document. In this study, a knowledge-engineerdriven approach was taken to specify an event ontology for each event topic. Accordingly, for the described event property extraction, we adopted the ontology-based information extraction system proposed by Embley et al. [18].

## 3.2.3. Similarity comparison

To determine whether the new news story discusses a new event, the news story needs to compare with each known event (consisting of a set of past news stories) in the event topic to which the news story is assigned. With its event property-based event detection nature, the NEED technique compares the event instantiation of the new news story with the event instantiations of each known event in the target event topic. Specifically, we defined and measured the similarity between the new news story s and a known event e as follows:

$$
\operatorname{sim} (s, e) = \frac {\sum_ {f = 1} ^ {p} \left[ \delta^ {(f)} \underset {\forall I _ {k} \in \mathrm{EI}} {\text { MAX }} (\operatorname{sim} (\mathrm{SI} ^ {(f)} , I _ {k} ^ {(f)})) \right]}{\sum_ {f = 1} ^ {p} \delta^ {(f)}}\tag{4}
$$

where SI is the event instantiation of the new news story s, EI is the set of event instantiations pertaining to the event $e , p$ is the number of slots in the template of the event topic under discussion, $\delta ^ { ( f ) } = 1$ if both the f th slot in SI and the f th slot of some $I _ { k }$ in EI contain nonmissing values, otherwise, $\delta ^ { ( f ) } = 0 .$ , and $\mathrm { s i m } ( \mathrm { S I } ^ { ( f ) } , I _ { k } ^ { ( f ) } )$ is the similarity between the f th slot of SI and that of $\mathrm { \Delta } Y _ { k } .$

For each slot in the template of the event topic under discussion, the event instantiation SI of the new news story s is compared to every event instantiation $I _ { k }$ belonging to a known event e. For each slot, the maximal similarity between SI and all $I _ { k }$ is obtained as the contribution of the slot to the overall similarity between s and e. If the fth slot is of the numeric type, $\mathrm { s i m } ( \mathrm { S I } ^ { ( f ) } , I _ { k } ^ { ( f ) } ) = 1$ when $\mathrm { S I } ^ { ( f ) } { = } I _ { k } ^ { ( f ) } ;$ otherwise, it is 0. On the other hand, if the fth slot is of the character string type, sim $( \mathrm { S I } ^ { ( f ) } , I _ { k } ^ { ( f ) } ) = \lvert$ Amatched<sub></sub>substring $( \mathrm { S I } ^ { ( f ) } , I _ { k } ^ { ( f ) } ) \vert / \mathrm { M A X } ( \vert \mathrm { S I } ^ { ( f ) } \vert , \vert I _ { k } ^ { ( f ) } \vert )$ where matched<sup>\_</sup> substring $( \mathrm { { S I } } ^ { ( f ) } , I _ { k } ^ { ( f ) } )$ is the maximal matched substring between $\operatorname { S I } ^ { ( f ) }$ and $I _ { k } ^ { ( f ) }$ . If the event instantiation of the new story $s \ ( \mathrm { i . e . , \ S I } )$ or all event instantiations of the event e (i.e., EI) contain missing values in a slot, this slot will be ignored from the described similarity calculation. Furthermore, if all slots are ignored $( \mathrm { i . e . , } \sum _ { f = 1 } ^ { p }$ $\delta ^ { ( f ) } = 0 )$ , the similarity between s and e is set to 0.

To illustrate use of the described similarity between a new news story and a known event, consider the following example. Assume the event topic be software release. Let the template pertaining to this event topic consist of two slots, namely software name and release version. Table 1 summarizes the event instantiations of a new news story s and four past news stories discussing two softwarerelease events. As noted, the event instantiation of the new news story s contains ‘‘Microsoft Internet Explorer’’ as the name of software newly released and 6 as the release version. The event instantiation for the past news story $n _ { 1 2 }$ includes ‘‘Internet Explorer’’ as the name of the new software, but its release version is unknown or could not be extracted from this news story.

Table 1  
Examples of event instantiations

<table><tr><td rowspan="2" colspan="2">Event/news story</td><td colspan="2">Event instantiation</td></tr><tr><td>Software name</td><td>Release version</td></tr><tr><td rowspan="2">New news story</td><td rowspan="2">s</td><td>Microsoft</td><td>6</td></tr><tr><td>Internet Explorer</td><td></td></tr><tr><td rowspan="2">Event  $e_{1}$ </td><td>News story  $n_{11}$ </td><td>IExplorer</td><td>6</td></tr><tr><td>News story  $n_{12}$ </td><td>Internet Explorer</td><td>null</td></tr><tr><td rowspan="2">Event  $e_{2}$ </td><td>News story  $n_{21}$ </td><td>Microsoft Office</td><td>null</td></tr><tr><td>News story  $n_{22}$ </td><td>Microsoft Office</td><td>null</td></tr></table>

The similarity between the new news story s and the event $e _ { 1 }$ is derived as follows. For the first slot (i.e., software name), the maximal matched substring between the event instantiations $\mathrm { S I } ^ { ( 1 ) }$ and $I _ { 1 1 } ^ { ( 1 ) }$ of s and $n _ { \mathrm { 1 1 } } .$ , respectively, is ‘‘Explorer’’, making sim(SI<sup>(1)</sup>, $I _ { 1 1 } ^ { ( 1 ) } ) = 8 / 2 7$ , where 27 is the maximal length of $\mathrm { S I } ^ { ( 1 ) }$ and $I _ { 1 1 } ^ { ( 1 ) }$ . On the other hand, $( \mathrm { S I } ^ { ( 1 ) } , I _ { 1 2 } ^ { ( 1 ) } ) { = } \bar { 1 } 7 / 2 7$ since the maximal matched substring between $\mathrm { S I } ^ { ( 1 ) }$ and $I _ { 1 2 } ^ { ( 1 ) }$ is ‘‘Internet Explorer’’. Hence, the contribution of the first slot to the overall similarity between s and $e _ { 1 }$ is 17/ 27, i.e., the maximum of 8/27 and 17/27. For the second slot (i.e., release version), $\sin ( \mathrm { S I } ^ { ( 2 ) } , \ I _ { 1 1 } ^ { ( 2 ) } ) = 1$ since the two instantiations contain identical release version, while $\mathrm { s i m } ( \mathrm { S I } ^ { ( 2 ) } , I _ { 1 2 } ^ { ( 2 ) } )$ will be ignored since $I _ { 1 2 } ^ { ( 2 ) }$ contains a null value in this slot. Thus, the contribution of the second slot to the similarity between s and $e _ { 1 }$ is 1. Accordingly, the overall similarity between s and $e _ { 1 }$ is the average of the contributions from the two slots, i.e., $( 1 7 / 2 7 + 1 ) / 2 = 0 . 8 1 4 8$ . The similarity between s and $e _ { 2 }$ is derived similarly. sim $( \mathrm { S I } ^ { ( 1 ) } , I _ { 2 1 } ^ { ( 1 ) } ) { = } 9 / 2 7$ since the maximal matched substring between the event instantiations $\mathrm { S I } ^ { ( 1 ) }$ and $I _ { 2 1 } ^ { ( 1 ) }$ (or $\overset { - } { I } _ { 2 2 } ^ { ( 1 ) } )$ is ‘‘Microsoft’’, while the second slot will be ignored since all of the event instantiations of $e _ { 2 }$ contain null values in this slot. Thus, the overall similarity between s and $e _ { 2 }$ is 9/ $2 7 = 0 . 3 3 3 3$ , i.e., the contribution of the software name slot only.

As with traditional feature-based event detection techniques, a linear decaying-weight similarity function was employed by the NEED technique to preserve the tendency that events appear in news bursts. Accordingly,

$$
\operatorname{sim} (s, e) = \left\{ \begin{array}{l l} \left(1 - \frac {i}{w}\right) \times \operatorname{sim} (s, e) & \text { if   the   event   } e \text {   has   any   news   story   in   the   time   window } \\ 0 & \text { otherwise } \end{array} \right.\tag{5}
$$

where i is the time gap measured in the number of days between the new news story s and the most recent news story of the event e and w is the time window measured in days prior to s.

Upon obtaining the similarities between the new news story s and all of the known events in the event topic to which s is assigned, the NEED technique labels s as containing a new event if the maximal similarity between s and the known events in the target event topic is below a prespecified novelty threshold $( t _ { n } ) ;$ ; otherwise, s is labeled as containing an old event. As mentioned, if the event topic for s is undecided in the event topic reasoning step, an event instantiation will be created in every event topic for s. Thus, the NEED technique labels s as a new event if the maximal similarity between s and the known events in all event topics is below the novelty threshold; otherwise, s is flagged as an old event. In the latter case, s will be assigned to the event topic where the maximal similarity is attained.

Finally, the event instantiation of s is stored in Event Instantiation Base for future event detection use. If s is identified as discussing an old event, its event instantiation is absorbed by the event to which s is associated; otherwise, it forms an event on its own.

## 4. Empirical evaluation

This section reports the empirical evaluation of the proposed NEED technique, using a traditional featurebased event detection technique as performance benchmarks. News stories from November 1999 to December 1999 were collected from a news website, http://excite.com. Five event topics were identified and selected, including airplane crash, adjustment of interest rate, business merger, business partnership, and computer virus. About 492 news stories (where 244 news from November 1999 and 248 news from

Table 3  
Table 2  
Summary of data corpus

<table><tr><td>Event topic</td><td>Number of events</td><td>Number of news stories</td><td>Average number of words per news story</td></tr><tr><td>Airplane crash</td><td>15</td><td>65 (53/12)a</td><td>616</td></tr><tr><td>Adjustment of interest rate</td><td>12</td><td>26 (16/10)</td><td>569</td></tr><tr><td>Business merger</td><td>173</td><td>245 (115/130)</td><td>527</td></tr><tr><td>Businesses partnership</td><td>78</td><td>86 (33/53)</td><td>563</td></tr><tr><td>Computer virus</td><td>11</td><td>70 (27/43)</td><td>486</td></tr><tr><td>Total</td><td>289</td><td>492 (244/248)</td><td>552</td></tr></table>

<sup>a</sup> (53/12) denotes 53 news stories from November 1999 and 12 from December 1999.

December 1999) pertaining to the five event topics were manually identified. The event contained in each news story was also coded manually. The summary of the data corpus is provided in Table 2. Furthermore, the event ontology (including the template and extraction rules) for each event topic, as required by the NEED technique, was engineered manually rather than generated by an inductive learning technique in this study. The summary of the event ontologies used in this empirical evaluation is summarized in Table 3.

## 4.1. Evaluation criteria

The effectiveness of an event detection technique is measured by miss and false alarm rates. The miss rate is defined as the percentage of that an event detection technique fails to detect a new event, while the false alarm rate is defined as the percentage of that an event detection technique fails to detect an old event. To address the inevitable tradeoffs between miss and false alarm rates, Detection Error Tradeoff (DET) curves were employed [4,43,44]. An event detection technique with its DET curve closer to the origin would be more desirable. In the context of supporting environmental scanning, a low miss rate may improve an organization’s responsiveness to the changes of its external environment and therefore can enhance the organization’s adaptability to its environment. On the other hand, an improvement in the false alarm rate reduces an organization’s load in filtering news stories containing known events. Because of ever-increasing complexity and dynamics of an organization’s environment, responsiveness and adaptability of the organization clearly are more essential than efficiency of environmental scanning. In this light, event detection should aim at achieving the lowest attainable miss rate while maintaining false alarm rate at a satisfactory level.

## 4.2. Performance benchmarks

A traditional feature-based event detection technique was used to provide the desired effectiveness benchmarks. Specifically, the single-pass incremental clustering (INCR) for event detection proposed by Yang et al. [43,44] was employed. Without loss of generality, we modified its linear decaying-weight similarity function by changing the time window from the number of news stories to the number of days, as follows:

$$
\operatorname{sim} (x, c) = \left\{ \begin{array}{l l} \left(1 - \frac {i}{w}\right) \times \operatorname{sim} (x, c) & \text { if   } c \text {   has   any   member   documents   in   the   time   window } \\ 0 & \text { otherwise } \end{array} \right.\tag{6}
$$

where i is the number of days between x and the most recent document in c and w is the time window measured in number of days before x.

## 4.3. Parameter tuning experiments for INCR

The INCR technique involves three parameters: the number of features $k ,$ time window w, and novelty threshold $t _ { n } .$ . In this study, the news stories of November 1999 were employed as the data set for parameter tuning. Specifically, the news stories from the first 15 days in this tuning set were used as historical news stories, while the rest of news stories in the tuning set were included as the testing set. To detect whether a news story in the testing set contained a new event by using the INCR technique, the news story was compared to all of its prior news stories (including historical ones). To expand the number of trials, 70% of the news stories were randomly selected from the historical and testing sets, respectively, and the random selectionand-detection process was repeated 10 times. Thus, the overall detection effectiveness was estimated by averaging the performance across all iterations.

Summary of event ontologies

<table><tr><td>Event topic</td><td>Number of slots</td><td>Number of extraction rules</td></tr><tr><td>Airplane crash</td><td>2</td><td>9</td></tr><tr><td>Adjustment of interest rate</td><td>2</td><td>10</td></tr><tr><td>Business merger</td><td>2</td><td>18</td></tr><tr><td>Businesses partnership</td><td>2</td><td>18</td></tr><tr><td>Computer virus</td><td>1</td><td>7</td></tr></table>

We investigated the number of features k ranging from 50 to infinite $( k \small = 5 0 , 1 0 0 , 1 5 0 , 2 0 0$ , and infinite), the time window w ranging from 7 to 60 $( w = 7 , 1 4 , 3 0 ,$ and 60 days), and the novelty threshold $t _ { n }$ ranging from 0.1 to 0.2 at increments of 0.01. Evidently, the increase of the novelty threshold resulted in the decrease of miss rate at the cost of false alarm rate. At any level of w investigated, the Detection Error Tradeoff (DET) curve, in general, was getting closer to the origin as k increased from 50 to infinite (INF). When k = INF, setting w as 7 resulted in the worst detection effectiveness (as shown in Fig. 5). The DET curves for $w = 1 4 ,$ 30, and 60 were comparable when the false alarm rate was lower than 2.5%. However, at any level of false alarm rate that was higher than 2.5%, the DET curves with the time window of 14 and 30 outperformed that with the time window of 60. Over the range of novelty thresholds examined, since the maximal false alarm rate attained by the time window of 30 was much less than that by the time window of 14, w = 30 appeared to be better than others for the INCR technique. When w was 30 and k was infinite, the best performance was achieved at the novelty threshold of 0.18 (where the minimal Euclidean distance to the origin was attained). Thus, we selected the time window of 30 and infinite number of features for the INCR technique.

## 4.4. Parameter tuning experiments for NEED

As discussed, the NEED technique consists of the learning and detection processes. The learning process involved four decisions, including the feature selection method (correlation coefficient or TF  IDF), the number of features k (in this study, we examined k ranging from 50 to 200 at increments of 50), the representation scheme (binary or TF), and the induction algorithm (C4.5 or CN2). As with the tuning experiments for INCR, the news stories of November 1999 were employed as the tuning data set. Specifically, we adopted the tenfold cross-validation technique [39], with which the included news stories were randomly divided into 10 mutually exclusive data subsets of equal size. The learning-and-testing proceeded in an iterative manner. In each learning-and-testing iteration, one data subset was chosen as the testing data and the others were used for learning purpose. Thus, the overall learning performance was estimated by averaging the performance across the 10 iterations.

![](/api/attachments/9H3BCQMV/fulltext/images/db0127892d302ef80d81ca53508e7fb74e77f1fdc17b26256f5e39bd44729679.jpg)  
Fig. 5. Detection error tradeoff curves of INCR (k = infinite).

Table 4  
Average accuracy of event categorization (using CN2 for learning)

<table><tr><td rowspan="2">Feature selection method</td><td rowspan="2">Representation scheme</td><td colspan="4">Number of features (k)</td></tr><tr><td>50</td><td>100</td><td>150</td><td>200</td></tr><tr><td rowspan="2">Correlation coefficient</td><td>Binary</td><td>84.43%</td><td>84.02%</td><td>83.61%</td><td>81.56%</td></tr><tr><td>TF</td><td>84.02%</td><td>85.25%</td><td>85.25%</td><td>85.66%</td></tr><tr><td rowspan="2">TF × IDF</td><td>Binary</td><td>82.38%</td><td>83.20%</td><td>82.79%</td><td>84.02%</td></tr><tr><td>TF</td><td>85.66%</td><td>86.48%</td><td>84.43%</td><td>84.43%</td></tr></table>

As shown in Table 4, when CN2 was used as the induction algorithm, the TF representation outperformed the binary one in event categorization at almost any number of features investigated. However, the effect of number of features on event categorization accuracy was inconclusive, when using CN2 for learning event categorization patterns. In contrast, when C4.5 was employed (as shown in Table 5), the binary representation achieved higher categorization accuracy at almost any number of features examined, and the increment of the number of features generally resulted in lower event categorization accuracy. In general, C4.5 appeared to outperform CN2 in event categorization accuracy. Among all experiments, the combinations of (induction algorithm = C4.5, feature selection = TF  IDF, representation = TF, k = 50) and (induction algorithm = C4.5, feature selection = correlation coefficient, representation = binary, k = 50) achieved the highest categorization accuracy. Thus, in this study, C4.5 with the TF  IDF feature selection method, the TF representation scheme, and the number of features as 50 was adopted as the parameter setting for further experiments.

Once the parameter values for the learning process were selected, tuning experiments for the detection process of the NEED technique were conducted. As mentioned, the detection process involves two parameters: time window w and novelty threshold $t _ { n } .$ The parameter tuning experiment for the NEED technique was designed in the same manner as that for the INCR technique, and the tuning experiment was repeated 10 times. As mentioned, in the NEED technique, to detect whether a news story in the testing set contains a new event, the news story was first assigned to an event topic based on event categorization patterns induced from the historical news stories. As a result, the news story was compared to all news stories (including historical ones) that were prior to and in the same event topic as the target testing news story.

We investigated the time window ranging from 7 to 60 (w = 7, 14, 30, to 60) and the novelty threshold $t _ { n }$ ranging from 0.01 to 1.0 at increments of 0.01. The DET curves of the NEED technique over different w and $t _ { n }$ are shown in Fig. 6. As shown, at any level of false alarm rate that was lower than 10%, the DET curves of the NEED technique generally shifted toward the origin as the time window increased from 7 to 60. On the other hand, when the false alarm rate was higher than 10%, the DET curves of the NEED technique were comparable over different time windows examined. The NEED technique arrived at the best performance when w was 60 and the novelty threshold was 0.48. Thus, we decided on the time window of 60 for the NEED technique.

## 4.5. Comparative evaluation of event detection techniques

The traditional feature-based event detection (INCR) and information extraction-based event detection (NEED) techniques were compared using the parameter values determined in the previous subsections. Similar to the tuning experiments described previously, the data corpus was divided into two sets: historical (including news stories in November 1999) and testing (including news stories in December 1999). Since the NEED technique requires inducing event categorization patterns, the historical data set was also used for the learning purpose. To expand the number of trials, 70% of news stories were randomly selected from the historical and the testing set, respectively, and the random selection process was repeated 30 times. In each trial, the reduced historical set was also employed for inducing event categorization patterns, as required by the NEED technique. The overall detection effectiveness was then estimated by averaging the performance across all trials.

Average accuracy of event categorization (using C4.5 for learning)

<table><tr><td rowspan="2">Feature selection method</td><td rowspan="2">Representation scheme</td><td colspan="4">Number of features (k)</td></tr><tr><td>50</td><td>100</td><td>150</td><td>200</td></tr><tr><td rowspan="2">Correlation coefficient</td><td>Binary</td><td>88.52%</td><td>87.30%</td><td>87.30%</td><td>87.70%</td></tr><tr><td>TF</td><td>85.25%</td><td>84.84%</td><td>84.84%</td><td>84.43%</td></tr><tr><td rowspan="2"> $\text{TF} \times \text{IDF}$ </td><td>Binary</td><td>87.70%</td><td>88.11%</td><td>86.89%</td><td>87.30%</td></tr><tr><td>TF</td><td>88.52%</td><td>88.11%</td><td>86.48%</td><td>86.48%</td></tr></table>

![](/api/attachments/9H3BCQMV/fulltext/images/10db3a1e0aa07ada0b80c8b80af9a9937e39767f264580b5fcf6ed2837e75727.jpg)  
Fig. 6. Detection error tradeoff curves of NEED.

We investigated the novelty threshold $t _ { n }$ for INCR ranging from 0.01 to 0.5 and that for NEED ranging from 0.41 to 1.0 at 0.01 increments. As shown in Fig. 7, at almost any level of false alarm rate that was lower than 45%, the INCR technique achieved lower miss rates than the NEED technique did. However, if a low miss rate was desirable, the NEED technique outperformed its counterpart at almost any level of miss rate lower than 4%. In general, the miss rate achieved by the NEED technique was lower than 12% at any novelty threshold investigated. As mentioned, in the context of supporting environmental scanning, a low miss rate attainable by an event detection technique is more important than a low false alarm rate. Hence, judging from this view, the NEED technique was superior to the INCR technique.

As mentioned, during the event topic reasoning step in the NEED technique, if a news story cannot be classified into any event topic, this news story will be processed in every event topic at the subsequent steps of the detection process. As shown in Fig. 8, the detection effectiveness of the NEED technique on those unclassified news stories was significantly unsatisfactory. If the detection effectiveness of those unclassified news stories was not considered when estimating the overall detection effectiveness of the NEED technique, its DET curve shifted toward the origin and outperformed that of the INCR technique at any level of the novelty threshold investigated. Thus, it can be expected that improvement in the coverage of event topic reasoning in the NEED technique (i.e., reduction in the number of unclassified news stories) will improve the detection effectiveness of the NEED technique.

![](/api/attachments/9H3BCQMV/fulltext/images/53f9026eb82627ed9db46304fc4479d07103523ab0c9b76ea266d9aa518d32fb.jpg)  
Fig. 7. Detection error tradeoff curves of different event detection techniques.

![](/api/attachments/9H3BCQMV/fulltext/images/e866269ece9edc94179fa7bc837aeb1d139787baf0f65893eda8229bcc654859.jpg)  
Fig. 8. Detailed detection error tradeoff curves of NEED technique.

## 5. Conclusions and future research directions

Environmental scanning is an important process of strategic management that permits an organization to adapt to its environment and subsequently to develop effective responses to secure or improve its position in the future. Event detection that detects the onset of new events from news documents is essential to facilitating an organization’s environmental scanning activity. Traditional feature-based event detection techniques detect events by comparing the similarity between features of news stories and incur several problems. For example, as a feature-based approach, traditional event detection techniques greatly suffer from the word mismatch and inconsistent orientation problems and do not directly support event categorization and news stories filtering. In this study, we developed an information extractionbased event detection (NEED) technique that combines text categorization and information extraction techniques to address the problems inherent to traditional feature-based event detection techniques. Using a traditional feature-based event detection technique (i.e., INCR) as benchmarks, the empirical evaluation results showed that the proposed NEED technique improved the effectiveness of event detection measured by the tradeoff between miss and false alarm rates. As an information extraction-based approach, our technique (i.e., NEED) requires a prespecified set of event topics as well as an event ontology (consisting of a template defining event properties to be extracted and a set of extraction rules defining how event properties are extracted from news documents) for each event topic. In the context of supporting environmental scanning, it is justifiable to assume that event topics to be detected and their associated templates can be predetermined. Therefore, the proposed NEED technique is adequate for supporting event detection needed by environmental scanning, but may not be equally effective for facilitating general event detection tasks.

Some future research works related to this study should be continued. In this study, C4.5 and CN2 were employed as alternative induction methods for learning event categorization patterns. As discussed previously, improvements in the coverage of event topic reasoning would enhance the resulting detection effectiveness of the NEED technique. Thus, it would be essential to adopting and evaluating other learning strategies (e.g., k-nearest neighbor classification, neural network, Naı¨ve Bayes probabilistic classification, etc.) for the target learning and reasoning requirements of the NEED technique. On the other hand, the detection effectiveness of the NEED technique would be based on accurate and complete extraction rules for each event topic. However, the manual engineering of extraction rules is often time-consuming and errorprone. Thus, a mechanism for learning extraction rules for each event topic is essential to the NEED technique. Furthermore, in this study, the experimental data set used to evaluate the NEED technique only comprised news stories of five event topics across 2 months. A larger data set with more news stories and event topics for empirical evaluation of the proposed technique is desirable. The lexical and temporal similarity function was employed in the NEED technique. However, the incorporation of domain knowledge has the great potential to improving the detection effectiveness of the proposed technique. For example, two event property values, ‘‘IBM’’ and ‘‘International Business Machine’’, will be evaluated as completely different ones by the similarity function currently employed in this study. However, with the inclusion of domain knowledge (e.g., a company name may exist in an acronym form) in the similarity function, ‘‘IBM‘‘ and ‘‘International Business Machine’’ could correctly be evaluated as equivalent. Finally, in this study, we focused only on event detection for supporting environmental scanning. The development of an appropriate event tracking method based on the proposed NEED technique would be desirable to supporting another challenging task in organizational scanning of external environments.

## Acknowledgements

This work was supported by National Science Council of the Republic of China under the grant NSC 89-2416-H-110-095.

## References

[1] R. Agrawal, R. Bayardo, R. Srikant, Athena: mining-based interactive management of text databases, Proceedings of the Seventh Conference on Extending Database Technology, Konztanz, Germany, Springer, 2000, pp. 365–379.

[2] F.J. Aguilar, Scanning the Business Environment, Macmillan Publisher, New York, 1967.

[3] N. Ahituv, J. Zif, I. Machlin, Environmental scanning and information systems in relation to success in introducing new products, Information and Management 33 (1998) 201 – 211.

[4] J. Allan, R. Papka, V. Lavrenko, Online new event detection and tracking, Proceedings of 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Melbourne, Australia, 1998, pp. 37 – 45.

[5] C. Apte´, F. Damerau, S. Weiss, Automated learning of decision rules for text categorization, ACM Transactions on Information Systems 12 (3) (1994) 233– 251.

[6] L.D. Baker, A.K. McCallum, Distributed clustering of words for text categorization, Proceedings of 21st International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Melbourne, Australia, 1998, pp. 96 – 103.

[7] E. Brill, A simple rule-based part of speech tagger, Proceedings of the Third Conference on Applied Natural Language Processing, Association for Computational Linguistics, Trento, Italy, 1992, pp. 152 – 155.

[8] E. Brill, Some advances in rule-based part of speech tagging, Proceedings of the Twelfth National Conference on Artificial Intelligence, AAAI Press, Seattle, WA, 1994, pp. 722 – 727.

[9] C.W. Choo, Information Management for the Intelligent Organization: The Art of Scanning the Environment, 2nd ed., Information Today, Medford, NJ, 1998.

[10] C.W. Choo, The art of scanning the environment, Bulletin of the American Society for Information Science (1999) 21 – 24.

[11] P. Clark, T. Niblett, The CN2 induction algorithm, Machine Learning 3 (4) (1989) 261 – 283.

[12] P. Clark, R. Boswell, Rule induction with CN2: some recent improvements, Proceedings of the 5th European Conference (EWSL ’91), 1991, pp. 151–163.

[13] W.W. Cohen, Y. Singer, Context-sensitive learning methods for text categorization, Proceedings of the 19th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Zurich, Switzerland, 1996 August, pp. 307–315.

[14] W.W. Cohen, Y. Singer, Context-sensitive learning methods for text categorization, ACM Transactions on Information Systems 17 (2) (1999 April) 141 – 173.

[15] R.L. Daft, J. Sormunen, D. Parks, Chief executive scanning, environmental characteristics and firm performance: an empirical study, Strategic Management Journal 9 (1988) 123 – 139.

[16] S. Dumais, J. Platt, D. Heckerman, M. Sahami, Inductive learning algorithms and representations for text categorization, Proceedings of the 7th International Conference on Information and Knowledge Management, ACM Press, Bethesda, MD, 1998, pp. 148 – 155.

[17] L. Eikvil, Information Extraction from World Wide Web: A Survey, Norwegian Computer Center, Report No. 945, 1999 July.

[18] D.W. Embley, D.M. Campbell, R.D. Smith, Ontology-based extraction and structuring of information from data-rich unstructured documents, Proceedings of 7th International Conference on Information and Knowledge Management, ACM Press, Bethesda, MD, 1998, pp. 52 – 59.

[19] D.C. Hambrick, Specialization of environmental scanning activities among upper level executives, Journal of Management Studies 18 (1981) 299– 320.

[20] M. Iwayama, T. Tokunaga, Cluster-based text categorization: a comparison of category search strategies, Proceedings of 18th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Seattle, WA, 1995, pp. 273– 281.

[21] D. Jennings, J. Lumpkin, Insights between environmental scanning activities and porter’s generic strategies: an empirical analysis, Journal of Management 18 (4) (1992) 791 – 803.

[22] W. Lam, C.Y. Ho, Using a generalized instance set for automatic text categorization, Proceedings of the 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Melbourne, Australia, 1998, pp. 81–89.

[23] L. Larkey, W. Croft, Combining classifiers in text categorization, Proceedings of the 19th Annual International ACM SIGIR Conference on Research and Development in Information Re trieval, ACM Press, Zurich, Switzerland, 1996, pp. 289 – 297.

[24] D. Lewis, M. Ringuette, A comparison of two learning algorithms for text categorization, Proceedings of Symposium on Document Analysis and Information Retrieval, UNLV Publications/Reprographics, Las Vegas, NE, 1994, pp. 81 – 93.

[25] B. Masand, G. Linoff, D. Waltz, Classifying news stories using memory based reasoning, Proceedings of the 15th Annual International ACM SIGIR Conference on Research and De velopment in Information Retrieval, ACM Press, Copenhagen, Denmark, 1992, pp. 59 – 64.

[26] P. Mayeux, Broadcast News: Writing and Reporting, 2nd ed., Brown & Benchmark Publishers, Guilford, CT, 1996.

[27] A.K. McCallum, K. Nigam, A comparison of event models for naı¨ve Bayes text classification, Proceedings of AAAI-98 Workshop on Learning for Text Categorization, 1998.

[28] I. Muslea, Extraction patterns for information extraction tasks: a survey, Proceedings of AAAI-99 Workshop on Machine Learning for Information Extraction, American Association for Artificial Intelligence, Orlando, FL, 1999, pp. 1 – 6.

[29] H.T. Ng, W.B. Goh, K.L. Low, Feature selection, perception learning, and a usability case study for text categorization, Proceedings of Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Philadelphia, PA, 1997, pp. 67– 73.

[30] J.R. Quinlan, Induction of decision trees, Machine Learning 1 (1986) 81 – 106.

[31] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993.

[32] E. Riloff, W. Lehnert, Information extraction as a basis for high-precision text classification, ACM Transactions on Information Systems 12 (3) (1994 July) 296 – 333.

[33] H. Schutze, D.A. Hull, J.O. Pedersen, A comparison of classifiers and document representations for the routing problem, Proceedings of 18th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Seattle, WA, 1995, pp. 229– 237.

[34] F. Smadja, K.R. Mckeown, V. Hatzivassilogou, Translating collocations for bilingual lexicons: a statistical approach, Computational Linguistics 22 (1) (1996 March) 1 – 38.

[35] S. Soderland, Learning information extraction rules for semistructured and free text, Machine Learning 34 (1999) 233 – 272.

[36] A. Voutilainen, Nptool: a detector of English noun phrases, Proceedings of Workshop on Very Large Corpora, Columbus, OH, 1993 June, pp. 48 – 57.

[37] C. Wei, P. Hu, Y.X. Dong, Managing document categories in e-commerce environments: an evolution-based approach,

European Journal of Information Systems 11 (3) (2002 September) 208–222.

[38] S.M. Weiss, C. Apte, F.J. Damerau, D.E. Johnson, F.J. Oles, T. Goetz, T. Hampp, Maximizing text-mining performance, IEEE Intelligent Systems, (1999 July/August) 63– 69.

[39] S.M. Weiss, C.A. Kulikowski, Computer Systems that Learn: Classification and Predication Methods from Statistics, Neural Nets, Machine Learning, and Expert Systems, Morgan Kaufmann, San Mateo, CA, 1991.

[40] W. Wiener, J.O. Pedersen, A.S. Weigend, A Neural Network Approach to Topic Spotting, Proceedings of the 4th Annual Symposium on Document Analysis and Information Retrieval, ACM Press, Las Vegas, NE, 1995, pp. 317– 332.

[41] Y. Yang, Expert network: effective and efficient learning from human decisions in text categorization and retrieval, Proceedings of the 17th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Dublin, Ireland, 1994, pp. 13– 22.

[42] Y. Yang, C.G. Chute, An example-based mapping method for text categorization and retrieval, ACM Transactions on Information Systems 12 (3) (1994) 252 – 277.

[43] Y. Yang, T. Pierce, J.G. Carbonell, A study on retrospective and on-line event detection, Proceedings of 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Melbourne, Australia, 1998, pp. 28– 36.

[44] Y. Yang, J.G. Carbonell, R.D. Brown, T. Pierce, B.T. Archibald, X. Liu, Learning approaches for detecting and tracking news events, IEEE Intelligent Systems 14 (4) (1999 July/ August) 32 – 43.

[45] Y. Yang, X. Liu, A re-examination of text categorization methods, Proceedings of 22nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM Press, Berkeley, CA, 1999, pp. 42 – 49.

![](/api/attachments/9H3BCQMV/fulltext/images/e92270ed3ab8d04c48720f0313b3b0b3709776ab071da910580746f6c94025ce.jpg)

Chih-Ping Wei received a BS in Management Science from the National Chiao-Tung University in Taiwan, ROC in 1987 and an MS and a PhD in Management Information Systems from the University of Arizona in 1991 and 1996. He is currently a professor of Department of Information Management at National Sun Yat-Sen University in Taiwan, ROC and was a visiting scholar at the University of Illinois at Urbana-Champaign in 2001. His papers

have appeared in IEEE Transactions on Engineering Management, IEEE Software, IEEE Intelligent Systems, IEEE Transactions on Information Technology in Biomedicine, Decision Support Systems, European Journal of Information Systems, Expert Systems with Applications, Journal of Organizational Computing and Electronic Commerce, etc. His current research interests include knowledge discovery and data mining, information retrieval and text mining, knowledge management, multidatabase management and integration, and data warehouse design. He is a member of the ACM and IEEE.

![](/api/attachments/9H3BCQMV/fulltext/images/f24c28c9f93659f05a8f1b21381857748d1818df5c46932e8abe850f09f5d489.jpg)

Yen-Hsien Lee received a BS and an MBA in Information Management from the National Sun Yat-Sen University in Taiwan, ROC in 1998 and 2000. He is currently a PhD candidate of Department of Information Management at National Sun Yat-Sen University in Taiwan, ROC and a visiting scholar at the University of Utah. His papers have appeared (including forthcoming) in Decision Support Systems, Expert Systems with Applications, etc. His current research

interests include knowledge discovery and data mining, knowledge management, information retrieval and text mining, and web mining.
