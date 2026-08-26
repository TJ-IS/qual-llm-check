---
otero_id: 8900
otero_key: "MXPNN43W"
title: "Visualized cognitive knowledge map integration for P2P networks"
authors: "Fu-ren Lin; Jen-Hung Yu"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.11.020"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Visualized cognitive knowledge map integration for P2P networks

Fu-ren Lin ⁎, Jen-Hung Yu

Institute of Technology Management, National Tsing Hua University, 101 Sec. 2, Kuangfu Rd., Hsinchu 300, Taiwan, ROC

a r t i c l e i n f o

Available online 3 December 2008

Keywords: Self-organizing map (SOM) Knowledge map Peer-to-peer (P2P) Egocentric SOM (ESOM)

## a b s t r a c t

This study proposes a visualized cognitive knowledge map integration system, called VisCog, to facilitate knowledge management on P2P networks. By using the SOM (self-organized map)-like model, Egocentric SOM (ESOM), VisCog can merge the other peers' knowledge artifacts (e.g., documents) under a focal peer's knowledge structure and visually present the cognitive knowledge map of the P2P network. The experimental results from evaluating VisCog performance show that VisCog can retain an individual peer's knowledge structure while articulating with those of other peers to build its cognitive knowledge map.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Knowledge management is an important practice for individuals or organizations that want to retain their competitive advantages. In general, knowledge can be possessed either in a tacit or an explicit form. Tacit knowledge is rooted in action, experience, and involvement in a speci<sup>fi</sup>c context. Knowledge that can be articulated, codi<sup>fi</sup>ed, and communicated in symbolic form and/or natural language is called explicit knowledge. Knowledge management (KM) consisting of four basic processes, such as creating, storing/retrieving, transferring, and applying knowledge, refers to identifying and leveraging the collective knowledge in an organization to help the organization compete [2,28]. Since explicit knowledge can be easily transformed into an electronic format, called knowledge artifacts (e.g., documents), it is a main concern when developing a knowledge management system (KMS). A centralized KMS, which operates on the centralized network structure and the centralized knowledge artifact repository, has been widely used and investigated in practice as well as in research [6,13].

To facilitate a user's retrieval and understanding of the knowledge artifacts of an organization, a knowledge map, which organizes scattered knowledge artifacts and presents them visually in meaningful categorizations, has been applied and investigated in a centralized KMS [8]. The most common display formats of knowledge maps include: (1) hierarchical displays [16], (2) network displays [10,17,19] and (3) map displays [22]. From the perspective of information retrieval [15], a hierarchical display, which organizes and represents information according to its generality and similarity into different levels and branches, can provide users both global and local views of information; hence, a user's attention can be directed to the appropriate level of generality. A hierarchical display, however, may result in oversimpli<sup>fi</sup>cation of certain information, and the selection of knowledge artifacts among the hierarchical branches may increase a user's cognitive load. A network display using nodes and links to arrange and to represent the relationship between concepts can provide a more complex knowledge structure than a hierarchical display. Moreover, it can facilitate a user to infer through the links shown on the network. If, however, the network structure is too complex, it may confuse and distract users. A map display portrays the similarity among knowledge artifacts using geographical metaphors that include a set of conventional and elaborate signs and symbols, such as shapes, locations, and distances. By mapping high-dimensional information into two-dimensional visual space, a map display allows a viewer to browse the major concepts and semantic interrelationship hidden in a large amount of information. In general, a map display can provide a more comprehensive and convenient view than hierarchical and network displays so that a user can browse the knowledge distribution embedded in a large knowledge artifact repository.

A centralized KMS has been shown to be ineffective for sharing knowledge due to several factors [9,21]. Firstly, knowledge producers have to write down/upload information collected from daily jobs according to the uni<sup>fi</sup>ed format. Secondly, knowledge demanders have to search knowledge according to both <sup>fi</sup>xed and unfamiliar categorizations. In both situations, the inef<sup>fi</sup>ciency of the storage/ retrieval process would reduce a user's inclination to share knowledge. Thirdly, knowledge artifacts are separated from persons in a centralized KMS. That is, identities of knowledge contributors are lost and reputations or rewards for creating them are hard to implement such that a centralized KMS reduces users' incentives to share knowledge [11]. In contrast to a centralized KMS, a peer-to-peer knowledge management system (P2PKMS) is better related to the nature of knowledge sharing, and it has been given much attention in the KM discipline such as works seen in [3,4,11,14,20,29]. In a P2PKMS, individuals decide the codi<sup>fi</sup>ed format and the categorization of knowledge artifacts. The knowledge sharing process is accomplished directly between knowledge contributors and demanders.

For a P2PKMS, knowledge artifacts are scattered over different peers instead of being gathered together at a centralized repository. A mechanism, such as the knowledge map used in a centralized KMS, is more critical and useful for helping peers retrieve knowledge artifacts from others. However, techniques proposed for a centralized KMS may not be suitable for direct application to P2PKMS due to the characteristics of P2PKMS, such as (1) no centralized repository responsible for gathering, codifying and storing knowledge artifacts and (2) the fact that the categorization of knowledge artifacts is decided by individuals (which may increase peers' cognition load especially while using their own categorization to browse). The aim of this study is to propose a mechanism to create a knowledge map that addresses the aforementioned concerns for a P2PKMS. The resulting visualized cognitive knowledge map integration system proposed in this study possesses the following characteristics: (1) it does not need a pre-decided common term vector to represent concepts used in individuals' knowledge artifacts repositories, (2) it organizes other peers' knowledge artifacts under the guidance of the personal knowledge structure, and (3) it adopts the Egocentric SOM (ESOM) algorithm for representing knowledge maps, which is generally more comprehensive and convenient than hierarchical and network displays. We demonstrate the visualized cognitive knowledge map integration system using the abstracts of industrial research reports collected from the Industrial Economics and Knowledge (IEK) Center at the Industrial Technology Research Institute (ITRI), Taiwan.

The remainder of this paper is organized as follows. In Section 2, we review the related SOM-like algorithm and P2P knowledge management literatures. In Section 3, we propose the framework of the visualized cognitive knowledge map integration system. The visualized cognitive knowledge map integrator is implemented and evaluated in Sections 4 and 5, respectively. Finally, we conclude this study in Section 6.

## 2. Related works

The research problem addressed in this study is to create a knowledge map suitable for application in P2PKMS. For creating the knowledge map, which concerns map display format, techniques related to a self-organizing map are adopted and described in Section 2.1. Recent efforts on distributed knowledge management, especially on P2P networks, are also reviewed in Section 2.2.

## 2.1. Self-organizing map (SOM)

Self-organizing map (SOM) proposed by Kohonen [12] is an unsupervised arti<sup>fi</sup>cial neural network model that can be trained by feeding input data repeatedly without any extra guidance. There are two major advantages of SOM: (1) it maps high-dimensional input data into a two-dimensional visual space, and (2) it represents similarity of input data by distance of locations in which input data are projected. Because SOM can provide the visualization ability for users to browse distribution and inter-relations among input data, it has been used to solve document clustering problems [5,22,30].

## 2.1.1. SOM algorithm

The original data, such as documents, are transformed to the vector space model (VSM) [24] as inputs to the SOM model. A VSM is an m×n matrix, where the number of columns, n, denotes the total number of distinct terms in a document collection; and the number of rows, m, denotes the total number of documents, where each document is represented as a vector of terms. The weight of each distinct term in each document, $w _ { i j } ,$ can be simply measured by binary numbers. Namely, $w _ { i j } = 0$ denotes a distinct term j that does not appear in document i, whereas $w _ { i j } = 1$ denotes that it does. The weight of each distinct term in each document $w _ { i j }$ can be also measured by tfidf weight $\begin{array} { r } { w _ { i j } = t f _ { i j } \cdot \log { \frac { N } { n } } } \end{array}$ to determine a term's importance in distinguishing documents [18,25], where w<sub>ij</sub> is the weight of distinct term t<sub>j</sub> in a document $D _ { i } , t f _ { i j }$ is the frequency with which t<sub>j</sub> appears in document $D _ { i } ,$ N is the number of documents in the collection, and n is the number of documents in which the term t appears at least once. Brie<sup>fl</sup>y, a term with a higher weight has a higher discriminating power. After calculating the weight for each distinct term, the top N terms will be selected to form the VSM. N is often determined by trial and error on the basis of balancing the computing cost and discriminating power.

An SOM algorithm consists of initialization and training phases. In the initialization phase, the number of the units and the topology of the output layer are determined <sup>fi</sup>rst. Then, the reference vector of each unit $( \boldsymbol { m _ { i } } \mathbf { \bar { ( } } \mu _ { \ i 1 } , \mu _ { i 2 } , \dots , \mu _ { \ i n } \mathbf { ] } ^ { T } { \in } \mathfrak { R } ^ { n } \mathbf { ) } \}$ ) of output layer is initiated. The training phase begins by <sup>fi</sup>rst randomly selecting a term vector x from the document corpus to <sup>fi</sup>nd the best-matching unit (BMU) from all units of output layer for x. The BMU is identi<sup>fi</sup>ed as $\begin{array} { r } { | | x { - } m _ { c } | | = \operatorname* { m i n } _ { i } \left\{ | | x { - } m _ { i } | | \right\} } \end{array}$ <sup>jj jj jjf gjj</sup>where c is the BMU, i is a unit of output layer and ||x−m || is the Euclidean distance between x and i. Next, it activates the BMU and other units that are topographically close to the BMU through the formula m (t+1)= $m _ { i } ( t ) + h _ { c i } ( t ) [ x ( t ) - m _ { i } ( t ) ]$ , where $t { = } 0 , 1 , 2 , \ldots$ is an integer denoting the discrete-time coordinate, $h _ { c i } ( t )$ is called neighborhood function shown as $h _ { c i } ( t ) { = } \alpha ( t ) { \cdot } \exp ( - ( | | r _ { c } { - } r _ { i } | | ^ { 2 } ) / ( 2 \sigma ^ { 2 } ( t ) ) )$ , where $\alpha ( t )$ is the learning rate $( 0 < \alpha ( t ) < 1 )$ decaying with time, $r _ { c } { \in } \Re ^ { 2 }$ and $r _ { i } { \in } { \mathfrak { R } } ^ { 2 }$ are the location vectors of nodes c and i, and $\sigma ( t )$ de<sup>fi</sup>nes the width of the kernel. In the neighborhood function, $\| r _ { c } - r _ { i } \| ^ { 2 }$ is used to measure the distance from the units to the BMU. Obviously, $h _ { c i } ( t )$ is inversely proportional to the distance of these two units. $\alpha ( t )$ and $\sigma ( t )$ are monotonically decreasing functions of time; therefore, the training phase will be convergent as time increases. At the end of the training phase, the input data with similar features will be projected into the same or adjacent zones. In practice, it usually selects a speci<sup>fi</sup>c number of training iterations as the stop criterion for stopping training.

