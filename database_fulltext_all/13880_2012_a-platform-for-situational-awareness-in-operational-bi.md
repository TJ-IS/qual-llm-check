---
otero_id: 13880
otero_key: "FJJ3XM48"
title: "A platform for situational awareness in operational BI"
authors: "Malu Castellanos; Chetan Gupta; Song Wang; Umeshwar Dayal; Miguel Durazo"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A platform for situational awareness in operational BI

Malu Castellanos ⁎, Chetan Gupta, Song Wang, Umeshwar Dayal, Miguel Durazo

HP Labs, United States

a r t i c l e i n f o

Available online 29 November 2011

Keywords: Information extraction Correlation Unstructured data Streaming data Real-time Business intelligence Situational awareness

## a b s t r a c t

Enterprises are being swamped with data, and much of it is unstructured in origin. As these data volumes for unstructured data increase, there is a need to extract more value from them. For the purpose of gaining business insight, besides traditional text mining, we need capabilities to correlate unstructured data emanating from different sources. An important instance of this is the capability to correlate streaming unstructured web data with internal document data in near real time, which can give enterprises signi<sup>fi</sup>cant tremendous competitive advantage by enabling them to be aware of external events that can affect their business operations. This situational awareness gives business managers the opportunity to make informed operational decisions before it is too late. SIE-OBI is a platform being developed at HP Labs that responds to this need. In this paper, we describe SIE-OBI and illustrate its use via an application that provides awareness of events described in news articles that could affect the contracts of an enterprise. We present the main components of the platform architecture and illustrate their functionality to our contractual situational awareness scenario.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

In the context of an enterprise, the capability to extract valuable information from all sorts of data (i.e., structured, semi-structured and unstructured) and act instantly, either reactively or proactively, provides a tremendous competitive advantage. In particular, identifying external events and information that may affect the enterprise operations, objectives or decisions is essential to an intelligent enterprise. Today when so much of this data is available at our <sup>fi</sup>ngertips, we fall rather short in our capability to consume it at the pace with which it is generated. This is particularly true of unstructured data. Enterprises today not only have mountains of internal semi-structured and unstructured data in the form of contracts, release documents, customer reviews, etc., but also endless external data from the Web in terms of news articles, product reviews, etc. Very often, the external data is available as soon as it is generated. External sources such as social media in the form of news feeds, tweets and blogs, among others, provide the opportunity to get informed instantly, but only if we can quickly <sup>fi</sup>gure out the relevance of the information contained in them to the enterprise. One way to <sup>fi</sup>gure out the relevance is to <sup>fi</sup>nd correlations between the external and the internal data.

Typically, enterprise data warehouses (EDW) serve the vital function of being a single version of the truth for historical business reporting, but they often fall short when it comes to providing a real-time view for operational decision making. Moreover, in general, EDWs are fed from structured sources like relational databases and ignore unstructured sources like document repositories and social media feeds. As a consequence, the opportunity to gain competitive advantage from correlating unstructured historical data with the unstructured streaming data from the web in a timely manner is lost.

Large enterprises have thousands of customers and partners all over the world and a myriad of legacy contracts of a variety of types with them. Data buried in the legalese of contracts is not being used to make business decisions upon the occurrence of world events that may affect contractual relationships. Numerous examples of such events and their potential impact on business operations exist: political instability in a country (what contracts exist with suppliers based in this country?), signi<sup>fi</sup>cant <sup>fl</sup>uctuations in currency values (what contracts are denominated in this currency?), changes in commercial law (how does the change affect the risk in each contract?), mergers and acquisitions (what contracts exist with the parties involved in the merger?), a natural disaster in a region (what contracts exist with providers in that region?). If business managers were aware of events like those mentioned above and the contractual relationships that they affect, they would have the opportunity to take immediate action. For example, in case of a typhoon in the Paci<sup>fi</sup>c region where a manufacturing company has its main suppliers, the ability of extracting and correlating this information from news feeds with the suppliers' contracts in near real time would alert the business managers of a situation that may affect the business operations that depend on those suppliers. It is easy to see the complexity and infeasibility of manually correlating news feeds with contracts. Not only is the volume of news articles massive (and the number of contracts might be quite large as well) but the stream arrival rate is too fast to cope with. Furthermore, it is practically impossible to keep track of the many details in the contracts to identify the news articles that might affect them, especially to do so for every contract and every news article. This is what we call contractual situational awareness [6].

As another example, for the same manufacturing company, it is important to know what customers are saying about its new products or its competitors' products so that it can intervene in blog discussions or provide immediate feedback to the development team to make its products more competitive. That is, once a product is announced in some news site, people start commenting on its features, on blogs, tweets, review sites, etc. Analyzing these comments gives valuable insight into the customers' experience with a particular product. This is what we call sentiment awareness, and it is a very important aspect of operational customer intelligence which nowadays is a key capability that companies must have to get insight into the voice of their customers, and adapt to their needs.

In our investigations and to our surprise, we found out that scenarios like the two above are a common reality in many different domains in industry. An important requirement of situational awareness applications is to provide timely insight into these situations so that appropriate action can be taken in real time. This motivated us to develop a novel platform called SIE-OBI (Streaming Information Extraction for Operational Business Intelligence) that integrates the required functionalities to exploit relevant fast streaming information from the web by correlating it with internal (historical or slow streaming) data sources to alert business managers of situations that can potentially affect their business. In this paper, without loss of generality of the functional principles of the platform, we elaborate on its application to situational awareness in the contracts scenario. This will help illustrate the platform's capabilities.

In a nutshell, SIE-OBI situational awareness applications use novel techniques to extract relevant information from two or more disparate sources of unstructured data, typically one internal slow text stream and one external fast text stream, and to determine which elements (i.e., documents) in one stream are correlated to which elements in the other stream. Notice that our goal in developing SIE-OBI is to create a framework to facilitate the development of situational awareness applications. SIE-OBI reduces the time and effort to build data <sup>fl</sup>ows that integrate structured and unstructured, slow and fast streams, and correlates and analyzes them in near-real-time. As part of this effort we are developing algorithms for different functions, including information extraction and analytics, to be wrapped as operators of a library used to build data <sup>fl</sup>ows. In addition, we are developing techniques to optimize these <sup>fl</sup>ows with respect to different quality metrics in addition to performance (we call this, QoX-based optimization) [7].

In this paper we <sup>fi</sup>rst give an overview of the architecture of SIE-OBI in Section 2. Then, in Sections 3 and 4, we describe the functionality of some of its components for information extraction and hybrid query processing, respectively. In Section 5, we illustrate the use of the SIE-OBI platform for the contractual situational awareness application. In Section 6, we describe a prototype implementation of the application and show experimental results on real data. Finally in Section 7, we pinpoint some of the main differences with related work, and in Section 8, we conclude with our plans for ongoing and future work.

## 2. Architecture

Fig. 1 shows the proposed framework that is the basis of the SIE-OBI platform. It provides the application developer with a uni<sup>fi</sup>ed interface to build situational awareness applications, and a platform on which the applications execute. One of the design goals of SIE-OBI is to facilitate the declarative speci<sup>fi</sup>cation of the application logic as data <sup>fl</sup>ow graphs, and let the framework build the appropriate physical data <sup>fl</sup>ow (i.e., execution plan). In this way the application developer doesn't need to worry about optimizing data <sup>fl</sup>ows and is only required to specify the corresponding QoX objectives and tradeoffs [7] that he is willing to make (e.g., he may prefer to gain more accuracy even at the cost of lower performance). Then, the optimizer takes the QoX objectives into account when coming up with an execution plan (see Section 5). The SIE-OBI framework also provides runtime components to support adaptive optimization, runtime statistics gathering and monitoring, and an execution engine.

To create an application, which is the main objective of this framework, the developer needs to specify the following items through the application development interface:

1. Data Sources: Two or more data sources may be speci<sup>fi</sup>ed.

2. Processing Logic: The logical operations are expressed in the form of a data <sup>fl</sup>ow graph, which includes the extraction operations, and the queries that specify the streaming correlation and other processing required.

3. QoX objectives and tradeoffs: The QoX speci<sup>fi</sup>cation for each logical operation or a set of logical operations in the data <sup>fl</sup>ow can include accuracy, response time, throughput, freshness etc.

For the kind of situational-awareness applications described in this paper, where the data sources are textual, the main data <sup>fl</sup>ow containing the processing logic can be separated into the two stages shown in Fig. 2:

– Information extraction (IE) (processed by the information extraction component in Fig. 1)

– Hybrid query processing (processed by the hybrid SQL query processing component in Fig. 1).

