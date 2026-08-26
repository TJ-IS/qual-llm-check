---
otero_id: 1076
otero_key: "BRN9TRGG"
title: "Storyline-based summarization for news topic retrospection"
authors: "Fu-ren Lin; Chia-Hao Liang"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.06.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Storyline-based summarization for news topic retrospection

Fu-ren Lin <sup>a,⁎</sup>, Chia-Hao Liang <sup>b</sup>

<sup>a</sup> Institute of Technology Management National Tsing Hua University, Hsinchu City, Taiwan 300, ROC <sup>b</sup> Department of Information Management National Sun Yat-sen University, Kaohsiung City, Taiwan 804, ROC

Available online 23 June 2007

## Abstract

Electronics newspapers gradually become main sources for news readers. When facing the numerous reports on a series of events in a topic, a summary of stories from news reports will benefit news readers in reviewing the news topic efficiently. Besides identifying events and presenting news titles and keywords the TDT (Topic Detection and Tracking) techniques are used to do, a summarized text to present event evolution is necessary for general news readers to review events under a news topic. This paper proposes a topic retrospection process and implements the SToRe (Story-line based Topic Retrospection) system that identifies various events under a news topic, and composes a summary that news readers can get the sketch of event evolution in the topic. It consists of three main functions: event identification, main storyline construction and storyline-based summarization. The constructed main storyline can remove the irrelevant events and present a main theme. The storyline-based summarization extracts the representative sentences and takes the main theme as the template to compose the summary. The storyline summary not only provides readers enough information to understand the development of a news topic, but also serves as an index for readers to search corresponding news reports. Following a design science paradigm, a lab experiment is conducted to evaluate the SToRe system in the question-and-answer (Q&A) setting. The experimental results show that SToRe enables news readers to effectively and efficiently capture the evolution of a news topic. © 2007 Elsevier B V All rights reserved

Keywords: Topic retrospection; Topic detection and tracking (TDT); Event threading; Summarization

## 1. Introduction

The prevalence of Internet technologies (e.g., World Wide Web, P2P network) and innovative applications (e.g., Weblog, electronic newspaper), diversifies the information aggregation and dissemination. Online news spreads across Internet due to its responsiveness and customization features. Information regarding events occurred around the world can be known via these channels. People may keep track of the development of news topics for individual or institutional interests. For example, for a company in an industry, it is beneficial to keep eye on news reports of its partners and competitors to gain its competitive intelligence. However, the amount of information which people can efficiently and effectively process is limited. Many techniques have been developed to ease this cognitive load, such as search engines (information retrieval), automated categorization, clustering, and recommendation [5,7,13,47].

Some news media may collect related events under a news topic to ease news readers' search efforts. For example, in Taiwan, most of news databases provide the function of the clipping folder system (http://udndata. com/ndapp/specialtopic/StIndex) that collects related events in a news topic by professional reporters. News readers can query news by accessing news databases, and edit individual clipboards. Even with those easy-to-query and personal clips, online news readers still face the information overloading problem. As the time passes by, people gradually forget events which occurred related to a specific topic, including what the most important event is, how it starts, and its turning point and consequence.

Information overloading is not only associated with the quantity of information, but also with information format and quality [19]. Search engines, although fast and comprehensive, only present their results as lists of hits that a user needs to read through to differentiate relevant from irrelevant information. Search engines contribute to the dimension of information quantity. To face constituently evolving news events, topic detection and tracking (TDT) techniques have been developed to group news reports on related events together in a topic and keep track of future events corresponding to the topic. Mechanisms developed in TDT research enable news readers to identify clustered news sets. However, most of researches merely present a list of news reports, and ignore the information presentation.

Existing TDT techniques and systems usually present an event in a topic as a cluster of news reports using clustering techniques. For people to review events occurred long time ago, it takes a great effort to pick an anchor report in the cluster as the entry point to cognitively recognize events. It is also a cognitively expensive and time consuming for readers to comprehend the evolution of the news topic. A better information presentation may ease such cognitive load and facilitate readers to quickly capture the theme of a news topic.

The efficiency and effectiveness of recalling occurred events in a topic from news reports demand a news topic retrospection mechanism. The retrospection mechanism may possess the capability of releasing news readers' cognitive loading in articulating occurred events and presenting a logical sequence of news stories in a summary. Therefore, a news reader can submit a set of topic terms into the news topic retrospection system, and obtain a storyline summary of news events of the topic. For example, Carly Fiorina, former chairman and chief executive officer of Hewlett-Packard Co. Ltd. has agreed to serve as an independent member on the board of directors of leading foundry Taiwan Semiconductor Manufacturing Co. Ltd. This news was publicized on April 6, 2006. People tend to recall the HP's acquisition of Compaq occurred in 2001-2002 while reading news reports related to Carly Fiorina. However, it would be a great effort for them to obtain a comprehensive view of the series of events occurred during the acquisition process. Therefore, a storyline summary will facilitate readers to recall events of this acquisition case.

This paper proposes a topic retrospection mechanism that demonstrates the story telling capability for news readers to understand the context of topic development in an efficient way. The implemented SToRe (Storylinebased Topic Retrospection) system consists of three main functions: event identification, main storyline construction and storyline-based summarization. It identifies events and their relations under a news topic and then composes a storyline summary which gives readers the sketch of event evolution in the topic. The main storyline construction removes irrelevant events and presents a main theme that exhibits the sequence of events in a news topic. The storyline-based summarization does not only provide abstract information to highlight events occurred in a news topic, but also serves as an index to facilitate readers to read corresponding news reports. News readers may gain general perspectives prior to reading news articles.

A lab experiment is conducted to evaluate the SToRe system in the question-and-answer (Q&A) setting. The experimental results demonstrate that SToRe can help news readers effectively and efficiently capture the evolution of a news topic, and in turn, reduce their cognitive loads. Therefore, once the topic retrospection system is successfully implemented, it will grant the story telling capability for news readers to understand the context of topic development, and in turn, reduce information loading. As more companies spend their efforts on gaining competitive intelligence from public available information, such as news reports, blogs, etc., the needs of concisely summarizing information and articulating in a meaningful sequence increase. The insights brought from the experimental results of adopting the proposed event retrospection mechanism study shed light on the future development of competitive intelligence systems.

This paper is organized as follows after briefly introducing research motivations and highlighting the theme of this study. Section 2 reviews techniques related to the retrospection mechanism proposed in this study. Section 3 presents the SToRe architecture. An experiment to evaluate SToRe's efficiency and effectiveness on the storyline summarization using the news topic on HP's acquisition of Compaq is designed in Section 4. Section 5 summarizes and discusses the experimental results. Section 6 concludes this study with suggestions for future research.

## 2. Related works

The topic retrospection with summarization integrates techniques from machine learning and text mining researches, such as topic detection and tracking, selforganizing map, event threading and text summarization.

## 2.1. Topic detection and tracking

Topic Detection and Tracking (TDT) research aims to provide a variety of automatic techniques for discovering and threading together topically related materials in streams of data such as newswire and broadcast news. In TDT study, a topic is defined to be a seminal event or activity, along with all directly related events and activities [15]. Further, an event is defined as something (non-trivial) that happens at a particular time and place [1]. TDT integrates the research of information retrieval, information management and data mining to devise powerful, broadly useful, fully automatic algorithms for determining the topical structure of human language data. TDT Pilot Study in 1997 laid the essential groundwork by conducting three main tasks: the segmentation, tracking and detection tasks. In 2004, TDT program [41] defined five research applications: (1) story segmentation to detect changes between topically cohesive sections, (2) topic tracking to keep track of stories similar to a set of example stories, (3) topic detection to build clusters of stories that discuss the same topic, (4) first story detection to detect if a story is the first story of a new, unknown topic, and (5) link detection to detect whether or not two stories are topically linked.

Topic detection is the task of grouping articles corresponding to the same topic. Comparing with topic tracking, topic detection has no prior information or description about the topic. Therefore, it learns what the topic is based on unsupervised clustering algorithm [25,15]. To be more precise, topic detection consists of two tasks: retrospective and online detections. The former entails the discovery of previously unidentified events in an accumulated collection. Event detection can be regarded as a discovery problem to mine the data stream for new patterns in document content. It analyzes the feature of documents and calculates the intra-similarity as a criterion of the same group. The latter strives to identify the onset of new events from live news feeds in real-time [52].

Topic tracking is the process of monitoring a stream of news stories to find those that track (or discuss) the same event as one specified by a user. While a new story coming, the system judge whether the story belongs to an existent topic or a new topic. Generally speaking, a topic tracking system assigns stories to specific topics based on a supervised classification [1,15]. In other mechanisms, Swan and Allen [49] used the $\chi ^ { 2 }$ -method to identify a burst of feature terms that appear more frequently at a time than at other times. Kleinberg [23] proposed a formal model of “bursts of activity” using an infinite-state automaton. Morinaga and Yamanishi [38] model a text stream with a finite mixture model, and trace the change of a topic trend by learning the finite mixture model dynamically.

## 2.2. Self-organizing maps

