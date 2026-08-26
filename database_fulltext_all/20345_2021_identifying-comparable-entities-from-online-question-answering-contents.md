---
otero_id: 20345
otero_key: "3SWZH27J"
title: "Identifying comparable entities from online question-answering contents"
authors: "Jin Zhang; Liye Wang; Kanliang Wang"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103449"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identifying comparable entities from online question-answering contents

![](/api/attachments/3SWZH27J/fulltext/images/0c6bc61d84221fa2fa1ee74047178a56d536446c29ffe9137a5d87642c4ff443.jpg)

Jin Zhang, Liye Wang, Kanliang Wang

School of Business, Renmin University of China, Beijing 100872, China

## A R T I C L E I N F O

Keywords: Comparable entity identification Question-answering contents Entity ranking Comparison network

## A B S T R A C T

As an emerging platform, online question-answering (Q&A) communities are becoming valuable corpus sources that reflect the opinions of expert consumers on comparable entities. In this study, a novel method-Identifying Comparable entities from online Question-Answering contents (ICQA)-is proposed to effectively extract com parable entities from online Q&A communities. In ICQA, candidate entities are firstly extracted by utilizing the advantages of pattern-based methods and supervised learning-based methods. An entity comparison network is then built by considering the credibility difference and entity relatedness in Q&A contents to analyze compet itiveness between entities and extract comparable entities from candidate entities accordingly. Thus, within the same method framework, comparable entities and their competitiveness ranks can be simultaneously identified for a given entity specified by managers or consumers. By taking the automotive industry as the experimental background, the effectiveness of ICQA is demonstrated with comprehensive experiments regarding comparable entity identification and comparable entity ranking. Experimental results demonstrate that compared with stateof-the-art methods, ICOA can identify more accurate and broader comparable entities, find novel entities ignored by other methods, and provide a more solid comparable entity rank-features that are deemed desirable and applicable for both managers and consumers in making rational decisions based on online Q&A contents.

## 1. Introduction

Comparable entities, such as “BMWG” and “Mercedes-Benz”, are entities that share a common utility and meet the needs of the same groups of consumers [14,41]. In terms of mining a complete and accu rate set of comparable entities for a given entity, a comparable entity identification method plays an important role for both consumers and companies in the fast-moving market. Consumers usually find and compare products with similar prices, functions or qualities from online information before making a purchase decision [8]. However, the pro cess of collecting comparative information requires a substantial body of domain knowledge, and online information is quite complicated and overloaded. Bounded by time and cognitive ability [34], it is difficult for consumers to efficiently identify comparable entities. This raises the strong need for effective comparable entity identification methods.

Comparable entity identification methods are also vital for com panies, who must develop knowledge about entities comparable to their products to maintain a competitive advantage. Existing management research has shown that managers judge comparable entities based on products’ mental representations of supply sources and consumers in their minds [7]. However, the number of comparable entities managers can name is limited, and they are unable to process information in large quantities [4]. Comparable entity identification methods can help managers establish market structures and industry boundaries [4], and they can provide a basis for marketing activities such as product design and positioning, channel development, and pricing policies [3]. More over, identifying comparable entities is conducive to building a keen awareness of the competitive environment to help companies cope with potential risks and attacks [34,30].

Therefore, some recent studies have been devoted to identifying comparable entities and extracting comparative relations. User-Generated Content (UGC) nowadays has become a valuable corpus source for comparable entity identification from the consumers perspective. Some recent studies have focused on identifying compara ble entities by utilizing UGC, to fully express consumer opinions about comparable entities. Such comparable entity identification methods can be categorized into learning-based methods and pattern-based methods. While helpful in identifying comparable entities, these two kinds of methods still suffer from some defects. Learning-based methods require a pre-given candidate entity set and lots of manual annotations to train the learning model, which are time-consuming and sensitive to subject cognition [46]. Pattern-based methods do not need manual annotations, but they only deal with comparable entity identification in comparative sentences. In contents where co-occurrence patterns are scarce or even non-existent, pattern-based methods are unable to discover comparative relations [41]. Moreover, in most cases, entities discussed across con tents are also relevant and comparable. Existing pattern-based methods ignore this broader form of comparison, such that comparable entities identified by such methods are not sufficiently comprehensive [41]. Hence, a more effective comparable entity identification method is needed that can overcome the limitations of existing methods.

In addition, there are still some concerns with UGC, leading to stateof-the-art methods being not effective enough for UGC applications. First, contextual relatedness of UGC is neglected by existing studies, i.e., surrounding sentences are related [15], and entities discussed separately in non-comparative statements are still likely to be comparable. Existing studies treat sentences in the same content as independent individuals and only regard entities discussed in the same sentence as comparable. Second, the quality of UGC varies in an open setting [28]. Existing studies simply treat all the information equally, which may include in accuracy in the identification results.

To overcome the limitations of existing methods and the concerns above, in this study, we focus on the following research question: How do we propose a more effective comparable entity identification method that can identify comparable entities from both comparative sentences and noncomparative sentences of UGC with little manual work? We take Q&A contents as a typical kind of UGC for the research data. Recently, Q&A communities like Yahoo!Answers, Quora, Naver, and Zhihu are attracting more and more expert users to contribute knowledge about product selection and share shopping experiences of similar products [51]. They have built extensive and valuable archives of high-quality Q&A contents, where information seekers can acquire first-hand infor mation about products by searching through the Q&A contents that satisfy their information needs [49]. Previous studies reveal that the quality of some Q&A contents can sometimes reach or even surpass the information quality given by library reference services and experts [10]. Therefore, Q&A contents have been valuable repositories for various research tasks like knowledge mining, question-answering searches [53], and especially for comparable entity identification. As a typical type of UGC, Q&A contents also have the two concerns with UGC mentioned above. It is worth noting that the contextual relatedness of Q&A contents has a special form: i.e., questions and answers are also semantically related to each other [15]. Comparable entities not only exist in the same question or answer, but also exist across questions and answers. Thus, targeted technical treatment needs to be taken into ac count for the relatedness of Q&A contents.

This study proposes a novel comparable entity identification method, called Identifying Comparable entities from online Question-Answering contents (ICQA). The method that not only identifies en tities comparable to a given entity, but also analyzes the competitiveness between entities and ranks them accordingly. The contributions of the proposed method includes the following: (1) Without manually labeled training data or a pre-given entity set, ICQA can identify comparable entities exiting in both comparative and non-comparative sentences. (2) ICQA can capture broader comparison relations between entities by considering the contextual relatedness of Q&A contents. And (3) ICQA eliminates the influence of quality variation through the social behavior in UGC. The effectiveness of ICQA is evaluated and demonstrated with real-world Q&A community data. The results of extensive experiments show that compared with current baseline methods, the precision and recall values of comparable entities identified by ICQA can reach a higher level, and furthermore ICQA can find novel comparable entities ignored by other methods. These features are desirable to both managers and consumers in meeting their needs. Moreover, ICQA can better measure the competitiveness between entities and provide a more reli able comparable entity rank.

This study belongs to the paradigm of design science. The compa rable entity identification problem is a known application area whose significance has been well recognized for both consumers and managers. However, existing solutions are not effective enough and ignore the common features of UGC. In response to the limitations of existing so lutions, this study formulates the problem in the Q&A context and proposes a more effective method to improve the solution. Specifically, in the proposed method, an entity identification process is designed to solve the completeness problem of pattern-based methods and the manual annotation problem of learning-based methods. In the design of competitiveness analysis, the proposed method involves broader com parison patterns and utilizes the votes that the Q&A pair receives into the comparison network. This makes up for the neglect of contextual relatedness and quality variation in UGC by existing methods. The proposed method is evaluated with real-world data experiments, which provide evidence of its improvement over current solutions. Therefore, from the viewpoint of design science research, the contribution of the study can be positioned in the “improvement” quadrant [9].

The remainder of this paper is organized as follows. Related work is discussed in Section 2. Section 3 introduces the proposed comparable entity identification method in detail. Next, a real descriptive example and algorithmic details about comparable entity identification with the proposed method are provided in Section 4. In Section 5, experimental results of comparable entity identification and competitiveness analysis are illustrated. Finally, conclusions and future work are summarized in Section 6.

## 2. Related work

Studies related to this work can be grouped into four categories: pattern-based comparable entity identification methods, learning-based comparable entity identification methods, comparative aspect and di rection extraction, and studies related to Q&A communities.

## 2.1. Pattern-based comparable entity identification method

Pattern-based methods are the mainstream research efforts of com parable entity identification. Pioneered by the work of [18], these research efforts assume that comparable entities are frequently mentioned together in the same comparative sentence. Some studies proposed mining comparable entities through a set of pre-defined lin guistic comparative patterns such as “A is better than B”, “A versus B”, and so forth [2]. Based on that, bootstrapping methods were further proposed to heuristically identify comparable entities. In these methods, parts of comparable entities were initially identified according to pre-defined patterns, based on which new comparative patterns were further extracted. The newly discovered patterns were then utilized to learn more comparable entities. The extraction process terminated when no new patterns or entities were identified. Depending on bootstrapping methods, [13] proposed a method for comparable entity identification from web pages and query logs. [16] presented a comparable entity mining algorithm and constructed a comparable entity graph over query logs. Regarding comparative questions, [26] developed a weakly su pervised method for identifying comparable entities. [36] proposed a comparable entity identification method based on the pre-defined comparative patterns for tables, lists, and free texts in corporate prospectuses.

## 2.2. Learning-based comparable entity identification method

Learning-based methods include discriminative learning models and generative learning models. Discriminative learning methods infer whether there is a comparative relation between two given entities with features extracted from online data. Specifically, [29] constructed a network from online news, where structural attributes were extracted and utilized to discriminate the relation between two companies. [33] proposed three online isomorphism metrics based on firms’ website contents and linkage structures, and then verified that they were good indicators in comparative relation classification. Utilizing the long short-term memory(LSTM) model, [1] captured the inter-dependencies of entities, comparison aspects, and comparison directions in compar ative sentences and synchronously identified them. Generative learning models are the other type of method used in learning-based comparative entity identification. [48] proposed a two-level conditional random field (CRF) model to extract comparative relations between products from customer reviews. [50] bridged the Twitter network with a patent network and trained a topical factor graph model to classify the relations between entities. [38] designed a dynamic probabilistic model to characterize the topical evolution of entities that could be directly used for topic-level comparative relation discovery.

## 2.3. Comparative aspect and direction extraction

Based on comparable entity identification, some studies further analyzed comparison relations from the perspectives of comparative aspect extraction and comparison direction identification between en tities. [41] defined the competitiveness between entities based on the overlap of product aspects mentioned in online reviews. [46] conducted competitiveness analysis through conjoint keywords of two entities in web search logs. [39,40] proposed a generative model for comparative sentences in online reviews to model comparative directions of com parable entities concerning product aspects. [45] identified product advantages by comparing the topic differences between the positive and negative reviews of different entities. [27] compared review sentiments of different products and identified competitive advantages of an entity as the aspects that obtain much higher sentiment orientation than its comparable entities. [24] proposed an improved hierarchical deep neural network to infer user preferences for comparable entities from online reviews.

## 2.4. Question-answering community

Q&A communities and contents have recently attracted considerable attention from researchers and practitioners. Part of this research effort has involved attempts at improving efficiency of user access to infor mation, and can be divided into three aspects. One is to find potential expert users who may answer a given question [54]. The second is question retrieval to find questions related to a user’s query [55]. The third is answer ranking, which involves extracting a set of powerful features such as structural, textural, and community features to compute global scores of answers, and then presenting high-scoring answers to users [47], or learning answers suitable for queries with supervised machine learning models [31].

Another type of research treats Q&A communities as knowledge sharing platforms and explore user behavior on the platforms. [20] found that users’ active participation in Q&A communities centered on external artifacts, pursuit, and automatic activation of goals. Self-presentation, peer recognition, and social learning were also shown to play essential roles in user knowledge-contribution behavior [17]. Meanwhile, social behavior in knowledge sharing platforms is another aspect of recent studies related to Q&A communities. [44] found that user-to-user social networks enhanced social ties and encouraged votes and additional high-quality answers. [32] pointed out that stronger social ties contributed more to overall user knowledge. Moreover, [52] examined the impact of user expertise on knowledge consumption satisfaction.

Even though there are a large number of studies related to Q&A communities, they only focused on information retrieval or the inter pretation of user behaviors within the communities. The value of knowledge accumulated in the communities as the so-called wisdom of the crowd and its applications in other business fields are rarely considered, especially in comparable entity identification.

## 2.5. Summary

