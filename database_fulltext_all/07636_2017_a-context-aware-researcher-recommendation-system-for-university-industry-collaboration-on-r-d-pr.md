---
otero_id: 7636
otero_key: "EGK8YU3A"
title: "A context-aware researcher recommendation system for university-industry collaboration on R&D projects"
authors: "Qi Wang; Jian Ma; Xiuwu Liao; Wei Du"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.09.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A context-aware researcher recommendation system for university-industry collaboration on R&D projects

Qi Wang <sup>a,b,</sup>⁎, Jian Ma <sup>b</sup>, Xiuwu Liao <sup>a</sup>, Wei Du <sup>c</sup>

<sup>a</sup> School of Management, The Key Lab of the Ministry of Education for Process Control and Efficiency Engineering, Xi'an Jiaotong University, Xi'an 710049, Shaanxi, China

<sup>b</sup> Department of Information Systems, City University of Hong Kong, Kowloon, Hong Kong

<sup>c</sup> School of Information, Renmin University of China, Beijing, China

## a r t i c l e i n f o

Article history: Received 24 January 2017 Received in revised form 1 September 2017 Accepted 4 September 2017 Available online xxxx

Keywords: University-industry collaboration Project collaboration Collaborator identification Context-aware recommendation

## a b s t r a c t

University-industry collaboration plays an important role in the success of R&D projects. One of the main challenges of university-industry collaboration is the identification of suitable partners. Due to the information asymmetry problem, it is difficult for companies to identify researchers from universities for collaboration on their R&D projects. Various expert recommendation systems (e.g., question responder recommenders and co-author recommenders) have been proposed, but they fail to characterize companies' needs in identifying suitable researchers. This paper proposes a context-aware researcher recommendation system to encourage universityindustry collaboration on industrial R&D projects. The system has two modules: an offline preparation module and an online recommendation module. In the offline preparation module, candidate researchers are identified in advance to improve the efficiency of the context-aware recommendation. In the online recommendation module, contextual information (i.e., R&D projects) is captured from a social network platform, and then, candidate researchers are recommended based on a contextual trust analysis model, which combines the expertise relevance, quality, and trust relations of researchers to profile and evaluate candidate researchers for the R&D project collaboration. An offline experiment and a user study are conducted to evaluate the effectiveness of the proposed recommendation system. The results show that the proposed method achieves better performance than the baseline methods.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

University-industry collaboration is very important for research and innovation in a knowledge-based society [9,22,23]. Local governments have designed various policies to encourage open innovation and university-industry collaboration [11]. With industries' pressing needs for frontier technologies, university-industry collaboration on industrial R&D projects is widespread in practice and is significantly valuable to both parties [21]. However, it is a challenging task for companies to select suitable researchers as collaboration partners from universities because of the information asymmetry problem. For example, companies find it difficult to search for research output from different sources in order to understand a researcher. With the high potential risk of R&D projects, the information asymmetry problem could also lead to mistrust between researchers and companies, which further hinders university-industry collaboration.

Prior research has explored the incentives to encourage universityindustry collaboration [6,8,9,14,21,22], but this paper studies university-industry collaboration from the perspective of partner selection with the support of an expert recommendation system. Expert recommendation systems have been widely explored for various applications, including responder recommendation systems in online Q&A communities [34], expert finding systems for knowledge management in organizations [37], researcher recommendation systems for coauthor seeking [30] and reviewer assignment systems for project management [29]. However, current expert recommendation systems can hardly meet the need of recommending researchers for industrial R&D projects. The aforementioned recommendation systems mainly analyze the expertise and social relations of the experts available for recommendation, but they lack capacity to profile companies' need for experts and identify researchers for R&D project collaboration.

In this paper, a context-aware recommendation system is proposed to recommend researchers for industrial R&D projects. The proposed context-aware recommendation system captures contextual information from a social network platform, and then, proactively recommends researchers to inspire university-industry collaboration. We adopt a hybrid recommendation strategy and design two modules for the system. The offline preparation module provides two candidate selection strategies and selects candidate researchers at the backend to improve the efficiency of the context-aware recommendation. The online recommendation module captures companies' contexts and identifies suitable researchers from the corresponding candidate sets. In this paper, three important aspects of researchers, i.e., expertise relevance, quality, and trust relations, are introduced to profile and analyze researchers as collaboration partners [6,21,22]. A contextual trust analysis model is proposed to combine the three aspects and evaluate the candidate researchers for recommendation.

An offline experiment and a user study are conducted to evaluate the effectiveness of the proposed recommendation method in comparison with the baseline methods, i.e., the content-based method, the social network-based method, and the sum method (defined in Section 4.3). The experiment results show that the proposed method achieves higher recommendation accuracy than the content-based method and the sum method, and it also performs better than the social network-based method in terms of recommending collaborators who have not collaborated with the companies in the past (i.e., new collaborators). Researchers suggested by the proposed recommendation system have higher relevance and quality values than that selected by companies without recommendation systems. In addition, the results of the user study show that the proposed method obtains a higher average rating than the baseline methods.

The remainder of this paper is organized as follows. Section 2 reviews related work in recommendation systems and universityindustry collaboration. Section 3 presents the framework of the proposed recommendation system. Section 4 introduces the experiment design for evaluation with an offline experiment and a user study and Section 5 provides the results. The contributions and limitations of the research are summarized in Section 6.

## 2. Related work

This study designs a researcher recommendation system to promote university-industry collaboration. We review recommendation systems with a focus on expert recommendations, and investigate universityindustry collaboration research to define the evaluation criteria for researcher recommendation.

## 2.1. Recommendation systems

Recommendation systems are widely used in online platforms to help users identify items of interest, e.g., products, courses, services, experts and so on [24]. Lu et al. made a comprehensive review of the applications of recommendation systems and the related techniques used in different application contexts [19]. In addition to recommendation systems for individual users (e.g., tourism service recommendation systems [1]), group recommendation systems are designed to recommend items for a group of users [35]. For expert recommendation systems, current recommendation methods can be classified into three types, i.e., content-based methods, collaborative filtering methods and hybrid methods.

Content-based (CB) methods employ text-mining techniques to extract keywords from associated documents (e.g., browsed articles and published articles) and use the extracted keywords as features to define the expertise of users [17,29,30,34]. The vector space model is widely used to profile the expertise of experts by a list of keywords with importance weights [29,34]. However, content-based methods usually suffer from a high calculation cost when there are enormous documents to be analyzed for profiling and the vector space is getting large.

Collaborative filtering (CF) methods construct a user-item rating matrix based on users' browsing, viewing, and searching behaviors [4]. Similar users are identified for recommendations according to their past behaviors instead of analyzing the content of the associated documents. With the wide use of social networks, social relations are employed in recommendation systems to ease the data sparsity problem [20]. Social network-based recommendation systems recommend users who have strong social relations (e.g., friendship and coauthorship) with the target user based on the assumption that users with social proximity have similar interests [7,28]. Liben-Nowell and Kleinberg conducted an experiment to compare several proximity measures in a co-author network, where Katz's approach performs best in co-authorship prediction [18]. However, one critical concern about CF and social network-based methods is that they could identify irrelevant experts in different domains.

Hybrid methods are proposed to make use of the advantages of content-based methods and collaborative filtering methods. Wang et al. proposed a new algorithm to identify suitable responders for unsolved questions in online Q&A communities [34]. The new algorithm combines content-based expertise analysis and social network-based authority analysis to make suggestions. Li et al. combined semantic similarity and social relations for recommendations to improve knowledge sharing in online forum communities [16]. A research analytical framework (RAF) was proposed to recommend researchers for project selection [29]. The RAF extends the content-based approach and social network approach with the extension of quality analysis, and it also has been applied for expert identification in scientific communities [30]. Previous hybrid methods mainly combine content-based methods and social network methods by using weighted aggregation techniques. In this paper, we use a hybrid recommendation strategy and propose a contextual trust analysis model for the context-aware researcher recommendation system.

## 2.2. University-industry collaboration

