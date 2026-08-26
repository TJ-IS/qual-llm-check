---
otero_id: 23970
otero_key: "EY3PQA88"
title: "Managing document categories in e-commerce environments: an evolution-based approach"
authors: "C-P Wei; P J Hu; Y-X Dong"
year: "2002"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000429"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.palgrave-journals.com/eji

# Managing document categories in e-commerce environments: an evolution-based approach

C-P Wei<sup>1</sup>, PJ Hu<sup>2</sup> and Y-X Dong<sup>1</sup>

<sup>1</sup>Department of Information Management, College of Management, National Sun Yat-Sen University, Kaohsiung, Taiwan, ROC; and <sup>2</sup>Accounting and Information Systems, David Eccles School of Business, University of Utah, Salt Lake City, Utah 84112, USA

Management of textual documents obtained from various online sources represents a challenge in emerging e-commerce environments, where individuals and organisations have to perform continual surveillance of important events or trends pertinent to multiple topic areas of interest. Observations of textual document management by individuals and organisations have suggested the popularity of using categories to organise, archive and access documents. The sheer volume and availability of documents obtained from the internet make manual document-category management prohibitively tedious, if practicable or effective at all. An automated approach underpinned by appropriate artificial intelligence techniques has potential for solving this problem. In this vein, a critical challenge is the preservation of the user’s perspective on semantic coherence in different documents and thus supports his or her preferred practice for document groupings. Motivated by the significance of, and the need for automated document-category management, the current research proposed and experimentally examined an evolution-based approach for supporting user-centric document-category management in e-commerce environments. Specifically, we designed and implemented the Category Evolution (CE) technique, capable of supporting personalised document-category management by taking into account categories previously established by the user. Our evaluation results suggest that CE exhibited satisfactory effectiveness and reasonable robustness in different scenarios and achieved a performance level better than that recorded by the benchmark technique using complete category discovery. European Journal of Information Systems (2002) 11, 208–222. doi:10.1057/palgrave.ejis.3000429

## Introduction

Recent advances in computer network technologies have contributed significantly to global connectivity and stimulated the development and deployment of an expanding array of exciting online business applications or innovations, commonly referred to as e-commerce. Typically, business operations and activities proceed at a rapid pace in an e-commerce environment where competition, to a great extent, is defined by information velocity and agile adaptation to dynamic market conditions. Critical to the success or bottom-line survival in this greatly compacted market-space is constant surveillance of fast-changing business environments. Not surprisingly, the information sources available on the internet have grown tremendously in number and sheer volume, primarily because of global connectivity and ease of publishing. As a result, individuals and organisations have increasingly shifted from employing conventional media to using the Internet for information search and access.

Hence, management of information obtained from various online sources has become a challenging issue for individuals and organisations in the emerging e-commerce environments.

Imaginably, an individual simultaneously has to perform continual surveillance of important events, developments or trends pertinent to different topic areas of interest. For instance, an individual owning or considering equity acquisition of a firm needs to monitor closely events or changes that may affect the firm’s operations or market performance. The described information monitoring/tracking needs or interests are likely to extend beyond investments and thereby require comparable surveillance in other topic areas. The breadth or depth of such surveillance at the organisational level is likely to exceed that common to individuals. When performing environmental scanning, an organisation usually has to deal with an extensive array of topic areas of fine granularity, including important issues, events and trends concerning its customers, competitors, governmental regulations or policies, technology developments or opportunities, market trends, and many others.

In the current research, we concentrated on text which remains a prevalent and dominant form of information available on the internet, despite growing use of multimedia. Observations of textual document management by individuals and organisations have suggested the popularity of using categories (eg, folders) to organise, archive and access documents. Such document grouping behaviours are intentional acts, reflecting a user’s preferential perspective on semantic coherency or relevant groupings between subjects (Rucker & Polanco, 1997). Understandably, a category may not effectively reflect or represent its current document collection when influxes of new documents arrive. That is, the adequacy of an existing category may diminish as its content changes over time. The sheer volume and availability of documents obtained from various internet sources make manual document-category management approach prohibitively tedious, if at all practical or effective. Hence, an automated approach underpinned by appropriate artificial intelligence (AI) techniques represents an appealing alternative. In this vein, the preservation of a user’s perspective on semantic coherence with respect to different documents or the support for his or her preferred document grouping practice is essential. The described personalised aspect of document-category management issue is fundamental to many e-commerce applications and can be addressed by retaining the user’s document grouping perspective which is embedded in his or her preferred practice observed in the categories previously established.

From a research perspective, document clustering is clearly relevant to automated document-category management. Most previous document clustering research has taken a full or complete discovery approach; ie discovering categories from ground zero. According to this approach (hereafter referred to as the category discovery-based approach), categories are created as documents are clustered or grouped, without consideration of the categories already established. As a consequence, this approach creates a single set of categories for all users without taking into account individuals’ preferences or prior grouping behaviours and therefore is not likely to support personalisation. Furthermore, the resultant categories may significantly deviate from those expected by, or familiar to the user; thus, demanding an increased cognitive load on the part of the user when browsing through the new categories. Also related to the current research is text categorisation whose prior research has assumed, implicitly or explicitly, that categories, once created, will not evolve over time. This assumption is not realistic because the adequacy or practicality of an existing category may significantly diminish as new documents arrive and thereby change its content.

The current research was motivated by the importance of, and need for automated management of document categories. We address the discussed personalisation requirement by taking an evolution-based approach to supporting user-centric document-category management. Central to our approach is category decomposition and amalgamation. When an influx of new documents changes the content of a category considerably, it may be desirable to decompose the category into multiple categories, each of which contains documents of a more specific scope and increased cohesion. On the other hand, distinction or distance between or among several existing categories may become less prominent or meaningful as their delineation is blurred by new documents included in the respective categories. In this case, merging these categories may become practical or appealing. Managing existing categories’ evolution over time rather than relying on periodical (complete) discovery may be more effective for supporting the personalisation requirement in automated document-category management. Specifically, we designed and implemented the Category Evolution (CE) technique, which takes into consideration categories previously established by the user. Experimentally, we evaluated CE’s performance using that achieved by a category discovery-based technique as a benchmark. Our technique is capable of preserving personal perspective or preferences and thus represents an appealing and plausibly more effective alternative to the category discovery-based approach commonly adopted by prior research.

The remaining of the paper is organised as follows: Section 2 reviews relevant previous research and highlights our research motivation. Section 3 details the proposed technique (ie CE), including its design and overall process. Section 4 describes the evaluation design and discusses important experimental results. The paper is concluded with a summary, discussion of its contributions and limitations, and some future research directions in Section 5.

## Literature review and research motivation

Both document clustering and text categorising are relevant to automated document-category management. In essence, document clustering groups documents into clusters or categories, each of which contains similar or related documents. Most prior document clustering research is anchored in document content analysis, whereby documents are grouped into distinct clusters. Ideally, the documents in a cluster would exhibit maximal similarity to those in the same cluster and, at the same time, share minimal similarity to the documents from other clusters.

Broadly, document clustering is comprised of several phases: feature extraction/selection, document representation, and clustering. In the feature extraction/selection phase, a set of features are extracted from the source documents and used to represent these documents. Typically, feature extraction commences with the parsing of each source (input) document to produce a list of nouns or noun phrases commonly referred to as features. In most cases, features exclude a set of specified stop words that are non-semantic bearing words. Following extraction is feature selection, which reduces the size of an extracted feature set. Feature selection has important implications for the subsequent clustering efficiency and effectiveness because it condenses the size of the ultimate feature set and, at the same time, suppresses potential biases embedded in the original (ie non-condensed) feature set (Dumais et al, 1998; Roussinov & Chen, 1999). According to the top-k selection method, commonly used in previous research, the k features with the highest selection metric scores are selected as features for representing a source document. However, previous research varies considerably in the underlying metric used in feature selection. Common examples include TF (which denotes the occurrence frequency of a particular term in the document collection), TF × IDF (where IDF denotes the inverse document frequency measured by log (N/DF), where N is the number of documents in the collection and DF is the number of documents which includes the particular term under discussion), and their hybrids (Boley et al, 1999; Larsen & Aone, 1999).

In the document representation phase, a source document is represented using the features selected from the feature extraction/selection phase. A review of prior research suggests the prevalence of several representation methods that include binary (which indicates the presence or absence of a feature in a document), TF, and TF × IDF (Larsen & Aone, 1999; Roussinov & Chen, 1999). Based on the representation scheme of choice, a source document is then described by a vector space jointly defined by the k features selected in the feature extraction/selection phase.

