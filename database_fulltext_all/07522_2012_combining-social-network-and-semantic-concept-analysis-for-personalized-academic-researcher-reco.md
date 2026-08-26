---
otero_id: 7522
otero_key: "R5S3M87E"
title: "Combining social network and semantic concept analysis for personalized academic researcher recommendation"
authors: "Yunhong Xu; Xitong Guo; Jinxing Hao; Jian Ma; Raymond Y.K. Lau; Wei Xu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Combining social network and semantic concept analysis for personalized academic researcher recommendation

Yunhong Xu <sup>a,</sup>⁎, Xitong Guo <sup>b</sup>, Jinxing Hao <sup>c</sup>, Jian Ma <sup>c</sup>, Raymond Y.K. Lau <sup>c</sup>, Wei Xu

<sup>a</sup> Faculty of Management and Economics, Kunming University of Science and Technology, China

<sup>b</sup> School of Management, Harbin Institute of Technology, China

<sup>c</sup> Department of Information Systems, City University of Hong Kong, Hong Kong

<sup>d</sup> School of Information, Renmin University of China, China

## a r t i c l e i n f o

Article history: Received 28 February 2012 Accepted 11 August 2012 Available online 21 August 2012

Keywords: Recommender agents Social network analysis Semantic concept analysis Knowledge management Expertise recommendation

## a b s t r a c t

The rapid proliferation of information technologies especially Web 2.0 techniques has changed the fundamenta ways how things can be done in many areas, including how researchers could communicate and collaborate with each other. The presence of the sheer volume of researchers and research information on the Web has led to the problem of information overload. There is a pressing need to develop researcher recommendation agents such that users can be provided with personalized recommendations of the researchers they can potentially collaborate with for mutual research bene<sup>fi</sup>ts. In academic contexts, recommending suitable research partners to researchers can facilitate knowledge discovery and exchange, and ultimately improve the research productivity of researchers. Existing expertise recommendation research usually investigates the expert recommending problem from two independent dimensions, namely, their social relations and expertise information. The main contribution of this paper is that we propose a network based researcher recommendation approach which combines social network analysis and semantic concept analysis in a uni<sup>fi</sup>ed framework to improve the effectiveness of personalized researcher recommendation. The results of our experiment show that the proposed approach signi<sup>fi</sup>cantly outperforms the other baseline methods. Moreover, how our proposed framework can be applied to the real-world academic contexts is explained based on a case study.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The rapid proliferation of information technologies especially Web 2.0 techniques have changed the nature of the information processing mechanisms in many areas, including the ways how researchers may communicate and collaborate with each other to conduct research work in academic contexts [21]. Fig. 1 shows the development of web techniques to facilitate researchers' works at various levels. The techniques in the <sup>fi</sup>rst strand allow researchers to access massive amounts of information and knowledge from various sources (e.g., academic databases and search engines) but contribute less to socialization aspect. The techniques in the second strand enable researchers to share their research related objects, e.g., research papers, progress reports, proposals, etc. The techniques in the second strand focus on sharing and exchanging of research related objects (content centered), where few provide direct connections with researchers. The techniques in the third strand offer platform to let researchers reveal their pro<sup>fi</sup>les and communicate with other researchers they might be interested in. For example, various academic community sites (e.g., LinkedIn,

ResearcherID,<sup>2</sup> Mendeley<sup>3</sup>) have been developed to help researchers all over the world to communicate effectively, to make new connections and form interest groups. The techniques in this strand are user centered, where researchers can directly communicate with each other [35], which bursts the bounds of the traditional way wherein the collaboration is usually limited to researchers they might know or referred by their colleagues. Through these community sites, they can browse the registered researchers' information all over the world, search other researchers they might be interested in and establish relationships with them.

With the rapid growth of academic communities, the large number of researchers available on the web presents great challenges to users looking for researchers they might be interested in. For example, it is reported that there were more than 60 million users registered on LinkedIn till February, 2010.<sup>4</sup> And the number of users exceeded 150 million in 2012.<sup>5</sup> Searching from so many choices is a tough task.

![](/api/attachments/R5S3M87E/fulltext/images/9d7aba500c312854d25697698b4d16681a3167f798329df158fe904a42d1c97b.jpg)  
Fig. 1. The development of web services provided for researchers.

Recommender agents can reduce the information overload by providing users with personalized and <sup>fi</sup>ltered information [23]. Moreover, providing users with value-added services such as suggesting to them a list of potential contacts they might be interested can bene<sup>fi</sup>t both researchers and academic communities. For researchers, they can easily <sup>fi</sup>nd other researchers they might be interested in from a huge number of researchers and establish relationships with them. For research communities, providing these services can improve users' loyalty and satisfaction to retain researchers and attract new ones in an academic community.

Expertise recommendation as a sub<sup>fi</sup>eld of knowledge management aims to elicit interests or preferences of users and recommend to them a list of experts they might be interested in. Researcher recommendation can be considered as an instantiation of expertise recommendation in academic contexts. Expertise recommendation has attracted much interest from the academic <sup>fi</sup>eld. Current research on expertise recommendation can be generally categorized into two streams. The <sup>fi</sup>rst stream is rooted in document retrieval and recommends experts based on analysis of knowledge content of experts and users' needs, where techniques like data mining and text mining are used [28]. Experts whose expertise matches the users' needs the most are recommended to users. The basic assumption is that people's expertise can be exactly accessed and represented like documents. The implicit nature of expertise knowledge makes it possible for information to get lost during expertise formalization. Moreover, most expertise recommendation agents use google-like keyword matching techniques, and the semantic analysis of the expertise content is lacking. Therefore, it is possible that experts with similar expertise as requested by users will never be recommended to them. For example, experts of network analysis will never be recommended to users if they are looking for experts of link analysis when semantic relationship is not taken into consideration. The second stream addresses the recommendation problem by analyzing the social relationship aspect of experts and making recommendations accordingly. However, existing social network based recommendation approaches use only the network connectivity information to explore the social relationships of persons; consideration of semantic information concerning people's expertise is lacking.

We believe that social relations and semantic information of expertise are two crucial factors to help prepare the ground for the development of expertise recommendation mechanisms. In researcher recommendation context, it is important to introduce personalized and socially related researchers to users they might be interested in through recommendation mechanism. Although some researchers combine the social dimension and expertise dimension to make recommendations, the two dimensions are loosely connected and only simple <sup>fi</sup>ltering approach was used [13].

Previous expertise recommendation research lacks an integrated and systematic approach to combine the social and expertise information especially when the semantic concept analysis of expertise is considered. This paper aims to propose a network based approach which integrates semantic analysis of expertise content and social network information of experts together to make expertise recommendation, where the semantic analysis based on domain ontology is used to analyze the semantic similarity of experts' expertise; social network analysis is employed to deal with the social relationships between experts. This paper also illustrates how the expert recommendation problem arising from the academic scenario (to recommend researchers whom a user may be interested in) can be addressed by the proposed network based approach. This paper investigates how the proposed approach can be used in researcher recommendation context through a case study. And the experimental results show that the proposed approach outperforms other baseline methods in terms of users' satisfaction.

