---
otero_id: 10712
otero_key: "G2MRNV5D"
title: "Managing Knowledge in Light of Its Evolution Process: An Empirical Study on Citation Network-Based Patent Classification"
authors: "Xin Li; Hsinchun Chen; Zhu Zhang; Jiexun Li; Jay F. Nunamaker"
year: "2009"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222260106"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Managing Knowledge in Light of Its Evolution Process: An Empirical Study on Citation Network-Based Patent Classification

Xin Li , Hsinchun Chen , Zhu Zhang , Jiexun Li & Jay F. Nunamaker

To cite this article: Xin Li , Hsinchun Chen , Zhu Zhang , Jiexun Li & Jay F. Nunamaker (2009) Managing Knowledge in Light of Its Evolution Process: An Empirical Study on Citation Network-Based Patent Classification, Journal of Management Information Systems, 26:1, 129-154

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222260106

![](/api/attachments/G2MRNV5D/fulltext/images/46b2b4962d3058611d4d5b5d0f8890e0316a078631f8daeeab9710ae1d575ad4.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/G2MRNV5D/fulltext/images/bb046cb35a34a4ab29fd4e0339189bc79788570b57e72bf34ad90211a6048925.jpg)

Submit your article to this journal

![](/api/attachments/G2MRNV5D/fulltext/images/1b0c052a1ef61a369c558e2f27e7c04ae02aeeebdf8165d87bd51e9083f709c7.jpg)

Article views: 13

![](/api/attachments/G2MRNV5D/fulltext/images/fb3941b1266af3036fa509f93667d80f9a1d9adcf46b7b9293ecbef2863bae28.jpg)

View related articles

![](/api/attachments/G2MRNV5D/fulltext/images/109c09deb9fc984de5fd3e01d0b3d8d0c66eb31b0dfb51b969fa5a9327590139.jpg)

Citing articles: 2 View citing articles

# Managing Knowledge in Light of Its Evolution Process: An Empirical Study on Citation Network–Based Patent Classification

Xin Li, Hsin ch un Chen , Zh u Zh an g, Jiex un Li, and Jay F. Nun amake r Jr.

Xin Li is an Assistant Professor in the Department of Information Systems at the City University of Hong Kong. He received his Ph.D. in Management Information Systems from the University of Arizona. He received his B.S. and M.S. from the Department of Automation at Tsinghua University, China. His research interests include business intelligence, knowledge discovery and data mining, social network analysis, patent analysis, and bioinformatics. His work has appeared in the Journal of Biomedical Informatics, Journal of the American Society for Information Science and Technology, Bioinformatics, and Nature Nanotechnology, and in various conference proceedings including the AC M/IEEE Joint Conference on Digital Libraries.

Hsinch un Ch en is McClelland Professor of Management Information Systems at the University of Arizona and Andersen Consulting Professor of the Year (1999). He received a B.S. from National Chiao-Tung University in Taiwan, an MBA from SUNY Buffalo, and a Ph.D. in Information Systems from New York University. Dr. Chen is a Fellow of IEEE and A S. He received the IEEE Computer Society 2006 Technical Achievement Award. He is author/editor of 13 books, 17 book chapters, and more than 130 Science Citation Index journal articles covering digital library, intelligence analysis, biomedical informatics, data/text/Web mining, knowledge management, and Web computing. He serves on ten editorial boards and has served as a scientific counselor/advisor of the National Library of Medicine. He has been an advisor for major National Science Foundation (NSF), Department of Justice (DOJ), National Library of Medicine (NLM), Department of Defense (DOD), Department of Homeland Security (DHS), and other international research programs in digital library, digital government, medical informatics, and national security research.

Zh u Zh ang is an Assistant Professor in the Department of MIS at the University of Arizona. He received his Ph.D. in Computer and Information Science from the University of Michigan. His research interests include data and text mining, machine learning, and Internet computing. His work has appeared in the Journal of the American Society for Information Science and Technology, IEEE Intelligent Systems, and Information Systems, and in various conference proceedings. Dr. Zhu is a member of the AIS, A I, AC L, and AC M.

Jiex un Li is an Assistant Professor in the College of Information Science and Technology at Drexel University. He received his Ph.D. in Management Information Systems from the University of Arizona in 2007 and his M.S. in Management from Tsinghua University, Beijing, China, in 2002. His research focuses on data/text mining and machine learning for knowledge discovery. His research in knowledge discovery has covered various application areas such as business, bioinformatics, and security. He has published in Communications of the ACM, Journal of the American Society for Information Science and Technology, Bioinformatics, IEEE Transactions on Information Technology in Biomedicine, Decision Support Systems, and Journal of the Association for Information Systems.

Jay F. Nunamaker Jr. is Regents and Soldwedel Professor of MIS, Computer Science and Communication, and Director of the Center for the Management of Information at the University of Arizona, Tucson. He received his Ph.D. in Systems Engineering and Operations Research from Case Institute of Technology, an M.S. and B.S. in Engineering from the University of Pittsburgh, and a B.S. from Carnegie Mellon University. Dr. Nunamaker received the LEO Award from the Association of Information Systems at ICIS in Barcelona, Spain, December 2002. This award is given for a lifetime of exceptional achievement in information systems. He was elected as a fellow of the Association of Information Systems in 2000. Dr. Nunamaker has over 40 years of experience in examining, analyzing, designing, testing, evaluating, and developing information systems. He served as a test engineer at the Shippingport Atomic Power facility, as a member of the ISDOS team at the University of Michigan, and as a member of the faculty at Purdue University prior to joining the faculty at the University of Arizona in 1974. His research on group support systems addresses behavioral as well as engineering issues and focuses on theory and implementation. He has been a licensed professional engineer since 1965.

Abstract: Knowledge management is essential to modern organizations. Due to the information overload problem, managers are facing critical challenges in utilizing the data in organizations. Although several automated tools have been applied, previous applications often deem knowledge items independent and use solely contents, which may limit their analysis abilities. This study focuses on the process of knowledge evolution and proposes to incorporate this perspective into knowledge management tasks. Using a patent classification task as an example, we represent knowledge evolution processes with patent citations and introduce a labeled citation graph kernel to classify patents under a kernel-based machine learning framework. In the experimental study, our proposed approach shows more than 30 percent improvement in classification accuracy compared to traditional content-based methods. The approach can potentially affect the existing patent management procedures. Moreover, this research lends strong support to considering knowledge evolution processes in other knowledge management tasks.

Key words and ph rases: citation analysis, classification, kernel-based method, knowledge management, machine learning, patent management.

types of knowledge and information. As a result, managers face more challenges in organizing and managing knowledge for future sharing and usage [12, 39]. Some typical knowledge management (KM) tasks include indexing and classifying patents for intellectual property protection and licensing, analyzing online news articles for decision support, managing technical documents for research and development, and maintaining employee profiles for team building.

To facilitate such KM tasks, automated tools such as classification, clustering, and visualization techniques have been widely adopted [49]. In documents and multimedia items, the textual and multimedia contents are often regarded as the major carrier of knowledge (i.e., explicit knowledge) for human cognition [50]. Most previous automated KM techniques treat knowledge items independently and process their contents alone for KM tasks.

However, knowledge items are not independent from each other. Ignoring relationships among them may limit the ability of the KM tools. Knowledge evolves after transfer and reuse during human collaboration [3]. Knowledge creation has been considered as a path-dependent evolution process [38], where innovation is created based on the recombination of prior knowledge elements [15]. For example, project reports can be written based on previous meeting memos, technical documents can be compiled based on older versions, and new patents are invented based on existing technologies. From this perspective, the knowledge evolution processes may affect the newly created knowledge, as reflected in its content. Therefore, not only the knowledge content but also the knowledge evolution process should be taken into account in KM tasks.

