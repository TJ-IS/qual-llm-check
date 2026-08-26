---
otero_id: 25052
otero_key: "SQEQZNNW"
title: "Verifying the Proximity and Size Hypothesis for Self-Organizing Maps"
authors: "Chienting Lin; Hsinchun Chen; Jay F. Nunamaker"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518256"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Verifying the Proximity and Size Hypothesis for Self-Organizing Maps

Chienting Lin, Hsinchun Chen & Jay F. Nunamaker

To cite this article: Chienting Lin, Hsinchun Chen & Jay F. Nunamaker (1999) Verifying the Proximity and Size Hypothesis for Self-Organizing Maps, Journal of Management Information Systems, 16:3, 57-70, DOI: 10.1080/07421222.1999.11518256

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518256

![](/api/attachments/SQEQZNNW/fulltext/images/b146acfcf5b7093158bdcc317fa3bb8bc2f1720a0123e39050eafdf02f573508.jpg)

Published online: 02 Dec 2015.

![](/api/attachments/SQEQZNNW/fulltext/images/f5c50d906399f80e2b51566841f4031cb35166bea324030ac466ed6630d911f6.jpg)

Submit your article to this journal ↗

![](/api/attachments/SQEQZNNW/fulltext/images/c08f4b8c8f1c49f8926808da79ada8ae72976836a35bb2b74adb16746e296b6c.jpg)

Article views: 1

![](/api/attachments/SQEQZNNW/fulltext/images/ff31eeac3cea6685b1080d42ff104bc3e1b1856ab807b0a74ae5b41e8f8dab11.jpg)

View related articles ↗

# Verifying the Proximity and Size Hypothesis for Self-Organizing Maps

CHIENTING LIN, HSINCHUN CHEN, AND JAY F. NUNAMAKER

CHIENTING LIN is a doctoral student in management information systems at the University of Arizona, where he also received his master's degree in 1995. His work has focused on knowledge management systems and enterprise resource planning applications. His work has appeared in IEEE Transactions on Pattern Analysis and Machine Intelligence and been presented at the International World Wide Web Conference and the Hawaii International Conference on System Sciences (HICSS). He is a member of the ACM and IEEE Computer Society.

HSINCHUN CHEN is McClelland Professor of MIS and Director of the Artificial Intelligence Lab at the University of Arizona, Tucson. He has published more than seventy articles covering semantic retrieval, search algorithms, knowledge discovery, and collaborative computing in publications such as Communications of the ACM, IEEE Computer, Journal of the American Society for Information Science, IEEE Expert, and Advances in Computers. He received the Ph.D. degree in information systems from New York University in 1989.

JAY F. NUNAMAKER, JR. Please see the Guest Editors' Introduction for biographical information.

ABSTRACT: The Kohonen Self-Organizing Map (SOM) is an unsupervised learning technique for summarizing high-dimensional data so that similar inputs are, in general, mapped close to one another. When applied to textual data, SOM has been shown to be able to group together related concepts in a data collection and to present major topics within the collection with larger regions. This article presents research in which we sought to validate these properties of SOM, called the Proximity and Size Hypotheses, through a user evaluation study. Building upon our previous research in automatic concept generation and classification, we demonstrated that the Kohonen SOM was able to perform concept clustering effectively, based on its concept precision and recall7 scores as judged by human experts. We also demonstrated a positive relationship between the size of an SOM region and the number of documents contained in the region. We believe this research has established the Kohonen SOM algorithm as an intuitively appealing and promising neural-network-based textual classification technique for addressing part of the longstanding “information overload” problem.

KEY WORDS AND PHRASES: document clustering techniques, experimental research, group support systems, self-organizing maps, unsupervised learning algorithms.

WITH THE SUDDEN EMERGENCE AND PROLIFERATION OF INTERNET SERVICES, the information overload problem has become more pressing than ever. Researchers in the field of information and knowledge management have started to seek assistance from the information retrieval and artificial intelligence communities, who have much to offer concerning advanced information indexing, searching, and classification techniques. Previous research has strongly suggested the Kohonen Self-Organizing Map (SOM) algorithm as an ideal candidate for classifying textual documents [2]. The Kohonen SOM [5] provides an intuitively appealing organization of input data. Documents are classified according to their content, and conceptual regions are formed and named on a two-dimensional grid. Kohonen SOM output also exhibits two distinctive characteristics that are appealing for cognitive and visual reasons: First, the related topics/regions are clustered closely (the proximity hypothesis); second, larger regions represent more important aspects of a data collection (the size hypothesis). The graphical display of SOM maps prompted us to experiment with these features in a study intended to validate both the proximity and the size hypotheses. These hypotheses, if verified, would have significant implications for designing an effective and graphically appealing human-computer interface for textual analysis.