## 2. Related research

## 2.1. Expertise management and expertise recommendation

With more and more information and knowledge being created and exchanged, the world has become more knowledge-oriented than ever before. Knowledge management is considered a crucial factor for success of different types of entities. Based on whether knowledge can be formally represented and easily communicated, two forms of knowledge have been identi<sup>fi</sup>ed and de<sup>fi</sup>ned by researchers in the <sup>fi</sup>eld of knowledge management: explicit and tacit knowledge [1]. Explicit knowledge can be expressed or codi<sup>fi</sup>ed using formal representation and easily shared among individuals [37]. Tacit knowledge is highly personal and dif<sup>fi</sup>cult to articulate as it is usually embedded in individual minds, where intangible factors such as personal beliefs, ideas, perspectives, and mental models are involved [4]. In most organizations, explicit knowledge is usually stored in the form of documents like reports, articles, patents, manuals, etc. Tacit knowledge resides in the form of expertise in people's minds [11]. Document management and expertise management can be considered two sub<sup>fi</sup>elds of knowledge management, to deal with explicit and tacit knowledge, respectively [19].

Effective management of expertise can bene<sup>fi</sup>t both organizations and individuals by facilitating access to knowledge, as well as sharing and applying knowledge. However, this is not an easy task. The tacit nature of expertise makes it dif<sup>fi</sup>cult to represent, assess and utilize such kind of knowledge [5]. In addition, the existence of large amounts of information about expertise presents great challenge in locating or <sup>fi</sup>nding experts concerning a particular subject or user, especially when the size of the organization is large [43]. And the phenomenon of information overload makes users confront quite a large number of deemed experts from whom they have to search for the right one. Thus, it is necessary to provide users value-added services like <sup>fi</sup>ltering large volumes of information and recommending experts who might satisfy users' particular needs.

In an information seeking community, recommendation agents are considered potential solutions to solve the information overload problem, which refers to recommending interesting or relevant information in a large archive. Expertise recommendation as a sub<sup>fi</sup>eld of knowledge management aims to alleviate the information overload problem by recommending to users a list of experts who might possess particular expertise knowledge required by users. Expertise recommendation could reduce the search costs of users and enhance communication between people in organizations by recommending possible experts to users [44]. Facilitating collaborations and communication through expertise recommendation is a fundamental part of knowledge management which ensures that expertise in the organization will be accessed and fully utilized [45].

## 2.2. Approaches for expertise recommendation

In the past few years, various approaches have been proposed in the expertise recommendation <sup>fi</sup>eld. Based on the source of information used, these recommendation approaches can be mainly classi<sup>fi</sup>ed into two types: recommendation approaches based on expertise information and approaches based on social relations of experts.

## 2.2.1. Expertise recommendation approaches based on expertise information

Expertise recommendation approaches based on content of expertise information have drawn much from document retrieval techniques. These approaches return a list of candidate persons who might have particular expertise requested by users [6]. The underlying assumption is that the co-occurrence of the name of a person and topics in the same context can be considered evidence that the person possesses the expertise. And experts are identi<sup>fi</sup>ed by uncovering associations between people and topics [9].

Various expertise recommendation methods and models are proposed based on this idea, ranging from the basic TF-IDF weighting [24] to complex probabilistic models [14,46]. The database approach stored expertise information in a database structure, and a user interface was provided to allow users to search for experts [12]. The pro<sup>fi</sup>le-based approach <sup>fi</sup>rst merged all sources concerning a candidate expert into a single personal pro<sup>fi</sup>le, then these pro<sup>fi</sup>les were ranked with respect to user queries using traditional retrieval techniques, and then the best candidate experts were recommended to the user [31]. The document-based approach tried to use supporting documents to rank the candidate experts based on the co-occurrences of topics and candidates mentioned in the documents [5].

Most current expertise recommendation approaches actually follow document retrieval mechanisms, where the focus is on the content of expertise itself [40]. The basic assumption is that people's expertise can be exactly accessed and represented like documents. However, due to the implicit nature of expertise knowledge, information loss is unavoidable when extracting and representing them in an explicit manner.

## 2.2.2. Expertise recommendation approaches based on social relations

McDonald and Ackerman [33] claimed that expertise is fundamentally a collaborative activity. Perugini et al. [39]. pointed out that recommending agents has an inherently social element and ultimately brings people together. Generally speaking, people are more likely to communicate with those who have certain relationships with them rather than with a stranger [13]. Therefore, expertise recommendation should re<sup>fl</sup>ect the social context in which people are embedded to point towards the connection paths and facilitate their interactions. Besides, social network relations re<sup>fl</sup>ect expertise information indirectly to some extent.

In order to address the social and collaborative aspects, various recommendation approaches based on social network information were proposed in previous research. For example, social network analysis was used to recommend possible collaborators for employees in a business context [32]. Christopher et al. [8] used graph ranking algorithm to recommend experts based on their email communications. Shen et al. [47] proposed a network with question/answer relations among people to calculate the reputation score of each user, recommendations were made on the basis of the score. Another example is expertise recommender, where the distance between the user and the expert in their social networks was used to <sup>fi</sup>lter recommended experts in an organizational environment [34]. Pavlov and Ichise [38] developed a link prediction based approach to recommend experts using collaboration network.

However, it was found that using only social network information to recommend experts and lacking the analysis of expertise could not generate satisfactory results [32]. Although social network analysis based recommendation approaches can implicitly provide latent information related to expertise, there is no explicit representation of expertise [5]. For example, graph based expertise <sup>fi</sup>nding approach is proposed to measure the centrality of persons in a social network while the relevant content related to expertise is ignored [26]. The underlying principle is that an expert will be in a central position in the network. This approach is sometimes designed as expertise independent measures of prior belief that a person is authoritative within a certain knowledge community and therefore is supposed to be an expert in every area. While for very constrained and specialized communities this assumption seems plausible, there is no guarantee that central users from multidisciplinary knowledge networks are experts in every area. Therefore, augmenting social network information with semantic information related with expertise can yield better performance than what can be achieved when using only social information.

## 2.2.3. Expertise recommendation approaches based on both social and expertise information

Due to the fact that the content of expertise and social relations of experts are two important dimensions concerning expertise recommendation, researchers have made efforts to combine these two dimensions together. One of the famous expertise recommendation systems is the ReferralWeb [25], which claimed to combine social network and collaborative <sup>fi</sup>ltering to recommend expertise. However, how to combine the two sources of information remains a black box. Although some researchers combined the social and expertise information to make recommendations, these two types of information are loosely connected and only simple <sup>fi</sup>ltering approach was used [13]. The basic principle of simple <sup>fi</sup>ltering is that a candidate expert list is generated based on expertise information, and social network information is used to <sup>fi</sup>lter the candidate expert list, those who have close social relationships with the target user are recommended.

