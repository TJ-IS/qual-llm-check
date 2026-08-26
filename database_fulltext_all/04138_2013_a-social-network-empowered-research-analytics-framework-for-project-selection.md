---
otero_id: 4138
otero_key: "6CXZKUAU"
title: "A social network-empowered research analytics framework for project selection"
authors: "Thushari Silva; Zhiling Guo; Jian Ma; Hongbing Jiang; Huaping Chen"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.01.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A social network-empowered research analytics framework for project selection

Thushari Silva <sup>a</sup>, Zhiling Guo <sup>a,</sup>⁎, Jian Ma <sup>a</sup>, Hongbing Jiang <sup>a,b</sup>, Huaping Chen <sup>b</sup>

<sup>a</sup> Department of Information Systems, City University of Hong Kong, Hong Kong

<sup>b</sup> School of Management, University of Science and Technology of China and USTC-CityU Joint Advanced Research Centre, Suzhou, PR China

## a r t i c l e i n f o

Available online 9 January 2013

Keywords: Research project selection Research social networks Research analytics

## a b s t r a c t

Traditional approaches for research project selection by government funding agencies mainly focus on the matching of research relevance by keywords or disciplines. Other research relevant information such as social connections (e.g., collaboration and co-authorship) and productivity (e.g., quality, quantity, and citations of published journal articles) of researchers is largely ignored. To overcome these limitations, this paper proposes a social network-empowered research analytics framework (RAF) for research project selections. Scholarmate.com, a professional research social network with easy access to research relevant information, serves as a platform to build researcher pro<sup>fi</sup>les from three dimensions, i.e., relevance, productivity and connectivity. Building upon pro<sup>fi</sup>les of both proposals and researchers, we develop a unique matching algorithm to assist decision makers (e.g. panel chairs or division managers) in optimizing the assignment of reviewers to research project proposals. The proposed framework is implemented and tested by the largest government funding agency in China to aid the grant proposal evaluation process. The new system generated signi<sup>fi</sup>cant economic bene<sup>fi</sup>ts including great cost savings and quality improvement in the proposal evaluation process. © 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

There is a steadily growing trend for government funding agencies to support an increasing number of research proposals. For example, there were 42,225 research grant proposals submitted to the National Science Foundation (NSF) in the U.S. in 2010. The estimated number of submission for 2012 will increase to 46,000. The number of proposals submitted to the National Natural Science Foundation of China (NSFC) has increased from 23,636 in 2001 to over 147,000 in 2011. The sheer volume of submission has posed a signi<sup>fi</sup>cant challenge for research project selection due to dif<sup>fi</sup>culties of assigning the most suitable reviewers to the most relevant project proposals.

A research project can be characterized by a set of qualitative and quantitative, tangible and intangible attributes. Management scientists, Economist and IS practitioners have proposed various decision models, methodologies and decision support systems to assist decision making tasks related to research project selection [13,15,34,35]. Traditional approaches based on mathematical programming and optimization are useful for handling large volume of submissions, but are less ef<sup>fi</sup>- cient in dealing with subjective judgment and information. Machine learning techniques incorporating fuzzy logic, genetic algorithms and arti<sup>fi</sup>cial intelligence techniques are capable of learning complex patterns in data, but are limited by their ability to generalize from training data and optimize decisions over the entire decision space. Other traditional approaches involve manually assigning proposals to reviewers based on their claimed expertise, which is neither ef<sup>fi</sup>cient nor practical to support increasing complexity of decision making faced by funding agencies.

Current computer-based methods mainly consider matching research relevance in terms of keywords or disciplines, while ignoring the social connections (e.g., collaboration and co-authorship) and productivity (e.g., quality, quantity, and citations of published journal articles) of researchers. It is desirable to incorporate all these aspects into a uni<sup>fi</sup>ed evaluation framework. To achieve this goal, we propose a research analytics framework that is empowered by a research social network (www.scholarmate.com) for effective research project selection. Better identi<sup>fi</sup>cation of social connection can effectively cluster researchers based on topics of interests, methodologies, and research disciplines. Being able to identify community structure in the social network helps us understand and exploit the research network more effectively. On the one hand, such information can be used to identify most suitable reviewers. On the other hand, it can help avoid con<sup>fl</sup>ict of interests to ensure fair evaluation.

Speci<sup>fi</sup>cally, we propose to de<sup>fi</sup>ne pro<sup>fi</sup>les of research entities (e.g. project proposals, researchers) from three dimensions, i.e. relevance (e.g., keywords and research disciplines), productivity (e.g., quality, quantity, and citations of published journal articles), and connectivity (e.g., project collaborators, co-authors and colleagues). Represented by visual research CVs, pro<sup>fi</sup>les of proposals and potential reviewers are built by extracting information from multiple sources including submitted proposals, bibliographic databases (e.g., ISI, Scopus, and

EI), and research social network (i.e. www.Scholarmate.com). By aggregating information in the three dimensions, we construct a unique matching algorithm to assist decision makers (e.g. panel chairs or division managers) in optimizing the assignment of reviewers to research project proposals.

To demonstrate the usability of the proposed framework, we implemented the system to aid China's largest government funding agency in its grant proposal evaluation. The research analytics framework builds upon scientometrics, business intelligence and social network analysis techniques. Its powerful search and data access capabilities provide timely and relevant information in visualized forms for research project evaluation. The implemented system generates significant economic bene<sup>fi</sup>ts including cost savings and quality improvement in the proposal evaluation process.

This paper is organized as follows. Section 2 reviews the relevant literature. Section 3 provides an overview of the research analytics framework and the Scholarmate research social network. Section 4 presents the detailed methods for pro<sup>fi</sup>ling and algorithms to calculate the key performance indicators. An optimization problem for reviewer assignment is proposed in Section 5. Section 6 reports evaluation of the proposed system by China's largest government funding agency for its grant proposal evaluation. Section 7 concludes with a summary of contribution and directions for future research.

## 2. Literature review

The major challenge in reviewer assignment for proposal evaluation is identifying and recommending the most suitable reviewers who have a high level of expertise and will make valuable professional judgment on given proposals [13,38]. In this paper, we propose a pro<sup>fi</sup>le-based approach to assign reviewers for proposal evaluation.

Previous research has identi<sup>fi</sup>ed two approaches to scienti<sup>fi</sup>c researcher pro<sup>fi</sup>ling. One approach relies on subjective self-claimed information declared by researchers themselves. The other approach is based on objective measurement obtained through automated inferences about the researcher's behavior patterns related to publications and citations derived from relevant resources [37]. The <sup>fi</sup>rst approach uses qualitative methods (e.g. surveys, questionnaires, or interviews) and traditional information retrieval models (e.g., term-based modeling [3] and rough-set modeling [19]) to gain knowledge of a researcher's interests and resulted pro<sup>fi</sup>les. The latter approach utilizes various feature selection techniques in machine learning to learn user pro<sup>fi</sup>le [10].

The machine learning approaches tend to learn the mapping between incoming set of documents relevant to user input and real numbers which represent the strength of user preferences. The features of the documents are <sup>fi</sup>rst extracted by widely used techniques including information gain [8,21] and correlation coef<sup>fi</sup>cient [32]. Then the key features are used as attributes in the mapping functions. Some studies focus on techniques such as neural networks [22], Support Vector Machine (SVM) [11,16,29], K-Nearest Neighbors (K-NN) and logistic regression [6,40] before generating a mapping with a set of real numbers. Li et al. [20] proposed a rough threshold model (RTM) to analyze and extract keywords from the scienti<sup>fi</sup>c publications. In our approach we augment the original rough threshold model with phrase analysis algorithm to resolve semantic ambiguity that is not handled by the original rough threshold model for topic generation.

Collaboration network is one type of popular social networks that has been widely studied in the literature [4,5,23]. A property that many social networks have in common is clustering, or network transitivity [2,26,39]. Clustering coef<sup>fi</sup>cient is de<sup>fi</sup>ned as the probability that two of one's friends are friends themselves [7,39]. It typically ranges from 0.1 to 0.5 in many real-world networks. A related concept is community in which connection within the same community is dense and outside the community is sparse. Community structure in a social network represents real social groupings by interest or background [27].

For example, communities in a citation network represent related papers on a single topic [31].

There are two broad classes of hierarchical clustering methods to detect the community structure in a social network: agglomerative and divisive [28,30]. The agglomerative approach focuses on <sup>fi</sup>nding the strongly connected cores of communities by adding links [24], and the divisive approach uses information about edge betweenness to detect community boundaries by removing links [23]. For example, the Girvan–Newman algorithm [12] is one of the most widely used divisive methods and is effective at discovering the latent groups or communities that are de<sup>fi</sup>ned by the link structure of a graph. Newman's fast algorithm [25] is an ef<sup>fi</sup>cient reference algorithm for clustering in large networks. It falls in the general category of agglomerative hierarchical clustering methods. This method can be easily generalized to weighted networks in which each edge has a numeric value indicating link strength. It has been successfully applied to a collaboration network of more than 50,000 physicists. In this study, we adopt Newman's fast algorithm in our research social network analysis.

