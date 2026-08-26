---
otero_id: 19552
otero_key: "ETSTS326"
title: "A local social network approach for research management"
authors: "Xiaoyan Liu; Zhiling Guo; Zhenjiang Lin; Jian Ma"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.055"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Xiaoyan Liu <sup>a</sup>, Zhiling Guo <sup>a,</sup>⁎, Zhenjiang Lin <sup>b</sup>, Jian Ma <sup>a</sup>

<sup>a</sup> Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon, Hong Kong

<sup>b</sup> Advanced Analytics Institute, University of Technology Sydney, NSW 2007, Australia

a r t i c l e i n f o

Available online 7 November 2012

Keywords: Research management Collaboration analysis Social network analysis Research analytics

## a b s t r a c t

Traditional methods to evaluate research performance focus on citation count, quality and quantity of research output by individual researchers. These measures overlook the roles an individual plays in research collaboration, which is critical in an institutional research management environment due to the inherent interdependency among research entities. In order to address the organizational research management needs, we propose a research social network approach to better analyze local collaboration networks. For this purpose, we develop a new “collaboration supportiveness” measure to quantify an individual researcher's collaboration ability. Insights derived from this research are very helpful for managers to effectively allocate resources, identify research priorities, promote collaboration, and grow research in directions aligned with the organizational strategies.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Academic institutions face tremendous pressure to expand their research outputs in the global competition for reputation. Effective research management is critical to institutional mission in developing a successful research strategy to build solid research programs, grow research activities, and align institutional priorities with funding agency criteria. It can also inform organizational level strategic decisions, ease reporting to external stakeholders such as funding councils, and help strengthen collaboration within and beyond the institution's boundaries. Today, institutional research repository has been put into agenda in many countries. For example, Symplectic is a publication-oriented system widely used in the universities in UK. The European Organization for International Research Information (www.eurocris.org) provides support for users in their recording, reporting and decision-making concerning the research process. In North America, many universities partner with Thomson Reuters to expand their global research presence.

Traditionally, research management function is performed by university research of<sup>fi</sup>ce which collects research outputs (e.g., papers, patents, etc.) from faculty via individual annual reports. The collected information is hosted by a university information system. As universities establish their own research repositories, institutional managers realize a number of challenges in measuring research impact and performing research assessment. First, the most widely used research metric is the journal impact factor (JIF) developed by the Institute for Scienti<sup>fi</sup>c Information (ISI, now part of the Thomson Reuters group). The metric was originally intended as a tool for publishers to measure the impact of individual journals. Due to the lack of other reliable measures, institutions tend to overly rely on JIF as a research measure. It is clear that the use of such single metric is insuf<sup>fi</sup>cient to measure the impact of research. New metrics relevant to the speci<sup>fi</sup>c institutional research contexts need to be developed.

Second, institutional research performance assessment usually only emphasizes on quality, quantity, and citations of published journal articles. These existing metrics largely treat individuals as independent contributors in the knowledge production and dissemination process. However, most research is collaborative in nature. There exist strong interdependencies among research projects involving a group of related researchers. The tie is even stronger for certain research topics and in certain research disciplines. It is necessary to develop alternative, reliable and objective methods for managing and measuring research performance not only individually, but in the context of local collaboration networks.

To address these challenges, we propose a research social network approach to perform research performance evaluation. In addition to the standard measure of productivity (e.g., quantity and quality of research), the new framework emphasizes on relevance and connectivity. Relevance refers to information such as keywords and research disciplines that put the research evaluation in the relevant context. Connectivity refers to the inherent interdependencies among researchers and research topics. We aim to transform traditional research management by incorporating a comprehensive analysis of the local collaboration communities. Our major contribution is to propose local collaboration network as a new tool to inform strategic, organizational, and managerial decision making.

For this purpose, we further develop a new measure called “collaboration supportiveness” to quantify the individual contribution in the local collaboration network. By smart exploitation of a local research network in a university, we show that our method is very effective to discover rich patterns of collaboration and generate new insights. In comparison with the traditional collaboration network analyses such as citation network that essentially take a global view, we focus on more relevant, local social collaboration network from the perspective of institutional research management such as the research of<sup>fi</sup>ce.

Most social network applications in the literature only focus on either one type of subjects (e.g. authors) or single relationship (e.g. coauthorship) among subjects. However, the joint analysis of authors and topics can provide more information for better research group identi<sup>fi</sup>cation than separated networks. In this study we not only consider the traditional network analysis on the research collaboration, but also the links between researchers and topics based on two-mode network analysis methods. To the best of our knowledge, this research is the <sup>fi</sup>rst to employ two-mode network to perform joint analysis of researchers and topics in the context of research collaboration.

We developed a research online information system to effectively collect, disseminate, and regulate research outputs. The available services are classi<sup>fi</sup>ed into three types of users: institutional administrators, researchers, and public users. The system supports both tactical and strategic management functions at different levels. In this study, we focus on the information and management function from the institutional administrators' perspective. Our analyses help answer the following questions: what is an individual's social position and speci<sup>fi</sup>c roles he/she plays in the collaboration network? How many and which groups are the most cohesive collaboration research groups in the department/college/ university? What are the key research areas within the department or across the disciplines? Who belong to the core group of researchers to connect different research topics? Do there exist centers of excellence in terms of productivity? What are the new collaboration opportunities? Better understanding of these questions will enable information-rich collaboration, effective decision-making and successful management of research.

Overall, our system builds a more transparent research environment and gains more visibility in terms of the roles research centers and departments play in various research activities. This can help the research of<sup>fi</sup>ce in its internal resource allocation, balance the different demands of basic versus applied research, individual versus collaborative research, and identify research priorities or respond to national priorities. In addition, the decision support system can help make recommendations for institutions and policymakers, such as designing incentive mechanisms to award outstanding researchers, train human capital, and grow research capacity.

The rest of the paper is organized as follows. Section 2 brie<sup>fl</sup>y reviews the related work on research social network analysis methods and applications. Section 3 describes our research framework, details the management functions, key features, and the corresponding network analysis methods. We provide detailed analyses in Sections 4 and 5. Concluding remarks are presented in Section 6.

## 2. Related literature

In this section, we <sup>fi</sup>rst focus our attention on popular techniques used in social network analysis. We then review three major types of applications: paper-centered, author-centered, and topic-centered network analysis.

## 2.1. Social network analysis methods

Social network analysis, originally gained its popularity in social and behavior sciences, involves understanding the linkages among social entities and the implications of these linkages. With the rapid development of formal analyzing techniques, it has become an attractive tool for a variety of <sup>fi</sup>elds, such as economics [24,26], marketing [36], knowledge management [19], industrial engineering [1,18], etc. Academic collaboration network is an important type of social network that receives growing interests in recent years [2,11–13,29]. Such analyses provide important insights to drive the development and structure of the specific academic disciplines [27].

In the social network analysis, mode refers to distinct kind of social entities (or actors) in the network. We can categorize networks by how many modes the network has. Co-authorship network is an example of one-mode network in which researchers are de<sup>fi</sup>ned as a single type of entities. Two-mode networks focus on two distinct types of entities. For instance, the conference participation network consists of researchers and conferences. A bipartite graph can be constructed to express researchers' participation in different conferences [37].

The social network can also be distinguished by its global or local in-<sup>fl</sup>uence, depending on whether there are focal entities in the network [37]. A local network consists of focal entities (i.e., egos) with whom a set of actors have ties. It is also called ego-centered network. If all entities in the network are treated equally, the network is a global network.