University-industry collaboration is a challenging topic not only academically but also practically. Universities are requested to transfer knowledge to local industries, and industries are under pressure to upgrade their technologies to become competent in global markets [10]. Current research focuses on the influence of university-industry collaboration [10,11], the motivations and incentives of researchers for collaboration with industries [8,14], collaboration channels and their differences [9], and factors that influence the collaboration engagement and collaboration performance [3,21].

This paper concentrates on the factors that influence the engagement and performance of university-industry collaboration, especially with a focus on researcher partner selection. Influence factors determine the possibility that a researcher could work with companies. De Fuentes and Dutrénit summarized the influence factors from multiple perspectives. They found that the characteristics of researchers (e.g., age, work experience, research fields and academia status) have an influence on their engagement with industries [9]. Perkmann et al. found that the researcher quality is an important factor that influences the involvement of industries in collaboration with researchers [21]. Perkmann et al. summarized the determinants of researchers in collaborating with industries from individual, organization and institution levels [22]. They found that researchers' productivity and success in academic articles and research projects positively affect their engagement with the industries. Success factors influence the collaboration performance, which in turn affect the collaborator selection of companies for future collaboration. Barnes et al. explored the success factors of university-industry collaboration and identified several important characteristics of collaboration partners, including trust, good personal relationships and collaborative experiences [3]. Prior collaboration experiences and trust can reduce the barriers of collaboration, e.g., differences in the orientation and conflicts over the intellectual property [6].

The research findings provide solid foundations to define the criteria for researcher recommendation, i.e., expertise relevance, quality and trust relations. In this paper, the expertise relevance of researchers to R&D projects is analyzed based on the domain of the projects and the expertise of the researchers. The quality of researchers is defined based on their productivity in academic articles, projects, and patents. Trust relations are derived based on the previous collaboration experiences of the researchers with the companies.

## 3. The proposed recommendation system

This study proposes a context-aware researcher recommendation system for university-industry collaboration on industrial R&D projects. The context is defined as the projects of companies that are in need of external experts. For example, when a company obtains a government-funding project or establish a project for advanced technologies, the company may need external researchers from universities as collaborators for higher success rate. The system employs an offline module for candidate selection and an online module for the contextaware recommendation. Fig. 1 depicts the framework of the contextaware recommendation system. The offline module employs two strategies for candidate researcher identification. It identifies a set of candidate researchers for each company in advance to improve the efficiency of the online recommendation. The online recommendation module identifies suitable collaborators for companies from the prepared candidate sets once the system captures their R&D projects that are in need of experts, where candidate researchers are analyzed based on a contextual trust analysis model.

## 3.1. Offline preparation module

To improve the efficiency of online recommendation, this module produces a set of candidate researchers for each company offline. Two strategies are used for the candidate selection, where collaborators of collaborators are identified in Strategy I, and collaborators of similar companies are identified in Strategy II.

## 3.1.1. Strategy I: collaborators of collaborators

A heterogeneous social network (HSN) is built to describe the relations between companies and researchers. Fig. 2 illustrates the heterogeneous social network. The nodes are researchers or companies and the relationships are extracted from their academic activities, including co-authoring academic articles, co-participating in projects and coinventing patents. The edge exists if the two nodes have collaborations in terms of articles, projects, or patents. The connections of researchers can be seen as evidence that the researchers are amenable to collaboration.

In social network-based recommendation systems, it is known that users have relevant knowledge or similar interest to the users who are connected with them [36]. In this strategy, researchers who have direct links with the target company are first identified as candidate researchers, and they compose the set of “Direct Collaborators”, represented as DC. For example, the DC of company a in Fig. 2 is composed of researcher 1, researcher 2, researcher 3 and researcher 4. By inference, the collaborators of a user's collaborators are more likely to have relevant domain knowledge in comparison with a randomly selected one. Then researchers who have connections with researchers in the DC are selected to compose “Candidate Set 1”, represented as CS1. For example, researcher 5, researcher 6, researcher 7, researcher 8, researcher 9 and researcher 10 compose the CS1 of company a. These researchers are selected as candidate researchers for further analysis.

## 3.1.2. Strategy II: collaborators of similar companies

Collaborators of similar companies could have expertise to solve the target company's problem. We first analyze the similarity between companies and then identify researchers who have collaborated with similar companies as candidates.

The basic profiles of companies are defined based on their patents, articles, and projects. Keywords are extracted from the companies' documents to represent their technology domains, and a vector space model is used to index the extracted keywords with frequencies [2]. Tokenization including segmenting (i.e., separating words) and removing stop words (e.g., of, the, and, them, who, that), and normalization including case folding (i.e., converting all words to lower case) and stemming (i.e., reducing inflected words to their stem or root form) are necessary to process the keywords for indexing [32]. The basic profile of a company is represented as $\langle ( b K e y _ { 1 } , b T F _ { 1 } ) , ( b K e y _ { 2 } , b T F _ { 2 } ) , . . . , ( -$ $b K e y _ { n } , b T F _ { n } ) \rangle$ , where bKey<sub>i</sub> represents the i-th keyword and bTF<sub>i</sub> represents its corresponding weight. The weight is calculated by dividing the cumulative occurrence frequency of bKey in the company's documents by the total number of keywords in these documents.

![](/api/attachments/EGK8YU3A/fulltext/images/9c2a6abf3ab29df2329d165cb2ff24a19893741f488d2d8a3e6132cfd747fb8b.jpg)  
Fig. 1. Framework of the proposed recommendation system.

Please cite this article as: Q. Wang, et al., A context-aware researcher recommendation system for university-industry collaboration on R&D projects, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.001

Q. Wang et al. / Decision Support Systems xxx (2017) xxx–xxx

![](/api/attachments/EGK8YU3A/fulltext/images/99bfe81130be8bbd14628924370e2ebd8aab98d1b3d536fbb02f54a540dcb13c.jpg)  
Fig. 2. An illustration of the heterogeneous social network

The cosine value is the most popular similarity measurement of term vectors [29,34]. We measure the similarity between company c and company c’ by calculating the cosine value of their basic profile vectors.

$$
S I M _ {c c ^ {\prime}} = \frac {\sum_ {k = 1} ^ {n} b T F _ {c k} \cdot b T F _ {c ^ {\prime} k}}{\sqrt {\sum_ {k = 1} ^ {n} b T F _ {c k} ^ {2} \cdot \sum_ {k = 1} ^ {n} b T F _ {c ^ {\prime} k} ^ {2}}}\tag{1}
$$

where k is keyword index in the vectors, $b T F _ { c k }$ represents the weight of the k-th keyword in the basic profile of company c, and $b T F _ { c ^ { \prime } k }$ represents the weight of the k-th keyword in the basic profile of company c′.

For each company, the top K most similar companies are selected as neighbor companies. Researchers who have connections with neighbor companies compose “Candidate Set 2”, represented as CS2. For example, if company c is a neighbor company of company a in Fig. 2, then its collaborators, e.g., researcher 13 and researcher 14, will be selected to compose the CS2 of company a. The candidate researchers in CS2 will be evaluated for recommendation.

## 3.1.3. Candidate set

The n-step collaborator is defined as the researcher who is linked with an entity in n steps in a social network, i.e., HSN. Specifically, DC represents direct collaborators of the target company that are 1-step collaborators of the target company, and CS1 contains collaborators of the target company's direct collaborators that are 2-step collaborators of the target company. Collaborators of neighbor companies are 1-step collaborators of the neighbor companies and compose CS2. If necessary to consider more researchers for recommendation, CS1 can be expanded by adding n-step (n≥3) collaborators of the target company, e.g., adding researcher 11 that is a 3-step collaborator of company a, and CS2 can be expanded by adding n-step (n≥2) collaborators of neighbor companies, e.g., adding researcher 12 that is a 2-step collaborator of company c. The nal candidate set, labeled as CS, is the union of CS1, CS2, and DC. The system prepares candidate sets in advance in such a way that the online recommendation module can recommend researchers efficiently when capturing the context information of companies.

Notably, previous collaborators of companies are considered as candidate researchers for recommendation because they are more likely to have relevant domain knowledge and gain trust than other unknown researchers. Additionally, the system is designed to identify relevant collaborators for companies' projects to inspire collaboration, and companies can choose to collaborate with prior collaborators if they are qualified for the new R&D projects.

## 3.2. Online recommendation module