The knowledge evolution process is often embedded in the relationships among individual documents, as the knowledge producers refer to related sources. For example, patents and scientific literature have citations to specify their intellectual basis; Web pages contain hyperlinks to related pages. As individual documents are composed into such “linked” documents, the links potentially represent the evolution history of knowledge. In this research, we choose one type of linked document—patents—and conduct an empirical study to exploit the utility of knowledge evolution processes in KM tasks. Specifically, we focus on patent classification, which is both practically important to managers and theoretically representative to other KM tasks.

Patents contain a significant amount of knowledge on technical innovations. Patent management, at both the organization level and the society level, prompts the exchange of inventions [43] and reduces the duplication of research efforts [16]. In the past two decades, the advance of technology and the changes in patent policies have led to a surge in patent applications and publications, especially in high-tech fields [54]. As a result, patent processing time has been prolonged by more than 50 percent since 1994 [24], while the patent examiners’ workload has been continuously increasing [28]. In patent management, classification plays a critical role, including assigning patent applications to examiners [48] and organizing patents based on patent classification schemes, e.g., the United States Patent Classification (USPC) system. The performance of patent classification affects the efficiency of patent examination and the effectiveness of patent search systems.

Most previous studies in patent classification focused on only content analysis and addressed the problem as a canonical text categorization problem [35, 44]. Although various features extracted from patent contents have been used and several machine learning algorithms have been applied [13], such approaches have not provided satisfactory performance [48]. On the other hand, patent citations have been considered a valid representation of knowledge diffusion and reuse in innovation creation [1, 46], in the sense that citing patents adopt knowledge elements from cited patents. The evolution processes of innovations can be represented as patent citation networks. The unsatisfactory performance of existing content analysis approaches and the explicit representation of the knowledge evolution process by patent citations make patent classification a good test bed to evaluate knowledge evolution processes’ benefits to KM tasks.

Under a kernel-based machine learning framework, we explore different methods to model patent citation networks. We propose a novel model named labeled graph kernel, which shows a significant improvement in classification performance as compared with traditional content-based approaches. We also identify both the citation network structure and the features of cited patents as important factors in describing knowledge evolution processes for patent classification. This study shows the possibilities for further automating the patent examination process and the benefits of considering the knowledge evolution process in KM tasks.

## Literature Review

As a common type of knowl edge, linked documents such as patents, scientific literature, and Web pages are associated by links in the form of citations or hyperlinks. From a KM perspective, the document content contains different forms of knowledge, while the links among them indicate the process of knowledge transfer and diffusion.

The classification of linked documents is of interest to both managers and scholars. Classification tools have been developed and adopted in patent management [48], Web page management [9], and scientific literature management [19, 45, 49]. Among these tasks, patent classification has its unique challenges due to both its critical role in practice and its data characteristics [48]. Patent classification is usually conducted on a large number of categories (for example, the USPC has 450 first-level categories and 160,000 second-level categories). Many of these fine-grained classes have subtle semantic differences and usually have an uneven number of patent instances [30]. All of these factors make patent classification difficult to address compared to other linked document classification tasks.

## Classification of Linked Documents

We review previous patent classification studies in the context of linked document classification from two aspects: features, that is, how the documents are represented, and algorithms, that is, how the documents are classified.

## Feature Types

Previous studies on the classification of patents mainly consider the features in individual documents. Features related to the citations (links) between documents have also been used.

Features of Individual Documents. Most previous research considered only the knowledge embedded in individual patents and extracted features from individual documents to represent patents. These features can be categorized into content features and metadata features. Content features are often considered good indicators of document subjects, which can be extracted at the word level (i.e., “bag-of-words”) or phrase level from different parts of the documents. In patent classification, previous studies examined the features extracted from patent title [32], abstract [14, 32, 35], claims [23], and full-text [29]. Features from patent title and abstract have been found to be more effective in patent classification.

The metadata, which usually describe the document’s author, institution, publication date, and so forth, may be highly correlated with its content and topic. In patent classification, Richter and MacFarlane [42] have used a patent’s IPC category to help classify it into another classification scheme. In Web page classification, Yang et al. [56] used Web page headers to help label Web pages by industry sectors. These studies demonstrated metadata’s effectiveness in improving classification performance.

Features of Citations/Links. In machine learning literature, citations (links) indicate the close relationship between linked documents’ topics, methods, and so forth. From the knowledge creation perspective, citations (links) indicate the inheritance or transfer of knowledge elements between linked documents [15]. In linked document classification, features can be defined on direct citations or the entire citation network (of directly and indirectly connected documents) by considering different levels of the knowledge evolution process.

The simplest way to take advantage of direct citations is to combine features of the neighboring (directly cited) documents and use them to describe the focal document. Studies in both patent classification [7] and Web page classification [18, 40, 56] have shown that combining the neighbor documents’ content features cannot significantly improve classification performance. However, it has been found that combining neighbor documents’ classification category (metadata) features does yield improvement [7, 40].

Another method that utilizes direct citation information is to define features on linkage relationships. In Web page classification research, hyperlinks have been represented as first-order logic clauses to build first-order rules describing the common characteristics of Web pages in the same category [9, 56]. Document similarity measures based on document in-links (cocitation similarity) [47], out-links (bibliographic coupling similarity) [27], or both in-links and out-links (Amsler similarity) [2] have been used with the K‑ nearest neighbor (KNN) algorithm and the support vector machine (SVM) algorithm [6, 11, 25] in both Web page and scientific literature classification studies.

Although citation measures have been widely used in patent analysis studies to assess the impact of patents, inventors, and assignees [22, 37], few previous studies have taken advantage of linkage features.

While using direct citations only considers a single step of the knowledge transfer between citing and cited documents, using features extracted from the entire citation network is a natural extension that gives a more complete picture of the knowledge evolution process. In recent studies on network topological analysis, researchers found that the networks of patents [34], Web pages [5], and scientific literature [41] are different from random networks. Their organized topological characteristics indicate that rich information is contained in these networks. However, few studies have considered using features defined on patent citation networks to represent the knowledge transfer and innovation generation processes in patents and to address the patent classification problem.

## Algorithm Types

The algorithms used in patent and other linked document classification can be categorized into feature-based methods and kernel-based methods.

Feature-Based Methods. Feature-based methods are the major approach used in previous patent classification research. In feature-based methods, a data instance is represented by a feature vector, in which the features are explicitly constructed and selected based on domain knowledge or using automatic algorithms. In patent classification, KNN [53], Winnow [29, 30], naive Bayes, and probabilistic relational model (PRM) [52] have been widely applied on content features. Feature-based methods can utilize different types of information by incorporating different types of features in the feature vector. In previous research, content features and neighbor document features (direct citation features) have been used together with the naive Bayes algorithm in both patent and Web page classification [7, 40].

Kernel-Based Methods. Unlike feature-based methods, kernel-based methods do not require the explicit definition of feature vectors. A kernel-based method contains a kernel function and a kernel machine. The kernel function (or kernel) maps data instances from the input space χ to a feature space H (named reproducing kernel Hilbert space [RK HS]) $\Phi ( x ) : \chi \to H ,$ by defining a similarity measure between data instances $k \colon \chi \times \chi \to \Re \quad ( x , x ^ { \prime } ) \to k ( x , x ^ { \prime } )$ . Although F(x) is not explicitly defined, for every pair of data instances, the kernel function ensures that $k ( x , x ^ { \prime } ) = < \Phi ( x ) , \Phi ( x ^ { \prime } ) >$ A kernel machine, such as SVM, is a learning algorithm that performs learning tasks in the feature space H [17]. Given limited types of kernel machines (with SVM being state of the art), the performance of kernel-based learning is highly dependent on the selection and design of kernel functions [51].

In linked document classification, kernel-based methods have not been used as widely as feature-based methods. However, they have shown their potential in some recent studies. For example, Fall et al. [13, 14] compared the performances of KNN, naive

Bayes, and Winnow with SVM on a linear kernel using content features and found that SVM with the linear kernel outperformed the other three feature-based methods. In Web page classification, SVM has been used on kernels defined on linkage-based similarities and reported good performance [6].

In kernel-based methods, we can use well-established kernel composition rules to combine different types of information in a learning task [10, 25, 51]. In Web page classification, Joachims et al. [25] adopted such a kernel composition method to consider both direct citation information and content information.