To transform the structured or unstructured data sources into concept vectors required as input for the correlation, various information extraction methods are provided in a library. The library of operators is one of the main components of the SIE-OBI platform. It contains an extensible set of operators that are required for the speci<sup>fi</sup>cation of data <sup>fl</sup>ows. The application developer can specify which operators to use according to the nature of the application. The hybrid SQL query library also provides SQL-like operators over both streaming and static data. This includes the correlation operations, for which one implementation is the hierarchical neighborhood tree (HNT) based implementation. A metadata manager includes the schemas for the concepts that need to be extracted, and also the de<sup>fi</sup>nition of the concept hierarchies that are used both by the extraction operations and the HNT based correlation operations.

From the application logic (i.e., logical data <sup>fl</sup>ow), the optimizer will construct a physical plan with optimizations such as: (1) selection of physical operators for the logical ones; (2) setting of QoX knobs in some physical operators; (3) data partitioning to enable parallel execution; (4) pipelining of data <sup>fl</sup>ow and assignment of operations to physical processing nodes; (5) runtime adaptation of the physical data <sup>fl</sup>ow with current statistics; (6) QoX-based execution control through scheduling. Once this optimized data <sup>fl</sup>ow has been obtained, the execution engine executes the <sup>fl</sup>ow.

Notice that there is a distinction between logical operators that are used to specify logical data <sup>fl</sup>ows and their corresponding physical operators (i.e., implementation methods) that the optimizer uses to translate the logical <sup>fl</sup>ows into physical ones. In general, there are one or more implementations for each logical operator and it is the task of the optimizer to choose which ones to use. For example, a logical hierarchical similarity-based join could be translated into a physical HNT-based approximate join, or an entity extraction logical operator could be mapped to a genetic-based entity recognizer implementation.

In this paper we do not describe the optimizer and scheduler or the run time monitor. Instead, we focus on the information extraction and hybrid SQL query processing components in Fig. 1 and in particular, on the operators available for the corresponding data<sup>fl</sup>ow stages, shown in Fig. 2, of the kind of situational awareness applications addressed in this paper.

Next, we discuss the two different kinds of operators: operators for information extraction (Section 3) and operators for hybrid SQL query analysis (Section 4). Then in Section 5 we illustrate the use of the framework by describing a contract situational awareness application that employs the operators explained in Sections 3 and 4.

![](/api/attachments/FJJ3XM48/fulltext/images/738c6ca23c9ed6b4d69f90cd42e0c824099846b7c46742d2328a5e5954919160.jpg)  
Fig. 1. SIE-OBI framework

## 3. Information extraction (IE)

As mentioned above, one of the two main functionalities of SIE-OBI is the extraction of structured information from text streams of varying rates, typically a pair of internal and external streams. In this section we give an overview of the operation of the IE component of the platform and then describe the basic set of operators of its IE framework.

The main purpose of the IE component is to extract entities and our framework distinguishes two types: a) basic entity types and b) rolebased entity types. The <sup>fi</sup>rst type corresponds to the typical named entities such as organization names, people names and dates, but some less typical named entities such as attributes of products within a given industry are included as well. For most of the typical entities, there are open-source recognizers available, but for the non typical ones, models for new recognizers need to be built. Entities of the second type are those which have a speci<sup>fi</sup>c role, like the expiration date of a contract. Their extraction is at a higher semantic level. For instance, rather than just extracting any date that appears in the contract (often there is more than one), it is a date with a speci<sup>fi</sup>c role, expiration date of a contract, which is extracted. Supervised learning is used to train models that are capable of distinguishing entities with a given role.

Information extraction in SIE-OBI works in two phases. The <sup>fi</sup>rst one is off-line and domain-speci<sup>fi</sup>c; it is where it learns models to extract information from documents and to classify them. This phase is preceded by a speci<sup>fi</sup>cation step where the user de<sup>fi</sup>nes through a GUI the entities to be extracted from the documents in the streams and other relevant domain information such as document categories of interest. As will be explained below, we have developed <sup>fl</sup>exible models that learn regularities in the textual context of the entities to be extracted while allowing some degree of variability. The models are provided with knobs to tune according to quality requirements, for example, to trade off accuracy for performance or completeness for freshness.

![](/api/attachments/FJJ3XM48/fulltext/images/e01ff362a9511bac6702050bbed15383f76d8da372f001275ee936e3ad6c9d15.jpg)  
Fig. 2. Stages in situational awareness applications.

In the second phase, SIE-OBI applies the models learned in the previous phase to classify documents and extract information from them. It can do this either off-line for a static document collection such as a contract repository or on-line for text streams such as news feeds and tweets. Often, SIE-OBI <sup>fi</sup>rst needs to classify the documents so as to discard those which are irrelevant. For instance, news articles about sports are unlikely to affect contractual relationships between an IT company and its suppliers. Therefore, articles of irrelevant topics should be discarded before attempting to extract information from news. In addition to the extraction of entities, the IE component also extracts other kinds of information such as company names and locations, and expiration date of the contract. Fig. 3 shows the two IE phases described above for situational awareness applications.

All the functions mentioned above are implemented as operators that can be composed into data <sup>fl</sup>ows such as those illustrated later in Figs. 4 and 5. The set of operators is extensible and constitutes the essence of the IE framework. Next, we describe the operators involved in the model learning phase (Section 3.1), and then the operators that apply those models in the subsequent phase (Section 3.2).

## 3.1. Model learning operators

In the <sup>fi</sup>rst phase of the operation of SIE-OBI, different models are generated. Most of these models are learned off-line using supervised learning algorithms like those for categorizing documents and for extracting information from the text. To this end, the user <sup>fi</sup>rst needs to provide domain knowledge that the model learning algorithms will use during training. The task is performed once per domain and is facilitated through a GUI that allows the user to easily label a sample subset of the text documents (e.g., contracts, news articles, reviews) with their corresponding categories and other relevant information inside of the documents. This labeling task is accomplished by dragging and dropping items into the corresponding categories from a list of categories, pieces of text into the corresponding entity types from a list of entity types, etc. This in turn requires the previous specification of the document categories of interest and the relevant entity types to be found in the documents (these categories and entity types form the lists that appear on the GUI). Let's describe this speci<sup>fi</sup>cation task before presenting the operators of this phase:

1. Speci<sup>fi</sup>cation of the relevant document categories, which we call interesting categories. All other documents fall into a generic “uninteresting” category that is included by default. For example, the “natural disasters” category is interesting for contract situational awareness because this kind of news may impact contractual relationships as in the case of an enterprise that sells IT hardware and that has contracts with suppliers in Philippines. If a typhoon in the Paci<sup>fi</sup>c affects Philippines, the contractual relationships with these suppliers might be affected: it is likely that they won't be able to do a timely delivery of components according to the clauses in the contracts. A list of these categories becomes available to the user in the next step.

2. A sample set of documents is annotated with their corresponding categories. This set should have ample coverage over all the interesting categories and also over the generic uninteresting one. The annotated set will be used later for training the classi<sup>fi</sup>cation algorithm to produce models that will categorize the news articles.

3. Entity types to be extracted from documents in the interesting categories are de<sup>fi</sup>ned. For example, company name, catastrophe type, date and region, for news. A prede<sup>fi</sup>ned set of common entity types is available to the user for selecting those that are applicable, and if necessary he can extend it with new types.

4. Role-based entity types to be extracted from documents in the interesting categories also need to be de<sup>fi</sup>ned. For instance, the company name of the other party, its location, the contract expiration date and the contract object are useful information to identify world events that might affect contractual relationships. The company name can be used to identify news articles that mention the company, its location helps to identify news articles involving geographic areas that contain the location, the contract expiration date is useful to identify news that become more relevant as the contract expiration approaches, and the contract object is used to identify news about related objects (e.g., products). To this end, the user needs to specify the role-based entity types of interest in contracts. A list of these entity types becomes available to the user in the next step.

5. Tagging of entities. This applies mainly to role-based entity types but sometimes also to simple entity types. For example, new products with new features are coming out all the time and a dictionarybased recognizer won't catch those, so a model needs to be learned to detect new features. An example of role-based entity tagging is for the expiration date of contracts. The tagging is facilitated by dragging and dropping the items into the corresponding entity types from a list available on the GUI. This list includes typical base types as well as the role-based ones speci<sup>fi</sup>ed in a previous step. The tagged documents will be used as training set to learn extraction models for the different types of labeled entities.

Once categories and entity types have been speci<sup>fi</sup>ed, articles in the news sample have been annotated with their corresponding categories, and relevant entities in the contracts sample have been tagged, data <sup>fl</sup>ows with the appropriate operators are created to learn the required classi<sup>fi</sup>cation and information extraction models. The main operators of the learning phase are the following ones.