The online recommendation module captures the contexts of companies, i.e., the R&D projects that are in need of external experts, from online social networks, and then, it evaluates candidate researchers in the given context for recommendation. The following subsections introduce the capturing and profiling of the contextual information and then explain the evaluation model for researcher recommendation.

## 3.2.1. Context analysis

There are various definitions of context across different applications, such as locations, emotions and surrounding objects [12]. With contextual information, recommendation systems know the current preferences of users and make recommendations adaptively. In this research, it is crucial to know companies' need for external experts to make suitable recommendations. Companies have different requirements for collaborators for different R&D projects. Therefore, the R&D projects of companies that are in need of external experts are regarded as the companies' contexts, for which recommendations are generated. We define the context profiles of companies based on their R&D projects that are in need of external experts and extract keywords from the textual information of the projects. The vector space model is used to index the extracted keywords. The context profile of a company is represented as $\langle ( c K e y _ { 1 } , c T F _ { 1 } ) , ( c K e y _ { 2 } , c T F _ { 2 } ) , . . . , ( c K e y _ { n } , c T F _ { n } ) \rangle$ , where cKey represents the i-th keyword, and cTF is the corresponding weight of cKey . The weight is calculated by dividing the occurrence frequency of cKey in the project of the company by the total number of keywords in the project. According to the contexts of companies, the candidate researchers are evaluated based on a contextual trust analysis model.

The contexts of companies can be captured from online social networks. With a wide use of social network platforms, companies leverage the platforms as important channels to disseminate information, such as publishing R&D projects to demonstrate their technology achievement and attract researchers for collaboration. These are the sources to capture the contexts of companies from social network platforms. For example, companies can build homepages on ResearchGate to disclose their members, publications, and patents and publish recruitment information to attract researchers to join in them. ScholarMate encourages users to publish their R&D projects and provides a recommendation service for the users to find potential collaborators. The context-aware recommendation system can capture the context of companies from such social networks and suggest suitable researchers to inspire universityindustry collaboration. As shown in Fig. 3, the title and abstract of the project are regarded as the contextual information, and the system extracts a set of keywords from the project information, which can be seen as the context profile. Users can improve the context profile for more accurate recommendations by adding or removing keywords. A set of researchers are suggested for the given project by matching the context profile and researcher profiles.

Q. Wang et al. / Decision Support Systems xxx (2017) xxx–xxx  
![](/api/attachments/EGK8YU3A/fulltext/images/6f75c4af69cc837dab0ff28c2a516f60f63638d92cbaa249e4a20e20d0cf7aa1.jpg)  
Fig. 3. An illustration of the context-aware recommendation.

## 3.2.2. Researcher evaluation

A contextual trust analysis model, that combines expertise relevance, quality, and trust relations of researchers, is proposed to evaluate researchers for recommendation. The contextual relevance and quality of researchers are first analyzed to obtain their contextual authority, and then, the researchers' contextual authority and trust relations are integrated based on the proposed model.

3.2.2.1. Contextual relevance analysis. The contextual relevance evaluates whether a researcher has domain knowledge in the given context. The expertise of researchers is profiled according to their associated documents, including articles, patents, and projects. The vector space model is used to index the keywords that are extracted from the documents of researchers. Then, the profile of a researcher can be represented as $\langle ( r K e y _ { 1 } , r T F _ { 1 } ) , ( r K e y _ { 2 } , r T F _ { 2 } ) , . . . , ( r K e y _ { n } , r T F _ { n } ) \rangle$ , where rKey represents the i-th keyword, and $r T F _ { i }$ is the corresponding weight of rKey . The weight is calculated by dividing the cumulative occurrence frequency of rKey in the researcher's documents by the total number of keywords in these documents. The contextual relevance is measured by the cosine similarity between the researcher profile and the context profile. $R E L _ { r c }$ represents the expertise relevance of researcher r to the context of company $c ,$ which is computed as

$$
R E L _ {r c} = \frac {\sum_ {k = 1} ^ {n} c T F _ {c k} \cdot r T F _ {r k}}{\sqrt {\sum_ {k = 1} ^ {n} c T F _ {c k} ^ {2} \cdot \sum_ {k = 1} ^ {n} r T F _ {r k} ^ {2}}}\tag{2}
$$

where $r T F _ { r k }$ represents the weight of the k-th keyword in the profile of researcher $r ,$ and $c T F _ { c k }$ represents the weight of the k-th keyword in the context profile of company c.

3.2.2.2. Quality analysis. The quality of researchers is measured by their achievements which represent the ability of researchers. In this paper, the quality of researchers is analyzed with respect to three aspects, i.e., academic articles, patents, and research projects [21,22,29]. Adapting from Silva et al. [29], the quality of researcher r in terms of academic articles is measured as

$$
\text { article } _ {r} = \omega_ {A} \cdot Q _ {r A} + \omega_ {B} \cdot Q _ {r B} + \omega_ {C} \cdot Q _ {r C} + \omega_ {D} \cdot Q _ {r D}\tag{3}
$$

where $\omega _ { A } , \omega _ { B } ,$ ω and $\omega _ { D }$ are the weights of different journal levels and $Q _ { r A } , Q _ { r B } , Q _ { r C } \mathrm { a n d } Q _ { r D }$ are the quantity of articles published by researcher r in journals of the corresponding levels. We introduce Journal Citation Reports (JCR), which is issued by the Intellectual Property and Science business of Thomson Reuters, to define the journal levels. For example, the top 25% journals with the highest impact factors (IFs) are classified into the A level, journals of which the IFs are ranked between 25% and 50% will be classified into the B level, and so on.

The patent quality is introduced to evaluate researchers' quality in the patent aspect. Multiple indicators are identified for patent quality analysis [15,31]. In this paper, the forward citations and backward citations are used as quality indicators. Then, the performance of researcher r in the patent aspect is measured as

$$
\text { patent } _ {r} = \sum_ {p \in \text { patset } _ {r}} \left(f c _ {p} + b c _ {p}\right)\tag{4}
$$

where $p$ is the index of the patent, patset is the set of patents of researcher $r , b c _ { p }$ is the number of patents cited by patent p and $f c _ { p }$ represents its forward citations. To ease the anti-recency issue that old patents have a long time to accumulate forward citations and recent patents usually have few forward citations, the count of the forward citations of a patent is measured by the number of citations it received within the first five years from its publication [15,33]. Citations that are received soon after a patent's publication could influence its future citations and reflect its quality [15,33]. For the patents published within 5 years, we predict their forward citations by

$$
f c _ {p} = \log_ {2} (7 - y) \cdot f c _ {p} ^ {\prime}\tag{5}
$$

where $f c _ { p } ^ { \prime }$ represents the citations that paten $\boldsymbol { \cdot p }$ received since its publication, and y ranges from 1 to 5 and represents the number of years from the patent's publication.

In the project aspect, the number of projects, which is defined as project , is used to measure the researcher's quality. Then the quality of researcher r is calculated as

$$
\mathrm{QUA} _ {r} = \alpha \cdot \text { article } _ {r} + \beta \cdot \text { patent } _ {r} + \gamma \cdot \text { project } _ {r}\tag{6}
$$

where article , patent and project are scaled into [0, 1], and $\alpha , \beta$ and γ are the weights assigned to them $( \alpha + \beta + \gamma = 1 )$ . Given the context of company $c ,$ the contextual authority of researcher $\mathsf { \Gamma } ( \mathrm { i } . \mathsf { e } . , A U T _ { r c } )$ is measured based on the contextual relevance and quality of the researcher.

$$
A U T _ {r c} = \sqrt {R E L _ {r c} \cdot Q U A _ {r}}\tag{7}
$$

3.2.2.3. Contextual trust analysis. The trust is seen as a measurement of A's confidence in B that B will behave in A's expected manner [5]. In this study, trust relations between researchers and companies are extracted from previous collaboration activities, e.g., collaborating in R&D projects, papers or patents. The collaboration network is regarded as a proxy of the trust network. Trust contributes to collaboration and in turn, the collaboration brings trust to collaborators. Based on the properties of trust, including asymmetric, propagative, context-specific, and composable [27], a contextual trust analysis model is proposed to evaluate candidate researchers in a given context.