## 2.3. Network analysis based framework to combine two dimensions

Most current research on expertise recommendation makes recommendations by investigating the content of expertise and the social relations among experts separately and lacks a systematic framework to combine these two dimensions together. Network analysis provides us some guidelines to integrate social relations of experts and their expertise information. Network analysis has been employed to study the complex systems in the real world which take the form of networks [2]. Network analysis models the real system using nodes and links, where nodes represent elements of the systems, and links can be a single or multiple type of relationship or shared characteristics among elements [15].

Following the network analysis framework, in researcher recommendation context, we can denote researchers and the concepts used to represent their expertise as nodes, and the relationships between nodes as links, then the expertise recommendation problem for a particular user can be considered a similarity measure problem to determine which remaining researchers are close to the particular user in the network. Therefore, the expertise recommendation problem can be transformed into a search problem in the network. The starting node for this search problem is the speci<sup>fi</sup>c user to whom the recommendation service is provided and the ending nodes are a set of researchers who are close to the speci<sup>fi</sup>c user in terms of both expertise and social relations.

![](/api/attachments/R5S3M87E/fulltext/images/79fa7200ae6dd6df1e57e9b9f87785f8695852b6653ac6d5ecdb2eb6c4083f37.jpg)  
Fig. 2. The two-layer model combines social and semantic information.

## 3. A two-layer network for researcher recommendation

## 3.1. The network model

In this research, a two-layer network model is proposed to combine the social network and semantic expertise information (as shown in Fig. 2). In this <sup>fi</sup>gure, the nodes in the concept layer represent expertise of researchers in the form of words or phrases. The links in this layer denote the semantic relationships between research expertise areas, which can be obtained from ontology in a domain. The nodes in the researcher layer represent researchers, and the links between them represent some kinds of social relationships occurring in academic activities, such as e-mail communication, taking part in the same project, collaborating on a paper, etc. The links between concept and researcher layer mean that a researcher shows expertise in the corresponding area.

## 3.2. Semantic similarity measure of concepts

In this context, concepts refer to the topical terms used to represent researchers' expertise which consist of words or phrases. Due to the fact that different concepts may denote similar or related expertise, it is necessary to take their semantic similarity into consideration when making expertise recommendation. If expertise recommendation is made based on google-like keyword matching approaches, some semantic information concerning expertise will be missing and some important cues may not be captured. Therefore, we incorporate the semantic similarity of concepts in the expertise recommendation process.

In the past few decades, various approaches have been proposed to measure the semantic similarity of concepts (Jiang et al. 1997; [30]). The basic idea of these approaches is to measure the semantic similarity of concepts by constructing lexical resources as a network or a directed graph, and then computing the semantic similarity based on the properties of the paths. WordNet<sup>6</sup> is widely adopted as the fundamental ontology to capture the semantic relations of concepts.

To consider the information system domain, in this study, WordNet was <sup>fi</sup>rst adapted by information system domain terminology according to Navigli et al.'s domain ontology integration approach [36,52]. The generated information system domain ontology has the technical characteristics of WordNet and the specialized terms from the information system area. The general process is as follows:

Step 1 Terminology extraction. An information system terminology is extracted from available texts in the information systems domain and <sup>fi</sup>ltered using natural language processing and statistical techniques.

Step 2 Semantic interpretation. Terms are semantically interpreted and ordered to generate a domain concept forest according to taxonomic relations.

Step 3 Ontology construction. The domain concept forest is used to create an information system domain ontology.

After that, the following de<sup>fi</sup>nitions and notation are used to calculate the semantic similarity among concepts in the domain ontology.

• The length of the shortest path in the domain ontology from synset c to c is represented by $l e n ( c _ { i } , c _ { j } )$

• lso $\left( { { C _ { i } } , { C _ { j } } } \right)$ is the concept of the lowest super-ordinate (or most specific common subsumer) of two concepts $c _ { i }$ and $c _ { j } .$

• Given any formula sim( $\mathbf { \Phi } _ { ( 1 } , C _ { 2 } )$ to compute semantic similarity between two concepts c to $c _ { 2 } ,$ , the similarity sim $( w _ { 1 } , w _ { 2 } )$ )between two words w to $w _ { 2 }$ can be calculated as

$$
\operatorname{sim} (w _ {1}, w _ {2}) = \max _ {c _ {1} \in s (w _ {1}), c _ {2} \in s (w _ {2})} [ \operatorname{sim} (c _ {1}, c _ {2}) ]
$$

where $s ( w _ { i } )$ is “the set of concepts in the taxonomy that are senses of word w ” [41]. In other words, the similarity of two words is equal to that of the most-related pair of concepts that they denote.

The semantic similarity measure in this research has two levels. For simple concepts which can be directly found in the domain ontology, we use the approach described in Section 3.2.1 to measure their semantic similarity. For complex concepts which cannot be found in the domain ontology directly, we use the approach presented in Section 3.2.2 to compute their similarity.

## 3.2.1. Semantic similarity measure of simple concepts

Simple concepts mean concepts that appear directly in the domain ontology. Jiang and Conrath [22] proposed an approach which combines the edge-based approach of the edge counting scheme and node-based approach of information content calculation. The formula can be represented as follows:

$$
\begin{array}{l} S I M _ {J C} (c _ {1}, c _ {2}) = e ^ {2 \times I C (l s o (c _ {1}, c _ {2})) - (I C (c _ {1}) + I C (c _ {2}))} \\ = e ^ {2 \times (- \log p (l s o (c _ {1}, c _ {2}))) - (- \log p (c _ {1}) - \log p (c _ {2}))} \\ = e ^ {- 2 \log p (l s o (c _ {1}, c _ {2})) + \log p (c _ {1}) + \log p (c _ {2})} \end{array}
$$

where lso $\left( c _ { 1 } , c _ { 2 } \right)$ represents the concept of the lowest super-ordinate of two concepts. $I C ( c )$ is de<sup>fi</sup>ned as the information content of a concept $c . I C ( c ) = - \log p ( c )$ , where $p ( c )$ is the probability of encountering an ∑ count w

$$
c, p (c) = \frac {\sum_ {w \in W (c)} c o u n t (w)}{N}.
$$

instance of concept c, p c <sup>w∈W</sup> <sup>cð</sup> <sup>Þ</sup> . W(c)is the set of words N in the corpus whose senses are subsumed by concept $c , N$ is the total number of word tokens in the corpus that are also present in the domain ontology.

Li et al. [30] proposed another approach using multiple information sources. The formula can be represented as follows:

$$
S I M _ {L I} (c _ {1}, c _ {2}) = e ^ {- \alpha l} * \frac {e ^ {\beta h} - e ^ {- \beta h}}{e ^ {\beta h} + e ^ {- \beta h}}
$$