The self-organizing maps (SOM) algorithm is an artificial neural network model and unsupervised learning for clustering application [24]. It maps from highdimensional data space into a two-dimensional representation space. The SOM model is a widely used method for generating topology-preserving mappings and for data visualization. The remarkable characteristic of SOM is that the units of geographical vicinity within the representation space are relevant with each other.

In an abstract description, at first, terms extracted from documents are represented by vector space model [46]. Then, input vectors compare with all reference vectors in the map and the best matched location is the winner. The winner learns from an input vector and becomes more similar to the input vector. The neighbors of the winner are also allowed to learn some from input vector depending on the neighborhood function. After repeating the above actions, slowly the topology map becomes ordered; that is, nearby units have similar characteristic, and the characteristic change slowly and smoothly over the whole system.

There exist some drawbacks in the original SOM. First, the SOM uses a fixed topology network architecture in which the number and layout of neural processing units are defined prior to training. Second, hierarchical relations between input data are not mirrored in a straight-forward manner [11,16,48]. Dittenbach [11] proposes a revised artificial neural network architecture, called Growing Hierarchical Self-Organizing Map (GHSOM) to mend these drawbacks.

The concept of GHSOM is to use a hierarchical structure of multiple layers where each layer consists of a number of independent SOM. Each independent SOM has a flexible network structure which will be changed in the training process. Firstly, GHSOM starts with a “virtual” layer 0, which consists of only one single unit which reference weight is initialized as the average of all input vectors. The training process starts with a small map, e.g., 2 × 2 units in layer 1. After the same training process in SOM, the unit with the largest deviation between the reference vector and input vectors is selected as the error unit. Between the error unit and its most dissimilar neighbor, a new row or a new column of units is inserted. The reference weights of these new units are initialized as the average of their neighbors. Considering Fig. 1, the error unit is e and unit d is the dissimilar neighbor; therefore, insert a new row which is shown as shaded circles between unit e and unit d.

The criterion of stopping growing map depends on the mean quantization error (MQE). Each quantization error $q _ { i }$ of a unit is calculated as the sum of the distances between the reference vector of a unit i and the input vectors mapped onto this unit. The map grows until MQE is lower than a certain fraction $\tau _ { 1 }$ of the $q _ { i } .$ In the hierarchical structure, the unit is expanded by another layer in case of high quantization error $q _ { i }$ which is above threshold $\tau _ { 2 }$

Despite GHSOME overcomes aforementioned SOM's drawbacks, it still lacks the ability to deal with enormous data and dimensions. Kohonen [24] proposed WEBSOM to improve the scalability of SOM. The most important objective in designing the WEBSOM method is that it is scalable for use with large document collections [27]. WEBSOM adopts a simple approach called random mapping method proposed by Kaski [22]. It simply consists of multiple original document vectors with a random matrix that produces a smaller output dimensionality. Several methods have been proposed to support fast computation, for example, address old winner and initiate with best matching units [28]. Besides, parallelized batch map algorithm and saving memory by reducing representation accuracy are also proposed [27].

## 2.3. Event threading

Event threading detects events within in a topic, and also captures those dependencies among events [40]. The main difference to TDT is that event threading does not only identify events under the topic, but also digs out the relationship between a pair of events. Uramoto and Takeda first considered the relationship between multiple newspaper reports as directed graph, and genus and differentia words are used to calculate the similarities between reports [50]. They modified the original tfidf (term frequency times inverse document frequency) formula by adding the differentia words in the last k articles (k is a constant value specified by a user). These characteristics represented by the constructed graph are the cues of “story flow” of reports.

![](/api/attachments/BRN9TRGG/fulltext/images/6062793b240e97c3134ebb8079361a0745f08f55ae7d1146fd68c530be842061.jpg)  
Fig. 1. The example of insertion of units.

Events in a news topic are viewed as event threading to capture the structure of events and their dependencies [40]. Event threading which contributes to dependency modeling by adopting different clustering algorithms, such as average, complete, and single links, to cluster news reports into unique events in a topic. It relies on surface-features, such as time-ordering and word distribution, to construct dependency. The time-ordering feature is a basic feature to construct the complete-link model and nearest parent model. The feature of similarity is combined with time-ordering feature to form simple threshold, best similarity model and maximum spanning tree model. The dependency not only considers temporal-ordering but also causality. The cues of maximum spanning tree are taken account of causal dependency. Other related works according to publication sequence are concluded in Table 1.

## 2.4. Text summarization

Text summarization is a process of distilling the most important information from sources to produce an abridged version for particular users and tasks [35]. The research of text summarization has been in existence since 1950's, and disciplines such as library science and information retrieval have dominated research in this area [34].

An automated summarization can be decomposed into three phases: analyzing the input text, transforming it into a summary representation, and synthesizing an appropriate output form [35]. These three phases include three basic tasks: selection, aggregation, and generalization. It goes through selecting salient and non-redundant information, aggregating related information, and then inferring into a more general concept and format.

The importation criterion of summarization is the level of compression (a ration of summary length to source length). A perfect automated summarization is a high compression with full information which contains in the original document. However, the higher compression is the more information lost. Hence, it is a tradeoff for summarization. Traditionally, the compression rate ranges from 1% to 30%.

The content of summary can be divided into generic and user-focused in an audience viewpoint. The former can be served as surrogates for full-text, and the latter is extracted by user's needs, such as an area of interest, topic or query. Based on the purpose of summaries, there are three types of summary: indicative, informative and evaluative. Indicative summary aims to provide sufficient information which users can judge whether they need to read $\mathrm { i t } , e . g .$ ., academic abstract. Informative summaries intend to provide full information in a certain compression ratio. Moreover, evaluative summaries offer a critique of source text. Finally, in terms of output format of summary, the output format can be connected-text which is processed by NLP (natural language processing) or fragmentary (e.g., keyword or phrases).

Table 1  
The summary of related works of event threading

<table><tr><td>Authors</td><td>Applied area</td><td>Introduction</td><td>Method</td></tr><tr><td>Lewis et al. [30]</td><td>Threading electronic mail</td><td>It regards the similarity of subject, quoted and unquoted between two messages as a clue to judge whether a responsive relationship exist between them.</td><td>Text-based</td></tr><tr><td>Henzinger et al. [18]</td><td>Providing related news reports which is discussing on TV broadcast news</td><td>It proposes several query generation algorithms and three post processing techniques to filter out the news reports which are high relevant on the topic of the broadcast.</td><td>Query-based</td></tr><tr><td>Ichiro et al. [20]</td><td>Threading news video topics</td><td>It performs topic segmentation to identify topics in a news video and using semantic and chronological relation to track the chain of related reports in the same topic along time.</td><td>Text- and graph-based</td></tr><tr><td>Duygulu et al. [14]</td><td>Tracking the evolution of news topic in video</td><td>It takes the tendency of news channels to reuse the same video sequences to track the evolution of news topic.The proposed method exploits both visual cues and textual information to summarize evolving of news over time.</td><td>Text- and image-based</td></tr><tr><td>Kumar et al. [26]</td><td>Extracting the storylines from the search engine result</td><td>It rearranges the result of 10–100 documents which return from search result to provide a latent storyline. The maximum induced matching algorithm is proposed to dig out the signature structure as storyline on bipartite graph.</td><td>Graph-based</td></tr><tr><td>Chieu et al. [10]</td><td>A collection of news document</td><td>It ranks the sentences which are queried from a news corpus with interesting and bursty feature to represent them along a timeline.</td><td>Query-based</td></tr><tr><td>Nadamoto et al. [39]</td><td>Presenting a past series related reports of user-specified page</td><td>It extracts the topic structure of reports and finds the main topic and subtopic terms to query with similarity-detection and difference-detection in the corpus to select contextual pages.</td><td>Query-based</td></tr></table>

Four types of summarization methods are commonly used; they are knowledge-based, discourse-based, surface-level and entity-level approaches [3,35]. The knowl edge-based approach depends on rich domain knowledge sources, and is usually domain-specific and not applied widely. The discourse-based approach models the global structure of the text (e.g., the format of the document or rhetorical structure of the text) and its relation to communicative goals. The surface-level approach relies on shallow features (e.g., thematic features, location, background or cues words) to extract information. The entitylevel approach builds an internal representation for text, and analyzes the relationship according to similarity, proximity, and co-occurrence of entities.

Because of the difficulty of NLP and the specialization of the knowledge-based approach, most of the research applied surface- and entity-levels with sentence extraction [17]. These methods identify sentences that embody the key ideas of the text based on characteristics of the articles. Intuitively, the most important sentences are located at title, first paragraph, words which are boldface or in headline. Many heuristics can be used, including cue phrase, sentence length, thematic word, proper noun, anaphor, etc. [35,42,51,53]. These heuristics can be used individually or in combination.

Allan and coauthors generated and evaluated temporal summaries that help a person to monitor changes in news coverage over time [2]. The balance of novelty and usefulness determines whether a new incoming report should be included in the summary. Based on novelty and usefulness, a new coming sentence set will be compared with previous sentences to assign a score which indicates the importance of information that the new sentence provides. According to their experimental results, the writing style of inverted pyramid performs as well as their algorithm does.