a) Preprocessing operators (these also apply to the second phase)

• Cleansers: there are several of them but the most useful ones are for eliminating strange symbols from documents and for eliminating stop words. Stop word elimination is applied only after the NLP operators have been applied to avoid affecting the grammatical structure of sentences.

• Normalizer: this operator uses a normalization dictionary to transform words corresponding to a same concept to its standard (also called reference) word. For example, ‘HP’ is transformed to ‘Hewlett-Packard’.

![](/api/attachments/FJJ3XM48/fulltext/images/22f1f84de7c2c396fbf14f5d9be628d7c63f19730ced3a2f87d33180c2db766f.jpg)  
Fig. 3. Information extraction phases in situational awareness applications.

![](/api/attachments/FJJ3XM48/fulltext/images/5ab03cdfd9a97f32b8979567a77235091be8b6c24c9f654c43a2616289fecf3f.jpg)  
Fig. 4. Information extraction learning data<sup>fl</sup>ow.

b) NLP operators (these also apply to the second phase)

• Tokenizer: it scans a text to identify the different tokens (e.g., a word, a number, a punctuation mark, etc.)

• PoS tagger: it tags each token with a Part-of-speech tag (e.g., ‘NN for noun, ‘JJ’ for adjective, etc.)

• Lemmatizer: it reduces variations of a word to their base form (or lemma). For example, ‘went’ is transformed to ‘go’.

• Sentence detector: it separates a text into sentences by identifying sentence boundaries.

c) Model construction operators • Feature selector: it uses Bi-normal separation [9] to select the most discriminating features to build models that have better performance. For example, the words in the documents that are better indicators of category “natural disasters”.

• Classi<sup>fi</sup>er trainer: it uses an open source SVM-based classi<sup>fi</sup>er [8] that is trained on the labeled document sample to learn models that classify documents into relevant categories. As usual with text classi<sup>fi</sup>cation [8], stop words are eliminated and lemmatization is applied beforehand using the corresponding preprocessing operators. Notice that our SVM classi<sup>fi</sup>er trainer is only one of several classi<sup>fi</sup>er trainers that are available in the operators' library for other kinds of applications. The SVM-based classi<sup>fi</sup>er is used in situational awareness because SVM models have often proved to perform the best for text categorization.

![](/api/attachments/FJJ3XM48/fulltext/images/74a13f92949162bdb2a6073057039ae4a1b1883e5acfd14550e87bc17aa1b989.jpg)  
Fig. 5. Information extraction application data<sup>fl</sup>ow.

• Model-based entity recognizer trainer (MB-ERT): information extraction of role-based entities requires models that recognize textual contexts of such entities. To this end, the operators' library includes operators that use sophisticated techniques to train models on labeled datasets. One such operator is based on a genetic algorithm (GA) that learns the most relevant combinations of pre<sup>fi</sup>xes and suf<sup>fi</sup>xes from the textual context of labeled rolebased entities of an entity type of interest. These combinations are used later to recognize the occurrence of entities of the given entity type. For this purpose a bag of terms is built from all the pre-<sup>fi</sup>xes in the context of the tagged entities in the training set. Another bag is built from their suf<sup>fi</sup>xes. For example, given the tagged sentence “The present contract due to expire bexpirationDate> December 31, 2006, b/expirationDate> is hereby terminated”. The terms due, to, and expire are added to a bag of pre<sup>fi</sup>xes of the role-based entity type expirationDate whereas the terms is, hereby, and terminated are added to its bag of suf<sup>fi</sup>xes. The bags are then used to build individuals with N random pre<sup>fi</sup>xes and M random suf<sup>fi</sup>xes in the <sup>fi</sup>rst generation and for injecting randomness in the off-springs in later generations.

Since only the best individuals of each generation survive, the <sup>fi</sup>tness of an individual needs to be computed using a function such as the count of the number of the individual's terms (i.e., pre<sup>fi</sup>xes and suf<sup>fi</sup>xes) that match the context terms of the tagged instances. More complex functions involving term features such as their parts-of-speech and their relative positions can be used as well. After a predetermined number of iterations (a round), the <sup>fi</sup>ttest individual representing the best context pattern in that round is used to derive an extraction rule that recognizes entities of the corresponding type. The antecedent of the rule is the individual's context pattern given by its combination of terms and their features. This pattern is the one that will be matched against documents in the model application phase.

Rounds continue running to obtain more extraction rules corresponding to other context patterns. The process ends after a given number of iterations or when the <sup>fi</sup>tness of the new best individual is lower than a given threshold. The rules are validated against an unseen testing set and those with the highest accuracy (above a given threshold) constitute the <sup>fi</sup>nal rule set for the given role-based entity type.

Another model-based entity recognizer trainer available in the operator library is a statistical one based on conditional random <sup>fi</sup>elds (CRF). Often the GA and the CRF trainers will have to be trained and tested to see which one performs better for the given document collection. This is easily accomplished by just including both operators in the IE learning part of the data<sup>fl</sup>ow.

• Expression-based entity recognizer trainer (EB-ERT): when open source entity recognizers are not available for extracting a base entity of a given type, an entity-recognizer trainer (ERT) operator is used to learn how to extract such entities. Most often a set of regular expressions will suf<sup>fi</sup>ce to recognize such entities in which case an EB-ERT is used to facilitate the task. If this is not possible, then a MB-ERT (see above) needs to be used to learn a model.

The association of existing entity recognizers to base entity types of interest is actually done at the time that these types are speci<sup>fi</sup>ed during the domain speci<sup>fi</sup>cation step. The GUI basically shows a menu of prede-<sup>fi</sup>ned recognizers and the user drags and drops the speci<sup>fi</sup>ed entity type into the corresponding recognizer box. The complexity of this association step comes from the need to infer additional entity types that become relevant because they are related to those speci<sup>fi</sup>ed by the user. For example, the user may have indicated that “country” is an entity type of interest; by the same token, “region” becomes also interesting since an event that takes place in a region will also affect its countries. As another example, if a user indicates that “company” is an interesting entity type, the system should infer that “holding” and “consortium” are also interesting since an event that affects a consortium also affects its company members. The solution to this requirement is in the use of hierarchies. Nowadays, hierarchies or taxonomies have been proposed for many domains as part of the semantic web effort and SEI-OBI will make use of those hierarchies to identify other relevant entities that need to be extracted. In addition, the user can specify new hierarchies through the GUI. In this way, once an entity type is speci<sup>fi</sup>ed by a user, hierarchies are traversed to infer relevant related entity types which are presented to the user so that she associates appropriate entity recognizers for them just as for the entity types that she speci<sup>fi</sup>ed.

The operators described above are composed into data <sup>fl</sup>ows such as the one shown in Fig. 4. Notice that it is the task of the optimizer to determine if and how to execute the data<sup>fl</sup>ow including identifying opportunities for parallelizing the execution of operators (e.g., classi<sup>fi</sup>er generator and entity recognizer generator may execute in parallel to reach a performance objective if there are no precedence relations between these operators or parallelizing the execution of a classi<sup>fi</sup>er trainer by partitioning the document set).

## 3.2. Model application

Once the models have been built during the off-line phase, they become readily available to do on-line classi<sup>fi</sup>cation and information extraction on the streams using the corresponding operators. Next we present these operators.

• Classi<sup>fi</sup>er: it applies the appropriate SVM model learned in the previous phase to stored or streaming data.

• Entity Recognizers (ER): these are the operators that apply models, expressions or look up dictionaries to recognize entities in the text.

o Base entity recognizers (BER): these operators extract base entities. There are two types: those that encapsulate open source recognizers (e.g., GATE) or use web services (e.g., Open Calais) to extract typical named entities (e.g., person name) and those that are built during the off-line phase for non-standard base entities (e.g., product attributes).

o Role-based ER: these operators apply the IE models (e.g., a GA-based model) learned by the MB-ERT. As mentioned above, these models can be applied both during the off-line phase on stored data, as well as during the on-line phase on streaming data. In order to speed up the search for role-based entities, SIE-OBI uses a boosting approach where base entity recognizers are used <sup>fi</sup>rst to identify the base entity types underlying the rolebased ones and then the role-based entity recognizers are applied only on the entities recognized by the base ones. For example, if a model extracts expiration dates, <sup>fi</sup>rst a date entity recognizer will identify all the dates in a contract and only then the expiration date extraction model learned in the previous phase will be applied to the context (i.e., textual neighborhood) of each recognized date. Not only does this eliminate the need to apply the model on a sliding window from the beginning to the end of each contract, but it also improves the accuracy of the extraction.