where $\alpha \in [ 0 , 1 ] \mathrm { a n d } \beta \in [ 0 , 1 ]$ are constant parameters that scale the contribution of the shortest path and its depth. In this formula, $l { = } l e n ( c _ { 1 } , c _ { 2 } )$ presents the length of the shortest path between two concepts. And $h = d e p t h ( c _ { 1 } , c _ { 2 } )$ is the depth of the concept that subsumes two concepts $_ { \mathbb { C } _ { 1 } , \mathbb { C } _ { 2 } }$ in the hierarchical semantic nets.

It is found that combing the above two approaches can achieve better performance [3,16]. Thus, in this research, we use the following formula to synthesize these two approaches:

$S I M _ { J C \_ L I } ( c _ { 1 } , c _ { 2 } ) = \lambda S I M _ { J C } ( c _ { 1 } , c _ { 2 } ) + ( 1 - \lambda ) S I M _ { L I } ( c _ { 1 } , c _ { 2 } )$ , where λ is the adjustment parameter.

## 3.2.2. Semantic similarity measure of complex concepts

Complex concepts refer to concepts which do not appear directly in the domain ontology, but they can be viewed as phases composed of simple concepts. Therefore, the similarity of complex concepts is based on the measure of similarity of simple concepts. We follow the research of Li et al. [29] to compute the similarity of complex concepts:

$$
S I M (T _ {1}, T _ {2}) = \delta S _ {s} + (1 - \delta) S _ {r} = \delta \frac {s _ {1} . s _ {2}}{\| s _ {1} \| . \| s _ {2} \|} + (1 - \delta) \left(1 - \frac {\| r _ {1} - r _ {2} \|}{\| r _ {1} + r _ {2} \|}\right)
$$

where $S _ { s }$ represents the semantic information and $S _ { r }$ denotes the order similarity. $s _ { 1 }$ and s are two vectors, and the ith element of s is $s _ { 1 i } = \mathbf { \tilde {  { s } } } _ { i } \cdot I ( c _ { i } ) \cdot I ( \mathbf { \tilde {  { c } } } _ { i } )$ , and the jth element of $s _ { 2 }$ are $s _ { 2 j } = \mathbf { \tilde { \sigma } } _ { S _ { j } } { \cdot } I ( c _ { j } ) { \cdot } I ( \mathbf { \tilde { \sigma } } c _ { j } )$ $\widetilde { s }$ represents the lexical semantic vector. ˜c is the associated concept of $c _ { i } ,$ , which has the maximal semantic similarity among the concepts toward $c _ { i } . I ( c _ { i } )$ is the information content of $c _ { i } \operatorname { r } _ { 1 }$ and $\Gamma _ { 2 }$ represents the order of T1 and T2 respectively. And $\delta \in [ 0 , 1 ]$ determines the relative contribution of semantic and order information to the overall similarity computation. The detailed procedure to compute these parameters follows research of Li et al. [29].

## 3.3. Closeness measure of researchers

In academic contexts, there exist various social relations between researchers which may be related to expertise to some extent. One of the most important relations is their co-authorship. In reality, researchers' other social relationships which indicate their research expertise can also be taken into account and extracted from various resources [50]. For example, attending the same academic conference, or having the same education or work background, and so on (an example is shown in Fig. 3). The weights of the links represent the degree of importance of the social relationship towards expertise. For example, the co-authorship relation would have a higher weight than the experience of attending the same conference.

When various relationships among researchers are taken into account, the network of the researcher layer is extended to a multigraph where multiple edges among nodes are allowed. And the closeness of two researchers is based on aggregation and standardization of the weights of their links. The common way to deal with this is to aggregate the weight and transform the multigraph into a simple graph.

## 3.4. The evaluation of researchers' expertise

In academic contexts, researchers may have relatively more expertise in some particular research areas. The weights in the middle layer between concepts and researchers can be used to re<sup>fl</sup>ect this factor as shown in Fig. 4. The higher the weights, the more the expertise a researcher may possess in a particular area. In the real world, the impact of publication venue is used to re<sup>fl</sup>ect the impact of published research [48], which can be used to measure the expertise of researchers in a corresponding research area. Co-authorship network [42] and citation analysis [18] are used to rank researchers in terms of their expertise level. Also, researchers can claim their expertise levels themselves. For example, they can claim whether they are familiar with some research areas. Some research on evaluating expertise level of researchers used co-occurrences of the name of researchers and the research topics in particular areas as evidence that researchers have expertise in these areas. In practice, researchers' expertise in a topical area could be aggregated and measured by their publications, projects, and judgments given by their colleagues [49].

When evaluation of expertise is taken into consideration, researchers with high expertise level are easy to access in the two-layer network and thus have high probabilities of being recommended to other researchers. In the actual world, such researchers are authoritative and are considered experts in some particular areas.

![](/api/attachments/R5S3M87E/fulltext/images/496a6242f2dbb29ac63004260624f5aad6d8ff7b8cd6660857216049e930cb4d.jpg)  
Fig. 3. Integrating various social relations to form the researcher layer.

![](/api/attachments/R5S3M87E/fulltext/images/8d2483121f2e67b636c003523c2b550c62ed8d57eadef812c943e7ddfe196110.jpg)  
Fig. 4. The weights of the interlayer.

3.5. Transforming the recommendation problem to a similarity measure problem

As discussed in previous sections, the weights of links at the concept layer can be calculated using semantic analysis based on the constructed domain ontology. The weights of links at the researcher layer can be calculated based on their social closeness demonstrated in academic activities. And the weights of links in the between-layer measure researchers' expertise level towards corresponding areas. Thus, an undirected and weighted graph is generated based on the weights of three kinds of relationships, see Fig. 5 for example.

An extended matrix M can be used to capture three kinds of relationships in the two-layer network, where the elements in sub-matrix $M _ { C \times C }$ are the weights of the links for any pair of concepts. If no such links exist, the value of the element is 0. The elements in sub-matrix $M _ { R \times R }$ are the weights of links for researchers. If no links exist, the value of the element is 0. The elements in sub-matrix $M _ { R \times C }$ represent researchers' expertise level toward particular research topics, while the matrix $\mathsf { M } _ { C \times R }$ is the transpose of the matrix $M _ { R \times C }$

$$
M = \begin{array}{c} C \\ R \end{array} \left[ \begin{array}{c c} M 1 = M _ {C \times C} & M 2 ^ {T} = M _ {C \times R} \\ M 2 = M _ {R \times C} & M 3 = M _ {R \times R} \end{array} \right]
$$

From the measurement of the weights of links for concept and researcher, we know that the matrices $M _ { C \times C }$ and $M _ { R \times R }$ are symmetrical.

Based on this two-layer network, we can compute the similarities of the researchers and make recommendations accordingly. The underlying principle is that researchers tend to be interested in other researchers who are “close” to them, both in terms of their research areas and their social relations shown in academic activities. The similarity measurement problem can be considered a graph search problem, where the starting node is a particular researcher, and the ending nodes are a set of researchers. Two researchers are deemed highly similar in terms of their interests if they have strong links either through concepts or through other researchers. In this context, researchers who are similar will be connected by a comparatively larger number of short paths.