In the trust network, edge $e _ { i j }$ exists if node i and node j have collaborations in terms of academic articles, patents or projects. The trust strength of node i in node j is quantified as the ratio of documents that are collaboratively published by node i and node j to the total documents associated with node $i ,$ which is calculated as

$$
w _ {i j} = \left| U _ {i} \cap U _ {j} \right| / \left| U _ {i} \right|\tag{8}
$$

where $U _ { i }$ and $U _ { j }$ represent the set of associated documents $( { \mathrm { i . e . } }$ , articles, projects and patents) of node i and node j respectively. The higher the ratio is, the more trust node i has in node j. The trust that node i has in node j can be different from the trust that node j has in node i, which means that the trust relation is asymmetric.

Propagation means that trust information can be passed from one user to another [27]. For example, if there is no direct relationship between node i and node j and node k is a bridge node, then node i can derive an amount of trust in node j, and the trust strength is determined by how much node i trusts node k and how much node k trusts node j. Assuming that company c and researcher r are connected through the bridge nodes $( k _ { 1 } , k _ { 2 } , . . . , k _ { i } , . . . , k _ { n } )$ , then the trust chain can be represented as ${ \mathsf { c } } \to k _ { 1 } \to . . . \to k _ { i } \to . . . \to k _ { n } \to r ,$ , and the contextual trust that researcher r obtains from company c through this trust chain is computed as

$$
P T _ {c r} ^ {k _ {1}, k _ {2},.., k _ {n}} = M e t a \_ T _ {c k _ {1}} \cdot M e t a \_ T _ {k _ {1} k _ {2}} \dots \dots M e t a \_ T _ {k _ {n} r}\tag{9}
$$

$$
M e t a _ {-} T _ {i j} = \left(1 + A U T _ {j c}\right) ^ {w _ {i j}} - 1\tag{10}
$$

where Meta\_T represents the propagated trust along each trust propagation path, e.g., $c  k _ { 1 } , k _ { i }  k _ { i + 1 }$ and $k _ { n } \to r$ in the trust chain, and it is computed by Eq. (10). Meta ${ } _ { T _ { i j } }$ represents the contextual trust that node j obtains from node i, which is computed based on the trust strength of node i in node $\mathrm { ~ \ i ~ } ( \mathrm { i . e . , } w _ { i j } )$ , as well as the contextual authority of node j $( \mathrm { i } . \mathsf { e } . , A U T _ { j c } )$ because trust relation is context-specific [27]. If node i completely trusts node j, then the contextual trust that node j obtains from node i is equal to its own contextual authority. Otherwise, the contextual authority of node j is discounted by the relation strength between these two nodes. Specially, we add edges between the target company and its neighbor companies, and define the corresponding propagated trust values as their similarity scores, which are computed by Eq. (1), so that there is at least one trust chain that connects the company and its candidate researchers in CS2, where the neighbor companies act as bridge nodes.

There can be several trust chains that connect researcher r and company c. Composability denotes that the trust information can be composed if there is more than one trust chain. The weighted mean aggregation method, which has shown robustness in trust inferences [25], is used to compose the trust.

$$
C P T _ {c r} = \frac {\sum_ {T C _ {l} \in \text { TrustChain } (c \rightarrow r)} P T _ {c r} ^ {k _ {1} , k _ {2} , . . . , k _ {n}} \cdot W (T C _ {l})}{\sum_ {T C _ {l} \in \text { TrustChain } (c \rightarrow r)} W (T C _ {l})}\tag{11}
$$

$$
W (T C _ {l}) = (\mathrm{MTCL} - T C L _ {l} + 1) / \mathrm{MTCL}\tag{12}
$$

where TrustChain (c→r) represents the set of trust chains that connect researcher r and company $c , T C _ { l }$ is one of the trust chains and $( k _ { 1 } , k _ { 2 } , . . . , k _ { i } , . . . , k _ { n } )$ is the series of bridge nodes in TC that connect company c and researcher r. $W ( T C _ { l } )$ is the weight of $T C _ { l }$ as measured by Eq. (12), where MTCL is the threshold to control the maximum distance of propagation, and $T C L _ { l }$ is the length of $T C _ { l } .$ The longer the chain is, the lower the weight is. Trust chains of which the length is larger than MTCL will not be considered. The top N researchers with the highest contextual trust values are recommended for the project of the company.

## 4. Experiment design

An offline experiment and a user study are conducted to demonstrate the effectiveness of the proposed context-aware recommendation system. The following subsections introduce the design of the experiments.

Please cite this article as: Q. Wang, et al., A context-aware researcher recommendation system for university-industry collaboration on R&D projects, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.001

```txt
Zhi Qiang Fan
City University of Ho...
Add Friend
```  
SCI/SSCI Publications

## 4.1. Description of offline experiment

## 4.1.1. Experiment data of offline experiment

For the offline experiment, we collected data from ScholarMate, where users can build homepages to disclose their publications, projects, and patents (e.g., Fig. 4). In this experiment, 130 companies are randomly selected and all of them have at least one collaborative article, patent or project with academic researchers. Taking the cost and maneuverability of the experiment into account, approximately 100,000 researchers are randomly selected for recommendation and they have connections with the sample companies in four steps. The projects, articles, and patents of the sample companies and researchers during 2011–2015 are collected for the experiment. The articles, patents, and projects published during 2011 and 2014 are used to analyze the basic profiles of the companies and the profiles of the researchers. There are 2373 collaborative articles, patents, and projects of companies

![](/api/attachments/EGK8YU3A/fulltext/images/6b0adb1fb09d976350cc386ac2176c5faefcb56c7f2e9ce3f50f79197f1dc831.jpg)  
H-index (SCI/SSCI)

## Work Experience

![](/api/attachments/EGK8YU3A/fulltext/images/ea46f01903efc02d75168ed6ef7aab435892efe0c8456e9c70322b39eb057991.jpg)

![](/api/attachments/EGK8YU3A/fulltext/images/d2e536d5d3cb3ca5e98fdf356ec26242a6222673ce3ed72d05e0a5bf27ed4b02.jpg)

## Publications

![](/api/attachments/EGK8YU3A/fulltext/images/a6bcab241fa27b266e2f49db359bc2809c5327eca8fd65ca266a5d6b6e02bb1c.jpg)

```txt
Like(2) Share(1) Comment Save Full text
```

```txt
Like Share Comment Save Full text
```

3/2016.

```txt
wen chen
IRIS Systems (Shenzh..
+ Add Friend
```

Jing WANG

## >> More Publication

## Projects

```txt
Like(2) Share Comment
```

```txt
Like(2) Share Comment
```

Fig. 4. An example of researcher homepages on ScholarMate.

Please cite this article as: Q. Wang, et al., A context-aware researcher recommendation system for university-industry collaboration on R&D projects, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.001

in 2015, which are denoted by target projects in the following sections. Recommendations are generated for the target projects. The textual information of these target projects is used to build the companies' context profiles and their collaborators are used to compose the corresponding test sets for recommendation evaluation.

## 4.1.2. Evaluation metrics of offline experiment

In the offline setting, the recommendation accuracy is used to evaluate the performance of recommendation methods. Three measurements are widely used, i.e., the precision, recall and F-value. They are calculated as

$$
\text { precision@N } = | R S @ N \cap T S | / N\tag{13}
$$

$$
\text { recall@N } = | R S @ N \cap T S | / | T S |\tag{14}
$$

$$
\mathrm{F@N} = \frac {2 \cdot \text {precision@N} \cdot \text {recall@N}}{\text {precision@N} + \text {recall@N}}\tag{15}
$$

where RS@N is used to represent the set of the top N recommended researchers for a target project and TS represents the corresponding test set, which is composed of the actual collaborators of the target project. Precision represents the proportion of top N recommendations that were actual collaborators of the corresponding project. Recall measures the fraction of actual collaborators that are identified by the recommendation method. F-value is to find a trade-off between precision and recall.

## 4.1.3. Candidate sets of offline experiment

The candidate selection strategies are used to produce candidate sets. Candidate sets are evaluated by candidate coverage, which measures the proportion of actual collaborators that are identified by the candidate selection strategies. The coverage is calculated as