In sum, pattern-based comparable entity identification methods only concentrate on comparative statements, and are unable to discover comparative relations when the co-occurrence patterns are scarce or even non-existent [41]. As for learning-based methods and aspect-based analysis, they are mainly devoted to addressing comparative relation mining, aspect extraction, and entity ranking rather than comparable entity identification. These methods also require a large amount of manual annotation work or a pre-given entity set, which consumes a lot of time and resources in practical applications and limits the effective ness and efficiency. Furthermore, both pattern-based methods and learning-based methods ignore the semantic relatedness of entities mentioned separately in the same content and the quality variation of user-generated contents. Thus, the identified comparable entities are incomplete and may include inaccuracy.

Facing these limitations, this paper proposes a novel method that can identify comparable entities from both comparative sentences and noncomparative sentences without manual annotations or a pre-given entity set. The proposed method is thus more suitable for UGC, and captures broader comparison relations between entities by considering the contextual relatedness of UGC and distinguishing contents with different qualities to improve the accuracy.

## 3. Comparable entity identification method

In Q&A contents, users frequently ask questions like “With a budget of \$30,000, which SUV is suitable for me, except for Honda CR- $. V ? ^ { \prime \prime }$ to seek advice in Q&A communities. In different answers to this question, users may list several SUV entities, such as “JEEP Cherokee”, “VW Tiguan” and “Buick Envision”, and comment on their advantages and disadvantages. Under these circumstances, comparable entities do not co-occur in the same sentence, but rather in the same answer or across the question and answers. This is different from previous literature, which assumes that comparable entities often co-occur in the same comparative sentences. Such comparative statements are only a small part of consumer opinion expressions in Q&A contents [41]. Therefore, broader entity relatedness is considered in this study, and a two-stage method, called ICQA, is proposed, which helps users identify compara ble entities from the consumers’ perspective.

The framework of the ICQA method is shown in Fig. 1, where the two ovals represent the candidate entity identification stage and the competitiveness analysis stage, respectively. The first stage aims to extract candidate entities existing in Q&A contents related to the target domain. The extracted candidate entities may have potential relations with the focal entity at different levels of competitiveness. Thus, in the second stage of ICQA, a comparison network is constructed to model comparative relations between candidate entities, and to measure their competitiveness accordingly. As a result, ICQA identifies a subset of the candidate entities with higher competitiveness as comparable entities and outputs them to users. In the next subsections, the two stages of ICQA are elaborated in detail.

## 3.1. Candidate entity identification

The candidate entity identification of ICQA possesses the following two advantages:

(1) Less sensitive to manual annotations: only the co-occurrence patterns and entity patterns need to be pre-defined manually.

(2) More complete results: entities existing in the whole Q&A con tent can be identified, not just those in comparative statements.

Let T denote the set of Q&A contents in a Q&A community. Each question-answer pair in T can be represented by a tuple $( q _ { i } , a _ { i } ^ { k } , w _ { i } ^ { k } )$ , where $q _ { i }$ denotes the i-th question, $a _ { i } ^ { k }$ denotes the k-th answer to $q _ { i } ,$ and $w _ { i } ^ { k }$ is the number of votes $a _ { i } ^ { k }$ received from users on the platform. Questionanswer pairs randomly selected from T comprise the training corpus $T _ { t } = \{ ( q _ { 1 t } , a _ { 1 t } ^ { k } , w _ { 1 t } ^ { k } ) , ( q _ { 2 t } , a _ { 2 t } ^ { k } , w _ { 2 t } ^ { k } ) , . . . , ( q _ { \mathrm { j t } } , a _ { \mathrm { j t } } ^ { k } , w _ { \mathrm { j t } } ^ { k } ) \}$ }, which is used to train the candidate entity identification model. To reduce manual annotations, two types of patterns are defined to recognize a part of entities in advance, to serve as annotations of the training corpus:

![](/api/attachments/3SWZH27J/fulltext/images/3f924a38bb4843b9008eb9fcf43588492c2a8d0c8bb17297aba7b8e862ffa755.jpg)  
Fig. 1. The framework of ICQA.

• Co-occurrence pattern: In light of existing pattern-based methods [2,26], three co-occurrence patterns, i.e., <\$E/NN and $\$ 5080$ <\$E/NN or $\ S _ { \mathrm { E / N N > , } }$ and <\$E/NN versus \$E/NN>, are applied in ICQA, where \$E represents an entity and /NN requires that the POS tag of the entity must be a noun. For example, in the sentence “Both Mercedes-Benz and Toyota have excellent off-road all-wheel-drive technology.”, “Mercedes-Benz” and “Toyota” are extracted as entities since they meet the pattern <\$E/NN and \$E/NN>. With co-occurrence patterns, entities existing in comparative sentences are extracted, forming the entity set $E _ { c } = \{ e _ { c 1 } , e _ { c 2 } , . . . , e _ { \mathrm { c n } } \}$

• Entity pattern: By considering the characteristics of entity expres sion, a series of entity patterns can be defined. This is a classical task for feature and entity extraction [11]. Table 1 gives some typical entity patterns and their representative examples. Taking “/NN + $/ \mathrm { C D } ^ { \ast }$ as an example, it requires that the composition of the extracted entity should be a noun followed by a number. Similarly, “/NN + $/ \mathrm { J J ^ { \ast } }$ requires the extracted entity to be a noun followed by an ad jective. These patterns can help further identify entities discussed separately in non-comparative statements and improve the comprehensiveness of entity identification results. Words and phra ses in the training set satisfying entity patterns are identified as items of the entity set $E _ { e } = \{ e _ { e 1 } , e _ { e 2 } , . . . , e _ { \mathrm { e m } } \}$

Entities identified based on co-occurrence patterns and entity pat terns constitute the pattern-extracted entity set, denoted as $E _ { p } = E _ { c } \cup$ $E _ { e } = \{ e _ { p 1 } , e _ { p 2 } , . . . , e _ { \mathrm { p q } } \}$ . Since Q&A contents are freely generated by users, entities identified merely by patterns may have some noise data. Using such noise data as annotations may affect the accuracy of the subsequent supervised entity identification model. Thus, further semantic analysis is required to filter out noise data in $E _ { p } .$ . In general, if a word is a real entity, it should be highly similar to a known entity in terms of semantics.

Table 1  
Typical entity patterns and representative examples.

<table><tr><td>Entity patterns</td><td>Representative examples</td></tr><tr><td>/NN + /NN</td><td>Dell Inspiron</td></tr><tr><td>/NN + /CD</td><td>EOS 800D</td></tr><tr><td>/NN + /JJ</td><td>Buick Regal</td></tr></table>

Therefore, several representative entities that are frequently purchased by consumers can be selected as the target entity set $E _ { t }$ and utilized to screen noise data in the pattern-extracted entity set. Entities with high average semantic similarities with targeted entities can be recognized as qualified entities and serve as labels to train the supervised candidate entity identification model.

Generally speaking, search engine results provide detailed explana tions and descriptions of an entity keyword. To capture the semantic relations between words and target entities, a doc2vec model [23] is trained based on the search engine results of each candidate entity. For each entity $e _ { \mathrm { p i } } \in E _ { p } ,$ , its top 100 search results returned by the search engine are collected and serve as the entity document $d _ { \mathrm { p i } } .$ . All entity documents $D = d _ { p 1 } \cup d _ { p 2 } \cup . . . d _ { \mathrm { p q } }$ are used as the training corpus of the doc2vec model. In the training process, the distributed memory model of paragraph vectors(PV-DM) was selected to generate vector representa tions of entity documents, and vectors were updated through stochastic gradient descent, where the gradient was obtained via backpropagation [23]. Through doc2vec training, entity document $d _ { \mathrm { p i } }$ is embedded in a 100-dimension vector representation $\nu _ { \mathrm { p i } }$ that reflects key topics of $e _ { \mathrm { p i } } .$ Given the target entity set $E _ { t } = \{ e _ { \mathrm { t a r 1 } } , e _ { \mathrm { t a r 2 } } , . . . e _ { \mathrm { t a r z } } \}$ , vector representation of target entities can also be obtained from the doc2vec model. Thus, the semantic similarity score of candidate $e _ { \mathrm { p i } }$ is calculated as:

$$
S (e _ {\mathrm{pi}}) = \frac {\sum_ {1} ^ {z} \frac {v _ {\mathrm{pi}} \cdot v _ {\mathrm{tarp}}}{\left| v _ {\mathrm{pi}} \right| \times \left| v _ {\mathrm{tarp}} \right|}}{z}\tag{1}
$$

where $\nu _ { * }$ is the vector representation of entity ∗ obtained from the doc2vec model trained above.

Sorting entities in $E _ { p }$ according to their semantic similarities, the top k ranked entities $E _ { l } = \{ e _ { l 1 } , e _ { l 2 } , . . . e _ { \mathrm { l k } } \}$ are selected as qualified entities. With $E _ { l }$ as annotations, a CRF model can be trained on $T _ { t } ,$ which is an undirected statistical graphical model widely applied in various do mains for entity recognition [21]. The CRF model can help extract en tities that are not identified by the pre-defined simple patterns. Let $\bullet = < o _ { 1 } , o _ { 2 } , . . . , o _ { n } >$ be a sentence sequence of length n and S be a set of finite states, each of which corresponds to a label $l \in L .$ In our model, BMEWO encoding [6] is used to tag entities, i.e., B represents the beginning of an entity, M represents the middle of an entity, E represents the end of an entity, W represents a single entity, and O represents a word that does not belong to any entity. Let $s = < s _ { 1 } , s _ { 2 } , . . . , s _ { n } >$ be the sequence corresponding to labels assigned to words in the input sequence $\mathbf { o } .$ Given an input sequence, the linear-chain CRF defines the conditional probability of a state sequence as:

$$
P (\mathrm{s} | \mathrm{o}) = \frac {1}{Z _ {o}} \exp \left(\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \lambda_ {i} f _ {j} \left(s _ {i - 1}, s _ {i}, o, i\right)\right)\tag{2}
$$

where $Z _ { o }$ is a normalization factor over all state sequences, and $f _ { j } ( s _ { i - 1 } , s _ { i } ,$ $o , i )$ is the feature function that describes a feature that can query about previous words, next words, and conjunctions of all these. $\lambda _ { j }$ is the learned weight for each feature function, which is set to maximize the conditional log-likelihood of labeled sequences:

$$
\operatorname{LL} (D) = \sum_ {i = 1} ^ {n} \log \left(P \left(\mathrm{l} _ {\mathrm{(i)}} \mid \mathrm{o} _ {\mathrm{(i)}}\right)\right) - \sum_ {j = 1} ^ {m} \frac {\lambda_ {j} ^ {2}}{2 \sigma^ {2}}\tag{3}
$$

Once these settings are found, the labeling for a new, unlabeled sequence can be predicted using a modified Viterbi algorithm [42]. Applying the trained CRF model to the entire Q&A contents $T ,$ a more accurate and complete candidate entity set $E = \{ e _ { 1 } , e _ { 2 } , . . . e _ { p } \}$ can be obtained for further analysis. However, in Q&A contents, an entity can be expressed in various forms. Thus, two normalization methods are utilized to merge different expressions into the standard one. First, for compound entities composed with more than one part, their constituent parts are normalized into the full name. To confirm which full name an entity refers to in context, for each entity, other entities containing it are matched in the same Q&A pair. The matched full name is utilized as the standard form to normalize the original entity. For example, $\mathbf { \ddot { \Delta } X 1 } ^ { \prime \prime }$ is normalized to $\mathrm { ^ { * } B M W \ X 1 ^ { * } \ i f \ ^ { * } B M W \ X 1 ^ { , } }$ is mentioned in the same Q&A pair. In some cases where there is no full entity name in the Q&A pair, it is not easy to determine which full name the entity corresponds to. Thus, limited by the content integrity of the Q&A pair, the entity will not be normalized in this case. This could be seen as a limitation of our work. Second, anchor texts in Wikipedia are used to collect different expres sion forms of an entity [25]. In Wikipedia, different expressions of the same entity will all be anchored to the same web page. As illustrated in Fig. 2, “Mercedes” and “Benz” are anchored to “Mercedes-Benz” in Wikipedia. The anchored entity (“Mercedes-Benz”) is viewed as the standard form to normalize entities targeting it (“Mercedes” and “Benz”).

## 3.2. Comparativeness analysis

In this section, a competitiveness analysis process based on network analysis is introduced to pick out entities comparable to a given entity from E and rank them accordingly.