Existing social network analysis techniques focus on a number of important measurements about the network structure. Centrality is an indication of the social power of a node based on how well it connects the network. In general, there are three types of centrality measures: degree centrality, betweenness centrality, and closeness centrality. Degree of a node is the number of direct connections a node has in a network. Betweenness of a node is the number of shortest paths between other node pairs that pass through that node in a network. This measure gives a higher value for nodes that bridge clusters. It implies that, if more people depend on a person to make connections with other people, then more power that person has. Closeness of a node is the inverse of the sum of all shortest distances between that node and other nodes. It indicates the extent to which an individual is near all other individuals in a network directly or indirectly.

In bibliometrics, social network analysis techniques are often used to explore the collaboration patterns within certain disciplines. Researchers, papers, and keywords are most frequently used subjects. They are connected by relationships such as co-authorship, citation relationship, cooccurrence etc. According to the type of analyzed subjects, the related research output analysis can be mainly categorized into three classes: paper-centered analysis, author-centered analysis, and topics-centered analysis.

## 2.2. Paper-centered analysis

Paper-centered analysis usually uses publications or journals as major subjects. It focuses on citation or co-citation relationship. Citation analysis is one of the most widely used methods of bibliometrics [34]. When one research work cites another, a relationship, citation-from or citation-to, is established. This relationship could be extended to between authors, between journals, between <sup>fi</sup>elds, between institutions, or even between countries. For example, the Social Science Citation Index (SSCI) and the Science Citation Index (SCI) are designed to trace citations and indicate the importance and impact of the research papers and journals. The well-known link-based ranking algorithms such as PageRank [33] have been used in the citation network to more accurately measure research quality [9]. Building upon the PageRank algorithm, Google Scholar is a very popular automated citation indexing tool that analyzes citations in large-scale.

Citation analysis can be used to quantify the in<sup>fl</sup>uence of a single researcher. The best-known measures so far include h-index [16], in which both the number of publications and the number of citations per publication are taken into account, and g-index [10], which is calculated based on the distribution of citations received by a given researcher's publications. The h-index and g-index are highly correlated. These measures are used to evaluate an individual scholar's productivity and impact of the published work [32].

Citation analysis is also a means of determining “classic” publications. Walstrom et al. [35] conduct citation analysis on 118,364 references from 3752 articles published in top IS journals from 1986 to 1995.

Table 1  
![](/api/attachments/ETSTS326/fulltext/images/3350b3763570c51bdd1a4c0612900993350f3c29bf1ace84e3c015cf6e88a0b5.jpg)  
Fig. 1. Research analytics processes and steps.

They identi<sup>fi</sup>ed 91 “citation classics” and 13 “super classic” publications. These results are very useful to develop reading list and discover characteristics that make a reference classic. Whitley [38] analyzes the citation network of papers published in European Conference on IS (ECIS) during 1993–2002 to identify core research themes and up-to-date research subjects. Based on a network of research papers, Bhattacharjee et al. [3] develop a structural method to identify the in<sup>fl</sup>uential information elements and connections in an information resource network.

Co-citation analysis involves tracking pairs of papers that are cited together in the source articles indexed in ISIs databases. Bibliographic coupling and co-citation coupling are two types co-citation analysis that establish subject similarity between two research works. Culnan [7,8] explores the mainstream research sub<sup>fi</sup>elds in IS to identify the reference disciplines of each sub<sup>fi</sup>eld. These studies provide a useful framework for understanding the foundation of IS [31]. Although cocitation patterns can be used to address the issue of connectivity or collaboration among researchers, the effect is more global than local. Since we are interested in understanding the local collaboration patterns, we focus on author-centered and topic-centered analysis.

## 2.3. Author-centered analysis

Author-centered analysis, also called researcher-centered analysis, takes the co-authorship as the ties linking researchers together. This type of network has been studied extensively from various aspects such as degree (number of co-authors) distribution analysis [20], social community extraction (research group identi<sup>fi</sup>cation) [30], social entity ranking (researcher ranking) [21,39], knowledge exchange network [17,31], expert recommendation [15] etc. In addition, Morel et al. [28] study suitable research group identi<sup>fi</sup>cation in areas where researchers' productivity and impact factor of scienti<sup>fi</sup>c publications are of limited value. Goldenberg [11] performs dynamic analysis to investigate the evolution of the collaboration network in Marketing Science.

Co-authorship networks are created from a large set of publications by clusters of collaborating researchers. In such networks, each author is represented as one node, and an edge represents the papers co-authored by two authors. The weight of an edge is the total number of co-authored papers. Since most existing co-authorship networks are modeled using undirected graph, the well-known RageRank algorithm cannot be directly applied to more accurately measure the contribution of a researcher in the collaboration relationship, because those link-based methods are mainly designed for directed graphs.

More recently, Han et al. [14] introduce a novel “supportiveness” measure on co-authorship relation. They view the paper co-authored by two authors as one author supporting the other's scienti<sup>fi</sup>c work. A supportiveness-based author ranking scheme is proposed. They further use the k-nearest neighbor algorithms to <sup>fi</sup>nd the most supportive authors. To identify the groups of authors who contribute the most to the intra-department collaboration, we construct a bi-directional graph based on the “supportiveness” concept. We further introduce a new “collaboration supportiveness” measure to rank researchers based on their net weighted contribution to the department collaboration.

## 2.4. Topic-centered analysis

In the general research environment, scopes and aims are speci<sup>fi</sup>ed by journals, research interests are claimed by authors, and papers are associated with keywords. Such information is generally regarded as keywords or topics in our research. The topic-centered analysis usually focuses on the co-occurrence of these topics identi<sup>fi</sup>ed by the research works, journals or authors. There are much fewer works about keyword occurrence analysis than the citation analysis and co-authorship analysis.

The keyword analysis evolves from co-word analysis, which is a well-known relational bibliometric method. It was originally used to make target-oriented retrieval, and later it was used to evaluate the research outputs [4]. Today co-word analysis allows for the relational analysis of documents based on terms and term-groups. Keyword analysis is a type of co-word analysis that has started to play an important role in understanding the dynamics of knowledge development [22,23]. The techniques of keyword analysis might be a potential method for monitoring development trends and projecting future research directions [5,23].

Management functions supported by the collaboration network analysis.

<table><tr><td>Management functions</td><td>Key features</td><td>Types of network</td></tr><tr><td>Individual productivity assessment</td><td>Quantify the measure of “collaboration supportiveness”Identify the collaborative roles an individual researcher plays in the collaboration networkAnalyze a researcher&#x27;s collaboration patterns</td><td>Co-authorship network</td></tr><tr><td>Collaboration group analysis</td><td>Identify the most active research topics within departments and across disciplinesIdentify the most cohesive collaboration research groups within the department/universityIdentify center of excellence and the key research areas</td><td>Co-authorship networkTopic network</td></tr><tr><td>Researcher-theme path analysis</td><td>Determine a core group of researchers to connect different research topicsDiscover new collaboration opportunities by connecting researchers with the same research theme and by recommending promising themes to key group of researchers</td><td>Author-topic network</td></tr><tr><td>Strategic planning</td><td>Prioritize resource allocation to centers of excellence and provides seed funds to grow weak research areasDesign incentive mechanisms based on institutional needs and align organizational goals with those of the funding agencies</td><td>Co-authorship networkTopic networkAuthor-topic networkOther statistical tools</td></tr></table>

Table 4  
Table 2  
Authors' connectivity ranking in the department.

