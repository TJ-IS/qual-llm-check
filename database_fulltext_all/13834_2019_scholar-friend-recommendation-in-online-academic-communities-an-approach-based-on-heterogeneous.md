---
otero_id: 13834
otero_key: "TQG38ARG"
title: "Scholar-friend recommendation in online academic communities: An approach based on heterogeneous network"
authors: "Yunhong Xu; Duanning Zhou; Jian Ma"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.01.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Scholar-friend recommendation in online academic communities: An approach based on heterogeneous network

![](/api/attachments/TQG38ARG/fulltext/images/cdb1adad57223732d82b1a6d322cbe6b22f80c0e091f832517745b3a62e0370a.jpg)

Yunhong Xu<sup>a,⁎</sup>, Duanning Zhou<sup>b</sup>, Jian Ma<sup>c</sup>

<sup>a</sup> Faculty of Management and Economics, Kunming University of Science and Technology, China

<sup>b</sup> Department of Information Systems & Business Analytics, Eastern Washington University, USA

<sup>c</sup> Department of Information Systems, City University of Hong Kong, Hong Kong Special Administrative Region

## A R T I C L E I N F O

Keywords: Online academic community Scholar-friend recommendatior Expert recommendation Heterogeneous network Friend recommendation Network analysi

## A B S T R A C T

As a particular type of social networking site, online academic communities have revolutionized the way researchers collaborate and communicate with each other. Accompanying the growth in the number of users registered on online academic communities, the information overload problem presents a great challenge for researchers trying to find relevant and reliable friends there. Diferent from friends in conventional social net working sites, friends in online academic communities are denoted as scholar-friends in this research. Scholarfriend recommendation in online academic communities involves diferent entities (e.g., researchers, research articles, afiliations, research interests, and status updates) and various relationships among entities (e.g., scholar-friend relationship of researchers, post relationship between researchers and status updates, and writing relationship between researchers and papers), which constitute a complex heterogeneous network. By leveraging the entity and relationship data in online academic communities, this research proposes a heterogeneous network-based approach to recommending scholar-friends where information gain is used to identify valuable meta paths and a regularization-based optimization is employed to make personalized recommendations for each individual researcher. Experimental results based on historical data and user experiments demonstrate that the proposed approach can achieve better performance compared to some baseline approaches. Additionally, we further discuss how the meta paths and corresponding learned weights can help to understand researchers preferences and behaviors.

## 1. Introduction

Scientific research is vital to economic growth and societal revolution [1]. Due to the complex and multi-disciplinary nature of scientific research problems and the intense dynamics of research fields, collaboration has become one of the most crucial and common phenomena in the scientific community [2]. At the researcher level, collaborations may vary in forms, from earlier stages of scientific collaboration such as idea exchanges (e.g., the formulation of the research question, what hypothesis to test, how to conduct experiments, how to collect data, and how to relate research findings to theoretical contributions) to indepth collaboration like paper co-authorships or even project participation [3]. Collaboration enables researchers to access resources and knowledge necessary to conduct their research. Furthermore, collaboration may facilitate a melting pot of ideas, which may in turn help individual researchers generate new insights or perspectives. Collaboration at the individual level may advance scientific progress as a whole. Therefore, various initiatives have been launched and infrastructures have been constructed with the aim of fostering collaboration among individual researchers by bringing them together in research centers or research groups [2]. Considerable research has also suggested that information technologies have had significant efects on the research environment and made it so that the cyberinfrastructure of collaboration has been integrated into research contexts. Particularly, social networking techniques have served as the basis for online academic communities, which fundamentally change the way researchers collaborate with each other [4].

As a specific kind of online community based on social networking techniques, online academic communities aim to help scholars conduct scientific research. Online academic communities enable researchers to construct profiles which contain their information, like their names, photos, educational background, research interests, projects, and publications. Via engagement in online academic communities, researchers can gain two benefits: relational benefit and functional benefit. In terms of relational benefit, online academic communities help researchers manage their academic relationships through scholar-friend management. Scholar-friends are friends of researchers in online academic communities. Researchers not only use online academic communities to maintain contact with old scholar-friends, but also use these communities to find new scholar-friends they might be interested in connecting with. Maintaining relationships with old scholar-friends may strengthen their academic relations and makes researchers aware of their scholarfriends' recent works. Constructing new academic relations with others allows researchers to expand their academic circles via functions such as browsing others' profiles, seeking researchers with similar interests, sending an invitation to other researchers, becoming a scholar-friend, and communicating with each other. In terms of functional benefit, individual researchers can easily share and exchange knowledge, resources, skills, and techniques with others via online academic com munities. In addition, researchers could showcase their progress to others and disseminate research results including papers, presentations, patents, and projects, which may ultimately raise their academic influence. Through online academic communities, researchers can keep track of the works being conducted by others in professional areas, which can help them discover new information and develop research ideas. The usage of online academic communities through computers and mobile devices has become quite widespread, and recently, various online academic communities have been developed, e.g., ResearchGate, YourEncore,<sup>2</sup> and ScholarMate.<sup>3</sup> Those online academic communities allow researchers to connect with others in their field and facilitate academic collaboration among researchers.

Although online academic communities provide services to facil itate scientific collaboration in a global context by transcending conventional organizational and geographical boundaries [5], the information overload problem occurring on these platforms presents a great challenge for researchers trying to find interesting and relevant information. It is reported that by October 2017, ResearchGate had over 14 million registered researchers and > 100 million publication pages, and the number of users exceeded 56 million on Academia.<sup>4</sup> The increasing number of registered researchers and significant amount of relevant information in online academic communities pose challenges for researchers trying to find scholar-friends they might be interested in. The information overload problem may lead to a degraded user experience which could subsequently afect users' intentions to continue their usage of online academic communities [6]. In order to achieve a win-win outcome for both individual researchers and the platform of online academic communities, scholar-friend recommendation approaches are crucial to address the information overload problem by providing a limited number of preferred matches.

It is meaningful to propose the scholar-friend recommendation approach to facilitating knowledge management in online academic communities. From the perspective of online academic communities, satisfying users' needs by providing relevant and valuable services may enhance users' loyalty toward the platform and maintain prosperity for an extended period. From the perspective of individual researchers, providing value-added services like scholar-friend recommendation may reduce their search costs, enhance their knowledge-sharing and collaborative behaviors, extend their social circles, and thus ultimately increase their adoption and engagement in the online academic community [7]. In addition, the knowledge-sharing and collaborative behavior occurring at the individual researcher level may be aggregated to higher levels and enhance scientific knowledge flow among diferent academic organizations [8]. Knowledge exchanging in a broader con text can foster impactful knowledge discovery and innovation, and even advance the development of science.

In online academic communities, scholar-friend recommendation can be considered as an intersection of expert recommendation and friend recommendation in that both users' expertise and social in formation should be considered at the same time. Although expert recommendation and friend recommendation have been studied ex tensively and individually in previous research, scholar-friend recommendation has received less attention. The recommendation background, users' focus, and involved information are quite diferent in these three contexts. Directly applying existing expert recommendation or friend recommendation methods in online academic communities may lead to inefective results. In online academic com munities, users' expertise and social information is embedded in a complex heterogeneous network where diferent entities (e.g., re searchers. research articles. affiliations. research interests. and status updates) and various relationships among entities (e.g., scholar-friend relationship of researchers, post relationship between researchers and status updates, and writing relationship between researchers and pa pers) are involved. Relationships between entities may reflect researchers' expertise or social relationships to some extent. For example, a researcher may like others' posted articles. The liking relationship may also reflect this researcher's interest to some extent. Therefore, we need to systematically integrate expertise information and social information in online academic communities to provide personalized recommendations. To achieve this goal and address the uniqueness of scholar-friend recommendation, we use a heterogeneous network to integrate researchers' expertise and social relationship information in a unified framework. Moreover, existing expert and friend recommendation approaches lack a mechanism to explain why the recommendations are made and what information they are based on. In other words, they often treat recommendation as a black box, where the input is users' information and the output is the recommendation result. This research attempts to address this issue from two aspects. First. we use information gain to identify valuable meta paths that are useful to make recommendations. These meta paths represent what information users care about when they choose scholar-friends. Second, regular ization-based optimization is emploved to calculate the weights of the selected meta paths and make personalized recommendations for each individual researcher. The weight information of meta paths represents the extent to which users care about the information when choosing scholar-friends.

## 2. Literature review

While recommendation approaches have been extensively studied in previous research to solve the information overload problem and increase users' satisfaction in various contexts [9–11], few researches focus on scholar-friend recommendation in online academic communities because the concept and context is relatively new. There are two research streams relevant to this research: expert recommendation and friend recommendation. Expert recommendation tries to recommend experts who might possess particular expertise as required by users. Friend recommendation attempts to recommend friends to users with whom they may want to build relationships. We review expert recommendation and friend recommendation in the following sections. After that, the unique features of scholar-friend recommendation are identified by comparing scholar-friend recommendation with other two recommendation applications.

## 2.1. Expert recommendation