Cognitive psychology literature suggests that people store concepts as connected nodes in a mental associative network, where the associ ation strength represents the relatedness between the concepts [37,35]. Spreading-activation theory shows that humans retrieve information in the memory network through the spread of activation [5]. That ${ \mathrm { i } } s ,$ activation of one node in the network is likely to spread to the activation of another closely connected node in the network. Accordingly, in the generation of $\mathrm { U G C } ,$ comparable entities closely connected and related in users’ mental association networks are more likely to be retrieved from the memory concurrently, and mentioned close to each other in the contents [19]. Therefore, if two entities are frequently discussed by users in the same Q&A pair, or one is mentioned in the question and the other is in the answer, they may overlap in product features such as prices and functions, and are often considered together by consumers when pur chasing. This means there is a significant degree of comparison between these two entities. Meanwhile. if two entities are relatively close in the position they are discussed, they can be considered closely related in consumers’ minds. Thus, the local comparison degree between entities e and $e _ { j }$ in a question-answer pair $( q _ { l } , a _ { l } ^ { k } , w _ { l } ^ { k } )$ can be defined as:

![](/api/attachments/3SWZH27J/fulltext/images/c075a8e80fc50e680ca9b18127e0ecd8183bf7866ecfab4fb84d2688adbab11a.jpg)  
Fig. 2. Anchor texts in Wikipedia.

$$
C _ {\mathrm{lk}} \left(e _ {i}, e _ {j}\right) = \frac {n _ {\mathrm{lk}} \left(e _ {i}\right) \times n _ {\mathrm{lk}} \left(e _ {j}\right)}{r _ {\mathrm{lk}} \left(e _ {i} , e _ {j}\right)}\tag{4}
$$

$$
r _ {\mathrm{lk}} (e _ {i}, e _ {j}) = \frac {\sum_ {\forall e _ {i} \in (q _ {l} , a _ {l} ^ {k} , w _ {l} ^ {k})} \sum_ {\forall e _ {j} \in (q _ {l} , a _ {l} ^ {k} , w _ {l} ^ {k})} d _ {\mathrm{lk}} (e _ {i} , e _ {j})}{n _ {\mathrm{lk}} (e _ {i}) \times n _ {\mathrm{lk}} (e _ {j})}\tag{5}
$$

where $n _ { \mathrm { l k } } ( e ) = n _ { q _ { l } } ( e ) + n _ { a _ { \scriptscriptstyle l } ^ { k } } ( e )$ is the frequency that entity e is discussed in $( q _ { l } , a _ { l } ^ { k } , w _ { l } ^ { k } ) , r _ { \mathrm { l k } } ( e _ { i } , e _ { j } )$ represents the average relative spacing between $e _ { i }$ and $e _ { j }$ in the question-answer pair $( q _ { l } , a _ { l } ^ { k } , w _ { l } ^ { k } )$ , and $d _ { \mathrm { l k } } ( e _ { i } , e _ { j } )$ is the relative spacing between a specific pair of $e _ { i }$ and $e _ { j }$ in $( q _ { l } , a _ { l } ^ { k } , w _ { l } ^ { k } )$ . The more times $e _ { i }$ and $e _ { j }$ are discussed together and the smaller the average interval is, the larger $C _ { \mathrm { l k } }$ is, leading to a larger local comparison degree between e and $e _ { j } .$ Overall, the relative spacing can be defined as the number of words between entities in the context, which varies slightly depending on the circumstance where two entities are mentioned together. When e and $e _ { j }$ are discussed in the same question or answer, their relative spacing is the number of words between them in the question or answer. When $e _ { i }$ and $e _ { j }$ are mentioned across a question and an answer, the question and the answer are semantically related, and thus can be concatenated and viewed as a whole. The relative spacing is measured as the number of words in the new concatenating context. Such a concat enation assumes that the entity coming first in the answer is more relevant and comparable to the entity in the problem. For example, in the question “Which models does the Toyota RAV-4 primarily compete with? How do they compare?” users tend to list the entity that is the most comparable to Toyota RAV-4 in their mind ahead in the answer. Therefore, the distance between two entities (one in the question and the other in the answer) in the concatenated string can well reflect the comparison between them. In brief, the relative spacing $d _ { \mathrm { l k } } ( e _ { i } , e _ { j } )$ is formulated as:

$$
d _ {\mathrm{lk}} (e _ {i}, e _ {j}) = \left\{ \begin{array}{l l} \frac {| P _ {q _ {l}} (e _ {i}) - P _ {q _ {l}} (e _ {j}) |}{| q _ {l} |} & \text { if } e _ {i} \text { in } q _ {l}, e _ {j} \text { in } q _ {l} \\ \frac {| P _ {a _ {l} ^ {k}} (e _ {i}) - P _ {a _ {l} ^ {k}} (e _ {j}) |}{| a _ {l} ^ {k} |} & \text { if } e _ {i} \text { in } a _ {l} ^ {k}, e _ {j} \text { in } a _ {l} ^ {k} \\ \frac {| q _ {l} | - P _ {q _ {l}} (e _ {i}) + P _ {a _ {l} ^ {k}} (e _ {j})}{| q _ {l} | + | a _ {l} ^ {k} |} & \text { if } e _ {i} \text { in } q _ {l}, e _ {j} \text { in } a _ {l} ^ {k} \end{array} \right.\tag{6}
$$

where $P _ { * } ( e )$ represents the position of the e in $^ { * , }$ and $| * |$ is the length of ∗.

In a Q&A community, users can vote for high-quality answers they think are valuable when browsing. Whether users vote on an answer mainly depends on whether they think the answer appropriately ex plains the question. Greater votes of a question-answer pair indicate higher professionalism and credibility of the comparison information contained in it. Therefore, when there are multiple question-answer pairs with different local comparison degrees between two entities, the number of votes that an answer receives can be used as the weight of a question-answer pair to reflect the credibility of its local comparison degree. Given $S _ { \mathrm { i j } }$ as the set of question-answer pairs where e and $e _ { j }$ are discussed together, the global comparison degree between e and e is defined as:

$$
C (e _ {i}, e _ {j}) = \frac {\sum_ {S _ {\mathrm{ij}}} w _ {l} ^ {k} C _ {\mathrm{lk}} (e _ {i} , e _ {j})}{\sum_ {S _ {\mathrm{ij}}} w _ {l} ^ {k}}\tag{7}
$$

It is worth noting that when the local comparison degree between two entities has only one source (e.g., e and $e _ { j }$ only co-occur in one question but never in any of its answers or other questions), the global comparison degree does not need to distinguish the credibility of this unique local comparison degree. Under such circumstances, the calcu lation of the global comparison degree with Eq. (7) will degenerate into solely depending on the frequencies and positions between two entities. The global comparison degree explains how users in a Q&A community comprehensively view the relations between entities. A higher global comparison degree indicates a stronger comparison between them. Regarding global comparison degrees, an entity comparison network $G = ( E , V )$ is constructed, where E is the set of entity nodes in the network, and V represents the set of edges. When e has a comparison relation with $e _ { j } , \mathrm { i . e . , }$ , the global comparison degree between them is not zero, an edge is added from $e _ { i }$ to $e _ { j }$ with comparison probability $p _ { \mathrm { i j } } .$ . The comparison probability between entities is asymmetric, which is consistent with the practical situation. Thus, the conditional probability is utilized to capture the asymmetry of entity comparison probabilitie in the comparison network, and the comparison probability from e<sub>i</sub> to e<sub>j</sub> is calculated as:

$$
p _ {\mathrm{ij}} = \frac {C (e _ {i} , e _ {j})}{\sum_ {m \in E} C (m , e _ {j})}\tag{8}
$$

Furthermore, comparative relations in G are transitive. If $e _ { a }$ is com parable to $e _ { b } ,$ and $e _ { b }$ is comparable to $e _ { c } ,$ there may also be a relation between e and e , even though they are not directly connected. A series of comparison paths from $e _ { i }$ to $e _ { j } ,$ , i.e., $\mathrm { P a t h } _ { \mathrm { i j } } = \{ \mathrm { P a } _ { \mathrm { i j } } ^ { 1 } , \mathrm { P a } _ { \mathrm { i j } } ^ { 2 } , . . . \mathrm { P a } _ { \mathrm { i j } } ^ { n } \}$ , can be constructed through directly comparative relations in G. For $\mathrm { P a } _ { \mathrm { i j } } ^ { t } = i , i _ { 1 } , i _ { 2 }$ $\ldots , i _ { k - 1 } , i _ { k } , j ,$ , the probability that $e _ { i }$ is comparable to $e _ { j }$ through $\mathrm { P a } _ { \mathrm { i j } } ^ { t }$ is formulated as:

$$
P _ {i j} ^ {t} = p _ {i, i _ {1}} \times p _ {i _ {1}, i _ {2}} \times \dots \times p _ {i _ {k - 1}, i _ {k}} \times p _ {i _ {k}, j}\tag{9}
$$

Considering all possible comparison paths, the competitiveness of e with respect to $e _ { j }$ should be the probability of the path with the highest likelihood, defined as:

$$
\operatorname{Comp} \left(e _ {i} \rightarrow e _ {j}\right) = \max P _ {\mathrm{ij}} ^ {t}: \forall \mathrm{Pa} _ {\mathrm{ij}} ^ {t} \in \text { Path } _ {\mathrm{ij}}\tag{10}
$$

For the given focal entity $\boldsymbol { e } _ { f } ,$ we sort other entity nodes in G according to their competitiveness with respect to $e _ { f } ,$ and retain the top-ranked entities to form the comparable entity set $E _ { \mathrm { c o m p } } ~ = ~ \{ e _ { 1 } ^ { \mathrm { c o m p } } , ~ e _ { 2 } ^ { \mathrm { c o m p } }$ $e _ { n _ { - } \mathrm { c } \mathrm { o m p } } ^ { \mathrm { c o m p } } \}$ , which helps both consumers and managers make rational and effective decisions.

## 4. Example and algorithm

In this section, the comparable entity identification process of ICQA is explained with an illustrative example of “Toyota RAV-4”. Then the algorithmic details and computational complexity of ICQA are presented and discussed.

## 4.1. Illustrative example

In the candidate entity identification stage, in virtue of co-occurrence patterns and entity patterns, 1638 entities are firstly identified from the training corpus, including “Audi O3”, “BAOJUN 510", “PASSAT"’, and “Mark Levinson”. A doc2vec model is trained to generate vector repre sentations, and four entities (“ENVISION”, “Porsche 911”, “Audi $A \boldsymbol { 6 } ^ { \mathrm { { \vec { { \mathbf { \nu } } } } } }$ and “Buick GL6”) are selected as the target entity set to help eliminate noise data. Taking “Audi $\boldsymbol { Q } \boldsymbol { 3 } ^ { , , }$ as an example, its vector representation obtained from the doc2vec model is $\nu _ { \mathrm { A u d i Q 3 } } = ( 0 . 2 2 8 , - 0 . 7 9 3 , . . . , 0 . 0 9 4 )$ , which is a 100-dimension vector. The cosine similarities between v and vector representations of four targeted entities are 0.883. 0.862, 0.787 and 0.873, respectively. Based on Eq. (1), the semantic similarity score of $\begin{array} { r } { \mathrm { ~  ~ \cdots ~ } } \\ { \mathrm { ~  ~ \theta ~ } } \end{array} \qquad Q 3 ^ { , , } \qquad \mathrm { i s }$ calculated as S(Audi $Q 3 ) = ( 0 . 8 8 3 + 0 . 8 6 2 + 0 . 7 8 7 + 0 . 8 7 3 ) / 4 = 0 . 8 5 1$ . Similarly, S(BAOJUN 510), S(PASSAT) and S(Mark Levinson) are calculated to be 0.8506, 0.8288, and 0.5024, respectively. After ranking all entities by similar ities from the greatest to the smallest, the indexes of “Audi $\boldsymbol { Q } \boldsymbol { 3 } ^ { \flat } )$

“BAOJUN 510”, and “PASSAT” are 1, 2 and 26 respectively, and they are identified as valid entities. “Mark Levinson”, the brand of car audio installed on Lexus (and not an automobile entity), is filtered out due to its relatively low similarity with known entities. With identified auto mobile entities serving as annotations, a CRF model is then trained to derive the λ that maximizes Eq. (3). The trained CRF model is applied to the entire Q&A contents for entity identification.