<table><tr><td>Rank</td><td>RID (i)</td><td>Degree ( $d_i$ )</td><td>Ndegree ( $d_i$ )</td><td>RID (i)</td><td>Betweenness ( $b_i$ )</td><td>RID (i)</td><td>Closeness ( $c_i$ )</td></tr><tr><td>1</td><td>6</td><td>10</td><td>0.185</td><td>6</td><td>0.1978</td><td>6</td><td>0.2636</td></tr><tr><td>2</td><td>24</td><td>8</td><td>0.148</td><td>9</td><td>0.1370</td><td>9</td><td>0.2361</td></tr><tr><td>3</td><td>5</td><td>8</td><td>0.13</td><td>3</td><td>0.1314</td><td>3</td><td>0.2292</td></tr><tr><td>4</td><td>9</td><td>7</td><td>0.1</td><td>5</td><td>0.1188</td><td>52</td><td>0.2054</td></tr><tr><td>5</td><td>38</td><td>7</td><td>0.074</td><td>24</td><td>0.0444</td><td>46</td><td>0.2028</td></tr><tr><td>6</td><td>14</td><td>4</td><td>0.074</td><td>38</td><td>0.0283</td><td>5</td><td>0.1906</td></tr><tr><td>7</td><td>54</td><td>4</td><td>0.074</td><td>2</td><td>0.0196</td><td>24</td><td>0.1883</td></tr><tr><td>8</td><td>3</td><td>4</td><td>0.074</td><td>14</td><td>0.0035</td><td>38</td><td>0.1883</td></tr><tr><td>9</td><td>40</td><td>4</td><td>0.074</td><td>48</td><td>0.0000</td><td>25</td><td>0.1818</td></tr><tr><td>10</td><td>39</td><td>4</td><td>0.074</td><td>47</td><td>0.0000</td><td>50</td><td>0.1818</td></tr></table>

The boldface type is used to highlight RIDs that are among top 10 based on all three measures (degree, betweenness, and closeness).

It is relatively new in the IS <sup>fi</sup>eld to employ keyword analysis. Choi [6] is among the <sup>fi</sup>rst to construct keyword network analysis based on published articles in <sup>fi</sup>ve major MIS journals from 1998 to 2008. The study provides useful insights to better understand the intellectual structure and research trends in the IS <sup>fi</sup>eld. In our research, we employ multiple research methods to explore the research collaboration patterns.

## 3. Research framework