In this research, the spreading activation approach is employed to simulate the activation process and measure the similarities of nodes. Initially, research on spread activation was associated with semantic networks but lately it has been used as a general processing framework for many networks of nodes and their corresponding relationships [27].

The goal of the spreading activation process is to identify the nodes that are highly linked to the given activated node. In this research, the Hop<sup>fi</sup>eld net algorithm [51] is chosen to perform the spreading activation process. The basic idea of the Hop<sup>fi</sup>eld net algorithm is that starting from one or some of the target nodes and walking through the two-layer network along the links of concept–concept, researcher– concept and researcher–researcher. Then the communication time from the starting node to the ending nodes in a network, or the number of times a node has been walked through during a limited period of time can be used to measure the similarities of researchers toward the target node.

To address the unique characteristics of the expertise recommendation context, the original Hop<sup>fi</sup>eld net algorithm is modi<sup>fi</sup>ed to <sup>fi</sup>t the context as described below:

Initialization. The activation level of the target node (here is the user to whom we recommend researchers) is set at 1 and all other nodes (including other researchers and topical terms) are set at 0. This is to activate the target node in the network.

Iterative activation and activation level computation. At each generation,

nodes in the two-layer network are activated in parallel. The activated nodes can spread their activation status to their neighbors through their links. The activation level of newly activated nodes is computed based on summation of the activation level of their neighbors. In each generation, only a <sup>fi</sup>xed number of nodes with the highest activation levels are activated. The activation level for each node is computed as $\mu _ { j } ( t + 1 ) = f _ { s } \left[ \sum _ { i = 1 } ^ { n } W _ { i j } \mu _ { i } ( t ) \right]$ , where $1 \leq i \leq n$ and $W _ { i j }$ is the weight of the links connecting node i and j in the corresponding network, and $\mu _ { j } ( t + 1 )$ is the activation level of node j at time $t + 1 . f _ { s }$ is the SIGMOID transformation function $\begin{array} { r } { f _ { s } ( { \boldsymbol { x } } ) = \frac { 1 } { 1 + \exp ( ( \theta _ { 1 } - { \boldsymbol { x } } ) / \theta _ { 2 } ) } , } \end{array}$ where $\theta _ { 1 }$ serves as a threshold or bias and $\theta _ { 2 }$ is used to modify the shape of the SIGMOID function [7]. The SIGMOID function makes sure that the activation level of any node is less than 1. An activation constraint value can be used as the threshold to control the spreading process. That ${ \mathrm { i } } s ,$ if the activation level of a node is below the threshold value, then activation would not spread from that node [10].

![](/api/attachments/R5S3M87E/fulltext/images/03d040a3ddde2248febcf46ce3023866fa500e1494155d8b9aa30f16ac826dbf.jpg)  
Fig. 5. The weighted graph.

Table 1  
Descriptions of data sample.

<table><tr><td>Number of articles</td><td>Number of authors</td><td>Time span</td></tr><tr><td>398</td><td>767</td><td>2007–2009</td></tr></table>

eria. The algorithm repeats until there are no signi<sup>fi</sup>cant changes in terms of output between the last two iterations. That is, $\sum _ { j } \Big | \mu _ { j } ( t + 1 ) - \mu _ { j } ( t ) \Big | < \delta$ where δ is a small positive constant. When the algorithm converges, the output is a set of researchers who are similar to the target researcher in terms of the research areas and social relations. And researchers who have high activation levels in the <sup>fi</sup>nal iteration of the algorithm are recommended to the target researcher as they are considered similar to some extent.

## 4. A case study

## 4.1. Data description

We collected all papers published in a particular Information Systems annual conference—Paci<sup>fi</sup>c Asia Conference on Information Systems—(including author names and keyword information of the paper) from year 2007 to 2009, where approximately 398 papers and 767 authors are involved (see Table 1 for detailed information). Researchers' interest or expertise can vary during their academic life. Therefore, we chose a short period of time (3 years) to ensure that their research interests may not vary greatly. The keywords demonstrate researchers' expertise in particular research areas. The co-authorship network is constructed such that the nodes represent researchers and two researchers are linked if they have co-authored a conference paper during this particular period of time. For a particular time point, researchers who have ever published papers at the conference are considered.

## 4.2. Experiment

## 4.2.1. Overview of the experimental design

Users' perception of recommendation results determines the success of recommendation approaches. If users perceive that the recommendation result is bad, then the corresponding recommendation approach is bad, although it may be good from technical view. Thus, we evaluate the recommendation approaches based on users' direct feedback. User Information Satisfaction (UIS) is de<sup>fi</sup>ned as the extent to which users believe the information provided to them meets their information requirements [17,20]. UIS as a subjective measure of the success of artifact provides some guidelines to evaluate the performance of recommendation approaches. In this research, we focus on whether users are interested in researchers recommended to them and their future collaboration behavior. Therefore, we asked users to give their satisfaction score based on the extent to which they are interested in the recommended researchers. That is, if researchers are more interested in the researchers recommended to them, then they might give higher satisfaction score of the recommend result.

The recommendation is made based on the two-layer network model, we illustrate how to construct concept network and social network respectively using the conference data and how to link them into an integrated network. The detailed steps are described as follows.

Step 1 Domain ontology construction. First, information systems terminology is extracted from available texts in the information systems domain and <sup>fi</sup>ltered using natural language processing and statistical techniques. Then, terms are semantically interpreted and arranged in a hierarchical fashion to generate a domain concept forest according to their taxonomic relations. Finally, the domain forest is used to create Information Systems domain ontology.

Step 2 Concept network construction. Keywords highly abstract the content of the paper and demonstrate researchers' expertise to some extent. Therefore, keywords are used to represent researchers' expertise. The keywords used by researchers are unstructured, $\mathrm { e . g . }$ , both short form and full spelling of the same concepts existing, so the keywords were pre-processed to make them more standard. The semantic similarity of keywords was calculated using the semantic analysis approach presented in previous section. And concept network of keywords is constructed in such that the nodes represent keywords, and the weight of links denote the normalized semantic similarity of keywords.

Step 3 Social network construction. The collaboration network of researchers is constructed based on their co-author relationship in this conference. For the collaboration network, the nodes represent researchers. If two researchers have co-authored a paper published in this conference, then there exists a link between them. Since no other social relations are involved, the weight of the co-authorship link is set to be 1 as default.

![](/api/attachments/R5S3M87E/fulltext/images/7d5a6f5dddb748f182c1bf1223128f41824cd4d8907c61ff4e71800d5d505bca.jpg)  
Fig. 6. The researcher recommendation process for the proposed CSNSA approach.

![](/api/attachments/R5S3M87E/fulltext/images/17cf117f75bf68a0ef467c729d3f5bf47ff0263f5ab2b3c425e2f36569248517.jpg)  
Fig. 7. The researcher recommendation model for the proposed SEA approach.

