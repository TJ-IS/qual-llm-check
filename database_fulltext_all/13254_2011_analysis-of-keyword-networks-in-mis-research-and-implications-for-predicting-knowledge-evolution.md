---
otero_id: 13254
otero_key: "YMCGDP2A"
title: "Analysis of keyword networks in MIS research and implications for predicting knowledge evolution"
authors: "Jinho Choi; Sangyoon Yi; Kun Chang Lee"
year: "2011"
journal: "Information & Management"
doi: "10.1016/j.im.2011.09.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analysis of keyword networks in MIS research and implications for predicting knowledge evolution

Jinho Choi <sup>a</sup>, Sangyoon Yi <sup>b,</sup>\*, Kun Chang Lee <sup>c,</sup>\*\*

<sup>a</sup> School of Business, Sejong University, Seoul, Republic of Korea

<sup>b</sup> Department of Marketing and Management, University of Southern Denmark, Denmark

<sup>c</sup> SKK Business School and Department of Interaction Science, Sungkyunkwan University, Seoul, Republic of Korea

## A R T I C L E I N F O

Article history: Received 23 June 2010 Received in revised form 18 July 2011 Accepted 29 August 2011 Available online 10 September 2011

Keywords: Keyword network MIS research Scale-free network Network analysis Centrality Trend analysis

## A B S T R A C T

New concepts and ideas build on older ones. This path dependence in knowledge evolution has promoted research to identify important knowledge elements, research trends, and opportunities by analyzing publication data. In our study, keyword networks formed from published academic articles were analyzed to examine how keywords are associated with each other and to identify important keywords and their change over time. Based on MIS publication data from 1999 to 2008, our analysis provided several notable findings. First, while the MIS field has changed rapidly, resulting in many new keywords, the connectivity among them is highly clustered. Second, the keyword networks show clear power-law distribution, which implies that the more popular a keyword, the more likely it is selected by new researchers and used in follow-on studies. In addition, a strong hierarchical structure is identified in the network. Third, the network-based perspective reveals interdisciplinary keywords which are different from popular ones and have the potential to lead research in the MIS field.

\- 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Being able to remain innovative and competitive has become heavily dependent on an organizations’ ability to promote knowledge creation and make best use of it [8]. As a consequence, knowledgemanagementandthe roleofsocialnetworkinknowledge sharing has become a popular research stream [6,7,11]. How knowledge is organized and evolves over time is an important question. The structure of knowledge and itsevolution are correlated withsocialstructure, becausenew ideasbuild onexistingknowledge and researchers are grouped in geographic, university, professional societies and this social structure tends to shape the form and variation of shared knowledge among them. Consequently, a network perspective has to be taken in the study of knowledge.

New concepts and ideas often result from extensive recombination of existing concepts or ideas [14,16]. In academia, researchers build on existing concepts and ideas to develop new ideas and theories that in turn serve as a basis for further research. The popularity of some keywords serve as an indicator of the importance of the research themes they represent. Further, when relationships among the keywords is drawn as a keyword network, network metrics such as centrality and betweenness can be used to elicit novel insights into and implications for the organization and evolution of knowledge.

In our study, we therefore attempted to (1) construct keyword networks from the papers published in five major journals in MIS research during the period from 1998 to 2008, (2) investigate the characteristics of the MIS keyword network by utilizing networkrelated measures, (3) find and compare important keywords from both popularity- and network-based perspectives, and (4) examine the change in the important keywords over time. The MIS research field was chosen for our investigation because:

1. To the best of our knowledge, there has been no previous study investigating the keyword network of the MIS research field.

2. Since the MIS research field is highly interdisciplinary in nature, the introduction and association of new concepts and keywords has been very active.

3. Our findings should provide useful insights to better understand the intellectual structure and research trends of a scientific field, such as the scale-free connectivity of keywords and the hierarchic structure of keyword networks.

## 2. Literature review

## 2.1. Identification of research themes

Efforts to identify research themes in a given field could enhance our understanding of it and may stimulate further research. Such research may be either popularity-based (typically using the titles or keywords of papers and analyzing their frequency of use; i.e., how often they appear in papers) or network-based (dealing with citations that represent the relationships among papers and authors).

For example, Ord et al. [15] used the popularity based approach to analyze the titles and keywords of papers published in the animal behavior research field utilizing knowledge visualization and data mining tools. Specifically, they evaluated similarities among the words in the paper titles and identified research topics by clustering the papers based on them. They also identified popular words in the paper titles using a burst detection algorithm.

Huang [9] examined the frequency of keywords in studies of obstructive sleep apnea (OSA). This analysis revealed a trend of specialization and identified large number of keywords that were used only once. Combined with the variety of subject categories, this seems to indicate a lack of continuity in this area of research and a wide disparity in research focus corresponding to the increased significance of OSA in multiple disciplines. An interesting variation, which has potential for further development and application, is a keyword-based morphology analysis [24]; Yoon and Park employed factor analysis and text mining to analyze patent keywords to identify new technology opportunities.

In network-based approach, Whitley and Galliers [23] analyzed the citation network of papers published in IS research to identify core research themes and up-to-date research subjects. Meyer et al. [10] also based their works on a citation network in order to reveal the intellectual structures of the research areas in strategic management, social simulation, and accounting. In this research paradigm, the visual representation of a citation network can help readers identify significant movements in research fronts and emerging research fields [3,5].

However these two approaches have inherent weaknesses. In the case of the popularity-based approach, the frequency analysis of titles or keywords could indicate their importance, but this information is post-publication. Moreover, this analysis cannot account for redundancy as more researchers work on them. In contrast, the network-based approach resolves this problem by analyzing the network structures. The duplication of a relationship between two elements of a network, for example, makes no difference to the network structure. However, a citation network does not directly represent a knowledge network.

Given this hole in the extant literatures, we investigated the relationships among keywords of published papers from a network perspective by constructing a keyword network for the MIS research field.

## 2.2. Complex networks

Research on complex networks has been a growing area in the past two decades. In its infancy, the study of complex networks had been limited to mathematical graph theory and social network analysis. In the 1950s, two mathematicians, Paul Erdo¨s and Alfred Re´nyi, proposed a random graph, the simplest and most straightforward example of a complex network. In sociology, applied research focused on a variety of networks from individuals to families to nations. One well known instance is the theory posited by Milgram. His famous theory claimed that there is a path of acquaintances with a typical length of about six between most pairs of people in the United States. He showed empirical evidence of this small world.