![](/api/attachments/FJJ3XM48/fulltext/images/e562f77726e5cd98d50f5d3d653c3869bf7902ee55f05bf378603e1eb4edd6ae.jpg)  
Fig. 6. An example HNT hierarchy

• Post processing operators: they apply some <sup>fi</sup>nal processing to the output of the Entity Recognizers.

o Entity Vector Mapper: the information extracted in the form of entities is assembled into descriptors to be processed by hybrid correlation queries (Section 4).

• Preprocessing operators (same ones described for the <sup>fi</sup>rst phase).

• NLP operators (same ones described for the <sup>fi</sup>rst phase).

In addition SIE-OBI has a set of adapters and readers to read text documents (contracts, news, tweets, etc.) from different sources, either stored data sources or stream data sources (e.g., news feeds and tweets).

A typical data<sup>fl</sup>ow for the IE model application (on-line) phase of a text-based situational awareness application is depicted in Fig. 5.

## 4. Hybrid query framework

The analysis challenge in situational awareness is to query both stored and streaming data. These queries could involve standard SPJ (Select, Project, Join), roll-ups and correlations. Computing correlations is a critical operation for situational awareness, and we discuss this in some more detail now.

## 4.1. Hybrid correlation

Correlation is critical to situation awareness, in fact we can formalize the situational awareness problem that we tackle in this paper as one of correlating two streams, $S _ { 1 }$ and $S _ { 2 }$ (of unstructured data) arriving at different rates $r _ { 1 }$ and $r _ { 2 }$ respectively, where $r _ { 1 } < r _ { 2 } ,$ to produce results at the rate of $r _ { 2 } .$ For example, in the contracts scenario above, the slower stream $S _ { 1 }$ can be thought of as the stored contracts collection data, and $S _ { 2 }$ as the quickly arriving news items data. Correlations in the context of unstructured data can be expressed in terms of joins. For example, we could de<sup>fi</sup>ne the following query $\left( Q _ { l } \right)$ over two streams sources $S _ { 1 }$ and S<sub>2</sub>:

$$
\begin{array}{l} \text {Select S_{1}.a, S_{2}.b From S_{1}, S_{2}} \\ \text {Where S_{1}.c = S_{2}.c,} \\ \text {And t_{1} <   S_{1}.timestamp <   t_{2} , and t_{3} <   S_{2}.timestamp <   t_{4}} \end{array}
$$

where, bS .timestamp $< t _ { 2 } ,$ and $t _ { 3 } < S _ { 2 } . t i m e s t a m p < t _ { 4 } ,$ , specify time windows for the two streams. Note that in the SQL statement above $S _ { 1 } . c ,$ S .c belong to the same dimension (attribute), but belong to two different sources, i.e., the join involves joining two streams over the same dimension.

Performing correlation via an equal-join is overly restrictive. We must allow these joins to be approximate. For example, while analyzing contracts, a natural disaster in a higher granularity location (e.g., a region) can affect contracts of suppliers located in cities in that region, and we should be able to <sup>fi</sup>nd such approximate correlations. For instance, assume a contract doesn't mention Mexico by name but is denominated in Mexican pesos, and a news article talks about a hurricane in the Gulf of Mexico. The peso belongs to a hierarchy where one of its ancestors is Mexico, and similarly Gulf of Mexico belongs to a hierarchy that also contains Mexico as an ancestor. In this case, the contract and the news article are neighbors at the level of Mexico. As a result we not only learn that these are neighbors but also that they are related through “Mexico”. We do this with hierarchical similarity. Using this operator, we can express our correlation as query (Q ), assuming that $S _ { 1 }$ is the news source and $S _ { 2 }$ is the set of contracts, as follows:

$$
\begin{array}{l} \text {Select S_{1}.a,S_{2}.b From S_{1} ,S_{2}} \\ \text {Where d_{C} (S_{1}.c,S_{2}.c) <   k And S_{1}.c = "Gulf of Mexico",} \\ \text {And t_{1} <  S_{1}.timestamp <   t_{2} , and t_{3} <  S_{2}.timestamp <   t_{4}} \end{array}
$$

where $d _ { C }$ is a distance function computed with respect to the hierarchy over dimension $c ,$ and k is some user speci<sup>fi</sup>ed threshold. If two tuples belong to the same node in the hierarchy, the distance between them is 0, if they share a common parent, the distance is 1, and if they share a common grandparent the distance is 2 and so on. Note again that, as in $Q _ { l } ,$ we joined two streams over the same dimension.

A useful generalization is to compute correlations involving more than one dimension, i.e., have distances over multiple dimensions (hence, concept hierarchies) in the where clause, so that these distances can be combined. For example, query (Q ):

$$
\begin{array}{l} \text { Select   S_{1} .a,S_{2} .b   From   S_{1} ,S_{2}} \\ \text { Where   d_{C} (S_{1}.c_{1} ,S_{2}.c_{1}) <   k_{1} and d_{C} (S_{1}.c_{2} ,S_{2}.c_{2}) <   k_{2} and S_{1}.c_{1} = "XX"} \\ \text { and   S_{1}.c_{2} = "YY"} \\ \text { And   t_{1} <  S_{1}.timestamp <   t_{2} ,and t_{3} <  S_{2}.timestamp <   t_{4} .} \end{array}
$$

In this query, we are specifying a join over two streams and over two dimensions. We can obviously combine the two distances into a multidimensional distance function de<sup>fi</sup>ned by the user.

The correlation queries speci<sup>fi</sup>ed above can include the other typical SQL operations such as projection, and aggregation. To compute correlation using the join queries speci<sup>fi</sup>ed and other standard SQL operations, we use hierarchical neighborhoods and use a structure called Hierarchical Neighborhood Trees (HNTs).

## 4.2. Hierarchical neighborhood trees

The correlation queries above can be answered in terms of hierarchical neighborhoods. These neighborhoods can be computed in terms of one or more metadata dimensions to which a document (from either source) has been mapped, for example the dimensions could be: author, date-time, location, user, product, etc. (IE is often used to extract the values of these dimensions). These standard dimensions often have associated hierarchies; for example, the time hierarchy consists of year, quarter, month, week, day, hour or the location hierarchy consists of region, state, county and city. These hierarchies are pre-built and used for correlation at the time of the execution of the data <sup>fl</sup>ow. These dimensions sometimes belong to a different type of hierarchy, i.e., this hierarchy is not a complete “part-of” hierarchy but is a specialization hierarchy. One such example is given in Fig. 6, where all tuples with “Model D” can be aggregated to “Laptop”, but there are facts about “Laptop” too in the fact table.

![](/api/attachments/FJJ3XM48/fulltext/images/cf2d84b7204eb0c30243c378f1e3c577f8a7e0ab29aa8da2fe47901d8af19ad8.jpg)  
Fig. 7. Insertion in an HNT.

![](/api/attachments/FJJ3XM48/fulltext/images/37071f558f7fe2019b8818a1379162f255350fca610ae88659e3e1c0c25f41db.jpg)  
Fig. 8. Contractual situational awareness data<sup>fl</sup>ow.

Given this, a typical schema for a document is: bdoc\_id, {metadata\_dimensions}, {other attributes}>. We store the data belonging to the hierarchical metadata dimensions in form of Hierarchical Neighborhood Trees (HNTs). HNT is a data-structure abstraction which is implemented as a hierarchical index over stored data.

We create an individual HNT for each dimension. In Fig. 6, we depict an example hierarchy that is maintained as an HNT. In this <sup>fi</sup>gure we have depicted a simple hierarchy for computer, called say, “computer hierarchy tree”. Now assume we have a contract $C _ { k }$ that mentions Model B for a desktop. Then a link to $C _ { k }$ is inserted in the corresponding node for Model B of the computer hierarchy tree. By this process, the node titled Model B will contain links to all contracts that mention Model B. In this way, each document (i.e., contract and news) is inserted into all the dimension hierarchies (hence HNTs) corresponding to its relevant metadata. Continuing with the example above, suppose the contract $C _ { k }$ contains the date dimension. Then a link to the contract would also be inserted in an HNT belonging to date at the appropriate node. HNTs are used for both the slow stream and the fast stream, i.e. each document belonging to either stream is inserted in HNTs.

HNTs have two distinguishing features: (i) use of hierarchical neighborhoods, and (ii) storage of every dimension by itself (discussed below). These two features provide us with the necessary ef<sup>fi</sup>ciency to answer queries over streaming data.