## 3. An overview of the RAF and Scholarmate

Research Analytics is the application of methods and theories in scientometrics, business intelligence and social network analysis to transform research related data into relevant information in research management. In this paper we demonstrate the research analytics framework in the context of reviewer recommendation for research project selection.

## 3.1. The RAF for reviewer recommendation

This study takes a pro<sup>fi</sup>le-based approach to reviewer recommendation. Fig. 1 illustrates the key framework.

Research Online (http://rol.scholarmate.com) is an institutional repository service provided by Scholarmate (http://www.scholarmate. com) to analyze proposals submitted through the Internet-based Science Information System (ISIS, https://isis.nsfc.gov.cn). It helps build standardized visual research CVs of researchers and identify the social groups to which they belong. These steps greatly ease the pro<sup>fi</sup>ling of proposals and researchers. Key features and attributes such as discipline codes and keywords to represent proposals and researchers are derived from the standard keyword dictionary. Phrase patterns are discovered by data mining the free text categories of the electronic documents from various databases (e.g. ISI, Scopus and EI). Based on the constructed comprehensive pro<sup>fi</sup>les of both the proposals and potential reviewers, the system generates key performance indicators in three dimensions, i.e., relevance, productivity and connectivity. Finally, a matching algorithm that takes into account all three dimensional measures is proposed for reviewer recommendation.

Speci<sup>fi</sup>cally, relevance refers to the keywords, research discipline and expertise area that are derived from both the researcher's scienti<sup>fi</sup>c publications and prior funded projects. Productivity is measured by quality, quantity, citations, and impacts of one's research, as well as other academic achievements. Connectivity among researchers is inferred through collaborations, such as collaborators in projects, co-authorship in publications, and colleagues in the same organizations. Their speci<sup>fi</sup>c roles in the reviewer assignment process can be demonstrated in Fig. 2. We will discuss each of them in detail in Section 4.

## 3.2. Scholarmate research social network

Scholarmate (http://www.scholarmate.com) is a professional research social network that connects people to research with the aim of “innovating smarter”. It offers research social network services that help researchers <sup>fi</sup>nd suitable funding opportunities and potential research collaborators, In addition to its important function of connecting people with similar interests, Scholarmate has a search tool to help researchers extract their publications from existing bibliographic databases (e.g., ISI, Scopus) directly, along with citations of the paper and impact factor of the journal. Moreover, Scholarmate provides researchers with the ability to disseminate research outcomes and information about their current interests over established social connections. On the one hand, researchers can use Scholarmate to manage their research outcomes and research in progress, including research proposal preparation. On the other hand, transparency in information sharing among scholars in Scholarmate will open an opportunity for researchers to timely participate in relevant scholarly activities, such as becoming potential reviewers. For example, a panel chair will be able to judge the recent research expertise of a researcher after analyzing the knowledge sharing activities in Scholarmate.

![](/api/attachments/6CXZKUAU/fulltext/images/b8c49032804523413fb758c17d8c4475a8986b46baca437e0cbb57faafffebbf.jpg)  
Fig. 1. The framework of pro<sup>fi</sup>le-based reviewer recommendation.

In Scholarmate, several types of networks can be constructed, such as citation networks, project collaboration and journal article co-authorship networks. An example of the collaboration network is presented in Fig. 3. The numbers beside the nodes are researcher identi<sup>fi</sup>cation numbers (RIDs). The numbers on the edges are the collaboration frequencies of two researchers. The frequency of collaboration is measured in terms of the number of co-authored publications, number of collaborated projects and number of co-cited papers extracted through the Scholarmate platform. Three major communities are identi<sup>fi</sup>ed and are indicated by the ovals in the <sup>fi</sup>gure. The communities are derived according to research expertise. We are also able to identify top researchers in the social network in terms of connectivity by degree, betweenness, and closeness, as shown in Table 1. The numbers in brackets denote the rankings under the corresponding measures. The researchers who have high ranks in the same community as principle investigators are identi<sup>fi</sup>ed as the potential reviewers subject to the condition that there's no direct connection between the potential reviewers and the principle investigators. For example, researcher 51 is a principle investigator and researcher 55 is identi<sup>fi</sup>ed as a potential reviewer because these two researchers are in the same community but they have no direct collaboration. The fact that both of them have collaborations with researchers 37 and 38 indicates potential overlap of research interests in some common research areas.

The research social network can enhance data representation in several ways. For example, existing databases only store data about published articles. Working papers that re<sup>fl</sup>ect the most recent research activities cannot be obtained by a search in bibliographic databases, but may be available on the social network site. Similarly, a researcher who has secured an industry grant that is relevant to the required reviewer expertise may be suitable to serve as a potential reviewer. However, traditional method cannot identify this researcher due to inability to access such information. Social network facilitates real-time information sharing and therefore is effective for such type of information acquisition. Such additional information greatly enhances the completeness and timeliness of our data representation.

## 4. Pro<sup>fi</sup>ling and key indices

In this section, we present a comprehensive representation of the proposal and researcher pro<sup>fi</sup>les from both available databases and the research social network, based on which three key performance indicators are derived: relevance, productivity, and connectivity. Fig. 4 shows relationship between three key performance indicators and their usage in reviewer recommendation.

![](/api/attachments/6CXZKUAU/fulltext/images/b0aba6e3d38bed2b49b20a426e57a9097bc258aaddf37698e175a7d1790c1243.jpg)  
Fig. 2. Stage diagram for proposal-reviewer recommendation.

![](/api/attachments/6CXZKUAU/fulltext/images/7c95cda3998a8a55e11b59f21b7aa38ed493ebaeb1c2dc148185ee42e9e7a26f.jpg)  
Fig. 3. An example of collaborated network.

Initially the system constructs pro<sup>fi</sup>les of proposals (indexed by i) and researchers (indexed by j), respectively. The proposal pro<sup>fi</sup>ling and reviewer pro<sup>fi</sup>ling are discussed in detail in Section 4.1. The three key indices are developed as follows. We <sup>fi</sup>rst use a component-based matching algorithm to calculate the relevance index (r ), which denotes the degree of matching between the proposal pro<sup>fi</sup>le and the reviewer pro<sup>fi</sup>le. Based on the Scholarmate platform services, we construct the connectivity index (c ) via the collaboration network indicating frequency of research collaboration among reviewers, PIs and co-PIs. The generated collaboration network is analyzed by identifying communities and their features such as structure and closeness, and those features are used in the generation of connectivity index. The connectivity index is used to resolve the con<sup>fl</sup>ict of interest and to identify the most relevant reviewers. Finally, we generate potential reviewers' productivity index (e ), which considers quality of the publications, research impact and academic achievement. The productivity index is used to balance the expertise of potential set of reviewers in the optimization program of reviewer recommendation.

## 4.1. Profiling

In general, pro<sup>fi</sup>ling is the process of determining key attributes that can be used to characterize a given object. In our project selection context we focus on proposal pro<sup>fi</sup>ling and researcher pro<sup>fi</sup>ling. The objective of proposal pro<sup>fi</sup>ling is to extract proposal relevant features and that of researcher pro<sup>fi</sup>ling is to extract researcher expertise. The quality of pro<sup>fi</sup>ling directly affects the effectiveness of research project selection. The integration of both subjective and objective information is necessary during the process of pro<sup>fi</sup>le generation.

Table 1  
Researchers' Connectivity Ranking.

<table><tr><td>RID</td><td>Degree</td><td>n-Degree</td><td>Betweenness</td><td>Closeness</td><td>Overall</td></tr><tr><td>37</td><td>11 (1)</td><td>0.1930</td><td>0.0345 (4)</td><td>0.2069 (1)</td><td>0.1685 (1)</td></tr><tr><td>18</td><td>9 (2)</td><td>0.1579</td><td>0.0459 (1)</td><td>0.1787 (3)</td><td>0.1459 (2)</td></tr><tr><td>27</td><td>6 (2)</td><td>0.1053</td><td>0.0382 (3)</td><td>0.1474 (7)</td><td>0.1129 (5)</td></tr><tr><td>10</td><td>6 (4)</td><td>0.1053</td><td>0.0453 (2)</td><td>0.1843 (2)</td><td>0.1328 (3)</td></tr><tr><td>15</td><td>5 (4)</td><td>0.0877</td><td>0.0143 (9)</td><td>0.1685 (4)</td><td>0.1134 (4)</td></tr><tr><td>31</td><td>5 (6)</td><td>0.0877</td><td>0.0244 (5)</td><td>-</td><td>-</td></tr><tr><td>19</td><td>5 (6)</td><td>0.0877</td><td>0.0169 (7)</td><td>-</td><td>-</td></tr><tr><td>38</td><td>5 (6)</td><td>0.0877</td><td>-</td><td>0.1345 (8)</td><td>-</td></tr><tr><td>52</td><td>4 (8)</td><td>0.0702</td><td>0.0122 (10)</td><td>0.1638 (5)</td><td>0.1054 (6)</td></tr><tr><td>43</td><td>4 (8)</td><td>0.0702</td><td>0.0163 (8)</td><td>-</td><td>-</td></tr><tr><td>34</td><td>-</td><td>-</td><td>0.0207 (6)</td><td>-</td><td>-</td></tr><tr><td>36</td><td>-</td><td>-</td><td>-</td><td>0.1340 (9)</td><td>-</td></tr><tr><td>44</td><td>-</td><td>-</td><td>-</td><td>0.1512 (6)</td><td>-</td></tr></table>

We <sup>fi</sup>rst focus on proposal pro<sup>fi</sup>ling. The proposal submitted through the Internet-based Science Information System (ISIS) has standard template to be <sup>fi</sup>lled in up to two discipline codes and <sup>fi</sup>ve keywords. We express the self-claimed discipline code (Discode) and keywords (Key) in the following sequence:

$$
<   \text { PropNo }, \text { DisCode1 }, \text { DisCode2 }, \text { Key1 }, \text { Key2 }, \dots , \text { Key5 } >\tag{1}
$$

where PropNo is the proposal number that uniquely identi<sup>fi</sup>es a proposal. This sequence can be directly extracted from the proposal.

To verify whether the claimed information is accurate, an objective examination of the proposal title and abstract is necessary. The second type of information is obtained through data mining the title and abstract sections of the proposal. It can be expressed in the following sequence:

$$
<   \text { PropNo }, \text { key1 }, \text { key2 },..., \text { keym } >.\tag{2}
$$

Note here that we use lower case key to represent keywords extracted from the non-standard content area (i.e., title and abstract). This set of keywords has some overlaps with, but is generally larger than, the standard keyword database de<sup>fi</sup>ned by the government funding agency. For the fair comparison of any two proposal documents, we extract m keywords in each document. The search algorithm that we will discuss later determines the preferred number of keywords. Ideally we can add the whole content of the proposal to obtain the highest ranked keywords through word frequency analysis. We found that this would increase the computational effort without adding too much new insight. Mining the title and the abstract is accurate enough to classify proposals according to the keywords.

We next consider researcher pro<sup>fi</sup>ling. The funding agency maintains an expert dictionary for the pool of potential reviewers. The expert dictionary is standardized and the available choices are the same as those in the proposal application. Initially each potential reviewer chooses his/her own disciplines and expertise areas (expressed as keywords). The self-claimed discipline code (Discode) and keywords (Key) are expressed in the following sequence:

![](/api/attachments/6CXZKUAU/fulltext/images/6dddd8f3cb114a474f2b70eb19b468546e0d390d5501cc2257758c884b455898.jpg)  
Fig. 4. Process model and relationship with key indices in reviewer recommendation.

$$
<   \text { ResearcherID }, \text { DisCode1 }, \text { DisCode2 }, \text { Key1 }, \text { Key2 },..., \text { Key5 } >\tag{3}
$$

where ResearcherID is used to uniquely identify a potential reviewer.

Each potential reviewer may have successful grants from different funding agencies and have publications, patents, or awards from various sources. We extract such objective information from several databases and list them as:

$$
<   \text { ResearcherID }, \text { GrantNo }, \text { DisCode1 }, \text { DisCode2 }, \text { Key1 }, \text { Key2 },..., \text { Key5 } >\tag{4}
$$

$$
<   \text { ResearcherID }, \text { PubNo }, \text { key1 }, \text { key2 },..., \text { keym } >.\tag{5}
$$

In addition, the potential reviewers may have social tags. Social tags are labels about expertise areas that are maintained by friends or other concerned parties who may know reviewers well in other capacities. For example, a panel chair may know research expertise of the reviewer from his/her previous service to the funding agency. Information extracted from reviewers' social tags can be aggregated and expressed as:

## 4.2. Extracting topic features from texts

During the process of objective information extraction, it is necessary to analyze non-free text areas such as titles and abstracts of electronic documents. The determination of a set of topic features from non-text <sup>fi</sup>elds follows several steps including extracting phrases, <sup>fi</sup>ltering out non-key phrases, resolve semantic heterogeneity and constructing keyword dictionary. In this study we combine several techniques including Rough Threshold Model and Database Tomography and develop an algorithm to calculate document phrase weight distribution.

When extracting information from texts such as titles and abstracts in funded projects and publications, we <sup>fi</sup>rst need to build a standard research keyword dictionary. Phrases (a combination of multiple words) rather than single word are used to solve semantic ambiguity as single words are rarely suf<sup>fi</sup>cient to accurately distinguish standing researcher interests [32]. Generally phrases carry more meaning than single words. We <sup>fi</sup>nd a phrase with length of 2–4 keywords strong enough to capture the meaning effectively.

The free-text category <sup>fi</sup>elds of scienti<sup>fi</sup>c publications (e.g. title, abstract and keywords) are analyzed and technical phrases were extracted using the Database Tomography (DT) process [17,18]. DT is a textual database analysis system that provides algorithms for extracting multi-word phrase frequencies with their proximities. We applied DT algorithm to extract all adjacent double, adjacent triple and adjacent quadruple word phrases from the text (i.e. title, abstract and keywords) along with their frequencies. We discarded those phrases with extremely high frequencies (not useful to distinguish documents) and those with extremely low frequencies (not useful to compare documents). Finally these phrases are built into the keyword dictionary.

According to Rough Threshold Model (RTM) [20], documents are represented in terms of weight distribution over topic features. We use an augmented RTM topic <sup>fi</sup>ltering algorithm to generate topic features from the documents. Speci<sup>fi</sup>cally, let $P { = } \{ p _ { 1 } , \dots p _ { m } \}$ be the initial set of phrases extracted from all documents $D = \{ d _ { 1 } , d _ { 2 } , . . . , d _ { n } \} .$ Let $f _ { i j }$ be the number of appearances of phrase j in document $d _ { i \cdot }$ A document $d _ { i }$ can be expressed by a set of phrases with corresponding occurring frequencies: $d _ { i } { = } \{ ( p _ { 1 } f _ { i 1 } ) , \ { \ldots } \ ( p _ { n } f _ { i m } ) \}$

The initial phrase set of d i $r p _ { i } { = } \{ p _ { j } | f _ { i j } { > } 0 \}$ . If two documents have the same phrase patterns, the two initial phrase patterns can be composed. For example, $\{ ( p _ { 1 } , 1 ) , ( p _ { 2 } , 3 ) \} \oplus \{ ( p _ { 1 } , 2 ) , ( p _ { 2 } , 2 ) \} = \{ ( p _ { 1 } , 3 ) , ( p _ { 2 } , 5 ) \}$ where ⊕ denotes the composition operation. We can group the initial phrase patterns that have the same phrase sets into clusters and use their composed phrase pattern to represent the cluster. Assume that there are rbn clusters. The cluster can be represented by $c r p _ { r } { = } \{ ( p _ { 1 }$ $c f _ { r 1 } ) , ( p _ { 2 } , \ c f _ { r 2 } ) , \ . . . , ( p _ { m } , \ c f _ { r m } ) \}$ , where the cluster frequency $c f _ { r k } =$ $\sum _ { i = 1 } ^ { | c r p _ { r } | } f _ { i k }$ , for $k = 1 , 2 , \dots m ,$ is the composed frequency in the cluster. <sup>¼</sup>We de<sup>fi</sup>ne the support for phrase pattern $r p _ { i } \in c r p _ { i }$ as follows.

$$
\operatorname{support} \left(c r p _ {r}\right) = \frac {\left| c r p _ {r} \right|}{\left| D \right|}\tag{7}
$$

Furthermore, $\textstyle \sum _ { r } s \mathbf { u p p o r t } ( c r p _ { r } ) = 1$

<sup>ð Þ ¼</sup>The normal form of the cluster phrase pattern can be described by the following association mapping function: $\beta ( c r p _ { r } ) = \{ ( p _ { 1 } , w _ { r 1 } ) , ( p _ { 2 } ,$ $w _ { r 2 } ) , . . . , ( p _ { m } , w _ { r m } ) \}$ , where phrase normalized frequency is de<sup>fi</sup>ned as:

$$
w _ {r k} = \frac {c f _ {r k}}{\sum_ {i = 1} ^ {m} c f _ {r i}}, k = 1, 2,..., m.\tag{8}
$$

The relative importance weight of phrase $p _ { k }$ in document i over all documents can be de<sup>fi</sup>ned as:

$$
\beta_ {i k} = \sum_ {p _ {k} \in r p _ {i} \in \beta (c r p _ {r})} \text { support } (c r p _ {r}) w _ {r k} \frac {f _ {i k}}{c f _ {r k}}.\tag{9}
$$

The document i can be alternatively represented by its phrase weighted distribution $\beta _ { i } = \{ \beta _ { i 1 } , \beta _ { i 2 } \dots \beta _ { i m } ) \}$ .

For a given document (i.e. set of publications and projects), all initial phrase patterns are calculated with their pattern frequency. Generated patterns are combined to construct clusters and clusters are labeled using phrases in combined patterns. Each pattern frequency in the cluster is normalized and normalized weights are calculated. Finally, a document that is uniquely represented by its initial phrase patterns can be characterized by its phrase weight distribution across all documents. The algorithm is described as follows.

## 4.3. Relevance

The relevance index is used to determine how well reviewer expertise is matched with the content of the proposal. It is calculated from matching the proposal and reviewer pro<sup>fi</sup>les. The task of pro<sup>fi</sup>le matching is to decide whether a sequence of key phrases that describe proposal pro<sup>fi</sup>le attributes matches key phrases that represent reviewer pro<sup>fi</sup>le attributes. Two widely accepted approaches for calculating similarity between terms are Euclidean distance and cosine similarity measure [14]. For the self-claimed information that is extracted in standard terms, we use the Jaccard similarity measure [1] to perform component-based matching over reviewer and proposal pro<sup>fi</sup>les. Data extracted by Eqs. (1), (3) and (4) can be matched using this method. The Jaccard index between reviewer i and proposal j is expressed as:

$$
J _ {i j} = \frac {F \left[ \left(\text { Key } _ {i 1} , \text { Key } _ {i 2} , \dots \text { Key } _ {i 5}\right) \cap \left(\text { Key } _ {j 1} , \text { Key } _ {k 2} , \dots \text { Key } _ {j 5}\right) \right]}{F \left[ \left(\text { Key } _ {i 1} , \text { Key } _ {i 2} , \dots \text { Key } _ {i 5}\right) \cup \left(\text { Key } _ {j 1} , \text { Key } _ {k 2} , \dots \text { Key } _ {j 5}\right) \right]}\tag{10}
$$

where $\mathrm { K e y } _ { i k }$ and $\mathrm { K e y } _ { i k } , k { = } 1 , 2 \ldots 5 ,$ are the <sup>fi</sup>ve keywords associated with reviewer i and proposal j in standard terms. The numerator denotes the number of keywords in common, and the denominator represents the total number of unique keywords in both pro<sup>fi</sup>les. As shown, the Jaccard similarity is measured by the ratio of the frequency of an intersection divided by the frequency of a union between two sets of keywords [1].

To determine the similarity of the non-standard phrase patterns, we adopt the cosine similarity measure. For researcher pro<sup>fi</sup>le i and proposal pro<sup>fi</sup>le j, the similarity can be calculated as follows [9].

$$
C _ {i j} = \frac {\beta_ {i} \beta_ {j}}{\| \beta_ {i} \| \| \beta_ {j} \|} = \frac {\sum_ {k = 1} ^ {m} \beta_ {i k} \beta_ {j k}}{\sqrt {\sum_ {k = 1} ^ {m} \beta_ {i k} ^ {2} \sum_ {k = 1} ^ {m} \beta_ {j k} ^ {2}}}\tag{11}
$$

where $\beta _ { i k }$ and $\beta _ { j k }$ are the normalized frequency of phrase patterns $p _ { k }$ in two pro<sup>fi</sup>les i and j. Phrase patterns extracted by Eqs. (2), (5), and (6) are processed by the algorithm presented in Table 2. The resulting weight distribution is used to derive the similarity measure.

Note that each researcher may have several grants or publications. There are different ways to de<sup>fi</sup>ne the similarity measure in the respective categories (grant or publication). The <sup>fi</sup>rst possibility is to consolidate several documents in the same category into one integrated document that represents the researcher pro<sup>fi</sup>le in that speci<sup>fi</sup>c category. Then the algorithm generates one weight distribution for the consolidated document. Within each category only one consolidated measure $C _ { i j }$ is derived. Another method is to treat the documents separately. The algorithm will result in one weight distribution for each document. Pair-wise similarity measure can be calculated between each of the researcher's documents and the proposal. We then choose the maximum similarity in a category as the <sup>fi</sup>nal measure of similarity between the proposal and the potential reviewer in that speci<sup>fi</sup>c category.

Since multiple sources of information, both subjective and objective, need to be aggregated, an appropriate weighting strategy is needed to re<sup>fl</sup>ect the relative importance in the overall evaluation [9]. Denote $r _ { i j }$ as the degree of matching between proposal i and the potential reviewer j. An aggregate measure in the relevance dimension can be obtained as follows:

$$
r _ {i j} = \alpha \text { Self } _ {i j} + \beta \text { Garnt } _ {i j} + \gamma \text { Pub } _ {i j} + \delta \text { Social } _ {i j}\tag{12}
$$

where $\alpha + \beta + \gamma + \delta = 1 .$

The four terms refer to self-claimed information, grants, publications, and social tags. Note that self-claimed information from proposal (Self) and the social tags that label the potential reviewers (Social) are related to the subjective judgment, while grants and publications provide objective measures related to the match between proposals and potential

Table 2 Algorithm to calculate document phrase weight distribution.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: A document set D and a phrase set P
Output: A document's phrase weight distribution  $\beta_{i}=(\beta_{i1},\beta_{i2},...,\beta_{im})$ 
Initialize RP =  $\Phi$ 
for each  $(d_{i}\in D)\{$ 
for  $(p_{j}\in P)$ $d_{i}=\{(p_{1},f_{i1}),...(p_{m},f_{im})\}$ $rp_{i}=\{p_{j}|f_{ij}&gt;0\}$ 
RP = RP ∪  $rp_{i}$ 
}
RP = ⊕ RP
Cluster document  $crp_{r}$  based on  $rp_{i}$ 
Calculate support  $(crp_{r})$  based on Eq. (7)
 $crp_{r}=\{(p_{1},cf_{r1}),(p_{2},w_{r2}),...,(p_{m},w_{rm})\}$  based on Eq. (8)
for each  $(d_{i}\in D)\{$ 
for  $(p_{j}\in rp_{i}\in crp_{r})$ 
calculate  $\beta_{ik}$  based on Eq. (9)}
END
</div>

<table><tr><td colspan="6">Proposal 53361479</td></tr><tr><td colspan="6">Discipline code 1: F020508 (Pattern recognition theory and application)Discipline code 2Keywords: Machine learning, Semi-supervised learning, Spectral clustering, Support vector machineAbstract: Machine learning based on data is an important direction for modern artificial intelligence. It allows computers to automatically learn characteristics of the unknown underlying probability distribution and refine learning based on empirical data from observed samples. Semi-supervised learning is a popular machine learning technique that make use of both labeled and unlabeled data in the learning process. Support vector machine is a new method for supervised learning that can be used for classification and regression analysis. Spectral methods are of fundamental importance in statistics and machine learning. This project aims to combine support vector machine and spectral clustering methods to study the semi-supervised learning problems for very large datasets.</td></tr><tr><td colspan="6">Principle Investigator XXXInstitution:XXX</td></tr><tr><td colspan="6">Relevance Score</td></tr><tr><td>Overall</td><td>Self(40%)</td><td>Grants(20%)</td><td colspan="2">Publications(20%)</td><td>Social(20%)</td></tr><tr><td>81</td><td>100</td><td>40</td><td colspan="2">85</td><td>80</td></tr><tr><td>Grant No.</td><td colspan="2">Title</td><td colspan="2">Discipline Code</td><td>Keywords</td></tr><tr><td>60775045</td><td colspan="2">Data Reduction Method for Machine Learning</td><td colspan="2">Discipline Code 1:F030504 Data mining and machine learningDiscipline Code 2:</td><td>Data reduction, Lie Group, Machine learning, Crystal classification</td></tr><tr><td>61033013</td><td colspan="2">Theories and Technologies of Image Invariant Features Based on Cognitive models</td><td colspan="2">Discipline Code 1: F0205 Computer application technologyDiscipline Code 2: F020512 Knowledge discovery and knowledge engineering</td><td>Image processing, Recognition, Machine learning, Scale space, Image invariant features</td></tr><tr><td>Grant No.</td><td colspan="2">Project Title</td><td colspan="3">Abstract</td></tr><tr><td>60775045</td><td colspan="2">Data Reduction Method for Machine Learning</td><td colspan="3">Data reduction is one of the main topics of machine learning. High dimension and nonlinearity are two key problems ... More</td></tr><tr><td>61033013</td><td colspan="2">Theories and Technologies of Image Invariant Features Based on Cognitive Models</td><td colspan="3">This interdisciplinary research aimsto integrate human knowledge, image processing, computer pattern recognition, and machine learning to extract image invariant features ... More</td></tr></table>

Fig. 5. Matching between proposal and reviewer to calculate the relevance score.

reviewers. Decision makers may assign different weights to aggregate both subjective and objective information.

As shown in Fig. 5, the proposal related information including discipline codes, keywords, abstracts and PI is displayed on the top of the screen. The relevance score is calculated and displayed in the middle. Clicking on each tab will show the matches that are identi<sup>fi</sup>ed by the system.

Ef<sup>fi</sup>ciency of the matching algorithm can be calculated in terms of time complexity. The algorithm requires a single traverse through all the set of reviewer pro<sup>fi</sup>les for each proposal. The matching between pre-generated subjective, objective and social information patterns in proposal and reviewer pro<sup>fi</sup>les requires O(n∗m) in its worst-case, where n is the number of proposals and m is the number of reviewers. The proposals are clustered according to their disciplines and a set of proposals is matched against all the reviewers. In order to reduce the computational complexity of the algorithm, pro<sup>fi</sup>les of reviewers and proposals are constructed beforehand.

## 4.4. Connectivity

The nature of connection between reviewers, PIs and co-PIs is very important when assigning reviewers to evaluate proposals. Bearing same expertise as principle investigators and having no direct personal con<sup>fl</sup>ict with PIs are essential constraints that should be satis<sup>fi</sup>ed by the reviewers. Thus in this study we utilize social network analysis related concepts such as community structure, closeness of individuals in the same community to discover non-trivial relationships among researches. After analyzing individuals in one community we are able to identify group of individuals who have similar research interests, who are active in the corresponding research area, and who have close connection with PIs or co-PIs. Such information is then used to remove con<sup>fl</sup>ict of interest and to aid preferential assignment to the most relevant reviewers.

Several types of networks can be constructed using the available social network data in Scholarmate. For example, we can represent scienti<sup>fi</sup>c papers as vertices in a graph. Vertices are connected by the edges when one paper cites the other one, which cites others as well. Alternatively, we can construct the researcher network. Each researcher is represented as a vertex in a graph. An edge is built when one researcher cites another's work (directed citation network), or when one researcher co-authored with another researcher (undirected collaboration network). We de<sup>fi</sup>ne the edge weight as the number of citations or collaborations between two researchers. Higher weight implies more connectivity between the two researchers.

We use graph clustering method to cluster graphs. Hierarchical clustering is a traditional method for detecting community structure. Here we focus on the collaboration network. We <sup>fi</sup>rst assign a weight u for a pair of vertices in the network, which is de<sup>fi</sup>ned as frequency of collaboration between two researchers and therefore represents how closely the researchers are connected. By analyzing the implicit community structure and estimating the strength of ties between individuals, we are able to discover nontrivial patterns of interactions in the scienti<sup>fi</sup>c collaboration networks.

Assume that there are s prede<sup>fi</sup>ned communities. De<sup>fi</sup>ne u as the fraction of collaboration frequency among researchers in community I to those in community J. Denote $\begin{array} { r } { a _ { I } = \sum _ { J } u _ { I J } , } \end{array}$ which represents the weighted fraction of edges that connect to vertices in community $I \ { \mathrm { ( i . e . } }$ ., the fraction of collaborations that researchers in community I collaborate with researchers in other communities). The Newman's fast algorithm is based on the idea of modularity [25]. Following their approach, we de<sup>fi</sup>ne the modularity measure for a network with s communities as:

$$
Q _ {s} = \sum_ {I = 1} ^ {s} \left(u _ {I I} - a _ {I} ^ {2}\right)\tag{13}
$$

where $u _ { I I }$ is the weighted fraction of edges in the network that connect vertices in the same community. A high value of $Q _ { s }$ represents a good community division. However, optimizing $Q _ { s }$ over all possible divisions is infeasible in practice for networks larger than thirty vertices. Various approximation methods are available, such as simulated annealing, genetic algorithms, and so on. A standard “greedy” optimization algorithm is used. The algorithm to determine the optimal community structure takes the following steps (Table 3).

The algorithm starts with n communities, where n is the total number of nodes in the collaboration network. Assuming that each vertex is the sole member of a distinctive community, and the algorithm iteratively merges each pair of communities in which there are edges connecting them. The time taken to join any pair of communities will at most be m, where m is the total number of edges in the graph. The change of $Q _ { s }$ can be calculated in constant time in each iteration. Following the join some elements in the matrix W should be updated by adding together the rows and columns corresponding to the joined communities. At each step the algorithm takes worst-case time O(n+m). When the algorithm completes its execution minimum n− 1 joins are required. Then the time complexity of the algorithm is $0 ( ( n + m ) n ) \operatorname { o r } 0 ( n ^ { 2 } )$

Since the value of $Q _ { | W | }$ is calculated in each iteration, <sup>fi</sup>nding the optimal community structure is straightforward. The hierarchical clustering method also enables us to de<sup>fi</sup>ne the community structure according to our required granularity level. To <sup>fi</sup>nd the connectivity, we extract all principle investigators and other members of proposal i. If none of them is in the same community as the potential reviewer j, we deem the reviewer is not an ideal candidate to review the proposal. Therefore, we label $g _ { i j } \ll 1$ to suggest a mismatch. Otherwise, we label $g _ { i j } = 1$ , indicating a high goodness of <sup>fi</sup>t.

Resolving con<sup>fl</sup>ict of interest is an important step in the reviewer assignment process. For example, to ensure an objective review of the proposal, the government funding agency requires that applicants and reviewers should not have co-author relationship in the last <sup>fi</sup>ve years. Con<sup>fl</sup>ict of interest can be immediately identi<sup>fi</sup>ed by a direct link in our collaboration network. If any of the primary members of proposal i has con<sup>fl</sup>ict of interest with a potential reviewer $j ,$ we label $c _ { i j } = 0$ , enforcing a “No” decision in the reviewer assignment.

## Table 3

Algorithm to cluster the collaboration network into communities

Step 1. Initially there are n vertices representing researchers. u is the collaboration frequency between researchers i and j. Initially each vertex is the sole member of a distinctive community. Calculate the within and between community collaboration fraction $u _ { I I }$ and $u _ { I J } ,$ and form matrix $W = \left| \begin{array} { c c c } { { u _ { 1 1 } } } & { { \ldots } } & { { u _ { 1 n } } } \\ { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { u _ { n 1 } } } & { { \ldots } } & { { u _ { n n } } } \end{array} \right|$ . Calculate $a _ { I } .$ Step 2. Calculate $\Delta Q _ { I J } = u _ { I J } + u _ { J I } - 2 a _ { I } a _ { J }$ . Choose (I,J)=argMaxΔQ to join if $\Delta Q _ { I J } \ge 0$ or $( I _ { \cal J } ) = a r g M i n \varDelta Q _ { \cal J J } \mathrm { i f } \varDelta Q _ { \cal J J } < 0 .$ Step 3. Update the matrix elements $u _ { I J }$ by adding together the rows and columns corresponding to the joined communities. Update a . Calculate $Q _ { | W | }$ according to Eq. (13). Step 4. Repeat steps 2 and 3 to join communities in pairs until all vertices are joined. Step 5. The optimal community structure is determined ${ \tt b y s } = a r g M a x Q _ { 1 W 1 } .$

## 4.5. Productivity

Productivity index is calculated for potential reviewers and is used to indicate the contribution to the <sup>fi</sup>eld made by them. For fair and unbiased project selection, productivity needs to be balanced among the reviewers who are to be assigned to evaluate same proposals. We measure the productivity of a potential reviewer in terms of the number of publications, quality of the publications and citation impact in the past <sup>fi</sup>ve years. A productivity index can be computed with aggregation of quality and quantity of publications.

Generally academic journals are classi<sup>fi</sup>ed into different disciplines and they are assigned a rank, such as level A journals, level B journals or level C journals. As in [33] we assume that the journal rank re<sup>fl</sup>ects the quality of the articles published in that journal as it is widely used in many research performance measuring activities related to merit increases and for allocation of research funding in university settings [36]. According to [33], we adopt a weighted scheme to generate the productivity index as a measure of overall contribution of a researcher to the <sup>fi</sup>eld. Let $q _ { i j }$ be reviewer $j ^ { \prime } s$ total number of publications in rank i level's journals, where i=A, B, C. The publication score of reviewer j is expressed as:

$$
G _ {j} = w _ {A} q _ {A j} + w _ {B} q _ {B j} + w _ {C} q _ {C j}\tag{14}
$$

where $w _ { A } > w _ { B } > w _ { C } ,$ , indicating the emphasis on quality work. There are different ways to de<sup>fi</sup>ne the weights. For example, the average impact factors for all the journals classi<sup>fi</sup>ed at the same level can be used to de<sup>fi</sup>ne the corresponding weight.

Professional titles $( \mathrm { e . g . }$ . senior scholars like Professor and Associate Professor, or junior scholars like Assistant Professor) and H-index can also be taken into consideration for recommending reviewers to proposals. We may assign higher rank score to higher professional titles. Let $R _ { j }$ and $H _ { j }$ be potential reviewer $j ^ { \prime } s$ rank score and H-index, respectively. An integrated research productivity measure can be obtained as follows:

$$
e _ {j} = u G _ {j} + v R _ {j} + t H _ {j}\tag{15}
$$

where $u + \nu + t = 1 .$

## 5. Assigning reviewers for proposal evaluation

The reviewer assignment process deals with assigning reviewers to evaluate proposals in speci<sup>fi</sup>c discipline area. Current practice is manual matching of proposals to reviewers based on their declared expertise. This is inef<sup>fi</sup>cient because subjective expertise judgment alone is insuf<sup>fi</sup>cient to decide reviewer expertise as it lacks objective evidences. We introduce the relevance measure to balance the selfclaimed expertise and the expertise induced from the derived objective information. The key objective is to maximize relevance between proposals and potential reviewers.

Because the quality of evaluation largely depends on the experiences and judgments from the reviewers, there is a need to balance reviewer expertise among the reviewers who are assigned to the same proposal. For example, senior scholars tend to give higher weight on innovativeness of the proposal than their junior counterparts, while junior scholars tend to put higher weight on methodology rigor in comparison with senior fellows. Let e be the desired average productivity level of the potential reviewers. This can be determined by relevant decision makers such as panel chairs or division managers. We want the average reviewer expertise levels to be close enough to this desired level. For example, if the potential reviewer is a junior scholar whose $e _ { j }$ is signi<sup>fi</sup>cantly lower than e, then the proposal would need a senior scholar whose productivity measure is signi<sup>fi</sup>cantly higher than e to review the proposal.

First we construct a network model where each proposal and potential reviewer is represented as a node in the network. The potential reviewer node is called the supply node, and the proposal node is called the demand node. Assume that there is a set of I proposals and a set of J potential reviewers. Let $x _ { i j }$ be the integer decision variable indicating the assignment of proposal i to potential reviewer j. Therefore, $x _ { i j } = 1$ implies recommending assignment and $x _ { i j } = 0$ implies that the assignment is not recommended. We maximize the relevance subject to the <sup>fl</sup>ow constraints which re<sup>fl</sup>ect the management's requirement of the reviewer assignment. The optimization problem can be expressed as:

$$
\begin{array}{l l} \text {Max} & \sum_ {i \in I} \sum_ {j \in J} c _ {i j} g _ {i j} r _ {i j} x _ {i j} \\ \text {s.t.} & \sum_ {j \in J} x _ {i j} \geq b \quad \text {for i\in I} \\ & \sum_ {i \in I} x _ {i j} \leq d \quad \text {for j\in J}. \\ & \sum_ {j \in J} \left(e _ {j} x _ {i j} - \overline {{e}}\right) \leq \varepsilon \quad \text {for i\in I} \\ & x _ {i j} \in \{0, 1 \} \quad \text {for i\in I, j\in J} \end{array}\tag{16}
$$

The coef<sup>fi</sup>cients in the objective function ensure that we maximize the overall relevance measure in the reviewer and proposal pools. $c _ { i j }$ is the indicator variable to remove con<sup>fl</sup>ict of interest, and $g _ { i j }$ is the coef<sup>fi</sup>cient for preferential assignment of reviewers in the same scienti<sup>fi</sup>c research community.

The <sup>fi</sup>rst set of constraints ensures that each proposal has at least b reviewers. The second set of constraints guarantees that each reviewer cannot review more than d proposals. In practice, usually b=3 and d= 20. The third set of constraints is used to balance reviewer expertise. Note that, ε>0 is the tolerance level that can be chosen by the panel chair or the management team.

As to the implementation of this model, we <sup>fi</sup>rst analyze community structures to remove con<sup>fl</sup>ict of interest and to identify potential reviewers. Next, we calculate the relevance degree between the reviewers and the proposals in such a way that the PIs of the proposals belong to the same community as their potential reviewers. The calculated relevance degrees are sorted and reviewers with high relevance degree are selected to evaluate those proposals. Finally, productivity among the reviewers who are assigned to one proposal is balanced and workload is evenly distributed among reviewers.

In order to achieve a higher degree of computational performance, the collaboration networks for reviewers and PIs of the proposals under each division are constructed and the optimal numbers of communities are derived before the reviewer assignment process is carried out. First, the time complexity for traversing through the community graph for connectivity index calculation is $0 ( n _ { 0 } + m _ { 0 } )$ , where $n _ { 0 }$ is the total number of nodes in one community and $m _ { 0 }$ is the number of connections between individuals. Second, it requires O(n m ) time complexity for spanning through the whole set of reviewers and proposals when generating the relevance degree matching. Third, the time complexity for sorting the end result is $\mathrm { O } ( n _ { 1 } \mathrm { l o g } n _ { 1 } )$ , where $n _ { 1 }$ represents the number of matching results. Finally, the time complexity for balancing productivity of reviewers in the same group is O(1) and it is negligible. In summary, the worst-case computational complexity of the proposed technique is $0 ( n _ { 0 } + m _ { 0 } + n _ { 0 } m _ { 0 } + n _ { 1 } \mathrm { l o g } n _ { 1 } )$ .

## 6. Implementation and evaluation

The proposed research analytics framework is implemented to aid the largest government funding agency in China for its grant proposal evaluation. It aims at funding scienti<sup>fi</sup>c research projects that could make huge social impact. The organizational hierarchy of the funding agency consists of one general of<sup>fi</sup>ce, <sup>fi</sup>ve bureaus, and eight scienti<sup>fi</sup>c departments. These departments are responsible for funding and managing research projects. Each department is further divided into divisions which are more focused on speci<sup>fi</sup>c research areas.

There is intensive competition for getting research projects funded, with the most recent funding rate of only 21% in 2011. The government funding agency received around 147,000 and 170,000 proposals in 2011 and 2012, respectively. Proposals are widespread over many scienti<sup>fi</sup>c disciplines. These conditions make it dif<sup>fi</sup>cult for the evaluation committee to directly participate in every project evaluation. The committee groups the proposals in different areas and delegates their authority to groups of experts according to research areas. Each area may consist of multiple related disciplines. For example, Business is an area that includes Management Science, Information Systems, and other business disciplines. There is a general budget to be distributed among the areas. The distribution of fund is not uniform and represents priorities set by the evaluation committee of the funding agency. The distribution could be adjusted based on the quality and quantity of proposals submitted to each area.

Research project selection is a process that involves multiple phases illustrated in Table A in Appendix A. To facilitate the project selection, the government funding agency has established an evaluation system which includes the peer review and expert panel evaluation. Division managers assign and invite external reviewers and panel experts to evaluate the proposals. The reviewers judge the quality of the project proposal based on their expertise, professional experience and with norms and criteria set by the funding agency. As seen, reviewer assignment is the most important phase that affects the quality and ef<sup>fi</sup>ciency of the research project selection.

We provide computerized support for the second phase of research project selection. In the prototype implementation of our system, distribution of fund is out of scope of this study. Our focus is the reviewer assignment recommendation. We have tested different subsets of proposals and reviewers. The system computes the score of matching in the relevance dimension for each pair of proposal and potential reviewer. The <sup>fi</sup>nal assignment problem can be solved in reasonable amount of time. The solution is recommended to the review panels in their respective divisions. The review panels examine the recommendation and have the right to either accept or reject our recommended assignment. Additionally, we provide data visualization to help managers view the assignment progress. Fig. 6 shows an example of the visualization.

Overall, it takes a maximum of 6 hours to compute matching degrees of 34,000 proposals and 30,000 reviewers, which is the largest number of proposals received in a single department of the government funding agency. Thus if we use parallel and distributed computing for the assignment optimization in each department (there are 8 distinctive departments in total), we can <sup>fi</sup>nish the recommendation task within 6 hours. It greatly improves work ef<sup>fi</sup>ciency as manual process of assigning reviewers usually takes up to two weeks to complete.

Quality of recommendation is acknowledged by the review panels. The pro<sup>fi</sup>le-based recommendation takes into consideration the detailed information in terms of relevance, productivity and connectivity. It can avoid con<sup>fl</sup>ict of interests and provide decision makers with most relevant information that can hardly be obtained by manual processes. The largest government funding agency has agreed to adopt our recommendation system in the next round of proposal evaluation.

## 7. Conclusion

Building upon a research analytics framework, this study presents a new approach for research project selection in a research social network environment. We built pro<sup>fi</sup>les of research entities (e.g. research proposals, reviewers) from three aspects including relevance, productivity and connectivity. Information for building the pro<sup>fi</sup>les of research entities can be obtained from the research social network (Scholarmate). Degrees of matching based on the pro<sup>fi</sup>les of research entitles can be calculated by aggregating subjective, objective and social information as collected from multiple sources. We implemented the system to aid the largest funding agency in China to optimize reviewer recommendation and support reviewer assignment. The implementation results showed that the proposed method greatly improved work ef<sup>fi</sup>ciency.

T. Silva et al. / Decision Support Systems 55 (2013) 957–968  
![](/api/attachments/6CXZKUAU/fulltext/images/f86279efd98b7967fc596aee13363765fafdd24b352d1a5bf6065d8172b606bc.jpg)

![](/api/attachments/6CXZKUAU/fulltext/images/0c1728b0528b9be58c635d726cbf8f24dbba1268a734763a4dd840d3a9f3a581.jpg)  
Fig. 6. Visualization of the reviewer assignment progress.

Our approach can be easily generalized to support different types of recommendations in the research social network environment. A direct application is journal article review. Based on the analysis of article features, our system can be used to select the initial pool of reviewers, calculate the degree of match between potential reviewers and the article, remove con<sup>fl</sup>ict of interests, balance reviewer expertise and productivity, and make <sup>fi</sup>nal reviewer assignment recommendations. The process can be automated and monitored by journal editors. In comparison with the current practice that mainly relies on editors' subjective judgment facilitated by automated search tools, our system has the ability to optimize reviewer recommendation empowered by more social functionalities. Improved accuracy and work ef<sup>fi</sup>ciency can be expected.

Other potential applications include recommending funding opportunities, publication outlets for research articles, and potential research collaborators. For example, researchers can easily promote their recently published articles using the social tools in the form of likes, tweets, shares, and more. They can even track results when their articles are cited by others. Meanwhile, the system may recommend researchers who work in the same research areas to each other within and across different research communities. Based on a researcher's pro-<sup>fi</sup>le, the research social network may also recommend journals that have published relevant topics as potential journal outlet for working papers. All these functions are very useful to promote timely distribution and target dissemination of research work.

There are a number of limitations and possible future research directions. First, a research project has various attributes that can potentially in<sup>fl</sup>uence both the impact and the probability of success of the projects. We do not model the decision makers' preferences, beliefs, priorities, and their risk attitudes. Presumably the reviewer assignment decision problem can be modeled as a multi-objective decision problem.

Second, our proposed framework only focuses on the evaluation of individual projects without building a portfolio of the most promising projects among all submitted proposals. The portfolio of projects to be funded and the individual amount that will be funded to each project are out of the scope of this research. Project evaluation, like product review, is highly subjective. There is no feedback mechanism available in the current framework to assess the quality of reviews. Historical records of funded projects, including the relevant characteristics, evaluation given by the reviewers, and the research output measured by publications, could be valuable to make better evaluation of new proposals and to select unbiased reviewers. Future extension of the research framework may take into account these aspects.

Finally, the power of Scholarmate is its ability to extract and aggregate information from multiple sources. We need to continuously improve the search tool to meet the increasing search needs of users. Moreover, standardization of the keyword dictionary can greatly help the phrase pattern recognition. While we keep evaluating and updating the keyword dictionary based on feedback of algorithm performance, we are aware that social vote is another ef<sup>fi</sup>cient approach to identify relevant keywords and remove those less meaningful ones. We have implemented many social tools to aid the system improvement. The ultimate goal is to promote a healthy research environment for researchers to engage in innovative research production.

## Acknowledgment

This research is partially funded by the General Research Fund of the Hong Kong Research Grant Council (Project No: CityU 119611), the National Natural Science Foundation of China (Project Nos: 71171172 and J1124003) and the City University of Hong Kong (Project No: 6000201).

## Appendix A

Research project selection process at the government funding agency.

<table><tr><td>Phases in R &amp; D project selection</td><td>Key decisions</td></tr><tr><td>Call for proposal and proposal submission</td><td>1) Check the validity of the submitted proposal content2) Fulfillment of application requirement by the principle investigator and by the proposal</td></tr><tr><td>Identifying the most suitable external reviewers for proposal evaluation</td><td>1) Selection of potential reviewers based on claimed expertise2) Assignment of external reviewers for validated proposals based on predefined criteria3) Transferring proposals to responsible divisions</td></tr><tr><td>Peer review</td><td>1) Review the quality and content of proposals by external reviewers based on the provides guidelines2) Validate the review content3) Coordinate with external reviewers and completion of the review process as scheduled</td></tr><tr><td>Review results aggregation</td><td>1) Aggregate the review results and transform the review results into comparable measurement and rank the proposal accordingly2) Recommend proposals for panel evaluation</td></tr><tr><td>Panel evaluation</td><td>1) Refine the suggested proposal list by making decisions on marginal proposals by panel of expertise2) Suggestion on funded project list</td></tr><tr><td>Final decision making</td><td>1) Consideration of exceptional cases2) Recommend list of projects to be funded</td></tr></table>