Once all automobile entities contained in Q&A contents have been extracted, comparison degrees between these entities are calculated. In a specific Q&A pair, “Toyota RAV-4” and “WEY VV5” are mentioned three times and two times, respectively in the answer. In a sentence of this Q&A pair, a user discusses these two entities as “I have taken both Toyota RAV-4 and WEY VV5 for a test drive”. On the basis of Eq. (6), the relative spacing between “Toyota RAV-4” and “WEY VV5” in the sen tence is $\textstyle { \frac { 1 } { 2 7 0 } }$ , since there is only one word between them and the length of the answer is $^ { 2 7 0 . }$ . In the same way, the relative spacing of the other five pairs of entities is measured as ${ \textstyle \frac { 2 5 } { 2 7 0 } } , { \textstyle \frac { 6 } { 2 7 0 } } , { \textstyle \frac { 1 8 } { 2 7 0 } } , { \textstyle \frac { 5 0 } { 2 7 0 } }$ and $\scriptstyle { \frac { 1 2 } { 2 7 0 } }$ respectively. Based on $\operatorname { E q . } \left( 4 \right) ,$ , the local comparison degree in this Q&A pair between “Toyota $R A V  – 4 ^ { * }$ and “WEY VV5” is:

$$
C _ {1 1} (\text {   ToyotaRAV   } - 4, \text {   WEYVV5   })
$$

$$
\begin{array}{l} = \frac {n _ {1 1} (\text {ToyotaRAV} - 4) \times n _ {1 1} (\text {WEYVV5})}{\sum_ {\text {eachToyotaRAV} - 4 \text {in} (q _ {1} , a _ {1} ^ {1} , w _ {1} ^ {1}) \text {eachWEYVV5in} (q _ {1} , a _ {1} ^ {1} , w _ {1} ^ {1})} d _ {1 1} (\text {ToyotaRAV} - 4 , \text {WEYVV5})} \\ \hline n _ {1 1} (\text {ToyotaRAV} - 4) \times n _ {1 1} (\text {WEYVV5}) \\ = \frac {3 \times 2}{\frac {1}{2 7 0} + \frac {2 5}{2 7 0} + \frac {6}{2 7 0} + \frac {1 8}{2 7 0} + \frac {5 0}{2 7 0} + \frac {1 2}{2 7 0}} = 8 6. 7 9 \\ \hline 3 \times 2 \end{array}\tag{11}
$$

Meanwhile, this Q&A pair receives 74 votes from users on the plat form. Together with other Q&A pairs mentioning “Toyota RAV-4” and “WEY VV5”, the global comparison degree is calculated as:

$$
\begin{array}{l} C (\text {ToyotaRAV-4,WEYVV5}) = \frac {\sum_ {S _ {\text {ToyotaRAV-4,WEYVV5}}} w _ {l} ^ {k} C _ {\mathrm{lk}} (\text {ToyotaRAV-4,WEYVV5})}{\sum_ {S _ {\mathrm{ij}}} w _ {l} ^ {k}} \\ = \frac {8 6 . 7 9 \times 7 4 + 4 2 . 1 3 \times 2 0 3 + \dots}{7 4 + 2 0 3 + \dots} = 3 0. 1 3 \end{array}\tag{12}
$$

At the same time, the sum of global comparison degrees between “Toyota $R A V  – 4 ^ { , , }$ and all the other entities is 50.50, based on which the comparison probability of “WEY VV5” concerning “Toyota $R A V  – 4 ^ { , , }$ is calculated as:

$$
\begin{array}{l}P (\text { WEY   VV5 } \rightarrow \text { Toyota   RAV } - 4) = \frac {C (\text { Toyota   RAV } - 4 , \text { WEY   VV5 })}{\sum_ {m \in E} C (m , \text { Toyota   RAV } - 4)}\\= \frac {3 0 . 1 3}{5 0 . 5 0} = 0. 5 9 6 6\end{array}\tag{13}
$$

Then, a comparison network is constructed, three nodes of which are presented in Fig. 3. There are two comparison paths in this network from “Haval H8” to “Toyota RAV-4”. One is the direct link with a comparison probability of 0.001; the other is the indirect link “Haval H8 → WEY VV5 → Toyota RAV-4”, whose comparison probability is 0.59663 × $0 . 0 6 8 0 3 \ : = \ : 0 . 0 4 0 5 9$ . Thus, the competitiveness of “Haval $H 8 ^ { \ast }$ con cerning“Toyota RAV-4” is 0.04059, which is the greater comparison probability of the two comparison paths.

Some comparable entity identification results regarding the focal entity “Toyota RAV-4” are presented in Fig. 4 with their product images. The price ranges of entities were manually recorded from a typical automobile information website (http://auto.sina.com.cn) on November 20, 2018. The website collects quoted prices of vehicles with different configurations from different retailers in Beijing. It is evident that the identified comparable entities are all typical household SUVs that have the same price range as “Toyota RAV-4”, and are often considered and compared together with “Toyota RAV-4” when con sumers make their purchase decisions. Take “WEY VV5” and “Toyota RAV4” as an example. “Toyota RAV4” is a joint venture brand SUV while “WEY VV5” is a Chinese proprietary brand SUV with a slightly lower price. On a Q&A platform, many consumers ask whether “WEY VV5” is worth buying over “Toyota RAV4” to save cost. As for “WEY VV5”, other Chinese proprietary brand SUVs like “Haval H6” and “LYNK&CO 01” are more comparable to it than “Toyota RAV4”, and thus are more frequently discussed by consumers. Based on these O&A contents. the comparison network is constructed. In the network, the competitiveness of “WEY VV5” regarding “Toyota RAV4” is higher than many other entities linked to “Toyota RAV4”, while the competitiveness of “Toyota RAV4" regarding “WEY VV5” is relatively low, which is consistent with the comparison relations in the real world.

![](/api/attachments/3SWZH27J/fulltext/images/1be85c691c78805fe5619a79b12e0942916662eaf58fc1d8c59431420281fd7b.jpg)  
Fig. 3. Example of comparison network.

## 4.2. Algorithmic details

Algorithm 1 presents the pseudo-code for ICQA, which is mainly composed of the candidate entity generation stage and the competi tiveness analysis stage.

## Algorithm 1. Algorithm of ICQA.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: The set of question-answer content, $T$; The set of patterns, $P = P_{c} \cup P_{e}$; The set of target entity $E_{t} = \{e_{\mathrm{tar1}}, e_{\mathrm{tar2}}, \ldots, e_{\mathrm{tarn}}\}$; The focal entity, $e_{f}$.  
Output: Comparable entity set, $E_{\mathrm{comp}} = \{e_1^{\mathrm{comp}}, e_2^{\mathrm{comp}}, \ldots, e_{n - c\mathrm{comp}}\}$;
</div>

(continued on next column)

(continued )

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Initialization:  $E_{cand} = \varnothing$ ;  $D_{corp} = \varnothing$ ;  $G = O(N \times N)$ ;  $S = \varnothing$ ; dist =  $E(N \times 1)$ 
2:  $T_t = RandomSelect(T)$ 
3: for  $(q_i, a_i^k, w_i^k) \in T_t$  do
4:    if IsMatchPattern(P,  $q_i, a_i^k$ ) then
5:  $E_p \longleftarrow E_p + ExtractEntity(q_i, a_i^k)$ 
6:    end if
7: end for
8: for  $e^i \in E_p \cup E_t$  do
9:    $d_i = ExtractSearchResults(e^i)$ 
10:    $D_{corp} \longleftarrow D_{corp} + d_i$ 
11: end for
12:  $M_{doc} \longleftarrow TrainDoc2vec(D_{corp})$ 
13: for  $e_{tari} \in E_t$  do
14:    $V_{tar}(e_{tari}) = Rrepresentation(e_{tari}, M_{doc})$ 
15: end for
16: for  $e_p^i \in E_p$  do
17:    $v_{e_p}^i = Representation(e_p^i, M_{doc})$ 
18:    $sim(e_p^i) = Similarity(v_{e_p}, V_{tar})$ 
19: end for
20:  $E_a = Rank(sim, k)$ 
21:  $M_{entity} = TrainCRF(T_t, E_a)$ 
22: E = MineEntity(T,  $M_{entity}$ )
23: for  $(q_i, a_i^k, w_i^k) \in T$  do
24:    for  $e_i \in E$  do
25: OE←OE + Occur( $e_i, q_i, a_i^k$ )
26:    end for
27:    for  $e_p, e_q \in OE$  do
28:  $C_{ik}(e_p, e_q) = LocalComparison(e_p, e_q, q_i, a_i^k)$ 
29:  $G'(e_p, e_q) = G'(e_p, e_q) + w_i^k * C_{ik}(e_i, e_i)$ 
30:  $W(e_p, e_q) = W(e_p, e_q) + w_i^k$ 
31:    end for
32: OE = ∅
33: end for
34: for  $e_i, e_j \in E$  do
35:    $G(e_i, e_j) = G'(e_i, e_j)/W(e_i, e_j)$ 
36:    $P_{ij} = Comparability(G(e_i, e_j), G(*, e_j))$ 
37: end for
38: while  $E \neq \varnothing$  do
39:    $S \longleftarrow S + u; E \longleftarrow E - u$ 
40:    for  $w \in E$  do
41: if dist(u) * P_uw &gt; dist(w) then
42:    dist(w) = dist(u) * P_uw
43: end if
44:    end for
45:    u = FindMaxProbability(E, dist)
46: end while
47:  $E_{comp} = Rank(dist, n\_c omp)$ 
48: Output= $E_{comp}$
</div>

![](/api/attachments/3SWZH27J/fulltext/images/cfa9cb83f57c881880279f0537196885114e165579ce1560a1988eedf9641f19.jpg)  
Fig. 4. Examples of comparable entities of “Totyota RAV-4” identified by ICQA.

In the candidate entity generation stage, entities are firstly identified with predefined patterns (lines 3 − 7). Assuming there are n questionanswer pairs in total in the training corpus, the time complexity to extract entities matching patterns is $O ( n _ { t } )$ . After that, entity documents and target entity documents are employed to train the doc2vec model (lines 8–11). Supposing the number of extracted candidate entities is $n _ { c } ,$ the time complexity of collecting the top l pages of searching results of each candidate entity is ${ \cal O } ( n _ { c } \times l )$ . The process of training doc2vec(line 12) is $O ( \mathrm { d o c 2 v e c } )$ , which is larger than $O ( n _ { d } \times \ W + n _ { d } \times \ \log _ { 2 } V + n _ { d } ) _ { ! }$ where $n _ { d }$ denotes the dimensionality of document vectors, W denotes the size of windows, and V represents the total number of words in the training corpus. Based on the vector representations of the doc2vec model, the similarities between candidate entities and the target entities can be calculated, and the top k entities serve as training annotations (lines 13–20) with the time complexity of $O ( n _ { c } )$ . The CRF model is further trained with complexity of $O ( t \times p ^ { 2 } )$ (line 21), where t represents the number of sentences in the training corpus and $p$ is the number of annotations in the training corpus. Afterwards, $n _ { e }$ entities are be iden tified by applying the trained model to the corpus T (line 22). Thus, the total time complexity of the first stage for entity identification is esti mated at the level of $O ( n _ { t } + n _ { c } \times ( l + 1 ) + \operatorname { d o c } 2 \mathrm { v e c } + t \times p ^ { 2 } )$

In the competitiveness analysis stage, the occurrence entity set OE is first picked to record entities in each question-answer pair and their positions(lines 23–26). Based on that, the local and global comparison degrees between entities in OE are calculated (lines 27–33), whose time complexity is ${ \cal O } ( n _ { t } \times n _ { e } )$ . The comparison network is then constructed with the time complexity of $O ( n _ { e } ^ { 2 } )$ (lines 34–37). To reduce the time complexity, a greedy algorithm similar to the classic Dijkstra algorithm is implemented at the cost of $O ( n _ { e } ^ { 2 } )$ (lines 38–46) to calculate the competitiveness of each entity node regarding the focal entity. Given the above, the total time complexity of ICQA is $O ( n _ { t } \times ( 1 + n _ { e } ) + n _ { c } \times ( l + 1 )$ $+ \mathrm { d o c } 2 \mathrm { v e c } + t \times p ^ { 2 } + 2 n _ { e } ^ { 2 } )$ ). When the size of the training corpus is huge, $n _ { c } , n _ { e } , W , p ^ { 2 }$ and $n _ { e } ^ { 2 }$ are far smaller than $V ,$ which is the main factor affecting the time complexity of doc2vec. Thus, when dealing with large-scale Q&A contents, the size of the training corpus for doc2vec is the dominating factor that affects the efficiency of ICOA.

## 5. Experiment

This section includes three experimental questions (EQs):

EQ1. What is the influence of the parameters and features used in ICQA, and how do we set the parameters?

EQ2. Compared with state-of-the-art comparable entity identification methods, how effective is ICQA in terms of precision and recall? EQ3. Compared with state-of-the-art competitiveness analysis methods, how does ICQA perform in evaluating competitiveness between comparable entities?