## 2.1.2. Growing hierarchical self-organizing map (GHSOM)

The growing hierarchical self-organizing map (GHSOM) [23] is composed of individual growing self-organizing maps to form a hierarchical arti<sup>fi</sup>cial neural network model. By providing a unitgrowing function in the training phase, GHSOM can adjust the topology and the number of units of a map according to input data and parameters automatically. Moreover, GHSOM can expand units that contain highly diverse input data by a new map at the sub-layer. Therefore, it is capable of tracing diverse units in a hierarchical way. These advantages have attracted researchers’ interests in applying GHSOM in clustering documents [26,27].

GHSOM starts with a virtual map, called $M _ { 0 } ,$ which has only one virtual unit called $U _ { 0 }$ in Layer $0 . U _ { 0 }$ represents the total input data that will be used to train the model later. For each map except $M _ { 0 } ,$ , GHSOM initiates it with $\tt { a } 2 \times 2$ grid and trains it by the SOM algorithm mentioned in Section 2.1.1. The unit-growing function is applied to each training epoch. At each training epoch, it <sup>fi</sup>rst identi<sup>fi</sup>es the unit with the most quantization error (QE), called unit E. Then, it selects the most irrelevant neighbor against unit E, called unit D. Finally, it inserts a row or a column of units between units E and D. Afterward, parameters of the map will be reset by their initial value and the next round of training epoch will proceed. This process will stop if the mean quantization error (MQE) of the current map is less than the fraction $\tau _ { 1 }$ of the QE of its parent unit. For the unit whose QE is bigger than the fraction $\tau _ { 2 }$ of the $\mathrm { Q E o f } U _ { 0 } ,$ the hierarchical-growth function will expand it to form a new map at a sub-layer.

## 2.2. Peer-to-peer knowledge management (P2PKM)

Knowledge management, including such activities as creating, storing/retrieving, transferring and applying knowledge, refers to identifying and leveraging the collective knowledge in an organization to help the organization compete [2,28]. With great progress in

Internet bandwidth, computing power, and storage capability, peerto-peer (P2P) networks have been applied in real world applications. Conceptually, a P2P network is a distributed architecture composed of peers that are usually identical with equal capability. P2P networks place emphasis on autonomy; in other words, each peer has its authority to manage individual resources and behavior. Moreover, tasks on P2P networks are achieved directly by the interaction between demanders and providers without any speci<sup>fi</sup>c mediators. These characteristics enable P2P networks to be an attractive platform to researchers who wish to investigate its potential as a suitable distributed knowledge management platform.

Because knowledge artifacts, $e . g . ,$ , documents, are scattered over different peers and classi<sup>fi</sup>ed by individuals' views, knowledge retrieval becomes more dif<sup>fi</sup>cult. Several efforts have attempted to deal with this problem. For example, Castano et al. [4] and Mangisengi and Essmayr [20] propose ontology-based P2P KM systems. Ontology represented as hierarchical concepts is used to represent local knowledge owned by an individual peer and to provide semantic matching for knowledge retrieval. The key feature of the former system is that each concept of ontology has location attributes that can be used to specify other peers who have related or similar concepts. The main characteristic of the latter is that peers can extend their ontology by the query responses in the query processes. Bonifacio et al. [3] propose a P2P architecture, called KEx, which emphasizes that each peer uses an explicit semantic schema, called content repository, to represent individual document repository. With the mechanism of content repository, peers can do semantic coordination while searching documents from other peers. Li et al. [14] focus on identifying peers that can provide the best answers for speci<sup>fi</sup>c questions. For achieving this goal, they propose an agent-based buddy-<sup>fi</sup>nding methodology, which is a reinforcement process based on a builtin fuzzy reasoning mechanism. They emphasize that peers who have similar interests or backgrounds to speci<sup>fi</sup>c questions may have more chances to give better answers. Besides peers' backgrounds, interaction processes between peers are also considered; hence, agents can improve their retrieval performance after <sup>fi</sup>nishing each task.

Besides technical issues, the factors that in<sup>fl</sup>uence the acceptance and utility of a P2PKMS are also important from a managerial perspective. Kwok and Gao [11] investigate the motivational theories from psychology and proposed a model that describes motivational factors in P2P communities. Moreover, based on this model, they propose several application features that aim to improve the productivity and the acceptability of P2PKMS. To verify the feasibility of P2PKMS applied in the real-world environment, Wang et al. [29] propose a P2P knowledge sharing system, called KTella, for communities of practices (CoPs) from the perspectives of human behavior and technological architecture. By peer clustering mechanisms and knowledge recommendation based on the collaborative <sup>fi</sup>ltering method, KTella can group peers that have similar knowledge domains to facilitate the distributed knowledge sharing process.

Generally, users utilize either searching or browsing to locate the information in which they are interested. Searching is conducted when users have related topics or keywords in mind, whereas browsing is adopted in situations that users do not have clear ideas about questions or they want to explore unfamiliar areas [22]. Currently, there are many efforts to improve the searching ef<sup>fi</sup>ciency for a P2PKMS using semantic methods or collaborative <sup>fi</sup>ltering methods, but the facilitating peers’ browsing of distributed contents is rare. Hence, the main contribution of this research is to generate a cognitive knowledge map on a P2P network to address this gap.