We mainly perform the social network-based research analytics on our Research Online (ROL) platform (http://www.irissz.com/en/rol. html). Research analytics is a set of processes that apply methods and theories in scientometrics, business intelligence, and analytics to transform research relevant data into useful information and actionable insights for research management. The ROL platform provides analytical tools to conduct comprehensive research analysis, evaluation, and management. The main management [25] functions, key features, and the types of social networks that are used to support the analyses are summarized in Table 1.

In general, we categorize research collaboration into four major management functions. The <sup>fi</sup>rst three functions, individual assessment, research group identi<sup>fi</sup>cation, and researcher-theme path analysis, can be used to support departmental level tactical planning. The fourth function is more useful for the college/university level strategic planning. Therefore, this framework aims to support decision making involved in research management at different levels. Evaluation of all these aspects usually involves ranking and clustering based on different measures. The analysis process is described as the following steps (Fig. 1).

First, we collect data from public databases such as ISI's Web of Knowledge database and Elsevier's Scopus. We extracted information such as titles, authors and af<sup>fi</sup>liations, abstracts, keywords, citation information etc. We next perform data cleaning to represent data in our standard format. This will avoid the data duplication problem due to different data storage formats used in different databases, which may lead to wrong article retrieval to authors' publications. After we prepare the data in the right format, we index articles, researchers, topics, and other research entities such as discipline, department, and university. In the data analysis step, we mainly perform social network analysis.

Table 3  
Individual position in department network.

<table><tr><td>Rank</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>RID</td><td>6</td><td>9</td><td>5</td><td>3</td><td>24</td><td>38</td><td>2</td><td>52</td><td>46</td><td>41</td></tr><tr><td>CIF</td><td>0.212</td><td>0.163</td><td>0.152</td><td>0.137</td><td>0.129</td><td>0.116</td><td>0.081</td><td>0.076</td><td>0.75</td><td>0.075</td></tr></table>

The major types of social networks we consider are co-authorship network, topic network, and author–topic network. The <sup>fi</sup>rst two types belong to one-mode and the third type is the two-mode network analysis. Other types of networks are possible as well.

The last step is to visualize the analysis results and represent information in different forms such as summary statistical reports, author/ topic ranking tables and <sup>fi</sup>gures, and collaboration graphs and maps at different granularity levels. For the social network analyses, we report the most important centrality measures including degree, betweenness, and closeness about the nodes for both one-mode and two-mode networks. These analyses were conducted by the social network analysis tool Pajek. In particular, we perform the core-periphery analysis on the networks. The k-core and component identi<sup>fi</sup>cations are also conducted. This is done by another popular social network analysis tool UNINET.

## 4. Research social network analysis

In this section, we present our detailed analyses based on the <sup>fi</sup>rst three key management functions illustrated in Table 1. We use the authors' af<sup>fi</sup>liated departmental level research social network data as an example to demonstrate the local social network approach for research management.

## 4.1. Individual assessment

The nature of academic research requires an individual to be both a productive researcher and an effective collaborator. As such, the assessment focuses on identifying in<sup>fl</sup>uential individuals by their social positions in light of their contributions in collaborative research. The analysis focuses on the collaboration ability of an individual, which is different from the impact factor analysis and h-index measure that evaluate the individual's research without taking into account collaboration.

## 4.1.1. Individual social position

The collaboration assessment is mainly based on the standard coauthorship network analysis to investigate the researcher's social position and in<sup>fl</sup>uence in the intra-department network. The network consists of n nodes, where each researcher is represented by a unique node. If two researchers are co-authors of the same paper, there is a tie between them. We apply the traditional centrality analysis to the collaboration network to identify the in<sup>fl</sup>uential individual researchers.

There are several centrality measures. The <sup>fi</sup>rst and the simplest is the degree of a node. It is de<sup>fi</sup>ned as the number of links between the focal node and other nodes in the network, denoted by $d _ { i } , i { = } 1 , { \ldots } , n .$ In our context, it directly measures how many other researchers with whom one collaborates. We can also de<sup>fi</sup>ne the normalized degree for researcher i, which is the degree of researcher i divided by the number of potential collaboration links in the network: $\begin{array} { r } { d _ { i } = \frac { d _ { i } } { n - 1 } } \end{array}$

In the social graph, a geodesic is the shortest path between two vertices. The distance from researcher i to researcher j is measured by the length of the geodesic from node i to j, denoted by $g _ { i j } .$ Closeness of researcher i is the number of other researchers divided by the sum of all distances between researcher i and all other researchers, expressed as $\begin{array} { r } { c _ { i } = \frac { n - 1 } { \sum _ { i \neq i } g _ { i i } } . } \end{array}$ Betweenness of researcher i is de<sup>fi</sup>ned as the proportion of all geodesics between pairs of nodes that include researcher i, denoted by b . It measures the extent that a researcher connects with other researchers.

Collaboration supportiveness of researchers in the department

<table><tr><td>Rank</td><td>RIDi</td><td>In-supportiveness $S_{l}(i)$ </td><td>Out-supportiveness $S_{O}(i)$ </td><td>Collaborationsupportiveness $u_{i}$ </td></tr><tr><td>1</td><td>24</td><td>1.5042</td><td>8.1679</td><td>6.6637</td></tr><tr><td>2</td><td>6</td><td>1.306</td><td>7.4405</td><td>6.1345</td></tr><tr><td>3</td><td>38</td><td>2.8122</td><td>7.4405</td><td>4.6283</td></tr><tr><td>4</td><td>5</td><td>2.1452</td><td>5.4831</td><td>3.3379</td></tr><tr><td>5</td><td>9</td><td>2.0871</td><td>4.7561</td><td>2.669</td></tr><tr><td>6</td><td>14</td><td>0.6446</td><td>2.347</td><td>1.7024</td></tr><tr><td>7</td><td>3</td><td>0.515</td><td>1.9285</td><td>1.4135</td></tr><tr><td>8</td><td>18</td><td>0.2062</td><td>1.4</td><td>1.1938</td></tr><tr><td>9</td><td>12</td><td>1.7397</td><td>2.5112</td><td>0.7715</td></tr><tr><td>10</td><td>2</td><td>0.4328</td><td>1.0717</td><td>0.6389</td></tr></table>

![](/api/attachments/ETSTS326/fulltext/images/d4d86b6f9e2665b0934d986f76be91e776b3ff31f5624437bd38317e979593ca.jpg)  
Fig. 2. Co-authorship network in the department.

Based on these measures, we are also able to identify the top 10 researchers in terms of three connectivity measures: degree/normalized degree, betweenness, and closeness. The top ten researchers based on each measure is shown in Table 2. The researcher IDs (RIDs) in boldface are the researchers ranked among top 10 for all the three centrality measures.

The researchers are ranked differently based on different connectivity measures. Under each measure, we sort the researchers in decreasing order. In terms of the degree or normalized degree, researcher 6 has the highest number of collaboration (10) within the department. Researcher 3 is ranked at 8th in terms of the number of collaboration. However, his/ her betweenness measure (ranked at 3rd) is very high. In fact, researcher 3 has collaborated with both researcher 6 and researcher 5, who are the local centers of different research groups. This implies that researcher 3's collaboration area is broader than his/her peers. His/her closeness measure is also high (ranked in the third place). This shows that he/she has closer collaboration with colleagues than most researchers in the department. He/she also shows potential to collaborate with other researchers in different groups. This is in contrast with researcher 24 who collaborated with others closely in local area (with degree of 8 and is ranked at 2nd), but has a weaker relationship with colleagues (closeness measure is ranked at 7th).

![](/api/attachments/ETSTS326/fulltext/images/0bdd73e86945636e514ec2deb974db1dae48fcdf78939b12c2367ba848097260.jpg)  
Fig. 3. Keywords network map in the department.

Table 5  
Keywords connectivity ranking in the IS department.

<table><tr><td>Rank</td><td>By degree</td><td>By betweenness</td><td>By closeness</td></tr><tr><td>1</td><td>Knowledge management</td><td>Trust</td><td>Trust</td></tr><tr><td>2</td><td>Information systems</td><td>E-commerce</td><td>E-commerce</td></tr><tr><td>3</td><td>Social influence</td><td>Virtual community</td><td>Virtual community</td></tr><tr><td>4</td><td>Satisfaction</td><td>Data mining</td><td>Knowledge sharing</td></tr><tr><td>5</td><td>Trust</td><td>Information systems</td><td>Self-consciousness</td></tr><tr><td>6</td><td>Classification</td><td>Knowledge sharing</td><td>Psychological safety</td></tr><tr><td>7</td><td>IS continuance</td><td>Social influence</td><td>Structural equation modeling</td></tr><tr><td>8</td><td>Knowledge sharing</td><td>Collaboration</td><td>Repurchasing intention</td></tr><tr><td>9</td><td>Web-intention</td><td>IS continuance</td><td>Data mining</td></tr><tr><td>10</td><td>E-commerce</td><td>Satisfaction</td><td>Social influence</td></tr></table>

In order to obtain an integrated measure to assess an individual in the collaboration network, we can assign weights to each of the above three measures and take the weighted average to rank the overall importance of researchers in intra-department collaboration. The overall rank is shown in Table 3 using weights 0.4, 0.3, and 0.3 for degree, betweenness, and closeness, respectively. The weights can be set by the administrator in the system. The integrated measure is called Collaboration In<sup>fl</sup>uence Factor (CIF).

We see that researcher 6 is the most outstanding researcher as he/ she dominates others in the integrated measure. Researcher 9's overall ranking is 2nd since he/she has collaborated a lot and bridge different groups often. The integrated measure CIF shows the social position of the researchers in the department collaboration.

## 4.1.2. Individual collaboration supportiveness

In the standard co-authorship network analysis, we focus on who is connected with whom. That is, as long as two researchers have collaboration, there is a link between them, regardless of their collaboration frequency. In addition, the co-authorship network is an undirected network. The undirected edges cannot show the asymmetric roles each author contributes to the other in the collaboration and, therefore, are unable to answer the questions such as how important the collaboration between two researchers is to each researcher and to the group. To address this challenge, we quantify the importance of collaboration by adopting a contribution-based measure following Han et al. [14]. This enables us to use a directed graph to distinguish the supportive authors from others based on their roles in collaboration. Furthermore, we propose a re<sup>fi</sup>ned measure, “collaboration supportiveness” index, to better identify an individual's contribution in supporting the departmental collaboration.

First, we recognize that not all collaborations should be counted equal ly. We should distinguish each co-author's role in each collaborated work. Let $j = 1 , . . . ,$ N index the N collaborated papers in the local collaboration network. Assume there are m co-authors in paper j. If the paper gives speci<sup>fi</sup>c notes such as “all authors contributed equally to this study”, or the authors are listed alphabetically by last names, we assign equal weight $\begin{array} { r } { w _ { i j } = \frac { 1 } { m _ { i } } } \end{array}$ to co-author i. If the authors are not listed alphabetically by last names, we assume there is an implicit order where the <sup>fi</sup>rst author contributed the most and the last author contributed the least in the collaboration. We assign a score m +1−k to the co-author whose name is at the kth place in the co-authored paper. For example, in a paper with four co-authors, the <sup>fi</sup>rst author gets a score of 4, and the second author gets 3, the third author gets 2, and the last author gets 1. Then we divide this score by the sum of scores of all co-authors to get the weighted score for each co-author. That is, the <sup>fi</sup>nal weighted score for the researcher i who is at the kth place in the jth paper that has m co-authors is: $w _ { i j } = \frac { m _ { j } + 1 - k } { \sum _ { i = 1 } ^ { m _ { j } } i }$ . If researcher i is not involved in a collaborated paper j, we assign $w _ { i j } = 0 .$ . Therefore, the aggregated weight for collaborated work by researcher i is $\begin{array} { r } { \nu _ { i } { = } \sum _ { j { = } 1 } ^ { N } w _ { i j } . } \end{array}$ For single-authored paper, the weight is automatically assigned by 1. So the weighted sum for single-authored papers is just the number of single-authored publications, denoted by q<sub>i</sub>. Therefore, the total weighted number of publications for researcher i is $p _ { i } = { \nu } _ { i } + q _ { i } .$

Next, we focus on the nodes and links construction in the collaboration network. Each researcher is denoted as a node. There is a directed arc from node i to node k. Let $N _ { i k } { = } \{ j | \mathbf { b } \mathbf { 0 } \mathrm { t h } $ researchers i and k are in paper j} be the index set of collaborated papers between researcher i and researcher k in the collaboration network. The collaboration weights between the two researchers are calculated as $\begin{array} { r } { \nu _ { i k } { = } \sum _ { j = 1 } ^ { N _ { i k } } w _ { i j } } \end{array}$ and $\boldsymbol { v } _ { k i } =$ $\begin{array} { r } { \sum _ { j = 1 } ^ { N _ { i k } } \boldsymbol { w } _ { k j } , } \end{array}$ respectively. We further de<sup>fi</sup>ne several concepts as follows.

![](/api/attachments/ETSTS326/fulltext/images/8ea47f7df22958350da2a0f12947ee4314329ea02896137936c617c1d2b2ea33.jpg)  
Fig. 4. Collaboration topic groups in the department.

Table 6  
Author centrality in the author–topic network.

<table><tr><td>Rank</td><td>RID</td><td>Degree</td><td>RID</td><td>Betweenness</td><td>RID</td><td>Closeness</td></tr><tr><td>1</td><td>16</td><td>39</td><td>4</td><td>0.3537</td><td>4</td><td>0.2509</td></tr><tr><td>2</td><td>4</td><td>35</td><td>45</td><td>0.1993</td><td>49</td><td>0.2331</td></tr><tr><td>3</td><td>7</td><td>33</td><td>49</td><td>0.1989</td><td>20</td><td>0.2231</td></tr><tr><td>4</td><td>49</td><td>30</td><td>16</td><td>0.1750</td><td>45</td><td>0.2089</td></tr><tr><td>5</td><td>6</td><td>29</td><td>7</td><td>0.1538</td><td>38</td><td>0.2062</td></tr><tr><td>6</td><td>30</td><td>26</td><td>6</td><td>0.1169</td><td>15</td><td>0.2033</td></tr><tr><td>7</td><td>40</td><td>20</td><td>20</td><td>0.1099</td><td>31</td><td>0.2019</td></tr><tr><td>8</td><td>38</td><td>20</td><td>38</td><td>0.1029</td><td>18</td><td>0.2013</td></tr><tr><td>9</td><td>46</td><td>19</td><td>46</td><td>0.0792</td><td>11</td><td>0.2002</td></tr><tr><td>10</td><td>47</td><td>16</td><td>11</td><td>0.0771</td><td>10</td><td>0.1999</td></tr></table>

The boldface type is used to highlight RIDs that are among top 10 based on all three measures (degree, betweenness, and closeness).

De<sup>fi</sup>nition 1 (Support). The support from researcher i to researcher k is de<sup>fi</sup>ned as $\begin{array} { r } { s _ { i k } = \frac { \nu _ { i k } } { p _ { k } } . } \end{array}$

Support is the ratio of the number of co-authored papers between the two researchers divided by the number of papers that researcher k has published. Therefore, there is a bi-directional link between any two nodes, with their respective asymmetric weights showing the supportiveness to each other.

De<sup>fi</sup>nition 2 (In/Out Support). The In-Support for researcher $i , S _ { I } ( i ) =$ $\sum { _ { k \neq i } S _ { k i } }$ is the support that researcher i receives from others; the Out-Support for researcher $\begin{array} { r } { i , S _ { O } ( i ) = \sum _ { k \neq i } s _ { i k } , } \end{array}$ is the support that researcher i provides to others.

The <sup>fi</sup>nal collaboration supportiveness index can be calculated as follows.

De<sup>fi</sup>nition 3 (Collaboration supportiveness). Collaboration supportiveness of researcher i is the net support of this researcher in the collaboration network: $c s _ { i } { = } S _ { O } ( i ) - S _ { I } ( i )$ ; the normalized collaboration supportiveness is the ratio of net support to the total number of collaborated papers: $\begin{array} { r } { u _ { i } = \frac { c s _ { i } } { v _ { i } } } \end{array}$

Collaboration supportiveness measures the ability of a researcher contributing to the departmental collaboration. Table 4 ranks researchers based on our proposed collaboration supportiveness measure.

Different from the insight obtained in the previous subsection, researcher 24, who is ranked as 5th is now ranked the <sup>fi</sup>rst by collaboration supportiveness measure. His/her in-support is lower than his/her outsupport, meaning that this researcher provides more support to others than what he/she receives from others. Clearly, the high overall collaboration supportiveness score indicates the researcher's critical position in supporting other researchers' collaborative work in the department.

It is worth noting that the two rankings complement, rather than contradict, with each other. The rankings in Table 3 focus on the broadness of collaboration (how many different collaborators an individual researcher has), while the rankings in Table 4 emphasize on the depth of collaboration (to what proportion one's work is supported by others or one supports others in the collaboration). Combing these two network analyses, we are able to recognize a variety of faculty research abilities, especially their speci<sup>fi</sup>c roles to support other faculty's research in the intra-department collaboration.

Directed networks have been constructed in the study of citations among scienti<sup>fi</sup>c papers and journals. For example, the directed links can be de<sup>fi</sup>ned as the average number of citations a paper received. It represents a type of voting by in-links that serves as a proxy for the collective attention that the scienti<sup>fi</sup>c community pays to a paper. Moreover, citations from journals that are of high impact should be viewed as more important. Following a similar notion of Google's PageRank for web pages, a PageRank importance measure has been used in citation network to rank authors [9]. We have not found other applications that analyze collaboration using directed networks.

## 4.2. Collaboration group identification

Collaboration groups can be de<sup>fi</sup>ned as a group of authors, a group of topics, even a group of authors associated with topics. In the following subsections, we illustrate each of these applications based on authorcentered, topic-centered, and author–topic network analyses.

## 4.2.1. Cohesive group of researchers

By analyzing co-authorship network, it is straightforward to identify the cohesive group of researchers. Fig. 2 shows the structure of the network and the identi<sup>fi</sup>ed groups. The numbers beside the nodes are researcher identi<sup>fi</sup>cation numbers. The numbers on the edges are the number of collaborated papers between two researchers. Three major collaboration groups are easily identi<sup>fi</sup>ed and are indicated by circles in the <sup>fi</sup>gure. We see that researchers 5, 6, 9, 24, and 38 are located in their respective local centers within the department collaboration network. Moreover, researchers 24, 38, 39, 40, and 54 form the most cohesive group in which everyone has collaboration with everyone else in the group.

Table 7  
Topic centrality in the author–topic network.

<table><tr><td>Rank</td><td>By degree</td><td>By betweenness</td><td>By closeness</td></tr><tr><td>1</td><td>Knowledge management</td><td>Information systems</td><td>Knowledge management</td></tr><tr><td>2</td><td>Trust</td><td>Knowledge management</td><td>Knowledge sharing</td></tr><tr><td>3</td><td>Knowledge sharing</td><td>Knowledge sharing</td><td>Information systems</td></tr><tr><td>4</td><td>Semantic web rule language</td><td>E-commerce</td><td>China</td></tr><tr><td>5</td><td>Owl (ontology web language)</td><td>Human-computer interaction</td><td>Data mining</td></tr><tr><td>6</td><td>Crisis contagion management</td><td>Game theory</td><td>E-commerce</td></tr><tr><td>7</td><td>Ontology</td><td>Online community</td><td>Game theory</td></tr><tr><td>8</td><td>Concept mapping</td><td>China</td><td>Negotiation</td></tr><tr><td>9</td><td>Problem solving</td><td>Trust</td><td>Quality of service</td></tr><tr><td>10</td><td>Entropy</td><td>Virtual community</td><td>Constraint satisfaction</td></tr><tr><td>11</td><td>Information theory</td><td>Business intelligence</td><td>Distributed decision making</td></tr><tr><td>12</td><td>Negotiation</td><td>Classification</td><td>Coordination</td></tr><tr><td>13</td><td>Game theory</td><td>Web design</td><td>Supply chain management</td></tr><tr><td>14</td><td>Virtual community</td><td>Data mining</td><td>Software agent</td></tr><tr><td>15</td><td>Text mining</td><td>Negotiation</td><td>Managerial control</td></tr><tr><td>16</td><td>Domain ontology</td><td>Social network analysis</td><td>E-government</td></tr><tr><td>17</td><td>Decision support system</td><td>Text mining</td><td>Developing country</td></tr><tr><td>18</td><td>China</td><td>Managerial control</td><td>Agency theory</td></tr><tr><td>19</td><td>Online community</td><td>E-government</td><td>Business intelligence</td></tr><tr><td>20</td><td>Human-computer interaction</td><td>Developing country</td><td>Team-external coordination</td></tr></table>

![](/api/attachments/ETSTS326/fulltext/images/284340b4c8b95e3243b0213d155a862ed82e63a657cbc7648b76bb3167754390.jpg)  
Fig. 5. Cohesive group in the author–topic network.

## 4.2.2. Research themes identification

Main research themes are identi<sup>fi</sup>ed through the topic network. In the topic network, keywords are represented as nodes. If two keywords appear in the same article, there is a tie between the two keywords. The strength of a tie is determined by the frequency of co-occurrence of the two keywords in the same article. Fig. 3 is the visualized keyword network map.

The range of degree is from 2 to 21 and the average degree of the topic network is 5.2. The higher degree of a topic indicates a wider connection with other topics. The average degree shows the concentration of topics in the collaboration network. The top 10 keywords by degree, betweenness, and closeness are listed in Table 5.

We have several observations. First, based on the measure of degree, knowledge management, information systems, and social in<sup>fl</sup>uence are the top three most collaborated keywords. This shows that these keywords frequently occur in the department research. Second, based on the measure of betweenness and closeness, trust, e-commerce, and virtual community are the top three keywords to connect different areas. Their average distances to all other keywords are among the shortest. This implies that these keywords play the most signi<sup>fi</sup>cant role in bridging different types of the department research.

We further investigate the research themes in collaborated topics by strong components extracted from the topic network. Fig. 4 presents further insights about the core topic groups in the department. We see that the departmental collaboration is mainly clustered in three topic groups. The topic group on the top is related to information system development and virtual team. The topic group at the bottom is related to decision support systems. The topic group on the left is about technology adoption.

![](/api/attachments/ETSTS326/fulltext/images/49189b22517b1195134070c38b6effd81ec617bea837c72117df135e50a3a439.jpg)  
Fig. 6. Core analysis in the author–topic network

Table 8  
Illustration of researcher-theme paths.

<table><tr><td>Starting point</td><td>Ending point</td><td>Researcher-theme paths</td></tr><tr><td>RID14</td><td>RID32</td><td>Online community</td></tr><tr><td>RID2</td><td>RID1</td><td>Online community-RID14-trust</td></tr><tr><td>RID10</td><td>RID21</td><td>Trust-satisfactiton-RID14</td></tr><tr><td>Trust</td><td>Virtual community</td><td>RID13</td></tr><tr><td></td><td></td><td>RID28</td></tr><tr><td></td><td></td><td>RID48</td></tr></table>

## 4.2.3. Research groups and topics joint analysis

In addition to analyzing researcher groups and topic groups separately, we can perform joint analysis of researchers and their associated topics in the author–topic network. This network is constructed by connecting researchers and standard keywords if he/she has published an article indexed by some keywords.

In general, the two-mode network can be transformed into two onemode networks. One is the transformed author network. If two authors share the same keywords, there is a tie between them, and the strength of the tie is the number of keywords shared by the two authors. The other is the transformed topic network. If two keywords are shared by two authors, there is a tie between them, and the strength of the tie is the number of authors who share the keywords. We illustrate the relationship between collaboration topics and researchers using the departmental collaboration data. There are 318 topics and 55 researchers in this local network. The top 10 researchers and top 20 topics in centrality measure are reported in Tables 6 and 7.

We see that several researchers connect with over 30 keywords. The highest betweenness measure is 0.35 and the highest closeness measure is 0.25. The correlation between the degree measure and their betweenness/closeness measures are not very high. This implies that the highly collaborative researchers conduct research in a variety of topics, and through them more topics and researchers are reachable.

Overall, researchers 4 and 49 play the most important roles in the department collaboration network. Although researchers 16, 7, and 6 have as diverse topics as researchers 4 and 49, the betweenness and closeness measurements show they are more constrained to collaborate within a small group. Since these researchers are capable of doing research across a wide range of topics, the department may create opportunities to encourage them to expand their collaboration with other faculty and boost the overall productivity in the department.

For the keywords, higher degree implies more researchers share the keywords. For example, knowledge management and information sharing are very popular collaboration topics among the researchers. The rankings by betweenness and closeness show the connectivity of these keywords with the authors and other keywords. Based on the above analysis, knowledge management and information systems have demonstrated the highest capability of connecting the researchers with different research interests and creating new study areas.

In order to gain more insights, we further conduct core-periphery analysis on the two-mode network. The core is de<sup>fi</sup>ned as a cluster of frequently co-occurring researchers and topics. The core consists of a partition of researchers who are closely connected with each of the topics in a topic partition, and simultaneously a partition of topics that are closely connected with the researchers in the core partition. The periphery consists of a partition of researchers who do not share the same topics, and a partition of topics that are disjoint because they have no researchers in common.

We apply the strong component analysis to the two-mode network and get the most cohesive group of 10 researchers and 20 topics as shown in Fig. 5. The graph reveals how leading researchers are connected with popular research topics. We see that researchers 14 and 21 have are the highly connected nodes. This shows that their expertise covers a wide range of research areas.

Next, we apply the core analysis to the author–topic network to identify the subgraphs with the highest connections. Two subgraphs are identi<sup>fi</sup>ed with the authors and topics, as shown in Fig. 6. The cluster on the left is about information processing for knowledge management. The cluster on the right is about web ontology and language. This shows that the expertise of researchers is highly clustered on these topic areas.

## 4.3. Researcher-theme path identification

The researcher-theme path identi<sup>fi</sup>cation is another important function in our local social network-based research management framework. Generally, the path between two given vertices in a graph is de<sup>fi</sup>ned as a sequence of vertices that connect these two endpoints. For any network we constructed in the research management context, we can provide all the paths between any two given nodes and the short paths have the priority. Here we use the author–topic network as an example to demonstrate the managerial insights conveyed by the different paths.

Table 8 demonstrates several types of researcher-theme paths that can be obtained from the author–topic two-mode social network analysis.

For example, it shows that researcher 14 and researcher 32 have collaborated on topics related to online community. It suggests that, although researchers 2 and 1 do not have overlapped research topics, they may work together with researcher 14 on topics such as trust issues in online community. Similarly, researchers 10 and 21 can work on online trust and customer satisfaction in the e-commerce environment, with the help from researcher 14 who has the relevant expertise in both areas.

![](/api/attachments/ETSTS326/fulltext/images/733db8223065c2429072e415134c620352ccddf0c38b08638cef7fcc58138195.jpg)  
Department Collaboration within College of Business

![](/api/attachments/ETSTS326/fulltext/images/7427ca2fb84c106ac3ba89c8335a5e0e875681119c02b588bf2acdfc867ed536.jpg)  
Department Collaboration within the University  
Fig. 7. Cross boundary collaborations of the department. Department collaboration within college of business. Department collaboration within the university

From another perspective, if there is a good funding opportunity related to trust building in virtual community, then the system recommends researchers 13, 28, or 48 might be good candidates. Research management of<sup>fi</sup>ce may inform these researchers about this funding opportunity.

## 5. Strategic planning

After detailed analyses of individual researchers and topics in the intra-department collaboration, a high level view beyond the department boundary and across the university is also important for the strategic planning of the university research management of<sup>fi</sup>ce. This is the fourth management function in Table 1. As an illustration, collaborations between the focal department and other departments within and outside the college are visualized in Fig. 7.

The graph on the left shows that the Departments of Information Systems, Management, and Marketing form a triad, which denotes a cohesive collaboration group. The graph on the right reveals that the IS Department has collaboration with Computer Science, Mathematics departments, and Of<sup>fi</sup>ce of Education Development. From research management perspective, the university research of<sup>fi</sup>ce can make favorable policies to promote collaboration among IS, Marketing and Management within College of Business, between IS and Computer Science, as well as continued support in education.

To gain better insights about IS research in a broader context, we may expand the scope of analysis to consider collaboration with other universities and with other researchers in different geographical locations. Further analysis shows that the IS Department has the most collaboration with University of Science and Technology of China (USTC). The collaboration with University of Arizona is ranked the second. Geographically, the IS Department has the most collaboration with mainland China, followed by USA and Hong Kong. These facts can be used by research management to evaluate past research performance and identify future collaboration opportunities. For example, the large number of collaborations with USTC that involve research students demonstrated that the joined Ph.D. education program launched eight years ago is highly successful. The strong collaboration relationship with University of Arizona indicates new opportunities to address the increasing demand for higher education. Therefore, the IS Department is encouraged to establish a collaborated Ph.D. program with them.

We further identify disciplines that are closely related to the IS discipline. After performing discipline network analysis, Business, Management, and Information Science are identi<sup>fi</sup>ed as the most relevant disciplines. This suf<sup>fi</sup>ciently demonstrates that IS is an interdisciplinary discipline between business and technology.

Finally, we demonstrate the university collaboration relationship in Fig. 8. The size of the circle is in proportion to the quantity of publications of the nodes. The values on the edges denote the quantity of collab orated papers between departments. A total of 35 units are identi<sup>fi</sup>ed among 20 colleges and centers within the university.

The average degree of this network is 2.5. This means that on average there are two papers collaborated between all the departments in the university. The green nodes in the <sup>fi</sup>gure denote School of Science and Engineering. The yellow ones denote School of Business and the red ones School of Liberal Arts and Social Science. We can see that School of Science and Engineering has plenty of collaboration both within and outside the school with other departments. It appears that this school has collaborated with almost all the other schools and centers.

Further drill down of the information shows that Department of Electronic Engineering (EE) plays an important role in the intra-university collaboration. This con<sup>fi</sup>rms the important position of EE in the university. The university gives priority to EE since it has eight IEEE Fellows and got the highest cumulative funding from Government's Competitive Research Grants in Electrical and Electronics Ares among all six universities in Hong Kong over years.

Similarly, we can perform two-mode network analyses for the department-topic network, discipline-topic network, and universitytopic network. The longitude social network analysis can be used to trace the trend of collaboration patterns.

## 6. Conclusion

This study takes a local social network approach to transform traditional research management in several aspects. First, we aim to inform managers about individual researchers and their collaboration relationships. We propose a new measure “collaboration supportiveness” to take into account an individual's contribution to support others' research. In comparison with the traditional methods that focus on quantity of publications, journal impacts, citation counts to assess research performance, the multi-dimensional and multi-level analyses provide a comprehensive understanding of an institution's research contribution both for individu al researchers and in the relevant context of collaboration.

![](/api/attachments/ETSTS326/fulltext/images/b74a76f258ea7504b330b6ef0e4c282c8e5cd9c1ad9f7988b8e89964bd484fa4.jpg)  
Intra-University Collaboration by Departments

![](/api/attachments/ETSTS326/fulltext/images/69210b3d563533a18f8da581f7ae1aef2dca21672a1dab631b74f4994ead8dd2.jpg)  
Intra-University Collaboration by Schools  
Fig. 8. Overview of intra-university collaboration. Intra-university collaboration by departments. Intra-university collaboration by schools.

Second, different from the bibliometric analysis in the IS literature, our analysis takes a more relevant local network perspective. Taking researchers, research topics, af<sup>fi</sup>liated departments and research centers, and research disciplines as different entities, we combine several social network analysis techniques including core-periphery analysis and twomode network analysis methods to reveal the collaboration patterns. We constructed several local social networks that provide additional insights particularly useful to support organizational level decision making such as internal resource allocation, recognizing top contributors, prioritizing research activities, and growing research capacity. Our objective is to build a more transparent research environment and gain more visibility in terms of the roles both individual researchers and institutional units (research centers and departments) play in various research activities. Patterns obtained from our local social network analyses also provide objective evidences for academic researcher ranking, as well as expert recommendation.

Several extensions are possible for future research. As mentioned, current analysis is based on published research data collected from several databases. Other research relevant data such as working papers that are not captured by these public sources are not incorporated into the analysis, although such information is helpful to identify an individual's supportiveness and collaborating ability in his/her local networks. Currently, our university research portal is expanding its ability to share working papers and other technical reports to promote timely dissemination of research outputs and knowledge production. However, much information is presented in non-standard format. We need more advanced text mining tools to extract useful information to enhance the current data analysis capability.

In this study, we have purposely omitted citation network analysis as its effect is inherently global. Our focus is on local collaboration relations. However, the analysis methods are universal and the system has the capability to provide both local and global views. In addition to the statistical reports, summary data can be visualized in various formats such as the tabular view, the graph view, and the map view. In the future, we will continue to enrich the current framework by adding more functionalities and analysis methods. For example, we may incorporate the forecasting functions to predict the likelihood of a research center being funded by major funding agencies in certain topic area and the corresponding funding scale. We may also use predictive models to foresee the future research outcome and impacts based on local research capabilities.

Overall, we provide a new, local network-based approach to scientific research management, which is very useful for institutional decision support and recommendation. We have demonstrated that the new approach brings many additional bene<sup>fi</sup>ts unavailable from traditional research management methods. The new approach has the potential to improve research management ef<sup>fi</sup>ciency, enable resource sharing and enhance research collaboration.

## Acknowledgements

This research is partially funded by the General Research Fund of the Hong Kong Research Grant Council (Project No: CityU 119611), the National natural Science Foundation of China (Project Nos: 71171172, J1124003) and City University of Hong Kong (Project No: 6000201).

## References

[1] A. Bajaj, R. Russell, AWSM: allocation of work<sup>fl</sup>ows utilizing social network metrics Decision Support Systems 50 (1) (2010) 191–202.

[2] L. Barabasi, H. Jeong, Z. Neda, E. Ravasz, A. Schubert, T. Vicsek, Evolution of the social network of scientific collaborations, Physica A 311 (3–4) (2002) 590–614

[3] S. Bhattacharjee, J.R. Marsden, H. Singh, An approach to identify in<sup>fl</sup>uential building blocks and linkages in an information resource network, Decision Support Systems 52 (2011) 217–231.

[4] M. Callon, J.P. Courtial, F. Laville, Co-word analysis as a tool for describing the network of interactions between basic and technological research: the case of polymer chemistry Scientometrics 22 (1) (1991) 155–205.

[5] W.T. Chiu, Y.S. Ho, Bibliometric analysis of tsunami research, Scientometrics 73 (1) (2007) 3–17.

[6] J. Choi, S. Yi, K.C. Lee, Analysis of keyword networks in MIS research and implications for predicting knowledge evolution, Information Management 48 (8) (2011) 371–381.

[7] M.J. Culnan, The intellectual development of management information systems, 1972–1982: a co-citation analysis, Management Science 32 (2) (1986) 156–172.

[8] M.J. Culnan, Mapping the intellectual structure of MIS, 1980–1985: a co-citation analysis, MIS Quarterly 11 (3) (1987) 341–353.

[9] Y. Ding, E. Yan, A. Frazho, J. Caverlee, PageRank for ranking authors in co-citation networks, Journal of the American Society for Information Science and Technology 60 (11) (2009) 2229–2243.

[10] L. Egghe, Theory and practise of the g-index, Scientometrics 69 (1) (2006) 131–152.

[11] J. Goldenberg, L. Barak, M. Eitan, S. Stremerch, The evolving social network of marketing scholars, Marketing Science 29 (3) (2010) 561–567.

[12] S. Goyal, M.J. van der Leij, J.L. Moraga-González, Economics: an emerging small world, Journal of Political Economy 114 (2) (April 2006) 403–412.

[13] J.W. Grossman, P.D.F. Ion, On a portion of the well-known collaboration graph Congressus Numerantium 108 (1995) 129–131.

[14] Y. Han, B. Zhou, J. Pei, Y. Jia, Understanding importance of collaborations in coauthorship networks: a supportiveness analysis approach, in: Proc. the Ninth SIAM International Conference on Data Mining, 2009, pp. 1112–1123.

[15] T. Heck, O. Hanraths, W.G. Stock, Expert recommendation for knowledge management in academia, Proceedings of the American Society for Information Science and Technology (ASIST) 48 (1) (2011) 1–4.

[16] J.E. Hirsch, An index to quantify an individual's scienti<sup>fi</sup>c research output, Proceedings of the National Academy of Sciences 102 (46) (2005) 16569–16572

[17] K. Hori, K. Nakakoji, Y. Yamamoto, J. Ostwald, Organic perspectives of knowledge management: knowledge evolution through a cycle of knowledge liquidization and crystallization, Journal of Universal Computer Science 10 (3) (2004) 252–261.

[18] D. Hu, J.L. Zhao, J. Cheng, Reputation management in an open source developer social network: an empirical study on determinants of positive evaluations, Decision Support Systems 53 (3) (2012) 526–533.

[19] M. Keith, H. Demirkan, M. Goul, The in<sup>fl</sup>uence of collaborative technology knowledge on advice network structures, Decision Support Systems 50 (1) (2010) 140-151.

[20] J. Kleinberg, Small-world phenomena and the dynamics of information, in: Proc. Advances in Neural Information Processing Systems, 14, 2001, pp. 431–438.

[21] H. Kretschmer, Author productivity and geodesic distance in bibliographic coauthorship networks, and visibility on the web, Scientometrics 60 (3) (2004) 409–420.

[22] J. Law, J. Whittaker, Mapping acidi<sup>fi</sup>cation research: a test of the co-word method, Scientometrics 23 (3) (1992) 417–461.

[23] P.C. Lee, H.N. Su, Investigate the structure of regional innovation system research, Innovation: Management, Policy & Practice 12 (1) (2010) 26–40.

[24] Z. Ma, O.R.L. Sheng, G. Pant, Discovering company revenue relations from news: a network approach Decision Support Systems 47 (4) (2009) 408–414

[25] J. Ma, W. Liu, W. Xu, H. Jiang, Smart research makes management scienti<sup>fi</sup>c: a novel lean project management for national natural science funding China, National Natural Science Funding 6 (2011) 331–334.

[26] A. Mayer, Online social networks in economics, Decision Support Systems 47 (3) (2009) 169–184.

[27] J. Moody, The structure of a social science collaboration network: disciplinary cohesion from 1963 to 1999, American Sociological Review 69 (2) (2004) 213–238.

[28] C.M. Morel, S.J. Serruya, G.O. Penna, R. Guimarães, Co-authorship network analysis: a powerful tool for strategic planning of research, development and capacity building programs on neglected diseases, PLoS Neglected Tropical Diseases 3 (8) (2009) e501.

[29] M.E.J. Newman, The structure of scienti<sup>fi</sup>c collaboration networks, Proceedings of the National Academy of Sciences of the United States of America 98 (2) (2001) 404–409.

[30] M.E.J. Newman, M. Girvan, Finding and evaluating community structure in networks, Pattern Recognition Letters 69 (2) (2004) 413–421.

[31] W. Oh, J.N. Choi, K. Kim, Coauthorship dynamics and knowledge capital: the patterns of cross-disciplinary collaboration in information systems research, Journal of Manage ment Information Systems 22 (3) (2005) 265–292.

[32] F. Osareh, Bibliometrics, citation analysis and co-citation analysis: a review of literature I, Libri 46 (1996) 149–158.

[33] L. Page, S. Brin, R. Motwani, T. Winograd, The pagerank citation ranking: bring orders to the web, Technical support, Stanford University, 1998.

[34] R. Rubin, Foundations of library and information science, Neal-Schuman Publishers, New York, 2010.

[35] K.A. Walstrom, L.N.K. Leonard, Citation classics from the information systems literature, Information Management 38 (2) (2000) 59–72.

[36] M.M. Wasko, R. Teigland, S. Faraj, The provision of online public goods: examining social structure in an electronic network of practice, Decision Support Systems 47 (3) (2009).254-265

[37] S. Wasserman, K. Faust, Social Network Analysis: Methods and Applications, Cambridge University Press Cambridge: New York 1994

[38] E.A. Whitley, R.D. Galliers, An alternative perspective on citation classics: evidence from the <sup>fi</sup>rst 10 years of the European Conference on Information Systems, Information Management 44 (5) (2007) 441–455.

[39] D. Zhou, S.A. Orshanskiy, H. Zha, C. Lee Giles, Co-ranking authors and documents in a heterogeneous network, in: IEEE International Conference On Data Mining (ICDM) 2007, pp. 739–744.

Xiaoyan Liu is a research fellow in the Department of Information Systems at City University of Hong Kong. She received her Ph.D. in Information Systems at the City University of Hong Kong in 2008. Her research interests include data mining, <sup>fi</sup>nancial information systems, social network analysis, research management and recommendation systems. Dr. Liu's papers have been published in journals including IEEE Transactions on Knowledge & Engineering, Applied Mathematics and Computation, and Optimization Methods & Software.

Zhiling Guo is an Assistant Professor in Information Systems at the City University of Hong Kong. She received her Ph.D. in Management Science and Information Systems from The University of Texas at Austin in 2005. Dr. Guo's general research interests include market mechanism design, supply chain information sharing, and e-commerce channel strategies. Dr. Guo's papers have been published in Management Science, Information Systems Research, Decision Support Systems, Journal of Management Information Systems, Journal of the Association for Information Systems, Information & Management, and European Journal of Operational Research.

Zhenjiang Lin is a business analyst at the CITINet Ltd., working on core algorithm design for academic recommendation systems and research management systems. He received his Ph.D. in Computer Science and Engineering from the Chinese University of Hong Kong in 2011. His research interests include Web mining, link analysis, social network, and recommender systems. He has years of industry experiences in software development, system design, and complex data analysis. Dr. Lin's papers have been published in journals including IEEE Transactions on Knowledge & Engineering, Knowledge and Information Systems, and Applied Mathematics and Computation.

Jian Ma is a professor in the Department of Information Systems, City University of Hong Kong. He received his Ph.D. in Computer Science from Asia Institute of Technology in 1991. He was a Lecturer in the School of Computer Science and Engineering at the University of New South Wales, Australia, before joining City University in 1993. Dr. Ma's research areas include web-based decision support systems and object-oriented methods for information system development. His research has been published in IEEE Transactions on Engineering Management, IEEE Transactions on Education, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems, and European Journal of Operational Research.
