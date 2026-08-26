---
otero_id: 14492
otero_key: "EHFNRXFH"
title: "Fraud detection: A systematic literature review of graph-based anomaly detection approaches"
authors: "Tahereh Pourhabibi; Kok-Leong Ong; Booi H. Kam; Yee Ling Boo"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113303"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fraud detection: A systematic literature review of graph-based anomaly detection approaches

![](/api/attachments/EHFNRXFH/fulltext/images/62cec38bc69177686ac2d71061dd63337bc670afe8bc74760009e922ce34ef4e.jpg)

Tahereh Pourhabibi<sup>a,⁎</sup>, Kok-Leong Ong<sup>b</sup>, Booi H. Kam<sup>a</sup>, Yee Ling Boo<sup>a</sup>

<sup>a</sup> School of Accounting, Information Systems and Supply Chain, RMIT University, Melbourne, Australia <sup>b</sup> Centre for Data Analytics and Cognition, La Trobe University, Melbourne, Australia

## A R T I C L E I N F O

Keywords: Fraud detection Graph-based anomaly detection Graph data Systematic literature review Social network Big data analytics

## A B S T R A C T

Graph-based anomaly detection (GBAD) approaches are among the most popular techniques used to analyze connectivity patterns in communication networks and identify suspicious behaviors. Given the diferent GBAD approaches proposed for fraud detection, in this study, we develop a framework to synthesize the existing literature on the application of GBAD methods in fraud detection published between 2007 and 2018. This study aims to investigate the present trends and identify the key challenges that require significant research efforts to increase the credibility of the technique. Additionally, we provide some recommendations to deal with these challenges.

## 1. Introduction

Advances in communication and digital technologies have created a highly connected world [1]. Diferent types of networks – social media, e-commerce websites, blogs, industry trading networks, telecommunication networks, banking networks, and insurance networks – have emerged, generating an increasing volume of data among them [1]. These networks ofer a vast array of information easily accessible via anonymous accounts, making them easy platforms for misinformation, mischiefs, and misdemeanors: fraudsters and attackers can conceal their malicious activities within the mountains of data [2]. With the relentless growth of such networks, opportunities for fraud sters to manipulate them for their benefits have also expanded [2].

Until recently, social networks have been relatively “relaxed” regarding third parties gaining access to their users' details. This allows fraudsters to engage in deceptive and destructive activities, such as enabling sexual predators to interact with unsuspecting vulnerable youngsters [3] or foreign interests to influence election outcomes [4]. Other networks have also been targets of fraudulent manipulations. For instance. in the United States. fraudulent claims in healthcare and in: surance led to financial losses amounting to \$98 billion [5] and \$300 billion [6] a year, respectively.

Not surprisingly, many organizations have been spending considerable resources, including the adoption of technologies and sophisticated mechanisms, to protect their networks and data from internal and external threats [7,8]. Specifically, attention has been directed to examining the interactions and activities of business clients or users within a network [9]. These interactions, which are represented as interdependencies and relationships between data objects in graphs,<sup>1</sup> are analyzed using data mining and machine learning techniques to detect possible embedded anomalies to be flagged as potential frauds [9].

In the era of Big Data, detecting fraudulent activities within networks is analogous to finding a needle in a haystack. Graph-based anomaly detection (GBAD) approaches, a branch of data mining and machine learning techniques that focuses on interdependencies between diferent data objects, have been increasingly used to analyze relations and connectivity patterns in networks to identify unusual patterns [1]. In recent years, GBAD techniques have considerably contributed to identifying fraudulent activities within networks and have been recognized by fraud detection experts as robust, reliable, and promising anomaly detection techniques [1,9].

There have been several comprehensive survey studies on anomaly detection [10], anomaly detection using graph-based methods [3,9,11,12], and anomaly detection for fraud detection [13–15]. However, our investigation suggests that no study has conducted review studies of GBAD techniques that consider the interdependencies between diferent data objects in a graph to detect fraudulent activities. Furthermore, none of these studies have provided an in-depth exploration of graph-based methods for graph data in fraud detection. In this study, we aim to consolidate existing research know-hows in the context of analyzing interdependent data objects in a graph for fraud detection using GBAD, making this review notably diferent from other survey studies on the subject.

We focus on research undertaken between 2007 and 2018 to pro vide a synthesized understanding of the state-of-the-art GBAD methods, identify key research issues raised against application contexts, and establish future directions to expand GBAD research in fraud detection. To achieve these objectives, we focus on studies using GBAD techniques with data containing interrelations between actors (nodes) in the net work. Additionally, to synthesize existing works, we develop a classification framework, which also serves as our analytic platform in identifying gaps and challenges to aid in further studies.

## 2. Overview of surveys on GBAD methods

Over the past few years, several survey articles on anomaly detection methods [10], anomaly detection for fraud detection [13–15], and application of graph-based methods on anomaly detection [3,9,11,12] have been published. Our focus is to review papers on anomaly detection using graph-based methods. As such, the review study by Chandola et al. [10], who surveyed diferent anomaly detection techniques on multidimensional data, existing challenges in anomaly de tection, and diferent types of detected anomalies in various application areas, is considered outside our scope of review. Likewise, the review studies by Abdallah et al. [14], Bhattacharyya et al. [13], and Ngai et al. [15], which specifically examined anomaly detection techniques to detect fraud in multidimensional data within various financial sectors, also belong to a diferent domain.

Our focus on anomaly detection studies using graph-based methods aligns with the studies conducted by Savage et al. [3], Akoglu et al. [9], Anand et al. [11], and Ranshous et al. [12].

Savage et al.'s [3] review primarily focused on existing computational techniques for detecting diferent types of anomalies (such as anomalous nodes, edges, or subgraphs) in online social networks (OSNs). They summarized the process of anomaly detection in OSNs in two steps: (i) selection and calculation of network features and (ii) classification of observations from this feature space. Owing to the lack of publicly available datasets, the reviewers also noted that the proposed solutions were tested on a limited number of datasets. This limitation led them to question if the solutions might be “over-fitted” to a particular type of anomaly, and therefore, the results may not be applicable across an extensive range of datasets or problems.

Akoglu et al. [9] also surveyed GBAD approaches by focusing on existing dificulties in anomaly detection and the importance of graph based methods to resolve the proposed challenges. They analyzed the technical characteristics and definitions of these approaches and dis cussed the application of GBAD methods in several real-world scenarios, including fraud detection.

In their conference paper, Anand et al. [11] reviewed several studies in anomaly detection in OSNs and classified them into two major categories: behavior-based methods, which analyze user behavior and interactions, and structure-based approaches, which focus on identi fying special types of network structures, such as cliques, clusters or communities, stars, and ego nets. In Ranshous et al.'s [12] review, anomaly detection in dynamic social networks was the main focus, covering a critical discussion on the technical aspects of existing methods and types of detected anomalies.

However, none of these reviews explicitly scrutinized the application of graph-based methods in fraud detection to identify recent pro. blems and challenges, a gap that this paper aims to fill. Through a rigorous systematic literature analysis, we map out the research trends, methods, and key challenges when using GBAD methods in fraud de tection. We present an overview of the current state-of-the-art GBAD methods in detecting frauds but exclude the technical details of the

GBAD methods employed.

Our review of existing works contributes to four areas of GBAD research in fraud detection. First, we propose a classification framework to categorize GBAD research studies and spotlight challenges. The proposed framework ofers a systematic probe for researchers and provides an in-depth understanding of how GBAD techniques can be used to analyze and detect frauds.

Second, we synthesize the findings of extant literature into a cataloging framework (see Table 3) to enable practitioners to appreciate the correspondence between the nature of their data network, types of anomalies, and appropriate graph-based methods that suit the needs of their specific application areas.

Third, this paper highlights the existing trends and significant challenges in fraud detection using GBAD approaches. Additionally, it suggests directions for future research to minimize the impact of the highlighted issues.

Finally, we outline possible future research directions in applying GBAD techniques to fraud detection in emerging areas, such as the financial technology (FinTech) industry [16], which is vulnerable to various forms of online fraud as it starts to grow rapidly.

## 3. Research methodology

In this study, we adopted Booth et al.'s [17] systematic approach to literature review and followed the three-phase methodology employed by Ngai et al. [15,18], as depicted in Fig. 1.

The first phase is “research definition.” It includes identifying the research area, formulating review goals, and defining the research scope. The research area in this review is “fraud detection” with three main goals: (1) to identify current trends, (2) to highlight current challenges and provide directions for future research, and (3) to introduce a classification framework for analyzing current studies. The scope covers studies that have employed GBAD techniques.

The second phase is “research methodology,” which starts with identifying scientific databases hosting articles related to our research context. Five major online scientific databases were selected: ScienceDirect, ACM Digital Library, IEEE Xplore, Springer, and ABI/ Inform. The literature search process began with the creation of criteria to determine the articles to include in, or exclude from, our analysis. Following Ngai et al. [15.18] and Frost [19], we set four criteria, sti pulating that the article must (1) be published in a peer-reviewed academic research journal, (2) be written in English, (3) be published between 2007 and 2018, and (4) have its full text available in at least one of the five databases.

To achieve a more efective and comprehensive search strategy, we employed Boolean expressions to combine three terms: “graph,” “anomaly detection,” and “fraud detection” (i.e., “graph” AND “anomaly detection” AND “fraud detection”). A total of 585 papers met the inclusion criteria. Then, we pruned the papers through a two-step process. The first step (“Abstract Reading and Skimming”) involved reading titles and abstracts, which resulted in eliminating 428 unrelated papers, white papers, and tutorials, 12 duplicated titles, and 80 literature review articles. The remaining 65 papers underwent secondlevel pruning, accomplished by “Reading the Whole Article.” This process eliminated another group of 26 unrelated papers, leaving 39 papers for the final analysis.

For the final “classification and analysis” phase, we applied a series of guided questions to sort the 39 papers, similar to the approach adopted by Chan et al. [20]. To ensure the reliability of the classification, each paper was independently reviewed by two authors. Classification discrepancies (e.g., incompatibility in the type of detected anomaly or nature of the input network (see Table 3)) were resolved by having the third author read the paper. The guided questions used were as follows:

![](/api/attachments/EHFNRXFH/fulltext/images/97471ee769bf654a56ac5ea0098354499cda909a94a559a28b0922c5f78f6194.jpg)  
Fig. 1. Systematic literature review process.

1. What were the study trends and focus?

2. How did the availability of existing labeled data influence the choice of anomaly detection techniques used in diferent studies?

3. What were the types of analyzed networks?

4. What were the types of detected anomalies?

5. What were the principal graph-based methods used?

6. What were the representation methods used?

7. What were the available research data samples?