## Table B

Table of notation.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td colspan="2">Profiling</td></tr><tr><td> $P = \{p_1, \dots p_m\}$ </td><td>Initial set of  $m$  phases</td></tr><tr><td> $D = \{d_1, d_2, \dots, d_n\}$ </td><td>Initial set of  $n$  documents</td></tr><tr><td> $r$ </td><td>Number of clusters</td></tr><tr><td> $f_{ik}$ </td><td>Occurrence frequency of phrase  $k$  in document  $d_i$ ,  $k=1, 2, \dots, m$ </td></tr><tr><td> $rp_i$ </td><td>Initial phrase set of the document  $d_i$ </td></tr><tr><td> $crp_r$ </td><td>Cluster of phrases</td></tr><tr><td>support( $crp_r$ )</td><td>Supporting measure of cluster  $crp_r$ </td></tr><tr><td> $w_{rk}$ </td><td>Normalized phrase frequency for cluster  $r$ ,  $k=1, 2, \dots, m$ </td></tr><tr><td> $\beta_{ik}$ </td><td>Relative importance weight of phase  $p_k$  in document  $i$ ,  $k=1, 2, \dots, m$ </td></tr><tr><td> $\beta(crp_r)$ </td><td>Normal form of the cluster phrase patterns</td></tr><tr><td> $\beta_i = \{\beta_{i1}, \beta_{i2}, \dots, \beta_{im}\}$ </td><td>Phrase weighted distribution of document  $i$ </td></tr><tr><td colspan="2">Relevance index  $r_{ij}$ </td></tr><tr><td> $J_{ij}$ </td><td>Jaccard similarity index of proposal  $i$  and reviewer  $j$ </td></tr><tr><td> $C_{ij}$ </td><td>Cosine similarity index of proposal  $i$  and reviewer  $j$ </td></tr><tr><td colspan="2">Connectivity index  $c_{ij}$ </td></tr><tr><td> $u_{ij}$ </td><td>Collaboration frequency between researchers  $i$  and  $j$ </td></tr><tr><td> $u_{IJ}$ </td><td>Collaboration frequency among researchers in community  $I$  to those in community  $J$ </td></tr><tr><td> $a_I$ </td><td>Weighted fraction of edges that connect to vertices in community  $I$ </td></tr><tr><td> $Q_s$ </td><td>Modularity measure for a network with  $s$  communities</td></tr><tr><td> $g_{ij}$ </td><td>Goodness of fit between proposal  $i$  to reviewer  $j$ </td></tr><tr><td colspan="2">Productivity index  $e_j$ </td></tr><tr><td> $G_j$ </td><td>Potential reviewer  $j$ &#x27;s publication score</td></tr><tr><td> $R_j$ </td><td>Potential reviewer  $j$ &#x27;s academic rank</td></tr><tr><td> $H_j$ </td><td>Potential reviewer  $j$ &#x27;s H-index</td></tr><tr><td> $e_j$ </td><td>Potential reviewer  $j$ &#x27;s productivity measure</td></tr><tr><td> $\overline{e}$ </td><td>Desired average productivity level determined by panel chairs or division managers</td></tr></table>