## 3. Visualized cognitive knowledge map integration system ( )

Based on practical experiences, people usually use their past experiences and knowledge backgrounds to recognize and interpret new things from the external world. In a centralized KMS, there exists only one uni<sup>fi</sup>ed view to classify knowledge artifacts even though it may not be consistent with users' recognition. The constraint is relaxed in a P2PKMS. The autonomy embedded in a P2P network not only grants peers the ability to classify their own knowledge artifacts, but it also allows them to organize someone else's knowledge artifacts according to individual views. To realize this idea, we <sup>fi</sup>rst assume that composition of knowledge artifacts in an individual repository can be viewed as the personal knowledge background. Furthermore, we adopt the classi<sup>fi</sup>cation structure of knowledge artifacts deposited in an individual repository to represent individual knowledge structure. Finally, we use individual knowledge structure to integrate the knowledge artifacts of other peers. To ful<sup>fi</sup>ll these tasks, this study proposes an architecture of the visualized cognitive knowledge map integration system, called Vis-Cog, as shown in Fig.1. VisCog is designed to embed in a host peer and to take charge of integrating the knowledge artifacts of other peers into the host peer's own knowledge structure. By using the clustering technique, GHSOM, the knowledge structure of individual's knowledge background can be extracted automatically from an individual knowledge artifacts repository. Then, to help peers browse overall knowledge artifacts distributed on a P2P network, ESOM, a clustering algorithm proposed in this study, is used to integrate the knowledge artifacts of others into an individual knowledge structure. VisCog consists of a visualized individual knowledge map generator and a visualized cognitive knowledge map integrator. The latter is introduced in Section 4, and the former is described in Section 3.1.

## 3.1. Visualized individual knowledge map generator

The visualized individual knowledge map generator is responsible for extracting the classi<sup>fi</sup>cation structure of knowledge artifacts deposited in an individual repository. It uses information retrieval techniques to transform unstructured and disordered knowledge artifacts of individual repository into an organized and meaningful representation. The output of this component is the visualized individual knowledge map, which is seen as the representation of self-knowledge structure and acts as an initiative map for the visualized cognitive knowledge map integrator. The detailed design of the visualized individual knowledge map generator is shown in Fig. 2 and described as follows.

(1) Keyword extraction: In this study, we assume that knowledge artifacts are stored as documents. Before clustering these documents, we have to select terms, $i . e . ,$ keywords that have enough discriminating power to represent these documents. Firstly, we segment sentences of documents into basic meaningful lexicon. Secondly, we prune lexicons that are not nouns or are single-character since most of these lexicons cannot represent complete concepts of documents. Thirdly, we further use tfidf weight to prune terms that have less discriminating power. Modifying the basic tfidf weight, this study considers the effect of different document lengths and uses the normalized tfidf weight $\begin{array} { r } { w _ { i j } = \frac { t f _ { i j } } { \sum t f _ { i } } } \end{array}$ <sup>d</sup> log ${ \frac { N } { n } } ,$ where $w _ { i j }$ is the weight of distinct term $t _ { j }$ in document $D _ { i } , t f _ { i j }$ is the frequency of term t appearing in document $D _ { i } , \Sigma t f _ { i }$ is the amount of terms in document $D _ { i } ,$ N is the amount of documents in the collection, and n is the number of documents where the term $t _ { j }$ appears at least once. Terms are sorted in descending order, and the top 40% of all terms are selected as the keyword repository according to their normalized tfidf weights.

(2) Document translation: We use keywords stored at the keyword repository to form a common term vector. By the common term vector, we translate all documents into traditional VSM as mentioned in Section 2.1.1.

(3) Clustering: After the aforementioned preprocessing stages, the clustering algorithm is applicable to cluster these documents. Because the GHSOM clustering algorithm provides the visualized capability by forming the clusters as a rectangle topology map and automatically adjusts the map size by the unit-growing function, we select the GHSOM clustering algorithm to cluster documents. Moreover, because the cognitive knowledge map is a single-layer map in this study, we set the expansion parameter τ of GHSOM to 1, which means that GHSOM will generate only a single-layer knowledge map.

![](/api/attachments/MXPNN43W/fulltext/images/d5615b690dcc5dc23e341c1cb129a5d9590a54bd2b5fb30ea3e79d2360518187.jpg)  
Fig. 1. Architecture of VisCog.

## 4. Visualized cognitive knowledge map integrator

The visualized cognitive knowledge map integrator is responsible for constructing a cognitive knowledge map that represents individual cognition of knowledge artifacts distributed on a P2P network. For ful<sup>fi</sup>lling the goal, this study proposes the Egocentric SOM (ESOM) algorithm, which emphasizes preserving the focal peer's knowledge structure while merging the knowledge artifacts of other peers. In the context of P2P networks, however, several issues have to be addressed before using ESOM. First, the focal peer's knowledge structure is usually narrow because it is merely created based on individual documents. To retain the <sup>fl</sup>exibility of structure rearrangement in the integration process, we exchange not only peers' individual knowledge maps but also peers' document-term matrices. The following reasons explain the choice of document-term matrices instead of documents. One reason is that document-term matrices are more ef<sup>fi</sup>cient to transmit on the Internet because they consist only of a vector of terms and a matrix of numerals. Another reason is that, from the perspective of privacy and intellectual property, peers may not be willing to surrender full copies of their documents. Also, because term vectors used to create document-matrices are varied, ESOM, which needs a common term vector, cannot be applied directly. To solve this problem and to reduce the integration complexity, this study proposes a procedure to generate cognitive knowledge maps, as shown in Fig. 3. In brief, it integrates the knowledge artifacts of other peers according to the similarity among peers' knowledge artifacts.

![](/api/attachments/MXPNN43W/fulltext/images/c62bf583647fc447a062abc45868f9dbc449255ed2931ad11f4c6bb4c3644be3.jpg)  
Fig. 2. Components of VisCog.

![](/api/attachments/MXPNN43W/fulltext/images/e5f7cbfffe83bdf8fe271b968efb40c88d53a679835cb61afbfbe2c40e1e5d92.jpg)  
Fig. 3. The procedure of visualized cognitive knowledge map integration.

## 4.1. Initialization and identifying the most similar knowledge map

At the initialization stage, VisCog uses the focal peer's individual knowledge map as the initial cognitive knowledge map and uses the focal peer's document-term matrix as the initial combined documentterm matrix. To reduce the complexity of the integration, in each round, VisCog identi<sup>fi</sup>es only one peer who has the most similar knowledge structure to merge. Because this study uses the knowledge map to represent peers' knowledge structures, we measure the knowledge structure similarity between the focal and neighboring peers by comparing their knowledge maps, respectively. Because their map sizes may differ, we calculate a representative unit for every map before proceeding to compare. The representative unit is the average of all units of the map. The equation used to calculate the map similarity is

$$
M _ {i j} = (n (i \cap j) / n (i)) \cdot \left(n (i \cap j) / \sqrt {\sum_ {k} \left(w _ {i k} - w _ {j k}\right) ^ {2}}\right),\tag{1}
$$

where n(i) is the number of terms used in the cognitive knowledge map, n(i∩j) is the number of the common terms appearing both in the cognitive and the neighboring peer's knowledge maps, $w _ { i k }$ and $w _ { j k }$ are the weight of the identical term in the cognitive and the neighboring peer's knowledge maps respectively, and $\begin{array} { r } { \sqrt { \sum _ { k } \left( w _ { i k } - w _ { j k } \right) ^ { 2 } } } \end{array}$ is the

![](/api/attachments/MXPNN43W/fulltext/images/35b4a219eab3d16f44671e265a0fca58c54fe9ec5cdd7928827837e7a61592c6.jpg)  
Fig. 4. The <sup>fl</sup>owchart of the ESOM algorithm.

![](/api/attachments/MXPNN43W/fulltext/images/6a3e069da71440698e73139746b20caea5ee67b3a3ecb80ec4ac5d38a5777d8c.jpg)  
Fig. 5. Examples of structure stability.