The storage in terms of hierarchical neighborhoods is especially useful while computing correlation. Storage in terms of hierarchical neighborhoods means that each node of the HNT tree de<sup>fi</sup>nes a neighborhood, and as the scale (scale here is a measurement of the level of a node in the HNT tree) increases, the neighborhood becomes smaller. Then, to <sup>fi</sup>nd points correlated with a given point, we look at the neighborhoods of interest only and hence do not have to access every point stored in the HNT. This is achieved by inserting every point into an HNT (discussed in detail later) at all levels (scales) of the hierarchy which implies that each node of the HNT contains all the neighbors of a point at that scale or level. Then queries in any one dimension can be answered by traversal of the HNT, followed by retrieval. For example, to answer query $Q _ { 2 } ,$ for k=1, we traverse the geography hierarchy to <sup>fi</sup>nd the parent of “Gulf of Mexico” to be “Mexico”, and then <sup>fi</sup>nd all contracts $\left( S _ { 2 } \right)$ that are inserted in the node named “Mexico”.

Use of a separate HNT for each dimension, provides us an ef<sup>fi</sup>cient way of composing dimensions for answering hybrid queries. Speci<sup>fi</sup>cal-$\mathsf { l y } ,$ there can be many ways of de<sup>fi</sup>ning correlation, and in particular, correlation could be computed over different sets of dimensions. For example a user might be interested in correlating only over a geography metadata dimension (for example query $\boldsymbol { Q } _ { 2 } )$ , whereas some other user might be interested in using both geography and time dimensions (for example query $Q _ { 3 } ) .$ . In general, for a data set with d dimensions, there are $2 ^ { d } { - } 1$ possible combinations of dimensions, and it is infeasible to store all such combinations. In our approach, to achieve hierarchical correlation over these many possible combinations of dimensions ef<sup>fi</sup>ciently, based on the dimensions speci<sup>fi</sup>ed in the query, the required dimensions are considered together at run time. For example, query $Q _ { 3 }$ can be answered by retrieving points at the appropriate level of hierarchy belonging to stream S using the HNTs built over dimension $c _ { 1 }$ and $c _ { 2 } ,$ and then <sup>fi</sup>nding the set of points that belong to both dimensions $c _ { 1 }$ and $c _ { 2 } .$ . If we denote the set of points over $c _ { 1 }$ by $R _ { 1 }$ , and over c<sub>2</sub> by $R _ { 2 } ,$ then the set of result of $Q _ { 3 }$ can be computed using intersection of $R _ { 1 }$ and R .

The above discussion points to three basic operations on HNT: insertion when a point enters the window of interest in a stream, deletion when a point leaves the stream, and intersection to compute neighborhoods over multiple dimensions.

In Fig. 7, we present the process of insertion, where point n is inserted in the appropriate levels in dimensions A and B. The <sup>fi</sup>gure also explains how the neighbors of point n are interpreted. For example, assuming we are dealing with contract documents, at scale 1 all the contract points are in the neighborhood. At scale 2, for dimension B the neighborhood still contains points {c1; c2; c3; c4}, but for dimension A, the neighborhood changes. At scale 3 point n has only one neighbor $c 2$ in dimensions B, and at level 4, it has no neighbors there. Deletion is essentially reverse of insertion. Intersection is a straightforward operation and is pretty ef<sup>fi</sup>cient, when each node stores points sorted by arrival time.

## 5. Applying the framework to contractual situational awareness

The goal of contractual situational awareness is to alert business managers of world events that may affect their contractual relationships with suppliers or customers potentially affected by those events. In order to do this, a data<sup>fl</sup>ow composed by different operators from the set of operators of SIE-OBI (see Sections 3 and 4) is speci<sup>fi</sup>ed at the logical level, this is called logical dataflow. The data<sup>fl</sup>ow speci<sup>fi</sup>es all the operations that are required to extract relevant information from news and contracts, correlate the extracted information to detect potentially risky situations, and send alerts to the appropriate business manager. Next, we describe the data<sup>fl</sup>ow (Fig. 8) in more detail.

![](/api/attachments/FJJ3XM48/fulltext/images/0f07d188dd0e469bd24f377011bd1ac48f8a4dce405646f41fd530dc0087601b.jpg)  
Fig. 9. Sample of data extracted from news.

(i) The <sup>fi</sup>rst step in the data <sup>fl</sup>ow is to extract relevant data from the contracts. This extracted data constitutes the seeds for the subsequent faceted search for news that may affect contractual relationships. For example, SIE-OBI could extract from the contract, the other party's company name, the expiration date of the contract and the country of the other party's location. Notice that this is not as simple as just recognizing company names, dates or country names. This is about what we call role-based entity recognition: from all the dates in the contract, only the one corresponding to the contract's expiration is the one to be extracted, and from all the mentions of company names (indeed, it is often the case that a same contract mentions companies other than the other party, typically as a result of a merger or acquisition, or when there are partnerships or parent companies), only the other party's company name is to be extracted.

(ii) The next step is to classify the articles from news feeds (e.g., New York Times RSS feeds, BBC news, Yahoo news feeds) into interesting (e.g., natural disasters like oil spill, volcano eruption, typhoon; economic crisis, political instability, etc.) and non-interesting (a single category for all irrelevant articles) categories.

(iii) From those articles in the interesting categories, the next step is to extract relevant data. For example, extract the event (e.g., oil spill) and region (e.g., Gulf of Mexico) in an article under the natural disasters category.

(iv) Concept vectors (also called descriptors) are built from the extracted entities in both the contracts and the news.

(v) Finally, the two data streams (i.e., news articles and the contracts) are correlated by inputting the concept vectors to the HNT based correlation operator to <sup>fi</sup>nd the contracts that are affected by reported events belonging to the relevant categories. What the operator does is to measure the similarity between contracts and interesting articles using the extracted information as features and extending the features along the prede<sup>fi</sup>ned hierarchies (Section 6). The similarity is de<sup>fi</sup>ned in terms of one or more of these hierarchical dimensions according to the situational awareness queries as will be seen in Section 6. Given the appropriate set of dimensions (e.g., location, date), similarity is computed in terms of hierarchical neighbors using our fast HNT streaming data structures (Section 4). The neighbor concept is used to measure the similarity of data derived from the two types of documents. If two entities (contracts or articles) have the same value for a particular dimension (e.g. both have Mexico for location variable), then they are highly correlated and will be put into one same node in the HNT. If they have different values then they will be put into different nodes in the HNT and thus they are neighbors only at the level of their lowest common ancestor, which reduces their similarity versus being in the same node. The hierarchical neighborhoods are critical to <sup>fi</sup>nding correlations between the contracts and the news items. For example, assume a contract doesn't mention Mexico by name but is negotiated in Mexican pesos and a news article talks about a hurricane in the Gulf of Mexico. The peso belongs to a hierarchy where one of its ancestors is Mexico, and similarly Gulf of Mexico belongs to a hierarchy that also contains Mexico as an ancestor. In this case, the contract and the news are neighbors at the level of Mexico. As a result we not only learn that these are neighbors but also that they are related through “Mexico”.

![](/api/attachments/FJJ3XM48/fulltext/images/8ee6efb9c345bdbfa2481cad9aa3d72bc09759976c0dfec17587a2b12845488f.jpg)  
Fig. 10. Labeling entities for training entity recognizers.

## 6. Experiments

In this section, we present some experimental results that illustrate our scenario of contractual situational awareness. First, we describe the use of the frontend of SIE-OBI and illustrate it with some screenshots Then, we explain the data<sup>fl</sup>ow and describe the hierarchies that we created for location and dates for our HNTs. Finally we present a few queries where our similarity correlation operator is used for detecting situations that may affect contractual relationships. The correlation operator uses the HNTs to detect correlations between similar entities extracted from the contracts and the news articles.

## 6.1. IE framework

The data sources that we used are: a) news from different news streams (Yahoo and BBC); b) an internal collection of contracts from an HP business division. For the news, we extended SIE-OBI with a Yahoo news feed reader and a BBC news reader. The readers insert the news into the SIE-OBI database from where the entity recognizers read them and extract the relevant entities which in turn are also inserted into the database. Fig. 9 shows a sample of the entity data that was extracted from the news of the oil spill in the natural disasters category. In particular, column G shows the places mentioned in the news article, and column H shows the dates. Column I contains the text of the news articles and column D is the data of the article. We do not show a sample of entity data extracted from contracts due to con<sup>fi</sup>- dentiality reasons, but we extracted customer company, customer location, and expiration date (all are role-based entity types) among others.

When using SIE-OBI, the user is presented with a frontend that during the of<sup>fl</sup>ine phase allows him to specify relevant domain knowledge (i.e., categories and entity types of interest) and label data for creating training sets to learn classi<sup>fi</sup>ers and entity recognizers. During the online phase, the frontend lets the user create data<sup>fl</sup>ows composed of the operators mentioned in Section 3.2, including the classi<sup>fi</sup>ers and recognizers learned in the of<sup>fl</sup>ine phase. Next, we illustrate some steps of this process.