Step 4 Linking concept and collaboration network. When the subnetworks of social network and concept network are generated, the proposed approach links these two networks into an integrated network based on the co-occurrence of the name of researchers and their research topics represented as keywords in the conference papers. The weight in the interlayer of the two-layer model represents researchers' expertise in related areas. Researchers publishing papers on related topics means that they show expertise in these areas. Since no other expertise information is included, we assume that researchers show the same expertise level if they published a paper in this conference. And the weight of the links in the interlayer is set at 1.

## 4.2.2. The proposed approach vs. two other baseline approaches

In order to evaluate the performance of the proposed approach and understand the advantage of the integrated framework, we compared the proposed approach, that is, the Combined Social Network and Semantic Analysis (CSNSA) approach with two other baseline approaches which used only social network or semantic information of expertise.

4.2.2.1. CSNSA approach. The CSNSA approach makes expertise recommendation utilizing both social network and semantic information of expertise. The recommendation is made based on calculating the similarity between the target researcher and other researchers along the two-layer network using the spreading activation algorithm. The target user node is activated <sup>fi</sup>rst, then the activation spreads to his/her related research topics, co-authors and other nodes along the two-layer network. The basic idea is to recommend target researchers other researchers who are close to them both in terms of research areas and social relations. The recommendation process of CSNSA approach is shown in Fig. 6.

4.2.2.2. SEA approach. As shown in Fig. 7, the SEA (SEmantic Analysis) approach uses only the semantic information of expertise content to make recommendations. For the spreading process of the SEA approach, the target researcher node is <sup>fi</sup>rst activated. Then the activation spreads to his/her related topical nodes. And the spreading activation algorithm walks along the concept layer and the inter-relationship between researcher and research topics. Researchers who are considered highly similar in their research topics are recommended to the target researchers.

4.2.2.3. SNA approach. As shown in Fig. 8, the SNA (Social Network Analysis) approach uses only the collaboration information of researchers to make recommendations. The spreading process starts from the target researcher node and then walks to his/her collaborators and other researchers along the network of the researcher layer. The idea is to recommend users researchers who are socially related to them. The SNA approach recommends to users researchers they might be interested in by calculating their similarity in their social network.

The SNA and SEA approaches can be considered simpli<sup>fi</sup>ed versions of the CSNSA approach, where part of the information is used to make researcher recommendations. As discussed in previous sections, the proposed CSNSA approach could overcome the weaknesses of using one kind of information alone, and thus may lead to greater perceived satisfaction.

## 4.2.3. Evaluation results

35 researchers who have published papers in this conference during this period of time were invited to participate in the experiment. These researchers had no prior knowledge about the recommendation approaches mentioned in this research. And they were chosen to be target researchers. For each target researcher, three groups of researchers were recommended to him/her using three approaches (CSNSA, SNA and SEA approaches) as described in previous section. For each approach, the top twenty researchers who have the highest activation level and have no co-authorship with the target researcher were recommended. The information about which group of recommended researchers was generated by which approach was hidden to avoid potential bias. The target subjects were asked to examine these three groups of recommended researchers and judged the recommendation results on a 10-point scale ranging from strong satisfaction to strong dissatisfaction (1, very unsatis<sup>fi</sup>ed; 5, average; 10, very satis<sup>fi</sup>ed.). And they were asked to give their satisfaction score based on the degree to which they were interested in the recommended researchers. Higher satisfaction score means target researchers have more potential to collaborate with the researchers recommended to them.

Table 2 shows the descriptive analysis of the performance of the three recommendation approaches in terms of satisfaction score. From this table, we can see that the average satisfaction score for the proposed CSNSA approach is 7.29, and the average satisfaction score of the SEA and SNA approach is 4.97 and 5.17 respectively. The standard deviation of the average satisfaction score of the CSNSA approach is 1.36, and the standard deviation for SNA and SEA approach is 1.93 and 1.62. The high average satisfaction score and low standard deviation may suggest that the proposed approach generated satisfactory recommendation results and the results are relatively stable.

![](/api/attachments/R5S3M87E/fulltext/images/e279cffedfcef15f8cfba8825fb3303f53108bd9b17f3a66b7311565fc8dcf56.jpg)  
Fig. 8. The researcher recommendation model for the proposed SNA approach.

Table 2  
Descriptive statistics of the performance of the three approaches.

<table><tr><td></td><td>Mean</td><td>S.D.</td></tr><tr><td>SNA</td><td>5.17</td><td>1.93</td></tr><tr><td>SEA</td><td>4.97</td><td>1.62</td></tr><tr><td>CSNSA</td><td>7.29</td><td>1.36</td></tr></table>

Since all subjects evaluated the three groups of researchers recommended by three approaches, we used paired sample T-tests to test the difference of their performances. The analysis result is shown in Table 3. And the test result further con<sup>fi</sup>rms that the proposed approach (CSNSA) was observed to achieve higher satisfaction scores than both SEA and SNA approaches at 5% signi<sup>fi</sup>cance level. Based on the results, we can draw the conclusion that the proposed CSNSA approach statistically signi<sup>fi</sup>cantly outperforms the other two baseline approaches which use only social information or semantic information of expertise. The superior performance of the proposed CSNSA approach was attributed to the integration of social network information of experts and semantic information of their expertise, which enables the recommendation of researchers who share common or related expertise and are socially close to some extent to the target researcher. Including social information in the recommendation approach enables us to explore social links between researchers. The semantic information of expertise captures the semantic relationship between researchers' research areas, which makes it possible to recommend related researchers in terms of expertise.

## 5. Conclusions and future research

Previous research on expertise recommendation is usually from two separate streams. One expertise recommendation stream is on exploring the social relationships of experts; the underlying principle is that people tend to connect with experts who have close relationships with them. Another is on investigating the content of their expertise. And previous research used simple <sup>fi</sup>ltering approach to integrate these two dimensions. Furthermore, the semantic analysis of expertise content is ignored. The main contribution of this paper is the design and development of a two-layer network analysis framework, which combines social network and semantic concept analyses, for recommending potential research collaborators in a principled manner. Social network analysis explores social relationships among researchers. And semantic analysis enables us to capture the semantic relationship of the content of researchers' expertise. Using this framework, we demonstrate how the association between candidate researchers and concepts can be combined in a natural and transparent manner. Based on the proposed network model, the problem of researcher recommendation can be transformed into a network search problem. And the case study shows that the proposed CSNSA approach could generate satisfactory recommendation results.

This study has important implications. Many communities emerge in academic contexts to support researchers sharing knowledge and communicating with each other. Some researchers have realized that communities work as a powerful platform for supporting knowledge management. The proposed researcher recommendation approach can be adapted and adopted in online social communities to suggest to users there a set of researchers they might be interested in. Providing value-added service like recommending to members other researchers they might be interested in can improve their loyalty toward a particular community and attract other researchers to become members. Besides, the proposed approach can be extended to recommend reviewers by considering the content of match between submission and reviewers' expertise and avoiding con<sup>fl</sup>ict of interest at the same time. In addition, the idea of combing social network and semantic analysis for expertise recommendation can be employed to recommend experts in other contexts, e.g., business contexts.