EQ1 is designed to test the influence of parameters and features on ICQA’s effectiveness at candidate entity identification and illustrate how these parameters are set in the experiment. EQ2 and EQ3 aim to compare the performance of ICQA to other state-of-the-art baseline methods. EQ2 aims to verify whether comparable entities identified by ICQA are correct and fully cover entities that users might compare. EQ3 tests whether ICQA can accurately measure competitiveness between entities and provide a more solid comparable entity rank accordingly. Section 5.1 describes the Q&A content dataset used in our experiments. Experimental results concerning EO1, EO2, and EO3 are elaborated in Sections 5.2, 5.3, and 5.4, respectively.

## 5.1. Experiment data

Taking the automobile industry as the verification field, we per formed data experiments on Q&A contents collected from Zhihu (htt ps://www.zhihu.com) to evaluate the performance of ICQA and base line methods on comparable entity identification and competitiveness analysis. Zhihu is the most popular Q&A community in China with 160 million users contributing more than 100 million answers. From Zhihu, 75 topics related to automobile brands were chosen, and the most popular 1000 Q&A pairs in each topic were collected as the evaluation dataset for comparable entity identification. There were 12,144 Q&A pairs in the evaluation dataset. On average, each Q&A pair had 29.2 sentences, 3.54 comparative sentences, and 6.22 entities.

Meanwhile, to comprehensively validate the performance of $\mathrm { I C Q A } ,$ 30 automobile entities covering typical automobile types that users often purchased and frequently discussed on Zhihu were chosen as focal entities in our experiments, as shown in Table 2.

## 5.2. Parameter experiment

In this section, the influence of the parameters used in ICQA and the computing efficiency of ICQA are validated and discussed. In order to discuss the influence of a specific parameter, we fixed all the other pa rameters and observed how the results varied with the changing parameter.

Firstly, the impact of the target entity size on CRF annotations was verified. With a target entity size of $^ { 2 , 4 , 6 , 8 , }$ , and 10, we randomly generated target entity sets from entities outside the pattern-extracted entity set. Each target entity set was used to measure the similarity scores of entities identified by patterns and rank them accordingly. For each target entity size, the target entity set selection process and the similarity score calculation were repeated for 30 times. The precision of the top 1000 ranked entities in each ranking result was utilized as the evaluation metric to compare the performance of different target entity sizes. Table 3 presents the mean values and standard deviations of 30 precision results of different target entity sizes.

As illustrated in Table 3, the accuracy of the top 1000 ranked entities remained stable when the target entity size and the selected target en tities changed. The independent-samples t-tests of the results showed that, within the 99% confidence interval, there were no differences in the results of different sizes of the target entity.

In addition, we tested whether selecting target entities inside or outside pattern-extracted entities has an influence on CRF annotations. With the target entity size fixed at 4, another 30 target entity sets were randomly selected from the pattern-extracted entity set. Similar to the target entity size experiment, each target entity set was utilized to calculate similarity scores and rank entities identified by patterns. The mean value of the precision of 30 target entity sets selected inside the pattern-extracted set was 0.9033. When comparing the precision of target entities selected inside and outside the pattern-extracted entity set, there was no difference between these two ranking results within the 99% confidence interval.

According to the two experiments above, neither the target entity size nor the target entity source influence the annotations entered into the CRF model. In practice, users can either select some well-known entities in the domain or directly choose entities from the entity extraction results of patterns as target entities. In the following param eter experiment and comparable entity identification experiment, the target entity size was set to $^ { 4 , }$ and “ENVISION”, “Porsche 911”, “Audi $A 6 ^ { \ ' } { } _ { \mathrm { i } }$ , and “Buick $G L 6 "$ were selected as target entities.

Table 2  
List of focal entities.

<table><tr><td>Index</td><td>Focal entity</td><td>Index</td><td>Focal entity</td><td>Index</td><td>Focal entity</td></tr><tr><td>1</td><td>Ford Mustang</td><td>11</td><td>Volvo XC60</td><td>21</td><td>LEXUS LS</td></tr><tr><td>2</td><td>Audi Q5</td><td>12</td><td>LEXUS GS</td><td>22</td><td>Volvo XC90</td></tr><tr><td>3</td><td>Buick GL8</td><td>13</td><td>Cadillac ATS</td><td>23</td><td>LEXUS RX</td></tr><tr><td>4</td><td>LYNK&amp;CO 01</td><td>14</td><td>Audi A3</td><td>24</td><td>Subaru BRZ</td></tr><tr><td>5</td><td>Cadillac CT6</td><td>15</td><td>Volvo S90</td><td>25</td><td>BMW M3</td></tr><tr><td>6</td><td>Audi A6</td><td>16</td><td>Haval H6</td><td>26</td><td>Porsche Panamera</td></tr><tr><td>7</td><td>Audi A4</td><td>17</td><td>NIO ES8</td><td>27</td><td>Audi TT</td></tr><tr><td>8</td><td>Volkswagen CC</td><td>18</td><td>BMW X1</td><td>28</td><td>Audi Q7</td></tr><tr><td>9</td><td>Audi A8</td><td>19</td><td>Toyota RAV4</td><td>29</td><td>GOLF GTI</td></tr><tr><td>10</td><td>Audi A5</td><td>20</td><td>BMW X3</td><td>30</td><td>Porsche Cayenne</td></tr></table>

Table 3  
Precision results of different target entity sizes.

<table><tr><td>Target entity size</td><td>2</td><td>4</td><td>6</td><td>8</td><td>10</td></tr><tr><td>Mean</td><td>0.9052</td><td>0.8972</td><td>0.9107</td><td>0.9068</td><td>0.9068</td></tr><tr><td>Standard Deviations</td><td>0.0228</td><td>0.0171</td><td>0.0198</td><td>0.0118</td><td>0.0142</td></tr></table>

In addition, the effect of the number of web pages contained in the entity document was tested. Selecting the top 25, top 50, top 75, top 100, top 125, and top 150 web pages returned by the search engine, different doc2vec models were trained, based on which representation vectors of entities identified by patterns and target entities were ob tained. The precision values of top 1000 entities ranked by similarity scores calculated with different representation vectors were measured, and the results are shown in Fig. 5.

As can be seen from Fig. 5, the precision trend of the top 1000 entities took a turn at 100, which means that 100 is the most suitable entity document size in our experimental setting. From 25 to 100, with the increase of web pages contained in the entity document, the description of entities becomes more abundant and complete. However, as the quality and relevance of low-ranked web pages worsen, when the size of the entity document is more than 100, including more web pages in the entity document introduces noise and hence reduces the accuracy of the vector representations.

Moreover, we tested how the size of CRF annotations influences its performance. Choosing top 600, top 800, top 1000, top 1200, and top 1400 entities in the similarity score ranking result as annotations, different CRF models were trained on the training corpus. To evaluate the performance of different models on candidate entity identification, a test corpus was constructed with the most popular Q&A pairs in each automobile-brand-related topic. In light of the TREC annotation framework [43]. three human annotators who were familiar with automobile entities according to their self-reports were employed to tag the automobile entities contained in the test corpus, and their annota tion results were used as the benchmark for candidate entity identifi cation. The $F _ { 1 }$ -measure results of different CRF models are presented in Fig. 6.

Fig. 6 shows that the $F _ { 1 }$ -measure has a turning point at the annota tion size of 1000. This is because qualified entities tended to have greater similarity scores with target entities and were ranked higher in the ranking result. Most of the entities ranked after 1000 were noises, such that their use as annotations limited the effectiveness of the CRF model. By the $F _ { 1 }$ -measure results, it can be found that the top 1000 entities in the entity ranking result are the most suitable CRF annotations.

![](/api/attachments/3SWZH27J/fulltext/images/a15399859796fdfec5a152ff5c1c2abeb52b3fe5becc154cf1eb36abeb9736f1.jpg)  
Fig. 5. Precision of different entity document sizes.

![](/api/attachments/3SWZH27J/fulltext/images/739e724d7cdf2515cf1cd8557c426fbcea96532d76bbdbd083946bc963f82894.jpg)  
Fig. 6. $F _ { 1 }$ -measure results of CRF models trained by different annotation sizes.

Furthermore, we tested the effectiveness of various features used in the CRF model. Common features shown to be effective in entity iden tification are the current, previous and next words (words), character n-grams of the current word (n-grams), and Part of Speech tag of the current word and surrounding words (POS) [21]. CRF models that individually utilized each feature and used different feature combina tions were trained. In addition, some deep-learning models, like Bi-LSTM CRF [12], can be used for candidate entity identification. Thus, the Bi-LSTM CRF model was also trained by taking the same qualified entities as annotations. The precision, recall and $F _ { 1 }$ -measure results obtained by all CRF variants on the test corpus are presented in Table 4.

As can be seen from Table 4, n-grams worked the best in CRF model that only used one feature, and the usage of n-grams and POS tags was better than other combinations of two features. Of all features and feature combinations, utilizing all three features performed the best, as three different types of features can provide more abundant linguistic information, and the POS tag information enhances the performance of the word feature. Moreover, consistent with the results reported in [12], in comparison with the best performing CRF model, the $F _ { 1 }$ -measure of BiLSTM-CRF improved by 0.014. Though the BiLSTM-CRF model ob tained better F -measure results, both models have their own merits in terms of the precision and recall of candidate entity identification, which form the basis for comparable entity identification. Therefore, it is necessary to further verify the performance of employing the CRF model and the BiLSTM-CRF model on comparable entity identification. More experiments were conducted, and the results are reported in Sec tion 5.3.

Finally, experiments were conducted to demonstrate the computa tional efficiency of ICOA and other baseline methods on different sizes of Q&A contents. We randomly selected the testing Q&A contents from the original dataset with sizes from 2000 to 12,000. On different test sizes, the completion time of each method was recorded. All the experiments were conducted on an Amazon Web Services with four Intel Xeon Platinum 8000 series processors (3.1GHz) and 16 GB of RAM. Fig. 7 shows the running time when the sizes of Q&A contents changed from 2000 to 12,000.

## Table 4

Candidate entity identification results of CRF variants.

<table><tr><td>Models</td><td>Precision</td><td>Recall</td><td> $F_1$ -measure</td></tr><tr><td>Words</td><td>0.8777</td><td>0.4885</td><td>0.6325</td></tr><tr><td>n-grams</td><td>0.8550</td><td>0.6654</td><td>0.7484</td></tr><tr><td>POS</td><td>0.7284</td><td>0.5606</td><td>0.6336</td></tr><tr><td>Words+n-grams</td><td>0.8569</td><td>0.6625</td><td>0.7472</td></tr><tr><td>Words+ POS</td><td>0.8254</td><td>0.6201</td><td>0.7082</td></tr><tr><td>n-grams+ POS</td><td>0.8554</td><td>0.6677</td><td>0.7500</td></tr><tr><td>Words + n-grams + POS</td><td>0.8623</td><td>0.6833</td><td>0.7624</td></tr><tr><td>Bi-LSTM CRF</td><td>0.8281</td><td>0.7306</td><td>0.7763</td></tr></table>

The results show that the computational efficiency of ICQA is lower than CoCI, TFGM, and CMiner, since these three baseline methods only need a few iterations in the Q&A contents. As discussed in Section 4.2, the efficiency of ICQA is dominated by the running time of the doc2vec model. As more entities are identified by patterns in larger Q&A con tents, the training corpus size of the doc2vec model increases, and the batch number in the training process increases accordingly. When the size of Q&A contents increases, the computing time of ICQA increases in a nearly linear trend. In comparison with ICQA, DLCIE and Bi-NET have more computational cost, which is mainly caused by the large number of parameter updates in the deep-learning model training. With an increase in Q&A content size, the number of training batches also increases; thus the increasing trend of the running time is nearly liner. The running time of the Logistic model is spent on building time-consuming classification features such as the in-link similarity, out-link similarity, and text sim ilarity. These need to repeatedly iterate in the whole experimental corpus and are thus influenced by the size of the Q&A contents.

## 5.3. Comparable entity identification

In this section, we discuss six recent comparable entity identification methods that were considered in comparison with ICQA. The first was the pattern-based method, CoCI [2,26], which assumes that comparable entities exist in the same comparative sentences. In CoCI, three commonly used patterns (<\$E/NN and \$E/NN>, <\$E/NN or \$E/NN> and <\$E/NN versus \$E/NN>) were selected as initial patterns to heu ristically identify comparable entities. The second one was the genera tive learning method, TFGM [50], where a topical factor model is trained on the Q&A dataset to classify whether entities have compara tive relations with the focal entity. The third one was a discriminative learning method that takes comparable entity identification as a clas sification task [29,33]. Following [33], the logistic regression model was chosen as the classifier, and in-link similarities, out-link similarities, text similarities, news counts, and search engine counts served as classifi cation attributes. Another baseline method was the deep-learning method proposed by [1], which is an LSTM framework designed to extract comparative information from comparative sentences. In order to validate the performance of employing deep-learning models to identify candidate entities in the first stage of ICQA, a composite method, named $\bf { B i - N e t } ,$ was created. With the same comparison network as ICOA, we pipelined it with the Bi-LSTM CRF model. In particular, we used candidate entities identified by the Bi-LSTM CRF model as inputs to the comparison network and identified comparable entities according to the competitiveness between entities in the network. Finally, a competitiveness analysis method, CMiner [41], which can also be applied for comparable entity identification, was included as a baseline method. In CMiner, nouns co-occurring with candidate entities are regarded as entity features for competitiveness calculation.

![](/api/attachments/3SWZH27J/fulltext/images/19cedeb6541f616d60a190e25ac31d4ad4050797d2cd30caac1eeca270a3a6d2.jpg)  
Fig. 7. Running time over different Q&A content sizes.

## 5.3.1. Evaluation data and metrics

For each focal entity, the top 20 comparable entities identified by each method were selected as its result set for comparison, and the TREC-style evaluation [43] was used to evaluate the performance of each method. TREC-style evaluation is one of the classical evaluation methods for information retrieval and has been used in the evaluation of many tasks, including comparable entity identification [2]. Thirty human evaluators who were experienced automobile consumers and familiar with automobile entities according to their self-reports were employed to label the ground truth of comparable entities. Comparable entities identified by each method were paired with the focal entity and shown randomly to three evaluators, who were asked to judge whether they were comparable in a real business environment. Entity pairs labeled as comparable by at least two evaluators were considered to have qualified comparative relations.

Four evaluation metrics commonly used in comparable entity iden tification [50,2]-precision, recall, $F _ { 1 }$ -measure, and novelty-were selected to evaluate different performance aspects of identification results.

Precision indicates the proportion of qualified comparable entities in the result set of each method. For a given focal entity, the comparable entity identification result provided by method $P _ { i }$ is $E _ { i } ,$ , and TE denotes the set of the qualified comparable entities in $E _ { i } .$ The precision of $P _ { i }$ is formulated as:

$$
\operatorname{Precision} \left(P _ {i}\right) = \frac {\left| \mathrm{TE} _ {i} \right|}{\left| E _ {i} \right|}\tag{14}
$$

where $\left| \mathrm { T E } _ { i } \right|$ and $\left| E _ { i } \right|$ represent the scale of $\mathrm { T E } _ { i }$ and $E _ { i }$ respectively.

The recall is calculated as the fraction of qualified comparable en tities provided by a method in all entities comparable to the focal entity in the market. Due to the broadness of the market, it is challenging to collect the entire potentially qualified entity set. In our experiment, without loss of generality, qualified comparable entities identified by all the seven methods were aggregated and served as comparable entity collection. Thus, for $P _ { i , }$ , the recall is formulated as:

$$
\operatorname{Recall} \left(P _ {i}\right) = \frac {\left| \mathrm{TE} _ {i} \right|}{\left| \bigcup_ {j = 1} ^ {n} \mathrm{TE} _ {j} \right|}\tag{15}
$$

where the denominator is the total number of qualified comparable entities identified by the seven methods.

The $F _ { 1 }$ metric is the harmonic mean of the precision and recall, used to comprehensively evaluate the methods:

$$
F _ {1} (P _ {i}) = \frac {2 \times \text { Precision } (P _ {i}) \times \text { Recall } (P _ {i})}{\text { Precision } (P _ {i}) + \text { Recall } (P _ {i})}\tag{16}
$$

Moreover, the novelty metric is utilized to evaluate the innovation of the proposed method in terms of detecting novel qualified entities that other methods cannot find. It measures the proportion of eligible com parable entities identified by one method but omitted by others. Similar to [22], the novelty value is formulated as:

$$
\text { Novelty } (P _ {i}) = \frac {\left| \mathrm{TE} _ {i} \backslash \bigcup_ {j = 1 , j \neq i} ^ {n} \mathrm{TE} _ {j} \right|}{\left| E _ {i} \right|}\tag{17}
$$

## 5.3.2. Experimental results

For comparable identification results, Fig. 8 shows a radar chart of the precision results of the seven methods, where spokes represent the 30 focal entities shown in Table 2. It can be seen from Fig. 8 that, CoCI had the best precision result on comparable entity identification. ICQA obtained similar precision results to DLCIE, and they were superior to TFGM, CMiner, Logistic, and Bi-Net. On average, ICQA was 11.33%, 62.83%, 22.83%, and 11.67% higher than TFGM, Logistic, CMiner, and Bi-Net, respectively.

Fig. 9 shows a radar chart of the recall results of the seven methods.

![](/api/attachments/3SWZH27J/fulltext/images/ede8d7a8ca1313ef7eb8aff13e5fe77449d4da6daaca9ae7f5ca13ec0dfdfde5.jpg)  
Fig. 8. Precision values of seven comparable entity identification methods.

Among the seven methods, ICQA obtained the best recall values in most cases. In contrast, the recall results of CoCI, DLCIE, and Logistic were significantly worse than those of other baseline methods. Compared to CoCI, TFGM, Logistic, CMiner, DLCIE, and Bi-Net, ICQA improved the recall value by 24.04%, 4.98%, 26.72%, 9.24%, 22.55%, and 4.46%, respectively, revealing that it can help to identify a broader range of

comparable entities.

The results of the $F _ { 1 }$ -measure are shown in Fig. 10. The $F _ { 1 }$ -measure simultaneously evaluates the accuracy and broadness of comparable entity identification results. Thus, it reflects the effectiveness of each method more comprehensively. The radar chart shows that ICQA was nearly the best among all the seven methods. On average, ICQA outperformed CoCI, TFGM, Logistic, CMiner, DLCIE, and Bi-Net by 30.34%, 6.89%, 37.32%, 13.11%, 29.2%, and 6.45%, respectively. ICQA can thus comprehensively identify comparable entities and help users have a more accurate and broader understanding of the market situation.

![](/api/attachments/3SWZH27J/fulltext/images/936a4f90906cbc75020e9bfb392104030ae9301c98221bc44d3d0c8db78b3cb1.jpg)  
Fig. 9. Recall values of seven comparable entity identification methods.

Table 5 illustrates the mean values of ICQA and the other six baseline methods over the 30 focal entities in terms of precision, recall, and the $F _ { 1 }$ -measure, with the bold fonts indicating the best values of each metric. Some findings are summarized from Table 5. First, of all the baseline methods, ICQA and Bi-Net obtained satisfactory results in terms of the precision of comparable entity identification, and performed the best in terms of recall and the $F _ { \mathrm { 1 } } { \mathrm { - m e a s u r e } } .$ . This means that whether the CRF model or the Bi-LSTM CRF model is applied in the first stage of candidate entity identification, compared with state-of-the-art methods, the pro posed ICQA framework more accurately and comprehensively identifies comparable entities from UGC. Also, ICQA performed significantly better than Bi-Net in terms of precision, recall, and $F _ { 1 }$ -measure, owing to the lower accuracy of the candidate entities identified by BiLSTM-CRF. Furthermore, although CoCI and DLCIE exceeded other baseline methods in terms of precision, they had poor performance in terms of recall and $F _ { 1 }$ -measure, since they only considered entities co-occurring in the same comparative sentences, which represent a small amount of UGC.

Three factors account for the better performance of ICQA. First, while state-of-the-art methods only take entities appearing in compar ative sentences as candidates or use pre-given candidate sets, ICQA utilizes a combined solution in the candidate entity identification pro cess mutually reinforces the strength of the pattern-based method and the learning-based method. Such a candidate entity set is more reliable and broader than the entity set extracted from comparative sentences, which further helps to improve the precision and recall on comparable entity identification. Second, ICQA fully considers the semantic relat edness of Q&A contents during the competitiveness measurement be tween entities. That is, entities that appear in different sentences within the same answer or across the question and the answer are also com parable. Existing UGC-based comparable entity identification method only regard entities appearing in the same comparative sentence as comparable entities, but ignore the relatedness of context. Moreover, ICQA utilizes the votes that Q&A contents received to differentiate comparison information with different qualities, that have not been integrated and taken into account by existing methods.

Simultaneously, pattern-based methods, deep-learning-based methods, the supervised learning-based method, and the competitive ness analysis method have other limitations when dealing with the problem of comparable entity identification in UGC. CoCI and DLCIE only consider entities co-occurring in the same comparative sentences, which represent a small part of UGC, resulting in their poor recall and $F _ { 1 }$ -measure. Compared with CoCI, which utilizes limited linguistic pat terns between comparable entities, DLCIE can inherently capture the interdependencies among comparable entities through the modeling of comparative sentence sequence, and thus can obtain better recall results than CoCI. For the supervised learning-based method, most of its clas sification attributes, such as in-link similarities and out-link similarities, are specially designed based on the presence of online isomorphism in firms’ websites. However, such link differences between entities are not apparent in UGC, making it challenging to distinguish comparable en tities from others. For the competitiveness analysis method, many irrelevant words are included in product features extracted from Q&A contents. This reduces the effectiveness- of the competitiveness analysis and further decreases the accuracy of its identification results.

It is also clear from Table 6 that ICQA can detect novel qualified comparable entities apart from those identified by the other methods. The average value of novelty on 30 focal entities was 0.6050. ICQA could additionally identify 60.5% of qualified entities and provide novel comparable entity identification results.

To summarize the experimental results above, ICQA provides com parable entity identification results with higher precision and recall, and identifies additional qualified comparable entities ignored by other methods. These two advantages make ICQA more appealing for both managers and consumers in making rational and informative decisions.

![](/api/attachments/3SWZH27J/fulltext/images/3ebfa7567392a7f69b8697f4b676d1f59ea223de258fcb8a47fa7ef1fd36f7f6.jpg)  
Fig. 10. $F _ { 1 }$ -measures of seven comparable entity identification methods.

Table 5  
Mean values of precision, recall and $F _ { 1 }$ -measure.

<table><tr><td></td><td>ICQA</td><td>CoCI</td><td>TFGM</td><td>Logistic</td><td>CMiner</td><td>DLCIE</td><td>Bi-Net</td></tr><tr><td>Precision</td><td>0.7817</td><td>0.9306</td><td>0.6683***</td><td>0.1533***</td><td>0.5533***</td><td>0.7138</td><td>0.6650***</td></tr><tr><td>Recall</td><td>0.3658</td><td>0.0991***</td><td>0.3098***</td><td>0.0679***</td><td>0.2637***</td><td>0.1021***</td><td>0.2834***</td></tr><tr><td> $F_1$ -measure</td><td>0.4954</td><td>0.1741***</td><td>0.4206***</td><td>0.0933***</td><td>0.3547***</td><td>0.1677***</td><td>0.3951***</td></tr></table>

\* Marks of “\*\*\*” indicate that ICQA has statistically significant improvement over the other baseline methods according to a paired t-test at the level of $p < 0 . 0 0 1$

Table 6  
Novelty values of ICQA and baseline methods.

<table><tr><td>Index</td><td>ICQA</td><td>CoCI</td><td>TFGM</td><td>Logistic</td><td>CMiner</td><td>DLCIE</td></tr><tr><td>1</td><td>0.6</td><td>0</td><td>0.7</td><td>0.05</td><td>0.4</td><td>0.05</td></tr><tr><td>2</td><td>0.55</td><td>0.25</td><td>0.35</td><td>0.1</td><td>0.4</td><td>0.2</td></tr><tr><td>3</td><td>0.6</td><td>0</td><td>0.7</td><td>0.05</td><td>0.3</td><td>0</td></tr><tr><td>4</td><td>0.55</td><td>0.25</td><td>0.65</td><td>0</td><td>0.2</td><td>0.3</td></tr><tr><td>5</td><td>0.45</td><td>0.2</td><td>0.55</td><td>0.05</td><td>0.3</td><td>0.15</td></tr><tr><td>6</td><td>0.6</td><td>0</td><td>0.4</td><td>0.05</td><td>0.25</td><td>0.2</td></tr><tr><td>7</td><td>0.6</td><td>0.05</td><td>0.65</td><td>0.2</td><td>0.35</td><td>0.2</td></tr><tr><td>8</td><td>0.45</td><td>0.05</td><td>0.8</td><td>0.65</td><td>0.5</td><td>0.05</td></tr><tr><td>9</td><td>0.55</td><td>0.1</td><td>0.7</td><td>0.55</td><td>0.4</td><td>0.1</td></tr><tr><td>10</td><td>0.55</td><td>0</td><td>0.4</td><td>0.15</td><td>0.45</td><td>0.1</td></tr><tr><td>11</td><td>0.25</td><td>0.2</td><td>0.25</td><td>0.2</td><td>0.3</td><td>0</td></tr><tr><td>12</td><td>0.6</td><td>0.05</td><td>0.4</td><td>0</td><td>0.55</td><td>0.05</td></tr><tr><td>13</td><td>0.7</td><td>0.05</td><td>0.75</td><td>0.15</td><td>0.35</td><td>0.05</td></tr><tr><td>14</td><td>0.4</td><td>0.1</td><td>0.35</td><td>0.05</td><td>0.3</td><td>0.25</td></tr><tr><td>15</td><td>0.5</td><td>0.05</td><td>0.55</td><td>0.05</td><td>0.45</td><td>0</td></tr><tr><td>16</td><td>0.7</td><td>0.25</td><td>0.45</td><td>0.2</td><td>0.55</td><td>0.45</td></tr><tr><td>17</td><td>0.45</td><td>0.05</td><td>0.55</td><td>0.1</td><td>0.4</td><td>0</td></tr><tr><td>18</td><td>0.8</td><td>0.25</td><td>0.45</td><td>0.1</td><td>0.4</td><td>0.15</td></tr><tr><td>19</td><td>0.85</td><td>0.05</td><td>0.5</td><td>0.2</td><td>0.45</td><td>0.05</td></tr><tr><td>20</td><td>0.6</td><td>0.1</td><td>0.85</td><td>0.25</td><td>0.45</td><td>0.05</td></tr><tr><td>21</td><td>0.45</td><td>0.1</td><td>0.6</td><td>0.15</td><td>0.25</td><td>0</td></tr><tr><td>22</td><td>0.55</td><td>0.05</td><td>0.4</td><td>0.05</td><td>0.35</td><td>0.05</td></tr><tr><td>23</td><td>0.7</td><td>0.05</td><td>0.4</td><td>0.1</td><td>0.5</td><td>0.05</td></tr><tr><td>24</td><td>0.4</td><td>0.05</td><td>0.45</td><td>0.05</td><td>0.25</td><td>0.1</td></tr><tr><td>25</td><td>0.4</td><td>0.15</td><td>0.3</td><td>0.05</td><td>0.45</td><td>0.05</td></tr><tr><td>26</td><td>0.4</td><td>0.05</td><td>0.45</td><td>0.05</td><td>0.45</td><td>0.05</td></tr><tr><td>27</td><td>0.7</td><td>0.3</td><td>0.55</td><td>0.15</td><td>0.35</td><td>0.05</td></tr><tr><td>28</td><td>0.7</td><td>0.1</td><td>0.4</td><td>0.15</td><td>0.35</td><td>0.15</td></tr><tr><td>29</td><td>0.7</td><td>0</td><td>0.45</td><td>0.15</td><td>0.25</td><td>0.05</td></tr><tr><td>30</td><td>0.6</td><td>0.15</td><td>0.4</td><td>0.15</td><td>0.35</td><td>0.05</td></tr><tr><td>Average</td><td>0.5650</td><td>0.1017</td><td>0.5133</td><td>0.1400</td><td>0.3767</td><td>0.1000</td></tr></table>

## 5.4. Competitiveness analysis

In this section, we discuss the effectiveness of ICQA at competitive ness analysis using two aspect-based competitiveness analysis methods as baselines. The first, CMiner, was proposed by [41]. CMiner defines the competitiveness of two entities based on the overlap of product as pects in online reviews. The second method, BCQ, was adopted from [46], and evaluates the competitiveness of two entities based on the conjoint keywords occurring in query logs.

## 5.4.1. Evaluation data and metrics

In the spirit of [26], who used the frequency of entities compared in webpages as an external validation of competitiveness, for each focal entity $e _ { f }$ and its top 20 ranked comparable entities $e _ { \mathrm { c o m p } }$ identified by ICQA, the number of webpages returned by Baidu.com using phrasal queries“e vs. $e _ { \mathrm { c o m p } } ^ { \ } { } ^ { \mathrm { , } \ }$ was collected in the experiment. The number of webpages returned by searching $" e _ { f } "$ and $" e _ { \mathrm { c o m p } } ^ { \ } : \ $ was also recorded separately to eliminate the popularity impact of each entity. The external competitiveness between $e _ { f }$ and $e _ { \mathrm { c o m p } }$ is formulated as:

$$
\operatorname{Comp} \left(e _ {f}, e _ {\text { comp }}\right) = \frac {N \left(e _ {f} \text { vs } e _ {\text { comp }}\right)}{N \left(e _ {f}\right) \times N \left(e _ {\text { comp }}\right)}\tag{18}
$$

where $N ( x )$ represents the number of webpages returned by searching x. Based on the calculated $\mathrm { C o m p } ( e _ { f } , e _ { \mathrm { c o m p } } ) .$ , a benchmark rank was generated by ranking entities from the most comparable to the least. If a competitiveness analysis method is competent enough, it should provide a consistent entity rank with the benchmark rank based on the competitiveness it calculated. Thus, a typical metric for comparing a given rank result with the benchmark rank, namely nDCG, was applied here to measure the performance of each competitiveness analysis method [46].

Given a focal entity $e _ { f }$ and a ranking method $P _ { j }$ whose entity rank is $E _ { j } = \{ e _ { j 1 } , e _ { j 2 } , . . . , e _ { j 2 0 } \}$ , nDCG of $P _ { j }$ is formulated as:

$$
\mathrm{nDCG} _ {j} = \frac {1}{Z} \left[ \sum_ {e _ {\mathrm{jk}} \in E _ {j}} \frac {2 ^ {\operatorname{comp} \left(e _ {f} , e _ {\mathrm{jk}}\right)} - 1}{\log_ {2} \left(1 + \operatorname{Ind} _ {i} \left(e _ {\mathrm{jk}}\right)\right)} \right]\tag{19}
$$

where $\mathrm { c o m p } ( e _ { f } , e _ { \mathrm { j k } } )$ ) represents the external competitiveness between $e _ { f }$ and $e _ { \mathrm { j k } }$ calculated based on Eq. (18), Ind ${ \mathrm { : } } ( e _ { \mathrm { j } \mathrm { k } } )$ ) represents the index for $e _ { \mathrm { j k } }$ in the ranking result of $P _ { j } ,$ and Z is the maximum possible discounted cumulative gain of the benchmark rank, which is formulated as:

$$
Z = \sum_ {e _ {\mathrm{jk}} \in E _ {j}} \frac {2 ^ {\operatorname{comp} \left(e _ {f} , e _ {\mathrm{jk}}\right)} - 1}{\log_ {2} \left(1 + \mathrm{BInd} _ {i} \left(e _ {\mathrm{jk}}\right)\right)}\tag{20}
$$

where BInd ${ \bf \nabla } _ { i } ( e _ { \mathrm { j { k } } } )$ represents the index assigned for $e _ { \mathrm { j k } }$ in the benchmark rank.

## 5.5. Experimental results

A larger value of nDCG reflects that the ranking result of a method is more consistent with the benchmark rank. The nDCG values of the three competitiveness analysis methods on 30 focal entities are presented in Table 7, where the bold fonts indicate the best nDCG values. ICQA performed the best on most of the 30 focal entities, indicating that it measures competitiveness between entities more accurately and pro vides a more reliable comparable entity rank.

Some inspiration can be drawn from the experimental results on the effectiveness of ICQA in competitiveness analysis. CMiner and BCQ analyze competitiveness between entities by the overlap of entity at tributes explicitly expressed in the contents. However, unlike online reviews and query logs where entity attributes are more transparent and easier to extract, comparison aspects are not clearly expressed in Q&A contents, leading to noise in the calculated competitiveness. ICQA does not focus on entity attributes, but rather considers the positional rela tionship of entities. In ICQA, position information between entities is fully integrated into the comparison network with credibility weights to eliminate the influence of noise. ICQA captures the comparison infor mation in Q&A contents, whether or not the aspects are explicitly mentioned. However, without explicitly utilizing entity aspects in the ranking process, the results of ICQA are not as interpretable as those of the aspect-based methods. This is the limitation of ICQA.