## References

[1] H. Abe, S. Tsumoto, Analysis of research keys as temporal patterns of technical term usages in bibliographical data, in: A. An, P. Lingras, S. Petty, R. Huang (Eds.), Active Media Technology, 6335, Springer, Berlin Heidelberg, 2010, pp. 150–157.

[2] E.M. Airoldi, X. Bai, K.M. Carley, Network sampling and classi<sup>fi</sup>cation: an investigation of network model representations, Decision Support Systems 51 (3) (2011) 506–518.

[3] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, Second edition Addison-Wesley, Wokingham, UK, 2011.

[4] A. Bajaj, R. Russell, AWSM: allocation of work<sup>fl</sup>ows utilizing social network metrics, Decision Support Systems 50 (1) (2010) 191–202.

[5] A.L. Barabasi, H. Jeong, Z. Neda, E. Ravasz, A. Schubert, T. Vicsek, Evolution of the social network of scienti<sup>fi</sup>c collaborations, Physica A: Statistical Mechanics and It Applications 311 (3) (2002) 590–614.

[6] J.P. Caulkins, W. Ding, G.T. Duncan, R. Krishnan, E. Nyberg, A method for managing access to web pages: <sup>fi</sup>ltering by Statistical Classi<sup>fi</sup>cation (FSC) applied to text, Decision Support Systems 42 (1) (2006) 144–161.