Labeling documents for training: the front end facilitates the labeling task of entities by enabling the user to simply drag and drop entity mentions to the corresponding entity types. Fig. 10 shows that the labeled entities are displayed in different colors on the text depending on the entity types with which they are associated. For example, for contracts, the entity type “Customer” is purple and the entity type “EffectiveDate” (date that the contract becomes effective) is blue. It is easy to see that the labeling task that usually involves a cumbersome process of typing the appropriate tags for each labeled entity is reduced to a simple drag and drop operation of phrases from the text panel to the entity types panel.

The labeled documents are then input to the classi<sup>fi</sup>ers and entity recognizers described in Section 3. Once the of<sup>fl</sup>ine phase terminates and classi<sup>fi</sup>ers and entity recognizers are learned, they are added to the set of classi<sup>fi</sup>er and entity recognizer operators and become readily available to be applied on any production document collection in the given domain. Fig. 11 shows the set of role-based entity recognizers from the SIE-OBI operators library that were chosen for this particular application. In this case, the user has selected the role-based entity recognizer (GA-based) to recognize the ‘customer company’, the ‘customer location’ and the ‘expiration date’ as can be seen in the data<sup>fl</sup>ow shown in the Operators section of the GUI (bottom right panel). By selecting operators from the list (on the left side of the GUI) and con<sup>fi</sup>guring their parameters in the con<sup>fi</sup>guration panel (to the right of the operators list), the operators are composed into a data<sup>fl</sup>ow that is displayed in the Data<sup>fl</sup>ow section of the GUI.

![](/api/attachments/FJJ3XM48/fulltext/images/85ea615f96a96d16abd0871b9d4ff2dc30f138a6fe6c3c53dace01a429f66e6f.jpg)  
Fig. 11. Applying entity recognizers to relevant role-based entity types.

Once the data<sup>fl</sup>ow has run and the entities have been extracted, they are inserted into the historical database table where they become available for further processing by operators of the same or other data<sup>fl</sup>ows. In this use case, they are correlated with the entities extracted from the news articles by the HNT-based similarity correlator.

## 6.2. Hybrid queries for correlation

The Contracts table obtained from the information extracted from contracts is stored in a database with internal HNT extensions for location and date hierarchies. On the other hand, each streaming news article forms one row for the News table as a result of the information extracted from it as it arrives. When the row is inserted, it triggers the computation of the HNT extension for the news article and then the correlation with the Contract table as a hybrid query over the stored and streaming data. In Fig. 12, we show the News table (top) and the Contracts table<sup>1</sup> (bottom). A single document (news or contract) can lead to more than one row in the table if it contains more than one value for a dimension. This typically happens for the location hierarchy.

Over this framework, we performed several experiments to test the effectiveness of our method for discovering situational awareness. For correlation, we use queries based on templates presented for query $Q _ { 2 }$ and query $Q _ { 3 }$ earlier. We use the location metadata hierarchy and location and date metadata hierarchies for query $Q _ { 2 }$ and query $Q _ { 3 } ,$ respectively. All hierarchies are implemented as HNTs. Before we present the results, we discuss our hierarchies and our queries in some more detail.

## 6.2.1. Location and date hierarchy

Location is a specialization hierarchy, and as discussed earlier this means that it is not a complete part-of hierarchy. The root node which corresponds to world has three children, for the three continents for which we studied the news, North America, Europe, and Asia. Each continent has children corresponding to countries, each country has children corresponding to states and each state has children corresponding to cities. We show a fragment of the location hierarchy in Fig. 13.