Evaluation is also a critical issue for summarization. A summary composed by human can be treated as a standard answer to compare with that generated by a summarization system. Since human summary is very subjective and does not have a formal definition, the question-and-answer (Q&A) approach uses questions which are identified from full-text important events to judge whether the summary can provide sufficient information. Besides, in order to eliminate the human factors, the method of question answering system has been proposed [32]. It retrieves answers and possible sentences from summary and full-text, respectively. Its remarkable characteristic is that using the computer can efficiently handle a large quantity of summaries and fulltext articles. It assumes that readers (machines) have the same reading ability and do not have memory between the summary and full-text in the retrieval system. Due to inherent differences between Chinese and Western languages, such as the lack of explicit separators, for example, blanks or delimiter in written sentences indicating word boundary [9], additional tasks are needed prior to processing Chinese text. In Chinese summarization, a Chinese text is partitioned into several meaningful units, those units describing the same topic can be linked together, and then multi-source summary is generated by the voting mechanism executed by reporters [8].

Each basic unit split by commas may contain too little information. On the other hands, it split by period perhaps contains too much information. Consequently, a meaning unit (MU) which denotes a complete meaning is used as the basic unit [8]. Three kinds of linguistic knowledge, punctuation marks, linking elements and topic chain, were applied to identifying MUs.

Besides, Lee, Chen and Jian [29] proposed an ontology-based fuzzy event extraction (OFEE) agent for Chinese weather e-news summarization. OFEE tags and filters the retrieved Chinese e-news into noun- and verb-tags by a Chinese part-of-speech (POS) tagger. Furthermore, it infers the relationship between extracted events based on a weather ontology and fuzzy inference rule. Finally, it constructs the inferred event and the rule base of sentence pattern for Chinese e-news documents which are represented by POS sentence patterns into summaries.

## 3. News topic retrospection with storyline-based summarization

This section formally proposes the architecture of news topic retrospection with mechanisms including event identification, main storyline construction, and storyline-based construction. We start with defining news topic retrospection in the next subsection.

## 3.1. Definition of news topic retrospection

This study adopts the definition of TDT in topic and event [1,15]. A topic is defined as a seminal event or activity, along with all directly related events and activities, $e . g .$ , terrorism activity. An event is something (non-trivial) that happens at a particular time and place, $e . g .$ ., Oklahoma City bombing and September 11 attacks.

A story is a news report on an event. Consequently, a topic is composed of a series of related events, and can be talked as a storyline distilled from news reports. Similar to a film (topic), a plot presents a main storyline with many episodes (events), so that a moviegoer can quickly capture a movie's main storylines.

Furthermore, this study defines topic retrospection as an integrated task to identify various events in a news topic and construct relations among these events to summarize news articles in order to give news readers the sketch of event evolution. This study differentiates topic retrospection from TDT, event threading and multi-source summarization in order to distinguish this research from related literatures [36,37]. The main distinction to TDT and event threading is that topic retrospection further filters, organizes, and summarizes topic with text. Additionally, taking the topic structure to compose a summary is also different from the multisource summarization.

Formally, a news topic retrospection problem is defined in mathematical notations as follows. This research takes a set of $n$ news stories $S { = } \left\{ s _ { 1 } , \ s _ { 2 } { , \ldots } { , } s _ { n } \right\}$ belonging to a certain news topic ${ \mathfrak { I } } ,$ and $t ( s _ { i } )$ denotes the corresponding date of reporting $s _ { i }$ as inputs. S is divided into m events $\boldsymbol { \mathrm { \varepsilon } } = \{ \varepsilon _ { 1 } , \varepsilon _ { 2 } , . . . , \varepsilon _ { m } \}$ , and the duration $d ( \varepsilon _ { k } ) =$ [min $t ( s _ { i } ) ,$ , max $t ( s _ { j } ) ]$ , is calculated by the first and last stories $( i . e . , s _ { i }$ and $s _ { j } )$ in event $\varepsilon _ { k } . \ d \left( \varepsilon _ { k } \right)$ .start and $d ( \varepsilon _ { k } ) .$ end denote the first and last reporting dates of event $\varepsilon _ { k } .$ Besides, this study assumes that (1) every story collected for reviewing a news topic belongs to a set of events $\varepsilon , ( 2 )$ a story only describes a single event in $\varepsilon ,$ and (3) the chronological relationship of two stories can be established if the first story of the first event is earlier than the first story of the second event. This study aims to construct a main storyline to represent the evolution of events by building the chronological relationship. An edge $E = \left\{ \varepsilon _ { i } , \varepsilon _ { j } \right\}$ denotes the chronological relation between two events $\varepsilon _ { i }$ and $\varepsilon _ { j } .$

Specifically, the news topic retrospection is constrained under the following propositional logic.

$$
\begin{array}{l l} \forall s _ {i} & \exists \varepsilon_ {k} \in \varepsilon \text {   s.t.   } s _ {i} \in \varepsilon_ {k} \\ \forall i, j & i \neq j, \varepsilon_ {i} \cap \varepsilon_ {j} = \emptyset \\ \forall k & d (\varepsilon_ {k}) = [ \min t (s _ {i}), \max t (s _ {j}) ] s _ {i}, s _ {j} \in \varepsilon_ {k} \\ E = \{\varepsilon_ {u}, \varepsilon_ {v} \} & \text {   iff   } \quad \exists \varepsilon_ {u}, \varepsilon_ {v} \in \varepsilon \quad d (\varepsilon_ {u}). \text {start } <   d (\varepsilon_ {v}). \text {start} \end{array} \tag {1}
$$

The structure of a news topic is expressed by a directed graph. Each vertex in the graph denotes an event, and an edge represents the dependency between two vertices. $\mathrm { A n }$ edge established between a pair of events $\varepsilon _ { i }$ and $\varepsilon _ { j }$ denotes the chronological relation that event $\varepsilon _ { i }$ proceeds event $\varepsilon _ { j } .$

## 3.2. News topic retrospection system

A news topic retrospection system proposed in this study consists of three main functions: event identification, main storyline construction, and storyline-based summarization. Event identification distinguishes various events under a news topic. This task is analogous to event detection in TDT. Similar news stories will be grouped together to indicate an event using the clustering algorithm.

Main storyline is constructed after identifying the relationship between events and calculating the relevance between these events which have been connected through Maximal Spanning Tree (MST) and topic terms representing the theme of the news topic. The relevance algorithm will be used to construct the main storyline structure.

A news topic summary is composed according to the storyline structure using the storyline-based summarization function. The accumulated weight summarization approach selects sentences which represent events by accumulating weight among different features. Although the relationship appearing in a storyline structure can be used to guide news readers to understand the topic evolution, a storyline summary fits the habit of news readers who tend to read news articles instead of browsing a directed graph denoting the storyline structure. Moreover, the extracted sentences from original news reports can be used to guide readers to read corresponding news articles.

The news retrospection architecture also contains preprocessing functions to collect and transform news reports. Table 2 summarizes functions used by the proposed storyline-based topic retrospection architecture, called SToRe (Storyline-based Topic Retrospection).

## 3.3. Preprocessing news reports

The preprocess aims to collect stories belonging to a certain topic and transform these unstructured or semistructured news articles into a vector space model as what data transformation task does in the KDD (Knowledge Discovery in Databases) process. At first, a meta-schema such as the title, reporter, category, and reporting time is extracted from original news reports in HTML collected by a news crawler robot. Because of inherent difference between Chinese and Western languages, Chinese sentences are composed of characters without explicit word boundaries. Consequently, the word segmentation mechanisms for Chinese sentences are different from those used for Western languages. This study adopts the word segmentation system [33] developed by CKIP, IIS (Chinese Knowledge and Information Processing, Institute of Information Science, Academia Sinica) in Taiwan to segment words, syntactically annotate terms by their part of speech (POS), and then saved with XML (eXtensible Markup Language) format.

The number of terms in corpus is too large if we need to compute all of them. Moreover, many terms lack representative, for instance, stop words, such as ‘and’, ‘the’, and ‘a’. According to the characteristics of news stories [25], the name entity terms which are identified with noun phrases, e.g., people, place, and organization, will appear intensively in the same event for the purpose of consistence. Hence, terms except noun phrases will be filtered out in order to retain nouns to denote main features of a document. Besides, tfidf, often taken in term weighting and information retrieval tasks, is also adopted to filter features. tfidf takes a simple idea that a term with high frequency (tf) exhibits its importance, but the appearance of a term in many documents shows its low discrimination. Therefore, a term in a report with a high tfidf can be regarded as a high representative to stand for the original story [45].

Morphological analysis executes the task to unify terms which present the same meaning according to a predetermined ontology. For example, two terms, “HP” and “Hewlett-Packard,” actually refer to the same company, and will be converted to $\mathrm { ^ { 6 6 } H P ^ { 5 9 } }$ in order to acquire high accuracy of term weighting.

Table 2 SToRe functions