## 6. Conclusion

A novel method ICQA was proposed to identify comparable entities from Q&A contents. Firstly, entities are accurately and broadly extracted by integrating the advantages of pattern- and learning-based methods. Then, competitiveness analysis between entities is conducted based on the comparison network constructed in consideration of the credibility difference and entity relatedness in Q&A contents. Accordingly, com parable entity ranking and comparable entity identification results are generated. Moreover, data experiments conducted on the Q&A contents of Zhihu demonstrated that, compared with state-of-the-art methods, ICQA can identify broader, more accurate, and novel comparable en tities, and can generate a more solid comparativeness analysis of com parable entities.

Table 7  
nDCG values of three comparable entity ranking methods.

<table><tr><td>Focal Entity Index</td><td>ICQA</td><td>CMiner</td><td>BCQ</td><td>Focal Entity Index</td><td>ICQA</td><td>CMiner</td><td>BCQ</td></tr><tr><td>1</td><td>0.9653</td><td>0.5931</td><td>0.5916</td><td>16</td><td>0.5010</td><td>0.3481</td><td>0.3527</td></tr><tr><td>2</td><td>0.7019</td><td>0.7235</td><td>0.7295</td><td>17</td><td>0.5856</td><td>0.5045</td><td>0.5006</td></tr><tr><td>3</td><td>0.5173</td><td>0.5423</td><td>0.5426</td><td>18</td><td>0.3405</td><td>0.3079</td><td>0.3044</td></tr><tr><td>4</td><td>0.7708</td><td>0.3047</td><td>0.3016</td><td>19</td><td>0.7275</td><td>0.5163</td><td>0.5155</td></tr><tr><td>5</td><td>0.4947</td><td>0.4765</td><td>0.4765</td><td>20</td><td>0.7140</td><td>0.7240</td><td>0.7363</td></tr><tr><td>6</td><td>0.6155</td><td>0.4509</td><td>0.4600</td><td>21</td><td>0.2825</td><td>0.2941</td><td>0.2889</td></tr><tr><td>7</td><td>0.3124</td><td>0.2913</td><td>0.2862</td><td>22</td><td>0.7652</td><td>0.7760</td><td>0.7981</td></tr><tr><td>8</td><td>0.5874</td><td>0.4274</td><td>0.4098</td><td>23</td><td>0.6868</td><td>0.6330</td><td>0.6246</td></tr><tr><td>9</td><td>0.6936</td><td>0.4976</td><td>0.5188</td><td>24</td><td>0.6029</td><td>0.2996</td><td>0.2921</td></tr><tr><td>10</td><td>0.6645</td><td>0.6415</td><td>0.6587</td><td>25</td><td>0.5865</td><td>0.6270</td><td>0.6576</td></tr><tr><td>11</td><td>0.3050</td><td>0.2893</td><td>0.2808</td><td>26</td><td>0.7674</td><td>0.6038</td><td>0.5633</td></tr><tr><td>12</td><td>0.4182</td><td>0.3981</td><td>0.3976</td><td>27</td><td>0.8285</td><td>0.8196</td><td>0.8004</td></tr><tr><td>13</td><td>0.7169</td><td>0.3653</td><td>0.3720</td><td>28</td><td>0.8033</td><td>0.7601</td><td>0.7560</td></tr><tr><td>14</td><td>0.4092</td><td>0.4004</td><td>0.3803</td><td>29</td><td>0.4918</td><td>0.4327</td><td>0.4330</td></tr><tr><td>15</td><td>0.4441</td><td>0.3262</td><td>0.3298</td><td>30</td><td>0.6056</td><td>0.6072</td><td>0.6058</td></tr></table>

From a practical perspective, the proposed method can effectively support consumers by offering an accurate and comprehensive under standing of comparable entities from the opinions of expert users, which further helps them make well-informed and relational purchase choices. For company managers, the proposed method can quickly help them learn about market competition in real time. On the basis of that, managers can make marketing strategies and rational decisions, which are deemed desirable in the increasingly complex and fast-moving market. Moreover, for the Q&A platforms, by leveraging the proposed method, the platforms can provide effective information service in terms of comparative information by deeply mining the value of Q&A con tents, and thus can attract more users to participate in the content generation and consumption on the platforms.

Future work can be centered on three aspects. In ICQA, entity aspects are not fully utilized to identify and rank comparable entities, and as such, the identification results are not sufficiently interpretable. Future work can investigate a more interpretable comparable entity identifi cation method based on conventional aspect-based methods. Moreover, ICQA can identify comparable entities that have been discussed and compared by consumers in Q&A contents. But for new products that are unknown to most consumers or have not been discussed, their compa rable entities cannot be appropriately identified. Future work can combine UGC with professionally generated content such as patent data, to identify comparable entities of new products from the perspective of entity functions. This can make up for the lack of discussion of new products in UGC. Furthermore, in entity normalization with ICQA, nicknames of entities cannot be automatically normalized and need to be manually added to the normalization list. Future work can identify nicknames of entities and include them into the entity normalization process.