$$
\text { candidate   coverage } = | \text { CSNUTS } | / | \text { UTS } |\tag{16}
$$

where CS represents the candidate set for a company and UTS represents the union set of the actual collaborators of the company's target projects. In this section, the step size (i.e., n) and the number of similar companies (i.e., K) for candidate selection are determined by analyzing the coverage and size of candidate sets.

Analysis of DC and CS1: Table 1 lists the average coverage and size of the candidate sets obtained by Strategy I. When n equals one, the candidate set contains the direct collaborators of the companies (i.e., DC), the average candidate set size is approximately 400, and its coverage is approximately 0.38. When n equals two, the candidate set contains direct collaborators (DC) and direct collaborators' collaborators (CS1). CS1 has 2322 candidates, and its coverage is approximately 0.14. The size of the union of CS1 and DC increases to 2731, and the coverage reaches 0.52. However, with the further increase in n, the size of CS1 increases rapidly, but the coverage has a small increment. For example, when n equals three, CS1 is extended with three-step collaborators and size of CS1 increases by more than ten thousand researchers, while the coverage increases by only 0.05.

Analysis of CS2: Table 2 lists the average coverage and size of CS2 obtained by Strategy II. In Table 2, when K increases, the average coverage of CS2 also increases and the size of the candidate set becomes larger. However, the coverage value is not very high (approximately 0.3) even though 17,000 researchers are selected in the candidate set. This

Table 1  
The coverage and size of the candidate sets obtained by Strategy I.

<table><tr><td>n</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Candidate coverage</td><td>0.38</td><td>0.52</td><td>0.57</td><td>0.63</td></tr><tr><td>Candidate set size</td><td>409</td><td>2731</td><td>13,182</td><td>23,433</td></tr></table>

## Table 2

The coverage and size of the candidate sets obtained by Strategy II.

<table><tr><td rowspan="2">n</td><td colspan="5">Candidate coverage</td><td colspan="5">Candidate set size</td></tr><tr><td>K = 1</td><td>K = 2</td><td>K = 3</td><td>K = 4</td><td>K = 5</td><td>K = 1</td><td>K = 2</td><td>K = 3</td><td>K = 4</td><td>K = 5</td></tr><tr><td>1</td><td>0.03</td><td>0.05</td><td>0.06</td><td>0.06</td><td>0.07</td><td>13</td><td>47</td><td>87</td><td>106</td><td>119</td></tr><tr><td>2</td><td>0.05</td><td>0.08</td><td>0.11</td><td>0.12</td><td>0.13</td><td>161</td><td>482</td><td>820</td><td>1012</td><td>1123</td></tr><tr><td>3</td><td>0.09</td><td>0.13</td><td>0.19</td><td>0.21</td><td>0.23</td><td>1696</td><td>3484</td><td>5637</td><td>7027</td><td>7691</td></tr><tr><td>4</td><td>0.17</td><td>0.21</td><td>0.26</td><td>0.29</td><td>0.31</td><td>9000</td><td>12,000</td><td>13,500</td><td>15,000</td><td>17,000</td></tr></table>

strategy is not as effective in our experiment but is still necessary to enlarge the channels to seek collaborators and discover more collaboration opportunities.

Analysis of CS: Balancing the size and coverage of the candidate sets, we set K to five and n to two in the experiment. The candidate set of each company contains the company's collaborators (DC), the collaborators of the company's collaborators (CS1) and the collaborators of its top-five similar companies' collaborators (CS2). Finally, the average size of the candidate sets (i.e., CS) is 3850, and the average coverage is 0.65.

Discussion: For the sake of system efficiency, we selected small sets of candidate researchers for recommendation. This process could lead to the loss of a few relevant researchers. Nevertheless, the proposed recommendation system aims to recommend collaborators in a timely fashion instead of retrieving all of the potential collaborators. There are millions of researchers and the efficiency of making recommendations from the whole researcher set is low. In this experiment, the system on average takes 0.5 s for each project when recommending from the reduced candidate sets but takes 110 s when recommending from the whole recommendation set. It is necessary to sacrifice the coverage to some degree to obtain higher efficiency of the system. The candidate sets for recommendation can be determined by balancing the efficiency of the recommendation system and the coverage of candidate sets in real application.

## 4.2. Description of user study

## 4.2.1. Experiment data of user study

A user study is conducted to obtain the real attitudes of companies to recommendations. For the user study, 35 companies are selected as subjects for survey, and researchers who have connections with these companies in four steps are selected as candidate researchers for recommendation. Documents (i.e., patents, projects, and publications) of companies and researchers are collected from ScholarMate to construct the companies' basic profiles and researchers' profiles. The companies' most recent projects are regarded as contexts, according to which we built context profiles and generate recommendations. We provided the subjects with their most recent projects to explain the recommendation contexts and presented them mixed recommendation lists containing recommendations of different methods. The subjects are asked to answer whether they would like to collaborate with the recommended researchers for the projects or not, and judge the recommendation results on a 5-point Likert scale to show the intensity of their willingness (1: strongly unwilling, 2: unwilling, 3: neither willing nor unwilling, 4: willing, 5: strongly willing). The information about how recommendations are generated is hidden to avoid potential bias. To assist the subjects to make decisions, a brief introduction to each recommendation is given, including demographic information, publications, patents, projects, and social relations.

## 4.2.2. Evaluation metrics of user study

The ratings of subjects on recommendations are collected to evaluate the effectiveness of different methods. The Average Rating score (AR) is selected to measure the performance of different methods in this user study. It is computed among the ratings from all of the subjects on all of the recommendations. The average rating score is computed as

$$
\mathrm{AR} = \frac {1}{| U |} \sum_ {i = 1} ^ {| U |} \frac {1}{N} \sum_ {j = 1} ^ {N} r _ {i j}\tag{17}
$$

where ∣U∣ represents the number of subjects in the survey, N represents the number of recommendations, and $r _ { i j }$ represents the rating of subject i on recommendation j. The AR represents users' satisfaction on the recommendations.

## 4.3. Baseline methods

The effectiveness of the proposed recommendation method is evaluated in comparison with the baseline methods, i.e., the contentbased method, the social network-based method and the sum method [30,34]. In this paper, the content-based method is represented as CB, the social network-based method is represented as SN, and the sum method is represented as SUM.

• CB. Researchers are evaluated and ranked based on their expertise relevance, which is computed by Eq. (2). The top N most relevant researchers are suggested to the company.

• SN. Katz's approach [13] is a widely adopted approach for social proximity analysis. Based on the collaboration network, the proximity of researcher r to company c is calculated as $\begin{array} { r } { p _ { c r } = \sum _ { l = 1 } ^ { n } \eta ^ { l } \cdot \vert ~ p a t h _ { c r } ^ { < l > } } \end{array}$ , where n is the step threshold, η is the damping factor and $| p a t h _ { c r } ^ { < l > } |$ ∣ represents the number of paths that connect researcher r and company c in step l. In this experiment, we set the step threshold as four. The top N researchers with the highest proximity values are recommended.

• SUM. The sum method uses addition techniques to combine the relevance, quality, and proximity evaluations. The recommendation score is computed as $R S _ { c r } { = } R E L _ { c r } { + } Q U A _ { r } { + } p _ { c r } ,$ where $p _ { c r }$ measures the proximity of researcher r with company c. The top N researchers with the highest recommendation scores are recommended.

• NEW. NEW is used to represent the proposed method, which combines the relevance, quality, and trust relations using a contextual trust analysis model. The top N researchers with the highest contextual trust values are recommended.

## 4.4. Determination of parameters

This paper focuses on the effectiveness of the proposed method in comparison with baseline methods instead of the optimal parameters for recommendation systems. The parameter values are given by experience in Table 3.

## 5. Experiment results

Results of the offline experiment and user study are analyzed to show the effectiveness of the proposed method.

## Table 3

Parameter setting.