<table><tr><td></td><td>Function</td><td>Description</td></tr><tr><td rowspan="5">Preprocessing</td><td>Corpus collection</td><td>Collect a set of stories which belong to a certain news topic by a news crawler robot.</td></tr><tr><td>Feature filter</td><td>Identify word boundaries in Chinese sentences by CKIP.</td></tr><tr><td>Word segmentation</td><td>Filter terms based on the criteria of tfidf and part of speech (POS).</td></tr><tr><td>Morphological analysis</td><td>Unify terms which present the same meaning.</td></tr><tr><td>Vector space export</td><td>Weigh terms by tf and paragraph sequence, and then covert them into vector space.</td></tr><tr><td rowspan="3">Topic retrospection</td><td>Event identification</td><td>Distinguishing various events in a news topic.</td></tr><tr><td>Main storyline construction</td><td>Identify event relationship and the relevance with the main storyline.</td></tr><tr><td>Storyline-based summarization</td><td>Extract representative sentences to compose summary according to event relationship.</td></tr></table>

The final task performed in the preprocessing stage is to assign a numerical weight to each term according to its importance to represent the document in which it appears. A term with high frequency is more useful to symbolize the document. In addition, the order of paragraphs in a news report shows its importance to the theme that the report intends to shed [2]. Based on the guideline for writing news [6], inverted pyramid is the most traditional story form. The information is arranged from the most to the least important by following the order of paragraphs. The inverted pyramid saves readers time to get the most important part of the story first, $e . g .$ the climax of the event, the theme of a speech, and the key finding in an investigation. It also saves an editor's space to shorten stories from the last paragraphs. Accordingly, this study adopts both functions to weigh a term as shown in Eq. (2). Additionally, the news reporting date is added into the last tuple of the vector space model (VSM) in representing a news report.