In the clustering phase, documents are grouped into clusters, based on the selected features and their respective values for each source document. Common approaches for document clustering include partitioningbased (eg Cutting et al, 1992; Boley et al, 1999; Larsen & Aone, 1999), hierarchical (eg El-Hamdouchi & Willett, 1986; Voorhees, 1986; Roussinov & Chen, 1999), and Kohonen neural network (eg Lagus et al, 1996; Roussinov & Chen, 1999). By and large, a partitioning-based approach partitions a set of documents into multiple non-overlapping clusters. Common partitioning-based algorithms include K-means (Anderberg, 1973) and Partitioning Around Medoids (PAM) (Kaufman & Rousseeuw, 1990). A hierarchical approach builds a binary clustering hierarchy whose leaf nodes represent the documents to be clustered. A representative hierarchical clustering algorithm is the hierarchical agglomerative clustering (HAC) method, which starts with as many clusters as there are documents; ie a cluster contains one document only (Voorhees, 1986). The two clusters that bear the most similarity are then merged to form a new cluster. This merging process continues until a hierarchy of clusters emerges, in which a single cluster resides at the top of the hierarchy and contains all source documents. The Kohonen neural network approach, also known as a Self Organising Map (SOM), uses an unsupervised two-layer neural network (Kohonen, 1989 and 1995). Within a Kohonen neural network, an input node corresponds to a coordinate axis in the input vector space. On the other hand, an output node represents a node in a two-dimensional grid. The network is fully connected; that is, each output node is connected to every input node with a particular connection weight. During the training phase, the documents to be clustered are fed into the network many times to train or adjust the connection weights in such a way that distribution of the output nodes would accurately represent or correspond to that of the input objects.

To improve clustering effectiveness, several interactive techniques have been proposed. To shed light on adequate or plausible clusters, Agrawal et al (1999) developed an interactive document clustering technique which presents a set of related documents to a user in an iterative manner so as to understand his or her clustering practice or preference. The user can remove ‘irrelevant’ documents from a cluster as well as include additional documents into a cluster. Similarly, Kim and Lee (2000) have developed a semi-supervised document clustering technique, a hybrid between the HAC method and a relevance-feedback learning technique.

Text categorisation is also related to automated document-category management and essentially deals with the assignment of textual documents to appropriate categories, based on their contents (Apte´ et al, 1994; Yang & Chute, 1994; Dumais et al, 1998; Cohen & Singer, 1999). Central to text categorisation is automatic learning or discovery of important text categorisation patterns, based on a pre-classified training document set. The general text categorisation process is similar to that of document clustering but has several interesting distinctions. For instance, in the feature extraction/selection phase of text categorisation, one or multiple feature sets can be extracted (ie a universal dictionary for all categories or multiple local dictionaries for the respective categories), whereas only one feature set is created in document clustering. In addition to TF and TF × IDF, other feature selection metrics have been commonly used in text categorisation, including correlation coefficient, 2 metric, and mutual information (Lewis & Ringuette, 1994; Schutze et al, 1995; Smadja et al, 1996; Ng et al, 1997; Dumais et al, 1998; Lam & Ho, 1998). In the document representation phase, a source document is represented by the features selected from the dictionary or dictionaries of choice and, at the same time, is labeled to indicate its category membership. From the perspective of AI-based inductive machine learning, category memberships greatly resemble the decision classes of a common classification problem.

Furthermore, text categorisation differs considerably from document clustering in its final (ie induction) phase, where important categorisation patterns are inductively learned using promising statistical or AI-based techniques (Apte´ et al, 1994; Wei & Lee, 2001). The text categorisation patterns critical to distinguishing categories from one another can be automatically induced from a set of pre-classified training documents. Broadly, the techniques for automatic text categorisation pattern learning can be classified into several types, including decision-tree induction (Weiss et al, 1999), decision-rule induction (Apte´ et al, 1994; Cohen & Singer, 1999), knearest neighbour classification (Masand et al, 1992; Yang, 1994; Iwayama & Tokunaga, 1995; Larkey & Croft, 1996), neural networks (Wiener et al, 1995; Ng et al, 1997), Bayesian networks (Lewis & Ringuette, 1994; Larkey & Croft, 1996; Baker & McCallum, 1998; McCallum & Nigam, 1998; Agrawal et al, 1999), and regression models (Yang & Chute, 1994). Yang and Liu (1999) have provided a detailed comparative analysis and empirical evaluation of the categorisation pattern induction techniques frequently used in prior research.

A review of the relevant document clustering and text categorisation literature suggested two areas where additional investigations are needed. First, most prior document clustering research has taken the category discovery-based approach; ie creating distinct categories from source documents without taking into account those previously established by the user. In this perspective, interactive document clustering techniques might support the preservation of an individual user’s document-category practice, but often require a large number of cognitively intense feedback interactions from the user. In spite of their diminished adequacy in waves of new document arrivals, existing categories conceivably can provide a reasonable or efficient foundation upon which new categories may evolve over time. The described category evolution-based approach is capable of preserving the user’s perspective on semantic coherence in different documents and supporting his or her preferred practice for document groupings. In this light, personalisation can be supported in the automated category management of documents obtained from various internet sources. Second, the implicit or explicit time-invariance assumption common to prior text categorisation research needs to be addressed. As discussed, an existing category has been created based on a particular document set, and therefore its adequacy or validity will diminish when its content considerably changes over time. Responding to the significance of automated category management for documents obtained from various internet sources and the discussed research needs in document clustering and text categorisation, we took an evolutionary approach to support of user-centric document management that is described in the following sec tion.

## Design and process of category evolution (CE) technique

Based on the described evolution-based approach, CE addresses the evolving nature of existing categories over time and hence supports personalisation in automated document-category management. Specifically, CE takes as inputs existing document categories and their documents together with the respective category assignments and then determines or generates new categories. For purposes of the intended feasibility assessment and illustration, the current design of CE concentrates on singlecategory documents and deals with a set of document categories rather than a document-category hierarchy.

Broadly, CE performs two functions: category decomposition and category amalgamation. Category decomposition splits an existing category into multiple new categories, each of which contains documents pertaining to a finer topic with a more cohesive or defined scope. Intuitively, decomposition may become desirable or necessary when a category includes a subset of documents on a related, but different topic or sub-topic that is significantly disjoint with that of the remaining documents in the category. On the other hand, category amalgamation merges multiple existing categories to form a single and thus more general category which contains documents of a broader scope. As depicted in Figure 1, the overall process of CE consists of category decomposition and amalgamation phases, of which major tasks are detailed as follows.

## Category decomposition

Several tasks are performed in the category decomposition phase, including feature extraction and selection, document representation, intra-category disjointness evaluation, and category split and document re-assignment. When performing feature extraction, CE extracts from the (categorised) documents a set of features; ie nouns and noun phrases. We adopted the rule-based partof-speech tagger technique developed by Brill (1992 & 1994) to syntactically tag each word in a document. Then, we followed the approach discussed by Voutilainen (1993) to implement a noun-phrase parser to extract nouns and noun phrases from each tagged document. Using the correlation coefficient or TF × IDF feature selection method, multiple (local) dictionaries were

$$
\operatorname{corr} (f, C) = \frac {(N _ {r +} N _ {n -} - N _ {r -} N _ {n +}) \sqrt {N}}{\sqrt {(N _ {r +} + N _ {r -}) (N _ {n +} + N _ {n -}) (N _ {r +} + N _ {n +}) (N _ {r -} + N _ {n -})}}
$$

![](/api/attachments/EY3PQA88/fulltext/images/271e39e753a88b8990e8ec9a250156ffc5cf20eede4d5edefbad22731510c8b2.jpg)  
Categories evolved and re-organized documents  
Figure 1 Overall process of CE.

constructed, each of which was tailored to a particular existing category. Choice of multiple local dictionaries over a universal dictionary was made primarily because of their effectiveness in retaining representative features of each category (Apte´ et al, 1994), a characteristic consistent with our preliminary analysis results.

Results from previous empirical studies showed that the binary representation scheme was able to achieve clustering quality at a level favourably comparable with or better than that attained by other schemes (Roussinov & Chen, 1999). Accordingly, we selected the binary scheme for document representation. Central to category decomposition is the intra-category disjointness evaluation, which examines whether or not a category contains disjoint sets of documents. A partitioning-based clustering approach (ie PAM) was used to tentatively cluster the documents in a category into two groups, whereby documents in the same group shared greater similarity to each other than to those from the other group. In this study, document similarity was measured by Pearson correlation coefficient, which was then transformed into a typical range [0, 1] for similarity measure. Thus, the similarity between two documents $d _ { i }$ and $d _ { j }$ was defined as:

$$
\text { Similarity } (d _ {i}, d _ {j}) = \frac {\left(1 + \frac {\operatorname{Cov} (d _ {i} , d _ {j})}{\sqrt {V (d _ {i}) V (d _ {j})}}\right)}{2}
$$

where $V ( d _ { i } )$ is the variance of feature values in $d _ { i } ,$ and $C o \nu ( d _ { i } , d _ { j } )$ is the co-variance of feature values between $d _ { i }$ and $d _ { j } .$

Accordingly, the degree of disjointness between the resultant groups was examined for each existent category; ie intra-category disjointness evaluation. In this study, we defined the intra-category disjointness measure as:

$$
\text{disjointness} (c, \sigma_ {d} \%) = 1 - \frac {2 \times \left| F _ {c _ {1}} \cap F _ {c _ {2}} \right|}{\left| F _ {c _ {1}} \right| + \left| F _ {c _ {2}} \right|}
$$

where $c$ is the target category whose documents are clustered into $c _ { 1 }$ and $c _ { 2 }$ groups, $\sigma _ { d } \%$ (feature inclusion threshold) is used to remove features of low frequency (ie less than $\sigma _ { d } \%$ of documents) in the category c, and $\boldsymbol { F } _ { c _ { 1 } }$ (or $F _ { c _ { 7 } } )$ is a set of features, each of which at least appears in $\sigma _ { d } \%$ of the documents in c as well as in some documents in $c _ { 1 }$ (or c<sub>2</sub>).

Use of the defined intra-category disjointness measure can be illustrated as follows. Let’s assume that a category currently contains 20 documents $\{ d _ { 1 } , d _ { 2 } , . . . , d _ { 2 0 } \}$ and includes 10 features $\{ f _ { 1 } , f _ { 2 } , . . . , f _ { 1 0 } \}$ selected to represent the documents. As shown in Table 1, assuming the 20 documents in the category be clustered into $c _ { 1 }$ and $c _ { 2 }$ groups, where $c _ { 1 }$ contains nine documents (ie, $d _ { 1 } ,$ $d _ { 2 } , . . . , d _ { 9 } )$ , and $c _ { 2 }$ holds the remaining documents. Let $\sigma _ { d } \%$ be 10%. In this case, $F _ { c _ { 1 } } = \{ f _ { 1 } , f _ { 3 } , f _ { 4 } , f _ { 5 } , f _ { 6 } \}$ . Feature $f _ { 2 }$ appears in document $d _ { 1 }$ (from the $c _ { 1 }$ group) but is not included in $\boldsymbol { F } _ { c _ { 1 } }$ because of its low frequency; ie appearing in less than 10% of the documents in the category. Similarly, $F _ { c _ { 2 } } = \{ f _ { 3 } , f _ { 5 } , f _ { 6 } , f _ { 7 } , f _ { 8 } , f _ { 9 } \}$ . Note that feature $f _ { 1 0 }$ is also excluded from $\boldsymbol { F } _ { c _ { 2 } }$ because of low frequency. Hence, disjointness(c, 10%) is calculated as

Table 1 Illustrations of intra-category disjointness evaluation

<table><tr><td rowspan="2">Groups</td><td rowspan="2">Documents</td><td colspan="9">Features</td><td></td></tr><tr><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $f_4$ </td><td> $f_5$ </td><td> $f_6$ </td><td> $f_7$ </td><td> $f_8$ </td><td> $f_9$ </td><td> $f_{10}$ </td></tr><tr><td rowspan="9"> $c_1$ </td><td> $d_1$ </td><td>y*</td><td>y</td><td>y</td><td>-</td><td>y</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_2$ </td><td>y</td><td>-</td><td>-</td><td>-</td><td>y</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_3$ </td><td>-</td><td>-</td><td>y</td><td>-</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_4$ </td><td>y</td><td>-</td><td>y</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_5$ </td><td>y</td><td>-</td><td>-</td><td>y</td><td>-</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_6$ </td><td>-</td><td>-</td><td>-</td><td>y</td><td>y</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_7$ </td><td>-</td><td>-</td><td>y</td><td>y</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_8$ </td><td>-</td><td>-</td><td>y</td><td>-</td><td>y</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_9$ </td><td>y</td><td>-</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="11"> $c_2$ </td><td> $d_{10}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>y</td><td>-</td><td>y</td><td>-</td><td>y</td><td>-</td></tr><tr><td> $d_{11}$ </td><td>-</td><td>-</td><td>y</td><td>-</td><td>y</td><td>-</td><td>-</td><td>y</td><td>-</td><td>-</td></tr><tr><td> $d_{12}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>y</td><td>-</td><td>-</td><td>y</td><td>-</td><td>-</td></tr><tr><td> $d_{13}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_{14}$ </td><td>-</td><td>-</td><td>y</td><td>-</td><td>y</td><td>y</td><td>-</td><td>y</td><td>y</td><td>-</td></tr><tr><td> $d_{15}$ </td><td>-</td><td>-</td><td>y</td><td>-</td><td>-</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_{16}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>y</td><td>-</td><td>y</td><td>y</td></tr><tr><td> $d_{17}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>y</td><td>y</td><td>-</td><td>y</td><td>-</td></tr><tr><td> $d_{18}$ </td><td>-</td><td>-</td><td>y</td><td>-</td><td>y</td><td>-</td><td>y</td><td>y</td><td>-</td><td>-</td></tr><tr><td> $d_{19}$ </td><td>-</td><td>-</td><td>y</td><td>-</td><td>y</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $d_{20}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>y</td><td>y</td><td>y</td><td>y</td><td>-</td></tr></table>

\*Documents are represented using a binary representation scheme where $\mathrm { ^ { * } y ^ { * } }$ denotes the presence of a feature in the document and $^ { \ell } - { } ^ { \ell }$ denotes the absence of the feature.

$$
1 - \frac {2 \times \left| F _ {c _ {1}} \cap F _ {c _ {2}} \right|}{\left| F _ {c _ {1}} \right| + \left| F _ {c _ {2}} \right|} = 1 - \frac {2 \times 3}{5 + 6} = 0. 4 5 5.
$$

When exhibiting an intra-category disjointness greater than the pre-specified threshold $( \alpha _ { s } )$ , a category should be split and its documents have to be re-assigned accordingly. The split decision needs to be evaluated for all existing categories. That is, a category c will be decomposed when disjointness(c, $\sigma _ { d } \% ) > \ \sigma _ { s } .$ . Otherwise, the category remains as it is. Using the discussed document similarity measure, CE adopts the PAM technique to decompose a target category into multiple categories. The exact number of categories created or decomposed from an existing category is determined by the silhouette coefficient measure<sup>2</sup> (Kaufman & Rousseeuw, 1990).

$$
s (i) = 1 - \frac {a (i)}{b (i)} \mathrm{if} a (i) <   b (i)
$$

Subsequently, all documents in the original category are assigned to appropriate (new) categories.

## Category amalgamation

The category amalgamation phase of CE consists of several tasks, including feature re-selection and document re-representation, inter-category overlapping evaluation, and category coalescence. For feature re-selection, CE performs or re-performs feature selection for each new (ie decomposed) category generated in the category decomposition phase. For categories that remain intact, feature re-selection is not necessary since their respective document sets remain the same. As a result, local dictionaries are re-constructed using the same feature selection method adopted by the category decomposition phase (ie correlation coefficient or $\mathrm { T F } \times \mathrm { I D F }$ feature selection method). The binary scheme used in the category decomposition phase is selected for document representation in the category amalgamation phase.

Following feature re-selection and document re-representation is the examination of overlapping categories, using an inter-category overlapping measure of choice. In this study, we defined and thus measured inter-category overlapping as follows.

$$
\text { overlapping } (c _ {i}, c _ {j}, \sigma_ {o} \%) = \frac {2 \times | F _ {c _ {i}} \cap F _ {c _ {j}} |}{| F _ {c _ {i}} | + | F _ {c _ {j}} |}
$$