<table><tr><td>location</td><td>docid</td><td>source</td><td>topic</td><td>time</td><td>title</td></tr><tr><td>Mexico</td><td>2</td><td>BBC</td><td>oil_spill</td><td>8/3/2010</td><td>What does it take to control a robot claw?</td></tr><tr><td>US</td><td>2</td><td>BBC</td><td>oil_spill</td><td>8/3/2010</td><td>What does it take to control a robot claw?</td></tr><tr><td>Gulf of Mexico</td><td>3</td><td>BBC</td><td>oil_spill</td><td>8/2/2010</td><td>BP plans to seal Gulf of Mexico oil well on Tuesday</td></tr><tr><td>Louisiana</td><td>3</td><td>BBC</td><td>oil_spill</td><td>8/2/2010</td><td>BP plans to seal Gulf of Mexico oil well on Tuesday</td></tr><tr><td>Houston</td><td>3</td><td>BBC</td><td>oil_spill</td><td>8/2/2010</td><td>BP plans to seal Gulf of Mexico oil well on Tuesday</td></tr><tr><td>US</td><td>3</td><td>BBC</td><td>oil_spill</td><td>8/2/2010</td><td>BP plans to seal Gulf of Mexico oil well on Tuesday</td></tr><tr><td>China</td><td>4</td><td>BBC</td><td>oil_spill</td><td>7/30/2010</td><td>BBC News - World News America - China struggles with the impact of the Dalian oil spill</td></tr><tr><td>Gulf Coast</td><td>4</td><td>BBC</td><td>oil_spill</td><td>7/30/2010</td><td>BBC News - World News America - China struggles with the impact of the Dalian oil spill</td></tr><tr><td>Louisiana</td><td>5</td><td>BBC</td><td>oil_spill</td><td>7/30/2010</td><td>BP boss Dudley says oil clean-up will be scaled back</td></tr><tr><td>Florida</td><td>5</td><td>BBC</td><td>oil_spill</td><td>7/30/2010</td><td>BP boss Dudley says oil clean-up will be scaled back</td></tr><tr><td colspan="6"></td></tr><tr><td>location</td><td>time</td><td>year</td><td colspan="2">filename</td><td>Customer (desensitized)</td></tr><tr><td>U.S.</td><td>4/1/2010</td><td>2010</td><td colspan="2">AISEXH~1.txt</td><td>KzpP=qxu3gg$%7c&amp;)F{UpUs</td></tr><tr><td>Thailand</td><td>4/1/2010</td><td>2010</td><td colspan="2">AISEXH~1.txt</td><td>KzpP=qxu3gg$%7c&amp;)F{UpUs</td></tr><tr><td>U.S.</td><td>10/1/2010</td><td>2010</td><td colspan="2">XXX General Agreement XXX36 20021001.txt</td><td>%37=h# ox 8DJh.oyd5%_ (Z#uTf?YP)RBoB=S1B/P)cUTX45l56</td></tr><tr><td>AMERICA</td><td>10/1/2010</td><td>2010</td><td colspan="2">XXX General Agreement XXX36 20021001.txt</td><td>%37=h# ox 8DJh.oyd5%_ (Z#uTf?YP)RBoB=S1B/P)cUTX45l56</td></tr><tr><td>Virginia</td><td>10/1/2010</td><td>2010</td><td colspan="2">XXX General Agreement XXX36 20021001.txt</td><td>%37=h# ox 8DJh.oyd5%_ (Z#uTf?YP)RBoB=S1B/P)cUTX45l56</td></tr><tr><td>Delaware</td><td>10/1/2010</td><td>2010</td><td colspan="2">XXX General Agreement XXX36 20021001.txt</td><td>%37=h# ox 8DJh.oyd5%_ (Z#uTf?YP)RBoB=S1B/P)cUTX45l56</td></tr><tr><td>America</td><td>10/1/2010</td><td>2010</td><td colspan="2">XXX General Agreement XXX36 20021001.txt</td><td>%37=h# ox 8DJh.oyd5%_ (Z#uTf?YP)RBoB=S1B/P)cUTX45l56</td></tr><tr><td>California</td><td>10/1/2010</td><td>2010</td><td colspan="2">XXX General Agreement XXX36 20021001.txt</td><td>%37=h# ox 8DJh.oyd5%_ (Z#uTf?YP)RBoB=S1B/P)cUTX45l56</td></tr><tr><td>Palo Alto</td><td>10/1/2010</td><td>2010</td><td colspan="2">XXX General Agreement XXX36 20021001.txt</td><td>%37=h# ox 8DJh.oyd5%_ (Z#uTf?YP)RBoB=S1B/P)cUTX45l56</td></tr><tr><td>U.S.</td><td>8/1/2010</td><td>2010</td><td colspan="2">YYY Support Agrmt 20050531_Compucredit.txt</td><td>%UDUIf{DR[BneQmT]WF7Z3vH=</td></tr><tr><td>USA</td><td>8/1/2010</td><td>2010</td><td colspan="2">YYY Support Agrmt 20050531_Compucredit.txt</td><td>%UDUIf{DR[BneQmT]WF7Z3vH=</td></tr></table>

Fig. 12. Figure showing the News (top) and the Contracts (bottom) tables.

Date hierarchy is a traditional complete part-of hierarchy. We were studying contracts that were over a period of 1 year and we have a hierarchy of year, month, week (week of month) and date. A contract's expiration date is inserted in the corresponding HNT, the intuition being that the closer a contract is to completion, the more important it is for the corporation to know, if it will be affected.

## 6.2.2. Queries

As mentioned earlier we experimented with queries based on the template query $Q _ { 2 }$ .

Select $S _ { 1 } . a , S _ { 2 } . b$ From $S _ { 1 } , S _ { 2 }$

Where $d _ { C } ( S _ { 1 } . c , S _ { 2 } . c ) < k A n d S _ { 1 } . c = " X X " ,$

And $t _ { 1 } { < } S _ { 1 } . t i m e s t a m p { < } t _ { 2 } ,$ and $t _ { 3 } < S _ { 2 } .$ .timestamp b t<sub>4</sub>

And query $\boldsymbol { Q } _ { 3 } \mathrm { : }$

Select $S _ { 1 } . a , S _ { 2 } . b$ From $S _ { 1 } , S _ { 2 }$

![](/api/attachments/FJJ3XM48/fulltext/images/5c6f7202bc59e1cd2cbff7f58e5e7aa4b463bd276f8d04c03dd069c197248486.jpg)  
Fig. 13. Fragment of the Location hierarchy.

![](/api/attachments/FJJ3XM48/fulltext/images/5f0d8f1d4b1e8eac13c170652a0894d78bc9d5dbf091e6153cbef7ca7f8eb66d.jpg)  
Fig. 14. Results for Query Set 1.

Where $d _ { C } ( S _ { 1 } . c _ { 1 } , S _ { 2 } . c _ { 1 } ) < k _ { 1 }$ and $d _ { C } ( S _ { 1 } . c _ { 2 } , S _ { 2 } . c _ { 2 } ) < k _ { 2 }$ and $\boldsymbol { S } _ { 1 } . \boldsymbol { c } _ { 1 } = " \boldsymbol { X } \boldsymbol { X } "$ and $S _ { 1 } . c _ { 2 } { = } ^ { * } Y Y ^ { * }$

And $t _ { 1 } { < } S _ { 1 }$ .timestampbt , and $t _ { 3 } < S _ { 2 } . t i m e s t a m p < t _ { 4 } .$

In the <sup>fi</sup>rst set of queries $Q S _ { 1 }$ , instead of $" X X "$ we use the location mentioned in the news article as the argument for the ‘where’ clause. If the article mentions two locations such that one is an ancestor of the other, we use the descendant as the argument for the query. The correlation is performed over the location hierarchy and we use three different values for k, $k _ { L } = 0 , 1 , 2 ,$ to obtain three queries for this set.

In the second set $Q S _ { 2 } ,$ as shown in query $Q _ { 3 }$ we use two dimensions. For our purpose they are the location and the date hierarchies. For location, just as for the <sup>fi</sup>rst set, we se $\ R = k _ { L } = 0 , 1 , 2$ and for the date hierarchy we use $k = k _ { D } = 1 , 2 ,$ , which correspond to week and month respectively (given that the news article date is a speci<sup>fi</sup>c day). This gives us a set of six queries. Using $k _ { D } = 0$ is too restrictive since a date match (meaning the date of the news is the same as the date the contract expires) is not very meaningful. This choice points to the usefulness of allowing approximate equalities in the joins to do similarity correlation.

## 6.3. Experimental results

Next we present our results for $Q S _ { 1 }$ and $Q S _ { 2 } .$ For $Q S _ { 1 }$ we present the results for several news items. Fig. 14 shows a comparison of the number of contracts correlated with a set of BBC news articles on selected topics for $k _ { L } = 0 , 1 , 2$ . Each point on the x-axis is an individual news article and y-axis indicates the number of correlations found. The diamonds show $k _ { L } = 0 ,$ the squares show $k _ { L } = 1 ,$ and the triangles show $k _ { L } = 2 .$ It can be seen that as expected the number of correlations increase as the value of $\dot { k } _ { L }$ increases since we are relaxing the requirements for correlation and allowing matches higher up in the hierarchy. We further present results for selected news items in Fig. 15, to clearly highlight the change in number of contracts as $k _ { L }$ increases.

In Fig. 16, we present results for two queries from $Q S _ { 2 } ,$ which present the effect of varying $k _ { L }$ and $k _ { D }$ together. We show $k _ { L } = 1 ,$ $k _ { D } = 1 \ a n d \ k _ { L } = 1 , k _ { D } = 2$ . It can be observed that as $k _ { D }$ increases we get a higher number of matching contracts. Also note that as compared to results for Query Set 1, we get fewer matching contracts since we are correlating over two dimensions. This is both expected and desirable.

We now give examples of the advantage of using our relaxation of equalities, i.e., we allow correlation higher up in the HNT hierarchy. For instance, BBC had a news article of an oil spill in the Gulf of Mexico near New Orleans on 25/07/2008, titled “BBC NEWS | Americas | Ships blocked after US oil spill”. Since the disaster reported in this article referred to New Orleans, strict match results in 20 contracts (those where the customer is located in New Orleans). When going one step up the location hierarchy to Louisiana, which is the parent of the location “New Orleans” in the location hierarchy we get 5 more contracts. This is sound since New Orleans is a major port in Louisiana and ships blocking may affect the contracts with customers in Louisiana and not only those in New Orleans. As another example, there was a BBC news about the recent Greek crisis, titled “BBC News – Today – No German stomach for Greek bailout” on 16/02/2010. When we did a strict match for Greece in a 1 month window, we found 4 contracts. As we step up the location hierarchy to Europe, we got three more contracts. This is again sound, as we know that the Greek economic crisis affected all of Europe.

![](/api/attachments/FJJ3XM48/fulltext/images/3402d32e16aa17c2a29c75db09a9fd93ebb9be8088717277c8d316af7c2434ed.jpg)  
Fig. 15. Results for some selected news items for Query Set 1.

![](/api/attachments/FJJ3XM48/fulltext/images/faaa867fbdc2f7602739aff6e0f306c438809e0313cfaf28c6c6292a0124970f.jpg)  
Fig. 16. Results for selected queries in Query Set 2.

## 7. Related work

The main contribution of this work is the proposed framework to easily develop situational awareness applications. This requires a platform with a rich set of components that ingest data streams of varying speeds and execute optimized data <sup>fl</sup>ows to perform information extraction and real-time analytics, in particular, hybrid correlation, on them. In this regards we are not aware of any platform that includes all the functionalities and features that SIE-OBI offers for situational awareness applications. Streaming systems [4] that have emerged over the last decade such as Aurora [1], Chaos [10] and System S [18] do not incorporate, to the best of our knowledge, all the functionalities that SIE-OBI provides.

Since the framework requires a rich library of operators we also developed novel algorithms underlying some of these operators, in particular, for information extraction and correlation.

With regards to information extraction, although many proposals for IE models exist (for a good survey see [20]), our experiments revealed that they do not work well for large documents nor they are <sup>fl</sup>exible enough to cope with variability in the text surrounding the information to be extracted in typical situational awareness applications. Using such models we ended up doing a lot of manual tuning. This led us to take the decision of creating our own algorithms for the high semantic level required for role-based entity extraction. Nevertheless, we include in the operators' library an entity recognizer trainer based on conditional random <sup>fi</sup>elds (CRFs) which is the most popular state of the art technique and may perform better than our GA-based trainer for some document collections. In contrast, for named entity extraction there are commercial and open-source frameworks and suites with recognizers well trained on vast collections of text or even manually created and with good coverage of some of the most popular named entities (e.g. person name). Some well-known open source ones are OpenCalais [14] and Gate [13] which are used in SIE-OBI.

Correlation is a well studied problem (refer to [16]), and is studied in time series literature as computing autocorrelation or cross-correlation functions [21]. In our problem however, instead of traditional time series data, our data is in form of events. There has been work in the data mining community on “correlation analysis” [12] over event data. In this community, the underlying problem studied [17] (also called “episode detection”) is the following: given a set of ordered events, which set of events (ordered or unordered) occurs frequently together within a time window. In other words correlation is understood be sets of events that occur together. This problem is also close to the problem of detecting sequential patterns [2]. Another variation [5] is to <sup>fi</sup>nd “correlation rules”, where in given prede<sup>fi</sup>ned sets of objects (could be events), the challenge is to <sup>fi</sup>nd subsets that are correlated with each other. There has been much work in extending these underlying ideas to problems such as motif mining [19], etc., including extending some of those for a streaming setting [12] (the setting we are interested in). Our problem is different from all these. We are interested in pairs of events coming from two different streams that are correlated, rather than <sup>fi</sup>nding sets of events from the same stream that occur frequently together. In other words, our de<sup>fi</sup>nition of correlation is that two events are correlated if their “distance” on some attributes of interest is within a certain threshold. Given this, the closest approaches would be those that are interested in <sup>fi</sup>nding nearest neighbors ef<sup>fi</sup>ciently over streams [15]. Similarly, the problem of outlier detection over streaming data, (such as presented in [3,11]), could require <sup>fi</sup>nding nearest neighbors. To the best of our knowledge these data mining approaches are interested in <sup>fi</sup>nding Euclidean distance. They do not consider the case of heterogeneity of fast streams and slow streams. In this paper we propose a novel solution with HNTs to measure the correlation among the contracts in a slow stream and news items in a fast stream based on computing hierarchical categorical distances, in an ef<sup>fi</sup>cient fashion.

## 8. Conclusion

In this paper we have presented a prototype design and implementation of a platform for streaming information extraction and analytics (SIE-OBI). The end goal of SIE-OBI is to reduce the time and effort to build data <sup>fl</sup>ows that integrate slow and fast streams of structured and unstructured data, and to correlate and analyze them in near-realtime. In this paper, we give an overview of the architecture and describe the functionality of some of its main components. We illustrate the ideas by expanding on the contract awareness application where a slow stream (contracts) and a fast stream (news feeds) are integrated into a data <sup>fl</sup>ow. We have illustrated the use of the platform with real news feeds from two sources and an internal contracts database.

Experiments to measure how well SIE-OBI can handle different stream arrival rates and case studies to <sup>fi</sup>nd out how useful it is ongoing. In particular, we are investigating the applicability of the platform for other situational awareness scenarios such as sentiment awareness. We also continue to work on improving and extending the machine learning and analytics algorithms. Finally, work on the QoX optimizer and run-time performance monitoring components is also ongoing.

## Acknowledgments

We thank Cornelio Inigo for his help with the implementation of adaptors for SIE-OBI.

## References

[1] D.J. Abadi, et al., Aurora: a new model and architecture for data stream management, VLDB Journal 12 (2) (2003) 120–139.

[2] R. Agrawal, R. Srikant, Mining sequential patterns, Proc. Of 11th ICDE, 3–14, Taipei, Taiwan, 1995.

[3] F. Angiulli, F. Fassetti, Detecting distance-based outliers in streams of data, CIKM, 2007, pp. 811–820.

[4] B. Babcock, S. Babu, R. Motwani, J. Widom, Models and issues in data streams, PODS, 2002, pp. 1–16.

[5] S. Brin, R. Motwani, C. Silverstein, Beyond market baskets: generalizing association rules to correlations, SIGMOD, Arizona, 1997.

[6] M. Castellanos, U. Dayal, FACTS: an approach to unearth legacy contracts, Proc. First International Workshop on Electronic Contracting (WEC-04), San Diego, CA, July 2004.

[7] U. Dayal, M. Castellanos, A. Simitsis, K. Wilkinson, Data integration <sup>fl</sup>ows for business intelligence, Proc. EDBT 2009, March 2009, St. Petersburg, Russia, ACM International Conference Proceeding Series 360 ACM 2009.

[8] R. Feldman, J. Sanger, The Text Mining Handbook: Advanced Approaches in Analyzing Unstructured Data, Cambridge University Press, New Yourk, NY, 2007.

[9] G. Forman, An extensive empirical study of feature selection metrics for text classi-<sup>fi</sup>cation, Journal of Machine Learning Research 3 (2003) 1289–1305.

[10] Gupta, et al., Chaos: a data stream analysis architecture for enterprise applications Proc. IEEE Conference on Commerce and Enterprise Computing, 2009, pp. 33–40, 2009.

[11] C. Gupta, R.L. Grossman, Outlier detection with streaming dyadic decomposition, Industrial Conference on Data Mining, 2007, pp. 77–91.

[12] J. Han, H. Cheng, X. Dong, X. Yan, Frequent pattern mining: current status and future directions, Data Mining and Knowledge Discovery 15 (2007) 55–86.

[13] http://gate.ac.uk/ie.

[14] http://www.opencalais.com.

[15] N. Koudas, B.C. Ooi, K.-L. Tan, R. Zhnag, Approximate NN queries on streams with guaranteed error/performance bounds, Proc. Of 13th VLDB, 2004, pp. 804–815.

[16] H.O. Lancaster, The Chi-squared Distribution, John Wiley & Sons, New York, 1969.

[17] H. Manilla, H. Toivonen, A. Verkamo, Discovery of frequent episodes in event sequences, Data Mining and Knowledge Discovery 1 (1997) 259–289.

[18] N. Jain, et al., Design, implementation, and evaluation of the linear road benchmark on the stream processing core, Proceedings of ACM SIGMOD, 2006.

[19] P. Patel, E. Keogh, J. Lin, S. Lonardi, Mining motifs in massive time series databases, Proc. Second IEEE International Conference on Data Mining (ICDM'02), 2002, p. 370.

[20] S. Sarawagi, Information extraction, Foundations and Trends in Databases, Vol. 1, No. 3, 2008, pp. 261–377.

[21] R.H. Shumway, D. Stoffer, Time Series Analysis and Its Applications, Springer, New York, 2006.

![](/api/attachments/FJJ3XM48/fulltext/images/5ff96b88361779a35c50438cac35f7c96b0021a112c72561a6245868a1ee8790.jpg)  
Dr Malu Castellanos is a senior researcher at Hewlett-Packard Labs where she has been developing and applying data management techniques and analytics for solving business problems related to different aspects of business intelligence. She is an active member of Program Committees (including VLDB, SIGMOD and ICDE), journal review boards and has served in the organization of international conferences. She is a member of the Executive Committee of IEEF Technical Committee of Data Engineering. Her current interests are real-time business intelligence, analytics, text mining, management of large volumes of data, and databases where she has numerous of publications and patents.

![](/api/attachments/FJJ3XM48/fulltext/images/434684e0d29caa795d11a199c055c8f631222c32e0f1431ac696309c51dedf13.jpg)

Dr. Umeshwar Dayal is an HP Fellow at Hewlett-Packard Laboratories, Palo Alto, California, where he leads research efforts in Live Business Intelligence and Analytics. Umesh has over 30 years of research experience in data and information management. Prior to joining HP Labs, he was a senior researcher at DEC's Cambridge Research Lab, Chief Scientist at Xerox Advanced Information Technology and Computer Corporation of America, and on the faculty at the University of Texas-Austin. He received his PhD from Harvard University. He has published over 180 papers and holds over 45 patents. He has served on the Editorial Board of several international journals, edited two books, and chaired and served on the Program Committees of numer-

ous conferences. He has been a member of the Board of the VLDB Endowment, the Steering Committee of the SIAM Data Mining Conference, and the Executive Committee of the IEEE TC on E-Commerce. Currently, he is on the Steering Committees of the IEEE International Conference on Data Engineering and the SPIE Visual Data Analysis Conference. Umesh is an ACM Fellow, and the recipient of the 2010 Edgar F Codd Award from ACM SIGMOD for his contributions to data management.

![](/api/attachments/FJJ3XM48/fulltext/images/65ff804406153f411ad5512b63a2e50e6f7c16625b0980bac822af781dea0f9a.jpg)

Dr. Chetan Gupta is a senior research scientist at Hewlett-Packard Labs. Chetan is currently working on analyzing large volumes of fast moving streams for identifying and acting upon complex events and patterns, a technology that will be key to the next generation of business intelligence. Chetan has published numerous papers and patents in the area of data mining, algorithms, complex events processing, situational awareness and workload management.

![](/api/attachments/FJJ3XM48/fulltext/images/13a7518a265dcc7dacb8e490dcfe002d252cc0ec7624b15c2c070784926fb4ef.jpg)

Dr. Song Wang is currently working with Hewlett-Packard Co. His research interests focus on Operational/- Real-time Business Intelligence, Stream Query Processing, Scalable and Adaptive Data Processing, Distributed Query Processing, XML and Web Query Processing.

![](/api/attachments/FJJ3XM48/fulltext/images/6dffd6a4b5499526e6a0e966c70506a21ca849b76249fb1a0d3b621e394aaec1.jpg)

Miguel Durazo studied computer science at the University of Sonora, Mexico, graduated in 2008, Since then he has been a research assistant for Hewlett-Packard Laboratories where he has been implementing and experimenting with techniques resulting from labs research as well as their applications.