<table><tr><td>Parameter</td><td>Description</td><td>Value</td></tr><tr><td> $\omega_A, \omega_B, \omega_C, \omega_D$ </td><td>Weights of A level, B level, C level and D level journalsa</td><td> $\omega_A = 1, \omega_B = 3/4, \omega_C = 1/2, \omega_D = 1/4$ </td></tr><tr><td> $\alpha, \beta, \gamma$ </td><td>Weights of quality indicators in articles, projects and patents</td><td> $\alpha = \beta = \gamma = 1/3$ </td></tr><tr><td>MTCL</td><td>Threshold of trust chain length</td><td>4</td></tr><tr><td> $\eta$ </td><td>Damping factor</td><td>0.5</td></tr><tr><td>N</td><td>Recommendation size</td><td>N=5, 10</td></tr></table>

<sup>a</sup> In our experiment, the top 25% journals with the highest impact factors (IFs) are classified into the A level, journals of which the IFs are ranked between 25% and 50% will be classified into the B level and so on.

## 5.1. Results of offline experiment

We first analyzed the accuracy performance of recommendation methods and then compared the recommendations with real collaborators in terms of expertise relevance, quality, and proximity.

## 5.1.1. Accuracy performance of recommendation methods

Table 4 shows the accuracy performance of methods. Significance tests (i.e., paired t-test and ANOVA test) are conducted to verify the differences between the proposed method and every baseline method. “Inclusive-of-prior-collaborators” denotes the case that prior collaborators are not specially removed from the test sets and recommendation sets, and “exclusive-of-prior-collaborators” denotes the case that prior collaborators are removed from recommendation sets and test sets. The results in inclusive-of-prior-collaborators show the performance of recommendation methods in identifying relevant researchers for the target projects, and the results in exclusive-of-prior-collaborators show their performance in identifying new collaborators specifically. We plot the precision, recall, and F values of recommendation methods as a box-and-whisker chart in Fig. 5. The top and bottom of the box denotes the first and third quartiles, and the whiskers denote the maximum and minimum. The dots represent outliers and the crosses represent mean values.

To show the power of recommendation methods, we introduced a random method (represented as RM in Table 4) that randomly selects N researchers for recommendation. As shown in Table 4, the random method fails to identify collaborators for companies' projects. The recommendation methods are useful to identify collaborators for companies' R&D projects in comparison with random selection.

With the increase in recommendation size, the precision value decreases but the recall value increases. The F-value is relatively higher when the recommendation size equals five. Taken together, it is suitable to recommend five researchers for each project. From the left part of Fig. $5 ,$ we see that the proposed method performs better than CB and SUM method. As shown in Table 4, the proposed method obtains significantly higher accuracy performance than SUM and CB method. The SN method has higher recommendation accuracy than the proposed method, but their differences are not significant. As shown in the right part of Table 4 and Fig. 5, the proposed method performs best in exclusive-ofprior-collaborators case, while the performance of SN method decreases dramatically.

In exclusive-of-prior-collaborators case, the recall values of the proposed method, CB method and SUM method are higher than their recall values in inclusive-of-prior-collaborators case. When recommending ten researchers, the proposed method can identify almost half of actual collaborators of target projects in exclusive-of-prior-collaborators case. However, the precision values of recommendation methods become lower. The reason could be that some correct recommendations are prior collaborators in inclusive-of-prior-collaborators case. Consequently, removing prior collaborators reduces the precision values, and SN method is most affected. Besides, the average size of test sets is smaller than the recommendation size after prior collaborators are removed, so the precision values are lower but the recall values are higher (except the recall values of SN method).

## 5.1.2. Comparison of real collaborator choices to recommendations

We compared the top five recommendations of different methods with the real collaborators (represented as “REAL” in Table 5) to see whether the recommendations have higher relevance, proximity and quality values than the researchers selected by companies without recommendation systems. Table 5 shows the average relevance, quality and proximity values of the real collaborators and the recommendations of different methods. Significance tests (i.e., paired t-test and ANOVA test) are conducted to compare the differences between real collaborators and recommendations. From Table 5, we can see that different methods emphasize on different aspects. Compared with the real researchers, recommendations of CB method have higher relevance and quality values but lower proximity values. Both SN method and SUM method recommend researchers with higher proximity and quality values but lower relevance values, which means that some of the recommended researchers are irrelevant to the given contexts of companies. The proposed method recommends researchers with higher relevance and quality values without reducing proximity values.

Table 4  
Accuracy performance of different recommendation methods

<table><tr><td rowspan="2"></td><td colspan="5">Inclusive of prior collaborators</td><td colspan="5">Exclusive of prior collaborators</td></tr><tr><td>RM</td><td>CB</td><td>SN</td><td>SUM</td><td>NEW</td><td>RM</td><td>CB</td><td>SN</td><td>SUM</td><td>NEW</td></tr><tr><td>Precision@5</td><td> $0.00^{-}$ </td><td> $0.11^{-}$ </td><td>0.21</td><td> $0.12^{-}$ </td><td>0.17</td><td> $0.00^{-}$ </td><td> $0.10^{-}$ </td><td> $0.05^{-}$ </td><td> $0.10^{-}$ </td><td>0.15</td></tr><tr><td>Recall@5</td><td> $0.00^{-}$ </td><td> $0.15^{-}$ </td><td>0.27</td><td> $0.16^{-}$ </td><td>0.23</td><td> $0.00^{-}$ </td><td> $0.24^{-}$ </td><td> $0.09^{-}$ </td><td> $0.26^{-}$ </td><td>0.35</td></tr><tr><td>F@5</td><td> $0.00^{-}$ </td><td> $0.12^{-}$ </td><td>0.22</td><td> $0.13^{-}$ </td><td>0.18</td><td> $0.00^{-}$ </td><td> $0.12^{-}$ </td><td> $0.06^{-}$ </td><td> $0.13^{-}$ </td><td>0.19</td></tr><tr><td>Precision@10</td><td> $0.00^{-}$ </td><td> $0.07^{-}$ </td><td>0.13</td><td> $0.08^{-}$ </td><td>0.11</td><td> $0.00^{-}$ </td><td> $0.06^{-}$ </td><td> $0.03^{-}$ </td><td> $0.07^{-}$ </td><td>0.09</td></tr><tr><td>Recall@10</td><td> $0.00^{-}$ </td><td> $0.19^{-}$ </td><td> $0.34^{+}$ </td><td> $0.22^{-}$ </td><td>0.29</td><td> $0.00^{-}$ </td><td> $0.30^{-}$ </td><td> $0.13^{-}$ </td><td> $0.34^{-}$ </td><td>0.43</td></tr><tr><td>F@10</td><td> $0.00^{-}$ </td><td> $0.10^{-}$ </td><td>0.18</td><td> $0.11^{-}$ </td><td>0.15</td><td> $0.00^{-}$ </td><td> $0.09^{-}$ </td><td> $0.05^{-}$ </td><td> $0.11^{-}$ </td><td>0.14</td></tr></table>

Note: label “<sup>−</sup>”/“<sup>+</sup>” represents the row value of the column method is significantly lower/higher than the corresponding value of the proposed method (i.e., NEW) in both paired t-test and ANOVA with Tukey HSD test (significance level = 0.05). The results are based on 2373 projects.

## 5.1.3. Discussion of offline experiment

The proposed method integrates multiple criteria of researchers for recommendation, but it has no significant accuracy improvement as compared with SN method in inclusive-of-prior-collaborators case. This could be due to the lack of an effective partner identification mechanism to support companies in identifying collaborators for project collaborations. The collaborators who are selected by companies without recommendation systems could largely depend on their previous social relations, and that is why SN method obtains the best performance in this case. The proposed method obtains the best performance in terms of recommending collaborators who have not collaborated with companies before, while the performance of SN method decreases dramatically in exclusive-of-prior-collaborators case.

Besides the evaluation on recommendation accuracy, an additional evaluation is provided to compare recommendations with the real collaborators selected by companies without a recommendation system. The results show that recommendations of the proposed method have higher relevance and quality values and the same proximity values as compared with the real collaborators, while recommendations of baseline methods have significantly lower values on some criteria. However,

![](/api/attachments/EGK8YU3A/fulltext/images/f5628599710708919457790c469dec8a2d4b6e386bc5c1b487867c3fcbb5be33.jpg)

![](/api/attachments/EGK8YU3A/fulltext/images/00eaa632030001269b399327d40d4a9299c42e9cae597da573bca66cb3cc1156.jpg)