8. What were the measures used to evaluate the findings?

9. What were the contributions of the studies, challenges faced during the research, and possible future directions?

The first six questions provide six distinct levels of analysis set within the data samples available for experimental studies (Question 7) and the range of measures used for evaluating the findings (Question 8). We structured the eight questions into a hierarchical classification framework to systematically categorize the 39 papers selected for review (see Fig. 2). The last question, Question 9, does not constitute part of the classification framework. It is included to remind us to compile the challenges identified by the review studies, including suggested directions for future research. The next section explains the classification framework developed based on the above-proposed questions.

## 4. Classification framework

Along with the sequence of the nine guiding questions stated in Section 3, the proposed classification framework begins with identi fying the domain of interest (i.e., study trends and focus). The other five components of this framework (Questions 2–6) are described below.

## 4.1. Availability of data labels

Depending on the available data labels, anomaly detection approaches are classified into three broad categories: (i) supervised, (ii) unsupervised, and (iii) semi-supervised [10]. Table 1 presents the comparison of the characteristics of the three approaches.

## 4.2. Nature of the input network

With GBAD approaches, the nature of the input network can influence the process of anomaly detection and design of the algorithm. As outlined in Table 2, these features include (i) information propagation in the network (such as the direction of links, and the time the links were established), (ii) node characteristics (such as node types and node attributes), and (iii) peer influences (such as link structures and link attributes) [22].

## 4.3. Types of anomalies

Various GBAD approaches have been designed to detect diferent anomalies. These methods [12,26] detect anomalies in various networks, such as dynamic or static graphs (attributed or unattributed) by capturing (a) anomalous nodes, (b) edges, (c) subgraphs, and (d) events. Therefore, the type of anomaly is a critical characteristic of our classification framework.

Anomalous nodes are a subset of nodes where every node in the subset has an irregular feature in comparison with the other nodes in the graph. Typically, each node is assigned an anomaly score based on its characteristics (e.g., the ratio of input/output degree and ego net density) [12,26]. Similar to anomalous nodes, anomalous edges are a

![](/api/attachments/EHFNRXFH/fulltext/images/8f9924eac483140b3abb702535da72cfb1230aaa158c43a222c2439d64b5d5a0.jpg)  
Fig. 2. Framework for the literature analysis and classification of GBAD fraud detection papers. Note: Numbers refer to the subsections in this paper, e.g., 4.5 means Section 4.5 of this paper.

Characteristics of the anomaly detection approaches based on the available data labels.

<table><tr><td>Supervised [13,21]</td><td>Unsupervised [14]</td><td>Semi-supervised [14]</td></tr><tr><td>Require labeled data samples of legitimate and fraudulent samplesBuild models based on patterns revealed in existing data samplesUnable to detect unseen suspicious activities</td><td>Do not need labeled data samplesAble to detect unseen suspicious activities</td><td>Use both labeled and unlabeled samplesRequires a few instances of labeled samplesAble to detect unseen suspicious activities</td></tr></table>

## Table 2

Characteristics of the diferent types of input networks.

<table><tr><td>Types of input network</td><td>Characteristics</td></tr><tr><td>Simple [23]</td><td>- One subset of nodes</td></tr><tr><td>vs.</td><td></td></tr><tr><td>Bipartite [23]</td><td>-Two disjoint subsets of nodes</td></tr><tr><td>Homogeneousa[23]</td><td>- One type of node or link</td></tr><tr><td>vs.</td><td>- Different types of nodes or links</td></tr><tr><td>Heterogeneousb[24]</td><td>- Difficult to detect suspicious activities [25]</td></tr><tr><td>Directed [23]</td><td>- Symmetric relations between nodes</td></tr><tr><td>vs.</td><td>- Asymmetric relations between nodes</td></tr><tr><td>Undirected [23]</td><td></td></tr><tr><td>Static [9,12]</td><td>- A single snapshot of a network [26]</td></tr><tr><td>vs.</td><td>- Structure constantly changing over time [9]</td></tr><tr><td>Dynamic [9,12]</td><td>- More difficult to analyze anomalies [9,12,26]</td></tr><tr><td>Attributed [9,12,26]</td><td>- Nodes or links with attributes</td></tr><tr><td>vs.</td><td>- Attributes revealing considerable information</td></tr><tr><td>Unattributed</td><td>regarding the network entities and their interactions [27]</td></tr><tr><td></td><td>- No attribute assigned to either nodes or links</td></tr></table>

subset of edges where every edge exhibits abnormal behavior, i.e., having scores higher than a specific threshold. This characteristic, in turn, suggests the existence of an anomaly, such as anomalous nodes. By contrast, the approach to finding an irregular subgraph is quite diferent. Typically, subgraphs are first identified by community detection methods (see Section 4.4), and then each subgraph is assigned an anomaly score based on intra-graph comparisons (see Noble and Cook [28] for more information). The last anomaly type is event and change detection. This type of anomaly is exclusively found in dynamic networks and designed to locate the specific time period(s) in which activities are significantly diferent from those in the rest of the periods [12].

## 4.4. Graph methods

Graph methods include the machine learning algorithm(s) that are applied to the networks to detect diferent types of anomalies. Depending on the available data labels, nature of the input network, and types of anomalies that are to be discovered in a network, prior studies have captured diferent anomalies across five approaches, as described in Fig. 3.

<sup>a</sup> Also called simple, simplex, or monoplex.

![](/api/attachments/EHFNRXFH/fulltext/images/2f1a088fc04c041448d721413d1319b67174efb5781ab706db3c1ea6dff3dd42.jpg)  
Fig. 3. Five diferent types of GBAD approaches.

## 4.5. Structural representation

The success of graph methods depends on the choice of data representation being used [29,30]. Generally, feature engineering and graph representation learning (also called graph embedding) techniques aim to embed the structural representation of a graph into a vector space (or feature space), in which the machine learning models are then built [29]. Therefore, defining measures that can best map a network structure into a vector space is highly important. This method help preserve the topological and structural characteristics of nodes and network information, which can then be more explicitly analyzed by machine learning methods to detect anomalies [29].

Feature engineering is a useful way of capturing human ingenuity and prior knowledge [31]. In this technique, features are designed based on analysts' foreknowledge regarding the network entities and known suspicious activities. These features range from simple attri butes, such as in-degree,<sup>2</sup> out-degree,<sup>3</sup> and reciprocity, to more complex ones, such as clustering coeficients<sup>4</sup> [32]. Thus, the learning algorithms in feature engineering are highly dependent on human intervention, creating scalability problems. In recent years, GBAD researchers have started developing new methods, such as graph representation learning or graph embedding techniques [33], that aim to build graph structures without any human intervention. These techniques use diferent methods, such as deep learning [29,34], to quickly construct models and reveal hidden explanatory factors previously unknown to security experts.

## 5. Findings and discussions

Using the proposed classification framework (Fig. 2), we cataloged the 39 reviewed papers into five areas: graph methods, application areas, data label availability, input network, and types of anomalies (see Table 3). This cataloging aims to increase the understanding of a particular type of GBAD method while dealing with certain application areas and support researchers to explore which approach or paper to focus on when looking for specific types of anomalies in accordance with the nature of their input network and availability of their data labels. We discuss the findings of our review following the guiding questions presented in Section 3.

## 5.1. Research trends and focus

Fig. 4 shows the distribution of the 39 studies analyzed from 2007 to 2018 (none of the 39 papers reviewed were published in 2007 and 2008). This finding suggests a growing trend in the application of GBAD techniques for fraud detection.

Our analysis suggests that studies using GBAD methods to detect fraudulent activities generally fall into two major streams: traditional and OSNs (Fig. 5). The traditional stream, with applications in insurance [37,46,59], telecommunication [51], banking [45,46], online credit applications (OCA) [66], anti-money laundering (AML) [38], retail holding [53], trading [47], and internal organizational fraud (IOF) [67,68], has heavily relied on GBAD methods to analyze its data. However, the data used in these studies were not explicitly linked together. These studies have used graph data to detect fraud by inferring the links within the data. This growing trend is becoming significant and demonstrates the applicability and importance of GBAD methods for fraud detection in various applications.

Although research studies using GBAD methods are still sparse, the eforts devoted to detecting frauds in insurance and banking applications have become prevalent since 2017. Fig. 6 shows the diversity of research studies applying GBAD techniques on fraud detection by research area during the selected period. Since 2014, the analysis of OSNs where data are inherently linked to one another in networks [54,69,70] has also become an emerging stream. This observation implies the increasing popularity of online social activities. As businesses turn to social media to promote their products and services, they also create an additional opportunity and a fertile channel for fraudsters to conduct malicious activities [71]. For example, fake reviewers can earn between \$0.5 and \$3 for each fake review [71] by demoting or promoting a product, service, or business. As the range of online social activities increases, the possibility of diferent types of fraud in such networks also grows, necessitating a need to filter any suspicious behavior to mitigate the consequences.

## 5.2. Availability of data labels

From the data label perspective, approximately 87.2% of the reviewed research studies have exclusively developed their models using unsupervised learning techniques. The reason is that data labels are often in short supply or nonexistent in many real-world problems, such as fraud detection [14]. Consequently, unsupervised learning techniques have been the focus of many research studies. There are exceptions, such as Shehnepoor et al.'s [63] work, which can be applied in unsupervised and semi-supervised settings (2.6%), and the works of Bangcharoensap et al. [50] and Molloy et al. [46], which both exclusively used a semi-supervised-based approach. From our review, only 5.1% of the studies applied supervised learning methods.

Table 3  
Cataloging of graph-based fraud detection<sup>a</sup>.