Table 3  
The T-test results of the performance of the recommendation approaches.

<table><tr><td>SNA vs. CSNSA</td><td>SEA vs. CSNSA</td></tr><tr><td> $\mathrm{SNA} < \mathrm{CSNSA} (p=0.013<0.05)$ </td><td> $\mathrm{SEA} < \mathrm{CSNSA} (p=0.001<0.05)$ </td></tr></table>

In this research, we choose information systems as a speci<sup>fi</sup>c domain to make expertise recommendations. In future research, we could test the proposed approach with more participants from other scienti<sup>fi</sup>c domains. Furthermore, other kinds of information can shed light on the proposed approach, such as other publication and social network information. In this research, only conference information is used. By incorporating more publication and social information of researchers, we can pro<sup>fi</sup>le researchers in a comprehensive way and improve the performance of recommendation results.

## Acknowledgments

This study was partially funded by Research Fund (KKSY201208119) provided by Kunming University of Science and Technology, the National Science Foundation of China Grant (71101037, 70890082 and 90924015).

## References

[1] M. Alavi, D.E. Leidner, Review: knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25 (1) (Mar 2001) 107–136.

[2] R. Albert, A.-L. Barabási, Statistical mechanics of complex networks, Review of Modern Physics 74 (2002) 47–91.

[3] H. Al-Mubaid, H.N. Nguyen, A cluster-based approach for semantic similarity in the biomedical domain, in: Conference Proceedings of the IEEE Engineering in Medicine and Biology Society, New York, USA, 2006.

[4] G. Anand, P.T. Ward, M.V. Tatikonda, Role of explicit and tacit knowledge in Six Sigma projects: an empirical examination of differential project success, Journa of Operations Management 28 (4) (2009) 303–315.

[5] K. Balog, L. Azzopardi, M. de Rijke, A language modeling framework for expert <sup>fi</sup>nding, Information Processing and Management 45 (1) (2009) 1–19.

[6] I. Becerra-Fernandez, Searching for experts on the Web: a review of contemporary expertise locator systems, ACM Transactions on Internet Technology 6 (4) (2006) 333–355.

[7] H. Chen, Y. Zhang, A.L. Houston, Semantic indexing and searching using a Hop<sup>fi</sup>eld net, Journal of Information Science 24 (1) (1998) 3–18.

[8] S.C. Christopher, P.M. Paul, C. Alex, D. Byron, Expertise identi<sup>fi</sup>cation using email communications, in: Proceedings of the Twelfth International Conference on In formation and Knowledge Management, ACM, New Orleans, LA, USA, 2003.

[9] N. Craswell, A. De Vries, I. Soboroff, Overview of the TREC-2005 Enterprise Track in: The Fourteenth Text Retrieval Conference Proceedings (TREC 2005), 2005.

[10] F. Crestani, P.L. Lee, Searching the Web by constrained spreading activation, Information Processing and Management 36 (4) (2000) 585–605.

[11] K.C. Desouza, Facilitating tacit knowledge exchange, Communications of the ACM 46 (6) (2003) 85–88.

[12] T. Dingsøyr, H.K. Djarraya, E. Røyrvik, Practical knowledge management tool use in a software consulting company, Communications of the ACM 48 (12) (2005) 96-100

[13] K. Ehrlich, C.Y. Lin, V. Grif<sup>fi</sup>ths-Fisher, Searching for experts in the enterprise: combining text and social network analysis in: Proceedings of the 2007 International ACM Conference on Supporting Group Work, ACM, Sanibel Island, Florida, USA, 2007.

[14] H. Fang, C. Zhai, Probabilistic models for expert <sup>fi</sup>nding, in: Advances in Information Retrieval, 2007, pp. 418–430.

[15] S. Fortunato, V. Latora, M. Marchiori, Method to <sup>fi</sup>nd community structures based on information centrality, Physical Review E 70 (5) (Nov 2004).

[16] W. Gad, M. Kamel, New semantic similarity based model for text clustering using extended gloss overlaps, Machine Learning and Data Mining in Pattern Recognition Lecture Notes in Computer Science 5632 (2009) 663–677.

[17] D.F. Galletta, A.L. Lederer, Some cautions on the measurement of user information satisfaction Decision Sciences 20 (3) (1989) 419–438.

[18] M.F. Henk, New developments in the use of citation analysis in research evaluation, Archivum Immunologiae et Therapiae Experimentalis 57 (1) (2009) 13–18.

[19] Z. Huang, H.C. Chen, F. Guo, J.J. Xu, S.S. Wu, W.H. Chen, Expertise visualization: an implementation and study based on cognitive <sup>fi</sup>t theory, Decision Support Systems 42 (3) (Dec 2006) 1539–1557.

[20] B. Ives, M. Olson, J. Baroudi, The measurement of user information satisfaction, Communications of the ACM 26 (10) (1983) 785–793.

[21] I. Jahnke, M. Koch, Web 2.0 goes academia: does Web 2.0 make a difference? International Journal Web Based Communities 5 (4) (2009) 484–500.

[22] J.J. Jiang, D.W. Conrath, Semantic similarity based on corpus statistics and lexical taxonomy, in: Proceedings of International Conference on Research in Computational Linguistics, Taiwan, 1997, pp. 19–33.

[23] Y. Jiang, J. Shang, Y. Liu, Maximizing customer satisfaction through an online recommendation system: a novel associative classi<sup>fi</sup>cation model, Decision Support Systems 48 (3) (2010) 470–479.

[24] A. Kanfer, J. Sweet, A. Schlosser, Humanizing the net: social navigation with a “know-who” email agent, in: Proceedings of the 3rd Conference on Human Factors and the Web, 1997.

[25] H. Kautz, B. Selman, M. Shah, Referral web: combining social networks and collaborative <sup>fi</sup>ltering, Communications of the ACM 40 (3) (Mar 1997) 63–65.

[26] J.M. Kleinberg, Authoritative sources in a hyperlinked environment, Journal of the ACM 46 (5) (1999) 604–632.

[27] J. Lajos, Z. Katona, A. Chattopadhyay, M. Sarvary, Category activation model: a spreading activation network model of subcategory positioning when categorization uncertainty is high, Journal of Consumer Research 36 (1) (Jun 2009) 122–136.

[28] M. Li, L. Liu, C.-B. Li, An approach to expert recommendation based on fuzzy linguistic method and fuzzy text classi<sup>fi</sup>cation in knowledge management systems, Expert Systems with Applications 38 (7) (2011) 8586–8596.