[7] J. Choi, S. Yi, K.C. Lee, Analysis of keyword networks in MIS research and implications for predicting knowledge evolution, Information Management 48 (8) (2011) 371–381.

[8] Y. Dang, Y. Zhang, P.J. Hu, S.A. Brown, H. Chen, Knowledge mapping for rapidly evolving domains: a design science approach, Decision Support Systems 50 (2) (2011) 415–427.

[9] Y. Dong, Z. Sun, H. Jia, A cosine similarity-based negative selection algorithm for time series novelty detection, Mechanical Systems and Signal Processing 20 (6) (2006) 1461–1472.

[10] W. Fan, M.D. Gordon, P. Pathak, Effective pro<sup>fi</sup>ling of consumer information retrieval needs: a uni<sup>fi</sup>ed framework and empirical comparison, Decision Support Systems 40 (2) (2005) 213–233.

[11] M.A.H. Farquad, I. Bose, Preprocessing unbalanced data using support vector machine, Decision Support Systems 53 (1) (2012) 226–233.

[12] M. Girvan, M.E.J. Newman, Community structure in social and biological networks, Proceedings of the National Academy of Sciences of the United States of America 99 (12) (2002) 7821–7826.

[13] A.D. Henriksen, A.J. Traynor, A practical R&D project-selection scoring tool, IEEE Transactions on Engineering Management 46 (2) (1999) 158–170.