Euclidean distance between two knowledge maps. This equation emphasizes that the focal peer prefers the neighboring peer with more identical terms and closer term weights.

## 4.2. Creating a common term vector

To tackle the issue that term vectors used by the focal and merged neighboring peers may differ, VisCog <sup>fi</sup>rst combines both term vectors to generate a common term vector. Then, the common term vector adjusts the combined and neighboring peer's document-term matrices, respectively. Considering missing terms of both matrices, their term weights will be <sup>fi</sup>lled with zeros. Besides, the cognitive knowledge map is adjusted by the same strategy.

## 4.3. ESOM clustering

Conceptually, ESOM emphasizes articulating the distribution of input data under the guidance of the framework determined by users. Hence, the focal peer can use its own knowledge map as the framework and employ ESOM to integrate the document-term matrices of other peers. Because the focal peer's knowledge structure may be biased, to keep the balance between correct clustering and to retain the original framework, ESOM uses three strategies: (1) the smaller learning rate, which emphasizes the <sup>fi</sup>ne-tuning of training phases, (2) expanding the map semantically, and (3) the structure stability, which provides the option for users to determine the retained proportion of the original framework. The <sup>fl</sup>owchart of the ESOM algorithm is shown in Fig. 4 and described in the following subsections.

## 4.3.1. Structure stability measurement

Structure stability is used to measure the retained proportion of the original knowledge structure after merging the document-term matrices of neighboring peers. Because this study presents a peer's knowledge structure by a plane map, to retain the original knowledge structure is to keep the original relative locations between clusters in the merged map. We use Fig. 5 to explain this idea. Fig. 5(a) is an original knowledge structure in which clusters are denoted respectively as D0 to D8. In this case, to keep the original knowledge structure is to keep the relative locations of D0 to D8. Fig. 5(b) and (c) are two examples of merged maps. In the former, although the map size is changed, the relative locations of D0 to D8 are kept the same as shown in Fig. 5(a); hence, the original knowledge structure is completely retained. By comparison, in the latter, the map size stays the same, but the relative locations of D0 to D8 are changed. For instance, D3 moves from the left side of D4 to the right side of D4. Thus, the original knowledge structure of Fig. 5(c) is changed.

This study proposes a quanti<sup>fi</sup>cation index called structure stability, denoted as $S _ { i } { = } ( N { - } n _ { r } ) / N ,$ to measure the retained proportion of the original knowledge structure in the merged knowledge map, where S is the structure stability of map i, N is the amount of documents represented by the focal knowledge map, n is the number of documents that cause the map's change. Because each cluster usually contains more than one document in practice, we use documents instead of clusters to calculate the structure stability. Hence, the structure stability is the proportion of the focal documents that retain the original relative locations. The last task for measuring structure stability is to identify documents that really cause a map's change. In observing Fig. 5(c), we may conclude at <sup>fi</sup>rst glance that clusters except D2, D5, and D8 do not retain the original relative locations. After examining more carefully, however, we <sup>fi</sup>nd that only D3 and D4 really change their original

1. Before merging the map, determining and storing the relative locations of all documents;

2. After merging the map, determining and storing the wrong neighbors which are in the wrong relative location according to the information gathered from step 1 for all documents;

3. Identifying ringleaders which don't have enough space for their neighbors, removing these ringleaders from the wrong neighboring zone of other documents, and adding these ringleaders to the ringleader list;

```txt
4. While (any document with wrong neighbors exists) {
    Ringleader r;
    Candidate c[] ← documents which have the largest number of wrong neighbors;

    If (the number of c[] is more than one) {
    If (any candidate which has no legal space for moving) {
    r ← selecting a candidate which has no legal space to move randomly;
    } else {
    r ← selecting a candidate randomly;
    }
    } else {
    r ← candidate;
    }

    Removing r from the wrong neighboring zone of other documents;
    Adding r to the ringleader list;
}
```  
Fig. 6. The pseudo-code of identifying ringleaders from a map

relative locations. That is, if we remove D3 and D4, the relative locations of the remaining clusters recover correctly. Thus, we call D3 and D4 ringleaders and the structure stability of Fig. 5(c) is 7/9.