where $c _ { i }$ and $c _ { j }$ are the categories under evaluation, $\sigma _ { o } \%$ (feature inclusion threshold) is used to remove features of low frequency (ie less than $\sigma _ { o } \%$ of documents) in each category, and $F _ { c _ { i } } \left( \mathrm { o r } F _ { c _ { i } } \right)$ is the set of features, each of which at least appears in $( \sigma _ { o } \%$ of the documents in $c _ { i }$ (or $c _ { j } )$

We illustrate the defined inter-category overlapping measure as follows. Let’s assume the feature sets of categories $\mathrm { c } _ { 1 }$ and $c _ { 2 }$ be $F _ { c _ { 1 } } = \{ f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 } , f _ { 5 } , f _ { 6 } \}$ and $F _ { c _ { 2 } } =$ $\{ f _ { 4 } , f _ { 6 } , f _ { 7 } , f _ { 8 } , f _ { 9 } , f _ { 1 0 } \}$ , respectively. We also assume that $\sigma _ { o } \%$ is 0. Since feature $f _ { 4 }$ and $f _ { 6 }$ appear in both $c _ { 1 }$ and $^ { c _ { 2 } , }$ , the degree of overlapping between these two categories is 0.33, calculated as the follows:

$$
\text { overlapping } (c _ {1}, c _ {2}, 0 \%) = \frac {2 \times \left| F _ {c _ {1}} \cap F _ {c _ {2}} \right|}{\left| F _ {c _ {1}} \right| + \left| F _ {c _ {2}} \right|}
$$

$$
S C = \max _ {k} \bar {\mathrm{s}} (k)
$$

$$
= \frac {2 \times 2}{6 + 6} = 0. 3 3.
$$

Subsequently, CE performs category coalescence by comparing the degree of overlapping between categories to the pre-specified threshold. Assuming the merging threshold be $\alpha _ { m } ,$ two categories should be merged when exhibiting a degree of overlapping exceeds $\alpha _ { m } .$ . Conceivably, category coalescence proceeding in the described pair-wise manner might result in conflicting decisions. For instance, assume that categories A and B are suggested (by EC) to be merged because their degree of overlapping is greater than $\alpha _ { m }$ . So are categories B and C. The pair-wise merging process will ultimately merge categories A, $B ,$ and C into a larger category. However, if overlapping(A, C, $\begin{array} { r } { \sigma _ { o } \% ) \leq \ \alpha _ { m } , } \end{array}$ categories A and C indeed should not be merged; thus, conflicting decisions arise.

Category coalescence needs to address such conflicting category-merging decisions. Toward this, CE uses a graph representation to analyse the individual merging decisions under examination, where nodes represent categories and labeled undirected links indicate the respective merging decisions. The degree of overlapping between two categories (eg $c _ { i }$ and $c _ { j } )$ is associated with the link connecting the nodes that represent them. Using the described graph representation, we represent all the merging decisions suggested in the pair-wise inter-category overlapping evaluation. For each connected subgraph of size greater than one (as measured by the number of nodes) which is not a complete graph,<sup>3</sup> its link with the lowest overlapping measure is then removed. This process is repeated until all sub-graphs become complete graphs. To illustrate the discussed conflict resolution method, let’s assume that the merging threshold is 0.4 and that a graph has been constructed using merging decisions suggested by the pair-wise inter-category overlapping evaluation results (as shown in Figure 2). As noted, two sub-graphs of size greater than one exist. One sub-graph (including nodes $c _ { 1 } , \ : c _ { 2 } ,$ and $c _ { 3 } )$ is not a complete graph. In this case, the edge with the lowest value (ie the link connecting $c _ { 1 }$ and $c _ { 2 } )$ has to be removed. The resultant sub-graph then becomes complete, denoting that the merging of $c _ { 2 }$ and $c _ { 3 }$ should be performed, but not that for $c _ { 1 }$ and $c _ { 2 } .$ The other sub-graph (including $c _ { 4 } , \ : c _ { 5 }$ and $c _ { 6 } )$ is already a complete graph and thus the merging of $c _ { 4 } , \ : c _ { 5 }$ and $c _ { 6 }$ should proceed.

![](/api/attachments/EY3PQA88/fulltext/images/1b15d559d06adfde6688967e1456c3651aea637c2e260426776d6c58346aceb2.jpg)  
Figure 2 Graph-based conflicting coalescence decisions resolution— an example.  
<sup>3</sup> A graph is considered to be a complete graph when there exists an edge between every pair of nodes in an undirected graph.

Upon the completion of category amalgamation phase, CE generates a set of (new) categories that in effect evolve from those previously established by the user and accordingly re-assigns the (source) documents to the appropriate resultant categories. Appendix A describes the complete algorithm of CE. At a nutshell, CE addresses the category evolution phenomenon by generating a new set of categories through the re-organisation of existing categories. Hence, the assignment of a newly arrived document to an appropriate category can be performed manually or automatically (eg using a text categorisation algorithm). The CE technique is not designed for such document assignments; rather, it performs the needed document category re-organisation in situations where influxes of new documents significantly diminish the adequacy of the existing categories.

## Evaluation design and results