The next section summarizes techniques (statistical or neural network based) for document classification and presents a framework developed for applying the Kohonen SOM algorithm in document and concept clustering. We describe the hypotheses, experimental procedures and results used to validate the proximity hypothesis and then present the experimental results for the size hypothesis.

## Document Clustering Techniques

CLASSIFICATION OF TEXTUAL DOCUMENTS REQUIRES GROUPING similar concepts/terms by category or topic. There are two approaches to cluster analysis: the statistical approach and the neural network approach. In this section, we provide only a brief summary of the conventional statistical approach and a more detailed review of the newer parallel, neural network approach because our techniques are based on a neural network algorithm.

In the serial, statistical approach, automatic document classification involves determining a document representation structure and method for determining similarities between documents. The hierarchical clustering of documents can be done divisively or agglomeratively $[11]$ . Divisive clustering breaks one complete cluster into smaller pieces. In agglomerative clustering, similarities between individual documents are used as a starting point, and a gluing operation is carried out to form larger groups. Stepp $[12]$ described conceptual clustering as the new frontier in artificial intelligence. Algorithms for clustering involve cooccurrence of feature values, discovering conjunctive features among the attributes rather than variations in the value taken by a single attribute, and clumping concepts on the basis of most commonly occurring relations in the data. By these techniques, classes of similar objects are basically found by doing pairwise comparisons among all the data elements. These clustering algorithms are serial in nature in that pairwise comparisons are made one at a time and the classification structure is created in a serial order.

The neural network approach, on the other hand, addresses clustering and classification problems by means of a connectionist approach. Algorithms based on neural networks are parallel in that multiple connections among the nodes allow for independent, parallel comparisons. Neural network techniques can be classified as supervised and unsupervised. In supervised learning, a set of training examples is presented, one by one, to the network. The network then calculates outputs based on its current input. The resulting output is then compared with a desired output for that particular input example. The network weights are then adjusted to reduce any error. In unsupervised learning, network models are first presented with an input vector from the set of possible network inputs. The network learning rule adjusts the weights so that input examples are grouped into classes based on their statistical properties. Doszkocs, Reggia, and Lin [3] provide an excellent overview of connectionalist models in information retrieval including artificial networks, spreading activation models, associative networks, and parallel distributed processing. Chen [1] provides an up-to-date review of various machine learning techniques, neural networks, and genetic algorithms for intelligent information retrieval applications.

Among unsupervised learning methods, the Kohonen SOM has been strongly suggested as an ideal candidate for clustering of textual documents. Kohonen based his neural network on the associative neural properties of the brain. The network contains two layers of nodes: an input layer and a mapping layer in the shape of a two-dimensional grid. The output layer acts as a distribution layer. The number of nodes in the input layer is equal to the number of features associated with the input. Each node of the mapping layer has as many features as there are input nodes. Thus, the input layer and each node of the mapping layer can be represented as a vector that contains the number of features of the input. The network is fully connected in that every mapping node is connected to every input node. The topology of the Kohonen SOM network is shown in figure 1.

Several recent studies adapted the SOM approach to textual analysis and classification. Ritter and Kohonen [9] applied the Kohonen SOM to textual analysis in an attempt to detect the logical similarity between words from the statistics of their contexts. Miikkulainen [7] developed DISCERN (Distributed Script processing and Episodic memoRy Network) as a prototype of a subsymbolic natural language processing system based on the Kohonen SOM. Lin, Soergel, and Marchionini [6] used the Kohonen SOM for classifying documents for information retrieval. The documents were classified according to their content, and conceptual regions were formed and named on a two-dimensional grid. Lin's work first demonstrated the feasibility of using the Kohonen algorithm for classification of textual documents. Orwig and Chen adopted a scalable SOM algorithm to classify electronic brainstorming outputs and Internet homepages [2, 8]. The scalability was achieved using the Scalable SOM (SSOM) technique developed by Roussinov and Chen [10]. The SSOM data structure and algorithm took advantage of the sparsity of coordinates in the document input vectors and reduced the SOM computational complexity by several order of magnitude, thus making large-scale textual categorization tasks possible. Kaski, Honkela, Lagus, and Kohonen reported WEBSOM [4], an SOM-based text classifier for clustering postings to the Usenet newsgroups. The basic WEBSOM architecture consists of two hierarchically interrelated SOMs. A word category map [9] is created first to describe relations of words based on their averaged short contexts. In the second stage, the text of a document is mapped onto the word category map previously created, and a histogram of the hits on it is formed. The document map is then obtained using the histograms as the fingerprints of the textual documents. WEBSOM also provides automatic labeling as exhibited in Chen's work, but the lack of distinct region boundaries could limit its use.