<table><tr><td>Graph methods</td><td>Application areas</td><td>Reference</td><td>Availability of data labels</td><td colspan="4">Nature of the input network</td><td>Types of anomalies</td></tr><tr><td rowspan="7">Structural-based</td><td rowspan="3">OSN</td><td>[35]</td><td>US</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>SG</td></tr><tr><td>[2]</td><td>US</td><td>BH</td><td>ST</td><td>UD</td><td>UA</td><td>SG</td></tr><tr><td>[36]</td><td>US</td><td>SH</td><td>DY</td><td>UD</td><td>UA</td><td>N</td></tr><tr><td rowspan="2">Insurance</td><td>[5]</td><td>S</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>N</td></tr><tr><td>[37]</td><td>US</td><td>SH</td><td>ST</td><td>UD</td><td>A</td><td>N</td></tr><tr><td rowspan="2">AML</td><td>[38]</td><td>US</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>SG</td></tr><tr><td>[39]</td><td>US</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>N</td></tr><tr><td rowspan="12">Community-based</td><td rowspan="3">OSN</td><td>[40], [41,42]</td><td>US</td><td>BH</td><td>ST</td><td>UD</td><td>A</td><td>SG</td></tr><tr><td>[43]</td><td>US</td><td>SH</td><td>DY</td><td>D</td><td>A</td><td>SG</td></tr><tr><td>[44]</td><td>US</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>SG</td></tr><tr><td>AML</td><td>[45]</td><td>US</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>SG</td></tr><tr><td>Banking</td><td>[46]</td><td>SS</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>SG</td></tr><tr><td>Trading</td><td>[47]</td><td>US</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>SG</td></tr><tr><td>IOF</td><td>[48]</td><td>US</td><td>SH</td><td>ST</td><td>UD</td><td>UA</td><td>SG</td></tr><tr><td rowspan="2">Online Auction</td><td>[49]</td><td>US</td><td>BH</td><td>ST</td><td>UD</td><td>A</td><td>SG</td></tr><tr><td>[50]</td><td>SS</td><td>BH</td><td>ST</td><td>UD</td><td>A</td><td>SG</td></tr><tr><td rowspan="2">Telecom</td><td>[51]</td><td>US</td><td>SH</td><td>ST</td><td>UD</td><td>UA</td><td>SG</td></tr><tr><td>[52]</td><td>S</td><td>BH</td><td>DY</td><td>UD</td><td>A</td><td>SG</td></tr><tr><td>Retail Holding</td><td>[53]</td><td>US</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>SG</td></tr><tr><td rowspan="3">Decomposition-based</td><td rowspan="3">OSN</td><td>[54,55]</td><td>US</td><td>SH</td><td>DY</td><td>D</td><td>A</td><td>SG</td></tr><tr><td>[56]</td><td>US</td><td>SH</td><td>DY</td><td>D</td><td>A</td><td>N</td></tr><tr><td>[57]</td><td>US</td><td>SH</td><td>DY</td><td>D</td><td>A</td><td>N, SG</td></tr><tr><td rowspan="3">Compression- based</td><td>Trading</td><td>[7,8]</td><td>US</td><td>SH</td><td>ST</td><td>D/UD</td><td>A/UA</td><td>SG</td></tr><tr><td>OSN</td><td>[27]</td><td>US</td><td>BH/SH</td><td>ST</td><td>UD</td><td>A</td><td>N</td></tr><tr><td>Insurance, AML, Banking, Trading</td><td>[58]</td><td>US</td><td>BH/SH</td><td>ST</td><td>UD/D</td><td>A</td><td>N</td></tr><tr><td rowspan="10">Probabilistic-based</td><td rowspan="2">Insurance</td><td>[59]</td><td>US</td><td>BH</td><td>ST</td><td>UD</td><td>A</td><td>N</td></tr><tr><td>[60]</td><td>US</td><td>SH</td><td>ST</td><td>D</td><td>A/UA</td><td>N, SG</td></tr><tr><td rowspan="4">OSN</td><td>[61]</td><td>US</td><td>BH</td><td>ST</td><td>UD</td><td>A</td><td>N</td></tr><tr><td>[62]</td><td>US</td><td>BH</td><td>DY</td><td>UD</td><td>UA</td><td>N</td></tr><tr><td>[63]</td><td>US, SS</td><td>BH</td><td>ST</td><td>UD</td><td>A</td><td>N</td></tr><tr><td>[64]</td><td>US</td><td>SH</td><td>DY</td><td>D</td><td>A</td><td>SG</td></tr><tr><td>Online auction</td><td>[65]</td><td>US</td><td>BH</td><td>ST</td><td>UD</td><td>A</td><td>SG</td></tr><tr><td>OCA</td><td>[66]</td><td>US</td><td>SH</td><td>DY</td><td>D</td><td>A</td><td>E</td></tr><tr><td rowspan="2">IOF</td><td>[67]</td><td>US</td><td>SH</td><td>ST</td><td>D</td><td>A</td><td>N</td></tr><tr><td>[68]</td><td>US</td><td>SH</td><td>DY</td><td>D</td><td>A</td><td>SG</td></tr></table>

SH, simple and homogenous; BH, bipartite and heterogeneous;  
DY, dynamic; ST, static;  
D, directed; UD, undirected;  
A, attributed; UA, unattributed;  
S, supervised; U, unsupervised; SS, semi-supervised;  
N, node; SG, subgraph; E, edge; EV, event;  
AML, anti-money laundering; IOF, internal organizational fraud; OCA, online credit application.  
<sup>a</sup> Note:  
(1) Graph representation learning was only used in decomposition-based methods in [54,56].  
(2) Studies that model the input network as a bipartite graph are heterogeneous networks with diferent types of nodes and the rest of the studies are homogeneou networks.  
(3) None of the reviewed studies worked on anomalous event detection.

![](/api/attachments/EHFNRXFH/fulltext/images/17fdc2f33979f5e1b4461ee11c96b1b7c1d433a5722e8fd97aa610a3e3bde854.jpg)  
Fig. 4. Distribution of papers reviewed, 2009–2018.

![](/api/attachments/EHFNRXFH/fulltext/images/5da05d79d007b669398577be6e78d4a6ef44ab990973ae7f8cad89d6cebd0e16.jpg)  
Fig. 5. Data nature and application areas of GBAD techniques for fraud detection.

![](/api/attachments/EHFNRXFH/fulltext/images/8b45d39c87f34840e53112a6c14ebd5cf77807481e5e7bf6b9f83ae3faecda9a.jpg)  
Fig. 6. Distribution of research studies using GBAD techniques for fraud detection, 2009–2018.

The shortcomings related to supervised and semi-supervised learning techniques, as outlined in Section 4.1, may hinder the use of GBAD approaches in some cases. These methods are among the least commonly used methods found in this review.

## 5.3. Nature of the input network

The nature of the input network is a fundamental feature of GBAD approaches. Therefore, we unpack them into several units of analysis, which are described in this section.

## 5.3.1. Simple vs. bipartite