Design of our experimental evaluation focused on CE’s effectiveness and sensitivity to the quality of existing categories. The single-category version of Distribution 1.0 of Reuters-21578 document collection (available at http://www.research.att.com/-lewis/reuters21578.html) was the particular document set used in the evaluation. A sample news document is shown in Appendix B. We approximated a user’s true (or preferred) categories using those specified in the Reuters-21578 collection. The target category evolution phenomenon then can be simulated by category re-organisation scenarios. Accordingly, we created a scenario where category re-organisation was needed. Using the procedure to be described in section 4.1, we took the true categories and performed random merges or splits so that the documents contained in the randomised categories partially preserved the semantic coherency embedded in the categories specified by the Reuters. These randomised categories together with their documents then became input to the CE which, in turn, generated new categories whose quality was then evaluated against the true categories. Also included in the evaluation was a category discovery-based technique (using the PAM clustering algorithm) which provided a performance benchmark. Furthermore, we examined sensitivity of the CE’s performance to the quality of input (ie existing) categories. That is, we designed different scenarios where the input categories considerably varied in their desired or true category preservation and hence examined CE’s sensitivity to various input category quality under evaluation.

The source document set (ie Reuter-21578 collection) contains 64 categories and 9034 single-category documents. In our evaluation, we selected those categories that included a minimum of 100 documents. Among those selected, two categories (ie the ‘acq’ and ‘earn’ categories) contained more documents than others; ie 2237 and 3801 documents respectively. From these two categories, we only selected documents that were 10–30 lines in length in the evaluation. Choice of the document length contributed to balancing the size of the selected categories as well as that for the documents ultimately used. As a result, our evaluation included a total of 10 categories and 2697 documents, each of which had an average of 192 words.

## Evaluation procedure

We assumed the categories specified in the Reuters-21578 collection to be true categories. From the 10 categories that met our preliminary selection criteria, we randomly chose six for the test data set. To create or simulate a scenario where category re-organisation was needed, we randomly selected from the test data set three categories, each of which was then arbitrarily split into two (new) categories; thus, making the total of categories equal nine. The documents contained in each selected category were randomly, but evenly assigned to the newly created categories. From the nine resulting categories, two categories were randomly selected and merged to form a new category which then contained the documents from both categories merged. A total of three random merges were performed without repetition (ie no categories were merged twice); thus, making the final categories used in the evaluation equal to six. Hence, in the simulated scenario, six true categories in effect were arbitrarily transformed into six randomised categories whose re-organisation became necessary. Subsequently, CE was applied and its resulting categories were then compared with the true categories. A total of ten trials were performed to minimise the potential biases resulting from the randomisation procedure described.

## Evaluation criteria

The quality of the categories generated by CE or the benchmark category discovery-based technique was examined in terms of category composition and coverage. From a composition perspective, a category evolved or discovered should contain documents from a single true category only. We measured the composition of a resulting category using purity which is defined as the maximum number of documents pertaining to the same underlying true category divided by the total number of documents contained in the category (Agrawal et al, 1999):

$$
P u r i t y (c) = \frac {n _ {c}}{N _ {c}}
$$

where $n _ { c }$ denotes maximal number of documents in an evolved or discovered category c pertaining to the same true category, and $N _ { c }$ denotes the number of documents included in the category c.

The overall purity of a set of categories evolved or discovered can be derived by taking the weighted average of the purity of individual categories. Hence,

$$
P u r i t y = \sum_ {c} P u r i t y (c) \times \frac {N _ {c}}{N},
$$

where

$$
N = \sum_ {c} N _ {c}
$$

denotes the summation of the documents included in each evolved or discovered category.

From a coverage perspective, a set of evolved or discovered categories should cover all the true categories. The true category coverage or the dominant class of an evolved or discovered category denotes the true category from which an evolved or discovered category contains the maximal number of documents in its current content. Let’s assume an evolved category E contains 60% of its documents from the true category A and the remaining from the true category B. In the case, the true category coverage of $E$ is A because of its dominance in $E \ ' s$ current document collection. Specifically, we measured the power of true category coverage in terms of diversity which is defined as the portion of true categories that are covered by all the evolved or discovered categories under evaluation (Agrawal et al, 1999). Hence,

$$
D i v e r s i t y = \frac {R}{T}
$$

where R denotes the number of true categories covered by the evolved or discovered categories under evaluation, and T denotes the number of true categories.

Conceivably, the described purity and diversity measures would favour a large set of evolved or discovered categories, each of which contains few documents. At the extreme, each evolved or discovered category contains one document only and, in this case, the overall purity and diversity would be maximized (ie reaching 100%). When not properly addressed, the propensity in favour of a large category set would then defeat the purpose of document category and consequently the user has to browse documents from an overwhelmingly large category set. To mitigate or avoid such bias, the efficiency of true category coverage is important and was measured using specificity, defined as the number of true categories covered by the evolved or discovered categories divided by the total number of the categories evolved or discovered. Hence,

$$
S p e c i f i c i t y = \frac {R}{E}
$$

where E is the total number of evolved or discovered categories.

To illustrate use of the described evaluation criteria, consider the following example. Assume A, B, C and D be the true categories, each of which contains 250 documents. Let the evolved categories to be evaluated be $E _ { 1 } , E _ { 2 } , E _ { 3 } , E _ { 4 }$ and $E _ { 5 }$ . Table 2 summarises the documents in each evolved category and the true category covered by the respective evolved categories. As noted, the evolved category $E _ { 3 }$ contains 250 documents from true category B and 150 documents from true category C. In $E _ { 3 } ,$ the documents pertaining to true category B outnumbers those from true category C, making B the true category covered by $E _ { 3 }$

The purity of each evolved category can be calculated by dividing the number of documents from the true category covered by the total number of documents contained. For instance, Purity $( E _ { 3 } )$ is 0.625; ie 250/400 = 0.625. Similarly, the purity of the entire evolved category set can be derived as follows.

$$
\begin{aligned} Purity & = Purity (E_{1}) \times \frac{100}{1000} + Purity (E_{2}) \times \frac{120}{1000} + \\ & \quad Purity (E_{3}) \times \frac{400}{1000} + Purity (E_{4}) \times \frac{250}{1000} + \\ & \quad Purity (E_{5}) \times \frac{130}{1000} \\ & = \frac{100}{100} \times \frac{100}{1000} + \frac{120}{120} \times \frac{120}{1000} + \\ & \quad \frac{250}{400} \times \frac{400}{1000} + \frac{150}{250} \times \frac{250}{1000} + \\ & \quad \frac{100}{130} \times \frac{130}{1000} = 72 \% \end{aligned}
$$

As shown in Table 2, the set of evolved category under evaluation indeed covers true category A, B and D. Hence, the diversity of the evolved categories can be calculated as follows.

$$
D i v e r s i t y = \frac {\left| \{A , B , D \} \right|}{\left| \{A , B , C , D \} \right|} = \frac {3}{4} = 75 \%
$$

Table 2 Evaluation of evolved or discovered categories: an example

<table><tr><td>Evolved category</td><td>Document composition</td><td>True category covered</td></tr><tr><td> $E_{1}$ </td><td>100 documents from A</td><td>A</td></tr><tr><td> $E_{2}$ </td><td>120 documents from A</td><td>A</td></tr><tr><td> $E_{3}$ </td><td>250 documents from B, and 150 documents from C</td><td>B</td></tr><tr><td> $E_{4}$ </td><td>150 documents from D, and 100 documents from C</td><td>D</td></tr><tr><td> $E_{5}$ </td><td>30 documents from A, and 100 documents from D</td><td>D</td></tr></table>

Similarly, the specificity of the evolved category set can be obtained as follows.

$$
\text {Specificity} = \frac {\left| \{A , B , D \} \right|}{\left| \left\{E _ {1} , E _ {2} , E _ {3} , E _ {4} , E _ {5} \right\} \right|} = \frac {3}{5} = 60 \%
$$

Effects of feature size and feature selection method Choice of feature selection method and the exact number of features used to represent source (input) documents may affect CE’s effectiveness. Because of their common use in prior research, we implemented both correlation coefficient and $\mathrm { T F } \times \mathrm { I D F }$ feature selection methods and designed empirical evaluation for relative performance comparison. In addition, we also examined different numbers of features (k) to be used for document representation, ranging from 25–100 at increments of 25. Based on our preliminary parameter tuning evaluation results, we set the feature inclusion threshold for intracategory disjointness $( \sigma _ { d } \% )$ at 0.05, the feature inclusion threshold for inter-category overlapping measure $( \sigma _ { o } \% )$ at 0, a split threshold of 0.6, and a merging threshold of 0.4.

Table 3 summarises the evaluation results. As the number of features increased from 25–100, the purity of the resulting (ie evolved) categories generally improved when the correlation coefficient method was used for feature selection, except when $k = 1 0 0 .$ . On the other hand, the purity largely remained unchanged when the $\mathrm { T F } \times \mathrm { I D F }$ method was used for feature selection. In either case, an increase in the number of features appeared to have shown marginal effects on diversity. Furthermore, an increase in the number of features resulted in a noticeable reduction in specificity of the evolved categories, regardless of the feature selection method used.

In addition, use of the correlation coefficient method resulted in higher purity and diversity than those achieved by the TF × IDF method, across the different numbers of features examined. However, the specificity resulting from the use of TF × IDF method was significantly higher than that using the correlation coefficient method, regardless of the number of features. A plausible explanation may be that use of the correlation coefficient method would select highly distinctive features capable of differentiating one category from the others, whereas the $\mathrm { T F } \times \mathrm { I D F }$ method is effective for selecting representative features for each category. In this case, choice of the correlation coefficient method for feature selection can reduce the degree or likelihood of feature overlapping between categories, making category coalescence relatively difficult than would with the TF × IDF method. With the correlation coefficient method, the average number of categories evolved is significantly higher than that of true categories (ie six) or that by the $\mathrm { T F } \times \mathrm { I D F }$ method, across all the number of features examined (as shown in Table 3). Taken all the evaluation criteria into consideration, the TF × IDF method overall appeared to have exhibited a more balanced if not better performance than did the correlation coefficient method. Hence, we selected the TF × IDF method for feature selection and set the number of features at 50 in the subsequent evaluation.

Table 3 Evaluation results using $\alpha _ { s } = 0 . 6 ,$ $\alpha _ { m } = 0 . 4 ,$ $\alpha _ { d } \% = 0 . 0 5 ,$ , and $\sigma _ { o } \% = 0$

<table><tr><td>Feature selection method</td><td>Number of features (k)</td><td>Purity</td><td>Diversity</td><td>Specificity</td><td># of categories evolved</td></tr><tr><td rowspan="4">Correlation coefficient</td><td>25</td><td>83.61%</td><td>96.67%</td><td>68.79%</td><td>8.6</td></tr><tr><td>50</td><td>84.71%</td><td>96.67%</td><td>65.59%</td><td>9</td></tr><tr><td>75</td><td>92.41%</td><td>98.33%</td><td>47.61%</td><td>12.5</td></tr><tr><td>100</td><td>89.06%</td><td>100%</td><td>52.88%</td><td>11.5</td></tr><tr><td rowspan="4">TF × IDF</td><td>25</td><td>72.77%</td><td>83.33%</td><td>89.82%</td><td>5.7</td></tr><tr><td>50</td><td>71.06%</td><td>81.67%</td><td>88.57%</td><td>5.6</td></tr><tr><td>75</td><td>70.81%</td><td>80.00%</td><td>83.95%</td><td>5.8</td></tr><tr><td>100</td><td>72.62%</td><td>81.67%</td><td>77.82%</td><td>6.4</td></tr></table>

## Effects of split and merging thresholds

We also examined the effects of split and merging thresholds on CE’s effectiveness. Particularly, we examined different split thresholds, ranging from 0.4 –0.7 at increments of 0.1. At the same time, we investigated three merging thresholds; namely, 0.2, 0.3 and 0.4. As shown in Table 4d, an increase of the split threshold makes the category decomposition more difficult (ie resulting in a decreased number of categories evolved), whereas an increase of the merging threshold leads to an increased number of categories evolved. In general, the evolved categories improved in purity as the split threshold decreased, across all the merging thresholds examined (as shown in Table 4a). However, the purity of these categories diminished as the merging threshold decreased. As highlighted in Table 4b, effects of the split or merging threshold on the diversity of the evolved categories were similar to those observed for purity. On the other hand, effects of the split or merging threshold on the specificity of the evaluated categories, as shown in Table 4c, was largely opposite to that observed for purity or diversity. That is, the specificity of the evolved categories deteriorated when the split threshold decreased but improved when the merging threshold decreased.

Table 4 Effects of split and merging thresholds (using $\sigma _ { d } \% =$ 0.05, $\begin{array} { r } { \sigma _ { o } \% = 0 , } \end{array}$ TF × IDF for feature selection, and $\bar { k } = 5 0 )$

<table><tr><td rowspan="2">Split threshold ( $\alpha_s$ )</td><td colspan="3">Merging threshold ( $\alpha_m$ )</td></tr><tr><td>0.4</td><td>0.3</td><td>0.2</td></tr><tr><td colspan="4">(a) Purity of the categories evolved</td></tr><tr><td>0.7</td><td>72.49%</td><td>69.16%</td><td>65.84%</td></tr><tr><td>0.6</td><td>71.06%</td><td>69.26%</td><td>65.09%</td></tr><tr><td>0.5</td><td>73.53%</td><td>71.06%</td><td>67.70%</td></tr><tr><td>0.4</td><td>78.90%</td><td>77.21%</td><td>74.79%</td></tr><tr><td colspan="4">(b) Diversity of the categories evolved</td></tr><tr><td>0.7</td><td>78.33%</td><td>75.00%</td><td>70.00%</td></tr><tr><td>0.6</td><td>81.67%</td><td>75.00%</td><td>70.00%</td></tr><tr><td>0.5</td><td>83.33%</td><td>78.33%</td><td>71.67%</td></tr><tr><td>0.4</td><td>91.67%</td><td>90.00%</td><td>86.67%</td></tr><tr><td colspan="4">(c) Specificity of the categories evolved</td></tr><tr><td>0.7</td><td>92.67%</td><td>98.00%</td><td>100%</td></tr><tr><td>0.6</td><td>88.57%</td><td>98.33%</td><td>98.00%</td></tr><tr><td>0.5</td><td>84.96%</td><td>91.33%</td><td>96.33%</td></tr><tr><td>0.4</td><td>79.82%</td><td>82.05%</td><td>85.80%</td></tr><tr><td colspan="4">(d) Number of the categories evolved</td></tr><tr><td>0.7</td><td>5.1</td><td>4.6</td><td>4.2</td></tr><tr><td>0.6</td><td>5.6</td><td>4.6</td><td>4.3</td></tr><tr><td>0.5</td><td>6.0</td><td>5.2</td><td>4.5</td></tr><tr><td>0.4</td><td>7.1</td><td>6.8</td><td>6.2</td></tr></table>

The overall diversity was satisfactory, recorded at a 79.31% level. Likewise, the specificity achieved by CE was also satisfactory, ranging from 79.82–100%. As shown in Table 4d, choice of a split threshold higher than 0.4 would result in an under-split tendency of CE. On the other hand, a merging threshold of 0.2 would lead to an over-merging behavior by CE. Taken all three evaluation criteria into account, a split threshold of 0.4 and a merging threshold of 0.3 appeared to be adequate, as suggested by the recorded 77.21% in purity, 90% in diversity, and 82.05% in specificity.

## Performance benchmark evaluation

The performance of CE was further examined, using that achieved by a category discovery-based technique as a benchmark. To support the comparative analysis, we implemented a partitioning-based clustering algorithm for category discovery. Given the choice of the binary scheme for document representation in CE implementation, the PAM algorithm was selected, primarily because of its capability of handling non-numerical values. Accordingly, the six randomised categories in a simulated scenario were merged into a single category to which the PAM-based discovery technique was applied to group the documents into clusters. Implementation of the PAM-based category discovery technique used the silhouette coefficient measure to determine an optimal number of clusters.

To reduce biases and preserve consistency (with the procedure for CE evaluation), the selection-and-discovery process was performed ten times. The overall performance was obtained by averaging the performance recorded in each trial run. Compared to those by CE, the category discovery-based technique produced higher diversity but lower purity and specificity. As highlighted in Table 5, the benchmark category discovery-based technique appeared to have exhibited a tendency for creating a larger number of categories; ie 7.70 vs 5.35 by CE. Given the split and merging thresholds of choice (ie $\alpha _ { s } = 0 . 4$ and $\alpha _ { m } = 0 . 3 )$ , CE noticeably outperformed the benchmark technique in terms of purity and specificity and was able to maintain the diversity at a level comparable to that accomplished by the benchmark technique. Results from our comparative evaluation jointly suggested that CE was more effective than the benchmark category discovery-based technique.

## Sensitivity to input category quality

Imaginably, CE is likely to be applied to category reorganisation situations which considerably vary in the existing (input) category quality. In essence, the described randomised split and merging procedure had indeed altered the quality of existing categories with respect to that of the original (ie true) Reuter-21578 classification. Logically, the quality of an evolved category is likely to deteriorate as additional random splits or merges are applied. Hence, we evaluated CE’s sensitivity to the quality of input categories by examining its effectiveness in scenarios created by a different number of random splits and merges, ranging from two to five respectively.

To evaluate a particular split and merge combination, we randomly selected from the source document set (ie ten categories) a total of six true categories, from each of which we then chose 100 documents randomly. The rationale for selecting the same number of documents for each true category is to isolate potential effects of category size on evaluation results. Thus, we performed on the chosen data set the particular number of splits and merges under examination. The process was repeated ten times for each split-merge combination evaluated. CE was then applied to the resulting categories and its overall performance was analyzed. Specifically, our sensitivity evaluation used the same methods or parameter values discussed in Section 4.3 and 4.4; ie $\mathrm { T F } \times \mathrm { I D F }$ for feature selection, binary scheme for document representation, top 50 features, a feature inclusion threshold for intra-category disjointness measure $( \alpha _ { d } \% )$ of 0.05, a feature inclusion threshold for inter-category overlapping measure $( \alpha _ { o } \% )$ of 0, a split threshold $( \alpha _ { s } )$ of 0.4, and a merging threshold $( \alpha _ { m } )$ of 0.3. Table 6 summarizes the sensitivity analysis results.

As shown in Table 6a, the purity of the evolved categories increased with the number of splits, but decreased with the number of merges. The effect of the exact number of splits or merges on diversity was similar to that observed for purity, as shown in Table 6b. The average diversity improved by 15.83% (ie from 76.67–92.50%) when the number of splits increased from two to five. Nevertheless, the average diversity appeared to have decreased as the number of merges increased from two to five; ie from 94.58–73.75%. Furthermore, specificity increased from 75.73–86.10% as the number of merges increased from two to five but remained largely stable across the number of splits examined (as shown in Table 6c). Overall, CE averaged 74.26% in purity, 85.94% in diversity, and 81.74% in specificity. In the most challenging scenario characterised by the maximal number of splits and merges under evaluation, CE was able to exhibit satisfactory or reasonable effectiveness; ie 70.17% in purity, 83.33% in diversity and 79.55% in specificity.

## Summary

Continually, an existing category has to adapt to the changes in its document collection. Motivated by the importance of automated management for textual documents obtained from various internet sources, we designed, implemented and experimentally evaluated an evolution-based technique for managing existing categories’ evolution over time. Judged by the evaluation results, the proposed technique is able to preserve essential personal perspective on or practice for document groupings and, at the same time, shed light on the desirability of the evolution-based approach as a feasible and appealing alternative to the category discovery-based approach common to previous research. In addition, this research also responds to the unrealistic time-invariance assumption made by most prior text categorisation studies.

Table 5 Comparative performance—CE vs benchmark discovery-based technique

<table><tr><td></td><td>Purity</td><td>Diversity</td><td>Specificity</td><td># of categories resulted</td></tr><tr><td>CE (average)</td><td>71.34%</td><td>79.31%</td><td>91.32%</td><td>5.35</td></tr><tr><td>CE ( $\alpha_s = 0.4, \alpha_m = 0.3$ )</td><td>77.21%</td><td>90.00%</td><td>82.05%</td><td>6.80</td></tr><tr><td>PAM-based category discovery</td><td>62.96%</td><td>93.33%</td><td>76.72%</td><td>7.70</td></tr></table>

Table 6 Results of CE’s sensitivity to existing (input) category quality

<table><tr><td rowspan="2">Number of merges</td><td colspan="5">Number of splits</td></tr><tr><td>2</td><td>3</td><td>4</td><td>5</td><td>Average</td></tr><tr><td colspan="6">(a) Purity of the categories evolved</td></tr><tr><td>2</td><td>81.74%</td><td>81.91%</td><td>88.91%</td><td>92.54%</td><td>86.27%</td></tr><tr><td>3</td><td>71.92%</td><td>77.45%</td><td>82.32%</td><td>82.63%</td><td>78.58%</td></tr><tr><td>4</td><td>64.54%</td><td>73.97%</td><td>72.27%</td><td>77.15%</td><td>71.99%</td></tr><tr><td>5</td><td>51.50%</td><td>56.51%</td><td>62.59%</td><td>70.17%</td><td>60.19%</td></tr><tr><td>Average</td><td>67.43%</td><td>72.46%</td><td>76.52%</td><td>80.62%</td><td>74.26%</td></tr><tr><td colspan="6">(b) Diversity of the categories evolved</td></tr><tr><td>2</td><td>88.33%</td><td>91.67%</td><td>98.33%</td><td>100%</td><td>94.58%</td></tr><tr><td>3</td><td>78.33%</td><td>90.00%</td><td>96.67%</td><td>95.00%</td><td>90.00%</td></tr><tr><td>4</td><td>78.33%</td><td>85.00%</td><td>86.67%</td><td>91.67%</td><td>85.42%</td></tr><tr><td>5</td><td>61.67%</td><td>68.33%</td><td>81.67%</td><td>83.33%</td><td>73.75%</td></tr><tr><td>Average</td><td>76.67%</td><td>83.75%</td><td>90.83%</td><td>92.50%</td><td>85.94%</td></tr><tr><td colspan="6">(c) Specificity of the categories evolved</td></tr><tr><td>2</td><td>80.70%</td><td>78.50%</td><td>67.26%</td><td>76.48%</td><td>75.73%</td></tr><tr><td>3</td><td>88.48%</td><td>77.20%</td><td>76.64%</td><td>77.45%</td><td>79.94%</td></tr><tr><td>4</td><td>89.81%</td><td>86.05%</td><td>77.37%</td><td>87.55%</td><td>85.19%</td></tr><tr><td>5</td><td>88.81%</td><td>88.50%</td><td>87.56%</td><td>79.55%</td><td>86.10%</td></tr><tr><td>Average</td><td>86.95%</td><td>82.56%</td><td>77.21%</td><td>80.26%</td><td>81.74%</td></tr></table>

Measured by purity, diversity and specificity, the proposed technique (CE) exhibited satisfactory effectiveness across different category evolution scenarios and various split or merge thresholds. Overall, CE outperformed the benchmark category discovery-based technique, showing better purity and specificity and, at the same time, maintaining the diversity at a comparable level. The observed effectiveness was reasonably robust with respect to differential input (existing) category quality.

This study has contributed document management research by addressing the probable evolution phenomenon of existing document categories over time, a fundamental issue which has not yet duly been examined by prior research. Research contributions are also made by examining the feasibility and desirability of an evolution-based approach for document-category management of which previous research is dominated by the category discovery-based approach. Toward this, we develop a reasonably satisfactory and robust technique whose effectiveness is better than that of a common category discovery-based technique. From a practical perspective, findings from the current research also advance the document management practice by individuals and organisations in the emerging e-commerce environments. Anchored at the discussed evolution-based approach, the proposed technique probably is more desired than those based on complete category discovery. By adapting from existing categories that reflect an individual’s preference or practice, our technique supports personalisation in automated document-category management.

This study is intended to serve as a departure point for continued research on document-category management, and thus has several limitations. First, the timing or condition under which a merge or split becomes necessary or desired has not been examined. Our evaluation focused on demonstrating the proposed technique’s effectiveness and thus proceeded with scenarios where document category re-organisation was required. Additional investigations are needed to examine the particular timing or condition under which a merge or split has to be performed. Second, use of simulated rather than real-world scenarios in the evaluation is another limitation. To address this limitation which may constrain the degree to which the reported results can be generalised, designs of further evaluation that involve human subjects are currently underway. Third, our research scope also represents another source of limitation. Because of its illustration purpose, this study focuses on single-category documents. Understandably, a document may simultaneously pertain to multiple categories (to equal or differential degrees) and thus effective category management requires a technique capable of dealing with multi-category documents. In addition, this research concentrated on categories organised nonhierarchically; ie using a (flat) set. Hence, the proposed technique (CE) has to be extended for multi-category documents and hierarchical category structure. Last but not least, issues on the user behaviours in response to category change and document re-assignment are important as well. Users familiar with existing but

increasingly inadequate document categories may incur considerable cognitive efforts to learn and become accustom to the newly evolved categories for the subsequent document access. In this vein, changes in access behaviour have to be examined and supported using mechanisms effective for the transition. In turn, these limitations and others single out the particular areas where continued investigations are needed.

Acknowledgments – This work was supported in part by National Science Council of the Republic of China under the grant NSC-89- 2416-H-110-095. The authors would like to thank Professor N-S Chen who provided helpful comments on an earlier draft of this paper.

## References

Agrawal R, Bayardo R and Srikant R (1999) Athena: miningbased interactive management of text databases. In Proceedings of the Seventh Conference on Extending Database Technology, pp 365–379.

Anderberg MR (1973) Cluster Analysis for Applications. Academic Press.

Apte´ C, Damerau F and Weiss SM (1994) Automated learning of decision rules for text categorization. ACM Transactions on Information Systems 12(3), 233–251.

Baker LD and McCallum AK (1998) Distributional clustering of words for text classification. In Proceedings of the 21st International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 96–103.

Boley D, Gini M, Gross R, Han E, Hastings k, Karypis G, Kumar V, Mobasher B and Moore J (1999) Partitioning-based clustering for web document categorization. Decision Support Systems 27(3), 329–341.

Brill E (1992) A simple rule-based part of speech tagger. In Proceedings of the Third Conference on Applied Natural Language Processing.

Brill E (1994) Some advances in rule-based part of speech tagging. In Proceedings of the Twelfth National Conference on Artificial Intelligence (AAAI-94).

Cohen WW and Singer Y (1999) Context-sensitive learning methods for text categorization. ACM Transactions on Information Systems 17(2), 141–173.

Cutting D, Karger D, Pedersen J and Tukey J (1992) Scatter/gather: a cluster-based approach to browsing large document collections. In Proceedings of 15th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 318–329.

Dumais S, Platt J, Heckerman D and Sahami M (1998) Inductive learning algorithms and representations for text categorization. In Proceedings of the ACM 7th International Conference on Information and Knowledge Management (CIKM ’98), pp 148–155.

El-Hamdouchi A and Willett P (1986) Hierarchical document clustering using ward’s method. In Proceedings of ACM Conference on Research and Development in Information Retrieval, pp 149–156.

Iwayama M and Tokunaga T (1995) Cluster-based text categorization: a comparison of category search strategies. In Proceedings of 18th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 273–281.

Kaufman L and Rousseeuw PJ (1990) Finding Groups in Data: An Introduction to Cluster Analysis. John Wiley & Sons, New York.

Kim H and Lee S (2000) A semi-supervised document clustering technique for information organisation. In Proceedings of the 9th International Conference on Information and Knowledge Management (CIKM), pp 30–37.

Kohonen T (1989) Self-Organization and Associative Memory. Springer.

Kohonen T (1995) Self-Organizing Maps. Springer.

Lagus K, Honkela T, Kaski S and Kohonen T (1996) Self organising maps of document collections: a new approach to interactive exploration. In Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining.

Lam W and Ho CY (1998) Using a generalized instance set for automatic text categorization. In Proceedings of the 21st International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 81–89.

Larkey L and Croft W (1996) Combining classifiers in text categorization. In Proceedings of the 19th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 289–297.

Larsen B and Aone C (1999) Fast and effective text mining using linear-time document clustering. In Proceedings of the 5th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp 16–22.

Lewis D and Ringuette M (1994) A comparison of two learning algorithms for text categorization. In Proceedings of Symposium on Document Analysis and Information Retrieval.

Masand B, Linoff G and Waltz D (1992) Classifying news stories using memory based reasoning. In Proceedings of the 15th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 59–65.

McCallum AK and Nigam K (1998) A comparison of event models for naΧve bayes text classification. In Proceedings of AAAI-98 Workshop on Learning for Text Categorization.

Ng HT, Goh WB and Low KL (1997) Feature selection, perception learning, and a usability case study for text categorization. In Proceedings of the 20th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 67–73.

Roussinov D and Chen H (1999) Document clustering for electronic meetings: an experimental comparison of two techniques. Decision Support Systems 27(1–2), 67–79.

Rucker J and Polanco MJ (1997) Siteseer: personalized navigation for the Web. Communications of the ACM 40(3), 73–75.

Schutze H, Hull DA and Pedersen JO (1995) A comparison of classifiers and document representations for the routing problem. In Proceedings of the 18th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 229–237.

Smadja F, Mckeown KR and Hatzivassilogou V (1996) Translating collocations for bilingual lexicons: a statistical approach. Computational Linguistics 22(1), 1–38.

Voorhees EM (1986) Implementing agglomerative hierarchical clustering algorithms for use in document retrieval. Information Processing and Management 22, 465–476.

Voutilainen A (1993) NPtool: a detector of english noun phrases. In Proceedings of Workshop on Very Large Corporation.

Wei C and Lee YH (2001) Event detection for supporting environmental scanning: an information extraction-based approach. In Proceedings of 5th Pacific Asia Conference on Information Systems (PACIS).

Weiss SM, Apte C, Damerau FJ, Johnson DE, Oles FJ, Goetz T and Hampp T (1999) Maximizing text-mining performance. IEEE Intelligent Systems 14(4), 63–69.

Wiener W, Pedersen JO and Weigend AS (1995) A neural network approach to topic spotting. In Proceedings of the 4th Symposium on Document Analysis and Information Retrieval (SDAIR ’95), pp 317–332.

Yang Y (1994) Expert network: effective and efficient learning from human decisions in text categorization and retrieval. In Proceedings of the 17th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 13–22.

Yang Y and Chute CG (1994) An example-based mapping method for text categorization and retrieval. ACM Transactions on Information Systems 12(3), 252–277.

Yang Y and Liu X (1999) A re-examination of text categorization methods. In Proceedings of the 22nd International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 42–49.

## Appendix A: CE algorithm

Inputs: Existing categories EC and categorised documents, feature inclusion threshold for intra-category disjointness $( \sigma _ { d } \% )$ , feature inclusion threshold for inter-category overlapping $( \sigma _ { o } \% )$ , split threshold $( \alpha _ { s } )$ , merging threshold $( \alpha _ { m } )$ , and number of features (k) Output: Categories evolved CR and re-organised documents

## Begin

## /\* Category Decomposition Phase \*/

CR = ;

Extract features (ie nouns and noun phrases) from all documents organised in EC;

For each existing category $E _ { i }$ in EC do {

Construct a local dictionary $L D _ { i }$ with k features for $E _ { i }$ using the correlation coefficient or $\mathrm { T F } \times \mathrm { I D F }$ feature selection method;

Represent each document in $E _ { i }$ with $L D _ { i }$ using the binary representation scheme;

If disjointness(E<sub>i</sub>, $\sigma _ { d } \% ) > \alpha _ { s }$ then

{ Split (by applying PAM) the documents of $E _ { i }$ into m clusters (ie into $E _ { i 1 } , E _ { i 2 } , . . . , E _ { i m }$ subcategories) where m results in the silhouette coefficient;

For each document d in $E _ { i }$ do {Assign d to the closest subcategory $E _ { i j } { \mathrm { ; } } { \mathrm { } } { \mathrm { } } { \mathrm { } } { \mathrm { } } { \mathrm { } } { \mathrm { } } { \mathrm { } }$

$C R = C R \cup \{ E _ { i 1 } , E _ { i 2 } , . . . , E _ { i m } \}$ ; /\* decomposing $E _ { i }$ into $E _ { i 1 } , E _ { i 2 } , . . . ,$ and $E _ { i m } ~ ^ { * / } \}$

Else $C R = C R \cup \{ E _ { i } \} ; \ d { \ne } E _ { i }$ is not decomposed \*/ }

/\* Category Amalgamation Phase \*/

For each category $R _ { i }$ in CR do {

Re-construct a local dictionary $L D _ { i }$ for $R _ { i }$ using the same feature selection method employed in the category decomposition phase;

Re-represent the documents in $R _ { i }$ with $L D _ { i }$ using the binary representation scheme; }

Include every category $R _ { i }$ in CR into MGraph;

For every pair of categories $R _ { i }$ and $R _ { j }$ in CR do { If overlapping $( R _ { i } , R _ { j } , \sigma _ { o } \% ) > \alpha _ { m }$ Then

Update MGraph by adding an edge between $R _ { i }$

## About the authors

Chih-Ping Wei received a BS in Management Science from the National Chiao-Tung University in Taiwan, ROC in 1987 and an MS and a PhD in Management Information Systems from the University of Arizona in 1991 and 1996. He is currently an associate professor of Department of Information Management at National Sun Yat-Sen University in Taiwan, ROC and was a visiting scholar at the University of Illinois at Urbana-Champaign in 2001. His papers have appeared (including forthcoming) in IEEE Transactions on Engineering Management, IEEE Software, IEEE Intelligent Systems, IEEE Transactions on Information Technology in Biomedicine, Decision Support Systems, Expert Systems with Applications, and Journal of Organizational Computing and Electronic and $R _ { j }$ where the edge is labeled with overlapping $( R _ { i } , R _ { j } , \sigma _ { o } \% ) ;$ }

Repeat

Remove from MGraph all sub-graphs of size equal to 1;

For each remaining sub-graph SG in MGraph do $/ { * }$ the size of SG is greater than $1 ~ ^ { * } / ~ \left\{ \begin{array} { r l } \end{array} \right.$ {

If SG is not a complete graph Then Remove the edge with the lowest overlapping measure from SG;

Else

{ Merge all categories $\{ M _ { 1 } , M _ { 2 } , . . . , M _ { l } \}$ appear in SG into a new category $M ;$

MGraph = MGraph − SG;

$$
C R = (C R - \{M _ {1}, M _ {2}, \dots , M _ {l} \}) \cup \{M \}; \}
$$

Until MGraph is an empty set;

Return CR;

End;

## Appendix B: Sample news document

Category: Interest

Subject: BANK OF JAPAN TO SELL 1200 BILLION YEN IN BILL

Date: June 18, 1987

The Bank of Japan will tomorrow sell 1200 billion yen in bills from its holdings to help absorb a projected money market surplus of 2100 billion, money market traders said.

Of the total, 800 billion yen will yield 3.6004 pct on sales from money houses to banks and securities houses in 34-day repurchase agreements maturing on August 3. The other 200 billion yen will yield 3.6003 pct in 43- day repurchase accords maturing on August 12. The remaining 200 billion yen will yield 3.6503 pct in 50- day repurchase agreements maturing on August 19. The repurchase agreement yields compare with the 3.5625 pct 1-month commercial bill discount rate today and 3.6250 pct on 2-month bills. They attributed the projected surplus mainly to 1900 billion yen of government tax allocations to local governments and public bodies.

Commerce, etc. His current research interests include knowledge discovery and data mining, information retrieval and text mining, knowledge management, multidatabase management and integration, and data warehouse design. He is a member of the ACM and IEEE. Contact him at the Department of Information Management, National Sun Yat-Sen University, Kaohsiung, Taiwan, ROC; cwei@mis.nsysu.edu.tw.

Paul J Hu is an assistant professor of Information Systems in David Eccles School of Business at the University of Utah. He received his PhD in Management Information Systems from the University of Arizona. He has papers published (including forthcoming) in Journal of Management Information Systems,

Decision Sciences, Decision Support Systems, IEEE Transactions on Engineering Management, IEEE Transactions on Information Technology in Biomedicine, IEEE Intelligent Systems, IEEE Software, Journal of Organizational Computing and Electronic Commerce, Topics in Health Information Management, and Journal of Telemedicine and Telecare. His current research interests include information technology management and applications in health care, electronic commerce, human-computer interaction, and software project management.

Yuan-Xin Dong received a BS in Transportation Communication Management from the National Cheng-Kung University in Taiwan, ROC in 1998 and an MS in Information Management from the National Sun Yat-Sen University in Taiwan, ROC in 2000. He is currently an MIS manager at China Telecommunications Company in Taiwan, ROC. His research interests include data mining and text mining.