[14] E. Herrera-Viedma, C. Porcel, Using incomplete fuzzy linguistic preference relations to characterize user pro<sup>fi</sup>les in recommender systems, Ninth International Conference on Intelligent Systems Design and Applications, ISDA '09, 2009, pp. 90–95.

[15] C.C. Huang, P.Y. Chu, Y.H. Chiang, A fuzzy AHP application in governmentsponsored R&D project selection, Omega 36 (6) (2008) 1038–1052.

[16] T. Joachims, A statistical learning model of text classi<sup>fi</sup>cation with support vector machines, Proceedings of ACM SIGIR'01, 2001, pp. 128–136.

[17] R.N. Kostoff, J.A. Del Roi, J.A. Humenik, E.O. Garcia, A.M. Ramirez, Citation mining: integrating text mining and bibliometrics for research user pro<sup>fi</sup>ling, Journal of the American Society for Information Science and Technology 52 (13) (2001) 1148–1156.

[18] R.N. Kostoff, T. Braun, A. Schubert, D.R. Toothman, J.A. Humenik, Fullerene data mining using bibliometrics and database tomography, Journal of Chemical Information and Computer Science 40 (Jan–Feb 2000) 19–39.

[19] Y. Li, C. Zhang, J.R. Swan, An information <sup>fi</sup>ltering model on the web and its application in job agent, Knowledge-Based Systems 13 (5) (2000) 285–296.