## Authors’ contribution

Jin Zhang: Writing – Review & Editing, Conceptualization, Project administration, Methodology, Investigation, Software. Liye Wang: Methodology, Validation, Formal analysis, Investigation, Writing – Original Draft. Kanliang Wang: Writing – Review & Editing, Project administration, Funding acquisition, Resources.

## Acknowledgement

The work was supported by the National Natural Science Foundation of China (71772177, 72072177, 71331007).

## References

[1] J. Arora, S. Agrawal, P. Goyal, S. Pathak, Extracting entities of interest from comparative product reviews, Proceedings of the 2017 ACM on Conference on Information and Knowledge Management (2017) 1975–1978

[2] S. Bao, R. Li, Y. Yu, Y. Cao, Competitor mining with the web, IEEE Trans. Knowl. Data Eng. 20 (2008) 1297–1310.

[3] M. Bergen, M.A. Peteraf, Competitor identification and competitor analysis: a broad-based managerial approach, Manage. Decis. Econ. 23 (2002) 157–169.

[4] B.H. Clark, D.B. Montgomery, Managerial identification of competitors, J. Market. (1999) 67–-83

[5] A.M. Collins, E.F. Loftus, A spreading-activation theory of semantic processing, Psychol. Rey, 82 (1975) 407.

[6] R. Cotterell, K. Duh, Low-resource named entity recognition with cross-lingual character-level neural conditional random fields, Proceedings of the Eighth International Joint Conference on Natural Language Processing (Volume 2: Shor Papers) (2017) 91–96.

[7] G.S. Day, A.D. Shocker, R.K. Srivastava, Customer-oriented approaches to identifying product-markets, J. Market. 43 (1979) 8–19.

[8] R. Filieri, F. McLeay, B. Tsui, Z. Lin, Consumer perceptions of information helpfulness and determinants of purchase intention in online consumer reviews of services, Inf. Manage, 55 (2018) 956–970.

[9] S. Gregor, A.R. Hevner, Positioning and presenting design science research fo maximum impact, MIS Q. (2013) 337–355.

[10] F. Harper, D. Raban, S. Rafaeli, J. Konstan, Predictors of answer quality in online q&a sites, Proceedings of the 2008 Conference on Human Factors in Computing Systems (2008) 865–874

[11] M. Hu, B. Liu, Mining and summarizing customer reviews, in: Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2004, pp. 168–177.

[12] Z. Huang, W. Xu, K. Yu, Bidirectional LSTM-CRF Models for Sequence Tagging, arXiv preprint arXiv:1508.01991, 2015.

[13] A. Jain, P. Pantel, How do they compare? Automatic identification of comparable entities on the web, in: 2011 JEEE International Conference on Information Reuse and Integration (IRI), IEEE, 2011, pp. 228–233.

[14] M. Jang, J.w. Park, S.w. Hwang, Predictive mining of comparable entities from the web, Twenty-Sixth AAAI Conference on Artificial Intelligence (2012).

[15] J. Jeon, W.B. Croft, J.H. Lee, Finding similar questions in large question and answer archives, in: Proceedings of the 14th ACM International Conference or Information and Knowledge Management, Association for Computing Machinery, New York, NY, USA. 2005.

[16] Z. Jiang, L. Ji, J. Zhang, J. Yan, P. Guo, N. Liu, Learning open-domain comparable entity graphs from user search queries, in: Proceedings of the 22nd ACM International Conference on Information and Knowledge Management, ACM, 2013, pp. 2339–2344.

[17] J. Jin, Y. Li, X. Zhong, L. Zhai, Why users contribute knowledge to online communities: an empirical study of an online social O&A community, Inf. Manage 52 (2015) 840–849.

[18] N. Jindal. B. Liu, Mining comparative sentences and relations, AAAI (2006) 9.

[19] D.R. John. B. Loken. K. Kim. A.B. Monga. Brand concept maps: a methodology for identifying brand association networks. J. Market. Res. 43 (2006) 549–563.

[20] L. Khansa, X. Ma, D. Liginlal. S.S. Kim, Understanding members' active participation in online question-and-answer communities: a theory and empirical analysis, J. Manage. Inf. Syst. 32 (2015) 162–203.

[21] V. Krishnan, C.D. Manning, An effective two-stage model for exploiting non-loca dependencies in named entity recognition. Proceedings of the 21st International

Conference on Computational Linguistics and the 44th annual meeting of the Association for Computational Linguistics, Association for Computational Linguistics (2006) 1121–1128.

[22] N. Lathia, S. Hailes, L. Capra, X. Amatriain, Temporal diversity in recommender systems, in: Proceedings of the 33rd International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2010, pp. 210–217.

[23] Q. Le, T. Mikolov, Distributed representations of sentences and documents, International Conference on Machine Learning (2014) 1188–1196.

[24] H.C. Lee, H.C. Rim, D.G. Lee, Learning to rank products based on online product reviews using a hierarchical deep neural network, Electron. Commerce Res. Appl. 36 (2019) 100874.

[25] C. Li, J. Weng, Q. He, Y. Yao, A. Datta, A. Sun, B.S. Lee, TwiNER: named entity recognition in targeted twitter stream, in: Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2012, pp. 721–730.

[26] S. Li, C.Y. Lin, Y.I. Song, Z. Li, Comparable entity mining from comparative questions, IEEE Trans. Knowl. Data Eng. 25 (2013) 1498–1509.

[27] Y. Liu, C. Jiang, H. Zhao, Assessing product competitive advantages from the perspective of customers by mining user-generated content on social media, Decis. Support Syst. 123 (2019) 113079.

[28] R. Lukyanenko, J. Parsons, Y.F. Wiersma, The IQ of the crowd: understanding and improving information quality in structured user-generated content, Inf. Syst. Res. 25 (2014) 669–689.

[29] Z. Ma, G. Pant, O.R. Sheng, Mining competitor relationships from online news: a network-based approach, Electron. Commerce Res. Appl. 10 (2011) 418–427.

[30] P. Mikalef, J. Krogstie, I.O. Pappas, P. Pavlou, Exploring the relationship between big data analytics capability and competitive performance: the mediating roles of dynamic and operational capabilities, Inf. Manage. (2019).

[31] L. Nie, X. Wei, D. Zhang, X. Wang, Z. Gao, Y. Yang, Data-driven answer selection in community QA systems, IEEE Trans. Knowl. Data Eng. 29 (2017) 1186–1198.

[32] K. Panovich, R. Miller, D. Karger, Tie strength in question and answer on social network sites. in: Proceedings of the ACM 2012 Conference on Computer Supported Cooperative Work, ACM, 2012, pp. 1057–1066.

[33] G. Pant, O.R. Sheng, Web footprints of firms: using online isomorphism for competitor identification, Inf. Syst. Res. 26 (2015) 188–209.

[34] M.A. Peteraf, M.E. Bergen, Scanning dynamic competitive landscapes: a marketbased and resource-based framework, Strategic Manage. J. 24 (2003) 1027–1041.

[35] M.R. Quillian, Word concepts: a theory and simulation of some basic semantic capabilities, Behav. Sci. 12 (1967) 410–430.

[36] T. Ruan, Y. Lin, H. Wang, J.Z. Pan, A multi-strategy learning approach to competitor identification, in: Joint International Semantic Technology Conference, Springer. 2014. pp. 197–212.

[37] E.E. Smith, E.J. Shoben, L.J. Rips, Structure and process in semantic memory: a featural model for semantic decisions, Psychol. Rey, 81 (1974) 214.

[38] J. Tang, B. Wang, Y. Yang, P. Hu, Y. Zhao, X. Yan. B. Gao, M. Huang, P. Xu, W. Li. W., et al., PatentMiner: topic-driven patent analysis and mining, in: Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2012, pp. 1366–1374.

[39] M. Tkachenko, H.W. Lauw, Generative modeling of entity comparisons in text, Proceedings of the 23rd ACM International Conference on Conference on Information and Knowledge Management (2014) 859–868.

[40] M. Tkachenko, H.W. Lauw, Comparative relation generative model, IEEE Trans. Knowl. Data Eng, 29 (2017) 771–783.

[41] G. Valkanas, T. Lappas, D. Gunopulos, Mining competitors from large unstructured datasets, IEEE Trans. Knowl. Data Eng. 29 (2017) 1971–1984

[42] A. Viterbi, Error bounds for convolutional codes and an asymptotically optimum decoding algorithm, IEEE Trans. Inf. Theory 13 (1967) 260–269.

[43] E.M. Voorhees, D.K. Harman, et al., TREC: Experiment and Evaluation in Information Retrieval, vol, 63, MIT Press. Cambridge, 2005

[44] G. Wang, K. Gill, M. Mohanlal, H. Zheng, B.Y. Zhao, Wisdom in the social crowd: an analysis of quora, in: Proceedings of the 22nd International Conference on World Wide Web, ACM, 2013, pp. 1341–1352.

[45] W. Wang, Y. Feng, W. Dai, Topic analysis of online reviews for two competitive products using latent Dirichlet allocation, Electron. Commerce Res. Appl. 29 (2018) 142–156.

[46] Q. Wei, D. Qiao, J. Zhang, G. Chen, X. Guo, A novel bipartite graph based competitiveness degree analysis from query logs, ACM Trans. Knowl. Discov. Data

[47] W. Wei, Z. Ming, L. Nie, G. Li, J. Li, F. Zhu, T. Shang, C. Luo, Exploring heterogeneous features for query-focused summarization of categorized community answers. Inf. Sci, 330 (2016) 403–423.

[48] K. Xu, S.S. Liao, J. Li, Y. Song, Mining comparative opinions from customer reviews for competitive intelligence, Decis, Support Syst. 50 (2011) 743–754.

[49] L. Yang, S. Bao, Q. Lin, X. Wu, D. Han, Z. Su, Y. Yu, Analyzing and predicting notanswered questions in community-based question answering services, Proceedings of the Twenty-Fifth AAAI Conference on Artificial Intelligence (2011).

[50] Y. Yang, J. Tang, J. Keomany, Y. Zhao, J. Li, Y. Ding, T. Li, L. Wang, Mining competitive relationships by learning across heterogeneous networks, in: Proceedings of the 21st ACM International Conference on Information and Knowledge Management, ACM, 2012, pp. 1432–1441.

[51] H. Zhang, Z. Wang, S. Chen, C. Guo, Product recommendation in online social networking communities: an empirical study of antecedents and a mediator, Inf. Manage. 56 (2019) 185–195.

[52] J. Zhang, J. Zhang, M. Zhang, From free to paid: customer expertise and customer satisfaction on knowledge payment platforms, Decis. Support Syst. 127 (2019) 113140.

[53] K. Zhang, W. Wu, H. Wu, Z. Li, M. Zhou, Question retrieval with high quality answers in community question answering, Proceedings of the 23rd ACM International Conference on Conference on Information and Knowledge Management, Association for Computing Machinery (2014).

[54] Z. Zhao, L. Zhang, X. He, W. Ng, Expert finding for question answering via graph regularized matrix completion, IEEE Trans. Knowl. Data Eng. 27 (2015) 993–1004.

[55] G. Zhou, Y. Zhou, T. He, W. Wu, Learning semantic representation with neura networks for community question answering retrieval, Knowl. Based Syst. 93 (2016) 75–83.

Jin Zhang is an associate professor at the Department of Management Science and Engi neering, School of Business, Renmin University of China. He received his PhD degree in the Department of Management Science and Engineering from the School of Economics and Management at Tsinghua University. His current research interests include data mining, business intelligence, and web search. His work has been published in journals such as Mis Quarterly, INFORMS Journal on Computing, Decision Support Systems, Information & Management, and IEEE Transactions on Neural Network and Learning Systems.

Liye Wang is currently pursuing her PhD degree at the Department of Management Science and Engineering, School of Business, Renmin University of China. Her research interests cover text mining, competitive intelligence and machine learning. Her work has been published in journals of Decision Support Systems, Frontiers of Business Research in China.

Kanliang Wang is a professor at the Department of Management Science and Engineering, School of Business, Renmin University of China. His current research interests include crowd-sourcing, online personalization, and digital commerce. His articles have appeared in premium information systems journals such as Management Science, MIS Quarterly, Decision Support Systems, Information & Management and Communications of the ACM, and top-tier conferences such as the International Conference on Information Systems.