The availability of large-scale empirical data and the advances in computing power and theoretical understanding have led to a series of discoveries that have uncovered the topological properties that are common to a variety of diverse real-world networks (e.g., the Internet, scientific collaboration networks [13], and software architecture [20]. These studies show that most realworld networks are characterized by similar topological features (i.e. high clustering and low path-length).

Another important pattern found in real-world complex networks is their nodal degree distribution. Unlike the bell-shaped Poisson distribution of random graphs, the degree distributions of many real-world networks have power-law degree distributions,

$$
p (k) \sim k ^ {- r}\tag{1}
$$

where $p ( k )$ is the probability that a node has k edges. Statistically, the power-law distribution implies that there are a small number of nodes in the network that have a large number of links; thus the distribution of nodal degrees has a long right tail of values that are far above the mean as opposed to the fast-decaying tail of a Poisson distribution. Unlike general normal distributions, the power-law distribution does not have a representative scale. Networks with power-law distributions are therefore often referred to as scalefree networks [2].

## 2.3. Network-related measures

In order to understand the characteristics of the overall keyword network in MIS research, we selectively used a number of welldefined and widely used network-related measures in our analysis.

The first one was the degree centrality of a node; i.e., the number of neighboring nodes to which the focal node is connected. In a keyword network, a node of high degree has many ties with other keywords and interacts with them to constitute the ideas of the papers that hold them. We can determine the average networkwide degree by averaging the degree centrality of all nodes.

The second was the betweenness centrality of a node; i.e., the extent to which a node lies on the paths between other nodes. It is measured as the fraction of the shortest paths between all pairs of other nodes in the network containing the node. In the keyword network, this represents the importance of a keyword in bridging subsets of keywords. For instance, a keyword that lies between two distinctive research themes (i.e., clusters of closely related key words)canhavehighbetweennesscentralityeventhoughitmayhave a small number of connections to other keywords in each theme.

The third was the characteristic path length of the network; i.e., the average length of all the shortest paths between node pairs. The shorter the characteristic path length, the closer the nodes are to each other. The flow of information and ideas tends to be faster in networks of shorter characteristic path length.

The fourth was the clustering coefficient, a network-level measure that illustrates the tendency of nodes to cluster in densely interconnected modules. This indicates the small-world property of the network: it has a small average distance between nodes in spite of the large number of them. The clustering coefficient quantifies the degrees of connectivity to the neighbor nodes in a network; it is measured as the average of the coefficients of all nodes, the ratio of the number of existing connections to the number of possible connections among its neighboring nodes. For instance, if a node has three neighboring nodes with three possible connections among them, although there is only one actual connection, then its clustering coefficient is 1/3 (0.333).

The fifth measure we used was the density of the network, which is obtained by dividing the number of ties in the network by the number of all possible ties; this obviously ranges between 0 and 1, with higher values indicating denser networks, In real-world networks, the density depends on the size of the network; increasing its size generally leads to a decrease in the density.

In addition to using network-related measures, we applied the visualization software LaNet-vi [1] to obtain a clear sense of connectivity, clustering characteristics, and hierarchical properties of keyword networks; it provides images of large scale networks on a two-dimensional layout, whose algorithm is based on k-core decomposition involving the identification of particular subsets of the graph, called k-cores. The k-core of a graph is a maximal subgraph in which each node has at least degree k. It can be obtained by recursively removing all vertices with a degree less than k, until all vertices in the remaining graph have a degree of k or more. A node has coreness k, if it belongs to a k-core but not to a (k + 1)-core. Larger coreness value implies high degree and more central position in the network’s structure. The presence of degree-coreness correlations indicates that the central nodes are most likely high-degree hubs of the network. In this way, the k-core decomposition can disentangle the hierarchical structure of the network.

## 3. Data and keyword networks

Our aim was to investigate the characteristics of the keyword network of MIS research and to identify the important keywords from this perspective. To fulfill this goal, we selected the five top journals in the MIS research field and constructed a database composed of keywords from all papers published in the journals during the 10-year period from 1999 to 2008. Then we examined the characteristics of the keyword networks and identified important keywords from the view point of their frequency of use in the publications and centrality in the keyword network. We also determined how the important keywords varied across the importance measures and selected journals.

Given that different MIS researchers might have different opinions about the characteristics of their journals in MIS research, we attempted to obtain a set of journals with a broad degree of theoretical/empirical/technical frameworks approach. Given the objective of our study, the target journals had to be at least 10 years old. The selection was slightly subjective as there were only a limited number of highly ranked journals of MIS research of that age. We therefore used:

 Decision Support Systems, DSS, from 1999 24(3&4) to 2008 46(1), 957 papers.

 Information & Management, IM, from 1999 36(1) to 2008 45 (8), 561 papers.

 Information Systems Research, ISR, from 1999 10(1) to 2008 19(4), 226 papers.

 Journal of Management Information Systems, JMIS, from 1999 15(4) to 2008 25(3), 368 papers.

 Management Information Systems Quarterly, MISQ, from 1999 23(1) to 2008 32(4), 257 papers.

Based on the publication information of these 2369 journal articles, six keyword networks were constructed: a combined one for all journals and five separate ones for each journal.

Generally, a keyword network has two features: (1) it is an undirected network (the links between nodes are symmetric) and (2) it is a weighted network (i.e., a link between two keywords is numbered – this shows how many times the two keywords appear in the network: this number shows the strength of the connection.

In our study, we focused on the topological characteristics of the keyword network and assigned a weight of one to each link.

Before the constructing the keyword network, the keywords had to be standardized because the keyword information was provided by the authors, and individual keywords can be expressed differently; e.g., in abbreviated or singular/plural form. Therefore, considerable time and effort had to be invested in editing the keywords.

The basic principle for the refinement of keywords was that all keywords with fundamentally the same meaning (representing the same idea) were changed to a standard form. The following list contains the rules used in the refinement of keywords, which are shown in capital letters:

 Standardization into a singular form: e.g., AGENT, AGENTS ! A-AGENT.

 Removing redundant keywords: when a keyword and its abbreviated form were used together, the abbreviated form was deleted; e.g., ADAPTIVE STRUCTURATION THEORY (AST) ! ADAPTIVE STRUCTURATION THEORY.

 Removing hyphens: hyphens that link two words were deleted if the meaning was not affected by this; e.g., CONSUMER-DECISION MAKING ! CONSUMER DECISION MAKING.

 Avoidance of abbreviations: when there were both the original word and abbreviated form(s) in the keyword list, they were consolidated into the original word; e.g., B2B, B2B E-COMMERCE, B2B ELECTRONIC COMMERCE, BUSINESS-TO-BUSINESS ELEC-TRONIC COMMERCE ! BUSINESS TO BUSINESS ELECTRONIC COMMERCE.

 Unification of synonyms: when two or more synonyms existed in the list, they were changed into the most general keyword; e.g., AHP, ANALYTIC HIERARCHICAL PROCESS, ANALYTIC HIERARCHY PROCESS, ANALYTICAL HIERARCHY PROCESS ! ANALYTIC HIER-ARCHY PROCESS.

 Separation of multiple terms in a keyword: in cases where two or more distinct terms were used for a keyword, they were separated and considered as individual keywords. e.g., EFFICIEN-CY AND EFFECTIVENESS ! EFFICIENCY, EFFECTIVENESS.

After this refinement, the resulting keyword database consisted of 6480 keywords.

In order to analyze the structure of the keyword network constructed from this database, we used UCINET software,<sup>1</sup> a network analysis tool that has been widely used to provide network-related measures in a rigorous but user-friendly way.

The network analysis consisted of two parts which analyzed:

 The characteristics of the keyword networks based on networklevel and node-level measures (network density, average distance or characteristic path length, and clustering coefficient) and the correlations between node-level measures (degree centrality, betweenness centrality, and clustering coefficient).

 The important keywords from the perspective of centrality in the keyword network and from the traditional perspective of frequency of use in publication.

Then the keywords were classified by measure and journal, and sorted by their importance.

## 4. The results of keyword network analysis

## 4.1. Network characteristics

As shown in Table 1, the total number of keywords during the 10- year period was 12,594 but after our refinement process the final set had reduced to 6480. Therefore, a published paper introduced, on average, 2.74(= 6480/2369) new keywords, while each paperhad 5.3 keywords on average; thus MIS research has spanned a broad range of issues and many new concepts. Papers published in IM and ISRhad relatively more keywords than the other three journals. In the whole network and sub-networks for each journal and time period, the clustering coefficients were very high while the network density was very low. This implied that research themes based on a set of closely related concepts or keywords were used for reasoning, theorizing, and communication.

Table 1  
The statistics on the whole network and the sub-networks by journal and time periods.

<table><tr><td></td><td>Papers</td><td>Keywords</td><td>Density</td><td>Distance</td><td>Clustering coefficient</td></tr><tr><td>ALL</td><td>2369</td><td>12,594</td><td>0.0014</td><td>3.650</td><td>0.856</td></tr><tr><td>DSS</td><td>957</td><td>4699</td><td>0.0024</td><td>3.719</td><td>0.891</td></tr><tr><td>IM</td><td>561</td><td>2922</td><td>0.0038</td><td>3.940</td><td>0.878</td></tr><tr><td>ISR</td><td>226</td><td>1337</td><td>0.0069</td><td>4.735</td><td>0.909</td></tr><tr><td>JMIS</td><td>368</td><td>2083</td><td>0.0051</td><td>4.180</td><td>0.885</td></tr><tr><td>MISQ</td><td>257</td><td>1553</td><td>0.0073</td><td>4.502</td><td>0.891</td></tr><tr><td>1999–2000</td><td>375</td><td>1906</td><td>0.0046</td><td>4.585</td><td>0.906</td></tr><tr><td>2001–2002</td><td>335</td><td>1753</td><td>0.0052</td><td>4.206</td><td>0.904</td></tr><tr><td>2003–2004</td><td>434</td><td>2330</td><td>0.0044</td><td>3.952</td><td>0.893</td></tr><tr><td>2005–2006</td><td>594</td><td>3213</td><td>0.0034</td><td>4.008</td><td>0.892</td></tr><tr><td>2007–2008</td><td>631</td><td>3392</td><td>0.0031</td><td>4.136</td><td>0.889</td></tr></table>

Among the structural characteristics of the keyword network, a most interesting result was that the cumulative degree distribution followed a clear power-law distribution (see Fig. 1, where the X-axis is the log scale of the degree, and the Y-axis is the proportion of the keywords whose degree is higher than the corresponding one in the X-axis. For example, a value of 16 on the X-axis corresponds to a value of 0.1, indicating that 10% of the keywords have more than 16 connections to other keywords).

Researchers have found power-law distributions in various kinds of networks resulting from intellectual activities, including citation networks, collaboration networks [12], and patent networks [21]. A well known mechanism of this pattern is the preferential attachment (rich-get-richer) mechanism, whereby a node with more links is likely to attain further new links in the evolution of the network. The presence of heavy-tailed scale-free distribution represents the fundamental signature of an emergent collective behavior of the actors who contribute to forming the network. In our context, the more popular a keyword becomes, the more often it is selected by researchers and the more it is associated with other keywords or concepts to constitute and convey new ideas. The evidence of power-law distribution implies that the preferential attachment mechanism suggests the origin of heavy-tailed distributions in a wide range of growing keyword networks.

Another notable feature is hierarchy, which has been long considered as an important structural feature in complex systems. Although studying the collective behavior of the elements of a network can shed light on the large-scale structure in which the network is self-organized, the presence of a power-law distribution does not necessarily imply a hierarchical structure. There have been several research efforts aimed at developing measures to characterize the relationship between scale-free topology and hierarchical structure, most of these have focused on the linear relationship between degree and the clustering coefficient [18,19].

![](/api/attachments/YMCGDP2A/fulltext/images/ba5eb6b01476dba2c40d2ee0cf5cc6f750b089a7c4efe1621326814ce1f01fa5.jpg)  
Fig. 1. Cumulative degree distribution of the whole keyword network.

![](/api/attachments/YMCGDP2A/fulltext/images/d0e410b7e6e59e6ae5a3172dfb8d715c24f4e307bd207615361be449e32f7626.jpg)  
Fig. 2. Correlation between average clustering coefficient and degree.

As shown in Fig. 2, the average clustering coefficient exhibits a heavy tail as a function of degree (k). This implies that keywords are associated with each other in a hierarchic fashion. The result is consistent with studies of other complex networks such as the Internet [22] which can be represented as highly clustered regional networks sparsely interconnected by hub nodes.

Based on the results, we can infer that keywords in a hub or central position in the keyword network are usually connected with many neighboring keywords as a result of preferential attachment process in the evolution of the network. This feature, however, does not necessarily imply that the keywords in a hub are linked to those in other hubs. Indeed, hub keywords have a large number of links, and only a few of them have connections to other hubs. This means that, whereas the small-degree keywords tend to be parts of highly cohesive and densely connected clusters, the hub keywords are not – their neighboring keywords are very sparsely linked. In other words, the hub keywords play a role of bridging distinct clusters of highly associated keywords into an integrated network.

To be more sophisticated, we employed a k-core analysis. Fig. 3(a) shows the correlation between the degree and the coreness of the keyword nodes. By definition, a node with the coreness of k has at least k degrees [4]. The color code in Fig. 3(b) visualizes relative importance of the keywords by color and position. The keywords in the inner shell (red) form the nucleus of the keyword network. Those with high coreness but being in the external shell correspond to local hubs. The degree-coreness correlation and the network structure vary across the journals. It is worth noting that the shell index and degree are highly correlated, implying a clear hierarchical structure. In other words, the degree of nodes increases when moving from the periphery of the network to its center.

In high-level shells of MISQ, however, the correlations between degree and coreness are less clear, with local hubs in the external shells. In addition, MISQ has the highest k-core of 15, although having the second smallest number of keywords of the five journals. This implies that the keywords are highly interconnected in the MISQ keyword network, which is confirmed by the fact that the network density is the highest among the five journals. Also the keywords in the external layer, especially in DSS and IM, tend to be linked with the keywords in a broad range of layers. On the other hand, the keywords in the central layer (i.e., at highest level of the hierarchy), are clustered in the same layer.

How would the importance of a node vary depending on the metrics used? Fig. 4 shows the correlation between the measures of keyword importance. This shows positive correlation between the frequency, degree, and normalized betweenness of the keywords (nBetweenness, is the normalized betweenness centrality computed as the betweenness divided by the maximum possible betweenness). This implies that the keywords that have received a great deal of attention from researchers also have structural importance in the keyword network. However, we also observed many outliers that do not follow a clear linearity, which suggests that structural measures, such as degree and betweenness, provide additional implications.

![](/api/attachments/YMCGDP2A/fulltext/images/ecb06ffbfc7ed64831fe8669cc417392f2d05829c06430ddc06a246e1860a266.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/1f9051d41b01e06ff1a9b6048492630c25592e24b3e840b7f818427e18399be3.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/8e35b5f77b630f04f6b7a7f8d7ded90d784ee656ccce9425b4467b00d26b7f79.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/f80ab81125c3e498b1fef3ebf9ec29306f65c0f72fb58945b572458f99cf2979.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/46d11dfa99e8a40a2f203062a9e415a9d777be93095e96ca91ae0922d8605a5a.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/1700fa93e4595fc9fba96e32e65eb5e3455611d8a6ae8af43bc37a55587bdc7e.jpg)  
Fig. 3. (a) Degree-coreness correlation for each journal, (b) Illustration of the k-core of the nodes in the keyword network for each journal; degree and coreness are shown by size and color, respectively.

![](/api/attachments/YMCGDP2A/fulltext/images/063aeb1f94069f5e60b4781181c0425e2c45ff39fd408c56981a723bbe612500.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/77238b0b5d3e19e33f0c98174a5de2d39ffd22a64d2c8e1e6e2be7825b88ede0.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/65473583c519f47761e6ef20014c78869f9b7a88780f935a417e5da44eaacab5.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/7f80c0c504ff3242771bd878935aa2fad35549767598ae5a2c22543a4c64714e.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/7cd0412b0206548b4627b381a8c6436ddd391feea3eb08a064ce2eed305b664b.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/31ad75446997c880cc34fa9a2f8a01ea51936a027fbb98e31d27a5f116fcb5f0.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/9ef59d533aa30234a5697f9f673e3cffcc6d6f6c51fbe3c2ca73244131a7daee.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/0bdeb7b364b41a7117816e41309d23c1acba5dad3b58c433fb2473de3806a54f.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/2d634d71fcc11835caa4f45b883d0957169447b9ed93d100ac82827fb3e3b47d.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/5f1d3b033a6bda2656318a9af8284cdcbea187982f6e7cc66316a0a8ced39a0e.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/f70fb63272deb8de1e5d7948105c82577fac0b90949a878bb0503b4087e2acc6.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/65d6b81d9107bba689279cc6d91d5fd496a29495d178585fd6166246c0b6736b.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/17fae55e25aa3c148a57ba47c1073fe2b24ee9254bae6fbb0fa01371f3383ab4.jpg)

![](/api/attachments/YMCGDP2A/fulltext/images/c13d6fff9607d17bb604ca78141d6d2d9ad9f55aae35e4fc8b7434b87fdb308d.jpg)  
Fig. 4. Correlation between frequency, degree, and betweenness

![](/api/attachments/YMCGDP2A/fulltext/images/ca1e05da908b647fc1fe6635a71760fd2dd0b356cf4a8b7bfb3829945b9219f0.jpg)

Another notable feature of the keyword network is the strong degree-betweenness correlation. In most natural or artificial networks, a significant difference exists between degree centrality and betweenness centrality. This is easily explained by the distinctive nature of these two measures and is the reason why they are used separately. The strong correlation between them two, therefore, is an unusual characteristic of the keyword network of MIS. Maybe the sparseness of the keyword network and a very low redundancy with respect to node connectivity is the reason.

## 4.2. Important keywords

The deviation from the average linear correlation in Fig. 4 shows that the three measures of frequency, degree, and nBetweenness have their own roles in explaining the importance of a keyword. The extent of the dispersion varies across the journals. DSS shows the strongest linear correlation, while MISQ shows high dispersion around the linear average correlation. This difference implies that there is a difference in the set of important keywords by the three measures. To determine the important keywords and how they differ across journals and measures, we chose the top 20 keywords for each measure and compared them (see Table 2). For each journal, the top 20 keywords for each measure were classified into corresponding columns, and the common keywords in the three top 20 lists were moved to the last column (Common). For example,

Table 2 Important keywords in MIS research from 1999 to 2008.

<table><tr><td colspan="2"></td><td>Degree</td><td>nBetweenness</td><td>Common</td></tr><tr><td rowspan="2">DSS</td><td>EXPERT SYSTEM</td><td>EXPERT SYSTEM</td><td>CUSTOMER RELATIONSHIP MANAGEMENT</td><td>DECISION SUPPORT SYSTEM</td></tr><tr><td>INTELLIGENT AGENT MULTICRITERIA ANALYSIS</td><td>WEB SERVICE WORLD WIDE WEB</td><td>ANALYTIC HIERARCHY PROCESS INFORMATION TECHNOLOGY</td><td>ELECTRONIC COMMERCE KNOWLEDGE MANAGEMENT DATA MINING GROUP DECISION SUPPORT SYSTEM ONLINE ANALYTIC PROCESSING DATA WAREHOUSE INFORMATION RETRIEVAL DECISION MAKING GENETIC ALGORITHM NEURAL NETWORKS DECISION SUPPORT SIMULATION ELECTRONIC MARKET INTERNET MULTI AGENT SYSTEM CLUSTERING</td></tr><tr><td rowspan="2">IM</td><td>ENTERPRISE RESOURCE PLANNING WORLD WIDE WEB</td><td rowspan="2">OUTSOURCING ENTERPRISE RESOURCE PLANNING COMPETITIVE ADVANTAGE</td><td rowspan="2">OUTSOURCING INFORMATION SYSTEM IMPLEMENTATION WORLD WIDE WEB</td><td rowspan="2">TECHNOLOGY ACCEPTANCE MODEL ELECTRONIC COMMERCE INFORMATION TECHNOLOGY KNOWLEDGE MANAGEMENT INTERNET ELECTRONIC RESOURCE PLANNING GROUP DECISION SUPPORT SYSTEM DECISION SUPPORT SYSTEM TRUST INFORMATION SYSTEM PROJECT MANAGEMENT INFORMATION SYSTEM DEVELOPMENT TECHNOLOGY ADOPTION DATA MINING USER SATISFACTION BUSINESS PROCESS REENGINEERING CASE STUDY</td></tr><tr><td>INFORMATION SYSTEM IMPLEMENTATION</td></tr><tr><td>ISR</td><td>LABORATORY EXPERIMENT ELECTRONIC MARKET STRUCTURAL EQUATION MODELING ELECTRONIC DATA INTERCHANGE</td><td>LABORATORY EXPERIMENT FEEDBACK STRUCTURAL EQUATION MODELING NETWORK EXTERNALITY SOCIAL NETWORKS ELECTRONIC MARKET ONTOLOGY NETWORK ECONOMICS</td><td>NETWORK EXTERNALITY DATA WAREHOUSE DATA MODEL INFORMATION SYSTEMS MANAGEMENT NETWORK ECONOMICS KNOWLEDGE SHARING ONTOLOGY MEASURE</td><td>ELECTRONIC COMMERCE COMPUTER-MEDIATED COMMUNICATION TRUST INFORMATION TECHNOLOGY INFORMATION TECHNOLOGY INVESTMENT VIRTUAL TEAM AUCTION ELECTRONIC BUSINESS HUMAN COMPUTER INTERACTION TECHNOLOGY ACCEPTANCE MODEL TECHNOLOGY ADOPTION DECISION MAKING</td></tr></table>

Table 2 (Continued )

<table><tr><td colspan="2"></td><td>Degree</td><td>nBetweenness</td><td>Common</td></tr><tr><td rowspan="5">JMIS</td><td rowspan="2">COMPUTER-MEDIATEDCOMMUNICATIONBUSINESS VALUEBUSINESS PROCESS REENGINEERING</td><td rowspan="2">COMPUTER-MEDIATEDCOMMUNICATIONVISUALIZATIONSOCIAL NETWORKS</td><td>SUPPLY CHAIN</td><td>ELECTRONIC COMMERCE</td></tr><tr><td>SOCIAL NETWORKSBUSINESS PROCESSREENGINEERING</td><td>GROUP DECISION SUPPORT SYSTEMKNOWLEDGE MANAGEMENT</td></tr><tr><td>INFORMATION TECHNOLOGYCOLLABORATIONECONOMIC ANALYSIS</td><td>BUSINESS VALUEPRICINGINFORMATION SYSTEMDEVELOPMENT</td><td>VISUALIZATIONTACIT KNOWLEDGESURVEY</td><td>TRUSTINFORMATION TECHNOLOGY INVESTMENTELECTRONIC MARKET</td></tr><tr><td rowspan="2">INFORMATION TECHNOLOGYINFRASTRUCTURE</td><td rowspan="2">INFORMATION TECHNOLOGY</td><td rowspan="2">BUSINESS VALUE OFINFORMATION TECHNOLOGY</td><td>INFORMATION SYSTEM DEVELOPMENT</td></tr><tr><td>INFORMATION GOODSVIRTUAL TEAMDATA MININGTECHNOLOGY ADOPTIONCASE STUDYINTERORGANIZATIONAL SYSTEM</td></tr><tr><td rowspan="6">MISQ</td><td>TECHNOLOGY ADOPTION</td><td>INFORMATION SYSTEMSMANAGEMENT</td><td>VIRTUAL TEAM</td><td>INFORMATION SYSTEM DEVELOPMENT</td></tr><tr><td>INFORMATION SYSTEMSIMPLEMENTATION</td><td>INTERNET</td><td>DESIGN SCIENCE</td><td>TECHNOLOGY ACCEPTANCE MODEL</td></tr><tr><td>OFFSHORINGVIRTUAL TEAMOUTSOURCING</td><td>POWEROUTSOURCINGTECHNOLOGY ADOPTION</td><td>GENDERQUALITATIVE ANALYSISCOMPUTER-MEDIATEDCOMMUNICATION</td><td>ADOPTIONKNOWLEDGE MANAGEMENTTRUST</td></tr><tr><td>QUALITATIVE ANALYSIS</td><td>ORGANIZATIONAL CHANGE</td><td>STRATEGIC INFORMATIONSYSTEM</td><td>ELECTRONIC COMMERCE</td></tr><tr><td>DESIGN SCIENCEELECTRONIC MARKET</td><td>INFORMATION SYSTEM USESTRATEGIC INFORMATION SYSTEM</td><td>POWERDISTANCE</td><td>INFORMATION SYSTEM MANAGEMENTTECHNOLOGY ADOPTION</td></tr><tr><td>INFORMATION SYSTEM USE</td><td>IMPLEMENTATION</td><td>CREATIVITY</td><td>GROUP DECISION SUPPORT SYSTEMINFORMATION SYSTEMORGANIZATIONAL LEARNINGCASE STUDY</td></tr></table>

the first row corresponds to DSS, and 17 keywords are common in the top 20 lists of the three measures. They are placed in the last column, and the other important keywords remain in the three columns corresponding to each measure. The underlined keyword in each column means it is ranked in the top 20 only by the corresponding measure. For example, in DSS, MULTICRITERIA ANALYSIS and INTELLIGENT AGENT were in the top 20 list by frequency, and thus they were very popular keywords used in many papers. However, they were not in the top 20 lists by degree and betweenness centrality and thus their importance was rather low in terms of their structural position in the keyword network. On the other hand, WEB SERVICE and WORLD WIDE WEB were keywords that had high structural importance in the keyword network and were only captured by degree centrality. In that sense, we see that CUSTOMER RELATIONSHIP MANAGEMENT and ANALYTIC HIERAR-CHY PROCESS play an important role in bridging separated keyword groups or research themes, while they do not have many connections with other keywords and are not popular ones. In the Common column, those in bold-italic keywords are unique across the five journals. In the DSS journal row, for example, DECISION SUPPORT SYSTEM, ELECTRONIC COMMERCE, and KNOWLEDGE MANAGEMENT commonly in the top 20 lists by the three measures for all journals. In contrast, ONLINE ANALYTIC PROCESSING, DATA WAREHOUSE, and INFORMATION RETRIEVAL do not appear in the common-keyword lists in the other four journal rows.

We can observe differences in the classification of the top 20 keywords across measures and journals. As shown in Fig. 4, the difference in the top-ranked keywords according to the three measures, which is inversely proportional to the number of common keywords in the last column, is larger in ISR, JMIS, and MISQ than in DSS and IM. This implies that, in DSS and IM, the popular keywords that researchers choose also have many connections with other keywords, and the keywords also play a bridging role. This characteristic is consistent with the high correlation or small dispersion in the graphs of DSS and IM in Fig. 4. The structures of the keyword networks for DSS and IM can therefore be thought of as consistently increasing shapes, and there are few distinctive keywords that have high centrality with low frequency. On the other hand, redundancy in frequency, degree, and nBetweenness is relatively low in the keyword networks of ISR, JMIS, and MISQ, which implies that a number of distinctive keywords with low frequency but high centrality exist in these networks. Among the three, ISR has the largest number of important bridging keywords in the nBetweenness column that are not recognized by the other measures; this shows that ISR has contributed to MIS research by introducing interdisciplinary keywords that bridge research themes that are not likely to be identified from the popularity perspective. The important keywords of ISR in terms of nBetweenness are DATA WAREHOUSE, DATA MODEL, INFORMATION SYSTEMS MANAGE-MENT, KNOWLEDGE SHARING, and MEASURE. JMIS shows an outstanding contribution that can be recognized only by this kind of comparative analysis. It has few unique keywords in the Common column. This means the important keywords in JMIS that are common for the three are also important to other journals. Thus JMIS has maintained a balanced and general stance when introducing new research themes. In contrast, DSS has the largest number of unique keywords, indicating their important position in technical research. The distinctive keywords in DSS are usually related to IS or IS processing. such as ONLINE ANALYTIC PROCESSING. DATA WAREHOUSE, INFORMATION RETRIEVAL, GENETIC ALGORITHM, and NEURAL NETWORKS.

The contribution of MISQ apparently is associated with an organization-wide and managerial view when considering the role of IS. In the important keywords in its Common column, we find the keywords INFORMATION SYSTEM DEVELOPMENT, TECHNOLOGY ACCEPTANCE MODEL, ADOPTION, and KNOWLEDGE MANAGE-MENT, as well as TRUST. The Degree column also has keywords such as OUTSOURCING, ORGANIZATIONAL CHANGE, and INFOR-MATION SYSTEM USE, which have many connections with other research areas.

Table 3  
Top 20 keywords in MIS research by three measures (1999–2008 vs. 2007–2008).

<table><tr><td rowspan="2">Rank</td><td colspan="4">Frequency</td></tr><tr><td>1999–2008</td><td>Frequency</td><td>2007–2008</td><td>Frequency</td></tr><tr><td>1</td><td>ELECTRONIC COMMERCE</td><td>160</td><td>DECISION SUPPORT SYSTEM</td><td>43</td></tr><tr><td>2</td><td>DECISION SUPPORT SYSTEM</td><td>148</td><td>ELECTRONIC COMMERCE</td><td>31</td></tr><tr><td>3</td><td>KNOWLEDGE MANAGEMENT</td><td>101</td><td>KNOWLEDGE MANAGEMENT</td><td>26</td></tr><tr><td>4</td><td>GROUP DECISION SUPPORT SYSTEM</td><td>85</td><td>TRUST</td><td>21</td></tr><tr><td>5</td><td>TECHNOLOGY ACCEPTANCE MODEL</td><td>69</td><td>TECHNOLOGY ADOPTION</td><td>15</td></tr><tr><td>6</td><td>DATA MINING</td><td>67</td><td>DATA MINING</td><td>13</td></tr><tr><td>7</td><td>TRUST</td><td>60</td><td>VIRTUAL TEAM</td><td>12</td></tr><tr><td>8</td><td>INFORMATION TECHNOLOGY</td><td>49</td><td>ONLINE ANALYTIC PROCESSING</td><td>11</td></tr><tr><td>9</td><td>INTERNET</td><td>47</td><td>DECISION SUPPORT</td><td>11</td></tr><tr><td>10</td><td>ELECTRONIC MARKET</td><td>45</td><td>MULTICRITERIA ANALYSIS</td><td>11</td></tr><tr><td>11</td><td>TECHNOLOGY ADOPTION</td><td>44</td><td>OUTSOURCING</td><td>11</td></tr><tr><td>12</td><td>INFORMATION SYSTEM DEVELOPMENT</td><td>42</td><td>COMPUTER-MEDIATED COMMUNICATION</td><td>11</td></tr><tr><td>13</td><td>DECISION MAKING</td><td>39</td><td>TECHNOLOGY ACCEPTANCE MODEL</td><td>11</td></tr><tr><td>14</td><td>INFORMATION TECHNOLOGY INVESTMENT</td><td>37</td><td>OFFSHORING</td><td>11</td></tr><tr><td>15</td><td>CASE STUDY</td><td>36</td><td>DECISION MAKING</td><td>10</td></tr><tr><td>16</td><td>DECISION SUPPORT</td><td>36</td><td>ELECTRONIC MARKET</td><td>10</td></tr><tr><td>17</td><td>DATA WAREHOUSE</td><td>34</td><td>ENTERPRISE RESOURCE PLANNING</td><td>10</td></tr><tr><td>18</td><td>INFORMATION SYSTEM</td><td>34</td><td>SIMULATION</td><td>9</td></tr><tr><td>19</td><td>ENTERPRISE RESOURCE PLANNING</td><td>34</td><td>DATA WAREHOUSE</td><td>9</td></tr><tr><td>20</td><td>ELECTRONIC DATA INTERCHANGE</td><td>33</td><td>MULTI AGENT SYSTEM</td><td>9</td></tr></table>

<table><tr><td rowspan="2">Rank</td><td colspan="4">Degree</td></tr><tr><td>1999–2008</td><td>Degree</td><td>2007–2008</td><td>Degree</td></tr><tr><td>1</td><td>ELECTRONIC COMMERCE</td><td>608</td><td>DECISION SUPPORT SYSTEM</td><td>161</td></tr><tr><td>2</td><td>DECISION SUPPORT SYSTEM</td><td>503</td><td>ELECTRONIC COMMERCE</td><td>154</td></tr><tr><td>3</td><td>KNOWLEDGE MANAGEMENT</td><td>338</td><td>TRUST</td><td>103</td></tr><tr><td>4</td><td>GROUP DECISION SUPPORT SYSTEM</td><td>279</td><td>KNOWLEDGE MANAGEMENT</td><td>98</td></tr><tr><td>5</td><td>TRUST</td><td>256</td><td>TECHNOLOGY ADOPTION</td><td>64</td></tr><tr><td>6</td><td>TECHNOLOGY ACCEPTANCE MODEL</td><td>227</td><td>VIRTUAL TEAM</td><td>60</td></tr><tr><td>7</td><td>DATA MINING</td><td>221</td><td>OUTSOURCING</td><td>59</td></tr><tr><td>8</td><td>INFORMATION TECHNOLOGY</td><td>211</td><td>DECISION MAKING</td><td>56</td></tr><tr><td>9</td><td>INTERNET</td><td>207</td><td>OFFSHORING</td><td>55</td></tr><tr><td>10</td><td>TECHNOLOGY ADOPTION</td><td>177</td><td>SOCIAL NETWORKS</td><td>54</td></tr><tr><td>11</td><td>ELECTRONIC MARKET</td><td>174</td><td>DATA MINING</td><td>53</td></tr><tr><td>12</td><td>DECISION MAKING</td><td>160</td><td>CASE STUDY</td><td>51</td></tr><tr><td>13</td><td>INFORMATION SYSTEM DEVELOPMENT</td><td>156</td><td>COMPUTER-MEDIATED COMMUNICATION</td><td>50</td></tr><tr><td>14</td><td>CASE STUDY</td><td>156</td><td>DECISION SUPPORT</td><td>48</td></tr><tr><td>15</td><td>INFORMATION SYSTEM</td><td>150</td><td>TECHNOLOGY ACCEPTANCE MODEL</td><td>48</td></tr><tr><td>16</td><td>INFORMATION TECHNOLOGY INVESTMENT</td><td>147</td><td>UNCERTAINTY</td><td>44</td></tr><tr><td>17</td><td>COMPUTER-MEDIATED COMMUNICATION</td><td>134</td><td>ENTERPRISE RESOURCE PLANNING</td><td>44</td></tr><tr><td>18</td><td>DECISION SUPPORT</td><td>132</td><td>KNOWLEDGE TRANSFER</td><td>43</td></tr><tr><td>19</td><td>SIMULATION</td><td>130</td><td>INFORMATION TECHNOLOGY INVESTMENT</td><td>43</td></tr><tr><td>20</td><td>VIRTUAL TEAM</td><td>130</td><td>ONLINE ANALYTIC PROCESSING</td><td>40</td></tr></table>

<table><tr><td></td><td>1999–2008</td><td>nBetweenness</td><td>2007–2008</td><td>nBetweenness</td></tr><tr><td>1</td><td>ELECTRONIC COMMERCE</td><td>0.159</td><td>DECISION SUPPORT SYSTEM</td><td>0.141</td></tr><tr><td>2</td><td>DECISION SUPPORT SYSTEM</td><td>0.132</td><td>ELECTRONIC COMMERCE</td><td>0.131</td></tr><tr><td>3</td><td>KNOWLEDGE MANAGEMENT</td><td>0.081</td><td>KNOWLEDGE MANAGEMENT</td><td>0.085</td></tr><tr><td>4</td><td>GROUP DECISION SUPPORT SYSTEM</td><td>0.056</td><td>TRUST</td><td>0.085</td></tr><tr><td>5</td><td>DATA MINING</td><td>0.044</td><td>VIRTUAL TEAM</td><td>0.040</td></tr><tr><td>6</td><td>INFORMATION TECHNOLOGY</td><td>0.041</td><td>CASE STUDY</td><td>0.039</td></tr><tr><td>7</td><td>TRUST</td><td>0.038</td><td>TECHNOLOGY ADOPTION</td><td>0.037</td></tr><tr><td>8</td><td>INTERNET</td><td>0.032</td><td>DATA MINING</td><td>0.035</td></tr><tr><td>9</td><td>TECHNOLOGY ACCEPTANCE MODEL</td><td>0.030</td><td>OFFSHORING</td><td>0.034</td></tr><tr><td>10</td><td>DECISION MAKING</td><td>0.026</td><td>DECISION MAKING</td><td>0.031</td></tr><tr><td>11</td><td>ELECTRONIC MARKET</td><td>0.025</td><td>DECISION SUPPORT</td><td>0.030</td></tr><tr><td>12</td><td>TECHNOLOGY ADOPTION</td><td>0.024</td><td>ENTERPRISE RESOURCE PLANNING</td><td>0.029</td></tr><tr><td>13</td><td>INFORMATION SYSTEM</td><td>0.024</td><td>TECHNOLOGY ACCEPTANCE MODEL</td><td>0.029</td></tr><tr><td>14</td><td>CASE STUDY</td><td>0.023</td><td>COLLABORATION</td><td>0.027</td></tr><tr><td>15</td><td>INFORMATION SYSTEM DEVELOPMENT</td><td>0.021</td><td>OUTSOURCING</td><td>0.026</td></tr><tr><td>16</td><td>DECISION SUPPORT</td><td>0.021</td><td>SOCIAL NETWORKS</td><td>0.026</td></tr><tr><td>17</td><td>INFORMATION TECHNOLOGY INVESTMENT</td><td>0.019</td><td>COMPUTER-MEDIATED COMMUNICATION</td><td>0.025</td></tr><tr><td>18</td><td>SIMULATION</td><td>0.019</td><td>UNCERTAINTY</td><td>0.024</td></tr><tr><td>19</td><td>INFORMATION RETRIEVAL</td><td>0.018</td><td>SATISFACTION</td><td>0.024</td></tr><tr><td>20</td><td>OUTSOURCING</td><td>0.018</td><td>ONLINE ANALYTIC PROCESSING</td><td>0.023</td></tr></table>

## 4.3. Changes in important keywords over time

How have the important keywords changed over time and what are the recent important keywords? To address these questions, we compared the important keywords in the keyword network constructed from the 10 years of data (1999–2008) with those from recent data covering the two years (2007 and 2008). We compared the top 20 keywords across the three importance measures for all five journals (see Table 3). The connections between keywords accumulate over time, producing an inherent difficulty in the analysis of the evolution of keyword networks. That is, the keyword network constructed for a certain time period provides information about the relationships among the keywords only for the papers published in that period, and thus excludes information about the relationships among the keywords in other periods. The relationships between keywords across different time periods should be affected by each other and thus correlated. This is a common issue in the investigation of the evolution of citation, author, or keyword networks. Comparing the keyword network over a long time period with that from recent years should mitigate the potential loss of the information about recent changes in important keywords.

This comparison reveals some notable results. ELECTRONIC COMMERCE, DECISION SUPPORT SYSTEM, and KNOWLEDGE MANAGEMENT were the three most important keywords by the three measures for both time periods, and they have received consistent and high attention over the last decade. Decision support-related keywords (DECISION MAKING, DECISION SUP-PORT SYSTEM, DECISION SUPPORT, etc.) have also received growing attention over the 10 years, as system user-related keywords (TECHNOLOGY ACCEPTANCE MODEL, TRUST, TECHNOL-OGY ADOPTION, etc.) and knowledge management-related keywords (KNOWLEDGE MANAGEMENT and KNOWLEDGE TRANSFER). In particular, the importance of knowledge management-related keywords has been substantially increased, as shown in our supplementary analysis. OUTSOURCING and OFFSHORING have been selected as important research keywords by many researchers in the recent two years. However, system-related keywords (INFORMATION TECHNOLOGY, INFORMATION SYSTEM, and INFORMATION SYSTEM DEVELOPMENT) have received less research interest. INTERNET lost most interests for all measures.

Comparing with the top 20 keywords, the analysis by degree and nBetweenness provided interesting findings. SOCIAL NET-WORKS became an important keyword in terms of degree and nBetweenness for 2007–2008, while KNOWLEDGE TRANSFER and ONLINE ANALYTIC PROCESSING experienced growing importance from the degree perspective. However, system-related keywords (e.g., DATA WAREHOUSE and MULTI AGENT SYSTEM) were excluded from the top 20 lists by the two measures, though COLLABORATION and SATISFACTION became important keywords in terms of nBetweenness for the period of 2007–2008, which means that they have played an important role in bridging other research themes.

## 5. Discussion and concluding remarks

In our study, we examined the structure of the keyword networks of MIS research and observed five interesting results:

(1) The keyword network of MIS research is very sparse with a long average distance. It is possible that this field has changed fast, introducing many new topics and concepts. However, the keyword network of MIS research is highly clustered and shows a clear power-law degree distribution. This suggests that there are local clusters of more densely connected keywords that are associated with research themes led by groups of researchers (such as a university department and its faculty).

(2) The MIS keyword networks share a number of common features with other intellectual networks [17]. However, the tail of the power-law distribution of the keyword networks is remarkably clearer than citation/collaboration networks, which is a unique feature of keyword networks.

(3) The keyword network is organized in a hierarchical structure – as this has been considered to be an important feature of many complex networks and evolving systems, this should provide meaningful implications for this stream of research – especially, for inquiry into correlation between the structure of our collective knowledge and the structure of our world.

(4) The popularity-based measure (frequency) and centralitybased measures (degree, betweenness) are positively correlated in the keyword network. The correlation may be due to MIS researchers having pursued new topics and concepts. The positive degree-betweenness correlation could be a unique feature of MIS keyword networks, implying that popular keywords in MIS research are those that also bridge distant clusters of related concepts and ideas. Thus it is an interdisciplinary research area.

(5) The extent of the positive correlations among the frequency, degree and betweenness of the keywords significantly varies across the five journals. This means that they are differentiated.

Our research method can be applied to a broader scope of scientific fields, rather than to a single one. The comparative and integrative analysis of the keyword networks from interrelated scientific areas could contribute to our understanding of the organization and the evolution of knowledge.

## Acknowledgements

Authors appreciate valuable comments and commitments made by reviewers and editor to improve the quality of this paper. This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea Government (MEST) (No. 2009-0070359).

## References

[1] J.I. Alvarez-Hamelin, L. Dall’Asta, A. Barrat, A. Vespignani, K-core decomposition: a tool for the visualization of large scale networks, Advances in Neural Information Processing Systems 18 (41), 2006.

[2] A. Baraba´ si, Scale-free networks: a decade beyond, Science 325 (5939), 2009, pp. 412–413.

[3] K.W. Boyack, K. Bo¨rner, Indicator-assisted evaluation and funding of research: visualizing the influence of grants on the number and citation counts of research papers, Journal of the American Society for Information Science and Technology 54 (5), 2003, pp. 447–461.

[4] G. Caldarella. A. Vespignani. Large scale structure and dynamics of complex networks, World Scientific 2007, p. 176.

[5] C. Chen, T. Cribbin, R. Macredie, S. Morar, Visualizing and tracking the growth of competing paradigms: two case studies, Journal of the American Society for Information Science and Technology 53 (8), 2002, pp. 678–689.

[6] W.S. Chow, L.S. Chan, Social network, social trust and shared goals in organiza tional knowledge sharing, Information and Management 45 (7), 2008, pp. 458– 465.

[7] R. Cross, L. Sproull, More than an answer: information relationships for actionable knowledge, Organization Science 15 (4), 2004, pp. 446–462.

[8] G. Dosi, M. Faillo, L. Marengo, Organizational capabilities, patterns of knowledge accumulation and governance structures in business firms: an introduction Organization Studies 29 (8–9), 2008, pp. 1165–1185.

[9] C.P. Huang, Bibliometric analysis of obstructive sleep apnea research trends, Journal of the Chinese Medical Association 72 (3), 2009, pp. 117– 123.

[10] M. Meyer, I. Lorscheid, K.G. Troitzsch, The development of social simulation as reflected in the first ten years of JASSS: a citation and co-citation analysis, Journal of Artificial Societies and Social Simulation 12 (4), 2009.

[11] P.A. Mischen, S.K. Jackson, Connecting the dots: applying complexity theory, knowledge management and social network analysis to policy implementation, Public Administration Quarterly 32 (3), 2008.

[12] S.P. Nerur, A.A. Rasheed, V. Natarajan, The intellectual structure of the strategic management field: an author co-citation analysis, Strategic Management Journal 29 (3), 2008, pp. 319–336.

[13] M. Li, J. Wu, D. Wang, T. Zhou, Z. Di, Y. Fan, Evolving model of weighted networks inspired by scientific collaboration networks, Physica A: Statistical Mechanics and its Applications 375 (1), 2007, pp. 355–364.

[14] W. Oh, J. Choi, K. Kim, Coauthorship dynamics and knowledge capital: the patterns of cross-disciplinary collaboration in information systems research Journal of Management Information Systems 22, 2006, pp. 266–292.

[15] T.J. Ord, E.P. Martins, S. Thakur, K.K. Mane, K. Bo¨rner, Trends in animal behaviour research (1968–2002): ethoinformatics and the mining of library databases, Animal Behaviour 69 (6), 2005, pp. 1399–1413.

[16] P.C. Palvia, S.C. Jain Palvia, J.E. Whitworth, Global information technology: a meta analysis of key issues, Information and Management 39 (5), 2002, pp. 403–414.

[17] J.J. Ramasco, S.N. Dorogovtsev, R. Pastor-Satorras, Self-organization of collaboration networks, Physical Review E 70, 2004, p. 036106

[18] E. Ravaz, A.L. Barabasi, Hierarchical organization in complex networks, Physica Review E 67, 2003, p. 026112

[19] H. Tangmunarunkit, R. Govindan, S. Jamin, S. Shenker, W. Willinger, Network topologies, power laws, and hierarchy, ACM SIGCOMM Computer Communication Review 32 (1), 2002, p. 76.

[20] S. Valverde, R. Cancho, R. Sole, Scale-free networks from optimal design, Europhysics Letters 60, 2002, pp. 512–517.

[21] S. Valverde, R.V. Sole, M.A. Bedau, N. Packard, Topology and evolution of technology innovation networks, Physical Review E 76, 2007, p. 056118.

[22] A. Vazquez, R. Pastor-Satorras, A. Vespignani, Large-scale topological and dynam ical properties of internet, Physical Review E 65, 2002, p. 066130.

[23] E.A. Whitley, R.D. Galliers, An alternative perspective on citation classics: evidence from the first 10 years of the European Conference on Information Systems, Information and Management 44 (5), 2007, pp. 441–455.

[24] B. Yoon, Y. Park, A systematic approach for identifying technology opportunities: keyword-based morphology analysis, Technological Forecasting and Socia Change 72 (2), 2005, pp. 145–160.

![](/api/attachments/YMCGDP2A/fulltext/images/05644aa58c134a6c738ef15babd57844bbfc84f64392723b53a1fec6a8a21755.jpg)

Jinho Choi is an assistant professor School of Busines at Sejong University. He received his master and PhD degree from the Korea Advanced Institute of Science and Technology (KAIST). Prior to joining Sejong University, he worked for Entrue Consulting Partners, LG CNS as a business/IT consultant and worked for International Center for Electronic Commerce (ICEC) and Human Computers as a researcher. His research works has appeared in several international journals including OMEGA, JCIS, JASSS, and ESWA. His research interests are knowledge evolution and knowledge management, management of technology, data mining application, and supply chain optimization.

![](/api/attachments/YMCGDP2A/fulltext/images/158802bf5516dd1b0b718114041a971ff1bab5e2620d5913bff71e57d344909c.jpg)

Sangyoon Yi is a research and teaching fellow at the department of marketing and management, University of Southern Denmark. He got his master’s degree in electronic engineering and PhD degree in management from the Korea Advanced Institute of Science and Technology (KAIST). His research focuses on understanding knowledge and learning as critical sources of innovation and competitive advantage. His published papers appear in academic journals including Strategic Management Journal.

![](/api/attachments/YMCGDP2A/fulltext/images/7ed98f1b8557eb1f68cf90bea2f96a4fee21647afdfa02fc0d1e304164061dbf.jpg)

Kun Chang Lee is a professor in the SKK Business School and WCU professor in the Department of Interaction Science at Sungkyunkwan University, Seoul, Korea. His recent research interests include creativity science and context-modeling. Regarding the creativity science, he investigates the creativity revelation process at individual-team-organization level in modern firms, and its influence on corporate performance. For the context modeling, he develops a new breed of context prediction mechanism where user’s behavior is predicted and a proper ubiquitous service is provided to them in ubiquitous contexts.