[20] Y. Li, X. Zhou, P. Bruza, Y. Xu, R.Y.K. Lau, A two-stage decision model for information <sup>fi</sup>ltering, Decision Support Systems (2011), http://dx.doi.org/10.1016/j.dss.2011. 11.005.

[21] T.M. Mitchell, Machine Learning, McGraw-Hill, New York, NY, 1997.

[22] J. Mostafa, W. Lam, Automatic classi<sup>fi</sup>cation using supervised learning in a medical document <sup>fi</sup>ltering application, Information Processing and Management 36 (3) (2000) 415–444.

[23] M.E.J. Newman, The structure of scienti<sup>fi</sup>c collaboration networks, Proceedings of the National Academy of Sciences of the United States of America 98 (2001) 404-409.

[24] M.E.J. Newman, Coauthorship networks and patterns of scienti<sup>fi</sup>c collaboration, Proceedings of the National Academy of Sciences of the United States of America (PNAS) 101 (Suppl. 1) (2004) 5200–5205.

[25] M.E.J. Newman, Fast algorithm for detecting community structure in networks, Physical Review E 69 (6) (2004).

[26] G. Oestreicher-Singer, A. Sundararajan, Recommendation networks and the long tail of electronic commerce, MIS Quarterly 36 (1) (2012) 65–83.