Identification of people with the relevant expertise in a specific area could be of considerable value in many applications, e.g., assigning appropriate reviewers to academic articles [12], finding leading experts in a research group [13], and recommending the right doctors for a specific disease [14]. Initially, most research on expert recommendation has been conducted within organizations, where a repository is built to store knowledge of experts. However, building and maintaining the repository is time-consuming and labor-intensive. Moreover, the static repository cannot reflect the continuous change of peoples' expertise. To mitigate these shortcomings and satisfy organizations' information needs, many automatic systems have been proposed to find experts for a given problem in organizations such as Answer Garden [15], Expertise Recommender [16], and DEMOIR approach [8]. Text Retrieval Conference (TREC), which launched the expert search task in the Enterprise track in 2005, provided a common platform for researchers to empirically evaluate methods and techniques, and consequently various approaches have been proposed [17,18].

Most of these organizational expert search works fall into two categories: link-based or content-based approaches. The link-based expert recommendation employs graph-based ranking algorithms to rank ex perts and make recommendations accordingly [19]. The content-based expert recommendation approach can be further divided into two categories: profile-based and document-based. The profile-based expert recommendation approach first merges all sources concerning a candidate expert into a single personal profile, then ranks these individual profiles with respect to user queries using retrieval techniques and suggests best candidate experts to the target user [20]. For profile-based expert recommendation approaches, various methods are proposed in previous research to measure the relevance between experts' profiles and users' needs, e.g. fuzzy logic [21], and the vector space model [22]. The document-based expert recommendation approach tries to use supporting documents to rank the candidate experts based on the cooccurrences of topic and candidates mentioned in the documents [23].

With the development of social networking techniques and the growth of social network sites, the scope of expert-finding research has been extended from physical organizations to online communities [24]. Concerning expert recommendation in online communities, two types of information are widely used: expertise (e.g., domain expertise, key words, documents, posts) and network information (e.g., trust, co-author, ask and answer).

Existing research emphasizes how to integrate related information to make expert recommendations. As for online question and answer communities, Alam et al. [25] developed a dynamic points-based user reputation model to generate diverse replier recommendations where users' ratings and social network analysis methods were considered. Zhou et al. [26] designed a topic-sensitive probabilistic model which incorporated link structure and topical similarity among users into a unified framework to search experts. Liu et al. [27] integrated user subject relevance, their reputation, and authority of a category to find experts in online question and answer communities. Huang et al. [28] designed a system to recommend experts based on users' social capita and expertise similarity. For product review websites, Wei et al. [29] proposed an ExpRank algorithm which integrated the positive and negative agreement relations of users to make expert recommendations. Wang et al. [30] proposed the ExpertRank algorithm, where both document-based relevance and users' authority were used to find ex perts for online knowledge communities. Omidvar et al. [31] employed WordNet dictionary and social network analysis to find experts for an online community. Given the expertise evidence of the current time, Neshati et al. [32] proposed a learning framework to predict the ranking of experts in the future for online communities, where four features were considered: topic similarity, emerging topics, user behavior, and topic transition. Pal et al. [33] proposed a probabilistic model to identify experts from other users by analyzing their selection pre ferences.

## 2.2. Friend recommendation

Social networking sites such as Facebook, Twitter, and Flickr have experienced rapid growth over the past decade [34]. These social networking sites allow users to seek information and express themselves. Furthermore, users in social networking sites can make online friends and engage in a variety of social activities, e.g., visiting friends' statuses, discussing with each other, and sharing information with their friends. The aim of friend recommendation in these platforms is to suggest new potential friends to users and expand their existing social networks. Initially, friend recommendation in social networking sites was based on social network information such as friends of friends. However, recommendation approaches based on friends of friends cannot generate satisfactory results because making online friends is a complex decision making process and friend information alone cannot capture the whole picture. To achieve better recommendation performance, in addition to friend information, more factors were included in later research [35,36], e.g., user interests, user profiles, social environment, social behaviors, social roles, and interaction networks. Several principles serve as the guidelines to integrate various kinds of information and make friend recommendations, e.g., similar users tend to contact each other more than dissimilar ones, potential relationships occur depending on existing relationships, users who have ofline social relationships have a higher probability of becoming online friends [37].

Research on friend recommendation in social networks has received much attention and various methods have been proposed to conduct recommendation eficiently. Using nodes to represent people and edges to depict friendships among them, link prediction was employed to infer future links of users and recommend friends accordingly [38]. Chen et al. [6] combined learning to rank techniques with social in fluence to model and analyze user behavior, and informative friend were recommended based on the analysis results. Huang et al. [39] investigated the structure of social networks and developed an algo rithm for social friend recommendation based on network correlation. Xu-Rui et al. [40] first identified key factors for friendship prediction, and then proposed a friendship prediction method based on selected features. Jiang et al. [41] used a novel probabilistic matrix factorization method to fuse individual preference and interpersonal influence in latent space, and proposed a scalable algorithm to make social friend recommendation in Twitter and Facebook. Huang et al. [42] applied a two-stage framework to synthesize heterogeneous information from diferent domains to recommend friends. In the first stage, possible friends were obtained based on aligning the tag-similarity network to the friend network. In the second stage, a topic model was used to further refine the recommendation results based on the relationship between image features and users. Zheng et al. [43] proposed a tem poral-topic model to recommend friends in a microblogging system, where users' topic distributions were extracted from keyword usage patterns and friend recommendations were made based on the simila rities of user’ topic distribution. Huang et al. [39] proposed an algo rithm for network correlation-based social friend recommendation, where related networks were aligned by selecting important features from each network. Based on user similarity and users' contact strength. Liao et al. [37] developed a friend recommendation approach. Jiang et al. [44] proposed a big data analytic solution that used the MapRe duce model to discover groups of frequently connected users for friend recommendation. Modelling user's daily life as life documents and ex tracting their life styles using the latent allocation algorithm. Friend. book calculated the similarity of life styles between users and returned a list of people with highest recommendation scores to the query user [45]. Yu et al. [46] proposed a friend recommendation method called ACR-FoF (algebraic connectivity regularized friends-of-friends), where both success rate and content spread in the network were considered when making recommendations

## 2.3. The unique features of scholar-friend recommendation

Scholar-friend recommendation demonstrates several unique features which make it diferent from the other two recommendation contexts. In this section, we address these unique features by comparing these three recommendation contexts from several aspects: recommendation purpose, interaction types, the meaning of expertise, and social relations. In the expert recommendation context, users need experts to solve particular problems or answer specific questions. The interactions between users and experts are problem-oriented, and their relationships tend to be temporary. The interaction relationships are often represented as ask-and-answer. Expertise information of expert recommendations may reside in users' profiles, documents, or even their interaction activities. Social relations are used to filter experts such that experts who are close to target users in the social network are recommended. In the friend recommendation context, users focus more on the entertainment and relationship aspect. Therefore, the interac tions among users may be more frequent and may last for a long time, and the interaction may take various forms, e.g., communicating, commenting and liking. As for scholar-friend recommendation, the frequency and the length of time of interactions may lie between expert and friend recommendation. The interactions tend to be more research related, e.g. via their papers, projects, or academic activities. Both expertise and social relationship information is contextual information, which varies in diferent applications and contexts. Particularly, in the online academic community context, researchers' social relationship information includes their scholar-friend relationship, co-authorships, coming from the same afiliations, joining the same groups, liking and commenting on others' status updates, and sharing articles with other members. Researchers' expertise information can be directly reflected through their published papers and claimed research interests in their profiles, or indirectly imbedded in the social relationships of researchers. To address the unique features of online academic communities and integrate multi-dimensional information on expertise and social relations, we propose a scholar-friend recommendation approach based on a heterogeneous network.

## 3. Definition and research framework

According to the literature review, we know that compared to expert recommendation and friend recommendation, scholar-friend recommendation in online academic communities has its own char acteristics. Expertise and social relations are context-specific and research-oriented in online academic communities. To systematically integrate information in online academic communities and make recommendations accordingly, this section first introduces relevant definitions and concepts used in this research. After that, a scholar-friend recommendation framework is proposed based on a heterogeneous network.

## 3.1. Definition and concepts

## 3.1.1. Definition 1 heterogeneous network [47]

A network can be described as an augmented graph G(V,E), where V represents entities, and E denotes connections among entities. Based on the graph, there is an entity type mapping function : $\mathrm {  ~ V ~ } \to \mathcal { A } ,$ , which means that each entity $\mathbf { v } \in \mathrm { V }$ belongs to an entity type $\sigma ( \mathbf { v } ) \in \mathcal { A } .$ Similarly, there is a link type mapping function $\varphi \colon \mathrm { E }  \mathcal { R }$ , which means each link e ∈ E belongs to a link type (e) . A network is a het erogeneous network when there are multiple types of entities or links, in other words. either $| { \mathcal { A } } | > 1 \mathrm { o r } | { \mathcal { R } } | > 1$

Fig. 1 shows the heterogeneous network of entities and their links in an online academic community. In this heterogeneous network, entities have diferent types, e.g., researcher, paper, afiliation, and group. The links between entities also have diferent types. Taking the link between researcher and update entity for example, the relationship can take various types, e.g., posting, liking, and commenting. As the figure shows, researchers can have three kinds of social relationships in online academic communities: direct social relationships, entities-based in direct relation with equal roles, and entities-based indirect relation with diferent roles. Direct social relationships mean that researchers are directly connected with each other without other entities. Scholarfriend is one important direct social relationship. Entity-based indirect relations with equal roles mean that social relations of researchers can be inferred through connections of other entities, and their roles in the relations are same, e.g., two researchers coauthor one paper, come from the same afiliation, share common research interests, and join the same group. Entity-based indirect relations with diferent roles mean that researchers' roles in the inferred relationship based on other entities are diferent, $\mathrm { e . g . , }$ one researcher posts an update and another researcher comments on the update. Here one researcher is the writer and another one is commenter. The updates can take various forms, e.g., the papers they have read, the conferences they are going to attend, and even their papers they are going to publish.