Among the papers that modeled the input network as a bipartite graph, the most represented application is OSNs with 20.5% (8 of the 39 papers). The other applications are insurance (5.1%; two papers), auction (7.7%; three papers), and telecommunication fraud detection (2.6%; one paper). We can explain this finding based on the nature of the above application areas, where the connections between users and products or services should be analyzed to detect suspicious behaviors (e.g., the number of parties bidding a seller's product in auction fraud, number of ratings to a product in online business websites, and claims submitted by a specific insurance provider). The remaining 25 papers analyzed user-to-user connections (e.g., the number of messages sent by a specific user to others) to detect suspicious activities, thus modeling their input network as simple graphs.

## 5.3.2. Homogeneous vs. heterogeneous

The reviewed research papers on OSNs, insurance, and auction frauds have extensively considered the analysis of suspicious activities in bipartite networks. These studies model bipartite networks using two different sets of nodes, mainly users and products or users and services. These networks are considered heterogeneous networks with diferent types of nodes (Table 3). Among the studies, only two [27,44] have considered different types of activities (e.g.. different types of links). However, in [44], each type of relationship was simulated as a simple network and analyzed separately. Another study [27] also simulated the input network as a heterogeneous bipartite network. As mentioned in Section 5.3.1, 25 papers investigated users' behavior on simplex networks and only considered one type of user activity, thus ignoring the inherent multiplex nature of human interactions in their analysis [25]. These studies did not consider diferent types of users' activities in the network to detect suspicious activities (see Section 4.2).

## 5.3.3. Directed vs. undirected

As the information summarized in Table 3 indicates, approximately 48.7% of the research studies are solely applied to directed networks, 43.6% are practiced only on undirected networks, and the remaining 7.7% are applied to directed and undirected networks.

Studies modeling their input network as an undirected network mainly explore user-to-product or user-to-service relationships and are mostly bipartite networks (14 of the reviewed papers employed bipartite networks).

## 5.3.4. Static vs. dynamic

In recent years, dynamic networks have increased in popularity owing to their applications in social networks, insurance, and online banking [54,56,66,68]. The relentless growth of social networks, in particular, has provided opportunities for fraudsters to infiltrate these networks and spread their illusive activities by frequently establishing new connections with other users or changing their relations with existing users [72]. In other words, fraudsters can easily evade current detection mechanisms. Although the importance of analyzing dynamic networks for suspected fraud has surged, it is still a nascent research area [54,56,66,68]. Of the papers reviewed, only 28.2% of research studies worked on fraud detection in dynamic networks, whereas the remaining 71.8% (28/39) merely searched for suspicious activities in static networks.

## 5.3.5. Attributed vs. unattributed

The link and node attributes are essential elements for diferentiating users' behavior in a communication network [27]. They provide useful information for detecting anomalies in a network. Table 3 shows that only five papers that were reviewed (12.8%) ignored the importance of attributes. Among those that used attributes to distinguish suspicious activities (87.2%), most employed link attributes, such as interaction strength.

## 5.4. Graph methods and types of anomalies detected

Depending on the available data labels and nature of the input network, five diferent GBAD methods were employed to capture different types of anomalies in the network among the 39 papers reviewed. Community-based approaches were the most widely used (35.9%) with probabilistic-based methods as the second most popular approach (25.6%). Around 17.9% of the studies used structural-based techniques, whereas compression-based (10.3% of the studies) and decomposition-based approaches (10.3% of studies) were among the least-used methods (see Fig. 7).

Fraud is characteristically manifested as a collective behavior in networks, as fraudsters attempt to coordinate their behavior as a group [72]. Detection of such illusive user communities (also referred to as groups or clusters) has become a key focus. Table 3 reveals that around two-thirds of the research studies focused on identifying anomalous subgraphs. Among them, the top two GBAD methods, community-based and probabilistic-based methods, exhibited the highest share. By contrast, the other three GBAD methods were mostly used to detect the most suspicious nodes or edges within the network.

![](/api/attachments/EHFNRXFH/fulltext/images/8ab2a50b0dca96e144f9785aa780d0dcd96f02b084f1262386a43c1853380999.jpg)  
Fig. 7. Spread of diferent GBAD methods in the papers reviewed.

## 5.5. Dataset

Research studies on fraud detection have mostly used real-world data as their test platforms [73,74]. Many have also used synthetic data to simulate specific scenarios [73,74]. Owing to privacy considerations, organizations and stakeholders are reluctant to share their fraud in formation [73]. This hinders research and afects the reproducibility of the experiments conducted. One possible solution is to use synthetically created data [74]. However, generating a realistic dataset presents enormous challenges in terms of topologies, attribute values of nodes and edges, community structures, data distributions, and correlations [74]. Furthermore, the similarity between synthetically generated networks and the original networks extracted from human behavior remains unanswered.

Table 4 presents an overview of the diferent publicly available data and datasets used among the studies reviewed. It shows that 87.2% of the studies tested their approach using real-world data (34/39), of which 41.0% are publicly available for research studies (16/39). A third of the 39 studies used synthetic data. Among the studies using publicly available datasets, 81.3% used OSN data (13/16), reflecting their broad availability for anomaly detection research.

## 5.6. Evaluation measures

As presented in Table 4, research studies have used diferent mathematical measures to evaluate the outcome of their proposed al gorithms. For those with suficiently available labeled data, the classical criteria based on receiver operating characteristic (ROC) or precision–recall (PR) curves have been used to analyze the performance of the proposed algorithms. ROC curves are commonly used to present the results for binary decision problems in machine learning [75,76]. However, with highly skewed datasets, ROC does not provide much insight into the data, and PR curves tend to provide a more informative picture of an algorithm's performance. In fraud detection, the number of negative samples considerably exceeds that of positive examples. Consequently, a substantial change in the number of false positives (FPs) can lead to a small change in the FP rate used in the ROC analysis [75,76].

Furthermore, precision captures the efect of many negative examples on the algorithm's performance by comparing FPs to true positives rather than to true negatives [75,76]. F-measure is the second most commonly used performance measure. This preference over the next measure, i.e., accuracy, comes as no surprise given the nature of fraud problems. Accuracy favors true negative, which is inconsequential in fraud detection. Instead, a measure that weighs higher on false negative (FN) and FP is of better value in an uneven class dis tribution. In such cases, the F-measure is preferred as it balances precision and recall, resulting in a better evaluation of a fraud detection model. Moreover, we observe that accuracy is only used in five studies [58,62,65,67,68] (see Table 4).

Although some measures are preferred over others, no measure is perfect, and they can only serve as an approximation to a technique's performance on a specific dataset. Ideally, the evaluation is checked against authentic data sourced from the specific problem, which the fraud detection technique is designed for. However, in practice, authentic labeled datasets are in short supply or nonexistent [14]. This limitation is further complicated by the need for expert knowledge to create a labeled dataset or evaluate results during model development, a time-consuming and expensive process. As a compromise or balance, many have used a case study analysis on samples of the data as a proxy of a technique's true capability. Nevertheless, evaluating the performance of fraud detection algorithms will always be a problem given the insuficient data samples and scenarios. An alternative is to use an ensemble of fraud detectors along with computer-based knowledge sources [77]. Lastly, a recent study [78] discussed two new approaches, called excess-mass (EM) and mass–volume (MV) curves, to evaluate the performance of anomaly detection approaches on dimensional data without data labels. However, to the best of our knowledge, the two approaches have not been applied in anomaly detection or fraud detection on graph data.

## 5.7. Recommendations

Table 5 summarizes the main contributions and specific types of fraud across the 39 research studies. It highlights their problem focus, approaches to finding solutions, challenges faced in the process, and recommended directions for future studies. This table ofers a quick guide of relevant works for researchers using GBAD approaches to investigate frauds in networks, informing them of the range and nature of application problems faced, GBAD baseline approaches to consider, and unsettled areas for further investigations. In preparing Table 5, we further identified four key challenges. We propose some recommendations and considerations that serve as a scafold for the fu ture design of fraud detection mechanisms to address these challenges.

## 5.7.1. Dealing with unavailability of data

Fraud is a highly sensitive topic, and many stakeholders are reluctant to share their information on fraud. One of the major challenges in data sharing in various application areas, such as healthcare, in surance, and banking, are regulations that prohibit the transmission and distribution of highly confidential personal and financial data. This challenge poses a major obstacle in fraud detection research in sectors where data contain confidential information. Consequently, many fraud detection algorithms resort to mathematical evaluation measures, which, as we noted, are the best that we can get in a scenario where only a few databases are available for research. This issue has also urged researchers using synthetic datasets with diferent characteristics to test their solution for the problem they are looking to address. Synthetic network generators generally duplicate a small subset of the original network's properties for specific applications, such as community detection [79]. Usually, some sets of abnormal samples are injected into a predefined normal distribution of data (e.g., power-law networks) to generate synthetic data for fraud or anomaly detection [79]. If we further consider the fact that the proposed method is evaluated over mathematical measures, then the overall reliability of the empirical evaluation of a fraud detection model may not be a good reflection of the actual problem and use case [74,79,80].

The main challenge in producing synthetic datasets is to make the generated networks mimic various aspects of human behavior, including noise and randomness, as how these characteristics are incorporated will determine the realism of the simulated networks [74]. With synthetic data, the characteristics of the dataset can impact the performance of any new methods developed. Researchers should ensure that the simulated data are reflective of the actual network that the new algorithm is designed to detect fraud [74,80]. Otherwise, the performance of the algorithm evaluated within simulated environments will not reflect real-world networks [80]. Hence, we recommend evaluating algorithms on synthetic data and real-world datasets whenever possible.

Table 4  
Mapping catalog for types of datasets, public data used, and evaluation measures.

<table><tr><td>Graph methods</td><td>Application areas</td><td>Reference</td><td>Availability of data labels</td><td>Types of dataset</td><td>Types of evaluation measures</td></tr><tr><td rowspan="7">Structural-based</td><td rowspan="3">OSN</td><td>[35]</td><td>US</td><td>P (Twitter, Tencent Weibo), SY, RW</td><td>PR curve, run-time, accuracy</td></tr><tr><td>[2]</td><td>US</td><td>P (Amazon, TripAdvisor, Epinions, WikiVote), SY, RW</td><td>F-measure, run-time</td></tr><tr><td>[36]</td><td>US</td><td>RW</td><td>PR, F-measure</td></tr><tr><td rowspan="2">Insurance</td><td>[5]</td><td>S</td><td>RW</td><td>F-measure, ROC</td></tr><tr><td>[37]</td><td>US</td><td>P (Medicare-B), RW</td><td>Case study</td></tr><tr><td rowspan="2">AML</td><td>[38]</td><td>US</td><td>No experimental data</td><td>No experimental study</td></tr><tr><td>[39]</td><td>US</td><td>RW</td><td>Pearson&#x27;s correlation of features</td></tr><tr><td rowspan="14">Community-based</td><td rowspan="5">OSN</td><td>[40]</td><td>US</td><td>SY, RW</td><td>Run-time, recall, convergence time</td></tr><tr><td>[41]</td><td>US</td><td>P, SY, RW (Amazon, iTunes)</td><td>AUC of PR, NMI</td></tr><tr><td>[42]</td><td>US</td><td>P, RW (Amazon, Yelp)</td><td>Precision, F-measure, CDF</td></tr><tr><td>[43]</td><td>US</td><td>P, RW (Twitter)</td><td>Power-law analysis</td></tr><tr><td>[44]</td><td>US</td><td>P, RW (Twitter Honeypot)</td><td>TPR, FPR, PR, F-measure</td></tr><tr><td>AML</td><td>[45]</td><td>US</td><td>SY</td><td>Visual analytics</td></tr><tr><td>Banking</td><td>[46]</td><td>SS</td><td>RW</td><td>ROC</td></tr><tr><td>Trading</td><td>[47]</td><td>US</td><td>RW (Roget, Stock)</td><td>Run-time, case study</td></tr><tr><td>IOF</td><td>[48]</td><td>US</td><td>P, RW (CERT)</td><td>Case study</td></tr><tr><td rowspan="2">Online Auction</td><td>[49]</td><td>US</td><td>RW</td><td>NDCG</td></tr><tr><td>[50]</td><td>SS</td><td>RW</td><td>NDCG</td></tr><tr><td rowspan="2">Telecom</td><td>[51]</td><td>US</td><td>RW</td><td>CDF</td></tr><tr><td>[52]</td><td>S</td><td>RW</td><td>PR, F-measure, ROC</td></tr><tr><td>Retail Holding</td><td>[53]</td><td>US</td><td>RW</td><td>Case study</td></tr><tr><td rowspan="4">Decomposition-based</td><td rowspan="4">OSN</td><td>[54]</td><td>US</td><td>SY</td><td>ROC</td></tr><tr><td>[55]</td><td>US</td><td>P, RW (Yelp, Amazon, BeerAdvocate)</td><td>F-measure, ROC</td></tr><tr><td>[56]</td><td>US</td><td>P, RW (Yelp, Android, YahooM, KoWiki, ENWiki, YouTube)</td><td>ROC, detection time</td></tr><tr><td>[57]</td><td>US</td><td>P, SY, RW (Software Marketplace, Reddit)</td><td>PR, F-measure</td></tr><tr><td rowspan="4">Compression- based</td><td rowspan="2">Trading</td><td>[7]</td><td>US</td><td>SY</td><td>Case study</td></tr><tr><td>[8]</td><td>US</td><td>SY, RW</td><td>Case study</td></tr><tr><td>OSN</td><td>[27]</td><td>US</td><td>P, RW (Flipkart)</td><td>Precision</td></tr><tr><td>Insurance, AML, Banking, Trading</td><td>[58]</td><td>US</td><td>P, SY, RW (German Credit Card, ICIJ Offshore Leaks, COIL2000 insurance)</td><td>Accuracy</td></tr><tr><td rowspan="10">Probabilistic-based</td><td rowspan="2">Insurance</td><td>[59]</td><td>US</td><td>RW</td><td>Case study</td></tr><tr><td>[60]</td><td>US</td><td>RW</td><td>AUC</td></tr><tr><td rowspan="4">OSN</td><td>[61]</td><td>US</td><td>P, SY, RW (Goodreads, Buzzcity)</td><td>Precision</td></tr><tr><td>[62]</td><td>US</td><td>P, RW (Yelp)</td><td>PR, F-measure, accuracy, AP, ROC</td></tr><tr><td>[63]</td><td>US, SS</td><td>P, RW (Yelp)</td><td>AP, AUC</td></tr><tr><td>[64]</td><td>US</td><td>RW</td><td>PR, F-measure, accuracy</td></tr><tr><td>Online auction</td><td>[65]</td><td>US</td><td>SY</td><td>AUC, TPR, FPR</td></tr><tr><td>OCA</td><td>[66]</td><td>US</td><td>RW</td><td>Hit rate, TPR</td></tr><tr><td rowspan="2">IOF</td><td>[67]</td><td>US</td><td>SY, RW</td><td>Accuracy, ROC</td></tr><tr><td>[68]</td><td>US</td><td>SY, RW (CMU-CERT Insider Threat)</td><td>AUC, ROC</td></tr></table>

S, supervised; U, unsupervised; SS, semi-supervised;  
P, public datasets; SY, synthetic datasets; RW, real-world datasets;  
PR, precision–recall; ROC, receiver operating characteristics; AP, average precision; NMI, normalized mutual information; TPR, true positive rate; FPR, false positive rate;  
CDF, cumulative distribution function;  
NDCG, normalized discounted cumulative gain.

On real-world datasets, studies published to support the research community are not without their own challenges. During our review, we noted that some real-world datasets have missing elements or that only part of the dataset is made publicly available. These issues create a challenge in terms of allowing the community to efectively evaluate any new methods developed against a published piece of work that used the full dataset. Without the means to adequately benchmark new al gorithms, the progress of research in this area will be slow or limited [80].

Data anonymization can address this issue by hiding confidential information while maintaining the analytical utility of the data [81]. This technique allows data scientists and organizations to engage in a win–win collaboration. Data scientists will have the chance to analyze data in diferent areas and share their discoveries with businesses. In turn, businesses can be equipped with new fraud detection methodologies.

However, in some cases, even anonymized data have business value for the party owning them. Unauthorized disclosure of such data, as such, may damage the party owning them or other parties afected by their disclosure [82]. Here, data confidentiality still matters even after data anonymization, because clever adversaries can reidentify or deanonymize the information hidden in anonymized data by linking anonymized data to outside information to unearth the true identity of the data subjects [82]. While not suggesting that all anonymization techniques fail to protect privacy, we caution that some techniques have proven to be dificult to reverse [82]. Some researchers reject anonymization as a privacy-protecting panacea [82].

Nevertheless, this challenge should motivate us to continue to explore, or reexamine, the possibility of adapting synthetic data as an

Domain of interest, highlights of the research, challenges faced, and future directions. Table 5

<table><tr><td>Graph methods</td><td>Application areas</td><td>Reference</td><td>Focus of analysis</td><td>Highlights of approach and detection improvements</td><td>Challenges (C) and future directions (D)</td></tr><tr><td rowspan="7">Structural-based</td><td rowspan="4">OSN</td><td>[35]</td><td>Detecting synchronized behavior (suspicious nodes that have an extremely similar behavioral pattern) and rare behavior (nodes with connectivity patterns very different from the majority) to spot fake followers and fake accounts</td><td>- Effectiveness: high accuracy in spotting synchronized behaviors and catching suspicious source-target groups- Scalability: linear complexity with the number of edges- Parameter-free- Oblivious side information</td><td>D: Incorporate temporal information and other additional features</td></tr><tr><td>[2]</td><td>Spotting fraudsters in the presence of camouflage or hijacked accounts to detect fake followers and fake accounts</td><td>- Effectiveness: using sufficient condition to detect fraudsters perfectly (e.g., 100% precision and recall)- Scalability: linear complexity with the number of edges</td><td>D: Incorporate temporal information</td></tr><tr><td>[36]</td><td>Spotting suspicious behaviors in online social communities</td><td>- Scalability: scalable to a large volume of data using big data in-memory cluster computing</td><td>C: Dependent on a user-selected similarity threshold</td></tr><tr><td>[5]</td><td>Assessing healthcare fraud risk to detect fraudulent providers</td><td>- Effectiveness: F-measure of 0.919 and an ROC area of 0.960</td><td>C: Lack of providers known to have committed healthcare fraudD: Include additional types of information relevant to healthcare fraud prediction</td></tr><tr><td rowspan="2">Insurance</td><td></td><td>[37]</td><td>Analyzing healthcare fraud to detect fraudulent insurance claims</td><td>- Effectiveness: detecting previously unreported anomalies</td></tr><tr><td></td><td>[38]</td><td>Detecting patterns of money laundering and financing terrorism</td><td>- Incorporating fuzzy concepts</td></tr><tr><td>AML</td><td></td><td>[39]</td><td>Detecting patterns of money laundering to assess risk profiles of clients involved in the factoring business</td><td>- Introducing a predictive (rather than just a detective model) model for AML- Using a visual analysis of network data for any suspiciousness detection</td></tr><tr><td rowspan="12">Community-based</td><td rowspan="5">OSN</td><td>[40]</td><td>Detecting fraud in Internet advertising for crowd fraud detection</td><td rowspan="2">- Requiring nearly no human interaction- Scalability: scalable to a large volume of data- Effectiveness: accuracy over 90%- Effectiveness: NMI of over 0.94 for various settings and over 0.95 AUC of PR curve on synthetic data and high accuracy on real-world data- Robustness: robust with a variety of parameters, so it requires almost no tweaking of parameters to work correctly</td><td rowspan="2">C: Use user-defined parameters that depend on data from past events</td></tr><tr><td>[41]</td><td>Detecting opinion spammer groups in the existence of camouflage</td></tr><tr><td>[42]</td><td>Detecting product review spammers</td><td>- Effectiveness: outperforming baselines over all databases used in experiments</td><td>C: Evaluate the annotation of a huge volume of review data manuallyC: Sloppiness in user evaluation</td></tr><tr><td>[43]</td><td>Analyzing re-tweeting to find fake users in the presence of camouflage</td><td>- Introducing RTGEN, a scalable realistic synthetic data generator</td><td>C: Spot long-term spam activities in the presence of camouflage</td></tr><tr><td>[44]</td><td>Analyzing tweeting activities for spamming community detection</td><td>- Effectiveness: outperforming baseline methods with a precision, recall, F-measure, and TP rate over 0.85 and FP rate of 0.132</td><td>D: Evaluate the approach based on more realistic data</td></tr><tr><td>AML</td><td>[45]</td><td>Analyzing mobile payments to detect money laundering</td><td>- Introducing an interactive visualization application</td><td rowspan="2">C: Use limited visualization techniques</td></tr><tr><td>Banking</td><td>[46]</td><td>Analyzing payment transactions for cross-channel frauds</td><td>- Effectiveness: reducing FPR by 63%</td></tr><tr><td>Trading</td><td>[47]</td><td>Analyzing trading ring patterns to discover cross-account collaborative fraud for market manipulation</td><td>- Scalability: several orders of magnitude faster than the baseline</td><td>C: Correlate user behaviors across multiple trading accounts</td></tr><tr><td>IOF</td><td>[48]</td><td>Analyzing enterprise users&#x27; web access pattern to detect insider threats</td><td>- Introducing an interactive visualization application</td><td>C: Rely on some user-defined threshold parameter that should be refined</td></tr><tr><td rowspan="2">Online Auction</td><td>[49]</td><td>Analyzing the social graph of online auction users to detect auction fraud</td><td>- Effectiveness: detects suspicious nodes as the compared baseline</td><td rowspan="2">C: Detect the homophilic behavior of auction fraudsters who frequently bid in auctions hosted by a seller(s) working in the same collusion group</td></tr><tr><td>[50]</td><td>Analyzing the social graph of online auction users to detect auction fraud</td><td>- Effectiveness: outperforming baseline with 5.3% in NDCG- Scalability: parallelize in MapReduce</td></tr><tr><td>Telecom</td><td>[51]</td><td>Analyzing voice calls to detect fraud in a cellular network</td><td>- Effectiveness: detecting 85% of all the victims and the root cause of 78% of fraud calls</td><td>D: Apply additional (expensive) approaches, e.g., incorporating billing information, manual investigation,</td></tr></table>

Table 5 (continued) (continued on next page)

<table><tr><td>Graph methods</td><td>Application areas</td><td>Reference</td><td>Focus of analysis</td><td>Highlights of approach and detection improvements</td><td>Challenges (C) and future directions (D)</td></tr><tr><td rowspan="2"></td><td></td><td>[52]</td><td>Detecting telecom fraud</td><td>- Effectiveness: outperforming baseline methods with a precision, AUC, and F-measure over 0.80 and recall over 0.74</td><td>user calls history, and instant user fraud reports to analyze the detection results to further confirm the fraud activitiesC: Analyze varieties of callers&#x27; and callees&#x27; behaviors in the telecom network to capture all types of telecom fraud</td></tr><tr><td>Retail Holding</td><td>[53]</td><td>Detecting fraudulent transfer pricing when two subsidiaries agree to overprice imports or underprice exports to declare less profit to pay less tax</td><td>- Using data visualization to find hot spots for fraud</td><td>C: Rely on data quality and availability to reveal internal relations between companies and their affiliated domain users</td></tr><tr><td rowspan="3">Decomposition-based</td><td rowspan="3">OSN</td><td>[54][55]</td><td>Detecting random link attackers Detecting suspicious spikes of bursts and drops, in the existence of camouflage</td><td>- Effectiveness: low false negatives Scalability: sub-quadratic time complexity- Effectiveness: achieving higher accuracy than the competitors</td><td rowspan="3">C: Rely on some historical data for further analysisC: Aggregate suspiciousness signals from different attributes</td></tr><tr><td>[56]</td><td>Analyzing stream changes in tensors for fake rating detection</td><td>- Scalability: a million times faster- Effectiveness: detecting previously unreported anomalies</td></tr><tr><td>[57]</td><td>Analyzing dense blocks in tensors to detect bot-like behaviors</td><td>- Scalability: linearly scalable with the size of the data- Generalizability: being applied to a variety of domains- Effectiveness: scoring the suspicious entities with high accuracy and detected previously unreported anomalies</td></tr><tr><td rowspan="3">Compression- based</td><td>Trading</td><td>[7,8]</td><td>Analyzing business transactions and processes to detect deceptive orders</td><td>- Effectiveness: minimum or no false positives</td><td>C: Find anomalies in graph-based data where the anomalous substructure in a graph is part of (or attached to or missing from) a non-anomalous substructure or the normative substructure</td></tr><tr><td>OSN</td><td>[27]</td><td>Analyzing user-product ratings to find rating fraud</td><td>- Effectiveness: 0.87 precision over the top 100 results- Scalability: logarithmic scalability with the number of nodes and linear to the number of edges</td><td>C: Granularity in user behavior (e.g., different users may rate products in different ways)</td></tr><tr><td>Insurance, AML, Banking, Trading</td><td>[58]</td><td>Analyzing financial and trading transaction to detect financial fraud</td><td>- Effectiveness: better detection results on sparse graphs- Ability to trace the origin of suspicious activities</td><td>D: Incorporate temporal information</td></tr><tr><td rowspan="6">Probabilistic-based</td><td rowspan="2">Insurance</td><td>[59]</td><td>Analyzing the relations between providers (hospitals) and consumers (cities) to find healthcare fraud committed by hospitals</td><td>- Effectiveness: detecting previously unreported anomalies- Visual analysis and manual labeling</td><td>D: Detect anomalies in big cities with very distributed anomaliesD: Use more precise evaluations because of the limitation of evaluation using visual analysis and manual labeling</td></tr><tr><td>[60]</td><td>Detecting automobile insurance fraud</td><td>- No requirement for the availability of large data- The imputation of the domain expert&#x27;s knowledge- Adopted to new types of fraud as soon as they are noticed</td><td>C: Rely on some user-defined threshold/ factor parameters that should be refined</td></tr><tr><td rowspan="4">OSN</td><td>[61]</td><td>Detecting opinion spammers</td><td>- Effectiveness: significant performance gains compared with the baselines</td><td>C: Make a clear split between opinion groups</td></tr><tr><td>[62]</td><td>Analyzing online reviews for fake review detection</td><td>- Robustness: robust to data sparsity- Effectiveness: highly outperforms the baselines- Model parameters are refined through a learning algorithm</td><td>C: Model the distributions of objects&#x27; reviews and users&#x27; credibility from sparse review data</td></tr><tr><td>[63]</td><td>Analyzing online reviews for spam review detection</td><td>- Effectiveness: outperforming the existing methods in AUC and AP- Scalability: linearly scalable with the number of edges</td><td>D: Incorporate product feature for spammer detectionD: Incorporate meta-path concept for group spammer detection</td></tr><tr><td>[64]</td><td>Detecting organized spammers in micro-blogging</td><td>- Effectiveness: accuracy of 93.6% for all the topics and an F1-score of 82.1% for anomalous topics</td><td>C: Detect anomalous topics hijacked by spammer groups from numerous trending topicsC: Detect the hijacked long-term topics that lasted for daysC: Scalability issue on large dataD: Detect new evolving types of spammers</td></tr></table>

Table 5
(continued)

<table><tr><td>Graph methods</td><td>Application areas</td><td>Reference</td><td>Focus of analysis</td><td>Highlights of approach and detection improvements</td><td>Challenges (C) and future directions (D)</td></tr><tr><td rowspan="4"></td><td>Online auction</td><td>[65]</td><td>Analyzing the social graph of online auction users and detect auction fraud, including shilling fraud, reputation manipulation, and non-delivery fraud</td><td>- Effectiveness: ability to detect all three types of fraud (with an AUC of over 0.98, TPR of over 0.97, and an FPR of 0.05) that may happen in an auction, while the existing methods are tuned to detect just one of those types each- Scalability: linearly scalable with the number of bids</td><td>C/D: Rely on some user-defined parameters that should be refined</td></tr><tr><td>OCA</td><td>[66]</td><td>Analyzing transaction data for credit application fraud detection</td><td>- Real-time scoring of incoming transaction streams- Effectiveness: low false alarm rates and achievement of consistent hit rates</td><td>C: Scalability is a major limitation as there is a trade-off between efficiency (rapid detection time and high scalability) and effectiveness (high hit and low false alarm rates)</td></tr><tr><td rowspan="2">IOF</td><td>[67]</td><td>Analyzing companies&#x27; general ledger to find accounting fraud</td><td>- Scalable: linearly scalable with the number of edges- Robustness: robust with a variety of parameters, so it requires almost no tweaking of parameters to work correctly- Effectiveness: high labeling accuracy of up to 97% compared with spectral clustering- Generalizability: can be applied to a variety of domains</td><td>C: Rely on experts to assess fraudulent behaviors based on the associated risk of each account</td></tr><tr><td>[68]</td><td>Detecting insider threats in a company</td><td>- Effectiveness: AUC of 0.9520, 6% improvement of ROC over the best performing baselines</td><td>C: Make more genuine alarms over a user profile that usually undergoes some continuous changes over time</td></tr></table>

alternative to alleviate the data privacy issue. Synthetic network generators ofer a common benchmark allowing multiple groups of researchers to evaluate their research on the same dataset. However, many algorithms that perform well on synthetically generated networks may perform poorly in real applications [80] because real data are often messy, possessing isolated nodes, strange degree distributions, and unbalanced class distributions. Thus, many challenges relating to synthetically generated networks remain. While it is important to continue to develop new and better algorithms, there should also be research into areas that answer the following questions: How good or realistic are the synthetically generated networks? Should this be a measure, or are there other ways to gauge this? How can noise and randomness be incorporated in the generated networks so that it is as close to the type of network that we wish our fraud detection algorithms to be dealing with [74]? How can the eficiency of diferent synthetic network generators be evaluated?

## 5.7.2. Keeping track of network user activities over diferent timestamps

Most real-world networks evolve and fraudsters leverage their dynamics to evade detection by spreading and altering their activities over time, thus camouflaging their real intent, i.e., their fraudulent activities [41]. This characteristic makes detecting fraudsters behavior even more challenging. Therefore, core criminal behavior that can withstand such changes over time should be understood [41].

Our literature review shows that research on fraud detection in dynamic networks is scarce (see Section 5.3.4), leaving a research gap that needs to be urgently filled, particularly with the prevalence of OSNs. Therefore, we strongly suggest that the design of fraud detection solutions should consider employing a time-evolving network structure to continuously track suspicious activities across diferent time-based snapshots.

Dealing with these time-evolving network structures requires several key considerations (see Table 5). One consideration is that solutions for these networks need to be scalable to balance the trade-of between eficiency (rapid detection time and high scalability) and effectiveness (high hit and low false alarm rates) [66]. It is also important to ensure that the solution is robust because a time-evolving network structure has data sparsity issues [62]. Hence, suspicious activities from diferent attributes and times of evolving network structures should be aggregated [55]. As a result, the algorithms developed for such networks need to consider new data characteristics

## 5.7.3. Investigating the inherent multiplex behavior of network users

Our review analysis shows that many current studies do not consider the intrinsic multiplex nature of human interactions. They tend to investigate users' behavior in simplex social networks, focusing on just one type of activity. However, capturing diferent aspects of relations and activities among the same individuals can give more clues to detect any suspicious activity (e.g., individuals may have diferent kinds of activities within an online social media platform, such as making friends, sending messages, reviewing profiles, liking posts, and poking). Thus, all kinds of activities should be analyzed to reveal any suspicious activity [25].

A multiplex network contains multiple layers that share the same sets of nodes, with each layer representing one type of communication among entities. Analyzing just one mode of interaction cannot provide a complete picture of the relationships among network users. Therefore, to identify anomalies and suspicious activities in multiplex networks, we suggest examining the rich information hidden in individual network layers [72]. Detecting suspicious activities in multiplex networks remains a relatively unexplored research area.

We suggest that multiplex networks should be given higher attention because social interactions in communities comprise diferent and multiple relationship types [25,72]. Therefore, it will be inadequate, if not unrealistic, to focus on a singular view using simplex social networks to detect fraudulent activities. We advocate that a pragmatic design for fraud detection solutions or algorithms should acknowledge and consider the varieties and abundance of human interactions that multiplex networks better capture. Neglecting such a multiplicity of human interactions can lead to information loss and may obscure important information from being discovered [25,72]. Furthermore, such interactions in multiplex networks are digital footprints of potential fraudsters that need to be holistically represented and extracted as important evidence for combating frauds and possibly crimes [25,72]. Consequently, feature engineering and graph representation learning (also called graph embedding) techniques are reported as the two main families of approaches for extracting and representing the structural features or characteristics of multiplex networks (see Section 4.5).

## 5.7.4. Eliminating human intervention in structural information extraction

Recently, there has been a surge towards the use of graph representation learning (or graph embedding) techniques to automatically encode the structural information about the network [33]. The key idea behind these approaches is to learn a mapping that embeds nodes, links, or the entire network into a lower-dimensional vector space to extract important hidden structural features. This is diferent from traditional approaches, such as feature engineering, which relies on prior knowledge of domain experts to hand-engineer features (e.g., degrees, clustering coeficients). In large and time-evolving networks, feature engineering is time-consuming, expensive, and, ultimately, lack scalability as detection models will need to be regularly updated to reflect the fraudster's altered behavior and activities [83]. Hence, we recommend the use of graph representation learning techniques to overcome these issues.

Graph representation learning techniques have shown to extract structural information from networks without the need for knowledge experts and can be adopted to learn and capture the structural information of time-evolving multiplex networks. This characteristic is attractive for fraud detection in our setting as it allows us to track fraudulent activities over time in a massive multiplex network for continuous learning in the detection model. As a result of recent developments in deep learning methods [29,34], there are now many graph representation learning techniques that can deal with massive network data. These techniques include graph convolutional networks [84], graph attention networks [85], and recurrent networks [86]. Another reason to seriously consider graph representation learning is that in many of the literature we reviewed. subsequent stages of fraud detection require the topological and structural characteristics of the network to be preserved. For example, many solutions include an anomaly detection stage that uses machine learning tasks (e.g., clustering and classifications) and require this information to operate.

All said, the role of human experts is irreplaceable for the time being. Any detected anomaly will still require domain knowledge assessment to make adjustments based on the given complex situations of an application domain. As far as automation goes, algorithms can assist with scoring to create blocking mechanisms [66] and block any suspicious fraudulent activities or behaviors by having regular expert input to improve the detection capability [68].

The four challenges are important considerations for those trying to develop new algorithms to efectively detect fraud within a time-evolving multiplex network. As we have learned from the various works in this review, a good algorithmic solution should follow a solution sketch (or exhibit characteristics):

Ensure access to good multiplex network data that are either from the problem source or, if synthetically generated, capture the net work characteristics;

• Exploit characteristics of time and multiplicity of relationships in these networks for better detection capabilities;

Avoid feature engineering but, instead, consider a range of graph representation learning approaches for scalability and intrinsically capture important structural information; and

Consider methods to automate feedback for continuous model learning and minimize human intervention using suitable machine learning techniques (see Section 4.4).

## 6. Conclusion and future research directions

This study aimed to identify, analyze, and synthesize various GBAD approaches employed in fraud detection research disseminated in data mining. Using eight questions that probe into specific aspects of GBADbased fraud detection research, we developed a classification framework to systematically analyze 39 academic papers identified through a systematic literature search.

This study makes significant contributions in theory and practice. The proposed classification framework ofers a systematic probe for researchers to gain a more insightful understanding of the application of GBAD techniques. The highlighted gaps challenge data scientists to embark on new empirical research in this domain. Equally, this paper also ofers practitioners a roadmap to appreciate the correspondence between the nature of their network, diferent types of anomalies, and appropriate graph-based methods that serve their needs and application areas.

Our review also reveals that GBAD approaches have been employed for fraud detection in various application areas. Owing to the unavailability of public data, most research using GBAD approaches have focused on OSNs. Consequently, we see a dearth of research works on datasets where personal confidential information is embedded, e.g., in areas, such as banking, insurance, and healthcare.

GBAD techniques have potential applications in the FinTech enterprise. As an emerging term in the financial industry in recent years, FinTech has provided a convenient gateway to diferent online financial services [87]. The rapid growth and pervasive use of FinTech have made the financial industry vulnerable to various forms of online frauds and cyber-crimes [87]. As a result, the financial sector is ripe to embrace new technological advances to prevent and detect digital identity frauds [87], opening up directions for researchers to investigate the application of GBAD techniques in fraud detection in the FinTech industry. For example, Blockchain, an innovation by FinTech, has attracted considerable attention by enabling bitcoin-based online transactions [16]. As a form of digital currency that is fully transparent and not controlled by any central authority, Bitcoin is another example where the GBAD techniques can be used. Many websites are now involved in Bitcoin trading, and diferent forms of fraudulent activities may occur in this trading process. With no central authority to set the price of Bitcoin, various websites can ofer diferent prices. For instance, a fake profile on a social media website can send false news regarding Bitcoin exchanges, with unsuspecting individuals conducting Bitcoin trading based on those fraudulent exchanges [88]. GBAD techniques can be used to predict a person's digital identity and to detect fraudulent connections, unreliable data patterns, or irregular activities. Some latest applications of GBAD techniques have shown that it is possible to assign a trust level to individual users to indicate how likely each individual will, for instance, repay a loan or if these individuals are who they say they are, based on data on each individual uncovered from the Internet [88].

Although these advancements increase the ability to identify highrisk individuals in advance, aggregating various sources of data to achieve predictive analytics raises ethical implications for a privacy violation, as was the case with Cambridge Analytica, which used Facebook data for predictive analysis [89]. The challenge is to identify new ways to safeguard individual privacy.

Another finding from our review is the dependency of research studies on domain knowledge for analyzing connectivity patterns in networks to detect suspicious activities. Our review found that only 28.2% of studies considered the dynamic nature of networks when analyzing anomalous activities. To address these problems, we suggest that (i) research studies should employ representation learning to lessen their dependence on domain knowledge [83] and (ii) business vendors should share their anonymized data for further analysis by data scien tists to provide opportunities for new discoveries.

Our systematic literature review, although extensive, may have omitted some relevant studies owing to the limitations of the scientific databases, specific keywords employed in the search, and timeframe selected for this review. Furthermore, GBAD techniques have been widely employed for fraud detection in the OSN area, which covers a vast range of applications, such as e-commerce, online shopping, dating, online recommendation, and social media websites. Each ap plication may be under the threat of diferent types of fraud (e.g., spam, deception and fake reviews, fake opinions, “Like” farms, advertising fraud, and cyberbullying), which may have been inadvertently excluded from our review because of the choice of keyword search. Therefore, a detailed analysis of diferent types of fraudulent activities in OSNs and the application of GBAD approaches for detecting such activities can be addressed in future review studies. Lastly, we exclusively selected papers from academic sources for review in this study. Future work will benefit by including non-academic sources where the application of GBAD techniques is reported.

## References

[1] S. Velampalli, W. Eberle, Novel graph based anomaly detection using background knowledge, Proceedings of FLAIRS 2017, AAAI Press, 2017, pp. 538–543.

[2] B. Hooi, K. Shin, H.A. Song, A. Beutel, N. Shah, C. Faloutsos, Graph-based fraud detection in the face of camouflage, ACM Transactions on Knowledge Discovery 11 (4) (2017) 1–26.

[3] D. Savage, X. Zhang, X. Yu, P. Chou, Q. Wang, Anomaly detection in online social networks, Soc. Networks 39 (2014) 62–70.

[4] G.R. Kelly, Social media’s contribution to political misperceptions in U.S. presidential elections, PLoS One 14 (3) (2019) e0213500.

[5] L.K. Branting, F. Reeder, J. Gold, T. Champney, Graph analytics for healthcare fraud risk estimation, ASONAM 2016, IEEE, 2016, pp. 845–851.

[6] V. Chandola, S.R. Sukumar, J.C. Schryver, Knowledge discovery from massive healthcare claims data, Proceedings of SIGKDD 2013, ACM, 2013, pp. 1312–1320

[7] W. Eberle, L. Holder, Mining for insider threats in business transactions and pro cesses, CIDM 2009, IEEE, 2009, pp. 163–170.

[8] W. Eberle, L. Holder, Discovering structural anomalies in graph-based data, ICDMW 2007, JEEE, 2007, pp. 393–398.

[9] L. Akoglu, H. Tong, D. Koutra, Graph based anomaly detection and description: a survey, Data Min. Knowl. Disc. 29 (3) (2015) 626–688.

[10] V. Chandola, A. Banerjee, V. Kumar, Anomaly detection: a survey, ACM Comput. Sury, 41 (3) (2009) 1–58.

[11] K. Anand, J. Kumar, K. Anand, Anomaly detection in online social network: a survev, JCICCT 2017. JEEE, 2017, pp. 456–459

[12] E. Ranshous, S. Shen, D. Koutra, S. Harenberg, Anomaly detection in dynamic networks: a survey, Comput. Stat. 7 (3) (2015) 223–247.

[13] S. Bhattacharyya, S. Jha, K. Tharakunnel, J.C. Westland, Data mining for credit card fraud: a comparative study, Decis, Support, Syst, 50 (3) (2011) 602–613

[14] A. Abdallah, M.A. Maarof, A. Zainal, Fraud detection system: a survey, J. Netw. Comput. Appl. 68 (2016) 90–113.

[15] E.W.T. Ngai, Y. Hu, Y.H. Wong, Y. Chen, X. Sun, The application of data mining techniques in financial fraud detection: a classification framework and an academic review of literature, Decis. Support. Syst. 50 (3) (2011) 559–569.

[16] J.J. Xu, Are blockchains immune to all malicious attacks? Financial Innovation 2 (25) (2016).

[17] A. Booth, A. Sutton, D. Papaioannou, Systematic Approaches to a Successful Literature Review, 2nd ed., Sage, London, 2011.

[18] E.W.T. Ngai, L. Xiu, D.C.K. Chau, Application of data mining techniques in customer relationship management: a literature review and classification, Expert Syst. Appl. 36 (2) (2009) 2592–2602

[19] R.B. Frost, C.W. Choo, Revisiting the information audit: a systematic literature re view and synthesis, Int. J. Inf. Manag. 37 (1) (2017) 1380–1390.

[20] T.K.H. Chan, C.M.K. Cheung, Z.W.Y. Lee, The state of online impulse-buying research: a literature analysis, Inf, Manag, 54 (2) (2017) 204–217.

[21] R.J. Bolton, D.J. Hand, Statistical fraud detection: a review, Stat. Sci. 17 (3) (2002) 235–255.

[22] R. Agrawal, M. Potamias, E. Terzi, Learning the nature of information in social networks. Proceedings of ICWSM 2012, AAAI Press, 2012

[23] A. Kaveh, Introduction to graph theory and algebraic graph theory, Optimal Analysis of Structures by Concepts of Symmetry and Regularity, Springer Vienna, Vienna, 2013, pp. 15–35.

[24] S. Lee, S. Park, M. Kahng, S.-g. Lee, Pathrank: ranking nodes on a heterogeneous graph for flexible hybrid recommender systems, Expert Syst. Appl. 40 (2) (2013) 684–697.

[25] S. Fakhraei, J. Foulds, M. Shashanka, L. Getoor, Collective spammer detection in evolving multi-relational social networks, Proceedings of KDD15, ACM, 2015, pp. 1769-1778.

[26] P.V. Bindu, P.S. Thilagam, Mining social networks for anomalies: methods and challenges, J. Netw, Comput, Appl. 68 (Supplement C) (2016) 213–229.

[27] N. Shah, A. Beutel, B. Hooi, L. Akoglu, S. Gunnemann, D. Makhija, M. Kumar,

C. Faloutsos, Edgecentric: Anomaly detection in edge-attributed networks, ICDMW 2016. JEEE. 2016. pp. 327–334

[28] C.C. Noble, D.J. Cook, Graph-based anomaly detection, Proceedings of SIGKDD 2003, ACM, 2003, pp. 631–636.

[29] P. Goyal, E. Ferrara, Graph embedding techniques, applications, and performance: a survey, Knowledge Based Systems 151 (2018) 78–94.

[30] S. Cresci, R. Di Pietro, M. Petrocchi, A. Spognardi, M. Tesconi, Fame for sale: eficient detection of fake twitter followers, Decis. Support. Syst. 80 (2015) 56–71

[32] S.Y. Bhat, M. Abulaish, Community-based features for identifying spammers in online social networks, ASONAM 2013, IEEE, 2013, pp. 100–107.

[33] H. Cai, V.W. Zheng, K. Chen-Chuan Chang, A comprehensive survey of graph embedding: problems, techniques and applications, IEEE Trans. Knowl. Data Eng. 30 (9) (2017) 1616–1637.

[34] G. Zhong, L.-N. Wang, X. Ling, J. Dong, An overview on data representation learning: from traditional feature learning to recent deep learning, Journal of Finance and Data Science 2 (4) (2016) 265–278.

[35] M. Jiang, P. Cui, A. Beutel, C. Faloutsos, S. Yang, CatchSync: catching synchronized behavior in large directed graphs, Proceedings of SIGKDD 2014, ACM, 2014, pp. 941–950.

[36] H.C. Manjunatha, R. Mohanasundaram, BRNADS: big data real-time node anomaly detection in social networks, ICISC 2018, IEEE, 2018, pp. 929–932.

[37] J. Seo. O. Mendelevitch. Identifving frauds and anomalies in medicare-b dataset EMBC 2017, IEEE, 2017, pp. 3664–3667.

[38] L.S. Bershtein, A. Tselykh, A clique-based method for mining fuzzy graph patterns in anti-money laundering systems, Proceedings of SIN 2013, ACM, 2013, pp. 384–387.

[39] A. Fronzetti Colladon, E. Remondi, Using social network analysis to prevent money laundering, Expert Syst. Appl. 67 (2017) 49–58.

[40] T. Tian, J. Zhu, F. Xia, X. Zhuang, T. Zhang, Crowd fraud detection in internet advertising, WWW 2015, International World Wide Web Conferences Steering Committee, 2015, pp. 1100–1110.

[41] J. Ye, L. Akoglu, Discovering opinion spammer groups by network footprints, ECML PKDD 2015. Springer International Publishing. 2015. pp. 267–282

[42] Z. Wang, S. Gu, X. Zhao, X. Xu, Graph-based review spammer group detection, Knowl. Inf. Syst. 55 (3) (2018) 571–597.

[43] M. Giatsoglou, D. Chatzakou, N. Shah, C. Faloutsos, A. Vakali, Retweeting Activity on Twitter: Signs of Deception, PAKDD 2015, Springer International Publishing, 2015. pp. 122–134.

[44] P.V. Bindu, R. Mishra, P.S. Thilagam, Discovering spammer communities in twitter, J. Intell, Inf, Syst, 51 (3) (2018) 503–527.

[45] E. Novikova, I. Kotenko, Visual analytics for detecting anomalous activity in mobile money transfer services, Cd-Ares 2014, Springer International Publishing, 2014, pp. 63-78.

[46] I. Molloy, S. Chari, U. Finkler, M. Wiggerman, C. Jonker, T. Habeck, Y. Park, F. Jordens, R. van Schaik, Graph Analytics for Real-Time Scoring of Cross-Channel Transactional Fraud, FC 2016, Springer, Berlin Heidelberg, 2017, pp. 22–40

[47] Z. Li, H. Xiong, Y. Liu, Mining blackhole and volcano patterns in directed graphs: a general approach, Data Min. Knowl. Disc. 25 (3) (2012) 577–602.

[48] A. Gamachchi, S. Boztaş, Web access patterns reveal insiders behavior, IWSDA 2015, IEEE, 2015, pp. 70–74.

[49] S. Liang, J. Zeng, C. Li, H. Chen, A framework for spotting anomaly, FSKD 2010, IEEE, 2010, pp. 2260–2264.

[50] P. Bangcharoensap, H. Kobayashi, N. Shimizu, S. Yamauchi, T. Murata, Two step graph-based semi-supervised learning for online auction fraud detection, ECML PKDD 2015, Springer International Publishing, 2015, pp. 165–179.

[51] J. Nan, J. Yu, S. Ann, H. Wen-Ling, J. Guy, P. Siva, Z. Zhi-Li, Isolating and analyzing fraud activities in a large cellular network via voice call graph analysis, Proceedings of MobiSys 2012, ACM, 2012, pp. 253–266.

[52] H. Yan, Y. Jiang, G. Liu, Telecomm fraud detection via attributed bipartite network, ICSSSM 2018, IEEE, 2018, pp. 1–6

[53] A. Tselykh, M. Knyazeva, E. Popkova, A. Durfee, A. Tselykh, An attributed graph mining approach to detect transfer pricing fraud, Proceedings of SIN 2016, ACM, 2016, pp. 72–75.

[54] P. Moriano, J. Finke, Model-based fraud detection in growing networks, CDC 2014. JEEE. 2014. pp. 6068–6073

[55] S. Liu. B. Hooi, C. Faloutsos, HoloScope: Topology-and-spike aware fraud detection. Proceedings of CIKM 2017, ACM, 2017, pp. 1539–1548.

[56] K. Shin. B. Hooi, J. Kim. C. Faloutsos, DenseAlert: incremental dense-subtensor detection in tensor streams KDD 2017 ACM 2017 pp 1057–1066

[57] H. Lamba, B. Hooi, K. Shin, C. Faloutsos, J. Pfefer, ZOORANK: Ranking Suspicious Entities in Time-Evolving Tensors, ECML PKDD 2017, Springer International Publishing, 2017, pp. 68–84.

[58] D. Huang, D. Mu, L. Yang, X. Cai, CoDetect: financial fraud detection with anomaly feature detection, JEEE Access 6 (2018) 19161–19174

[59] L.F.M. Carvalho, C.H.C. Teixeira, W. Meira, M. Ester, O. Carvalho, M.H. Brandao, Provider-consumer anomaly detection for healthcare systems, ICHI 2017, IEEE, 2017, pp. 229–238.

[60] L. Subeli, S. Furlan, M. Baiec, An expert system for detecting automobile insurance fraud using social network analysis, Expert Syst. Appl. 38 (1) (2011) 1039–1052.

[61] H. Dai, F. Zhu, E.P. Lim, H. Pang, Detecting anomalies in bipartite graphs with mutual dependency principles, ICDM 2012, IEEE, 2012, pp. 171–180.

[62] X. Wu, Y. Dong, J. Tao, C. Huang, N.V. Chawla, Reliable fake review detection via modeling temporal and behavioral patterns, IEEE BigData 2017, IEEE, 2017, pp. 494-499

[63] S. Shehnepoor, M. Salehi, R. Farahbakhsh, N. Crespi, NetSpam: a network-based spam detection framework for reviews in online social media, IEEE Transactions on Information Forensics and Security 12 (7) (2017) 1585–1595.

[64] Q. Dang, Y. Zhou, F. Gao, Q. Sun, Detecting cooperative and organized spammer

groups in micro-blogging community, Data Min. Knowl. Disc. 31 (3) (2017) 573–605.

[65] S. Tsang, Y.S. Koh, G. Dobbie, S. Alam, SPAN: finding collaborative frauds in online auctions, Knowl.-Based Syst. 71 (2014) 389–408.

[66] C. Phua, R. Gavler, V. Lee, K. Smith-Miles, On the communal analysis suspicion scoring for identity crime in streaming credit applications, Eur. J. Oper. Res. 195 (2) (2009) 595–612.

[67] M. McGlohon, S. Bay, M.G. Anderle, D.M. Steier, C. Faloutsos, SNARE: A link analytic system for graph labeling and risk detection, Proceedings of SIGKDD 2009, ACM, 2009, pp. 1265–1274.

[68] S.D. Bhattacharjee, J. Yuan, Z. Jiaqi, Y.P. Tan, Context-aware graph-based analysis for detecting anomalous activities, ICME 2017, IEEE, 2017, pp. 1021–1026.

[69] R.F. Lima, A.C.M. Pereira, A fraud detection model based on feature selection and undersampling applied to web payment systems, Wi-IAT 2015, IEEE, 2015, pp. 219-222.

[70] J. Meng, C. Peng, B. Alex, F. Christos, Y. Shiqiang, Catching synchronized behaviors in large networks: a graph mining approach, ACM Trans. Knowl. Discov. Data 10 (4) (2016) 1–27.

[71] M. Rahman, R. Recabarren, B. Carbunar, D. Lee, Stateless puzzles for real time online fraud preemption, WebSci 2017, ACM, 2017, pp. 23–32.

[72] T. Pourhabibi, Y.L. Boo, K.L. Ong, B. Kam, X. Zhang, Behavioral analysis of users for spammer detection in a multiplex social network, AUSDM 2018, Springer Singapore, 2019, pp. 228–240.

[73] J. West. M. Bhattacharva, Intelligent financial fraud detection: a comprehensive review, Computers & Security 57 (2016) 47–66.

[74] D.F. Nettleton, A synthetic data generator for online social network graphs, Soc. Netw. Anal. Min. 6 (1) (2016) 44.

[75] J. Davis, M. Goadrich, The relationship between precision-recall and roc curves, Proceedings of ICML 2006, ACM, 2006, pp. 233–240.

[76] L.A. Jeni, J.F. Cohn, F. De La Torre, Facing imbalanced data recommendations for the use of performance metrics, ACII 2013, IEEE, 2013, pp. 245–251.

[77] H. Fanaee, J. Gama, Event labeling combining ensemble detectors and background knowledge, Progress in Artificial Intelligence 2 (2) (2014) 113–127.

[78] N. Goix, How to evaluate the quality of unsupervised anomaly detection algo rithms? ArXiv.1607.01152, 2016. https://arxiv.org/abs/1607.01152.

[79] L. Akoglu, C. Faloutsos, RTG: a recursive realistic graph generator using random typing, Data Min. Knowl. Disc. 19 (2) (2009) 194–209.

[80] A.M. Ali, Synthetic Generators for Simulating Social Networks, Department of Electrical Engineering and Computer Science, University of Central Florida. 2014

[811 B. Eze. L. Pevton. Systematic literature review on the anonymization of high di mensional streaming datasets for health data sharing, Procedia Computer Science 63 (2015) 348–355.

[82] P. Ohm, Broken promises of privacy: responding to the surprising failure of anonymization, UCLA Law Rev, 57 (2009) 1701.

[83] W.L. Hamilton, R. Ying, J. Leskovec, Representation learning on graphs: methods and applications, IEEE Data Engineering Bulletin 40 (2017) 52–74.

[84] M. Schlichtkrull, T.N. Kipf, P. Bloem, R. van den Berg, I. Titov, M. Welling, Modeling relational data with graph convolutional networks, ESWC 2018, Springer International Publishing, 2018, pp. 593–607.

[85] P. Shaw, J. Uszkoreit, A. Vaswani, Self-attention with relative position representations, ArXiv.1803.02155, 2018. https://arxiv.org/abs/1803.02155.

[86] R.B. Palm, U. Paquet, O. Winther, Recurrent relational networks, ArXiv.1711.08028, https://arxiv.org/abs/1711.08028, (2018).

[87] Y. Shim, D.H. Shin, Analyzing China’s fintech industry from the perspective of actor-network theory, Telecommun. Policy 40 (2) (2016) 168–181.

[88] A. Viswam, G. Darsan, An eficient bitcoin fraud detection in social media networks, ICCPCT 2017, IEEE, 2017, pp. 1–4.

[89] T. Jiya, Ethical implications of predictive risk intelligence, ORBIT Journal 2 (2) (2019).

Tahereh Pourhabibi is a Ph.D. candidate in the School of Accounting, Information Systems and Supply Chain, RMIT University, Melbourne, Australia. She received her Master of Science in Artificial Intelligence from Al-Zahra University, Tehran, Iran. Her research interests include machine learning, data mining, anomaly detection, and their application in suspicious activity detection and fraud detection.

Kok-Leong Ong is an Associate Professor at the Centre for Data Analytics and Cognition, La Trobe University. He received his Ph.D. in 1999 and B. A. Sc. (Hons) in 2004 from the Nanyang Technological University, Singapore. His research interest includes data mining and analytics, and machine learning and AI, and his works have been supported by over \$1.46m of grants to-date. He has published over 80 peer-reviewed papers and has served in over 60 Program Committees

Booi H Kam is a Professor in the School of Accounting, Information Systems and Supply Chain, RMIT University. His current research interests are in areas of strategic digital supply chain operations and supply chain relationships. A recipient of an Emerald Literati Network Awards for Excellence, Booi is regularly invited by universities in China, England, France, Korea, and Taiwan to give public lectures and teach into their degree programs. Booi holds a Ph.D. from the University of California at Los Angeles. He coauthors Consumer Logistics, a book by Edward Elgar Publishing.

Yee Ling Boo received her Ph.D. in Information Technology from Monash University Australia. She is currently a lecturer at the School of Accounting, Information Systems and Supply Chain, RMIT University, Melbourne, Australia. Her research interests include Data Mining, Brain-Inspired Computing, Cognitive Analytics, and their applications in business, education, and health. Before the pursuit of her Ph.D. degree, she was a software engineer in Malaysia. Her research works have appeared in reputable journals and conferences.