$$
\operatorname{weight} \left(\text { term } _ {i}\right) = \frac {t f _ {i}}{\sqrt {\sum_ {\text { vector }} (t f) ^ {2}}} \times \frac {1}{\# \text { paragraph } _ {\text { term } _ {i}}}\tag{2}
$$

## 3.4. Event identification

The first task in topic retrospection is to distinguish events occurred in a news topic. Event identification is similar to event detection in TDT. In previous research [12,48], SOM reviewed in Section 2 has been applied in clustering different types of documents, e.g., news, legal documents, etc., and shown its usefulness and reliability. Therefore, this study adopts SOM for unsupervised clustering to identify events.

In addition, we cannot anticipate the number of events beforehand since it is subject to change by different news topics. Hence, this study adopts the growing selforganizing map (GSOM) to overcome SOM's shortcomings where the map size must be defined prior to training. Another reason that this study chose SOM family as the event identification algorithm is on the derivative strength of LabelSOM. Since the final output of the topic retrospection is a summarized text, the summarization can take terms identified by LabelSOM as candidate terms to compose summary.

It needs to determine the training cycle times, a stopping criterion for horizontal growth, and the learning rate, prior to conducting clustering. The learning rate is directly adopted by the predefined parameter provided by the system. Two methods can be used to decide the epochs in training a neural network. One is the fixed number of epochs, and the other method is to stop training when the performance has not been significantly improved. This study implements the former method and finds suitable parameters based on the quality of results. The same method has also been applied with $\tau _ { 1 }$ the horizontal growth parameter, and considers the MQE (mean quantization error) of entire map and the quality of clustering. Each story will be appointed to only one cluster, i.e., a cell of the generated SOM, and each cluster is treated as an event in the news topic. Besides, the system also selects terms from the Label-SOM mechanism to denote each cluster.

## 3.5. Main storyline construction

In the event identification step, the system has identified various events in a topic. The goal of main storyline construction is to analyze the topic structure and specify the main theme. The relationship of events cannot be simply composed by a tree. In some cases, more than two events may lead to another event, or an event can be split into two different events. Sometimes, events may occur in parallel. Therefore, it is more complicated than a tree to represent events. This study takes a graph to express the structure where an edge is used to denote the relations between two events as we mentioned in Section 3.4.

At first, each event is weighted by Eq. (3). The edge (relationship) between a pair of vertices (events) is drawn when the similarity between the pair of events exceeds a given threshold. It is adopted from [50] and takes the ideas of genus and differentia words with previous k events. It gives a high weight to the differentia words which are not appeared in previous events because they contain new information. More differentia words an event has, the more difficult it links to the previous events, so that the event will become a root to link to follow-up events. The situation matches with the real world, when something new happens to influence the exist events. In addition, the algorithm is more efficient and can run in O(n) time.

$$
\operatorname{weight} \left(\operatorname{term} _ {i} ^ {\varepsilon_ {j}}\right) = \frac {C _ {\varepsilon_ {j}} \left(\operatorname{term} _ {i}\right)}{\sum_ {\text { vector }} C _ {\varepsilon_ {j}} (\operatorname{term})} \times \log \frac {k}{N _ {k} \left(\operatorname{term} _ {i}\right)} \times g _ {\text { term } _ {i}} ^ {\varepsilon_ {j}}
$$

$g _ { \mathrm { t e r m } _ { i } } ^ { \varepsilon _ { j } } = \left\{ \begin{array} { l l } { 1 . 5 } \\ { 1 } \end{array} \right.$ term does not appear in the previous $k$ events Otherwise

3

In Eq. (3), $C _ { \mathrm { { g } } _ { i } }$ (term<sub>i</sub>) means the frequency of term<sub>i</sub> in $\varepsilon _ { j }$ and $N _ { k }$ (term<sub>i</sub>) is the number of events that contains term in previous k events which are ordered chronologically. The calculation of $N _ { k }$ (term<sub>i</sub>) for the previous k events is similar to the concept of nearest parent [40] that events are influenced by another event which occurs closely before them. Cosine coefficient [45] is used to calculate the similarity between events. The topic structure is constructed after filtering out those edges which similarity scores are below the threshold set by users.

Given a topic structure, the next problem is how to find the main storyline. Intuitionally, the main topic will be discussed and distributed in the whole events. The same terms will repeatedly appear in most of stories. On the contrary, terms used to describe a unique event will appear only in certain events. Therefore, we define the main storyline as a path of events where the topic terms occur in a high frequency. The topic terms are similar with the concept, topic signature [31], a set of related words organized around head topics. The topic terms in this study will be determined by document frequency. Terms with high document frequency means that they are generally discussed in most of stories and highly associated with the topic.

The algorithm of relevance and maximum spanning tree (MST) are taken to trace the main storyline. After obtaining topic terms, we use the relevance algorithm shown in Eq. (4) to measure how relevant events are related to the main storyline. It adopts the concept of cluster-based retrieval [21]. In Eq. (4), TT denotes the set of topic terms. N is the number of stories an event has, and n is the number of stories that contain the topic  is an adjusted item to smooth the term that only appears in few stories. Because an event is composed by a group of stories, simply calculating the term frequency biases the topic terms which aggregately appear in few stories.

$$
R (\varepsilon | \mathrm{TT}) = \sum_ {t \in \mathrm{TT}} \left(\frac {t f _ {t}}{\sqrt {\sum_ {\text { vector }} (t f) ^ {2}}} \times \frac {n}{N}\right)\tag{4}
$$

The MST is the tree with the maximum length connecting nodes, where the length means the sum of the weights of the connecting links in the tree [44]. The MST can be applied to find a path which goes through the high relevance events. The spanning tree is derived from the graph whose edges are weighted by Eq. (5). The MST is simply the tree spanning the nodes which in total have the maximum weight. It is usually solved by a greedy algorithm as shown in Fig. 2. To avoid the biases that a greedy algorithm only considers the current node and finds a local optimal, the number of next path that $\varepsilon _ { j }$ has will be measured. It decreases the probability that MST finds a path that is a short path but with a high relevant end node.

$$
I \left(\varepsilon_ {i}, \varepsilon_ {j}\right) = \alpha \times R \left(\varepsilon_ {j} \mid \mathrm{TT}\right) + (1 - \alpha) \times \frac {\# \text { nextPath } _ {\varepsilon_ {j}}}{k}\tag{5}
$$

Finally, branches are added to the main path generated by MST. This study only considers nodes that connect to the main path and their relevance exceeds a given threshold. The threshold can simply be set with the average plus the standard deviation. It enhances the storyline construction by remedying what MST can only build a path without branches.

## 3.6. Storyline-based summarization

In the final stage of topic retrospection, the main purpose is to provide a meaningful description of each event to compose a summary of a news topic. Although keywords are used widely, they lack the semantic level of characteristics, and can even mislead readers. Consequently, we address an approach to integrate the main storyline into a summary to represent a news topic.

![](/api/attachments/BRN9TRGG/fulltext/images/8b3424eaafdeb14c0d62094c0300f215b0f463289980e8f81cc3a3166fe2b112.jpg)  
Fig. 2. Pseudo codes of MST.

Accumulated Weight Summary (AWS) is used to compose a summary that one or more descriptive sentences are extracted from news reports to represent the topic. The process of sentence extraction with accumulated weight will be used to identify sentences which fit the best. At first, we extract sentences from the first p paragraphs based on the heuristic of inverted pyramid, so that the most informative sentences will be extracted from the preceding p paragraphs to compose the summary.

These sentences will be segmented by punctuation marks of stop words, i.e., period, semicolon, and exclamation point. Summarization aims to use the fewest words to contain the most information. Label-SOM and tfidf are adopted as term weighting heuristics. LabelSOM uses the idea of quantization error to select representative terms. Terms which are chosen have a small error are those that are commonly used in documents. It is similar but some variations with tfidf. We give a high weight to sentences with these terms.

Consequently, this study composes differentiable sentences based on the Maximal Marginal Relevance (MMR) [17]. MMR computes penalty measures based on similarity factors to avoid selecting redundant sentences. Each pair of sentences is measured by their mutual similarity to avoid the redundancy. When two sentences in the same event provide the similar information, the sentence with a longer length will be removed. Each candidate sentence will be given an accumulated weight score, and top three sentences with the highest scores become the summary of an event.

After preparing the summary of each event, this study applies two general strategies, chronological ordering and majority ordering [4], which are generally used for multi-document summarization to compose a summary of the news topic complying with the main storyline. The summary of an event stands for a paragraph. The sequence of paragraph follows the first reporting date of an event. When two events reported on the same date, their ordering will be determined by the majority ordering strategy. When the majority of sentences in one event are earlier than the other, the summary of the event will appear in front of that of the other event. Finally, this study adds time period that an event occurred in front of each paragraph of the summary. A news reader can easily acquire the sketch of a news topic by reading the summary.

In summary, the SToRe system uses GHSOM for clustering documents into events. The storyline construction starts with determining events' weights (Eq. (3)), and then using cosine coefficient to calculate the similarity between events to sketch the topic. Eq. (4) is used to calculate the relevance between events and the storyline. The maximum spanning tree is derived from the graph whose edges are weighted by Eq. (5). Finally, this study adopts Accumulated Weight Summary (AWS) to compose a storyline-based summary.

## 4. SToRe implementation and experimental design

The primary goal of the implementation of the SToRe system is mainly to demonstrate how a storyline summary benefits news readers in capturing the evolution of major events in a news topic. A lab experiment is conducted to evaluate its performance in a question-andanswer (Q&A) setting.

## 4.1. System implementation

The SToRe system, implemented by Java, consists of two components, preprocessing and topic retrospection. In order to properly evaluate SToRe, this study sets four criteria to selecting news topics: (1) the number of stories exceeds readers' cognitive load, (2) the time period that the news topic occurred is far enough that readers may not remember it in details, (3) no similar topics occurred that readers can refer to, and (4) readers are not familiar with the topic or lack of domain expertise.

Udndata.com<sup>1</sup> which is established by United Daily News Group (UDN) is a Chinese news repository. It covers the past fifty years news reports gathered from United Daily News, Economic Daily News, and United Evening News. Udndata.com features a clipping folder system which clusters news reports in specific news topics by reporters.

Experimental data are collected from Udndata.com in business and economics categories which are the most dissimilar to subjects. There are 188 topics in these two categories and the average number of stories in each topic is 69. According to the aforementioned selection criteria, “HP's acquisition of Compaq”, is picked as the news topic. It occurred during years 2001 and 2002 (news reports from September 1, 2001 to April 1, 2002) and is far away from the time we conducted the experiment (June, 2005). Moreover, subjects cannot read all 179 stories in a short time. Therefore, the selected topic conforms to these criteria.

Table 3  
Parameters used in SToRe

<table><tr><td>Parameter</td><td>Value</td><td>Module</td><td>Criterion</td></tr><tr><td>Cycle times</td><td>1000</td><td>Event Identification</td><td>Empiric</td></tr><tr><td>Horizontal growth</td><td>0.008</td><td>Event Identification</td><td>Empiric</td></tr><tr><td>Learning rate</td><td>0.5</td><td>Event Identification</td><td>System initiation</td></tr><tr><td>k</td><td>3</td><td>Main storyline construction</td><td>Empiric</td></tr><tr><td>Similarity</td><td>0.04302</td><td>Main storyline construction</td><td>Median</td></tr><tr><td>Relevance</td><td>1.092</td><td>Main storyline construction</td><td> $\mu + 0.5 \times \sigma$ </td></tr><tr><td>Similarity</td><td>0.6</td><td>Storyline-based summarization</td><td> $\mu + 2 \times \sigma$ </td></tr><tr><td>p</td><td>2</td><td>Storyline-based summarization</td><td>Empiric</td></tr></table>

In the preprocessing stage, 179 reports are extracted and segmented into basic terms with CKIP. A term which part-of-speech (POS) is not a noun and its corresponding tfidf value is zero is removed from the term list, and 3025 terms are retained at the end. Therefore, the vector space model is composed of 3026 terms and a time stamp, and each weight is computed by Eq. (2).

In the topic retrospection stage, the GHSOM system version 1.6 [43] developed by the Department of Software Technology, Vienna University of Technology, was applied to implementing event identification function. The GHSOM system is capable of generating conventional SOM and GHSOM and compiled with C on Linux platform. GSOM is performed to identify various events in this topic. 19 events are identified and the average ten stories in each event. Each event is recoded by Eq. (3) to construct topic structure. The constant value k is 3 and the relationship is established when the similarity score is above 0.04302. The criterion is determined by median; that is, half of dependencies are removed. Depending on document frequency, eight terms are picked as topic terms. They are (HP), (Compaq), (acquisition), (global), (shareholder), (chief executive officer), (board directors), (enterprise). Fed by these topic terms, the system performs MST using a greedy algorithm to identify the main storyline. Those branches which corresponding relevance score is higher than 1.092 are also linked to the main storyline.

Given a main storyline, sentences of the first two paragraphs are selected as candidate sentences for summarization. Each sentence is weighted by LabelSOM and tfidf. The highest three sentences are selected and sorted by chronology and majority to compose the summary. News readers can read the summary which has hyperlinks to original news reports. Parameters used in this example topic retrospection are listed in Table 3.

## 4.2. Preliminary results

The main storyline of “HP's acquisition of Compaq” is drawn in Fig. 3. The solid lines are constructed by MST and dashed lines are branches. The brief introduction in block is labeled by human to explain the sketch of event evolution SToRe discovered.

![](/api/attachments/BRN9TRGG/fulltext/images/078fbd6d36fb54b2fb1a1e2dbf1ff79ca39de019aca237164cae5094e22d3198.jpg)  
Fig. 3. Event revolution process of “HP's acquisition of Compaq”.

The main storyline can give news readers the main path to go through the topic and remove some irrelevant events. For example, even though the data sets in Udndata.com are collected by reporters, some events do not directly influence or are not influenced by the event, e.g., the stock price of HP-Compaq's partner in Taiwan, are not included in the storyline.

In addition, sentences selected from news articles into the summary can give news readers the most useful information about how HP acquired Compaq and different opinions in the acquisition process. Although some sentences may not provide important information, they can be an index to facilitate the allocation of related information. Consequently, the main storyline can be regarded as a template to summarize events and give news readers an index to understand the development of events in a topic. It is different from the previous researches in TDT and summarization.

## 4.3. Experimental design

## 4.3.1. Subjects

The experiment was conducted with two groups under nearly identical conditions, and different formats of topic retrospection were presented to different groups. Subjects include 49 graduate students from the Department of Information Management at National Sun Yatsen University in Taiwan. Among them, 73% and 27% students are male and female students, respectively. Every subject was randomly assigned into the experimental or control group according to the sequence s/he registers to the experiment. All subjects received NT\$

200 to compensate their participations. In order to encourage subjects to make the best effort to answer questions, additional prizes rewarded subjects who gained the top five scores.

Subjects in both groups major in the same discipline with similar educational background. Moreover, questionnaires for assessing subjects' behaviors in reading news were conducted at the end of the experiment.

## 4.3.2. Experimental procedure

The experimental procedure will go through a laboratory experiment in a Q&A (question–answer) setting [34]. It takes 40 min for a subject to finish the experiment. The main difference between the experimental and control groups is on the format of displaying topic retrospection. The experimental group is given a storyline-based summarization to help subjects understand the event evolution of the news topic. On the other hand, the control group is present at events identified with news title and its corresponding keywords. Therefore, the experiment evaluates the proposed SToRe system with traditional TDT in helping news readers obtain the sketch of a news topic.

As illustrated in Fig. 4, the experiment consists of three phases. Before starting the experiment, subjects are briefly introduced to the purpose and the process of the experiment, and then a simulated examination is used to teach subjects how to operate the system. In the formal examination, subjects are granted 9 min to read the text provided by the system in different formats, and then subjects have 20 min to answer online questions to test their degree of understanding. After finishing the examinations, subjects filled out the questionnaire which asks subjects' experiences in reading electronic newspapers and their perception to the SToRe system.

![](/api/attachments/BRN9TRGG/fulltext/images/aa5067612a50ca16c45ef4ce04bb07e03ec6722293c575a5a6a834cf943589c0.jpg)  
Fig. 4. Experimental procedure.

Before conducting experiments, two pretests were taken to help design experimental settings. According to the feedback from the first pretest by eight subjects, we modified the expression of questions to avoid misunderstanding, and tuned the degree of difficulty to fit the problem setting. The second pretest invited the other eight subjects to adjust the time distribution for each section of the examination.

Since time plays an important factor in the experiment, we performed a loading test to ensure the acceptable response time during the experiment to guarantee that the server maintained a reasonable response time to serve 25 online users who requested once every 2 min. Hence, we set up two servers to provide services and each server was assigned to serve half of subjects randomly.

## 4.3.3. Examinational questions

Whereas questions are critical in the Q&A experimental setting, we asked a domain expert who did not involve with this study to issue questions. The domain expert was given the full news text of the topic without reading the storyline-based summary. According to the characteristic of news topic, questions were categorized into five types: WHO, WHAT, WHEN, WHICH and OTHER. The scope of questions varied from narrow in one event to a broad coverage of several events. Furthermore, some questions were considered the relationship between a pair of events or the sequence to sort the events. The format of questions included multiplechoice, blank filling, and true–false items. Table 4 lists the distribution of different question types.

26 questions were set as a unit, and each unit contained different types of questions based on their homologous proportion. The main purpose of this question dispatch was to assure that every type of questions had the chance to be answered in one unit. But the questions in the category of OTHER were only assigned into the last unit because they were less relevant to the topic and hard to be classified. The ordering of questions in each unit was sorted randomly. Hence, the sequence of questions which every subject faced is different from each other. It eliminated the bias that only easy or hard questions were answered by subjects firstly. After the experiment, two reviewers independently scored answers.

Table 4

<table><tr><td colspan="7">(a). Types of questions in formal examination</td></tr><tr><td></td><td>WHO</td><td>WHAT</td><td>WHEN</td><td>WHICH</td><td>OTHER</td><td>Total</td></tr><tr><td>Numbers</td><td>12</td><td>41</td><td>13</td><td>25</td><td>13</td><td>104</td></tr><tr><td>Percentage</td><td>11.5%</td><td>39.4%</td><td>12.5%</td><td>24.1%</td><td>13.5%</td><td>100%</td></tr></table>

(b). Format of questions in formal examination

<table><tr><td></td><td>Multi-choice</td><td>Blank filling</td><td>True/false</td><td>Total</td></tr><tr><td>Numbers</td><td>46</td><td>42</td><td>16</td><td>104</td></tr><tr><td>Percentage</td><td>44.2%</td><td>40.4%</td><td>15.4%</td><td>100%</td></tr></table>

Table 5  
Group statistics of measurements

<table><tr><td colspan="2"></td><td>Number</td><td>Mean</td><td>SD</td><td>SE mean</td></tr><tr><td rowspan="2">Score</td><td>Control group</td><td>24</td><td>9.292</td><td>4.258</td><td>0.869</td></tr><tr><td>Experimental group</td><td>24</td><td>14.500</td><td>8.638</td><td>1.763</td></tr><tr><td rowspan="2">Answered questions</td><td>Control group</td><td>24</td><td>18.250</td><td>8.440</td><td>1.723</td></tr><tr><td>Experimental group</td><td>24</td><td>23.458</td><td>14.102</td><td>2.879</td></tr><tr><td rowspan="2">Correctness rate</td><td>Control group</td><td>24</td><td>0.523</td><td>0.165</td><td>0.034</td></tr><tr><td>Experimental group</td><td>24</td><td>0.626</td><td>0.150</td><td>0.031</td></tr><tr><td rowspan="2">Article clicks</td><td>Control group</td><td>24</td><td>49.667</td><td>22.959</td><td>4.686</td></tr><tr><td>Experimental group</td><td>24</td><td>33.292</td><td>20.153</td><td>4.114</td></tr></table>

## 5. Experimental results

The experimental results are evaluated by statistical analysis. First, subject profiles were inspected in order to guarantee that subjects were common in terms of time, frequency, and category in reading electronic newspapers. The score, accuracy, query method and time between experimental and control groups were examined by t-test to evaluate the SToRe performance. Factors affecting the results were explained accordingly.

Among the results from 49 subjects, those from 48 subjects are reliable. One subject is removed from the result set because the subject failed to follow the experimental instruction throughout the process. We use the confidence interval α = 0.05 to test the statistical significance.

## 5.1. Subject profile

The gender of subjects is uniform distributed. Male and female subjects were uniformly assigned to each group according to the sequence of joining the experiment. Therefore, the experiment was conducted in two groups with similar gender distribution. The time, frequency, and category that subject read electronic newspapers were asked in the experiment to understand subject profiles. Five nominal scales were used to measure the frequency of reading electronic newspapers in a week. Because of using nominal scales, the test of homogeneity of proportions in chi-square tests was adopted to compare whether the proportion between groups was significantly different. Results from Chi-square tests show that the weekly frequency and category of reading electronic newspapers differs insignificantly in p-values of Pearson Chi-square, 0.785 and 0.829, respectively.

Table 6  
Independent samples test of measurements

<table><tr><td rowspan="2"></td><td colspan="2">Levene&#x27;s test for equality of variances</td><td rowspan="2">t</td><td rowspan="2">df</td><td rowspan="2">Sig. (2-tailed)</td><td colspan="2">95% confidence interval of the diff.</td></tr><tr><td>F</td><td>Sig.</td><td>Lower</td><td>Upper</td></tr><tr><td>Score</td><td>10.177</td><td>0.003</td><td>-2.650</td><td>33.554</td><td>0.012*</td><td>-9.205</td><td>-1.212</td></tr><tr><td>Questions answered</td><td>6.095</td><td>0.017</td><td>-1.553</td><td>37.604</td><td>0.129</td><td>-12.002</td><td>1.585</td></tr><tr><td>Correctness rate</td><td>1.022</td><td>0.317</td><td>-2.265</td><td>46</td><td>0.028*</td><td>-0.195</td><td>-0.011</td></tr><tr><td>Article clicks</td><td>0.031</td><td>0.861</td><td>2.626</td><td>46</td><td>0.012*</td><td>3.823</td><td>28.927</td></tr></table>

In summary, subjects were common not only in educational background but also on the habit of reading electronic newspapers. According to the statistical analysis, subjects had no significantly differences in the frequency, time, and category of reading newspapers. Consequently, this experiment was conducted in a similar subject profile.

## 5.2. Evaluating SToRe system

At first, we want to verify whether subjects did their best during the experiment. If subjects adopted a guessing strategy to answer questions, they might answer without finding any information from text. This guessing attempt cannot reflect the real effects from different display formats. Hence, a multi-choice or true–false question is regarded as a guessable question, while a blank filling question is categorized as a non-guessable question. The paired samples t-test shows that no significant difference (p-value = 0.127) exists between the correctness rate of guessable and non-guessable questions. That is, there is not enough evidence to support that subjects used the guessing strategy during the experiment.

Furthermore, in order to evaluate how SToRe helps news readers effectively and efficiently to retrospect news topics, this study measures the score, answered questions, correctness rate and article clicks during the experiment. The results are summarized in Table 5, and independent samples t-test statistical results are shown in Table 6.

Table 7  
Statistics of hyperlink clicks

<table><tr><td></td><td>Mean</td><td>Number</td><td>SD</td><td>SE mean</td></tr><tr><td>LFS</td><td>23.875</td><td>24</td><td>17.568</td><td>3.586</td></tr><tr><td>LFL</td><td>9.417</td><td>24</td><td>17.784</td><td>3.630</td></tr></table>

In terms of effectiveness, we expect that SToRe can help news readers correctly capture the theme of news articles of a topic in short time. Providing different display formats of topic retrospection, subjects in both groups answered questions extracted from news articles. The score, correctness rate, and answered questions in a Q&A test are used to evaluate the SToRe effectiveness. Table 6 shows via the p-value of score (0.012) and correctness rate (0.028) that subjects in the experimental group significantly outperform those in the control group in terms of correctly answering questions. This outcome supports that SToRe effectively facilitates news readers to catch main stories of a news topic in a short time. Although subjects in the experimental group answered more questions than those in the control group, the difference is not significant. This outcome can be explained as follows. SToRe gives subjects an impression of something happened. When a subject faces a question, s/he may verify his/her impression and ensure that his/her answer is correct. Therefore, two groups spent the similar time period in answering a question. However, a higher correctness rate made the experimental group have a higher score.

In terms of efficiency, the number of clicks to articles prior to answering a question was recorded in order to understand the efforts a subject spent on answering questions. If SToRe provides an efficient channel to find information, a news reader may find answers in few steps. The summarization is treated as an index to help news readers construct their own knowledge structure regarding a news topic. The average numbers of clicks for the control and experimental groups are 49.667 and 33.292, respectively (Table 5). Subjects in the experimental group used significantly less clicks than those in the control group $( p { = } 0 . 0 1 2 )$ . One reason is that summarization provides enough information for readers to capture the development of a topic. Another reason is that the efficient index can guide the information search. Subjects in the experimental group facilitated by SToRe seem to sail in the ocean guided by a compass. Facing numerous news titles, subjects in the control group may use the try-and-error strategy to find answers. Hence, it results in significantly different performance between two groups.

Table 8  
Paired samples test of hyperlink clicks

<table><tr><td rowspan="2"></td><td rowspan="2">Mean</td><td rowspan="2">t</td><td rowspan="2">df</td><td rowspan="2">Sig. (2-tailed)</td><td colspan="2">95% confidence interval of the diff.</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td>LFS-LFL</td><td>14.458</td><td>2.439</td><td>23</td><td>0.023*</td><td>2.193</td><td>26.723</td></tr></table>

Table 9  
Group statistics of answering questions in different types

<table><tr><td>Type</td><td>Measure</td><td>Group</td><td>Number</td><td>Mean</td><td>SD</td></tr><tr><td rowspan="4">WHO</td><td rowspan="2">Score</td><td>Control group</td><td>21</td><td>2.190</td><td>1.250</td></tr><tr><td>Experimental group</td><td>24</td><td>2.042</td><td>1.459</td></tr><tr><td>Correctness</td><td>Control group</td><td>21</td><td>0.702</td><td>0.317</td></tr><tr><td>Rate</td><td>Experimental group</td><td>24</td><td>0.545</td><td>0.262</td></tr><tr><td rowspan="4">WHAT</td><td rowspan="2">Score</td><td>Control group</td><td>24</td><td>4.208</td><td>1.911</td></tr><tr><td>Experimental group</td><td>24</td><td>6.958</td><td>4.048</td></tr><tr><td>Correctness</td><td>Control group</td><td>24</td><td>0.530</td><td>0.202</td></tr><tr><td>Rate</td><td>Experimental group</td><td>24</td><td>0.683</td><td>0.208</td></tr><tr><td rowspan="4">WHEN</td><td rowspan="2">Score</td><td>Control group</td><td>22</td><td>1.227</td><td>1.110</td></tr><tr><td>Experimental group</td><td>22</td><td>2.364</td><td>1.706</td></tr><tr><td>Correctness</td><td>Control group</td><td>22</td><td>0.474</td><td>0.430</td></tr><tr><td>Rate</td><td>Experimental group</td><td>22</td><td>0.775</td><td>0.299</td></tr><tr><td rowspan="4">WHICH</td><td rowspan="2">Score</td><td>Control group</td><td>24</td><td>2.042</td><td>1.367</td></tr><tr><td>Experimental group</td><td>24</td><td>3.417</td><td>2.358</td></tr><tr><td>Correctness</td><td>Control group</td><td>24</td><td>0.440</td><td>0.279</td></tr><tr><td>Rate</td><td>Experimental group</td><td>24</td><td>0.511</td><td>0.290</td></tr></table>

In addition, this study analyzes the effects on correctly answering questions with different hyperlinks to news articles in the experimental group. In the experiment settings, subjects had two ways to link to original new articles. One is called LFS (Link-From-Summarization) that the news article is linked from the end of each sentence in the summarization to the corresponding article. The other is called LFL (Link-From-List) that news articles are linked from a list of news titles corresponding to a paragraph of the summarization. If the summarization plays the role of index, subjects will prefer LFS to LFL. Therefore, we adopt paired samples t-test to examine whether this hypothesis is supported.

Results show in Tables 7 and 8 that LFS has significantly lower hyperlink clicks than LFL (p = 0.023). It indicates that links from summarized sentences facilitate the search of answers. Subjects can click articles from the summarized sentences instead of browsing all news titles to answer questions.

Besides, we analyze whether the facilitation of SToRe has different effects on different question types. Tables 9 and 10 summarize the statistics and results. Subjects in the experimental group have better performance than those in the control group in various types except in WHO type. It indicates that summarization does not help news readers identify people who are mentioned in the topic and their corresponding roles. One possible reason is on the news writing style that a person mentioned first time in a news article will be described with one's position, but only the person's name will be referred in the following paragraphs. Therefore, when SToRe extracts a representative sentence to denote the theme of the article, it may select the sentence which mentions a person without the title. Subjects in the experimental group may know the person's name and his/her attitudes in the summarization, but they cannot answer such question as a person's position.

Moreover, in answering questions in WHICH category, the correctness rate is also insignificant ( p-value=

Table 10  
Independent sample test of answering questions in different types

<table><tr><td rowspan="2">Type</td><td rowspan="2">Measurement</td><td rowspan="2">t</td><td rowspan="2">df</td><td rowspan="2">Sig. (2-tailed)</td><td colspan="2">95% confidence interval of the diff.</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td rowspan="2">WHO</td><td>Score</td><td>0.365</td><td>43</td><td>0.717</td><td>-0.674</td><td>0.972</td></tr><tr><td>Correctness rate</td><td>1.824</td><td>43</td><td>0.075</td><td>-0.017</td><td>0.331</td></tr><tr><td rowspan="2">WHAT</td><td>Score</td><td>-3.009</td><td>32.761</td><td>0.005**</td><td>-4.610</td><td>-0.890</td></tr><tr><td>Correctness rate</td><td>-2.581</td><td>46</td><td>0.013*</td><td>-0.272</td><td>-0.034</td></tr><tr><td rowspan="2">WHEN</td><td>Score</td><td>-2.619</td><td>42</td><td>0.012*</td><td>-2.012</td><td>-0.261</td></tr><tr><td>Correctness rate</td><td>-2.693</td><td>37.438</td><td>0.011*</td><td>-0.527</td><td>-0.075</td></tr><tr><td rowspan="2">WHICH</td><td>Score</td><td>-2.472</td><td>36.890</td><td>0.018*</td><td>-2.502</td><td>-0.248</td></tr><tr><td>Correctness rate</td><td>-0.869</td><td>46</td><td>0.390</td><td>-0.236</td><td>0.094</td></tr></table>

Table 11  
Statistics of survey in the experimental group

<table><tr><td>Measure</td><td>Number</td><td>Mean</td><td>SD</td><td>SE mean</td></tr><tr><td>Usefulness</td><td>24</td><td>3.708</td><td>1.083</td><td>0.221</td></tr><tr><td>Ease of use</td><td>24</td><td>3.125</td><td>1.191</td><td>0.243</td></tr><tr><td>Efficiency</td><td>24</td><td>3.500</td><td>1.142</td><td>0.233</td></tr><tr><td>Satisfaction</td><td>24</td><td>3.250</td><td>0.944</td><td>0.193</td></tr><tr><td>Comprehensibility</td><td>24</td><td>3.250</td><td>0.897</td><td>0.183</td></tr></table>

0.390). We conjecture that questions in WHICH category ask detailed information such as the amount of money or numerical data. Subjects are not skilled enough in answering this kind of questions. Consequently, the correctness rate does not have significant improvement.

Subjects in the experimental group answering WHEN questions obtain the highest score. This outcome can be explained as follows. Since the summarization is ordered chronologically and when subjects read the summarization, they can establish the chronological order of event occurrence. Therefore, it is easy for subjects in the experimental group to find the time point at which an event occurs.

Finally, this study used 5 point Likert scale to measure subjects' perceived values of SToRe, and the result shows that the mean is all above the average, 3.0 (Table 11). The highest mean is usefulness, and the lowest mean is ease of use. At present, no similar systems are available in the market to help news readers review news topics. From the result, we found that this facilitation is very useful for subjects as an efficient channel supported by statistical measurement in Tables 6 and 8 (e.g., article clicks and LFS). We also found that the output of summarization is similar with humanwritten one in comprehensibility. They felt satisfied with the experimental settings. In terms of ease of use, this study is the first time that subjects operate such system as SToRe to capture the evolution of events in a news topic. Hence, subjects couldn't comprehend functions embedded in the system. By training, subjects may be used to the system.

## 6. Conclusion and potential applications

This study proposes a mechanism to help a news reader review a news topic in a short time. Comparing with the previous approaches that only identify events represented as lists with news titles and keywords, the SToRe system adopts an integrated framework of TDT, event threading and summarization to support topic retrospection. It considers the quantity, format and quality of information to mitigate the information overloading problem faced by news readers.

The SToRe system can be applied in many fields. The most direct application is in news database. In Taiwan, most of news databases provide the function of the clipping folder system that collects related happened events in a topic. Hence, the mechanism may help a news reader get a sketch of happened events in a topic, and then identify specific news articles to read. Companies or government agents can collect digital documents for executed projects and capture the project development process by using the proposed topic retrospection mechanisms. The summary of a project can be used as a guide for a freshman or a junior manager to plan similar projects in the future. They can learn from these occurred activities in similar projects and pay attention on critical activities which lead a project to succeed or fail.

## References

[1] J. Allan, R. Papka, V. Lavrenko, On-line new event detection and tracking, Proceedings of the 21st annual international ACM SIGIR conference on Research and development in information retrieval, 1998.

[2] J. Allan, R. Gupta, V. Khandelwal, Temporal Summaries of News Topics, Proceedings of SIGIR 2001, 2001, pp. 10–18.

[3] C. Aone, M.E. Okurowski, J. Gorlinsky, B. Larsen, A scalable summarization system using robust NLP, Proceedings of the workshop on intelligent scalable text summarization at the 35th meeting of the association for computational linguistics, and the 8th conference of the European chapter of the association for computational linguistics, 1997, pp. 66–73.

[4] R. Barzilay, No. Elhada, K.R. Mckeown, Inferring strategies for sentence ordering in multidocument news summarization, Journal of Artificial Intelligence Research 17 (2002) 35–55.

[5] H. Berghel, Cyberspace 2000: dealing with information overload, Communications of the ACM 40 (2) (February 1997).

[6] B.S. Brooks, G.D. Kennedy, R. Moen, D. Ranly, News Reporting and Writing, St. Martin's Press, NY, 1996.

[7] J.S. Brown, P. Duguid, The Social Life of Information, Harvard Business School Press, Boston, 2000.

[8] H.-H. Chen, J.-J. Kuo, S.-J. Huang, C.-J. Lin, H.-C. Wung, A summarization system for Chinese news from multiple sources, Journal of the American Society for Information Science and Technology 54 (13) (2003) 1224–1236.

[9] L.-F. Chien, PAT-tree-based adaptive keyphrase extraction for intelligent Chinese information retrieval, Information Processing and Management 35 (1999) 5001–5521.

[10] H.L. Chieu, Y.K. Lee, Query Based Event Extraction along a Timeline, Proceedings of the 25th Annual ACM SIGIR Conference, 2004.

[11] M. Dittenbach, D. Merkl, A. Rauber, The growing hierarchical self-organizing map, Proceedings of the International Joint Conference on Neural Networks (IJCNN), 2000.

[12] M. Dittenbach, A. Rauber, D. Merkl, Uncovering hierarchical structure in data using the growing hierarchical self-organizing map, Neurocomputing 48 (2002) 199–216.

[13] W.P. Doran, N. Stokes, E. Newman, J. Dunnion, J. Carthy, A hybrid statistical/linguistic model fro generating news story

gists, Proceedings of the 27th annual international conference on Research and development in information retrieval, 2004.

[14] P. Duygulu, J.-Y. Pan, D.A. Forsyth, Towards auto-documentary: tracking the evolution of news stories, Proceedings of the ACM Multimedia Conference, 2004.

[15] M. Franz, J.S. McCarley, Unsupervised and supervised clustering for topic tracking, Topic Detection and Tracking Workshop, 2001.

[16] B. Fritzke, Growing grid: a self-organizing network with constant neighborhood range and adaptation strength, Neural Processing Letters 2 (5) (1995).

[17] J. Goldstein, V. Mittal, J. Carbonell, J. Callan, Creating and evaluating multi-document sentence extract summaries, Eighth International Conference on Information Knowledge Management (CIKM'00), 2000.

[18] M. Henzinger, B.-W. Chang, B. Milch, S. Brin, Query-free news search, Proceedings International WWW Conference, Budapest, Hungary, 2003.

[19] J. Ho, R. Tang, Towards an optimal resolution to information overload: an infomediary approach, Proceedings of the 2001 International ACM SIGGROUP Conference on Supporting Group Work, 2001.

[20] I. Ichiro, M. Hiroshi, K. Norio, Threading news video topics, Proc. of 5th ACM SIGMM International Workshop on Multimedia Information Retrieval, 2003.

[21] N. Jardine, C.J. Van Rijsbergen, The use of hierarchical clustering in information retrieval, Information Storage and Retrieval 7 (1971) 217–240.

[22] S. Kaski, Dimensionality reduction by random mapping: fast similarity computation for clustering, Proceedings of IJCNN'98, 1998 IEEE International Joint Conference on Neural Networks, 1998.

[23] J. Kleinberg, Bursty and hierarchical structure in streams, Proceedings of the 8th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2002.

[24] T. Kohonen, Self-Organizing Maps, 2nd Edition, Springer-Verlag, Berlin Heidelberg New York, 1997.

[25] L.-W. Ku, A study on the multilingual topic detection of news articles. Master Dissertation, Department of Computer Science and Information Engineering, National Taiwan University, (2000).

[26] R. Kumar, U. Mahadevan, D. Sivakumar, A Graph-theoretic approach to extract storylines form search results, Proceedings of the 2004 ACM SIGKDD international conference on Knowledge discovery and data mining, 2004.

[27] K. Lagus, T. Honkela, S. Kaski, T. Kohonen, WEBSOM for textual data mining, Artificial Intelligence Review 13 (5/6) (1998) 345–364.

[28] K. Lagus, S. Kaski, T. Kohonen, Mining massive document collections by the WEBSOM method, Information Sciences 163 (2004) 135–156.

[29] C.-S. Lee, Y.-J. Chen, Z.-W. Jian, Ontology-based fuzzy event extraction agent for Chinese e-news summarization, Expert Systems with Applications 25 (2003) 431–447.

[30] D.D. Lewis, K.A. Knowles, Threading electronic mail: a preliminary study, Information Processing and Management 33 (2) (1997) 209–217.

[31] C.-Y. Lin, E. Hovy, The automated acquisition of topic signatures for text summarization, Proceedings of the 17th conference on Computational linguistic, 2000.

[32] C.J. Lin, H.H. Chen, C.C. Liu, J.H. Tsai, H.J. Wong, Opendomain question answering on heterogeneous data, Proceedings

of ACL Workshop on Human Language Technology and Knowledge Management, 2001.

[33] W.-Y. Ma, K.-J. Chen, Introduction to CKIP Chinese word segmentation system for the first international Chinese word segmentation bakeoff, Proceedings of ACL, Second SIGHAN Workshop on Chinese Language Processing, 2003, pp. 168–171.

[34] I. Mani, Recent developments in text summarization, Proceedings of the tenth international conference on Information and knowledge management, 2001.

[35] I. Mani, M. Maybury, Introduction, in: I. Mani, M. Maybury (Eds.), Advances in Automated Text Summarization, MIT Press, 1999, pp. x–xv.

[36] K.R. McKeown, R. Barzilay, D. Evans, Columbia multi-document summarization: approach and evaluation, Proceedings of Document Understanding Conferences, 2001.

[37] K.R. McKeown, R. Barzilay, D. Evans, V. Hatzivassiloglou, J.L. Klavans, A. Nenkova, B. Sable, S. Sigelman, Tracking and summarizing news on a daily basis with Columbia's newsblaster, Proceedings of the Human Language Technology Conference, 2002.

[38] S. Morinaga, K. Yamanishi, Tracking dynamics of topic trends using a finite mixture model, International conference on knowledge discovery and data mining, 2004.

[39] A. Nadamoto, K. Tanaka, Time-based Contextualized-News Browser (T-CNB), Proceedings International WWW Conference, New York USA, 2004.

[40] R. Nallapati, A. Feng, F. Peng, J. Allan, Event Threading within News Topics, Proceedings of the Conference on Information and Knowledge Management (CIKM), 2004.

[41] NIST, Available at http://www.nist.gov, (2004)

[42] C.D. Paice, Constructing literature abstracts by computer: techniques and prospects, Information Processing and Management 26 (1) (1990) 171–186.

[43] A. Rauber, LabelSom: on the labeling of self-organizing maps, Proc. International Joint Conference on Neural Networks, 1999.

[44] C.J. van Rijsbergen, Information Retrieval, 2nd edition, Butterworth press, 1999.

[45] G. Salton, C. Buckley, Term-weighting approaches in automatic text retrieval, Information Processing and Management 24 (5) (1988) 513–523.

[46] G. Salton, M.J. McGill, Introduction to Modern Information Retrieval, McGraw-Hill, NY, 1983.

[47] F. Sebastiani, Machine learning in automated text categorization, ACM Computing Survey 34 (1) (2002) 1–47.

[48] J.-Y. Shih, Y.-J Chang, W.-H. Chen, J.-H. Ho, C.-Y. Kao, Constructing securities and futures markets legal maps of Taiwan using GHSOM, International conference on digital archive technologies, 2004.

[49] R. Swan, J. Allan, Extracting significant time varying features from text, Eighth International Conference on Information Knowledge Management (CIKM'99), 1999, pp. 38–45.

[50] N. Uramoto, K. Takeda, A method for relating multiple newspaper articles by using graph, and its application to webcasting, Proceedings of 36th conference on Association for computationa linguistics, 1998.

[51] P.-F. Wu, Use of text summarization for supporting event detection. Master Dissertation, Department of Information Management, National Sun Yat-Sen University, (2002).

[52] Y. Yang, T. Pierce, J. Carbonell, A study on retrospective and online event detection, Proceedings of the Document Understanding Workshop (DUC), 1998.

[53] J.-Y. Yeh, A study on automated text summarization and its application on Chinese documents. Master Dissertation. Institute of Computer and Information Science. National Chiao Tung University, (2002).

![](/api/attachments/BRN9TRGG/fulltext/images/71fb2beb8f29a74cc3871e19e1aad46a01ba99900d14d2a24ff545929e8cdb33.jpg)

Dr. Fu-ren Lin received the PhD degree in information systems from University of Illinois at Urbana-Champaign in 1996. He is a professor at the Graduate Institute of Technology Management of National Tsing Hua University (NTHU), Taiwan. Prior to joining NTHU in 2004, Professor Lin had taught at the Department of Information Management, National Sun Yat-sen University since 1996. His research interests include

electronic commerce, e-business management, data/text mining, and knowledge management. He has published academic papers in many journals, such as Decision Support Systems, International Journal of Electronic Commerce, Electronic Commerce Research and Applications, IEEE Transactions on Engineering Management, IEEE Intelligent Systems, Journal of Organizational Computing and Electronic Commerce, and Information Processing and Management.

![](/api/attachments/BRN9TRGG/fulltext/images/78f3b6e20f88bcb07bd79f7d109a2a773c788e42768e7702f4bb467fb88f0419.jpg)

Mr. Chia-hao Liang received the B.S. degree in Management Information System from National Chung Cheng University in 2003, and the M.S. degree in Information Management from National Sun Yat-sen University in 2005. He is currently an engineer at the Institute for Information Industry (III), Taiwan. His research interests include text mining, machine learning and ITenabled services.