![](/api/attachments/EGK8YU3A/fulltext/images/358261f682809a10cd8b737b6cefd42a1fee2d0cf6d04ff9caa70763dd27985d.jpg)  
F-value(1)

![](/api/attachments/EGK8YU3A/fulltext/images/d0978d13f528cda300fe308e0bfe168a7f368eb77804ec0a43fcbffa539146a2.jpg)

![](/api/attachments/EGK8YU3A/fulltext/images/40e4e5cd65c82e6fd56bf9000b7cb8f4dc1f6a72387f3f9eb95d53df66bc527f.jpg)

F-value(2)  
![](/api/attachments/EGK8YU3A/fulltext/images/ae058bf691a07346f636a71de75c6f5cfba25aab428566e8e2ac1fa97f9f83fc.jpg)  
Fig. 5. A box-and-whisker chart of accuracy performance of different methods. Note: (1) represents the inclusive-of-prior-collaborators case and (2) represents exclusive-of-priorcollaborators case. The number after method names represents the recommendation size. The chart is based on the accuracy performance of recommendations for 2373 projects.

Please cite this article as: Q. Wang, et al., A context-aware researcher recommendation system for university-industry collaboration on R&D projects, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.09.001

Table 5  
Relevance, quality, and proximity values of recommendations and real collaborators.

<table><tr><td></td><td>REAL</td><td>CB</td><td>SN</td><td>SUM</td><td>NEW</td></tr><tr><td>Relevance</td><td>0.19</td><td> $0.34^{+}$ </td><td> $0.16^{-}$ </td><td> $0.17^{-}$ </td><td> $0.28^{+}$ </td></tr><tr><td>Quality</td><td>0.03</td><td> $0.04^{+}$ </td><td> $0.05^{+}$ </td><td> $0.22^{+}$ </td><td> $0.05^{+}$ </td></tr><tr><td>Proximity</td><td>0.09</td><td> $0.07^{-}$ </td><td> $0.27^{+}$ </td><td> $0.17^{+}$ </td><td>0.09</td></tr></table>

Note: labe $" " \Gamma ^ { \prime \prime } / " + \ " \Gamma$ represents the row value of the column method is significantly lower/ higher than the row value of real collaborators (i.e., REAL) in both paired t-test and ANOVA with Tukey HSD test (significance level = 0.05). The results are based on 2373 projects.

in the offline experiment, we cannot obtain the real feedback of companies on the recommendations and analyze the influence of recommendation systems on companies' behavior [26].

## 5.2. Results of user study

In the user study, 35 companies are invited for the survey on whether the companies are willing to collaborate with the recommendations. Recommendations of the CB method, SN method, SUM method, and the proposed method are provided for companies. Each method contributes five recommendations so each subject should judge at most twenty recommendations. Table 6 shows the average ratings of companies on recommendations and the results of significance test. The average rating of the proposed method is 3.65 and the average rating of CB, SN, and SUM method is 2.32, 2.23, and 3.28, respectively. The proposed method achieves a higher average rating than baseline methods, and their differences are significant.

Although SN method obtains higher recommendation accuracy in the offline experiment, the recommendations generated by SN method are not satisfactory in user study because the expertise relevance of recommendations to the given project is not considered and irrelevant recommendations obtain low ratings. The average rating of CB method is low because companies are not familiar with the recommended researchers and they have no confidence to collaborate with them on R&D projects. The SUM method uses the addition technique to combine the relevance, quality, and proximity criteria. Its average rating is higher than CB and SN method but lower than the proposed method. The reason could be that the addition technique has compensability in that a higher value on one criterion can make up for a low value on another criterion. For example, recommendations of SUM method could include researchers who have very high proximity values but are irrelevant to the current context. The proposed method combines the contextual relevance, quality, and trust relations by a contextual trust analysis model and obtains a higher average rating from subjects. Companies have a stronger willingness to collaborate with researchers who are recommended by the proposed method.

Further, we divided the recommendations for companies' projects into two groups: prior collaborators and new collaborators, and calculated average rating for each group (Table 7). As shown in Table 7, the prior collaborators recommended by the proposed method and CB method have higher ratings than new collaborators, while prior collaborators recommended by SN method and SUM method have lower ratings than new collaborators. The proposed method and CB method take contextual relevance of researchers into consideration so that most recommendations are relevant to the target projects. In this situation, prior collaborators have priority than new collaborators because companies trust them. While the prior collaborators recommended by SN method

## Table 6

Average ratings of subjects on recommendations.

<table><tr><td></td><td>CB</td><td>SN</td><td>SUM</td><td>NEW</td></tr><tr><td>AR</td><td> $2.32^{-}$ </td><td> $2.23^{-}$ </td><td> $3.28^{-}$ </td><td>3.65</td></tr></table>

Note: Label <sup>−</sup> represents the AR value of the column method is signi cantly lower than the value of the proposed method in both paired t-test and ANOVA with Tukey HSD test (significance level = 0.05). The results are based on 35 projects.

Table 7  
Average ratings of subjects on prior collaborators and new collaborators.

<table><tr><td></td><td>CB</td><td>SN</td><td>SUM</td><td>NEW</td></tr><tr><td>AR of prior collaborators</td><td>2.45</td><td>2.19</td><td>3.16</td><td>3.92</td></tr><tr><td>AR of new collaborators</td><td>2.29</td><td>2.38</td><td>3.32</td><td>3.61</td></tr></table>

and SUM method could be in inferior position because they might be irrelevant to the target projects and companies know they are not experts for the target projects.

## 6. Conclusions

University-industry collaboration is becoming more and more important now. The major challenge of the R&D project collaboration is to find suitable collaborators. In this paper, a context-aware researcher recommendation system is proposed to suggest researchers for industrial R&D projects and promote university-industry collaboration. The proposed system employs an offline preparation module to identify candidate researchers and an online recommendation module to capture the contexts of companies and suggest researchers with a contextual trust analysis model. The contextual trust analysis model integrates multiple aspects of researchers for evaluation and recommendation, i.e., expertise relevance, quality and trust relations. An offline experiment and a user survey are conducted to evaluate the effectiveness of the proposed recommendation system. The results show that the proposed recommendation system is effective at identifying suitable collaborators for companies' projects.

The contributions of this research are summarized. A novel contextaware researcher recommendation system is proposed to promote the university-industry collaboration on industrial R&D projects, where a contextual trust analysis model is proposed to evaluate researchers for recommendation. Its effectiveness is demonstrated in the experiments. This study provides a new perspective for research on promoting university-industry collaboration. It also responds to the practical needs of promoting university-industry collaboration. The proposed recommendation system can be implemented on social network platforms to provide services for companies. Armed with social network platforms and recommendation systems, companies can easily access more experts. It is more likely for companies to collaborate with researchers with the support of efficient collaborator identification mechanisms.

The research work can be further extended. In this research, an offline experiment and a user study are conducted to analyze the effectiveness of recommendation systems. However, it is difficult to measure the collaboration performance in current experiments, which can be improved in future to evaluate the real value of the proposed recommendation system. For example, a controlled experiment can be designed to analyze the value of the recommendation system by comparing the outputs of collaborations facilitated by the proposed system with the outputs of collaborations facilitated by a baseline method. More contexts can be defined to promote the university-industry collaboration further. The proposed recommendation system promotes university-industry collaboration by solving the information overload and asymmetry problem faced in collaborator selection stage and it is effective at suggesting suitable researchers for R&D projects. However, its effect is limited after the start of the collaboration. There are still lots of work to be done to ensure the success of university-industry collaboration.

Qi Wang is a joint PhD student of City University of Hong Kong and Xi'an Jiaotong University. She received a Bachelor degree from Business school, Jilin University in 2013. Her research interests concern university-industry collaboration and recommendation systems.

Jian Ma is a Professor in the Department of Information Systems, City University of Hong Kong. He received his Doctor of Engineering degree in Computer Science from Asia Institute of Technology. Dr. Ma's research areas include decision and decision support systems, business intelligence, research information systems, research and innovation social networks. His past research has been published in IEEE Transactions on Engineering Management, IEEE Transactions on Education, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems, Information and Management, European Journal of Operational Research, and Scientometrics.