[29] Y.H. Li, D. McLean, Z.A. Bandar, J.D. O'Shea, K. Crockett, Sentence similarity based on semantic nets and corpus statistics, IEEE Transactions on Knowledge and Data Engineering 18 (8) (Aug 2006) 1138–1150.

[30] Y.H. Li, Z.A. Bandar, D. McLean, An approach for measuring semantic similarity between words using multiple information sources, IEEE Transactions on Knowl edge and Data Engineering 15 (4) (Jul-Aug 2003) 871–882.

[31] X. Liu, W.B. Croft, M. Koll, Finding experts in community-based questionanswering services, in: Proceedings of the 14th ACM International Conference on Information and Knowledge Management, 2005, New York, USA.

[32] D.W. McDonald, Recommending collaboration with social networks: a comparative evaluation in: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, Ft. Lauderdale, Florida, USA, 2003.

[33] D.W. McDonald, M.S. Ackerman, Just talk to me: a <sup>fi</sup>eld study of expertise location, in: Proceedings of the 1998 ACM Conference on Computer Supported Cooperative Work, ACM, Seattle, Washington, United States, 1998.

[34] D.W. McDonald, M.S. Ackerman, Expertise recommender: a <sup>fl</sup>exible recommendation system and architecture, in: Proceedings of the 2000 ACM Conference on Computer Supported Cooperative Work, ACM, Philadelphia, Pennsylvania, United States, 2000.

[35] K. Moeslein, A. Bullinger, J. Soeldner, Open collaborative development: trends, tools, and tactics, in: Human-Computer Interaction. New Trends, 2009, pp. 874–881.

[36] R. Navigli, P. Velardi, Learning domain ontologies from document warehouses and dedicated web sites Computational Linguistics 30 (2) (2004) 151–179

[37] D. Nevo, Y.E. Chan, A Delphi study of knowledge management systems: scope and requirements, Information Management 44 (6) (Sep 2007) 583–597.

[38] M. Pavlov, R. Ichise, Finding experts by link prediction in co-authorship networks, in: Proceedings of the Workshop on Finding Experts on the Web with Semantics, Busan, South Korea, 2007.

[39] S. Perugini, M.A. Goncalves, E.A. Fox, Recommender systems research: a connectioncentric survey, Journal of Intelligent Information Systems 23 (2) (Sep 2004) 107–143.

[40] T. Reichling, M. Veith, W. Volker, Expert recommender: designing for a network organization, Computer Supported Cooperative Work (CSCW) 16 (4) (2007) 431–465.

[41] P. Resnik, Using information content to evaluate semantic similarity in a taxonomy, in: Proceedings of the 14th International Joint Conference on Arti<sup>fi</sup>cial Intelligence, Montreal, 1995, pp. 448–453.

[42] M.A. Rodriguez, J. Bollen, An algorithm to determine peer-reviewers, in: Los Alamos National Laboratory Technical Report, LA-UR-06-2261, 2005.

[43] M.F. Schwartz, D.C.M. Wood, Discovering shared interests using graph analysis, Communications of the ACM 36 (8) (Aug 1993) 78–89.

[44] P. Serdyukov, L. Feng, A. van Bunningen, S. Evers, H. van Heerde, P. Apers, M. Fokkinga, D. Hiemstra, The right expert at the right time and place, in: Practical Aspects of Knowledge Management, 2008, pp. 38–49.

[45] M.A. Setiawan, S. Sadiq, R. Kirkman, W. Abramowicz, W. Aalst, J. Mylopoulos, M. Rosemann, M.J. Shaw, C. Szyperski, Facilitating business process improvement through personalized recommendation business information systems, in: Lecture Notes in Business Information Processing, Springer, Berlin Heidelberg, 2011, pp. 136–147.

[46] A. Shakery, C. Zhai, Smoothing document language models with probabilistic term count propagation, Information Retrieval 11 (2) (2008) 139–164.

[47] J. Shen, W. Shen, X. Fan, Recommending experts in Q&A communities by weighted HITS algorithm, in: Q.H. Zhou (Ed.), 2009 International Forum on Information Technology and Applications, Vol. 2, Proceedings, IEEE Computer Soc, Los Alamitos, 2009, pp. 151–154.

[48] Y. Sun, C.L. Giles, Popularity weighted ranking for academic digital libraries, in: 29th European Conference on Information Retrieval Research, Rome, Italy, 2007.

[49] Y.H. Sun, J. Ma, Z.P. Fan, J. Wang, A group decision support approach to evaluate experts for R&D project selection, IEEE Transactions on Engineering Management 55 (1) (2008) 158–170.

[50] J. Tang, J. Zhang, L. Yao, J. Li, L. Zhang, Z. Su, ArnetMiner: extraction and mining of academic social networks, in: Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, Las Vegas, Nevada, USA, 2008.

[51] D.W. Tank, J.J. Hop<sup>fi</sup>eld, Collective computation in neuronlike circuits, Scienti<sup>fi</sup>c American 257 (6) (1987) 104–114.

[52] P. Velardi, P. Fabriani, M. Missikoff, Using text processing techniques to automatically enrich a domain ontology, in: Proceedings of the International Conference on Formal Ontology in Information Systems New York, 2001.

Dr. Yunhong Xu is an Assistant Professor of Information Systems at the Kunming University of Science and Technology. She received her Ph.D. in Information Systems at the City University of Hong Kong and Ph.D. in Management Science at the University of Science and Technology of China. Her research interests include Network Analysis, Knowledge Recommendation and Business Analytics.

Dr. Xitong Guo is an Associate Professor of Information Systems at the Harbin Institute of Technology. He received his Ph.D. in Information Systems at the City University of Hong Kong and Ph.D. in Management Science at the University of Science and Technology of China. His current research focuses on collaborative process management, IT enabled innovation, e-Health and social computing. He has published in journals such as Journal of Management Information Systems, Electronic Commerce Research and Applications, etc.

Dr. Jinxing Hao received his Ph.D. in Business Information Systems from the City University of Hong Kong and Master in Informatics from Wuhan University. His research interests include Business Intelligence and Analytics, Knowledge Management, e-Learning and Social Search.

Dr. Jian Ma is a Professor in the Department of Information Systems, City University of Hong Kong. He received his Doctor of Engineering degree in Computer Science from Asia Institute of Technology, Dr, Ma's research areas include Decision and Decision Support Systems, Business Intelligence, Research Information Systems, Research and Innovation Social Networks. His past research has been published in IEEE Transactions on Engineering Management, IEEE Transactions on Education, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems, Information and Management, and European Journal of Operational Research.

Dr. Raymond Lau is an Assistant Professor in the Department of Information Systems at the City University of Hong Kong. His research interests include Information Retrieval, Text Mining, Automated Negotiation and Agent-Mediated e-Commerce. He is a Senior Member of the IEEE and the ACM respectively.

Dr. Wei Xu received his Ph.D. from the Chinese Academy of Sciences. His research interests include Complex Network Modeling, Intelligent Information Systems and Meta-Synthesis Forecasting.