## Kernel-Based Methods on Structure Information

Although feature-based methods have been widely used in classification problems, they are often criticized for requiring explicit feature extraction. It is also difficult to define and extract features from instances with complex structures. This may be one reason that citation networks have been used less in patent classification. Kernelbased methods provide an effective alternative to feature extraction for capturing such complex structure information.

In kernel-based methods different kernel functions have been designed to capture structure information [17]. Among these kernels, the convolution kernel [20] is one of the most widely used. For objects (data instances) containing a set of subobjects, convolution kernels calculate the similarities between object pairs by conducting pairwise comparisons between the set of subobjects they contain. As a special case of convolution kernels, graph kernels are designed for data instances whose subobjects constitute a graph. The similarity between two graphs can be calculated by comparing the substructures in the graphs, such as nodes, paths, and subgraphs. By representing graphs as random walk paths and conducting pairwise comparison of (matching) random walk paths, graph kernels have been successfully used to classify proteins according to their molecular (graph) structures [4, 26, 33].

Although previous studies showed the effectiveness of capturing structural information using graph kernels, most of these studies focus on the structure information of the subobjects contained in data instances. In the patent classification problem, patent citation networks represent the structural information outside of data instances—that is, the evolution processes of innovations. Few previous studies have made the effort to capture such context structure information for classification purposes.

## Research Gaps and Research Questions

As an important KM task, patent classification has been studied by a number of researchers. However, most previous studies isolated the knowledge contained in an innovation (patent) from its evolution process and employed only individual patent contents to address the classification problem. Even in the broader literature of linked document classification, use of the knowledge evolution process was limited to direct citations (one-step knowledge transfer). The structure of citation (linkage) networks has not been widely utilized.

We are interested in methods that will capture the structure of patent citation networks for the patent classification problem. We focus on the following two research questions in this research:

RQ1: Exploiting the evolution process: Can the methods using citation networks outperform those using only direct citations? Will the features in the directly and indirectly cited patents be helpful for classifying the citing patent?

RQ2: Combining an innovation’s intrinsic information with its evolution process: Will combining citation information with patent contents improve patent classification performance compared with using citation or content information alone?

## Research Design

To capture th e structure of citation networks, we adopt a kernel-based approach, which also enables us to combine citation information with content information.

## A Framework of Kernel-Based Patent Classification

Figure 1 presents a general framework for addressing the patent classification problem using a kernel-based approach. (1) A t the data acquisition and parsing stage, patent data are retrieved and parsed into structured data. It should be noticed that both the patents of interest and their directly or indirectly cited patents need to be extracted. (2) A t the kernel construction stage, the similarities between data instance pairs are precomputed according to the kernel function designs. Different kernel functions can capture different information in patents and patent citation networks. (3) A t the classifier learning stage, classifiers are learned based on the precomputed kernel values using a kernel machine. In this research, we chose SVM as the kernel machine because of its reported good performance [13, 14, 25, 35]. (4) A t the evaluation stage, testing data instances are provided to the classifiers for predictions. The classification performances of different classifiers are evaluated by comparing the predictions against the actual categories provide by experienced patent examiners.

In the proposed kernel-based framework, kernel functions define similarity measures between data instances and capture patterns in data instances. The kernel machine is in charge of building the classification models. The performance of kernel-based methods is highly dependent on the design of kernel functions [51]. The major problem (and contribution) of this research becomes designing appropriate kernel functions for patent classification.

## Kernel Function Design

In light of the research gaps, we adopt and design several citation-related kernels that utilize patent citation and content information. Among these kernels, the labeled citation graph kernel is a novel kernel that captures more comprehensive information from the patent citation networks.

![](/api/attachments/G2MRNV5D/fulltext/images/e6b4264ed4f9deea428fbb38a7ad96c211c3748e86180ae4b1ac92e70d262ee1.jpg)  
Figure 1. A Framework of Kernel-Based Patent Classification

## Using Citation Information

We considered two conditions in the design of citation-related kernels.

1. The scope of the cited documents. The different levels of citations represent the different steps of knowledge transfer. In addition to considering direct citations as an approximation for one-step knowledge transfer, we can extend the citation structure and consider multiple levels of cited documents, which represent a more complete picture of the knowledge evolution process.

2. The features of the cited documents. When modeling an innovation’s evolution process, we can choose to use or not use the cited documents’ features. Without considering features of cited documents, a patent’s cited patents are encoded only as identifiers. If cited documents’ features are considered, the semantics of knowledge elements in cited patents are used, which provide extra clues for understanding the focal innovation. In this study, we consider the known classification categories of the cited patents as this type of feature, due to reported effectiveness in patent classification [7].

By combining these two conditions, we construct four kernels on patent citation information (see Table 1): bibliographic coupling kernel (K\_Bib), labeled coreference kernel $( K \_ R e f )$ , graph overlap kernel $( K _ { - } O \nu r )$ , and labeled citation graph kernel (K\_Gra).

Bibliographic Coupling Kernel. The bibliographic coupling kernel (K\_Bib) design adopted from Calado et al. [6] was initially used in the context of Web page classification. It utilizes direct citations of patent documents without considering the cited documents’ features. In this kernel, a patent p is represented by a set of patents it cites: $C V _ { _ { p } } = \{ q { : } p c i t e s q \}$ . The similarity between two patents is defined as the number of their common citations divided by the total number of their citations:

$$
K \_ B i b (p _ {1}, p _ {2}) = \left| C V _ {p _ {1}} \cap C V _ {p _ {2}} \right| / \left| C V _ {p _ {1}} \cup C V _ {p _ {2}} \right|,
$$

Table 1. Kernels for Citation Information

<table><tr><td></td><td>No cited documents&#x27; features</td><td>Using cited documents&#x27; features</td></tr><tr><td>Direct citations</td><td>Bibliographic coupling kernel (K_Bib)</td><td>Labeled coreference kernel (K_Ref)</td></tr><tr><td>Citation network</td><td>Graph overlap kernel (K_Ovr)</td><td>Labeled citation graph kernel (K_Gra)</td></tr></table>

where $p _ { 1 }$ and $p _ { 2 }$ are two patents and $C V _ { p _ { 1 } }$ and $C V _ { p _ { 2 } }$ represent the two sets of patents they directly cited. In this kernel, the more common neighbors that two patents share, the more similar they are.

Labeled Coreference Kernel. We design a labeled coreference kernel $( K \_ R e f )$ to consider cited patents’ features (classification category) while using only the direct citations. In this kernel, a patent $p$ is represented as a classification category vector, $C C _ { _ { p } } { = } ( c _ { _ { 1 } } ^ { \phantom { - } } , c _ { _ { 2 } } ^ { \phantom { - } } { , . . . , c _ { _ { n } } ^ { \phantom { - } } } )$ , where the elements are the numbers of directly cited patents of $p$ that belong to each classification category. The labeled coreference kernel is defined as the normalized inner product of the classification category vectors:

$$
K _ {-} \operatorname{Ref} \left(p _ {1}, p _ {2}\right) = \left\langle C C _ {p _ {1}}, C C _ {p _ {2}} \right\rangle / \sqrt {\left\langle C C _ {p _ {1}} , C C _ {p _ {1}} \right\rangle \cdot \left\langle C C _ {p _ {2}} , C C _ {p _ {2}} \right\rangle},
$$

where $p _ { 1 }$ and ${ { p } _ { 2 } }$ are two patents and $C C _ { p _ { 1 } }$ and $C C _ { p _ { 2 } }$ represent their classification category vectors. In the labeled coreference kernel, if two patents have similar citation patterns in different categories, they have relatively high similarity.

Graph Overlap Kernel. Based on the idea of the bibliographic coupling kernel, we design a graph overlap kernel (K\_Ovr) which considers more than one level of the cited patents in the patent citation network. In this kernel, a patent $p$ is represented by the set of patents it directly or indirectly cited: $G V _ { _ { p } } = \{ C V _ { _ { p } } \subseteq G V _ { _ { p } } ; i f s \in G V _ { _ { p } }$ and s cites t then $t \in G V _ { p } \}$ . The similarity of two patents is defined by the ratio of the overlap part of the two patent citation networks in the union of the two networks:

$$
K _ {-} O v r \left(p _ {1}, p _ {2}\right) = \left| G V _ {p _ {1}} \cap G V _ {p _ {2}} \right| / \left| G V _ {p _ {1}} \cup G V _ {p _ {2}} \right|,
$$

where $| G V _ { p 1 } \cap G V _ { p _ { 2 } } |$ | is the number of common patents in the two citation networks, and $| G V _ { p _ { 1 } } \cup G V _ { p _ { 2 } } |$ is the total number of patents in the two networks. In the graph overlap kernel, the larger the overlap part of the two citation networks, the more similar the two patents are.

Labeled Citation Graph Kernel. Finally, as our main contribution, we propose a labeled citation graph kernel (K\_Gra) which considers both the network of cited documents and the cited documents’ features. In this kernel, a patent $p$ is associated with a labeled citation network, $G _ { _ p } : = ( G V _ { _ p } , G E _ { _ p } , G L _ { _ p } ) .$ , which contains the patents directly or indirectly cited by $p { : } G V _ { p } { : }$ and the citations between all patents in $G V _ { p } { : } G$ $E _ { _ p } = \{ ( s , t ) : \forall s , t \in G V _ { _ p }$ and s cites t}. In this network, each node (patent) is labeled with its classification category: $G L _ { _ p } = \{ l a b e l ( q ) : \forall q \in G V _ { _ p } \}$ . The similarity between two patents is measured by the similarity between the labeled citation networks associated with them.

![](/api/attachments/G2MRNV5D/fulltext/images/69b1b476e9b6f08d2c5f67399c5ad9541ed9fa0577592583eed2f140582162d0.jpg)  
Figure 2. Random Walk Paths on a Labeled Citation Network Related to Patent p

In order to analyze patents using their associated labeled citation networks, the labeled citation graph kernel compares the random walk paths, starting from the focal patents on their associated labeled citation networks, and composes path similarities into the similarities of focal patents. This is different from previous graph kernel studies that target analyzing graphs, which compare random walk paths starting from any nodes in the focal graphs [26]. The random walk paths are generated from the focal patents following patent citations (Figure 2). When a random walk is conducted, it follows a probability distribution and may jump from one patent to one of its neighbors (cited documents) or stop at the patent. From a knowledge diffusion perspective, the random walk paths represent the knowledge transfer paths (reversely) from prior innovations to focal patents. In this model, a longer random walk path has a lower probability of existence, indicating that older predecessors have less impact on new innovations. In the labeled graph kernel, each random walk path is represented as a sequence of labels (i.e., classification categories) of the nodes on the paths, which partially documents the knowledge elements related to this knowledge transfer path. The similarity of two paths is considered to be one if they share identical label sequences. Otherwise, it is considered to be zero for the sake of simplicity. The labeled citation graph kernel is defined as the sum of pairwise path similarity values, which are weighed according to the probabilities these random walk paths may exist. In other words, the kernel compares all knowledge transfer paths leading to each innovation to identify patents on similar topics. The algorithm to calculate the labeled citation graph kernel is summarized in Figure 3.

## Using Individual Documents’ Content Information