Xiuwu Liao is a professor in the School of Management, Xi'an Jiaotong University. He received his Doctor degree in 2002 from Dalian University of Technology. Dr. Liao's research area covers multi-criteria decision-making, group decision making, e-auctions and IT outsourcing. He has published in Information Systems Research, Annals of Operations Research, Decision Support systems, Information Systems, Knowledge-based Systems, Omega, and European Journal of Operational Research.

Wei Du is a lecturer in School of Information, Renmin University of China. She received her Doctor degree in 2016 from City University of Hong Kong. Her research interests include recommender systems, social network analysis and knowledge organization systems. Her research has published in Scientometrics, International Conference on Information Systems (ICIS), Hawaii International Conference on System Sciences (HICSS) and so on.

## Acknowledgements

The authors gratefully thank the Editor and all reviewers. This work was supported by the National Natural Science Foundation of China [grant numbers: 91546119, 71371164] and CityU Research Grant [grant numbers: 9620366, 7004715].

## References

[1] M. Al-Hassan, H. Lu, J. Lu, A semantic enhanced hybrid recommendation approach: a case study of e-Government tourism service recommendation system, Decis, Sup. port. Syst. 72 (2015) 97–109.

[2] R. Baeza-Yates. B. Ribeiro-Neto, Modern Information Retrieval. ACM Press, New York, 1999.

[3] T. Barnes, I. Pashby, A. Gibbons, Effective university–industry interaction: a multicase evaluation of collaborative R&D projects, Eur. Manag. J. 20 (3) (2002) 272–285.

[4] T. Bogers, A. Van den Bosch, Recommending scientific articles using citeulike, Proceedings of the 2008 ACM Conference on Recommender Systems, ACM 2008, pp. 287–290.

[5] F. Bonchi, C. Castillo, A. Gionis, A. Jaimes, Social network analysis and mining for business applications, ACM Transactions on Intelligent Systems and Technology (TIST) 2 (3) (2011) 22–58.

[6] J. Bruneel, P. D'Este, A. Salter, Investigating the factors that diminish the barriers to university–industry collaboration, Res. Policy 39 (7) (2010) 858–868.

[7] P. Chaiwanarom, C. Lursinsap, Collaborator recommendation in interdisciplinary computer science using degrees of collaborative forces, temporal evolution of research interest, and comparative seniority status, Knowl.-Based Syst, 75 (2015) 161–172.

[8] P. D'Este, M. Perkmann, Why do academics engage with industry? The entrepreneurial university and individual motivations, J. Technol. Transf. 36 (3) (2010) 316-339

[9] C. De Fuentes, G. Dutrénit, Best channels of academia–industry interaction for longterm benefit, Res, Policy 41 (9) (2012) 1666–1682

[10] K. Debackere, R. Veugelers, The role of academic technology transfer organizations in improving industry science links. Res. Policy 34 (3) (2005) 321–342.

[11] M. Gulbrandsen, J.-C. Smeby, Industry funding and university professors' research performance, Res. Policy 34 (6) (2005) 932–950.

[12] J.-Y. Hong, E.-H. Suh, S.-J. Kim, Context-aware systems: a literature review and classification, Expert Syst. Appl. 36 (4) (2009) 8509–8522.

[13] L. Katz, A new status index derived from sociometric analysis, Psychometrika 18 (1) (1953) 39–43.

[14] A. Lam, What motivates academic scientists to engage in research commercialization: ‘gold’, ‘ribbon’ or ‘puzzle’? Res. Policy 40 (10) (2011) 1354–1368.

[15] J.O. Lanjouw, M. Schankerman, Patent quality and research productivity: measuring innovation with multiple indicators, Econ. J. 114 (495) (2004) 441–465.

[16] Y.-M. Li, T.-F. Liao, C.-Y. Lai, A social recommender mechanism for improving knowledge sharing in online forums, Inf. Process. Manag. 48 (5) (2012) 978–994.

[17] Y. Li, M. Yang, Z.M. Zhang, Scientific articles recommendation, Proceedings of the 22nd ACM International Conference on Conference on Information & Knowledge Management, ACM 2013, pp. 1147–1156.

[18] D. Liben-Nowell, J. Kleinberg, The link-prediction problem for social networks, J. Am. Soc. Inf. Sci. Technol. 58 (7) (2007) 1019 1031.

[19] J. Lu, D. Wu, M. Mao, W. Wang, G. Zhang, Recommender system application developments: a survey, Decis. Support. Syst. 74 (2015) 12–32.

[20] M. Mao, J. Lu, G. Zhang, J. Zhang, Multirelational Social Recommendations Via Multigraph Ranking, 2016 (IEEE Transactions on Cybernetics).

[21] M. Perkmann, Z. King, S. Pavelin, Engaging excellence? Effects of faculty quality on university engagement with industry, Res. Policy 40 (4) (2011) 539–552.

[22] M. Perkmann, V. Tartari, M. McKelvey, E. Autio, A. Broström, P. D'Este, R. Fini, A. Geuna, R. Grimaldi, A. Hughes, S. Krabel, M. Kitson, P. Llerena, F. Lissoni, A. Salter, M. Sobrero, Academic engagement and commercialisation: a review of the literature on university–industry relations, Res. Policy 42 (2) (2013) 423–442.

[23] M. Perkmann, K. Walsh, University–industry relationships and open innovation: towards a research agenda, Int. J. Manag. Rev. 9 (4) (2007) 259–280

[24] F. Ricci, L. Rokach, B. Shapira, Introduction to recommender systems handbook, in: F. Ricci, L. Rokach, B. Shapira, P.B. Kantor (Eds.), Recommender Systems Handbook, Springer, US 2011, pp. 1–35.

[25] Q. Shambour, J. Lu, A trust-semantic fusion-based recommendation approach for ebusiness applications, Decis. Support. Syst. 54 (1) (2012) 768–780.

[26] G. Shani, A. Gunawardana, Evaluating recommendation systems, in: F. Ricci, L. Rokach, B. Shapira, P.B. Kantor (Eds.),Recommender Systems Handbook 2011, pp. 257–297 (Springer US).

[27] W. Sherchan, S. Nepal, C. Paris, A survey of trust in social networks, ACM Comput. Sury, 45 (4) (2013) 47–79

[28] R.L. Sie, H. Drachsler, M. Bitter-Rijpkema, P. Sloep, To whom and why should I connect? Co-author recommendation based on powerful and similar peers, International Journal of Technology Enhanced Learning 4 (1–2) (2012) 121–137.

[29] T. Silva, Z. Guo, J. Ma, H. Jiang, H. Chen, A social network-empowered research analytics framework for project selection, Decis. Support. Syst. 55 (4) (2013) 957–968.

[30] J. Sun, W. Xu, J. Ma, J. Sun, Leverage RAF to find domain experts on research social network services: a big data analytics methodology with MapReduce framework Int. J. Prod. Econ. 165 (2015) 185–193.

[31] A.J. Trappey, C.V. Trappey, C.-Y. Wu, C.-W. Lin, A patent quality analysis for innovative technology and product development, Adv. Eng. Inform. 26 (1) (2012) 26–34.

[32] P.D. Turney, P. Pantel, From frequency to meaning: vector space models of semantics L Artif Intell Res, 37 (1) (2010) 141–188.

[33] N. Van Zeebroeck, The puzzle of patent value indicators. Econ, Innoy, New Technol 20 (1) (2011) 33-62.

[34] G.A. Wang, J. Jiao, A.S. Abrahams, W. Fan, Z. Zhang, ExpertRank: a topic-aware expert finding algorithm for online knowledge communities, Decis. Support. Syst. 54 (3) (2013) 1442–1451.

[35] W. Wang, G. Zhang, J. Lu, Member contribution-based group recommender system, Decis. Support. Syst. 87 (2016) 80–93.

[36] Y. Xu, X. Guo, J. Hao, J. Ma, R.Y. Lau, W. Xu, Combining social network and semantic concept analysis for personalized academic researcher recommendation, Decis. Support. Syst. 54 (1) (2012) 564–573.

[37] D. Yimam-Seid, A. Kobsa, Expert-finding systems for organizations: problem and domain analysis and the DEMOIR approach, J. Organ. Comput. Electron. Commer. 13 (1) (2003) 1–24.