In online academic communities, researchers can build direct relationships with others by becoming scholar-friends. Furthermore, indirect relationships can be inferred from the interactions of researchers through objects (whether their roles are equal or diferent). For example, a researcher may post updates $( \boldsymbol { \mathrm { e . g . } }$ , his/her new publications) on online academic communities. His/her scholar-friends can express their feelings by simply clicking the $^ { \mathfrak { s } } \mathrm { L i k e } ^ { \mathfrak { n } }$ button or adding a few comments. Comments or likes suggest a sign of similar interest between researchers. Given that direct and indirect relationships are indicators of researchers' expertise or expertise embedded in the social behaviors, direct and indirect relationships can be integrated into a multi-layer heterogeneous network, where layers could reflect the expertise and social relations of researchers.

## 3.1.2. Definition 2 network schema [47]

The network schema can be denoted as $T _ { G } = \left( \mathcal { A } , \mathcal { R } \right)$ , which is a meta representation of network G(V,E) and specifies type constraints on the entities and link types among entities. These network schema constraints guide the semantic exploration of entities via links. Fig. 2 illustrates the network schema which describes the entities and their relationships in the network. In this example, the network schema contains seven entities and the relationships among them. Seven entities are included in the network schema: researcher, afiliation, research interest, paper, update, group, and academic resource. Entities are connected via links based on the link types. For example, the link between paper and researcher refer to two kinds of relationships in an online academic community: 1) researcher writes the paper or the paper is written by the researcher; 2) researcher shares the paper with other researchers or the paper is shared by a researcher. The links be tween researcher and update involve several relationships, e.g., post, like, comment. A network following the entity and type constraint of network schema is called a network instance.

## 3.1.3. Definition 3 network meta path

A meta path $\begin{array} { r } { \mathrm { p } = \mathrm { A } _ { 1 } \stackrel { \mathrm { R } _ { 1 } } {  } \mathrm { A } _ { 2 } \stackrel { \mathrm { R } _ { 2 } } {  } . . . \stackrel { \mathrm { R } _ { \mathrm { k } } } {  } \mathrm { A } _ { \mathrm { k } + 1 } } \end{array}$ is a path defined based on a network schema $\Gamma _ { G } = ( { \mathcal { A } } , { \mathcal { R } } )$ . The meta path denotes a new composite relation $\mathbf { R } = \mathbf { R _ { 1 } } ^ { \circ } \mathbf { R _ { 2 } } . . . \mathbf { R _ { k } }$ between entity type $\mathsf { A } _ { 1 }$ and $\mathbf { A } _ { \mathbf { k } + 1 } ,$ where $\mathbf { A } _ { \mathrm { i } } \in \mathcal { A }$ and $\mathrm { R } _ { \mathrm { i } } \in \mathcal { R } \ \mathrm { f o r ~ i = 1 , } , \ldots \mathrm { k } + 1 , ^ { \circ }$ represents composition operator on relations. A concrete path following the entity and relation requirement of a meta path is called a path instance. Diferent meta paths can have diferent semantic meanings. For example, the co-author relationship can be described using a length-2 meta path Researche $\cdot { \stackrel { \mathrm { w r i t e } } { \to } } \mathrm { P a p e r } ^ { \mathrm { w r i t e } ^ { - } }$ 1 Researcher. One researcher liking others' posted updates can be represented using a meta path $\stackrel { \mathrm { p o s t } } {  } \mathrm { U p d a t e } ^ { \mathrm { l i k e } ^ { - } }$ 1 Researche Researcher. Table 1 shows examples of meta paths and their physical meanings in this research context. The rich semantic information of meta paths enables us to explore diferent link with diferent paths between entities.

![](/api/attachments/TQG38ARG/fulltext/images/729a8fe5f5f008153d08d84d92c07481cb3e25d964c5fbb081eb9db3887455e9.jpg)  
Fig. 1. Heterogeneous network in an online academic community.

## 3.2. The proposed recommendation framework based on heterogeneous network

Based on above-mentioned definitions and concepts, we propose a heterogeneous network recommendation framework which consists of several steps as illustrated in the following sub-sections.

## 3.2.1. Meta path set generation

Researchers' expertise and relationship preference toward scholarfriends is embedded in their meta paths. Theoretically speaking, all possible meta paths could be used to make recommendations. Previous research has demonstrated that inclusion of some longer meta paths could significantly improve recommendation accuracy [48]. However, too many longer meta paths may lead to higher computational costs and bring noise information into the recommendation model. There fore, it is necessary to determine which meta paths should be included in the recommendation model based on their values. In other words, if the meta paths can add extra information to the recommendation, then the meta paths should be included. Otherwise, if the information of the meta paths is redundant, then it should not be used for recommendation. In this research, information gain is used to evaluate the value of the meta path.

Consider a meta path M represented $\operatorname { a s } X { \stackrel { R _ { 1 } } {  } } \ldots Y ,$ which means the meta path begins with entity type X and ends with entity type Y. This meta path contains an arbitrary number of composite relationships between X and Y, except that the first relation type of meta path M is $R _ { 1 }$ Then the information gain obtained by traversing from X to Y following the meta path M can be calculated as follows:

$$
G _ {M} = H (X) - H _ {M} (X \mid Y)\tag{1}
$$

where $G _ { M }$ represents the information gain of meta path M, H(X) denotes the entropy of entity type $X ,$ and $H _ { M } ( X | { \cal Y } )$ is the conditional entropy obtained following the meta path M. H(X) can be calculated using Eq. (2).

$$
H (X) = - \sum_ {x \in X} p (x) \log p (x)\tag{2}
$$

Eq. (2) means that to apply this equation, we need a measure of the probability of a particular node of a given type. In this research, we use degree centrality to measure the probability of this node. The basic idea is that nodes with higher degree are more likely to be encountered when walking along the network. And the probability of one single node is normalized by the total degree of all nodes of the same type. Therefore, the probability can be calculated using Eq. (3).

![](/api/attachments/TQG38ARG/fulltext/images/ac8e8155085a190197f424a3834e555da7e79cb28888a83fdd15e4499c608c1b.jpg)  
Fig. 2. An example of network schema in online academic community.

$$
p (x) = \frac {D e g r e e (x)}{\sum_ {n \in X} D e g r e e (n)}\tag{3}
$$

In Eq. (3), Degree(x) is defined as the number of edges that follow the relation type $R _ { 1 }$ incident on node $x ,$ and $R _ { 1 }$ is the first relation type of meta path M. $\textstyle \sum _ { n \in X }$ Degree n( ) represents the total degree of all node of the same type, which is used to normalize Degree(x).

The entropy of entity type X can be calculated using Eqs. (2) and (3). Next we discuss how to calculate conditional entropy. Conditional en tropy is used to measure the information uncertainty of one dimension given another dimension [49]. Conditional entropy $H _ { M } ( X | { \cal Y } )$ can be calculated as shown in Eq. (4).

$$
\begin{array}{r l} & H _ {M} (X \mid Y) = \sum_ {y \in Y} p (Y = y) \times H _ {M} (X \mid Y = y) \\ & = - \sum_ {y \in Y} p (y) \times \sum_ {x \in Y} p _ {M} (x \mid y) \log p _ {M} (x \mid y) \end{array}\tag{4}
$$

In Eq. $( 4 ) , p _ { M } ( x | y )$ represents conditional probability based on meta path $M . \ p _ { M } ( x | y )$ measures the fraction of all possible expansions starting from node x to node y out of all possible expansions from node x to some node with entity type ${ \cal Y } ,$ given a meta path M. $p _ { M } ( x | y )$ can be calculated using Eq. (5), where $\| \{ x \in X , y \in Y , m \in M , x {  } _ { m } y \} \|$ represents the number of instances starting from node x to node y following meta path M, and $\| \{ x \in X , n \in Y , m \in M , x {  } _ { m } n \} \|$ denotes the number of instances starting from node x to node n following meta path M.

$$
p _ {M} (x \mid y) = \frac {\| \{x \in X , y \in Y , m \in M , x \to_ {m} y \} \|}{\sum_ {y \in Y} \| \{x \in X , n \in Y , m \in M , x \to_ {m} y \} \|}\tag{5}
$$

Because the meta path starts from and ends with diferent entity types, normalization is necessary to better reflect the information gain of diferent meta paths. We use $\operatorname { E q . }$ (6) to normalize the information gain. Based on the value of information gain for meta paths, the ones with lower value have a higher probability to be noisier and contain less information. Therefore, those meta paths are eliminated and only meta paths with high information gain are used in recommendation.

$$
\widehat {G _ {M}} = \frac {G _ {M}}{\sqrt {H (X) H (Y)}}\tag{6}
$$