The kernel that uses individual documents’ content information represents the previous efforts that used content features to address the patent classification problem. In previous studies, features extracted from patent abstracts, claims, and descriptions have all been used. Patent abstracts have been reported to be slightly more informative than other features in patent classification [32, 35]. The linear text kernel has been reported to have good classification performance [13, 14]. Therefore, we use the patent abstract to represent the entire patent content and choose the linear text kernel to capture patent content information. Such a setting works as a baseline to evaluate the performances of the citation-based kernels. In the linear text kernel, each patent p is represented by a term vector, $C _ { _ { p } } = ( t _ { _ { 1 } } , t _ { _ { 2 } } , . . . , t _ { _ { m } } )$ , where the elements are the number of occurrences of terms in the abstract. The linear text kernel (K\_Txt) defines the similarity of two patents as the normalized inner product of the term vectors [25]:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. Random path generation
(1) The random walk starts from the patent to be classified $x_0$.
(2) On node $x_i$, the random walk has a probability of $p_q(x_i)$ to stop.
(3) If the random walk does not stop, the random walk has equal probability to choose any of $x_i$'s neighbors (which is noted as $x_{i+1}$) to jump to. The probability is noted as $p_t(x_{i+1}|x_i)$.
(4) Thus a random walk path $h = \{x_0, x_1, ..., x_n\}$ has the probability $P(h|G) = p_t(x_1|x_0)p_t(x_2|x_1) ... p_t(x_n|x_{n-1})p_q(x_n)$ to exist.
2. Kernel definition
The labeled citation graph kernel is defined as a convolution kernel
$K\_Gra(G_{p_1}, G_{p_2}) = \sum_h \sum_{h'} k(h, h')P(h|G_{p_1})P(h'|G_{p_2})$
For two random walk paths $h = \{x_0, x_1, ..., x_n\}$ and $h' = \{x_0', x_1', ..., x_m'\}$
if $n &lt; &gt;m$, $k(h, h') = 0$,
else $k(h, h') = \prod_{i=1}^{n} \hat{k}(x_i, x_i')$, where $\hat{k}(x_i, x_i') = 1$ if and only if $label(x_i) = label(x_i')$.
</div>

Figure 3. The Algorithm for Labeled Citation Graph Kernels

$$
K _ {-} T x t \left(p _ {1}, p _ {2}\right) = \left\langle C _ {p _ {1}}, C _ {p _ {2}} \right\rangle / \sqrt {\left\langle C _ {p _ {1}} , C _ {p _ {1}} \right\rangle \cdot \left\langle C _ {p _ {2}} , C _ {p _ {2}} \right\rangle},
$$

where $p _ { 1 }$ and $p _ { 2 }$ represent two patents and $C _ { p _ { 1 } }$ and $C _ { p _ { 2 } }$ are their term vectors.

## Using Both Content and Citation Information

Using kernel composition methods, it is easy to consolidate different types of information by combining multiple kernels. We use the simple addition operation to combine kernels that use citation information (K\_Bib, K\_Ref, K\_Ovr, and $K \_ G r a )$ with the linear text kernel (K\_Txt) into four composite kernels $( K \_ C o m _ { _ { I } } – K \_ C o m _ { _ { 4 } } )$ . For any two kernel functions $K _ { \scriptscriptstyle 1 } ( p _ { \scriptscriptstyle 1 } , p _ { \scriptscriptstyle 2 } )$ and $K _ { \scriptscriptstyle 2 } ( p _ { \scriptscriptstyle 1 } , p _ { \scriptscriptstyle 2 } )$ , the addition operation creates a new kernel by adding corresponding kernel values: $K ( p _ { 1 } , p _ { 2 } ) = \lambda K _ { 1 } ( p _ { 1 } , p _ { 2 } ) + ( 1 - \lambda ) K _ { 2 } ( p _ { 1 } , p _ { 2 } )$ . The addition operation on the two kernels implicitly combines the feature spaces defined by them. The parameter λ controls how much each kernel contributes to the composite kernel. This set of kernels represents the efforts that exploit both patent contents and the associated knowledge evolution process.

## Experimental Study

## Test Bed

In order to ex amine th e ef ectiveness of proposed kernel functions for patent classification, we conducted an experimental study on a nanotechnology-related patent data set acquired from the United States Patent and Trademark Office (USPTO). We chose USPTO patents because they have more complete citation information than patents from other patent offices (hence, more reliable citation networks). We selected patents in a specific domain so as to restrict the size of the test bed without significantly reducing the difficulty of the patent classification task. Specifically, nanotechnology was selected due to its deep impact on a nation’s technology advancement and its rapid development in patent publication in recent years, reflecting the characteristics of many high-tech domains.

We retrieved nanotechnology-related patents from the USPTO by key word searching in patent title, abstract, and claims, using a key word list provided by domain experts [22]. The retrieved patents were parsed into structured data and stored in a relational database. We also retrieved the patents they directly or indirectly cited to reconstruct the citation network. Because the number of cited patents increases exponentially as the citation level increases, from a practical standpoint we retrieved only cited patents that are two steps away from the core set of patents. (The test bed may contain a patent’s ancestors that are more than two steps away, if it cites the patents in the core set of patents.)

We split the test bed into a training set and a testing set following previous studies [30]. Given a specific date, patents published prior to that date were used as training data, while applications filed after that date were used as testing data. The patents under review on that day, which have been applied for but have not yet been issued, were not considered in either the training or testing data set. In this research, the patents published between January 1, 1999, and December 31, 2001, were used for training. The patent applications that were filed between January 1, 2002, and December 31, 2004, were used for testing. We used a patent’s major USPC category as its classification label. To provide enough instances to train the classifier, we restricted the experiments to categories with more than 100 patents in the training data set. After preprocessing, the training data set contained 13,913 data instances and the testing data set contained 4,358 data instances (see Table 2), which belong to 36 first-level USPC categories. The number of instances in each category varied from 109 to 1,895 in the training data and from 15 to 705 in the testing data (Figure 4). The retrieved citation network of the training set contained 336,303 patents, and that of the testing set contained 227,833 patents. As there were overlap patents in these two citation networks, in total we collected 451,853 patents.

Table 2. Number of Data Instances in the Testing and Training Data Sets

<table><tr><td></td><td>Number of patents</td><td>Number of categories</td><td>Number of patents in the citation network</td><td>Number of categories in the citation network</td></tr><tr><td>Training</td><td>13,913</td><td>36</td><td>336,303</td><td>426</td></tr><tr><td>Testing</td><td>4,358</td><td>36</td><td>227,833</td><td>410</td></tr></table>

![](/api/attachments/G2MRNV5D/fulltext/images/f5851e7979ffb82cd79f24a85c9ddb307189e098c0e0bf02cd5855c8c075bd0b.jpg)  
Figure 4. Patent Distribution in USPC Categories

Our research test bed illustrates the challenges in patent classification discussed earlier. Produced by a multidisciplinary research field, nanotechnology patents cover many USPC categories [22]. Some of these patents may have minor topical differences and are difficult to differentiate. In the data set, the numbers of instances are uneven in different categories. This data set contains 36 classification categories, which is comparable to previous patent classification studies.

## Experimental Procedures

After creating the training and testing data sets, we calculated the kernel matrices that contain the kernel values between the patents in the data sets. To construct the linear text kernel matrix, we preprocessed the contents (abstracts) of the patents in the test bed using the open source package Rainbow [36] for stemming, indexing, and feature selection (based on mutual information). To construct the kernel matrices of citation information, we used the extracted citation relations and classification categories of cited patents and precomputed the kernel values according to their definitions. To construct the four composite kernels, we set λ as 0.5 and added the linear text kernel matrix to each of the four kernel matrices of citation information. We chose λ as 0.5 for consistency with past research [25], where individual documents’ content and citation information have equal effect on the final kernel matrix. It is worth knowing that parameter λ can be optimized by solving a semidefinite programming problem [31]. However, parameter optimization is out of the scope of the current research and will be considered in the future. After the precomputation of kernel matrices, we used a well-known high-performance SVM package, LIBSVM [8], to build the classification models. We classify each patent to only one class, which is considered as its major classification category. The predictions on the testing data set are used for evaluation.

## Evaluation

For each of the data instances in the testing data set, we compared the classifiers predictions with its actual classification category in the USPTO. We used standard classification performance metrics, accuracy, precision, recall, and F-measure, to evaluate the performance of different kernels with the SVM algorithm. These metrics have been widely used in information retrieval and machine learning studies.

Accuracy is usually used to assess the overall performance of a classifier at the instance level. For the instances in the testing set,

$$
\text { Accuracy } = \frac {\text { number   of   all   correctly   identified   instances }}{\text { total   number   of   instances }}.
$$

Precision, recall, and F-measure are defined to evaluate the performance of a classifier on individual classes. For a class i, if $T { P _ { i } }$ is the number of correctly identified instances of class $i , F P _ { i }$ is the number of instances incorrectly assigned to class i, and $F N _ { i }$ is the number of instances that belong to class i and have been assigned to other classes by mistake, then

Precision $P _ { _ i } { = } T P _ { _ i } / ( T P _ { _ i } + F P _ { _ i } ) .$

Recall $R _ { _ i } { = } T P _ { _ i } / ( T P _ { _ i } + F N _ { _ i } )$ , and

F-measure $F _ { _ i } { = } 2 \times P _ { _ i } { \times } R _ { _ i } / ( P _ { _ i } { + } R _ { _ i } )$ , which combines precision and recall.

The micro-average (per instance) value and macro-average (per category) value of precision, recall, and F-measure can be used to compare the kernels’ overall performances [44, 55]. Given that our experiments are designed as single-label classification, the micro-averaged precision, recall, and F-measure are equal to accuracy, which favors the categories with large numbers of instances by giving each instance the same weight. Thus, we report the macro-averaged precision, recall, and F-measure, which favor the categories with small numbers of instances since each category has the same weight.

## Hypotheses

In correspondence with the research questions, we test two sets of hypotheses to examine the effects of using citation networks in patent classification. In these hypotheses, we adopt (a) accuracy and (b) F-measure (which combines the precision and recall) to gauge the instance-level and category-level performances of different settings.

H1.1a: Kernels that use the structures of patent citation networks will outperform those that use only direct citations on classification accuracy in patent classification.

H1.1b: Kernels that use the structures of patent citation networks will outperform those that use only direct citations on F-measure in patent classification.

H1.2a: Kernels that use classification categories as cited documents’ features will outperform those that do not use any cited documents’ features on classification accuracy in patent classification.

H1.2b: Kernels that use classification categories as cited documents’ features will outperform those that do not use any cited documents’ features on F-measure in patent classification.

H2.1a: Composite kernels of citation information and patent content will outperform the linear text kernel that uses patent contents on classification accuracy in patent classification.

H2.1b: Composite kernels of citation information and patent content will outperform the linear text kernel on patent contents on F-measure in patent classification.

H2.2a: Composite kernels of citation information and patent content will outperform kernels that use only citation information on classification accuracy in patent classification.

H2.2b: Composite kernels of citation information and patent content will outperform kernels that use only citation information on F-measure in patent classification.

We conducted single-sided pairwise t-tests to test these hypotheses. The t-test on accuracy was conducted at the instance level, in which the mean of every instance’s correctness (0 or 1) is accuracy. The t-test on F-measure was conducted at the category level, in which the mean of every class’s F-measure is the macro-averaged F-measure.

## Results and Discussion

## Overall Performances

Tabl e 3 reports th e perf ormances ach ieved by the SVM classifiers with different kernels. We can observe that both the labeled citation graph kernel (K\_Gra) and its composition with the linear text kernel $( K _ { - } C o m _ { 4 } )$ have high accuracies, precisions, recalls, and F-measures. They achieve much better performances (31.12 percent and 32.29 percent absolute improvement in accuracy, respectively) than the baseline linear text kernel (K\_Txt). Considering that the linear text kernel represents the performance of content analysis (using the knowledge embedded in patents) in previous research and applications, the two kernels show good potential to be used in real applications. Both kernels utilize the network structure of patent citations and the classification category features of cited documents, which account for their good performances.

In the experiments, the bibliographic coupling kernel (K\_Bib) and the graph overlap kernel (K\_Ovr) have low accuracy values (7.48 percent and 37.13 percent, respectively). This may be a direct result of their sparse kernel matrices. The designs of these two kernels compare patent citations according to exact match. Given the millions of patents existing in the world, the probability that two patents share the same references is very low. Thus, there is a high probability that the kernel values will be zero. In our experiments, the bibliographic coupling kernel has 99.88 percent zero values and the graph overlap kernel has 98.37 percent zero values. Compared with the linear text kernel whose matrix has 38.81 percent zero values, the two kernel matrices are too sparse to capture enough information to differentiate patents and build an effective classifier.

We also noticed that the bibliographic coupling kernel (K\_Bib) and the graph overlap kernel (K\_Ovr) have much lower recalls (5.81 percent and 29.08 percent, respectively) than the other kernels, while most kernels have similar precision values (except the labeled citation graph kernel and its composition with the linear text kernel). Further inspection shows that the two kernels tend to assign most patents into certain classes by mistake. For example, the bibliographic coupling kernel assigns most instances into USPC category 435 (chemistry: molecular biology and microbiology) with a low precision. The few instances left were assigned accurately, which lead to a high precision and a very low recall in most classes. For example, the bibliographic coupling kernel has 100 percent precision in assigning a couple of instances into some categories (e.g., three instances in USPC category 073, three instances in USPC category 106, and one instance in USPC category 252).

## Hypotheses Testing

To further assess the factors that affect the performances of different kernels, we tested the hypotheses by conducting single-sided pairwise t-tests on accuracy and F-measure (Table 4). The pairwise t-tests on accuracy were conducted at the instance level $( n = 4 , 3 5 8 )$ ; the pairwise t-tests on F-measure were conducted at the class level $( n = 3 6 )$

Table 3. Performances of Different Kernels (in percent)

<table><tr><td>Kernels</td><td>Accuracy</td><td>Averaged precision</td><td>Averaged recall</td><td>Averaged F-measure</td></tr><tr><td>Bibliographic coupling kernel (K_Bib)</td><td>7.48</td><td>47.87</td><td>5.81</td><td>5.71</td></tr><tr><td>Labeled coreference kernel (K_Ref)</td><td>61.50</td><td>56.04</td><td>56.82</td><td>55.50</td></tr><tr><td>Graph overlap kernel (K_Ovr)</td><td>37.13</td><td>53.32</td><td>29.08</td><td>34.91</td></tr><tr><td>Labeled citation graph kernel (K_Gra)</td><td>86.67</td><td>89.09</td><td>87.97</td><td>88.04</td></tr><tr><td>Composite kernel 1 (K_Com1)</td><td>57.82</td><td>53.65</td><td>44.24</td><td>46.50</td></tr><tr><td>Composite kernel 2 (K_Com2)</td><td>66.02</td><td>59.43</td><td>59.14</td><td>58.78</td></tr><tr><td>Composite kernel 3 (K_Com3)</td><td>59.64</td><td>55.49</td><td>47.56</td><td>49.72</td></tr><tr><td>Composite kernel 4 (K_Com4)</td><td>87.84</td><td>89.43</td><td>86.97</td><td>87.96</td></tr><tr><td>Linear text kernel (K_Txt)</td><td>55.55</td><td>51.65</td><td>39.29</td><td>40.83</td></tr></table>

Statistical tests confirm that the kernels that use networks of patent citations significantly outperform the kernels that use only direct citations on both accuracy and F-measure (i.e., H1.1a and H1.1b are supported). Using citation networks explicates the relationship between the patents that do not share directly cited patents but share indirect ancestors. Such explications may provide more evidence when the classifiers try to categorize such patents into the same class. In addition, using citation networks differentiates the patents with similar directly cited patents more distinctly by inspecting more levels of citations. Such detailed differentiation may enable the classifiers to categorize ambiguous patents into different classes more precisely.

Statistical tests confirm that the kernels that use cited documents’ classification category features significantly outperform those that do not use any cited documents features on both accuracy and F-measure (i.e., H1.2a and H1.2b are supported). In previous research, it was found that employing neighbor documents’ classification category information can improve the classification accuracy [7, 40], which is confirmed by our experiments. Our experiments further suggest that, when the entire citation network is considered, cited documents’ features can still play an important role.

Statistical tests show that all four composite kernels significantly outperform the linear text kernel $( K \_ T x t )$ on both classification accuracy and F-measure (i.e., H2.1a and H2.1b are supported). In the statistical test to compare composite kernels with the kernels using only citation information, although the labeled citation graph kernel and its composition with the linear text kernel do not have statistically significant differences in F-measures in the testing of H2.2b $( p \approx 0 . 5 3 3 )$ , all other tests on accuracy and F-measure confirm a better performance when combining information (i.e., H2.2a is supported and H2.2b is partially supported). The statistical test results strongly suggest the complementary roles of patent citations and patent contents when used in patent classification tasks. In our experiments, the bibliographic coupling kernel (K\_Bib) and the graph overlap kernel (K\_Ovr) achieved only 7.48 percent and 37.13 percent accuracy, respectively. However, when they were combined with the linear text kernel, the classification performance improved significantly. This indicates that even though the citation information may be sparse in patents and using it alone is not very helpful, combining citation and content information can still improve the performance for patent classification.

Table 4. Hypotheses Testing for Different Kernels

<table><tr><td>p-values</td><td>(a) Pairwise t-test on accuracy</td><td>(b) Pairwise t-test on F-measure</td></tr><tr><td colspan="3">H1.1</td></tr><tr><td> $K\_Bib < K\_Ovr$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td> $K\_Ref < K\_Gra$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td colspan="3">H1.2</td></tr><tr><td> $K\_Bib < K\_Ref$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td> $K\_Ovr < K\_Gra$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td colspan="3">H2.1</td></tr><tr><td> $K\_Txt < K\_Com_{1}$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td> $K\_Txt < K\_Com_{2}$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td> $K\_Txt < K\_Com_{3}$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td> $K\_Txt < K\_Com_{4}$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td colspan="3">H2.2</td></tr><tr><td> $K\_Bib < K\_Com_{1}$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td> $K\_Ref < K\_Com_{2}$ </td><td>&lt; 0.001</td><td>&lt; 0.005</td></tr><tr><td> $K\_Ovr < K\_Com_{3}$ </td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td> $K\_Gra < K\_Com_{4}$ </td><td>0.004</td><td>0.533</td></tr></table>

## Individual Class’s Performances

We also inspected the kernels’ performances on all 36 classes. Figure 5 shows the F-measure each kernel achieved in each class. In general, the labeled citation graph kernel $( K _ { - } G r a )$ and its composition with the linear text kernel $( K _ { - } C o m _ { 4 } )$ have high performance in most of the 36 categories. However, the F-measures of the other seven kernels vary in the 36 categories, which may reduce their usability. We observe that the seven kernels’ F-measures are relatively low in a similar group of categories. Table 5 provides some examples of these categories, which are difficult to classify and have a relatively small number of training instances. Our test bed includes other categories that share similar topics with these categories and have a larger number of training instances. The classifiers have a high probability of misclassifying patents belonging to these categories into other similar categories. For example, most of the instances in USPC category 216 (etching a substrate: processes) were incorrectly assigned to category 438 (semiconductor device manufacturing: process), which has 1,119 training instances. Many of the instances in category 264 (plastic and nonmetallic article shaping or treating: processes) were assigned to category 428 (stock material or miscellaneous articles), which has 774 training instances. Many of the instances in categories 422 (chemical apparatus and process disinfecting, deodorizing, preserving, or sterilizing), 436 (chemistry: analytical and immunological testing), 530 (chemistry: natural resins or derivatives; peptides or proteins; lignins or reaction products thereof), and 536 (organic compounds—part of the class 532–570 series) were assigned to 435 (chemistry: molecular biology and microbiology), which has 1,895 training instances. Even in these categories where most other kernels fail, the labeled citation graph kernel and its composition with the linear text kernel $( K _ { - } C o m _ { 4 } )$ are highly accurate. By considering patent citation information, the two kernels have better differentiation abilities on the categories with very similar topics and uneven numbers of instances.

![](/api/attachments/G2MRNV5D/fulltext/images/e39a7979003b99c20ab124345f8947158c9321b019bdb6714d1a582370d0c826.jpg)  
Figure 5. The Kernels’ Performances in Different Classes  
Note: The circles from inside to outside represent the F-measures from 10 percent to 100 percent.

Table 5. Some of the Categories That Are Difficult to Classify

<table><tr><td>USPC category</td><td>Category description</td><td>Number of training instances</td><td>Number of testing instances</td></tr><tr><td>216</td><td>Etching a substrate: processes</td><td>124</td><td>23</td></tr><tr><td>264</td><td>Plastic and nonmetallic article shaping or treating: processes</td><td>111</td><td>33</td></tr><tr><td>422</td><td>Chemical apparatus and process disinfecting, deodorizing, preserving, or sterilizing</td><td>143</td><td>23</td></tr><tr><td>436</td><td>Chemistry: analytical and immunological testing</td><td>229</td><td>28</td></tr><tr><td>530</td><td>Chemistry: natural resins or derivatives; peptides or proteins; lignins or reaction products thereof</td><td>367</td><td>15</td></tr><tr><td>536</td><td>Organic compounds—part of the class 532–570 series</td><td>265</td><td>18</td></tr></table>

The performance of the labeled citation graph kernel (K\_Gra) and its composition with the linear text kernel (K\_Com ) also changes slightly in different categories. In Figure 5, the labeled citation graph kernel (K\_Gra) does not achieve a high performance in USPC category 435 $( F { \mathrm { - m e a s u r e } } = 5 4 . 7 1 $ percent). Although it is better than most of the other kernels in the same category, such a performance is not comparable to the performance it achieved in other categories (F-measures between 77.78 percent and 98.31 percent). USPC category 435 has the largest number of training instances in the data set and a small number of testing instances. The patents in this category are on fundamental science topics or research tools, which were heavily cited by patents in all categories [34]. These characteristics may be the cause of the low performance of the labeled citation graph kernel and other kernels in USPC category 435. However, after combining it with the linear text kernel, the composite kernel $( K _ { - } C o m _ { 4 } )$ achieves a high F-measure on USPC category 435 (81.25 percent). The composite kernel (K\_Com ) employs content features in addition to citations, which may help the classifiers differentiate the patents belonging to USPC category 435 from the others. Actually, the composite kernel (K\_Com ) achieves consistent good performance in all categories (F-measures between 74.42 percent and 96.73 percent, average F-measure 87.96 percent, standard deviation 6.53 percent). Even the labeled citation graph kernel is highly accurate; considering patent contents (linear text kernel) ensures more consistent high performance for different categories.

## Conclusions

Using patent cl assif ication as an ex ampl e, this paper demonstrates that knowledge evolution processes can be useful in KM tasks. In this research, we utilized patent citation networks, which encode evolution processes of innovations, for the classification of patent documents. Under a kernel-based framework, we designed different kernel functions to capture the information of citation networks and found that our proposed labeled citation graph kernel improved patent classification performance. Our research showed that the features of cited patents and the structure of patent citation networks, which together represent innovations’ evolution history, can benefit the classification of focal patents. We also noticed that combining the information in citation networks with patent contents results in higher and more consistent performance.

In the practice of patent management, the significant performance improvement (> 30 percent in accuracy) in our experiments indicates the good potential of using our approach in real-life patent examination applications. Previous content-based methods usually cannot match the performance of junior examiners with some basic general knowledge [30]. Our proposed approach can potentially alleviate human efforts in patent preclassification and further expedite patent examination. Our research also lends support to a policy that requires inventors to file patent citations, since they often have the more complete knowledge about their innovation’s evolution. The USPTO has adopted this policy, which may need to be considered by other patent offices.

The effectiveness of our proposed approach implies a wider application area than patent classification. The proposed approach can be directly applied to classify other linked documents, such as Web pages and scientific literature. With appropriate adaptations it is also applicable to other knowledge codification and organization tasks such as building help desk systems, decision support systems, and knowledge repositories.

In the future, we will continue theorizing the role of knowledge evolution processes in KM and studying its applications in other types of KM tasks, such as the knowledge acquisition tasks in opinion mining and topic suggestion. For patent classification, we will extend this research to more realistic settings where multiple labels on hierarchical schemes are used to codify patents.

Acknowledgments: This research is supported by the NSF: IIS-0311652 “Intelligent Patent Analysis for Nanoscale Science and Engineering” and DMI-0533749 “NanoMap: Mapping Nanotechnology Development.” The authors thank the USPTO for making their data available for research purposes.

## Ref erences

1. Almeida, P., and Kogut, B. Localization of knowledge and the mobility of engineers in regional networks. Management Science, 45, 7 (1999), 905–917.

2. Amsler, R. Application of citation-based automatic classification. Technical Report, University of Texas at Austin, Linguistics Research Center, 1972.

3. Bieber, M.; Engelbart, D.; Furuta, R.; Hiltz, S.R.; Noll, J.; Preece, J.; Stohr, E.A.; Turoff, M.; and Van de Walle, B. Toward virtual community knowledge evolution. Journal of Management Information Systems, 18, 4 (Spring 2002), 11–35.

4. Borgwardt, K.M.; Ong, C.S.; Schonauer, S.; Vishwanathan, S.V.N.; Smola, A.J.; and Kriegel, H.P. Protein function prediction via graph kernels. Bioinformatics, 21, 1 (2005), I47–I56.

5. Broder, A.; Kumar, R.; Maghoul, F.; Raghavan, P.; Rajagopalan, S.; Stata, R.; Tomkins, A .; and Wiener, J. Graph structure in the Web. Computer Networks: The International Journal of Computer and Telecommunications Networking, 33, 1–6 (2000), 309–320.

6. Calado, P.; Cristo, M.; Goncalves, M.A.; de Moura, E.S.; Ribeiro-Neto, B.; and Ziviani, N. Link-based similarity measures for the classification of Web documents. Journal of the American Society for Information Science and Technology, 57, 2 (2006), 208–221.

7. Chakrabarti, S.; Dom, B.; and Indyk, P. Enhanced hypertext categorization using hyperlinks. In A. Tiwary and M. Franklin (eds.), Proceedings of the 1998 ACM SIGMOD International Conference on Management of Data. New York: AC M Press, 1998, pp. 307–318.

8. Chang, C.-C., and Lin, C.-J. LIBSVM: A library for support vector machines. National Taiwan University, Taipei, 2001 (available at www.csie.ntu.edu.tw/\~cjlin/libsvm).

9. Craven, M., and Slattery, S. Relational learning with statistical predicate invention: Better models for hypertext. Machine Learning, 43, 1–2 (2001), 97–119.

10. Cristianini, N., and Shawe-Taylor, J. An Introduction to Support Vector Machines (and Other Kernel-Based Learning Methods). Cambridge: Cambridge University Press, 2000.

11. Cristo, M.; Calado, P.; de Moura, E.S.; Ziviani, N.; and Ribeiro-Neto, B. Link information as a similarity measure in Web classification. In G. Goos, J. Hartmanis, and J. van Leeuwen (eds.), Proceedings of the International Symposium on String Processing and Information Retrieval. Berlin: Springer, 2003, pp. 43–55.

12. Dunford, R. Key challenges in the search for the effective management of knowledge in management consulting firms. Journal of Knowledge Management, 4, 4 (2000), 295–302.

13. Fall, C.J.; Torcsvari, A.; Benzineb, K.; and Karetka, G. Automated categorization in the International patent classification. ACM SIGIR Forum, 37, 1 (2003), 10–25.

14. Fall, C.J.; Torcsvari, A.; Fievet, P.; and Karetka, G. Automated categorization of Germanlanguage patent documents. Expert Systems with Applications, 26, 2 (2004), 269–277.

15. Fleming, L. Recombinant uncertainty in technological search. Management Science, 47, 1 (2001), 117–132.

16. Gallini, N.T. The economics of patents: Lessons from recent U.S. patent reform. Journal of Economic Perspectives, 16, 2 (2002), 131–154.

17. Gartner, T. A survey of kernels for structured data. ACM SIGKDD Explorations, 5, 1 (2003), 49–58.

18. Ghani, R.; Slattery, S.; and Yang, Y. Hypertext categorization using hyperlink patterns and meta data. In C.E. Brodley and A.P. Danyluk (eds.), Proceedings of the Eighteenth International Conference on Machine Learning. San Francisco: Morgan Kaufmann, 2001, pp. 178–185.

19. Ginsparg, P.; Houle, P.; Joachims, T.; and Sul, J.H. Mapping subsets of scholarly information. Proceedings of the National Academy of Sciences of the United States of America, 101, 1 (2004), 5236–5240.

20. Haussler, D. Convolution kernels on discrete structures. Technical Report UC S-CR L-99–10, University of California at Santa Cruz, 1999.

21. Huang, M.H.; Wang, E.T.G.; and Seidmann, A. Price mechanism for knowledge transfer: An integrative theory. Journal of Management Information Systems, 24, 3 (Winter 2007–8), 79–108.

22. Huang, Z.; Chen, H.; Yip, A.; Ng, G.; Guo, F.; Chen, Z.-K.; and Roco, M.C. Longitudinal patent analysis for nanoscale science and engineering: Country, institution and technology field. Journal of Nanoparticle Research, 5, 3–4 (2003), 333–363.

23. Hull, D.; Ait-Mokhtar, S.; Chuat, M.; Eisele, A.; Gaussier, E.; Grefenstette, G.; Isabelle, P.; Samuelsson, C.; and Segond, F. Language technologies and patent search and classification. World Patent Information, 21, 3 (2001), 265–268.

24. Hunt, R.M. You can patent that? Are patents on computer programs and business methods good for the economy? Federal Reserve Bank of Philadelphia Business Review, Q1 (2001), 5–15.

25. Joachims, T.; Cristianini, N.; and Shawe-Taylor, J. Composite kernels for hypertext categorisation. In C.E. Brodley and A.P. Danyluk (eds.), Proceedings of the Eighteenth International Conference on Machine Learning. San Francisco: Morgan Kaufmann, 2001, pp. 250–257.

26. Kashima, H.; Tsuda, K.; and Inokuchi, A. Marginalized kernels between labeled graphs. In T. Fawcett and N. Mishra (eds.), Proceedings of the Twentieth International Conference on Machine Learning. Menlo Park, CA : A I Press, 2003, pp. 321–328.

27. Kessler, M.M. Bibliographic coupling between scientific papers. American Documentation, 14, 1 (1963), 10–25.

28. King, J.L. Patent examination procedures and patent quality. In W.M. Cohen and S.A. Merrill (eds.), Patents in the Knowledge-Based Economy. Washington, DC: National Academies Press, 2003, pp. 54–73.

29. Koster, C.H.A.; Seutter, M.; and Beney, J. Multi-classification of patent applications with Winnow. In M. Broy and A.V. Zamulin (eds.), Perspectives of System Informatics, vol. 2890. Berlin: Springer, 2003, 546–555.

30. Krier, M., and Zacca, F. Automatic categorization applications at the European patent office. World Patent Information, 24, 3 (2002), 187–196.

31. Lanckriet, G.R.G.; De Bie, T.; Cristianini, N.; Jordan, M.I.; and Noble, W.S. A statistical framework for genomic data fusion. Bioinformatics, 20, 16 (2004), 2626–2635.

32. Larkey, L.S. A patent search and classification system. In G. Goos, J. Hartmanis, and J. van Leeuwen (eds.), Proceedings of the Fourth ACM Conference on Digital Libraries. New York: AC M Press, 1999, pp. 79–87.

33. Le, S.Q.; Ho, T.B.; and Phan, T.T.H. A novel graph-based similarity measure for 2D chemical structures. Genome Informatics, 14, 2 (2004), 82–91.

34. Li, X.; Chen, H.; Huang, Z.; and Roco, M.C. Patent citation network in nanotechnology (1976–2004). Journal of Nanoparticle Research, 9, 3 (2007), 337–352.

35. Loh, H.T.; He, C.; and Shen, L. Automatic classification of patent documents for TRIZ users. World Patent Information, 28, 1 (2006), 6–13.

36. McCallum, A.K. Bow: A toolkit for statistical language modeling, text retrieval, classification and clustering. University of Massachusetts at Amherst, 1996 (available at www. cs.cmu.edu/\~mccallum/bow).

37. Narin, F. Patent bibliometrics. Scientometrics, 30, 1 (1994), 147–155.

38. Nerkar, A. Old is gold? The value of temporal exploration in the creation of new knowledge. Management Science, 49, 2 (2003), 211–229.

39. Nidumolu, S.R.; Subramani, M.; and Aldrich, A. Situated learning and the situated knowledge web: Exploring the ground beneath knowledge management. Journal of Management Information Systems, 18, 1 (Summer 2001), 115–150.

40. Oh, H.-J.; Myaeng, S.H.; and Lee, M.-H. A practical hypertext categorization method using links and incrementally available class information. In E. Yannakoudakis, N.J. Blekin, M. Leong, and P. Ingwersen (eds.), Proceedings of the Twenty-Third Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. New York: AC M Press, 2000, pp. 264–271.

41. Redner, S. How popular is your paper? An empirical study of the citation distribution. European Physical Journal B, 4, 2 (1998), 131–134.

42. Richter, G., and MacFarlane, A. The impact of metadata on the accuracy of automated patent classification. World Patent Information, 27, 1 (2005), 13–26.

43. Scherer, F.M. The economics of human gene patents. Academic Medicine, 77, 12 (2002), 1348–1367.

44. Sebastiani, F. Machine learning in automated text categorization. ACM Computing Surveys, 34, 1 (2002), 1–47.

45. Sinclair, G. and Webber, B. Classification from full text: A comparison of canonical sections of scientific papers. In N. Collier, P. Ruch, and A. Nazarenko (eds.), Proceedings of the 2004 International Joint Workshop on Natural Language Processing in Biomedicine and Its Applications. Geneva, Switzerland: IC L, 2004, pp. 69–72.

46. Singh, J. Collaborative networks as determinants of knowledge diffusion patterns. Management Science, 51, 5 (2005), 756–770.

47. Small, H. Co-citation in scientific literature—New measure of relationship between 2 documents. Journal of the American Society for Information Science, 24, 4 (1974), 265–269.

48. Smith, H. Automation of patent classification. World Patent Information, 24, 4 (2002), 269–271.

49. Spangler, S.; Kreulen, J.T.; and Lessler, J. Generating and browsing multiple taxonomies over a document collection. Journal of Management Information Systems, 19, 4 (Spring 2003), 191–212.

50. Stenmark, D. Leveraging tacit organizational knowledge. Journal of Management Information Systems, 17, 3 (Winter 2000–2001), 9–24.

51. Tan, Y., and Wang, J. A support vector machine with a hybrid kernel and minimal Vapnik-Chervonenkis dimension. IEEE Transactions on Knowledge and Data Engineering, 16, 4 (2004), 385–395.

52. Taskar, B.; Abbeel, P.; and Koller, D. Discriminative probabilistic models of relational data. In J. Breese and D. Koller (eds.), Proceedings of the Eighteenth Conference on Uncertainty in Artificial Intelligence. San Francisco, Morgan Kaufmann, 2002, pp. 485–492.

53. Teichert, T., and Mittermayer, M.-A. Text mining for technology monitoring. In T. Durrani (ed.), IEEE International Engineering Management Conference 2002. Los Alamitos, CA : IEEE Computer Society Press, 2002, pp. 596–601.

54. U.S. Patent Statistics Chart Calendar Years 1963–2005. U.S. Patent and Trade Office, Washington, DC, 2005 (available at www.uspto.gov/web/offices/ac/ido/oeip/taf/us\_stat.htm).

55. Yang, Y. An evaluation of statistical approaches to text categorization. Information Retrieval, 1, 1–2 (1999), 69–90.

56. Yang, Y.; Slattery, S.; and Ghani, R. A study of approaches to hypertext categorization. Journal of Intelligent Information Systems, 18, 2–3 (2002), 219–241.