Each Output Node is a vector of N weights  
![](/api/attachments/SQEQZNNW/fulltext/images/ba72530e70917cd175118e77cde5b2bf2be7e6545c072d8c6dcf6d03cd898123.jpg)  
Figure 1. Kohonen Self-Organizing Map (SOM) Topology

## A Framework for Document Classification

The Kohonen SOM algorithm for classifying textual documents requires outputs from automatic indexing or the noun-phrase extraction process, which contain index terms for the documents and a list of terms in decreasing order of frequency for the entire collection. Based on the indexing terms identified, each document then is represented by a term vector of 1 or 0. The number of 1s in each document is equal to the number of terms in the document, and each vector position corresponds with one unique term.

We chose a 20'10 grid map for displaying SOM outputs, based on what would fit on an output screen. We used a hexagonal neighborhood area that considers six surrounding nodes to be a node's immediate neighborhood. Finally, we used the bubble adjustment method, which is an adjustment of the weights of neighboring nodes based upon the decreasing gain term. In the initial training phase, we used a gain term adjustment of 0.05, and a neighborhood size of 10. In the fine-tuning phase we used a small gain term adjustment of 0.01, and a smaller neighborhood size of 3.

After the training and tuning phases, the SOM visualization consisted of running the same input file against the trained map and reporting the map grid location that is the closest in Euclidean distance to each input. Each document (vector) and each term (represented as a unit vector) were thus mapped to a node and also to a region (of the same nodes) on the map. The nodes were then labeled so nodes with the same labels could form regions. The SOM algorithm we adopted, as opposed to the original Kohonen SOM, is summarized below:

1. Initialize input nodes, output nodes, and connection weights: Represent each document (or image) as an input vector of N keywords (or image features) and create a two-dimensional map (grid) of M output nodes (e.g., a 20'10 map of 200 nodes). Initialize weights from N input nodes to M output nodes to small random values.

2. Present each document or image in order: Represent each document by a vector of N features and present to the system.

3. Compute distances to all nodes: Compute distance $d_{j}$ between the input and each output node j using

$$
d _ {j} = \sum_ {i = 0} ^ {N - 1} \left(x _ {i} (t) - w _ {i j} (t)\right) ^ {2}
$$

where $x_{i}(t)$ is the input to node i at time t and $w_{ij}(t)$ is the weight from input node i to output node j at time period t.

4. Select winning node $j^{*}$ and update weights to node $j^{*}$ and neighbors: Select winning node $j^{*}$ as that output node with minimum $d_{j}$ . Update weights for node $j^{*}$ and its neighbors to reduce their distances (between input nodes and output nodes). (See [5] for the algorithmic detail of neighborhood adjustment.)

5. Label regions in map: After the network is trained through repeated presentation of all inputs, submit unit input vectors of single terms to the trained network and assign the winning node the name of input feature. Neighboring nodes that contain the same feature then form a concept or topic region. The resulting map thus represents regions of important terms or image patterns (the more important a concept, the larger a region) and the assignment of similar documents or images to each region.

6. Apply the above steps recursively for large regions: For each map region that contains more than k (e.g., 100) documents or images, conduct a recursive procedure to generate another self-organizing map until each region contains no more than k documents or images.

## Proximity Hypothesis

IN ORDER TO VALIDATE THE PROXIMITY HYPOTHESIS FOR SOM MAPS, we recently designed and conducted a user study aimed at answering the following questions:

Can the SOM really cluster related topics together? Can the results be systematically validated using human beings as judges? Specifically, do the term associations suggested by the SOM match the associations that human subjects expect to see?

## Experimental Hypothesis

To evaluate the term associations produced by the SOM, the SOM maps were compared with maps generated at random, which provided region associations created by chance without the treatment of the Kohonen SOM algorithm. Concept precision and recall were used as the measurements. The respective null and alternative hypotheses were:

$H_{0}$ : SOM performs no better than a map generated randomly in terms of precision and recall;

$H_{1}$ : Otherwise (SOM does perform better).

## Test Collections

Two data collections were used in order to compare results across different domains and types of documents. EBS was a set of electronic brainstorming output containing 206 comments. Each comment was one to four lines of textual description regarding the future of collaborative systems. This collection is a good example of a small data collection that focuses on a single topic. ITO was a collection of 586 project summaries for project proposals that have been awarded by the Information Technology Office (ITO) in the Defense Advanced Research Projects Agency (DARPA). These documents contained three to four pages of structured textual descriptions about the title, performer, objective, approach, and accomplishments of research projects. While the project summaries tended to be consistent in size, the range of topics within the ITO collection was much greater than within the EBS collection, covering everything from digital libraries to intelligent agents to IP multicasting. ITO provides a good example of a rich technical domain with a wide range of hardware and software topics.

## Preprocessing

Automatic indexing and noun phrasing were applied to the EBS and ITO collections. For the EBS collection, 1,104 concept terms were identified, while 4,258 terms were identified for ITO. Table 1 lists the twenty most frequently appearing terms in the ITO collection, along with their term frequency. For the EBS collection, we used 500 training iterations and 5,000 tuning iterations. The vector size (the number of terms used to form document vectors) was 100. It took five minutes to generate the EBS dataset on a mid-sized DEC Alpha 3000/600 server. For the ITO collection, the training and tuning cycles were 1,800 and 4,800, respectively. The vector size was 1,000. It took twenty minutes to generate when computation was done on a DEC 2100 server.

Table 1. Twenty Most Frequently Occurring Terms in the ITO Collection

<table><tr><td>Rank</td><td>No. occurrences</td><td>Term</td></tr><tr><td>1</td><td>29</td><td>User interface</td></tr><tr><td>2</td><td>29</td><td>Quality of service</td></tr><tr><td>3</td><td>28</td><td>Technology transfer</td></tr><tr><td>4</td><td>25</td><td>Fault tolerance</td></tr><tr><td>5</td><td>25</td><td>Resource management</td></tr><tr><td>6</td><td>22</td><td>Military applications</td></tr><tr><td>7</td><td>22</td><td>Message passing</td></tr><tr><td>8</td><td>21</td><td>Complex systems</td></tr><tr><td>9</td><td>20</td><td>Real-time systems</td></tr><tr><td>10</td><td>20</td><td>Software tools</td></tr><tr><td>11</td><td>19</td><td>Software components</td></tr><tr><td>12</td><td>17</td><td>Security services</td></tr><tr><td>13</td><td>17</td><td>System design</td></tr><tr><td>14</td><td>16</td><td>Real time</td></tr><tr><td>15</td><td>16</td><td>Programming languages</td></tr><tr><td>16</td><td>16</td><td>File system</td></tr><tr><td>17</td><td>15</td><td>Software architecture</td></tr><tr><td>18</td><td>15</td><td>Real-time applications</td></tr><tr><td>19</td><td>14</td><td>Analysis tools</td></tr><tr><td>20</td><td>14</td><td>Security mechanisms</td></tr></table>

The SOM output for the EBS collection is presented and discussed in $[8]$ . The SOM Map for the ITO collection is shown in figure 2. The SOM map created contains forty-five regions, with thirty-nine unique concepts. An alphabetical list view showing the unique concept regions in a sidebar is provided as an alternative to the two-dimensional grid. For easier map visualization, clicking items from the list will make their corresponding SOM regions blink. The numbers on the map correspond with the number of documents that are classified into a particular concept region. The concept regions can be clicked to view the documents directly. The initial outputs and computational characteristics for the ITO maps are interesting. We observed that many of the larger concept regions appeared to be meaningful and to relate to each other (e.g., DIGITAL LIBRARY and INFORMATION RETRIEVAL form neighboring regions in the middle of the map, while MOBILE NETWORK and WIRELESS NETWORK are on the top-right region of the map).

## Subjects and Experimental Procedures

The experiment involved thirty human subjects, mainly graduate students from the MIS and ECE departments at the University of Arizona. Subjects chosen possessed prior knowledge and training in collaborative computing and advanced artificial intelligence/software engineering topics so they could evaluate both the EBS and the ITO collections.

Downloaded by [University of Bath] at 19:24 15 March 2016

<table><tr><td colspan="7">Category List:</td></tr><tr><td colspan="7">Adaptive Computing System (13)</td></tr><tr><td colspan="7">Architectural Design (9)</td></tr><tr><td colspan="7">Collaborative Systems (13)</td></tr><tr><td colspan="7">Complex Systems (42)</td></tr><tr><td colspan="7">Demonstration Systems (30)</td></tr><tr><td colspan="7">Design Methodologies (13)</td></tr><tr><td colspan="7">Digital Library (22)</td></tr><tr><td colspan="7">Fault Tolerance (30)</td></tr><tr><td colspan="7">Formal Specifications (29)</td></tr><tr><td colspan="7">Hardware Designs (9)</td></tr><tr><td colspan="7">Image Processing (13)</td></tr><tr><td colspan="7">Information Infrastructure (5)</td></tr><tr><td colspan="7">Information Retrieval (53)</td></tr><tr><td colspan="7">Instruction-level Parallelism (13)</td></tr><tr><td colspan="7">Intelligent Agents (64)</td></tr><tr><td colspan="7">Intrusion Detection (9)</td></tr><tr><td colspan="7">Message Passing (33)</td></tr><tr><td colspan="7">Military Applications (22)</td></tr><tr><td colspan="7">Mobile Network (12)</td></tr><tr><td colspan="7">Multicast Routing (19)</td></tr><tr><td colspan="7">Network Management (16)</td></tr><tr><td colspan="7">Parallel Computers (13)</td></tr><tr><td colspan="7">Parallel Programs (14)</td></tr><tr><td colspan="7">Power Consumption (17)</td></tr><tr><td colspan="7">Programming Languages (18)</td></tr><tr><td colspan="7">Quality Of Service (41)</td></tr><tr><td colspan="7">Real-time Systems (24)</td></tr><tr><td colspan="7">Reliable Multicast (13)</td></tr><tr><td colspan="7">Resource Management (31)</td></tr><tr><td colspan="7">Runtime Environments (7)</td></tr><tr><td colspan="7">Security Services (27)</td></tr><tr><td colspan="7">Simulation Tools (12)</td></tr><tr><td colspan="7">Software Components (39)</td></tr><tr><td colspan="7">Software Tools (30)</td></tr><tr><td colspan="7">Speech Recognition (22)</td></tr><tr><td colspan="7">System Design (25)</td></tr><tr><td colspan="7">Technology Transfer (33)</td></tr><tr><td colspan="7">User Interface (41)</td></tr><tr><td colspan="7">Wireless Networks (16)</td></tr></table>

Figure 2. SOM Map for the ITO Collection

We first sampled regions from the SOM maps. For each region sampled, the number of its neighbors and the neighbors' respective region labels were recorded. We then asked the human subjects to select from a list of all region labels the same number of concepts as the SOM had found most relevant to the same concept we sampled. The subjects were asked to perform a total of nine tasks, four for the EBS collection and five for the ITO collection. The user interface for the experiment was a Java applet, shown in figure 3, which allowed users to drag and drop terms from the term list to single out concept terms most related to the head concept. Subjects completed the experiment in fifteen to thirty minutes.

## Experimental Results

The respective performances of the SOM and the random maps were computed using concept recall and precision as measurements determined by equations in which X represented terms suggested by either the SOM or the random map and Y represented terms suggested by the human subjects:

$$
\text { Precision } = \frac {(X \cap Y)}{X} \quad \text { Recall } = \frac {(X \cap Y)}{Y}.
$$

In our study, since the number of terms suggested by the human subject equaled the number of terms suggested by the SOM maps or the random maps, the concept precision and recall scores were effectively the same.

Tables 2 and 3 contain the results of statistical analysis (both ANOVA and paired t-tests) of the comparison of the recall/precision levels of SOM and the random maps as judged by the subjects. For the EBS collection, SOM achieved a respectable 32.29 percent precision and recall, versus 18.12 percent for the random map. For the ITO dataset, SOM had 26.85 percent precision and recall, versus 6.59 percent for the random map. In both cases, the p values = 0.0000 (meaning that they were less than 0.00005). With such a small p value, we have strong evidence that the mean change is greater than zero. We rejected our null hypothesis and concluded that SOM does make a difference in terms of the ability to cluster similar concepts/regions together. In summary, the results from our evaluation were encouraging. In light of the cognitive demand and the cumbersome nature of classifying/clustering textual documents, we believe this research has established the Kohonen SOM as a promising and visually appealing neural-network-based textual analysis and mining technique.

## Size Hypothesis

THE SIZE HYPOTHESIS SUGGESTS THAT LARGER REGIONS REPRESENT more important topics in the data collection. We expect that as more documents are assigned to a region, the size of the region will increase. The statistical test we performed therefore is aimed to answer the following question: Is there sufficient evidence to conclude that a significant positive relationship exists between the number of documents in a region (X) and the corresponding region size (Y)?

![](/api/attachments/SQEQZNNW/fulltext/images/fd5cc60762f4265fb4d3d40f73288773d744a88c65f0659cebdc70e3047872ba.jpg)  
Figure 3. Software Interface for User Evaluation

## Experimental Hypothesis

In this study, the relationship between X and Y is assumed to be linear. Let $b_{1}$ be the population slope. The null and alternative hypotheses are:

$H_{0}: b_{1} \leq 0$ (X provides no information)

$H_{1}: b_{1} > 0$ (X does provide information)

## Test Collections and Procedures

We used SOM maps generated for both the EBS and ITO collections to validate the size hypothesis. The size and number of documents contained within each region on the map were recorded and tabulated. From the SOM map for EBS collection, we recorded twenty-eight data entries (region size and document number pairs). From the SOM map for ITO collection, we recorded forty-two data entries in the data collection and discarded one outlier. We then performed a linear regression procedure on the data and conducted a one-tailed test on the slope of the regression line.

Table 2. Recall/Precision Analysis for the Small EBS Collection

<table><tr><td colspan="7">Analysis of variance</td></tr><tr><td>Source</td><td>DF</td><td colspan="2">SS</td><td>MS</td><td>F</td><td>P</td></tr><tr><td>Factor</td><td>1</td><td colspan="2">0.30104</td><td>0.30104</td><td>39.0</td><td>70.000</td></tr><tr><td>Error</td><td>58</td><td colspan="2">0.44690</td><td>0.00771</td><td></td><td></td></tr><tr><td>Total</td><td>59</td><td colspan="2">0.74794</td><td></td><td></td><td></td></tr><tr><td rowspan="2">Level</td><td rowspan="2">N</td><td rowspan="2">Mean</td><td rowspan="2">St. dev.</td><td colspan="3">Individual 95 % CI&#x27;s for mean based on pooled st. dev.</td></tr><tr><td colspan="3">- - - - + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</td></tr><tr><td>SOM</td><td>30</td><td>0.32292</td><td>0.8817</td><td></td><td></td><td>(- ---- * ----)</td></tr><tr><td>Random</td><td>30</td><td>0.18125</td><td>0.08738</td><td>(- ---- * ----)</td><td></td><td></td></tr><tr><td colspan="4">Pooled st. dev. = 0.08778</td><td>0.180</td><td>0.240</td><td>0.300</td></tr><tr><td colspan="7">Test of mu = 0.0000 versus mu n.e. 0.0000</td></tr><tr><td></td><td>N</td><td>Mean</td><td>St. dev.</td><td>SE mean</td><td>T</td><td>P value</td></tr><tr><td>SOM-random</td><td>30</td><td>0.1417</td><td>0.1303</td><td>0.0238</td><td>5.95</td><td>0.0000</td></tr><tr><td colspan="4">95.0% CI for mu SOM-random:</td><td></td><td colspan="2">(0.0930, 0.1903)</td></tr></table>

Table 3. Recall/Precision Analysis for the Large ITO Collection

<table><tr><td>Source</td><td>DF</td><td colspan="2">SS</td><td>MS</td><td>F</td><td>P</td></tr><tr><td>Factor</td><td>1</td><td colspan="2">0.61491</td><td>0.61491</td><td>120.01</td><td>0.000</td></tr><tr><td>Error</td><td>58</td><td colspan="2">0.29718</td><td>0.00512</td><td></td><td></td></tr><tr><td>Total</td><td>59</td><td colspan="2">0.91210</td><td colspan="3">Individual 95 % CI&#x27;s for mean based on pooled st. dev.</td></tr><tr><td>Level</td><td>N</td><td>Mean</td><td>St. dev.</td><td colspan="3">- - - - + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</td></tr><tr><td>SOM</td><td>30</td><td>0.26846</td><td>0.09030</td><td></td><td></td><td>(- ----*----)</td></tr><tr><td>Randon</td><td>30</td><td>0.06599</td><td>0.04576</td><td>(- ----*----)</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td colspan="3">- - - - + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</td></tr><tr><td colspan="4">Pooled st. dev. = 0.07158</td><td>0.070</td><td>0.140</td><td>0.210</td></tr></table>

<table><tr><td></td><td>N</td><td>Mean</td><td>St. dev.</td><td>SE mean</td><td>T</td><td>P value</td></tr><tr><td>SOM–random</td><td>30</td><td>0.2025</td><td>0.0963</td><td>0.0176</td><td>11.52</td><td>0.0000</td></tr><tr><td colspan="5">95.0% CI for mu SOM–random:</td><td colspan="2">(0.1665, 0.2384)</td></tr></table>

## Tests of Significance

The regression test statistics are shown in Tables 4 and 5, respectively. For the EBS collection, the regression output gives the test statistic t = 4.82 and the p values = 0. With 27 degrees of freedom, this value of t is highly significant, giving us evidence that $b_{1} > 0$ . Similarly, for the ITO dataset: t = 6.76 and the p values = 0. The t value is also highly significant, with 40 degrees of freedom. This in turn implies that the number of documents in a region is a useful predictor of the corresponding region size for these documents.

## Conclusions and Research Directions

THIS RESEARCH SOUGHT TO VALIDATE THE PROPERTIES OF THE KOHONEN SOM in the domain of textual classification. In evaluation of the proximity hypothesis, we compared SOM's clustering of concept terms with a random map topology and used human beings as judges. The results were encouraging; the SOM was able to cluster related topics (i.e., similar head concepts on the SOM map) together, thus allowing users of the data collection to identify concept clusters quickly. For example, the DARPA ITO program officers were able to identify several research streams that they have been supporting. These include projects with an emphasis on issues related to networking such as Multicast Routing, Mobile Network, and Wireless Network, or projects geared toward information retrieval and analysis, such as Digital Library, Intelligent Agents, and Speech Recognition related research.

For the size hypothesis, our results suggest is a positive correlation between the size of SOM regions and their relative importance in the data collection. This property is significant in that, when a user is presented an SOM map, his or her attention is immediately drawn to the larger regions on the map. If the larger regions on an SOM map indeed represent the major issues (judged by the concentration of documents in the SOM regions) in the data collection, SOM can then be used as a tool to provide graphical summaries for large textual data collection. For example, among the regions on the ITO SOM map, larger regions such as Quality of Services (QoS), User Interface, and Complex Systems were usually among the first few topics to be observed by the viewers.

More work is needed to extend this research to validate such properties in 3D SOM, in which the SOM outputs are mapped to 3D cubes as opposed to 2D nodes. Another possible extension involves evaluation of the multilayered SOM [2], which uses the divide-and-conquer strategy to provide scalable organization for large-scale textual collections. We believe this research has established the Kohonen SOM algorithm as an intuitively appealing and promising neural-network-based textual classification technique for addressing part of the longstanding problem of “information overload.”

Table 4. Regression Statistics for the Small EBS Collection  
The regression equation is $y = -0.72 + 0.996x$

<table><tr><td>Predictor</td><td>Coeff.</td><td>St. dev.</td><td>T</td><td>P</td></tr><tr><td>Constant</td><td>-0.720</td><td>1.855</td><td>-0.39</td><td>0.701</td></tr><tr><td>x</td><td>0.9962</td><td>0.2065</td><td>4.82</td><td>0.000</td></tr><tr><td>S=4.752;</td><td>R-sq = 47.2%;</td><td></td><td colspan="2">R-sq (adj) = 45.2%</td></tr></table>

Analysis of variance

<table><tr><td>Source</td><td>DF</td><td>SS</td><td>MS</td><td>F</td><td>P</td></tr><tr><td>Regression</td><td>1</td><td>525.44</td><td>525.44</td><td>23.26</td><td>0.000</td></tr><tr><td>Residual error</td><td>26</td><td>587.24</td><td>22.59</td><td></td><td></td></tr><tr><td>Total</td><td>27</td><td>1112.68</td><td></td><td></td><td></td></tr></table>

Table 5. Regression Statistics for the Large ITO Collection  
The regression equation is $y = -2.02 + 0.308x$

<table><tr><td>Predictor</td><td>Coeff.</td><td>St. dev.</td><td>T</td><td>P</td></tr><tr><td>Constant</td><td>-2.016</td><td>1.074</td><td>-1.88</td><td>0.068</td></tr><tr><td>x</td><td>0.30755</td><td>0.04552</td><td>6.76</td><td>0.000</td></tr><tr><td>S=3.044;</td><td>R-sq = 53.9%;</td><td></td><td colspan="2">R-sq (adj) = 52.7%</td></tr></table>

Analysis of variance

<table><tr><td>Source</td><td>DF</td><td>SS</td><td>MS</td><td>F</td><td>P</td></tr><tr><td>Regression</td><td>1</td><td>422.90</td><td>422.90</td><td>45.64</td><td>0.000</td></tr><tr><td>Residual error</td><td>39</td><td>361.35</td><td>9.27</td><td></td><td></td></tr><tr><td>Total</td><td>40</td><td>784.24</td><td></td><td></td><td></td></tr></table>

Acknowledgment: This project is supported by the following grants: NSF/DARPA/NASA Digital Library Initiative, IRI-9411318, 1994–1998 (B. Schatz and H. Chen, “Building the Interspace: Digital Library Infrastructure for a University Engineering Community”), DARPA Information Management Program, N66001-97-C-8535, 1997–2000 (B. Schatz and H. Chen, “The Interspace Prototype: An Analysis Environment for Semantic Interoperability”), and DARPA ITO N66001-99-1-8907 (J.F. Nunamaker, “Dialog Architecture for Collaboration”). We would also like to thank Olivia Sheng, Ron Larsen, and Allen Sears for comments and insights that have guided us in our research.

## REFERENCES

1. Chen, H. Machine learning for information retrieval: neural networks, symbolic learning, and genetic algorithms. Journal of the American Society for Information Science, 46 (1995), 194–216.

2. Chen, H.; Schuffels, C.; and Orwig, R. Internet categorization and search: a self-organizing approach. Journal of Visual Communications and Image Representation, 7, 1 (March 1996), 88–102.

3. Doszkocs, T.; Reggia J.; and Lin X. Connectionist models and information retrieval. Annual Review of Information Science and Technology, 25 (1990), 209–260.

4. Kaski, S.; Honkela, T.; Lagus, K.; and Kohonen, T. Creating an order in digital libraries with self-organizing maps. Proceedings of World Congress on Neural Networks, San Diego, 1996.

5. Kohonen, T. Self-Organizing Maps. Berlin: Springer-Verlag, 1995.

6. Lin X.; Soergel D.; and Marchionini G. A self-organizing semantic map for information retrieval. Proceedings of the Fifteenth Annual International ACM/SIGIR Conference on R&D in Information Retrieval, Copenhagen, 1992, pp. 37–50.

7. Miikkulainen, R. Symbolic Natural Language Processing: An Integrated Model of Scripts, Lexicons, and Memory. Cambridge, MA: MIT Press, 1993.

8. Orwig R.; Chen, H.; and Nunamaker, J.F. A graphical, self-organizing approach to classifying electronic meeting output. Journal of the American Society for Information Science, 48, 2 (1997), 157–170.

9. Ritter, H., and Kohonen, T. Self-organizing semantic maps. Biological Cybernetics, 61 (1989), 241–254.

10. Roussinov D., and Chen, H. A scalable self-organizing map algorithm for textual classification: a neural network approach to thesaurus generation. Communication Cognition and Artificial Intelligence (Spring 1998).

11. Salton, G. Automatic Text Processing. Reading, MA: Addison Wiley, 1989.

12. Stepp, R. Concepts in conceptual clustering. Proceedings of the Tenth International Joint Conference on Artificial Intelligence, Milan, 1987.