[27] J. Qiu, Z. Lin, A framework for exploring organizational structure in dynamic social networks, Decision Support Systems 51 (4) (2011) 760–771.

[28] S. Raghuram, P. Tuertscher, R. Garud, Research note: mapping the <sup>fi</sup>eld of virtual work: a cocitation analysis, Information Systems Research 21 (4) (December 2010) 983–999.

[29] S. Robertson, I. Soboroff, The TREC 2002 Filtering Track Report, TREC, 2002.

[30] J. Scott, Social Network Analysis: A Handbook, Sage Publications, London, 2000.

[31] N. Shibata, Y. Kajikawa, I. Sakata, Measuring relatedness between communities in a citation network Journal of the American Society for Information Science and Technology 62 (7) (2011) 1360–1369.

[32] T. Strzalkowski, Robust text processing in automated information retrieval, Proceedings of the 4th Applied Natural Language Processing Conference (ANLP), 1994, pp. 168–173.

[33] Y.H. Sun, J. Ma, Z. Fan, J. Wang, A group decision support approach to evaluate experts for R&D project selection, IEEE Transactions on Engineering Management 55 (1) (2008).158-170

[34] Y.H. Sun, J. Ma, Z.P. Fan, J. Wang, A hybrid knowledge and model approach for reviewer assignment, Expert Systems with Applications 34 (2008) 817–824.

[35] Q. Tian, J. Ma, J. Liang, R.C.W. Kwok, O. Liu, An organizational decision support system for effective R&D project selection, Decision Support Systems 39 (2005) 403–413.

[36] E. Turban, D. Zhou, J. Ma, A group decision support approach to evaluating journals, Information Management 42 (1) (2004) 31–44.

[37] A.S. Vivacqua, J. Oliveira, J.M. De Souza, i-ProSE: inferring user pro<sup>fi</sup>les in a scienti<sup>fi</sup>c context, The Computer Journal 52 (7) (2009) 789–798.

[38] K.M. Wang, C.K. Wang, C. Hu, Analytic hierarchy process with fuzzy scoring in evaluating multidisciplinary R&D projects in China, IEEE Transactions on Engineering Management 52 (1) (2005) 119–129.

[39] D.J. Watts, S.H. Strogatz, Collective dynamics of ‘small-world’ networks, Nature 393 (1998) 440–442.

[40] Z. Zheng, K. Chen, G. Sun, H. Zha, A regression framework for learning ranking functions using relative relevance judgments, Proc. of SIGIR'07, 2007, pp. 287–294.

Thushari Silva is currently pursuing her PhD in the department of Information Systems at the City University of Hong Kong. She received her MSc. in Information and Communication Technology from Asian Institute of Technology, Thailand in 2010. Her research interests include research social network analysis, recommender systems, business intelligence and semantic web.

Zhiling Guo is an Assistant Professor in Information Systems at the City University of Hong Kong. She received her Ph.D. in Management Science and Information Systems from The University of Texas at Austin in 2005. Dr. Guo's general research interests include online auctions, electronic markets, cloud computing, crowdsourcing, social networks, social media marketing, and supply chain risk management. Dr. Guo's papers have been published in Management Science, Information Systems Research, Journal of Management Information Systems, Decision Support Systems, among others

Jian Ma is a Professor in the Department of Information Systems at the City University of Hong Kong. He received his Doctor of Engineering degree in Computer Science from Asia Institute of Technology in 1991. Prof. Ma's general research interests include business intelligence, research and Innovation Social Networks, research information systems and decision support systems. His past research has been published in IEEE Transactions on Engineering Management, IEEE Transactions on Education, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems and European Journal of Operational Research, among others.

Hongbing Jiang is currently pursuing his PhD in the University of Science and Technology of China–City University of Hong Kong joint Advanced Research Center, Suzhou. His research interests include recommendation systems and social network analysis.

Huaping Chen is a Professor of School of Management at the University of Science and Technology of China. His research interests include information strategies, business intelligence and application. His past research has been published in Journal of Operations Management, Decision Support Systems and Computers & Operations Research, among others.