We present an example to show how to calculate information gain isscholarfriendof for a particular meta path M Researcher= have Researcher Research Interest.We first demonstrate how to calculate H (Researcher). For any node x with type Researcher, we use eq. (3) to calculate its probability, where Degree(x) represents the number of edges that follow the relation type isscholarfriendof incident on nodex. $\begin{array} { r } { \sum _ { n \in { \cal { X } } } D e g r e e ( n ) } \end{array}$ represents all number of edges incident on nodes of type Researcher. As shown in Eq. (2), we can use p(Researcher) to calculate H(Researcher). We then discuss how to calculate H (Researcher| Research Interest). As shown in Eq. (4), the key is to calculate p(Research Interest) and $p _ { M } ( \mathbf { \Omega }$ (Researcher| Research Interest). Similar to p(Researcher), p(Research Interest) can be calculated using degree information. $p _ { M } ($ (Researcher| Research Interest) can be calculated using Eq. (5). $\| \{ x \in X , y \in Y , m \in M , x \hat { \to } _ { m } y \} \|$ represents the number of instances starting from node x (with node type Researcher) to node y (with node type Research Interest) following meta path isscholarfriendof $\stackrel { h a v e } {  }$ M Researcher= Researcher Research Interest. $\textstyle \sum _ { y \in Y } \vert \vert \{ x \in X , n \in Y , m \in M , x  _ { m }$ }y denotes the total number of instances starting from node x (with node type Researcher) to all nodes of type Research Interest following meta path $i s s c h o l a r f r i e n d o f$ have M Researcher= Researcher Research Interest. After calculating H(Researcher) and H (Researcher| Research Interest), the information gain of this meta path $G _ { M }$ can be calculated as H(Researcher) $- \ : H _ { M }$ (Researcher| Research Interest). If the values of H (Researcher) and (Researcher| Research Interest) are roughly the same, then $G _ { M }$ is near $^ { 0 , }$ which suggests that the meta path M does not provide more information beyond what is contained in the Researcher dimen sion.

Example of meta path and their physical meaning.

<table><tr><td>Path instance</td><td>Meta path</td><td>Physical meaning</td></tr><tr><td> $Liu \overset{write"}{\rightarrow} Data\ minging\ using\ SVM" \overset{write^{-1}}{\rightarrow} Wang$ </td><td> $Researcher \overset{write}{\rightarrow} Paper \overset{write^{-1}}{\rightarrow} Researcher$ </td><td>Researchers collaborate on the same paper</td></tr><tr><td> $Chen \overset{post"}{\rightarrow} I\ will\ attend\ an\ academic\ conference$  $in\ July" \overset{like^{-1}}{\rightarrow} Wang$ </td><td> $Researcher \overset{post}{\rightarrow} Update \overset{like^{-1}}{\rightarrow} Researcher$ </td><td>Researchers like others&#x27; posted updates</td></tr></table>

## 3.2.2. Personalized weight learning for meta path

After deciding which meta paths should be used to make recommendations based on their information gains, the next step is to determine the personalized weights of every included meta path for each user. Researchers may express diferent preferences toward dif ferent meta paths. For example, some researchers only add their paper collaborators as scholar-friends. In this example, the meta path

Researcher $\stackrel { w r i t e } {  } P a p e r \stackrel { w r i t e ^ { - } } {  }$ Researcher is more important than other meta paths. Some researchers may prefer to become scholar friends with those who have similar research interests. For these researchers, the meta path Researcher $\stackrel { h a v e } {  }$ Research Interest $\stackrel { h a v e ^ { - 1 } } {  }$ Researcher plays a more significant role in recommendation. For each researcher, we calculate his/her personalized weight for each meta path. The detailed procedure is shown as follows.

For all users, the weight matrix of all selected meta paths can be represented as a matrix W. The entry of the matrix denotes that for a researcher u, the weight of meta path k is $w _ { u } ^ { \ k } , \forall k ,$ , ∀u. The row vector of the matrix is $W _ { u } = ( w _ { u } , ^ { 1 } { w _ { u } } ^ { 2 } \dots w _ { u } ^ { \hat { K } } ) .$ , which represents the weight vector of each meta path for researcher u. The column vector is $\pmb { W } ^ { k } = ( { w _ { 1 } } ^ { k } { w _ { 2 } } ^ { k } \ldots { \dot { w _ { u } } } ^ { k } ) ^ { T }$ , which represents the weight vector of all users on meta path M . The weight value of the meta paths should satisfy two requirements. First, minimize the squared error between the real scholar-friend relationships and the predicted recommendation score of scholar-friend relationships based on the weight of meta paths. Second, similar users tend to have similar path weights. Then the weight of a meta path can be calculated by solving the following optimization problem as shown in Eq. (7).

$$
\begin{array}{l} \underset {w} {\text {minL}} (W) = \frac {1}{2} Y - \sum_ {k = 1} ^ {K} \text {diag} (W ^ {k}) \hat {Y} _ {2} ^ {k ^ {2}} + \frac {\lambda_ {1}}{2} \sum_ {k = 1} ^ {K} W ^ {k} - \bar {S} ^ {- k} W _ {2} ^ {k ^ {2}} + \frac {\lambda_ {0}}{2} W _ {2} ^ {2} \\ \text {s.t.} W \geq 0, \forall u, \forall K \end{array}\tag{7}
$$

where Y is a matrix where the element $y _ { i , j } = 1$ means that researcher i and researcher j are scholar-friends and 0 otherwise. diag( $\boldsymbol { w } ^ { k } )$ denotes the diagonal matrix transformed from the vector $w ^ { k } . \ \| \cdot \| _ { 2 }$ stands for Frobenius norm. $\left\| \cdot \right\| _ { 2 } ^ { 2 }$ represents the square of the Frobenius norm. $\lambda _ { 0 } { \bf { a n d } } \lambda _ { 1 }$ are the parameters which reflect the importance of the com ponents in the objective function. ${ \widehat { Y } } ^ { k }$ is the predicted recommendation score of researchers based on meta path M , which is determined by two aspects: the similarity of users and their actual scholar-friend relationship.

$$
\widehat {Y} _ {i, v} ^ {k} = \sum_ {j} S _ {i, j} ^ {k} Y _ {j, v}\tag{8}
$$

$S _ { i , j } { } ^ { k }$ is the similarity between researcher i and j under meta path $M _ { k }$ which can be calculated as follows:

$$
S _ {i, j} ^ {k} = \frac {| | \{i \to_ {M _ {k}} j \} | |}{| | \{i \to_ {M _ {k}} i \} | | + | | \{j \to_ {M _ {k}} j \} | |}\tag{9}
$$

$S _ { i . \ j } ^ { \mathrm { ~ \textsc ~ { ~ k ~ } ~ } }$ is defined by two parts: (1) the connectivity measured by the number of path instances between these two researchers following meta path $M _ { k } ;$ (2) the balance of their visibility, where the visibility is defined as the number of path instances between themselves. $\| \{ i \to _ { M _ { k } } j \}$ ‖ denotes the number of path instances between researcher i and j following meta path $M _ { k } . \parallel \{ \textit { i } \to _ { M _ { k } } i \} \parallel$ is that between researcher i and i following meta path M , and $\| \{ j \to _ { M _ { k } } j \} \|$ is that between j and j. From this equation, we know that given a meta path $M _ { k } ,$ the similarity between two researchers is defined on two parts: first, their connectivity, which is defined by the number of paths between these two researchers following meta path M ; second, the balance of each researcher's visibility in the network, which is defined as the number of path instances between themselves following meta path $M _ { k }$

$\overline { { S } } _ { i , j } ^ { k }$ is the normalized researcher similarity based on meta path M , which can be calculated as follows:

$$
\overline {{S}} _ {i, j} ^ {k} = \frac {S _ {i . j} ^ {k}}{\sum_ {j} S _ {i . j} ^ {k}}\tag{10}
$$

Projected gradient method for non-negative bound-constrained optimization can be used to solve this optimization problem [50]. The gradient of Eq. (7) with respect to ${ w _ { u } } ^ { k }$ can be calculated as follows:

$$
\begin{array}{r} \frac {\partial L (W)}{\partial w _ {u} ^ {k}} = - \left(Y _ {u} - \sum_ {k = 1} ^ {K} w _ {u} ^ {k} \widehat {Y} _ {u} ^ {k}\right) (\widehat {Y} _ {u} ^ {k}) ^ {T} + \lambda_ {1} (w _ {u} ^ {k} - \overline {{S}} _ {u} ^ {k} W ^ {k}) \\ - \lambda_ {1} (\overline {{S}} _ {u} ^ {k}) ^ {T} (W ^ {k} - \overline {{S}} ^ {k} W ^ {k}) + \lambda_ {0} w _ {u} ^ {k} \end{array}\tag{11}
$$

${ w _ { u } } ^ { k }$ can be calculated using following equation:

$$
w _ {u} ^ {k} := \max \left(0, w _ {u} ^ {k} - \alpha \frac {\partial L (W)}{\partial w _ {u} ^ {k}}\right)\tag{12}
$$

where α is the step size and can be set according to Lin [50]. The pseudo code of the algorithm to learn the weight of meta path is shown in Fig. 3.

For a specific user u, we use an example to demonstrate how to calculate the weight of a particular meta path isscholarfriendof M Researcher= Researcher late the similarity between researcher u and any other researcher in the candidate list. After that, Eq. (10) is used to normalize user similarity. Then we use Eq. (8) to calculate the predicted recommendation score between researcher u and other researchers based on meta path M . After initializing ${ w _ { u } } ^ { k }$ , Eqs. (11) and (12) are repeatedly used to calculate the final ${ w _ { u } } ^ { k }$ until the stopping criteria are satisfied.

## 3.2.3. Researcher recommendation based on meta paths

After calculating weight of meta paths, the next step is to make personalized recommendations. The basic principle of recommendation is that target researchers tend to be interested in interacting with other researchers who are similar to them, especially those who are similar to them through important meta paths which the target researchers emphasize. We use recommendation scores to reflect users' similarity through important meta paths. For a target researcher, his/her potential scholar-friends are recommended based on recommendation score. Researchers who are already scholar-friends of a target researcher are removed from the candidate list. The recommendation score between target and candidate researchers is calculated by integrating the following information: the predicted recommendation score of candidate researchers based on selected meta paths and the weight of these meta paths. For a target researcher and candidate scholar-friend pair, the recommendation score is generated by summing all the products of the researchers' predicted recommendation score under each meta path and the weight of every path as shown in Eq. (13).

$$
S c o r e _ {u, v} = \sum_ {k} w _ {u} ^ {k} \widehat {Y} _ {u, v} ^ {k}\tag{13}
$$

For each target researcher, all candidate researchers are sorted based on their recommendation scores and recommendations are made accordingly.

![](/api/attachments/TQG38ARG/fulltext/images/603f74cd4d361f1f4eb92bb7853057e9e98e0417a13f10a8686900a6273986b6.jpg)  
Fig. 3. Algorithm for personalized weight learning.

## 4. Implementation and evaluation

## 4.1. Platform introduction

ScholarMate is an online academic community; its main webpage is shown in Fig. 4. Its mission is to construct an online platform for researchers, especially researchers in China, to communicate and collaborate with each other. Currently, there are > 3.6 million researchers using this platform to support their research activities. ScholarMate allows registered researchers to build their profiles which may contain information like their name, educational background, working experiences, researcher papers, and projects. Diferent from other online academic communities, ScholarMate allows researchers to conduct federated search from bibliographic databases, e.g., CrossRef, ISI, and Scopus. Researchers only need to confirm the collected results by a simple click. The confirmation process makes the results more reliable and relieves the name ambiguity problem. On ScholarMate, researchers can invite other researchers to become their scholar-friends and build academic relationships accordingly. Moreover, researchers can discover and share academic knowledge (e.g., publications, projects, initial research results, and drafts) with other members, and receive comments and suggestions from their peers. Researchers with similar interests can collaborate via self-organized special interest group (SIG) functions and use discussion boards, online chatting, document repository, and Internal e-mail for interaction. From the point of view of academic relationship management, the platform allows researchers to build social relationships with others and even foster the co-authoring of academic papers. From the point of view of academic knowledge management, via ScholarMate, researchers can be aware of others' works and share academic knowledge with their peers. From the point of view of social influence, demonstrating researchers' outputs on ScholarMate may help researchers build academic reputation and disseminate their research results.

![](/api/attachments/TQG38ARG/fulltext/images/bb4382e6a74ec317bddb5bf32c8d9fe4793661f9e51ea877a2d46dab9e3c70e4.jpg)  
Fig. 4. The main webpage of ScholarMate

## 4.2. Baseline approaches and evaluation methods

To evaluate the performance of the proposed scholar-friend re commendation approach, we compared our approach to other two baseline approaches which were capable of taking advantage of net work information.

## 4.2.1. MF (matrix factorization)

The main idea of matrix factorization is to map interactions of entities to a joint latent factor space [51]. Particularly in this context, matrix factorization attempts to model researchers' scholar-friend re lationship to a joint latent factor space of dimensionality $f ,$ such that the interactions of users are modeled as inner products in that space. Ac cordingly, each researcher r is associated with a vector $q _ { r } \in R ^ { f } ,$ , and each user u is associated with a vector $\boldsymbol { p } _ { u } \in R ^ { f } .$ . For a given researcher $r ,$ the elements of $q _ { r }$ measure the extent to which this researcher possesses those factors. For a given user $u ,$ the elements of $p _ { u }$ measure the extent of interest the user has in researchers who are high on corresponding factors. The final dot product $q _ { r } ^ { ~ T } p _ { u } ,$ represents researchers' overall interests in other researchers' characteristics. As shown in Eq. (14), factor vectors $( q _ { r }$ and $p _ { u } )$ can be learned by minimizing the regularized squared error based on the information of users' actual scholar-friend relationship with other researchers.

$$
\underset {q _ {r}, p _ {u}} {\arg \min} \sum_ {(u, r) \in f} (y _ {u r} - q _ {r} ^ {T} p _ {u}) ^ {2} + \omega (\| q _ {r} \| _ {2} ^ {2} + \| p _ {u} \| _ {2} ^ {2})\tag{14}
$$

In this equation, $\cdot f$ is the set of the $( u , r )$ pairs whose scholar-friend relationship is known. $y _ { u , \ r } = 1$ means that user u and researcher r are scholar-friends, and 0 otherwise. The parameter ω controls the extent of regularization. Then a gradient descent optimization approach can be used to solve the above equation. After calculating all factor vectors, we can have matrix P and Q. Final recommendations can be made accordingly.

## 4.2.2. RW $\begin{array} { r } { ( P _ { \alpha } ^ { 3 } ; } \end{array}$ :Approach based on random walks)

The basic principle of random walk is to rank recommended entities based on transition probabilities according to random walks between recommended entities and the target user [52]. In this scholar-friend recommendation context, a network is constructed where the nodes are researchers and links are their scholar-friend relationships. $p ^ { 3 }$ stands for the third power of the transition matrix $P = D ^ { - 1 } Y$ of a random walk, where D is the diagonal matrix of the vertex degree and Y is the adjacency matrix of the network. One candidate researcher who is not a scholar-friend of target user u can be ranked based on the probability distribution $p ^ { 3 } ( u , . )$ of the random walk at step 3, and u is the starting node. For two candidate researchers, if $p ^ { 3 } ( u , r ) > p ^ { 3 } ( u , r ^ { ' } )$ , then researcher r<sup>′</sup> is ranked higher than researcher r<sup>′′</sup>. ${ P _ { \alpha } } ^ { 3 }$ raises the transition probabilities to the power of α to improve the accuracy of the re commendation approach.

Based on these baseline approaches, two methods were used to evaluate the performance of the proposed approach from diferent perspectives: evaluation based on historical data and evaluation based on user experiment. Evaluation based on historical data assessed the performance of the proposed approach from functional perspectives, e.g., precision and recall. Evaluation based on user experiment attempted to assess the performance of the proposed approach from the perspective of users' subjective perceptions. These two methods provided a complete evaluation of the proposed approach, which might help to further understand the value of the proposed approach.

## 4.3. Evaluation based on historical data

## 4.3.1. Data description

ScholarMate as a particular online academic community provides a good platform to evaluate the proposed approach. The data collection was composed of three steps. First, 1000 researchers were randomly selected as seed researchers. Remaining researchers were found based on these seed researchers. Second, a snow ball sampling method was used to generate an initial sample along the scholar-friend network of these seed researchers, e.g., by crawling initial seeds' scholar friends and scholar-friends of scholar-friends, and so on. The data collection process continued until the crawled scholar-friends were connected to seed researchers in distance 5 along the scholar-friend network. This sample scholar-friend network was composed of large group of researchers who were connected with each other on ScholarMate, and about 31, 000 researchers were found during this stage. Third, these researchers were tracked to collect relevant information used for recommendation from two sources: information in their profiles $( \boldsymbol { \mathrm { e . g . } }$ their research interests, groups, publications, afiliations, and posted updates) and their interaction data $( \boldsymbol { \mathrm { e . g . , } }$ liking, commenting, sharing). Concerning privacy issues, sensitive information like their contact information was excluded in the dataset. The raw data was processed to satisfy the requirements of recommendation.

## 4.3.2. Evaluation metrics

Ten-fold cross validation was used to conduct the experiments: randomly divide the sets of users in the scholar-friend network into ten partitions, use nine partitions to train diferent recommendation approaches, and use one partition for approach testing. For each target user, only top k scholar-friends are recommended. In this research, two widely used metrics are employed to evaluate the performance of the three recommendation approaches: precision and recall. Pre @ K is used to measure precision, which denotes the extent to which the recommendation approach predicts scholar-friends of target users, who are their real scholar-friends in the online academic community. Recall metric Rec @ K indicates the recommendation approach's efectiveness in suggesting real scholar-friends. These two metrics are calculated as shown in follows.

$$
P r e @ K = \frac {1}{| T S |} \sum_ {r \in T S} \frac {| A F (r) \cap R M _ {k} (r) |}{k}\tag{15}
$$

$$
R e c @ K = \frac {1}{| T S |} \sum_ {r \in T S} \frac {| A F (r) \cap R M _ {k} (r) |}{| A F (r) |}\tag{16}
$$

In the above equations, TS is the set of researchers in test sample, and |TS| represents the number of researchers in test set. AF(r) represents the true scholar-friend set of target researcher r and RM (r) denotes the top − k recommended scholar-friend set of target researcher r.

## 4.3.3. Results

Tables 2 and 3 report the performance of three recommendation approaches. It is apparent that these three recommendation approaches achieve performance disparity in terms of two evaluation metrics: Pre @ K and Rec @ K. As shown in Table 2, the precision of MF at k = 5 is 0.314 which means that this recommendation approach has a 31.4% probability of suggesting appealing scholar-friends in the top − 5 recommendation list. This table shows that the proposed meta-path-based recommendation approach has the best precision (46.9% precision at k = 1, 42.8% precision at $k = 5 ,$ , and 33.2% precision at k=25). As shown in Table $^ { 3 , }$ the recall of MF at k = 5 is 0.036, which denotes that

Results of three recommendation approaches-precision.

<table><tr><td>Recommendation approaches</td><td>Pre@1</td><td>Pre@5</td><td>Pre@10</td><td>Pre@15</td><td>Pre@20</td><td>Pre@25</td></tr><tr><td>RW</td><td>0.250</td><td>0.216</td><td>0.198</td><td>0.183</td><td>0.170</td><td>0.162</td></tr><tr><td>MF</td><td>0.357</td><td>0.314</td><td>0.285</td><td>0.253</td><td>0.240</td><td>0.229</td></tr><tr><td>Meta path</td><td>0.469</td><td>0.428</td><td>0.387</td><td>0.363</td><td>0.341</td><td>0.332</td></tr></table>

Table 3  
Results of three recommendation approaches-recall.

<table><tr><td>Recommendation approaches</td><td>Rec@1</td><td>Rec@5</td><td>Rec@10</td><td>Rec@15</td><td>Rec@20</td><td>Rec@25</td></tr><tr><td>RW</td><td>0.013</td><td>0.024</td><td>0.043</td><td>0.062</td><td>0.076</td><td>0.089</td></tr><tr><td>MF</td><td>0.018</td><td>0.036</td><td>0.061</td><td>0.083</td><td>0.106</td><td>0.124</td></tr><tr><td>Meta path</td><td>0.025</td><td>0.049</td><td>0.089</td><td>0.129</td><td>0.161</td><td>0.199</td></tr></table>

![](/api/attachments/TQG38ARG/fulltext/images/0260ca6aa8c7c2f92ca6992fe4c2d4b2018a71be340c5c8da9e7f7d5599dc54b.jpg)  
Fig. 5. Comparisons of recommendation performance.

3.6% of true scholar-friends can be found in the top − 5 recommendation list. According to Table 3, the proposed meta-pathbased recommendation approach achieves the best recall (2.5% at k=1, 4.9% at k=5, and 19.9% at k=25). By integrating precision and recall information together, Fig. 5 depicts the performance of three re commendation approaches at diferent k. The results further confirm that our proposed meta-path-based recommendation approach outperforms the other two baseline approaches in terms of Pre @ K and Rec @ K metrics, followed by the MF recommendation approach.

Compared to the other two baseline approaches, the proposed meta path recommendation approach takes advantage of heterogeneous network information, especially researchers' diferent preferences toward the meta-paths. Moreover, the proposed recommendation method which is based on learning weights of meta-paths can represent researchers' interests and behavior information at a finer level of granu larity and therefore generate better results.

To further understand the meta path preference of researchers, Fig. 6 shows the weights of meta paths for the 11th, 13th and 19th researcher. The 11th researcher shows highest weight on the 4th meta path. The 4th meta path represents the relationship of Researcher $\begin{array} { r } { \stackrel { w r i t e } {  } P a p e r \stackrel { w r i t e } {  } } \end{array}$ -1 Researcher. Compared with other meta paths, the 11th researcher places more emphasis on the paper collaboration meta path, which means that the 11th researcher prefers his/ her co-authors to become scholar-friends. The 13th researcher has highest weight on the first meta path. The first meta path represents the have relationship of Researcher Research Interest Researcher  . The weight of this meta path is much higher than other meta paths, which means that the 13th researcher is likely to add researchers with similar interests as his or her new scholar-friends. From this figure, we can see that diferent from the two previous researchers, the 19th researcher doesn't demonstrate a significantly higher weight on any particular meta paths over others. In other words, this researcher doesn't show high preference of becoming scholar-friends with other researchers through particular meta paths.

## 4.4. Evaluation based on user experiment

In addition to functional metrics, recommendation approaches can be evaluated based on users' perception. Defined as the extent to which users believe the information provided to them meets their information requirements, user information satisfaction (UIS) provide some guidelines to assess the performance of recommendation approaches [53,54]. Particularly in this research, users were asked to rank the recommendation results based on their satisfaction. If users are more interested in the scholar-friends recommended to them, then they might give a higher satisfaction score to the recommended results.

Among 1000 seed researchers on ScholarMate, 55 researchers were invited to participate in the experiment. Subjects who refused to participate in the experiment or from who we cannot obtain complete experimental data were removed from the sample. The final sample used for the analysis consisted of 45 researchers. These researchers had no prior information about the recommendation approaches mentioned in this research. For each target user of these 45 researchers, we used three recommendation approaches (RW, MF and Meta-path) as mentioned in previous section to make recommendations and generated three groups of recommendation results respectively. For each approach, the top twenty researchers who were not scholar-friends of the target user were recommended. The information about which recommendation approaches were used to generate which group of recommendation results was hidden to avoid potential bias. All target users were asked to evaluate three groups of recommendation results based on a 5-point scale ranging from strong dissatisfaction to strong satisfaction (1, very unsatisfied; 3, average; 5, very satisfied). A higher score means users are more satisfied with the recommended results.

Table 4 shows the descriptive analysis results of the three recommendation approaches in terms of user satisfaction. From this table, we can see that the average satisfaction score of the proposed meta path based approach is 4.378, and the average satisfaction score of the RW and MF approach is 3.222 and 3.578 respectively. The standard deviation of the average score of the proposed approach is 0.65, and the standard deviation of the RW and MF approach is 1.491 and 1.252. The results suggest that the proposed approach has a higher average score and lower standard deviation.

Table 4 demonstrates that the proposed approach can achieve better performance in terms of user satisfaction. In order to determine whether the diferences between the proposed approach and other two approaches were significant, the following tests were performed. First, a normality test was conducted to determine whether the data was nor mally or approximately normally distributed. The Shapiro Wilk test was used based on the sample size with the results being shown in Table 5. Table 5 suggests that the values of satisfaction generated by the three recommendation approaches do not conform to a normal distribution $( p < 0 . 0 5 )$

Since the normal assumption of the data was not met, a non-parametric test was used instead of a t-test. In this research, the Mann-Whitney U test was employed to assess the diference between the proposed approach and the other two baseline approaches. The results are shown in Table 6. The test results further confirm that the proposed approach can achieve higher satisfaction scores than both the RW and MF approach at a 1% significant level. Therefore, we could conclude that the proposed approach statistically significantly outperforms the other two baseline approaches in terms of user satisfaction.

The Spearman rank correlation was employed to examine the consistency between the recommendation results made by the three approaches and users' actual satisfaction. The ranking mechanisms of user satisfaction and recommended scholar-friends are diferent. Specifically, a higher user satisfaction ranking means users are more satisfied with the recommendation results. Scholar-friends rankings are computed based on their recommendation scores. A higher scholarfriends ranking means that their recommendation scores are lower, and they have lower possibility to be recommended. To deal with this issue, two steps were used to measure the Spearman rank correlation coeficient between user satisfaction ranking and scholar-friend ranking generated by the three recommendation approaches. First, scholar-

![](/api/attachments/TQG38ARG/fulltext/images/950199ba27cdd78d7be31777d0b7e83807d921f437f053c23ef954fe1e4377f2.jpg)

have have−1 RIR represents Researcher  Research Interest  Researcher

isscholarfriendof RR represents Researcher Researcher

RGR represents Researcher $\cdot { \xrightarrow { b e l o n g t o } } G r o u p { \xrightarrow { b e l o n g t o ^ { - 1 } } }$ Researcher

write write−1 RPR represents Researcher  Paper  Researcher

belongto belongto ROR represents Researcher → Organization → Researcher

isscholarfriendot isscholarfriendof RRR represents Researcher → Researcher Researcher

RULR represents Researcher $\cdot { \xrightarrow { p o s t } } U p d a t e { \xrightarrow { l i k e ^ { - 1 } } } R$ esearcher

RUCR represents Researcher $\cdot { \xrightarrow { p o s t } } U p d a t e { \xrightarrow { c o m m e n t ^ { - 1 } } }$ Researcher

RAR represents Researcher $\xrightarrow { s h a r e } A r t i c l e \xrightarrow { s h a r e ^ { - 1 } }$ Researcher

have RIRGR represents Researcher  Research Interest

have−1 belongto belongto-1 → Researcher → Group → Researcher

Figure 6. Weights of meta paths for the 11th, 13th and 19 th researcher  
Fig. 6. Weights of meta paths for the 11th, 13th and 19 th researcher.  
Table 4  
Table 6  
Descriptive analysis results of user satisfaction.

<table><tr><td>Approach</td><td>Min</td><td>Max</td><td>Mean</td><td>S.D.</td></tr><tr><td>RW</td><td>1</td><td>5</td><td>3.222</td><td>1.491</td></tr><tr><td>MF</td><td>1</td><td>5</td><td>3.578</td><td>1.252</td></tr><tr><td>Meta-path</td><td>1</td><td>5</td><td>4.378</td><td>0.650</td></tr></table>

Results of Mann-Whitney U test.

<table><tr><td rowspan="2"></td><td colspan="2">Score</td></tr><tr><td>Meta-path vs. MF</td><td>Meta-path vs. RW</td></tr><tr><td>Mann-Whitney U</td><td>646.500</td><td>576.500</td></tr><tr><td>Wilcoxon W</td><td>1.682E3</td><td>1.612E3</td></tr><tr><td>Z</td><td>-3.212</td><td>-3.684</td></tr><tr><td>Asymp. Sig. (2-tailed)</td><td>0.001**</td><td>0.000***</td></tr></table>

<sup>⁎⁎</sup> Represents significance at $P < 0 . 0 1 .$

Table 5  
Normality test results.

<table><tr><td rowspan="2">Approach</td><td colspan="2">Shapiro Wilk test</td></tr><tr><td>Statistic</td><td>Sig.</td></tr><tr><td>RW</td><td>0.867</td><td>0.000</td></tr><tr><td>MF</td><td>0.788</td><td>0.000</td></tr><tr><td>Meta-path</td><td>0.757</td><td>0.000</td></tr></table>

<sup>⁎⁎⁎</sup> Represents significance at P < 0.001.

friend ranking was inverted. Then the Spearman rank correlation coeficient was calculated between the inverted scholar-friend ranking and the user satisfaction ranking. The results are reported in Table 7. The results indicate that the proposed meta-path based approach outperforms the other two baseline approaches by yielding a smaller estimation error.

Table 7  
Results of three recommendation approaches-Spearman rank correlation.

<table><tr><td>Approach</td><td>Spearman rank correlation (vs. actual user satisfaction)</td><td>Sig. (2-tailed)</td></tr><tr><td>RW</td><td>0.556</td><td>0.000***</td></tr><tr><td>MF</td><td>0.605</td><td>0.000***</td></tr><tr><td>Meta-path</td><td>0.708</td><td>0.000***</td></tr></table>

<sup>⁎⁎⁎</sup> Represents significance at $\mathrm { ~ P ~ } < \ 0 . 0 0 1$

## 5. Conclusions and future research

Online academic communities have become an increasingly im portant platform which facilitates scientific collaboration and knowledge sharing. Scholar-friend recommendation in online academic communities is important to expand researchers' academic circles and make them aware of others' works. Although scholar-friend recommendation is similar to expertise and friend recommendation to some extent, the recommendation purposes and contexts are quite diferent. Researchers in online academic communities have various characteristics and relationships which constitute a heterogeneous network that presents a challenge for making scholar-friend recommendations. Moreover, existing expert and friend recommendation approaches lack an eficient mechanism to explain what information should be used and how the information could be used to make recommendations. The main contribution of this research is the design and development of a heterogeneous network-based scholar-friend re commendation approach which integrates researchers' characteristic and relationship information in a systematic way. As for what in formation could be used to make scholar-friend recommendations, in formation gain is used to decide which meta paths should be included in the recommendation model. In terms of how this information could be used to make scholar-friend recommendations, a model based on regularization optimization is employed to determine the weights of meta paths for researchers. The proposed approach was evaluated using both historical data and user experiment, and experimental results show that the proposed approach outperforms other two baseline ap proaches in terms of several evaluation metrics and user satisfaction.

This research has several practical implications. Many online academic communities have been developed to help researchers manage knowledge and relationships. Recommendation methods have been used in several online academic communities to provide value-added services. For example, LinkedIn added a widget called “people you may know” to recommend potential connections, which was principally based on mutual connections [55]. As for ResearchGate, Hoang et al. [56] proposed a collaboration recommendation method that took into account previous research collaboration (e.g., collaboration time and number of co-authors) and research similarities (e.g., publications and academic events). The proposed scholar-friend recommendation approach can be adapted and adopted in online academic communities to suggest valuable resources and researchers. From a community standpoint, such value-added recommendation services can improve users loyalty toward a particular community. From a societal level, a more eficient recommendation of valuable resources and researchers may facilitate knowledge sharing and discovery.

This research also provides some directions for future research. First, for comment data, this research only used the relationship information and the content of the interaction was not included. In future research, content analysis and text mining techniques would be used to analyze the sentiment of comment data and enrich recommendation information. Second, future research could employ researchers' feedback information to improve recommendation results. Incorporating the proposed recommendation approach into real online academic community platforms will enable us to better understand users' responses to recommended scholar-friends, e.g., whether they will adopt or ignore recommendation results. Understanding why the recommendation results work or why they do not work might help us improve the recommendation approaches. Third, in this research, edges in the heterogeneous network are assumed to have the same weights. In future research. weighted information could be used to make re commendations. Fourth, although this research focuses on scholarfriend recommendation, the proposed approach can be adapted and adopted in online academic communities to provide more personalized recommendations, e.g., group recommendation, paper recommendation, and collaborator recommendation. Fifth, this research provide some guidelines to understand users' reactions toward the recommendation system. For example, the learned weights of meta paths reflect researchers' preferences toward scholar-friends. We can use meta path information to explain recommendations and find the association between researchers' preferences and their actual scholar-friend choosing behavior.

## Funding information

This work was partially supported by the National Natural Science Foundation of China (71861019, 71361017, 71640021, J1824028, M1552003, M1752008, J1424002, 71371164), Research Fund of Jiangxi Provincial Department of Science and Technology (20171ACH80019), and Strategic Research Fund of City University of Hong Kong (7004715, 9610365, 9680121).

## References

[1] Y. Dong, H. Ma, Z. Shen, K. Wang, A Century of Science: Globalization of Scientific Collaborations, Citations, and Innovations (arXiv preprint arXiv:1704.05150), (2017).

[2] E. Chung, N. Kwon, J. Lee, Understanding scientific collaboration in the research life cycle: bio- and nanoscientists' motivations, information-sharing and commu: nication practices, and barriers to collaboration, Journal of the Association for Information Science and Technology 67 (8) (2016) 1836–1848.

[3] E. Leahey, From sole investigator to team scientist: trends in the practice and study of research collaboration, Annual Review of Sociology 42 (2016) 81–100.

[4] Y. Xu, X. Guo, J. Hao, J. Ma, R.Y.K. Lau, W. Xu, Combining social network and semantic concept analysis for personalized academic researcher recommendation, Decision Support Systems 54 (1) (2012) 564–573.

[5] U. Farooq, C.H. Ganoe, J.M. Carroll, C.L. Giles, Designing for e-science: require ments gathering for collaboration in CiteSeer, International Journal of Human Computer Studies 67 (4) (2009) 297–312.

[6] C.C. Chen, S.-Y. Shih, M. Lee, Who should you follow? Combining learning to rank with social influence for informative friend recommendation, Decision Support Systems 90 (2016) 33–45.

[7] P. Serdyukov, L. Feng, A. van Bunningen, S. Evers, H. van Heerde, P. Apers, M. Fokkinga, D. Hiemstra, The right expert at the right time and place, Practical Aspects of Knowledge Management, 2008, pp. 38–49.

[8] D. Yimam-Seid, A. Kobsa, Expert-finding systems for organizations: problem and domain analysis and the DEMOIR approach, Journal of Organizational Computing and Electronic Commerce 13 (1) (2003) 1–24.

[9] L.Z. Cui, L.L. Sun, X.H. Fu, N. Lu, G.J. Zhang, Exploring a trust based recommendation approach for videos in online social network. Journal of Signal Processing Systems for Signal Image and Video Technology 86 (2–3) (2017) 207–219.

[10] K. Su, B. Xiao, B.P. Liu, H.Q. Zhang, Z.S. Zhang, TAP: a personalized trust-aware QoS prediction approach for web service recommendation, Knowledge-Based Systems 115 (2017) 55–65.

[11] F. Zhao, Y.J. Zhu, H. Jin, L.T. Yang, A personalized hashtag recommendation approach using LDA-based topic model in microblog environment, Future Generation Computer Systems 65 (2016) 196–206.

[12] S. Price, P.A. Flach, Computational support for academic peer review: a perspective from artificial intelligence, Communications of the ACM 60 (3) (2017) 70–79.

[13] M. Neshati, S.H. Hashemi, H. Beigy, Expertise finding in bibliographic network: topic dominance learning approach. JEEE Transactions on Cybernetics 44 (12) (2014) 2646–2657

[14] L. Guo, B. Jin, C. Yao, H. Yang, D. Huang, F. Wang, Which doctor to trust: a recommender system for identifving the right doctors, Journal of Medical Internet Research 18 (7) (2016) e186.

[15] M.S. Ackerman, T.W. Malone, Answer garden: a tool for growing organizational memory, Proceedings of the ACM SIGOIS and IEEE CS TC-OA conference on Ofic information systems, ACM, Cambridge, Massachusetts, United States, 1990.

[16] D.W. McDonald. M.S. Ackerman, Expertise recommender: a flexible recommendation system and architecture, Proceeding of the ACM 2000 Conference on Computer Supported Cooperative Work (CSCW′00), Philadelphia, PA, 2000, pp. 231–240.

[17] H. Fang, C. Zhai, Probabilistic models for expert finding, Advances in Information Retrieval, 2007, pp. 418–430

[18] D. Petkova, W.B. Croft, Hierarchical language models for expert finding in enterprise corpora, International Journal on Artificial Intelligence Tools 17 (01) (2008) 5–18.

[19] C.S. Campbell, P.P. Maglio, A. Cozzi, B. Dom, Expertise identification using email communications. Proceedings of the Twelfth International Conference on Information and Knowledge Management, ACM, 2003, pp. 528–531.

[20] X. Liu, W.B. Croft, M. Koll, Finding experts in community-based question-answering services. Proceedings of the 14th ACM International Conference on Information and Knowledge Management, New York, USA, 2005.

[21] O. Alhabashneh, R. Iqbal, F. Doctor, A. James, Fuzzy rule based profiling approach for enterprise information seeking and retrieval, Information Sciences 394 (2017) 18–37.

[22] K.-W. Yang, S.-Y. Huh, Automatic expert identification using a text categorization technique in knowledge management systems, Expert Systems with Applications 34 (2) (2008) 1445–1455

[23] Balog, K., Azzopardi, L., and de Rijke, M. “A language modeling framework for

expert finding,” Information Processing and Management (45:1) 2009, pp. 1–19.

[24] M. Rafiei, A.A. Kardan, A novel method for expert finding in online communities based on concept map and PageRank, Human-centric Computing and Information Sciences 5 (1) (2015) 10.

[25] A. Alam, S. Khusro, I. Ullah, M.S. Karim, Confluence of social network, social question and answering community, and user reputation model for information seeking and experts generation, Journal of Information Science 43 (2) (2017) 260–274.

[26] G.Y. Zhou, J. Zhao, T.T. He, W.S. Wu, An empirical study of topic-sensitive probabilistic model for expert finding in question answer communities, Knowledge-Based Systems 66 (Aug 2014) 136–145.

[27] D.-R. Liu, Y.-H. Chen, W.-C. Kao, H.-W. Wang, Integrating expert profile, reputation and link analysis for expert finding in question-answering websites, Information Processing and Management 49 (1) (2013) 312–329 2013/01/01/.

[28] S.L. Huang, S.C. Lin, R.J. Hsieh, Locating experts using social media, based on socia capital and expertise similarity, Journal of Organizational Computing and Electronic Commerce 26 (3) (2016) 224–243.

[29] C.-P. Wei, W.-B. Lin, H.-C. Chen, W.-Y. An, W.-C. Yeh, Finding experts in online forums for enhancing knowledge sharing and accessibility, Computers in Human Behavior 51. (2015) 325–335.

[30] G.A. Wang, J. Jiao, A.S. Abrahams, W. Fan, Z. Zhang, ExpertRank: a topic-aware expert finding algorithm for online knowledge communities, Decision Support Systems 54 (3) (2013) 1442–1451.

[31] A. Omidvar, M. Garakani, H.R. Safarpour, Context based user ranking in forums for expert finding using WordNet dictionary and social network analysis, Information Technology and Management 15 (1) (2014) 51–63

[32] M. Neshati, Z. Fallahnejad, H. Beigy, On dynamicity of expert finding in community question answering, Information Processing and Management 53 (5) (2017) 1026-1042.

[33] A. Pal, F.M. Harper, J.A. Konstan, Exploring question selection bias to identify experts and potential experts in community question answering, ACM Transactions on Information Systems 30 (2) (2012) 10.

[34] T. James, P.B. Lowry, L.G. Wallace, M. Warkentin, The Efect of Belongingness on Obsessive-Compulsive Disorder in the Use of Online Social Networks, (2017).

[35] X. Ma, J. Ma, H. Li, Q. Jiang, S. Gao, ARMOR: a trust-based privacy-preserving framework for decentralized friend recommendation in online social networks, Future Generation Computer Systems 79 (2018) 82–94 2018/02/01/.

[36] Z. Yu, C. Wang, J. Bu, X. Wang, Y. Wu, C. Chen, Friend recommendation with content spread enhancement in social networks., Information Sciences 309 (2015) 102–118.2015/07/10/

[37] Liao, H.-Y., Chen, K.-Y., and Liu, D.-R. “Virtual friend recommendations in virtua worlds,” Decision Support Systems (69) 2015, pp. 59–69.

[38] Liben, N., David, and Kleinberg, J. “The link-prediction problem for social networks,” Journal of the Association for Information Science and Technology (58:7) 2007, pp. 1019–7.

[39] S.R. Huang, J. Zhang, L. Wang, X.S. Hua, Social friend recommendation based on multiple network correlation. JEEE Transactions on Multimedia 18 (2) (2016) 287–299.

[40] G. Xu-Rui, W. Li, W. Wei-Li, Using multi-features to recommend friends on locationbased social networks. Peer-to-Peer Networking and Applications 10 (6) (2017) 1323-1330.

[41] M. Jiang, P. Cui, F. Wang, W. Zhu, S. Yang, Scalable recommendation with social contextual information. IEEE Transactions on Knowledge and Data Engineering 26 (11) (2014) 2789–2802.

[42] S. Huang, J. Zhang, D. Schonfeld, L. Wang, X.-S. Hua, Two-stage friend recommendation based on network alignment and series expansion of probabilistic topic model, IEEE Transactions on Multimedia 19 (6) (2017) 1314–1326.

[43] N. Zheng, S. Song, H. Bao, A temporal-topic model for friend recommendations in Chinese microblogging systems, IEEE Transactions on Systems, Man, and Cybernetics: Systems 45 (9) (2015) 1245–1253.

[44] F. Jiang, C.K. Leung, A.G.M. Pazdor, Big data mining of social networks for friend

recommendation, Proceedings of the 2016 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining Asonam 2016, 2016, pp. 921–922.

[45] Z.B. Wang, J.L. Liao, Q. Cao, H.R. Qi, Z. Wang, Friendbook: a semantic-based friend recommendation system for social networks, JEEE Transactions on Mobile Computing 14 (3) (Mar 2015) 538–551.

[46] Z. Yu, C. Wang, J.J. Bu, X. Wang, Y. Wu, C. Chen, Friend recommendation with content spread enhancement in social networks, Information Sciences 309 (2015) 102–118.

[47] C. Shi, Y. Li, J. Zhang, Y. Sun, S.Y. Philip, A survey of heterogeneous information network analysis, IEEE Transactions on Knowledge and Data Engineering 29 (1) (2017) 17–37.

[48] R. Burke, F. Vahedian, B. Mobasher, Hybrid recommendation in heterogeneous networks, International Conference on User Modeling, Adaptation, and Personalization, Springer, 2014, pp. 49–60.

[49] F. Vahedian, R. Burke, B. Mobasher, Multirelational recommendation in hetero geneous networks, ACM Transactions on the Web 11 (3) (2017) 15.

[50] C.-J. Lin, Projected gradient methods for nonnegative matrix factorization, Neura Computation 19 (10) (2007) 2756–2779.

[51] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommende systems, Computer 42 (8) (2009) 42–49.

[52] C. Cooper, S.H. Lee, T. Radzik, Y. Siantos, Random walks in recommender systems: exact computation and simulations. Proceedings of the 23rd International Conference on World Wide Web, ACM, 2014, pp. 811–816.

[53] D.F. Galletta, A.L. Lederer, Some cautions on the measurement of user information satisfaction, Decision Sciences 20 (3) (1989) 419–438

[54] B. Ives. M. Olson, J. BaroudiT. The measurement of user information satisfaction. Communications of the ACM 26 (10) (1983) 785–793

[55] I. Guy, I. Ronen, E. Wilcox, Do you know?:recommending people to invite into your social network, International Conference on Intelligent User Interfaces, 2009, pp. 77–86.

[56] D.T. Hoang, V.C. Tran, T.T. Nguyen, N.T. Nguyen, D. Hwang, A consensus-based method to enhance a recommendation system for research collaboration, in: N. Nguyen, S. Tojo, L. Nguyen, B. Trawiński (Eds.), Intelligent Information and Database Systems. ACIIDS 2017. Lecture Notes in Computer Science, Vol 10191 Springer, Cham, 2017.

Yunhong Xu is an Associate Professor of Information Systems at the Kunming University of Science and Technology. She received her Ph.D. in Information Systems at the City University of Hong Kong and Ph.D. in Management Science at the University of Science and Technology of China. Her research interests include network analysis, knowledg recommendation and business analytics. She has published in journals such as Decision Support Systems, Expert Systems with Applications, etc.

Duanning Zhou is a Professor in the Department of Information Systems and Business Analytics, Eastern Washington University. He received his PhD in information systems from City University of Hong Kong. His research interests include information systems, elearning, and user behavior. He has published in ACM Transaction on Internet Technology, Communication of Association for Information Systems. Group Decision and Negotiation. IEEF Transactions on Engineering Management. Information and Management. International Journal of Information Quality, Journal of Enterprise Information Management, and other journals.

Jian Ma is a Professor in the Department of Information Systems, City University of Hong Kong, He received his Doctor of Engineering degree in Computer Science from Asia Institute of Technology. Dr. Ma's research areas include decision and decision support Systems, business intelligence, research information systems, research and innovation social networks. His past research has been published in IEEE Transactions on Engineering Management, IEEE Transactions on Education, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems, Information and Management, and European Journal of Operational Research, etc.