To discover ringleaders, this study proposes an algorithm, shown in Fig. 6 and elaborated in Fig. 7. Fig. 7(a) is an original knowledge structure in which clusters are denoted as D0 to D8. Fig. 7(b) is a merged map. The procedure to identify ringleaders is described as follows. At step 1, before merging, all clusters recognize the relative locations with other clusters in Fig. 7(a). For instance, D0 <sup>fi</sup>nds that other clusters all locate in its right side except D3 and D6 and also that D3 to D8 locate in its lower side. Moreover, D0 has to preserve two columns, as the legal space, for its right neighbors and two rows, as the legal space, for D3 to D8. At step 2, after merging, all clusters <sup>fi</sup>gure out neighbors that change their relative location in Fig. 7(b). For instance, D0 <sup>fi</sup>nds that D4 no longer locates at its bottom side. The result of step 2 is shown in Fig. 7(c), where U, B, L, and R represent the legal space, i.e., rows or columns, in which clustering has to preserve legal space for their neighbors. After <sup>fi</sup>nishing the above preparation, we start to <sup>fi</sup>gure out ringleaders. At step 3, we identify ringleaders that do not preserve legal space for their neighbors. In this example, D4 is identi<sup>fi</sup>ed as a ringleader because it does not preserve one row for its neighbors above it. We remove each identi<sup>fi</sup>ed ringleader from the columns of wrong neighbors of remained clusters and add it into the ringleader list. Because only one cluster, D4, has to be removed at step 3, we proceed to step 4. At the <sup>fi</sup>rst round of step 4, there are D1, D3. D5 and D7 in the candidate array. c[l. Because there are four candidates, we have to decide which clusters have no legal space to move. In this case, both D1 and D7 must locate between D3 and D5, but there is no space between D3 and D5 for them. We randomly select D7 as a ringleader at this round. At the second round of step 4, D1 and D3 remain in the candidate array, c[]. Again, D1 still has no legal space to shift. We select D1 as a ringleader at this round. After the second round of step 4, there are no wrong neighbors for retained clusters, so this process is <sup>fi</sup>nished. Ringleaders in Fig. 7(b) are D4, D7 and D1. The structure stability of Fig. 7(b) is 2/3.

## 4.3.2. Learning rate tuning

To retain the original knowledge structure, the ESOM integration process is a <sup>fi</sup>ne tuning process. In other words, the learning rate used by ESOM is much smaller than those used by other SOM-like algorithms. The process of selecting a proper learning rate is a trialand-error process. To accelerate this process, we propose a pseudo code shown in Fig. 8. Parameters used in this process include max learning rate, learning rate refinement limit, increasing and decreasing scale limits. Max learning rate is the maximum value of the learning rate. Learning rate re<sup>fi</sup>nement limit restricts the times of continuous increase in the learning rate. Increasing and decreasing scale limits restrict the scale of learning rate adjustment because a very small scale of the learning rate adjustment does not render any improvement. The prede<sup>fi</sup>ned structure stability threshold is set the same as ESOM. At each round, if the structure stability value is higher than the prede<sup>fi</sup>ned threshold, it will increase the current learning rate set at the middle between upper bound learning rate and current learning rate; otherwise, it will decrease the current learning rate set at the middle between the current learning rate and the lower bound learning rate. Moreover, if the adjustment range is less than increasing or decreasing scale limits, this process will stop. Hence, the learning rate selection process can be viewed as a pendular process. The range of each wiggle is decreasing and slowing to a stop gradually.

## 4.3.3. Allocating the most similar neighboring peer's documents

Conceptually, input data that have similar features to the present knowledge structure have a higher probability of being directly merged into the present knowledge structure without breaking it. Hence, in this step, ESOM identi<sup>fi</sup>es a portion of the merged neighbor peer's document-term matrix that is the most similar to the present cognitive knowledge map. The speci<sup>fi</sup>c process is described as follows. First, ESOM projects combined and merged neighbor peer's document-term matrices into the cognitive knowledge map. Next, ESOM calculates the quantization error (QE) of those clusters into which portions of the merged neighbor peer's document-term matrix are projected. Finally, ESOM combines the portion of the merged neighbor peer's document-term matrix, which is projected into the cluster with the smallest QE, with the present combined document-term matrix.

## 4.3.4. Retraining the cognitive knowledge map

In this stage, ESOM takes the combined document-term matrix to retrain the cognitive knowledge map. The training method is the same as general SOM-like algorithms. After the training phase, we calculate the structure stability of the present cognitive knowledge map. If structure stability is equal to or higher than the prede<sup>fi</sup>ned threshold, the integration is successful, and ESOM can further integrate the remaining portions of the merged neighbor peer's document-term matrix. Otherwise, the knowledge structure of the cognitive knowledge map has to be adjusted to retain the focal knowledge structure while integrating other peer's document-term matrix.

(a)

<table><tr><td>D0</td><td>D1</td><td>D2</td></tr><tr><td>D3</td><td>D4</td><td>D5</td></tr><tr><td>D6</td><td>D7</td><td>D8</td></tr></table>

(b)

<table><tr><td>D0</td><td>D1</td><td>D4</td><td>D2</td></tr><tr><td></td><td>D3</td><td>D5</td><td></td></tr><tr><td>D6</td><td></td><td>D7</td><td>D8</td></tr></table>

(c)

<table><tr><td></td><td>Wrong neighbors</td><td>U</td><td>B</td><td>L</td><td>R</td></tr><tr><td>D0</td><td>D4</td><td>0</td><td>2</td><td>0</td><td>2</td></tr><tr><td>D1</td><td>D3, D4</td><td>0</td><td>2</td><td>1</td><td>1</td></tr><tr><td>D2</td><td>D4</td><td>0</td><td>2</td><td>2</td><td>0</td></tr><tr><td>D3</td><td>D1</td><td>1</td><td>1</td><td>0</td><td>2</td></tr><tr><td>D4</td><td>D0, D1, D2, D5</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>D5</td><td>D4, D7</td><td>1</td><td>1</td><td>2</td><td>0</td></tr><tr><td>D6</td><td></td><td>2</td><td>0</td><td>0</td><td>2</td></tr><tr><td>D7</td><td>D5</td><td>2</td><td>0</td><td>1</td><td>1</td></tr><tr><td>D8</td><td></td><td>2</td><td>0</td><td>2</td><td>0</td></tr></table>

Fig. 7. Examples of identifying ringleaders.

```solidity
1. Determining the following parameters: max learning rate, learning rate refinement limit, increasing and decreasing scale limits;
2. Setting current learning rate = max learning rate / 2, upperbound learning rate = max learning rate, lower bound learning rate = 0;
3. While (tuning is not finished){
    Training the cognitive knowledge map with the combined document-term matrix;
    Calculating the structure stability for the trained cognitive knowledge map;
    If (the structure stability > predefined structure stability){
    If (current learning rate == upper bound learning rate || learning rate refinement round == learning rate refinement limit) {
    tuning is finished;
    } else {
    lower bound learning rate = current learning rate;
    adjustment range = (upper bound learning rate - current learning rate) / 2;
    If (adjustment range < increasing scale limit) {
    tuning is finished;
    } else {
    current learning rate = current learning rate + adjustment range;
    learning rate refinement round ++;
    }
    }
    } else {
    upper bound learning rate = current learning rate;
    adjustment range = (current learning rate - lower bound learning rate) / 2;
    if (lower bound learning rate <> 0 && (adjustment range / lower bound learning rate) < decreasing scale limit) {
    current learning rate = lower bound learning rate;
    tuning is finished;
    } else {
    current learning rate = current learning rate - adjustment range;
    learning rate refinement round = 0;
    }
    }
}
```  
Fig. 8. The pseudo-code of identifying <sup>fi</sup>ne tuning learning rate.

To prevent the cognitive knowledge map from expanding too much before proceeding to adjust the cognitive knowledge map, it has to check the quantitative index, τ, of the cognitive knowledge map. The formula used to calculate τ is

$$
\tau = \frac {M Q E _ {m}}{M Q E _ {0}}, M Q E _ {m} = \frac {\sum_ {i} \sum_ {j} | | D _ {i j} - C _ {i} | |}{n}, \text { and } M Q E _ {0} = \sum_ {i} | | D _ {i} - \bar {D} | |,\tag{2}
$$

where n is the number of clusters of the trained map, $D _ { i j }$ is the weight vector of document j in cluster i, and C is the weight vector of the cluster i. Conceptually, τ will decrease with the expansion of the cognitive knowledge map. If τ is less than the prede<sup>fi</sup>ned threshold, ESOM will decrease the learning rate; otherwise, it will adjust the knowledge structure of the cognitive knowledge map.

## 4.3.5. Adjusting cognitive knowledge map structure

Conceptually, the adjustment of cognitive knowledge map structure is to expand the original map to identify a more suitable unit, called Unit W, for merged input data. Hence, these input data will be directly allocated into Unit W without breaking the original knowledge structure. The clue for identifying Unit W is to allocate the best-matching unit (BMU) for merged input data in the original cognitive knowledge map. BMU is the present most suitable unit but still has a gap with Unit W. To reduce the gap, ESOM tries to search BMU's neighboring unit, which has the most similar weight variation as Unit W. The row/column of units inserted between this neighboring unit and BMU may have a better chance to be Unit W.

![](/api/attachments/MXPNN43W/fulltext/images/a8ef254611fab034da278989c741d00be3d6ac1f4d6846dbfba8af88b800ede6.jpg)  
Fig. 9. An example of determining the insertion location.

![](/api/attachments/MXPNN43W/fulltext/images/912cb47bc45f552e2d215de4284e87be547e886402ae3babf22537cde33835f8.jpg)  
Fig. 10. Examples of the initialization of new column unit.

We use Fig. 9 to demonstrate the adjustment process. In Fig. 9, D represents a pseudo cluster that is the most suitable for merged input data, and U0 to U8 are nine units of the cognitive knowledge map. At <sup>fi</sup>rst, we identify the BMU for D. In this example, we assume that U4 is the BMU for D. Second, we calculate the weight differences between U4 and U4's neighbors, denoted as ΔU1, ΔU3, ΔU5, and ΔU7, respectively, and the weight differences between U4 and D, denoted as ΔD, as shown in Fig. 9. Third, we compare ΔD with ΔU1, ΔU3, ΔU5, ΔU7 by Eq. (3), respectively. The unit that has the most similar weight variance to D gets the highest score and will be selected. Additionally, if the BMU is in the boundary of the map, it may lack some neighbors. Thus, it will use the neighbor in the contrary direction instead. For example, as shown in Fig. 9, if U0 is the BMU, it will use (U0–U3) to represent the weight difference of the up side and use the (U0–U1) to represent the weight difference of the left side.

$$
\begin{array}{l} \text {Score} (D, U _ {i}) = \sum_ {j = 1} ^ {n} \text {Sim} \big (W D _ {j}, W U _ {j i} \big) \\ \text {Sim} \big (W D _ {j}, W U _ {j i} \big) = \left\{ \begin{array}{l} - | W U _ {j i} |, \text {if} W D _ {j} = 0 \& W U _ {j i} \neq 0 \\ 1, \text {if} W D _ {j} = 0 \& W U _ {j i} = 0 \\ 0, \text {if} W D _ {j} \neq 0 \& W U _ {j i} = 0 \\ \frac {W U _ {j i}}{W D _ {j}}, \text {if} | W U _ {j i} | <   | W D _ {j} | \& (W D _ {j} \cdot W U _ {j i}) > 0 \\ \frac {W D _ {j}}{W U _ {j i}}, \text {if} | W U _ {j i} | \geq | W D _ {j} | \& (W D _ {j} \cdot W U _ {j i}) > 0 \\ \frac {W U _ {j i}}{W D _ {j}}, \text {if} (W D _ {j} \cdot W U _ {j i}) <   0 \end{array} , \right. \end{array}\tag{3}
$$

where D is the vector of weight variance between the average of merged input data and BMU, $U _ { i }$ is the vector of weight variance between a unit $U _ { i }$ and BMU, WD is the weight variance of jth term in $D ,$ and $W U _ { j i }$ is the weight variance of jth term in $U _ { i \cdot }$

Finally, we insert a new row/column of units between the BMU and its selected neighboring unit using Eq. (3). There are two situations for initializing a new row/column. In the <sup>fi</sup>rst situation, as shown in Fig. 10(a), we directly use the average of neighboring units and merged input data to initialize, whereas, in the second situation, we use the neighbor in the reverse direction instead as shown in Fig. 10(b) because the new column of units is inserted at the boundary of the new map.

## 5. Evaluation of the visualized cognitive knowledge map integration

To verify whether VisCog can integrate other's knowledge artifacts on a P2P network effectively under the guidance of the focal peer's knowledge structure, two questions must be answered. First, can VisCog keep clustering correctness under the restriction of retaining designated proportion of the focal peer's knowledge structure? Second, if the focal peer's knowledge structure is narrow, can VisCog still work normally?

## 5.1. Data collection

To answer the aforementioned questions, we collected 10 authors and 108 abstracts of industrial research reports from Industrial Economics and Knowledge (IEK) Center at the Industrial Technology Research Institute (ITRI), Taiwan. We chose this document set for several reasons. First, in contrast to general articles, the abstract of a research report is the essence of the original research report. Second, the authors’ backgrounds vary because each peer has two to three different domain backgrounds, on average, and all peers in total have eleven different domain backgrounds. Third, the distribution of the document set, as shown in Fig. 11, is similar to the normal distribution. The aforementioned characteristics show that the document set is suitable for representing a subset of a P2P network composed of peers with different knowledge backgrounds.

![](/api/attachments/MXPNN43W/fulltext/images/d945851df94619f59ca4af44ffbe8549dd5442d267ef4fa7f8777534e6e99c68.jpg)  
Fig. 11. The number of documents in peers

## 5.2. Experiment design and procedure

The procedure of evaluating experiments is described as follows. First, we assign these documents to ten corresponding author peers. Second, individual peers use their own documents to create an individual knowledge map. The detailed process is mentioned in Section 3.1. Parameters used to create a peer's individual knowledge map are listed as follows: learning rate =0.7, t=0.85 and training epoch =1000. Two points need to be discussed further. First, we use the Chinese segment system, developed by CKIP projects in the Academia Sinica (http://ckip.iis.sinica.edu.tw/CKIP/), to segment these Chinese documents into basic meaningful lexicons. Second, because the domain backgrounds of peers vary, the individual term vectors extracted from personal documents are different. Next, individual peers create <sup>fi</sup>ve cognitive knowledge maps under <sup>fi</sup>ve structure stabilities, including 0.2, 0.4, 0.6, 0.8, and 1.0. Parameters used to generate cognitive knowledge maps are speci<sup>fi</sup>ed as follows: max learning rate =0.2, learning rate re<sup>fi</sup>nement limit =5, increasing scale of learning rate =0.0001, decreasing scare of learning $\mathrm { r a t e } = 0 . 0 1 , \tau = 0 . 1$ 1 and training epoch =1000 for each cognitive knowledge map. An example of the visualized cognitive knowledge map is shown in Appendix B. After the aforementioned process, the data of the control model are ready. For the reference model, because we do not have speci<sup>fi</sup>c categorization of the document set, we use the SOM algorithm to cluster all documents and use the result as the reference model. To determine the most suitable map size, we adopt the Min–Max partition [7]. Parameters used to create a global knowledge map by SOM are listed as follows: learning rate =0.7, map topology =4×3 and training epoch =1000. The global knowledge map is shown in Appendix A.

Returning to those key questions, for question one, we use the global knowledge map as a benchmark and compare <sup>fi</sup>ve cognitive knowledge maps of different peers with the benchmark to measure the performance of VisCog under different structure stabilities. For question two, we use the global knowledge map as a benchmark and then compare the individual knowledge map of different peers with the benchmark to measure the biased degree of an individual knowledge map. Then, we analyze the correlation between the biased degree of an individual knowledge map and the performance of Vis-Cog for different peers.

## 5.3. Evaluation criteria

Although using the user study to measure the performance of VisCog can provide more comprehensive understanding of users' perceptions, as a preliminary study, the quanti<sup>fi</sup>cation criteria calculated can provide more objective measurement to evaluate the performance of VisCog. There are three performance criteria: purity, specificity and diversity, which are widely used to evaluate the performance of document categorization [1,16,31], are adopted in this study. The de<sup>fi</sup>nitions of three criteria are described as follows:

Table 1  
ESOM performance corresponding to a global knowledge map

<table><tr><td></td><td>Peer 1</td><td>Peer 2</td><td>Peer 3</td><td>Peer 4</td><td>Peer 5</td><td>Peer 6</td><td>Peer 7</td><td>Peer 8</td><td>Peer 9</td><td>Peer 10</td><td>Avg.</td></tr><tr><td colspan="12">S.S.=0.2</td></tr><tr><td>Purity</td><td>0.44</td><td>0.41</td><td>0.44</td><td>0.44</td><td>0.37</td><td>0.46</td><td>0.49</td><td>0.37</td><td>0.49</td><td>0.42</td><td>0.43</td></tr><tr><td>f-measure</td><td>0.73</td><td>0.67</td><td>0.58</td><td>0.83</td><td>0.64</td><td>0.75</td><td>0.67</td><td>0.56</td><td>0.75</td><td>0.80</td><td>0.70</td></tr><tr><td colspan="12">S.S.=0.4</td></tr><tr><td>Purity</td><td>0.43</td><td>0.44</td><td>0.40</td><td>0.39</td><td>0.46</td><td>0.39</td><td>0.44</td><td>0.47</td><td>0.47</td><td>0.46</td><td>0.44</td></tr><tr><td>f-measure</td><td>0.73</td><td>0.67</td><td>0.67</td><td>0.58</td><td>0.75</td><td>0.48</td><td>0.75</td><td>0.75</td><td>0.75</td><td>0.67</td><td>0.68</td></tr><tr><td colspan="12">S.S.=0.6</td></tr><tr><td>Purity</td><td>0.40</td><td>0.42</td><td>0.41</td><td>0.41</td><td>0.39</td><td>0.36</td><td>0.38</td><td>0.37</td><td>0.41</td><td>0.47</td><td>0.40</td></tr><tr><td>f-measure</td><td>0.60</td><td>0.62</td><td>0.74</td><td>0.74</td><td>0.67</td><td>0.58</td><td>0.67</td><td>0.64</td><td>0.73</td><td>0.69</td><td>0.67</td></tr><tr><td colspan="12">S.S.=0.8</td></tr><tr><td>Purity</td><td>0.38</td><td>0.38</td><td>0.32</td><td>0.38</td><td>0.44</td><td>0.43</td><td>0.38</td><td>0.34</td><td>0.36</td><td>0.43</td><td>0.38</td></tr><tr><td>f-measure</td><td>0.74</td><td>0.58</td><td>0.64</td><td>0.67</td><td>0.67</td><td>0.75</td><td>0.67</td><td>0.58</td><td>0.73</td><td>0.71</td><td>0.67</td></tr><tr><td colspan="12">S.S.=1.0</td></tr><tr><td>Purity</td><td>0.40</td><td>0.39</td><td>0.38</td><td>0.38</td><td>0.32</td><td>0.39</td><td>0.42</td><td>0.38</td><td>0.37</td><td>0.40</td><td>0.38</td></tr><tr><td>f-measure</td><td>0.60</td><td>0.67</td><td>0.44</td><td>0.64</td><td>0.59</td><td>0.67</td><td>0.50</td><td>0.67</td><td>0.64</td><td>0.57</td><td>0.60</td></tr></table>

Table 2  
Two criteria for measuring individual knowledge maps

<table><tr><td></td><td>Peer 1</td><td>Peer 2</td><td>Peer 3</td><td>Peer 4</td><td>Peer 5</td><td>Peer 6</td><td>Peer 7</td><td>Peer 8</td><td>Peer 9</td><td>Peer 10</td><td>Avg.</td></tr><tr><td>Purity</td><td>1.00</td><td>0.78</td><td>0.69</td><td>1.00</td><td>0.63</td><td>0.71</td><td>0.64</td><td>0.67</td><td>0.73</td><td>0.57</td><td>0.74</td></tr><tr><td>f-measure</td><td>0.38</td><td>0.38</td><td>0.38</td><td>0.25</td><td>0.50</td><td>0.44</td><td>0.13</td><td>0.50</td><td>0.38</td><td>0.38</td><td>0.37</td></tr></table>

(1) Purity is used to calculate the similarity within each updated cluster. It is denoted as ${ \mathrm { P u r i t y } } = \sum _ { i = 1 } ^ { m }$ $\begin{array} { r } { \mathrm { P u r i t y } ( i ) \times \frac { N _ { i } ^ { U } } { N } , } \end{array}$ , and $\begin{array} { r l } { \operatorname { P u r i t y } ( i ) = } & { { } \frac { n _ { i } ^ { U } } { N _ { i } ^ { U } } , } \end{array}$ where $N _ { i } ^ { U }$ denotes the total number of documents in the updated cluster i, $n _ { i } ^ { U }$ denotes the maximum number of documents that belong to the same category in the updated cluster i, and N denotes the total number of documents in all clusters.

(2) Diversity is used to calculate the recall rate for the original clusters. It is denoted as Diversit $\begin{array} { r } { \ j = \frac { t _ { \mathrm { U } } } { T _ { 0 } } , } \end{array}$ , where $T _ { 0 }$ denotes the number of original category and $t _ { \mathrm { U } }$ denotes the number of true categories covered by the updated categories.

(3) Specificity is used to calculate the precision rate for the updated cluster. It is de<sup>fi</sup>ned as $\mathrm { S p e c i f i c i t y } = \frac { t _ { \mathrm { U } } } { T _ { \mathrm { I I } } }$ , where $T _ { \mathrm { U } }$ denotes the number of updated categories and $t _ { \mathrm { U } }$ denotes the number of true categories covered by the updated categories.

Because either diversity or speci<sup>fi</sup>city is only one aspect of measurement, f-measure is adopted for balancing these two criteria. This study de<sup>fi</sup>nes f-measure as 2 · (diversity · speci<sup>fi</sup>city) / (diversity + speci<sup>fi</sup>city). Hence, f-measure is the weighted harmonic mean of diversity and speci<sup>fi</sup>city. Only if both criteria are high can f-measure be high; thus, we use f-measure to evaluate the performance of VisCog. In summary, this study uses purity and f-measure as the two criteria for evaluating the performance of VisCog.

## 5.4. Experimental results

To answer question one, (i.e., can VisCog keep clustering correctness under the restriction of retaining designated proportion of the focal peer's knowledge structure?) we have to evaluate the performance of VisCog at various degrees of structure stability. We use a global knowledge map as the original cluster and a cognitive knowledge map as an updated cluster. The evaluation results are shown in Table 1, where we can see that ESOM performance is similar at <sup>fi</sup>ve structure stabilities. We also adopted one way ANOVA to test fmeasure, and the resulting p-value is 0.06. It indicates that the mean of f-measure at different degrees of structure stability does not have a conspicuous difference.

To verify question two, we analyze the correlation between the performance of cognitive knowledge maps and the extent of individual knowledge maps. We use the global knowledge map as the original cluster and an individual knowledge map as an updated cluster to calculate the purity and f-measure criteria for each peer. fmeasure is used to observe the extent of an individual knowledge structure. The evaluation results are shown in Table 2.

Table 3  
ESOM performance corresponding to individual knowledge map

<table><tr><td>Structure stability</td><td>0.2</td><td>0.4</td><td>0.6</td><td>0.8</td><td>1.0</td></tr><tr><td>Correlation coefficient</td><td>-0.34</td><td>-0.02</td><td>-0.31</td><td>-0.07</td><td>0.41</td></tr></table>

Next, we calculate the Pearson's correlation coef<sup>fi</sup>cient, ρ, of fmeasure in cognitive knowledge maps and in the individual knowledge map for each peer, respectively. The results are shown in Table 3, where the absolute values of ρ are less than 0.4 except for the structure stability 1.0. That is, excluding the structure stability 1.0, the focal knowledge structure does not strongly correlate with the cognitive knowledge map. The results are reasonable because the structure stability 1.0 means that VisCog has to preserve the focal peer's knowledge structure completely even if the focal peer's knowledge structure is narrow.

According to the results, we can make a preliminary conclusion that VisCog can meet the objectives set by the aforementioned questions. However, some limitations still exist. First, because this study use only a small set of documents to evaluate the performance of VisCog for preliminary tests, a large set of documents is needed to further examine VisCog scalability and ef<sup>fi</sup>ciency. Second, while the performance of VisCog is acceptable from the machine view, further investigation of the users' perceptions by the user study is required. For example, can VisCog reduce users' cognition loading? What are the effects of using different visualization methods to present the results of VisCog?

## 6. Conclusions

This study attempts to create a cognitive knowledge map that represents personal cognition of the knowledge distribution on a P2P network to facilitate knowledge sharing among peers. To achieve this goal, we developed a visualized cognitive knowledge map integration system, called VisCog, that employs ESOM, a SOMlike clustering algorithm proposed in this study. ESOM integrates input data under the guidance of the designated framework and forms the integrated result as a two-dimensional plane map that is easy and useful for users to browse the distribution and interrelationship between input data. To assess the effectiveness of VisCog, this study obtained the following results. (1) VisCog can keep correct clustering by retaining designated proportion of the focal peer's knowledge structure; (2) if the focal peer's knowledge structure is narrow, VisCog still works normally; (3) VisCog is robust and independent of the bias of the focal peer's knowledge structure except that the structure stability is set to 1.0.

## Appendix A. A global knowledge map

<table><tr><td>技術</td><td>產品</td><td>技術</td><td>國內</td></tr><tr><td>應用</td><td>國內</td><td>國內</td><td>產業</td></tr><tr><td>動向</td><td>潛力</td><td>市場</td><td>機械</td></tr><tr><td>產品</td><td>趨勢</td><td>產品</td><td>市場</td></tr><tr><td>電腦</td><td>市場</td><td>現況</td><td>日本</td></tr><tr><td>10</td><td>9</td><td>9</td><td>8</td></tr><tr><td>產業</td><td>半導體</td><td>市場</td><td>日本</td></tr><tr><td>電子零組件及材料</td><td>台灣</td><td>需求</td><td>機械</td></tr><tr><td>技術</td><td>產業</td><td>台灣</td><td>美國</td></tr><tr><td>需求</td><td>應用</td><td>產業</td><td>產值</td></tr><tr><td>市場</td><td>趨勢</td><td>價格</td><td>市場</td></tr><tr><td>12</td><td>12</td><td>10</td><td>10</td></tr><tr><td>產業</td><td>工業</td><td>機械</td><td>日本</td></tr><tr><td>電子零組件及材料</td><td>中國</td><td>台灣</td><td>美國</td></tr><tr><td>概況</td><td>發展</td><td>國內</td><td>市場</td></tr><tr><td>日本</td><td>市場</td><td>全球</td><td>概況</td></tr><tr><td>現況</td><td>產業</td><td>使用量</td><td>台灣</td></tr><tr><td>6</td><td>8</td><td>8</td><td>6</td></tr></table>

<table><tr><td>國內
機械
市場
產業
台灣
15</td><td>機械
市場
台灣
產品
模具
3</td><td>半導體
產品
製程
競爭
記憶體
7</td><td>半導體
工業
台灣
中國
電子
13</td></tr><tr><td>機械
國內
市場
基礎
投資
6</td><td>國內
機械
滿意度
市場
研究
6</td><td>現況
平面顯示器
韓國
歐洲
產業
7</td><td>產業
工業
光電
電腦
多媒體
9</td></tr><tr><td>國內
機械
美國
市場
倉儲
11</td><td>市場
運輸工具
機械
軟體
使用者
6</td><td>電子零組件及材料
顯示器
連接器
工業
產品
12</td><td>電子零組件及材料
產業
工業
貿易
電子
13</td></tr></table>

## References

[1] R. Agrawal, R. Bayardo, R. Srikant, Athena: mining-based interactive management of text databases, Proceedings of the 7th Conference on Extending Database Technology (EDBT00), 2000, pp. 365–379

[2] M. Alavi, D.E. Leidner, Review: knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25 (1) (2001) 107–136.

[3] M. Bonifacio, P. Bouquet, G. Mameli, M. Nori, Peer-mediated distributed knowledge management, Agent-Mediated Knowledge Management 2926 (2004) 31–47.

[4] S. Castano, A. Ferrara, S. Montanelli, D. Zucchelli, HELIOS: a general framework for ontology-based knowledge sharing and evolution in P2P systems, Proceedings of the 14th International Workshop on Database and Expert Systems Applications, 2003, pp. 597–603.

[5] H. Chen, C. Schuffels, R. Orwig, Internet categorization and search: a self organizing approach, Journal of Visual Communication and Image Representation 7 (1) (1996) 88–102.

[6] C.F. Cheung, M.L. Li, W.Y. Shek, W.B. Lee, T.S. Tsang, A systematic approach for knowledge auditing: a case study in transportation sector, Journal of Knowledge Management 11 (4) (2007) 140–158.

[7] S.-L. Chuang, L.-F. Chien, Taxonomy generation for text segments: a practical webbased approach, ACM Transactions on Information Systems (2005) 363–396 (TOIS).

[8] W. Chung, H. Chen, J.F. Nunamaker, A visual framework for knowledge discovery on the web: an empirical study of business intelligence exploration, Journal of Management Information Systems 21 (4) (2005) 57–84.

[9] L. Fahey, L. Prusak, The eleven deadliest sins of knowledge management, California Management Review 40 (3) (1998) 265–276.

[10] J.L. Gordon, Creating knowledge maps by exploiting dependent relationships, Knowledge-Based Systems 13 (2–3) (2000) 71–79.

[11] J.S.H. Kwok, S. Gao, Knowledge sharing community in P2P network: a study of motivational perspective, Journal of Knowledge Management 8 (1) (2004) 94–102.

[12] T. Kohonen, Self-organized formation of topologically correct feature maps, Journal of Biological Cybernetics (43) (1982) 59–69.

[13] J.-Y. Lai, C.-T. Wang, C.-Y. Chou, How knowledge map and personalization affect effectiveness of KMS in high-tech firms. Proceedings of the 41st Annual Hawaj International Conference on System Sciences 2008 p. 355

[14] X. Li, A.R. Montazemi, Y. Yuan, Agent-based buddy-<sup>fi</sup>nding methodology for knowledge sharing, Information & Management 43 (3) (2006) 283–296.

[15] X. Lin, Map displays for information retrieval, Journal of the American Society for Information Science 48 (1) (1997) 40–54.

[16] F.-R. Lin, C.-M. Hsueh, Knowledge map creation and maintenance for virtual communities of practice, Information Processing & Management 42 (2) (2006) 551-568.

[17] D.-R. Liu, C.-K. Ke, J.-Y. Lee, C.-F. Lee, Knowledge maps for composite E-services: a mining-based system platform coupling with recommendations, Expert System with Applications 34 (1) (2008) 700–716.

[18] H.P. Luhn, A statistical approach to the mechanized encoding and searching of literary information, IBM Journal of Research and Development 1 (4) (1957) 309–317.

[19] X.-F. Luo, Knowledge acquisition based on the global concept of fuzzy cognitive maps, Grid and Cooperative Computing, 2005, pp. 579–584, (GCC 2005).

[20] O. Mangisengi, W. Essmayr, P2P knowledge management: an investigation of the technical architecture and main process, Proceedings of 14th International Workshop on Database and Expert Systems Applications, 2003, pp. 787–791.

[21] M.L. Markus, Toward a theory of knowledge reuse: types of knowledge reuse situations and factors in reuse success, Journal of Management Information System 18 (1) (2001) 57–83.

[22] T.-H. Ong, H. Chen, W.-K. Sung, B. Zhu, Newsmap: a knowledge map for online news, Decision Support Systems 39 (4) (2005) 583–597.

[23] A. Rauber, D. Merkl, M. Dittenbach, The growing hierarchical self-organizing maps: exploratory analysis of high-dimensional data, IEEE Transactions on Neural Networks 13 (6) (2002) 1331–1341.

[24] G. Salton, A. Wong, C.S. Yang, A vector space model for automatic indexing, Communication of the ACM 18 (11) (1975) 613–620.

[25] K. Sparck Jones, A statistical interpretation of term speci<sup>fi</sup>city and its application in retrieval, Journal of Documentation 28 (1) (1972) 11–21.

[26] J.-Y. Shih, Y.-J. Chang, W.-H. Chen, Using GHSOM to construct legal maps for Taiwan's securities and futures markets, Expert Systems with Applications 34 (2) (2008) 850–858.

[27] A. Soriano-Asensi, J.D. Martin-Guerrero, E. Soria-Olivas, A. Palomares, R. Magdalena-Benedito, A.J. Serrano-Lopez, Web mining based on growing hierarchical self-organizing maps: analysis of a real citizen web portal, Expert Systems with Applications 34 (4) (2008) 2988–2994.

[28] G. Von Krogh, Care in knowledge creation, California Management Review 40 (3) (1998) 133–153.

[29] C.-Y. Wang, H.-Y. Yang, S.-C.T. Chou, Using peer-to-peer technology for knowledge sharing in communities of practices, Decision Support Systems 45 (3) (2008) 528–540 (Special Issue Clusters).

Mr. Jen-Hung Yu received his master degree in technology management from the Institute of Technology Management, National Tsing Hua University, in 2006. He now is a research assistant at the same institute. His research interests include knowledge management and peer-to-peer distributed system.

[30] S. Wang, H. Wang, Knowledge discovery through self-organizing maps: data visualization and query processing, Knowledge and Information Systems 4 (1) (2002) 31–45.

![](/api/attachments/MXPNN43W/fulltext/images/ec2d577ae68c4f64508fb3fb9e0d15a086d150b840ae15c42c60514d1fd9bbc5.jpg)

![](/api/attachments/MXPNN43W/fulltext/images/76befcc9cd2205e8cff131fb8dfa63e678b4a243f1511bd0bdf2cd0d3cddc72c.jpg)

[31] C.-P. Wei, P.-J. Hu, Y.-X. Dong, Managing document categories in E-commerce environments: an evolution-based approach, European Journal of Information Systems 11 (3) (2002) 208–222

Dr. Fu-ren Lin received the Ph.D. degree in Information Systems from the University of Illinois at Urbana-Champaign in 1996. He currently is a professor and chairman of the Graduate Institute of Service Science, National Tsing Hua University (NTHU), Taiwan. Prior to joining NTHU in 2004, Dr. Lin taught at the Department of Information Management, National Sun Yat-sen University since 1996, and was a Fulbright visiting scholar to his alma mater in 2002–2003 His research interests include e-commerce, business process innovation, data/text mining, knowledge management, and the emerging service science. He has published academic papers in many journals, such as International Journal of Electronic Commerce, Electronic Commerce Research and Applications, Decision Support Systems, IEEE Transactions on Engineering Management, IEEE Intelligent Systems, Journal of Organizational Computing and Electronic Commerce, and Information Processing and Management. He has served as a guest editor for journals, such as Information Systems and e-Business Management, and International Journal of Electronic Commerce Research and Applications. Professor Lin can be reached at the Institute of Service Science National Tsing Hua University Hsinchu Taiwan, R.O.C; frlin@mx.nthu.edu.tw.
