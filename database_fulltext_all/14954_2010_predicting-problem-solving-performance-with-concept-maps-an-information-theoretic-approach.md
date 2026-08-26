---
otero_id: 14954
otero_key: "DCBQUGFJ"
title: "Predicting problem-solving performance with concept maps: An information-theoretic approach"
authors: "Jin-Xing Hao; Ron Chi-Wai Kwok; Raymond Yiu-Keung Lau; Angela Yan Yu"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.12.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting problem-solving performance with concept maps: An information-theoretic approach

Jin-Xing Hao <sup>a,b,</sup>⁎, Ron Chi-Wai Kwok <sup>b</sup>, Raymond Yiu-Keung Lau <sup>b</sup>, Angela Yan Yu <sup>b</sup>

<sup>a</sup> School of Economics and Management, Beihang University, Beijing 100083, China

<sup>b</sup> Department of Information Systems, City University of Hong Kong, 83 Tat Chee Avenue, Kowloon, Hong Kong, China

## a r t i c l e i n f o

Article history: Received 21 March 2008 Received in revised form 18 August 2009 Accepted 2 December 2009 Available online 16 December 2009

Keywords: Information theory Entropy Problem solving Concept mapping Knowledge management

## a b s t r a c t

An increasing number of researchers and educational practitioners have shown their interest in the use of concept mapping techniques to elicit and represent individuals' knowledge structures. By extending previous research on concept map assessment, this study aims to develop a new evaluation metric enabling the “information uncertainty” embedded in concept maps to be assessed so as to predict individuals' problem-solving performance. In particular, our novel metric EntropyAvg is underpinned by the notion of entropy in information theory. A controlled experiment is carried out to evaluate the effectiveness of our proposed metric. Our experimental results demonstrate that the entropy values computed according to EntropyAvg strongly correlate to individuals' problem-solving performance and that the predictive power of EntropyAvg is signi<sup>fi</sup>cantly higher than that of existing widely used concept map evaluation metrics. Our research work opens the door to the application of concept mapping techniques in enterprise-wide knowledge management in general and enterprise-wide knowledge assessment in particular.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Knowledge structure (or cognitive structure) refers to a set of concepts and the relationships among such concepts [12,28]. The presence of certain knowledge structures in individuals' memories largely determines their ability to characterize a particular problem domain and their problem-solving performance [2]. Several mapping techniques such as concept maps [24], causal maps [4,20], and mind maps [5] have been developed to elicit implicit knowledge structure from an individual's memory. Among these mapping techniques, concept mapping is unique in the sense that concepts and propositions play the central role in the representation of knowledge structures and the construction of meanings [26].

Assimilation theory is generally considered the theoretical foundation of the concept mapping technique [2,25]. According to assimilation theory, new knowledge is acquired by linking novel concepts to the existing concepts of a knowledge structure. Both the newly acquired and the existing knowledge structures are modi<sup>fi</sup>ed during a learning process. The construction of a concept map through hierarchical organization, progressive differentiation, and integrative reconciliation shapes an individual's ability to assimilate and integrate knowledge and solve problems creatively. Accordingly, certain properties such as the structure and content of the concept map constructed can be used to predict an individual's problem-solving performance [2,18,31,37]. As the structural elements are the main building blocks of a concept map, it is technically feasible to develop a formal computational model to estimate the quality of the concept map based on its structural elements. This paper focuses on the design and development of a novel concept map evaluation metric to quantitatively measure the information uncertainty implied in the structural elements of a concept map. Information uncertainty can be quanti<sup>fi</sup>ed in terms of entropy [33].

Previous research has highlighted that assessing the quality of a concept map based on its structural properties is a promising approach [18,31,37]. Accordingly, several important evaluation metrics have been developed to examine the structural properties of concept maps [1,14,16,18,37]. Among these metrics, most of them extend or adapt the scoring method proposed by Novak and Gowin [26]. For example, the number of hierarchical levels presented in a concept map can be used to measure the degree of subsumption among concepts; the number of branchings from a concept node can be used to measure an individual's ability in progressive differentiation; the number of crosslinks presented in a concept map indicates an individual's ability in knowledge integration. Essentially, the concept map metrics of complexity and integration refer to the hierarchical levels of and the number of cross-links presented in the concept map [16]. The literature also frequently refers to the concept map metrics of density and centrality [1].

The existing concept map evaluation metrics are useful in distinguishing between expert knowledge and novice knowledge based on the knowledge structures encoded in concept maps. However, these metrics are not effective in measuring the psychometric properties of concept maps as an assessment tool to predict individuals' problemsolving performance. Although reliability and validity measures have been applied to evaluate the psychometric properties of concept maps, these measures are often the integral part of the concept mapping tasks and their effectiveness has been validated solely in the context of science teaching and learning [34]. From the problem-solving perspective, the search for a path which reduces information uncertainty in the solution space provides an essential guiding principle for the development of an effective solution for addressing the given problem [7,22,27]. Therefore, measuring the entropy (i.e., information uncertainty) attached to a concept map is likely to be a promising approach in predicting an individual's problem-solving performance. To the best of our knowledge, the research work reported in this paper represents the <sup>fi</sup>rst attempt to employ an entropy-based metric to evaluate the quality of concept maps. By assessing the entropy attached to a concept map, it is possible to infer the cognitive state of the individual who draws it; hence, the entropy-based metric we propose can be used to predict the individual's problem-solving performance.

The greatest potential bene<sup>fi</sup>ts of our proposed methodology will be realized when it is applied to ill-de<sup>fi</sup>ned problem domains. In general, a problem consists of three abstract elements: an initial state, a terminal state, and an operation (process) which transforms the initial state to the terminal state [30]. For well-de<sup>fi</sup>ned problems, because these three elements can easily be identi<sup>fi</sup>ed, the problemsolving process involves little uncertainty. However, for ill-de<sup>fi</sup>ned problems, the boundary between the initial state and the terminal state is vague, and the transformation process is not obvious. As a result, uncertainty arises during the problem-solving process. According to this observation, our proposed entropy-based concept map evaluation metric is quite applicable to predicting individuals' problem-solving performance for ill-de<sup>fi</sup>ned problems such as recruiting the most suitable employees. The main reason for this is that our proposed metric can effectively quantify information uncertainty, which is the key feature characterizing the problemsolving process for ill-de<sup>fi</sup>ned problems.

This study makes both theoretical and practical contributions. From the theoretical perspective, this study provides a better understanding of the structural properties of concept maps from the lens of entropy. Our entropy-based evaluation metric captures an important dimension of concept maps, that is, the information uncertainty which is implicitly embedded in concept maps. By quantifying the information uncertainty attached to the structural elements of a concept map, it is possible to infer the perceived uncertainty of the individual who draws the map. Based on the quanti<sup>fi</sup>ed entropy of the concept map, a prediction can then be made regarding the individual's problem-solving performance. As for its practical implications, our study contributes to the development of an effective methodology for predicting individuals' problem-solving performance based on the entropy embedded in their concept maps. Our novel concept map evaluation metric can also be applied to largescale automated knowledge assessment exercises which expand the traditional application areas of concept mapping tools.

The rest of the paper is organized as follows. In Section 2, we elaborate the theoretical foundation that underpins the development of the entropy-based concept map evaluation metric. Our controlled experiment to evaluate the entropy-based metric proposed is described in Section 3. In Section 4, we report our experimental results and discuss some of our <sup>fi</sup>ndings. We offer concluding remarks and describe the future direction of our research work in the <sup>fi</sup>nal section.

## 2. The theoretical foundation of concept map evaluation

Nodes and links are the basic components of a concept map. Nodes with designated labels represent concepts, which describe regularities of events or prominent objects within a problem domain. On the other hand, each link connecting a pair of nodes denotes the relationship between concepts. Each node-link-node triplet forms a proposition which provides a meaningful statement about certain objects or events. Nodes and links are arranged in a hierarchical fashion. As illustrated in Fig. 1, the key concept of a problem domain (i.e., the root node) can be represented by a hierarchy of nodes starting from a high level of abstraction (e.g., general concepts) to a low level of abstraction (e.g., speci<sup>fi</sup>c concepts). For instance, the key concept of “System” can be represented by general concepts such as “Arti<sup>fi</sup>cial system”, “Social system”, etc. “Arti<sup>fi</sup>cial system” can be represented by more speci<sup>fi</sup>c concepts such as “Computer system”. A branch of a concept map represents a speci<sup>fi</sup>c knowledge domain (e.g., “Computer system”). Links relate concepts that belong to the same branch. They are useful for de<sup>fi</sup>ning general concepts in terms of more speci<sup>fi</sup>c concepts. Cross-links, on the other hand, relate concepts from different branches (e.g., a cross-link connecting “Computer system” with “Social system” to de<sup>fi</sup>ne a new concept, “Socio-technical system”). They are useful for representing meaningful relationships across different knowledge domains.

In the following sub-sections we <sup>fi</sup>rst provide the formal notations used to describe a concept map. We then illustrate the information theory, which underpins the development of the novel entropy-based concept map evaluation metric we propose.

## 2.1. The formal notations for concept maps

According to the de<sup>fi</sup>nition of a concept map proposed by Novak and Gowin [26], each concept map can be taken as the abstraction of a “hierarchical graph”, that is, a graph with a hierarchical structure. The formal notation used to describe the structural properties of a concept map is derived from the graph theory, as follows:

(1) A concept map is taken as a hierarchical directed graph, C;

(2) Every domain concept is represented by a node or vertex, v, of the hierarchical directed graph C; the set of all the nodes of C is represented by $V { = } \{ \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { n } \}$ , with only one root node designated as $\nu _ { 1 } \in V ;$

(3) The relationship between a pair of concepts is represented by an edge, e, which is formally de<sup>fi</sup>ned by an ordered pair of two nodes such as $( \nu _ { 1 } , \nu _ { 2 } ) ;$ the set of all the edges of C is represented by $E = \{ e _ { 1 } , e _ { 2 } , . . . , e _ { m } \} ;$

(4) The number of edges that have node v as their terminal node is called the indegree of v, in (v), and the number of edges that have node v as their initial node is called the outdegree of v, out (v). If out (v) is 0, we say that node v is a leaf node; otherwise, node v is an intermediate node;

![](/api/attachments/DCBQUGFJ/fulltext/images/6045e56975ea49af6f734457994ca74e60fc2dcda9381d2176e0c2ccfc1e1416.jpg)  
Fig. 1. The structure of a concept map (adapted from [12]).

According to the formal notations based on the graph theory, the sample concept map depicted in Fig. 1 can be plotted as a hierarchical directed graph, as shown in Fig. 2. Moreover, the hierarchical directed graph can be formally de<sup>fi</sup>ned by:

$$
\begin{array}{r l} & C = (V, E), \\ & V = \{v _ {1}, v _ {2}, \dots , v _ {6} \}, E = \{e _ {1}, e _ {2}, \dots , e _ {6} \}, \\ & e _ {1} = (v _ {1}, v _ {2}), e _ {2} = (v _ {1}, v _ {3}), e _ {3} = (v _ {2}, v _ {4}), e _ {4} = (v _ {2}, v _ {5}), e _ {5} = (v _ {5}, v _ {6}), \\ & e _ {6} = (v _ {3}, v _ {6}). \end{array}
$$

(5) A branch of a concept map is seen as a sub-tree of the hierarchical directed graph. For example, node set $\{ \boldsymbol { v } _ { 2 } ,$ v , v , v } with edge set $\{ e _ { 3 } , e _ { 4 } , e _ { 5 } \}$ comprises one branch, and node set {v } with edge set ∅ forms another branch;

(6) A cross-link joins two branches. In the case of a cycle, we consider the direction of the cross-link from the parent node to the child node. In Fig. 2, the edge $e _ { 6 }$ which comprises the ordered pair from $\nu _ { 3 }$ to $\boldsymbol { v } _ { 6 }$ is a cross-link.

## 2.2. An information-theoretic concept map evaluation methodology

Concept mapping is a technique used to elicit and represent an individual's implicit knowledge structure. Our assumption is that the individual's problem-solving ability can be predicted on the basis of the structural properties encoded in his or her concept maps. Prior research has demonstrated that the structural properties of a concept map complexity and integration can be used as the key metrics to predict an individual's learning performance [13,16]. The structural properties of complexity and integration can re<sup>fl</sup>ect the individual's achievement in progressive differentiation and integrative reconciliation, which are two important elements of meaningful learning processes. Progressive differentiation refers to a continuous meaningful learning process in which greater inclusiveness and the speci<sup>fi</sup>city of concepts are discerned and more propositional links with other related concepts are identi<sup>fi</sup>ed. In contrast, integrative reconciliation occurs when an individual recognizes new relationships between related sets of concepts or propositions and integratively reconciles these new ideas based on old ones [26].

However, problem solving is not simply a learning process in which new knowledge is assimilated based on an individual's existing knowledge structure. In practice, problem solving requires an individual to utilize his or her knowledge to reduce the uncertainty of a problem space and identify an effective solution from the reduced solution space. Although the concept mapping technique has been applied to predict individuals' learning performance, the existing indictors such as complexity (the extent to which a learner can identify relevant and meaningful relationships among the concepts from the same concept hierarchy) and integration (the extent to which a learner can identify relevant relationships among the concepts that belong to different levels of hierarchies and abstraction) cannot measure the inherent characteristics of a problem domain, such as uncertainty. According to a previous study, complexity and integration do not offer suf<sup>fi</sup>cient explanatory power to analyze an individual's problem-solving performance [31]. This study thus aims to <sup>fi</sup>ll this gap in the extant concept map evaluation research by developing a metric that can be used to measure the uncertainty present in concept maps and analyze and predict individuals' problem-solving performance.

![](/api/attachments/DCBQUGFJ/fulltext/images/5ea7c23dfc088aa4f961e8d784a9a6408e8abcf0050aa866b5bf938dbef55416.jpg)  
Fig. 2. The formal representation of a concept map.

Problem solving refers to any activity in which both the cognitive representation of prior experience and the components of a current problem situation are reorganized to achieve a designated objective [2]. Problem solving consists of both knowledge assimilation and knowledge application [35]. Effective problem solving requires the transformation and re-integration of an individual's existing knowledge to <sup>fi</sup>t the speci<sup>fi</sup>ed means–end relationships which underpin the solution of a problem space. Successful problem solvers can focus on the prominent aspects of a problem and ignore its irrelevant aspects. Following such a rationale, problem solving can be viewed as a kind of information processing which can produce relevant outputs by reducing information uncertainty and distraction during the input– output transformation process [7,22,27].

To illustrate the notion of information uncertainty in the concept mapping context, we provide the two examples depicted in Figs. 3 and 4, respectively. Given a pair of concept maps with the same levels of complexity (i.e., number of nodes) and integration (i.e., number of crosslinks), the degree of information uncertainty and disorder can vary among these maps. For instance, information uncertainty increases when a broad thinking process is adopted, resulting in width extension and depth condensation during concept mapping. In contrast, information uncertainty decreases when deep thinking occurs, leading to width condensation and depth extension during concept mapping. Broad thinking focuses on the comprehensive understanding of a problem domain, whereas deep thinking leads to the development and justi<sup>fi</sup>cation of solutions to problems. The concept maps depicted in Figs. 3 and 4 have the same levels of complexity and integration. However, the degree of information uncertainty in the concept map shown in Fig. 4 is higher than that in the concept map depicted in Fig. 3. The concept map shown in Fig. 3 has a narrower and deeper structure than that of the concept map shown in Fig. 4; this implies that the creator of the former map focuses more on deep thinking. Despite the importance of gaining a comprehensive understanding of a problem domain, deep thinking contributes more toward the development of solutions to a particular problem, consequently leading to a reduction in information uncertainty [36]. Therefore, we believe that individuals who construct concept maps with deep structures (less information uncertainty) are more likely to outperform individuals who produce concept maps with broad structures, because the former have already acquired the knowledge required to focus on speci<sup>fi</sup>c issues related to the given problem.

![](/api/attachments/DCBQUGFJ/fulltext/images/fb77e8ef8d5920442bdc4a92de0dc61b1115db6dc81cdb21f61365c488c08741.jpg)  
Fig. 3. A concept map with a deep knowledge structure.

![](/api/attachments/DCBQUGFJ/fulltext/images/6bb09b750505ac6c6e53a6e1ee1f44712566c1556a8ccfb828385249f2d17617.jpg)  
Fig. 4. A concept map with a broad knowledge structure.

For the quantitative assessment of the information uncertainty present in concept maps, we refer to information theory and the notion of entropy in particular [33]. In the concept mapping context, each node or edge represents the semantics of a particular problem domain as perceived by the concept map creator. Each node can be viewed as an information item which is associated with uncertainty. The basic intuition is that the information uncertainty of a concept map represents the aggregation of the uncertainties associated with all the nodes. According to Shannon's entropy theory [33], the information uncertainty of an information item (e.g., a message) is inversely proportional to the probability of the event described by the information item. It is believed that the number of outgoing links of a concept can provide additional information regarding the concept's role in a particular concept map [17]. An event can thus be seen as the process of following the outgoing links from one concept to traverse to another concept. Therefore, the probability of transition from one concept (i.e., node v ) to one of its associated concepts (i.e., node $\nu _ { j } )$ can be estimated as the proportion calculated by dividing the number of child nodes of $v _ { j }$ (includes v ) by the total number of all child nodes of $\nu _ { i \cdot }$ Formally, the probability of the state transition of node $\nu _ { i }$ is de<sup>fi</sup>ned by:

$$
\operatorname * {P r} (v _ {i} \to v _ {j}) = \frac {p}{q},\tag{1}
$$

where $p$ is the number of child nodes of $v _ { j }$ (includes v ) and $q$ is the number of all child nodes of v . Our proposed approach for estimating the information uncertainty embedded in concept maps can be understood on the basis of the decision tree building process. For example, the objective of building a decision tree is to reduce the entropy (uncertainty and disorder) used for classifying an input dataset. The classi<sup>fi</sup>cation process starts at the root node (e.g., the highest entropy) and continues until one of the lead nodes which classify all the instances of one class (e.g., zero entropy). As can be seen, the entropy is progressively reduced at each level of the decision tree. The decision tree building process in which the appropriate nodes which lead to the reduction of entropy are found contributes to effective problem solving [8,29].

Based on Eq. (1), the following equation is developed to estimate the information entropy of an arbitrary node v in a concept map:

$$
E _ {v} = \left\{ \begin{array}{l l} \sum_ {i = 1} ^ {r} - \frac {p _ {i}}{q} \log_ {2} \left(\frac {p _ {i}}{q}\right) & \text { if   v   is   an   intermediate   node } \\ 0 & \text { if   v   is   a   leaf   node } \end{array} \right.,\tag{2}
$$

where

r is the number of branches of node v;

$p _ { i }$ is the number of nodes in the ith branch of node v; and

q is the total number of child nodes of node v, $q = \sum _ { i = 1 } ^ { } p _ { i } .$

The entropy-based evaluation metric for an arbitrary map can be developed by computing the average entropy, EntropyAvg, for all the non-leaf nodes of the concept map:

$$
E A = \frac {\sum_ {i = 1} ^ {n} E _ {v i}}{n - l},\tag{3}
$$

where

n is the total number of nodes in the map; and l is the total number of leaf nodes in the map.

Using Eq. (3) to compute the EntropyAvg of the concept maps depicted in Figs. 3 and 4, respectively, the following results are obtained (only the non-zero E is shown):

$$
E A _ {\text { Figure   3 }} = \frac {E _ {v _ {1}} + E _ {v _ {2}}}{1 2 - 4} = \frac {0 . 6 8 4 + 1 . 5 0 0}{8} = 0. 2 7 3;
$$

and

$$
\begin{array}{r l} E A _ {\text { Figure   4 }} & = \frac {E _ {v _ {1}} + E _ {v _ {2}} + E _ {v _ {3}} + E _ {v _ {7}}}{1 2 - 7} = \frac {0 . 8 4 5 + 1 . 1 4 9 + 1 + 1 . 5 8 5}{5} \\ & = 0. 9 1 6. \end{array}
$$

According to the computational results, the EntropyAvg of these concept maps shows a great difference although their complexity and integration are the same. the concept map shown in Fig. 3 has a lower EntropyAvg score than that of the concept map depicted in Fig. 4; the former map shapes a deep knowledge structure, while the latter map demonstrates a broad knowledge structure. The proposed metric is a promising tool for quantifying the uncertainty embedded in concept maps, and hence for predicting individuals' problem-solving performance. However, it is essential to conduct empirical tests to support our claim. We propose the following two hypotheses to verify the proposed metric empirically:

(1) the EntropyAvg scores derived from concept maps are highly correlated to the subjects' actual problem-solving performance; and

(2) the EntropyAvg metric provides signi<sup>fi</sup>cantly higher predictive power than the existing metrics.

## 3. Empirical evaluation

## 3.1. Overview of the experimental design

We conducted a controlled laboratory experiment to examine the predictive power of the proposed entropy-based concept map evaluation metric. The whole experiment took approximately 55 min to <sup>fi</sup>nish; it included a training session and a test session. In the test session, participants were asked to solve a choice dilemma problem by independently drawing a concept map using paper and pencil and submitting a choice of actions and a qualitative summary report to explain their choices. A group of two external assessors who were blind to the aim and design of the experiment were told to transform all the concept maps drawn by the subjects to a standardized format according to the principles of concept propositional analysis [26]. The assessors then entered the standardized concept maps into our concept map evaluation system. At the same time, another group of two external assessors evaluated the summary reports according to a pre-de<sup>fi</sup>ned rubric to determine the subjects actual problem-solving performance. Our concept map evaluation system was used to calculate the scores automatically according to several concept map evaluation metrics (e.g., EntropyAvg, complexity, and integration, etc.). The computational results were exported to

SPSS for further data analysis and to verify the correlation between certain evaluation metrics and the participants' problem-solving performance.

## 3.2. Participants

A total of 40 undergraduate students enrolled in an introductory management information systems course voluntarily participated in this experiment. The participants' average age was around 21 and there was an even gender distribution (i.e., half male and half female). To encourage participation and involvement in the problem-solving task assigned, incentives were provided in the form of cash prizes for participation (US\$15) and an extra bonus (US\$15) for the top problemsolving performance. The students were assured that their participation in the experiment and their problem-solving performance would not affect their course grades.

## 3.3. Training

As the participants' experience and elementary skills in concept mapping could facilitate our experimental process, all participants were exposed to concept mapping techniques in lectures and tutorials for one semester before the experiment began. Furthermore, a training session was provided to all participants so that their skill levels were similar for the speci<sup>fi</sup>c content-free concept mapping technique. The content-free concept mapping technique, which is derived from the general concept mapping technique, emphasizes the structural properties of concept maps rather than their contents [32]. The training session lasted for 15 min and comprised: (1) a facilitator explaining the meanings of nodes, links, and cross-links based on a sample concept map (5 min); (2) all participants being required to conduct an exercise by drawing a concept map for a simple topic (7 min); and (3) conducting a quiz about the usage of concept maps to test the participants' pro<sup>fi</sup>ciency in concept mapping (3 min).

## 3.4. Task and procedure

A choice dilemma task [9] was assigned to the participants. This particular task involved an ill-de<sup>fi</sup>ned problem with no obvious initial states, terminal states, or transformation processes. The task concerned an expanding insurance broking <sup>fi</sup>rm which planned to recruit a customer services assistant for its front counter (refer to Appendix A for more details). The participants were asked to decide which applicant should be offered the job. In the event that no applicant met the job requirements, they had to decide whether or not the vacancy should be re-advertised.

The main test session lasted for about 40 min and involved the following activities: (1) a facilitator brie<sup>fl</sup>y introduced the case including the requirements of the job, the background of the candidates who had been interviewed, and the interviewer's written comments (5 min); (2) the participants were asked to de<sup>fi</sup>ne and describe all related aspects of the recruitment case (15 min); (3) each participant was told to draw a concept map to illustrate the prominent issues in the recruitment case; the concept map was a re<sup>fl</sup>ection of the individual's knowledge structure for the given problem domain (10 min); and (4) each participant was asked to write a short report to summarize the factors justifying his or her choice and draw a conclusion (10 min).

## 3.5. Experimental control

Prior studies have identi<sup>fi</sup>ed several sources of errors in concept mapping experiments, including the concept map construction method used, variations in the participants' concept mapping pro<sup>fi</sup>ciency, and variations in the assessors' domain knowledge [18,31]. Accordingly, we developed appropriate procedures to minimize the in<sup>fl</sup>uence of these sources of errors.

(1) Control on the concept map construction method used. There are various methods for students to construct their own concept maps. In this study, we adopted the content-free concept map construction method used in prior studies [21,32]. The contentfree concept map construction method is designed primarily to assess the structure of a concept map rather than its content. Because concept maps are idiosyncratic, it is necessary to standardize the contents of concept maps to assess their structural properties. Speci<sup>fi</sup>cally, we employed the following procedure to minimize the degree of variation caused by the map construction method used:

a) we provided the participants with a set of standard concepts with corresponding labels;

b) the participants were asked to use the set of standard labels and focus on the structural properties of the concepts (e.g., positioning and linking of the concepts). To avoid constraining the participants' thoughts on the given concepts, the participants were allowed to identify new concepts and create corresponding concept labels; and

c) two assessors standardized the new concept labels the participants identi<sup>fi</sup>ed with each concept using a unique concept ID number; the assessors then entered all the standardized concept maps into our prototype system, where further concept map veri<sup>fi</sup>cation was conducted.

(2) Control on the participants' concept mapping proficiency. As noted in Section 3.3, we provided all the participants with appropriate training on the content-free concept map construction technique to ensure that they had an acceptable level of pro<sup>fi</sup>ciency in the technique.

(3) Control on the assessors' domain knowledge. We employed two groups of assessors in this experiment. Each group consisted of two assessors who were blind to the aim and design of the experiment. The <sup>fi</sup>rst two assessors were the concept mapping experts who were responsible for transforming the concept maps drawn by the participants into a standard format according to the principles of concept propositional analysis [26]. In particular, they converted the new concept labels developed by the participants into a set of standard concept labels and entered the standardized concept maps into our prototype system. The level of agreement on concept map encoding was 0.93, indicating an adequate inter-rater reliability. The remaining differences in concept map encoding were resolved through discussions between the two assessors.

The two assessors of the second group were human resource management professionals; they were responsible for assessing the participants' summary reports according to the adapted rubric extracted from the structure of the observed learning outcome (SOLO) taxonomy [3]. SOLO is a framework widely used for assessing the quality of answers given to open-ended problems [10]. James et al.'s [11] interrater reliability $r _ { w g }$ was used to evaluate the assessors' judgment and a result of 0.89 was obtained. The $r _ { w g }$ result indicated adequate agreement between the two assessors. The remaining differences in the assessment results were resolved via discussions between the two assessors. The high inter-rater reliability for each group of assessors reveals that there was little variation among the assessors. The con<sup>fl</sup>ict resolution procedures used also helped reduce the impact of the variations in the assessors' domain knowledge on the experiment results.

## 3.6. Prototype system

A prototype system for concept map analysis was developed using Visual Basic and Microsoft® Access. This prototype system adopted both the proposed concept map evaluation metric and other existing evaluation metrics. Fig. 5 graphically illustrates the architecture of our prototype system. The concept maps the participants drew were <sup>fi</sup>rst reviewed by the assessors before being entered into a Microsoft® Access database according to the schema (link\_ID, starting\_concept\_ID, ending\_concept\_ID, whether\_cross-link). Based on the manually entered concept map data, the prototype system generated a concept map according to the formal notations described in Section 2.1. The systemgenerated concept maps served two purposes. The <sup>fi</sup>rst was to verify the input data with reference to the concept maps generated. For example, if the system-generated concept map was not a connected graph, this indicated that certain relationships among the concepts had been entered mistakenly, and therefore that it was necessary to verify the original concept map data. The second purpose of the generated concept maps was to provide a basis for computing evaluation scores according to the pre-de<sup>fi</sup>ned concept map evaluation metrics. The prototype system developed includes <sup>fi</sup>ve evaluation metrics: EntropyAvg, complexity, integration, density, and centrality. The corresponding evaluation scores derived from these metrics were stored in a table and could easily be exported to SPSS for statistical data analysis. Our prototype system operates quite ef<sup>fi</sup>ciently, taking an average of around one second to generate a concept map and compute the corresponding evaluation score once the concept map data have been entered by an assessor.

![](/api/attachments/DCBQUGFJ/fulltext/images/d5a646574ae5d17bfbb9803070b541f704832fcfa26fa1f2f4c979fc2c12bb95.jpg)  
Fig. 5. The architecture of the prototype system for concept map analysis.

## 3.7. Measures

This experiment was aimed at testing the predictive power of the proposed entropy-based evaluation metric (EntropyAvg). More speci<sup>fi</sup>cally, we sought to examine the incremental predictive power of EntropyAvg by controlling the other two pairs of evaluation metrics: complexity and integration [16], as well as density and centrality [1]. Complexity is measured in terms of the number of direct links appearing in a concept map; it re<sup>fl</sup>ects an individual's comprehensiveness and differentiation during the articulation and elaboration of knowledge structure. Integration is measured by the number of crosslinks in a concept map; it re<sup>fl</sup>ects the interconnectedness and integration of knowledge structure by an individual [16]. Density and centrality are evaluation metrics developed on the basis of social network analysis. Density is calculated as the ratio of the total number of links to the total number of concepts in a concept map. It indicates the degree of connection among the concepts included in a map. Centrality re<sup>fl</sup>ects the extent to which a map is centralized and cohesive. It is the sum of each individual concept's centrality, which is measured in terms of the number of incoming and outgoing links to and from the concept. All of these metrics were applied to each concept map and the correlations of the corresponding quality scores and the subjects' problem-solving performance analyzed.

The assessors evaluated an individual's problem-solving performance based on his or her summary report. The rubric for performance assessment was adapted from the SOLO taxonomy [3,15]. Two external assessors examined the justi<sup>fi</sup>cations in each summary report and assigned a score for each justi<sup>fi</sup>cation ranging from 1 to 3 (where 1=marginal justi<sup>fi</sup>cation: the subject justi<sup>fi</sup>ed his or her decision without giving a relevant explanation; 2=good justi<sup>fi</sup>cation: the subject justi<sup>fi</sup>ed his or her decision with a brief explanation; and 3=excellent justi<sup>fi</sup>cation: the subject justi<sup>fi</sup>ed his or her decision with a very clear and detailed explanation). Any statement which was irrelevant to the given recruitment task was not considered as a justi<sup>fi</sup>cation. Each justi<sup>fi</sup>cation and explanation of the subject's decision given in the summary report was evaluated and scored individually; a <sup>fi</sup>nal score was then computed to represent the subject's problemsolving performance.

## 4. Experimental results and discussions

In this study, hierarchical regression analysis [6] was used to test the main hypotheses given in Section 2. The con<sup>fi</sup>dence level of pb0.05 was adopted as the acceptance criterion for our hypotheses. The statistical data were carefully examined to ensure the hierarchical regression assumptions were satis<sup>fi</sup>ed. One observation identi<sup>fi</sup>ed as an outlier according to most of the attribute values for the observation was thus excluded from further analysis. This left us with a total of 39 valid observations. The effects of demographic variables, such as gender and age, were also examined before we began testing the main hypotheses. These demographic variables were insigni<sup>fi</sup>cantly correlated to individuals' problem-solving performance.

To assess the effectiveness of the proposed evaluation metric, we utilized descriptive statistics and a correlation matrix of all the variables to examine its basic predictive power. We then employed hierarchical regression analysis to examine the incremental predictive power of the proposed metric in comparison with that of two pairs of predictors used in previous studies. As described above, these two pairs of predictors which we used as baseline measures were, respectively, complexity and integration, which are regarded as measures of the fundamental properties of a concept map, and density and centrality, which are underpinned by social network analysis.

Table 1 shows the descriptive statistics and the correlation matrix for the dependent variable (performance) and the predictive variables. Our proposed evaluation metric, EntropyAvg, was shown to have signi<sup>fi</sup>cant correlation with the dependent variable performance (r=−0.43, pb0.01). This result con<sup>fi</sup>rms the basic predictive power of our proposed metric. EntropyAvg was found to be weakly correlated to other metrics such as complexity (r = 0.11), integration (r = 0.14), and density $( r { = } 0 . 1 4 )$ . These results demonstrate that in assessing concept maps, the proposed metric captures an entirely different dimension to those captured by complexity and integration. Moreover, the high correlation between integration and density implies that these metrics measure largely similar properties of concept maps. Both of these metrics focus on the cross-links and interconnections among the nodes of a concept map. Nadkarni and Narayanan [19] observe that the density of a concept map corresponds to its integration.

Descriptive statistics and correlation matrix of the variables involved.

<table><tr><td></td><td>Mean</td><td>S.D.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1. Performance</td><td>14.87</td><td>7.43</td><td>—</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. EntropyAvg</td><td>0.71</td><td>0.14</td><td> $-0.43^{***}$ </td><td>—</td><td></td><td></td><td></td><td></td></tr><tr><td>3. Complexity</td><td>13.10</td><td>1.61</td><td> $-0.23^{*}$ </td><td>0.11</td><td>—</td><td></td><td></td><td></td></tr><tr><td>4. Integration</td><td>1.50</td><td>0.24</td><td> $0.32^{**}$ </td><td>0.14</td><td> $0.28^{*}$ </td><td>—</td><td></td><td></td></tr><tr><td>5. Centrality</td><td>0.30</td><td>0.07</td><td> $-0.36^{**}$ </td><td> $0.49^{***}$ </td><td>-0.19</td><td>-0.03</td><td>—</td><td></td></tr><tr><td>6. Density</td><td>1.28</td><td>0.09</td><td> $0.38^{**}$ </td><td>0.14</td><td>-0.08</td><td> $0.89^{***}$ </td><td>0.07</td><td>—</td></tr></table>

N = 39, <sup>\*</sup>p b 0.1, <sup>\*\*</sup>p b 0.05, <sup>\*\*\*</sup>p b 0.01 (2-tailed test).

To examine the predictability of the proposed metric, EntropyAvg, we constructed three hierarchical regression models for performance by introducing three clusters of control variables separately. Table 2 summarizes our empirical results.

Model 1 controlled for the effects of the fundamental structural properties of a concept map, i.e., complexity and integration. Consistent with prior studies [13,26], performance was signi<sup>fi</sup>cantly related to complexity $( \beta = - 0 . 3 5 ,  p { < } 0 . 0 5 )$ and integration $( \beta = 0 . 4 2 ,  p { < } 0 . 0 1 )$ . More importantly, our results demonstrated that EntropyAvg was signi<sup>fi</sup>cantly related to performance $( \beta = - 0 . 4 6 , p { < } 0 . 0 1 )$ ). Furthermore, EntropyAvg signi<sup>fi</sup>cantly increased the explanatory power of the variance in performance $( \Delta \bar { R } ^ { 2 } = 0 . 2 0 5 , ~ p < 0 . 0 \bar { 1 } )$ ). These results imply that EntropyAvg explains 20.5% more of the variance in problem-solving performance than that explained solely by complexity and integration. The signi<sup>fi</sup>cant improvement in $R ^ { 2 }$ after incorporating the EntropyAvg variable strongly supports its predictability and complementarity to the complexity and integration metrics in predicting problem-solving performance.

Model 2 controlled for the effects of centrality and density in testing the additional predictive power of EntropyAvg for individuals' problemsolving performance. The results showed that the predictive variable EntropyAvg was signi<sup>fi</sup>cantly correlated to performance $( \beta = - 0 . 3 9 , p \small { < } 0 . 0 5 )$ and explained an additional 11.3% of the variance in performance.

We further tested the predictive power of EntropyAvg based on Model 3, in which the effects of complexity, integration, and centrality were controlled. in this model, EntropyAvg together with the other three predictive variables explained 47% of the total variance in performance. As noted above, both integration and density are metrics designed to measure the interconnection of a concept map, although the methods used to compute these metrics vary. Rather than using density, we selected integration as one of the controlling variables. Taking this approach allowed us to avoid the potential problem of multicollinearity when both of these variables are included in regression analysis. Again, EntropyAvg was signi<sup>fi</sup>cantly correlated to problem-solving performance, with a magnitude of −0.32; it explained an additional 7.2% of the variance in problem-solving performance after controlling for the other three predictive variables.

Hierarchical regression on performance.

<table><tr><td rowspan="3">Predictor</td><td colspan="6">Dependent variable: problem-solving performance</td></tr><tr><td colspan="2">Model 1</td><td colspan="2">Model 2</td><td colspan="2">Model 3</td></tr><tr><td>Step 1</td><td>Step 2</td><td>Step 1</td><td>Step 2</td><td>Step 1</td><td>Step 2</td></tr><tr><td>Complexity</td><td>-0.35**</td><td>-0.31**</td><td></td><td></td><td>-0.43***</td><td>-0.38***</td></tr><tr><td>Integration</td><td>0.42***</td><td>0.47***</td><td></td><td></td><td>0.43***</td><td>0.47***</td></tr><tr><td>Centrality</td><td></td><td></td><td>-0.39***</td><td>-0.20</td><td>-0.44***</td><td>-0.27*</td></tr><tr><td>Density</td><td></td><td></td><td>0.40***</td><td>0.45***</td><td></td><td></td></tr><tr><td>EntropyAvg</td><td></td><td>-0.46***</td><td></td><td>-0.39**</td><td></td><td>-0.32**</td></tr><tr><td>R2</td><td>0.216**</td><td>0.421***</td><td>0.294***</td><td>0.407***</td><td>0.398***</td><td>0.470***</td></tr><tr><td>Adjusted R2</td><td>0.173**</td><td>0.372***</td><td>0.255***</td><td>0.356***</td><td>0.347***</td><td>0.408***</td></tr><tr><td>ΔR2</td><td></td><td>0.205***</td><td></td><td>0.113**</td><td></td><td>0.072**</td></tr></table>

N=39, <sup>\*</sup>pb0.1, <sup>\*\*</sup>pb0.05, <sup>\*\*\*</sup>pb0.01.

One of our interesting <sup>fi</sup>ndings was that the relationship between centrality and performance became insigni<sup>fi</sup>cant or marginally significant when EntropyAvg was added to Models 2 and 3, respectively. EntropyAvg, which measures the uncertainty embedded in a concept map, is somewhat similar to the metric of centrality in that both of these metrics evaluate the hierarchical structure of concept maps. Nevertheless, there is also a fundamental difference between these metrics. While the centrality of a concept map emphasizes the cohesive concepts it presents, it fails to capture the clarity of each hierarchical layer. In contrast, EntropyAvg re<sup>fl</sup>ects the extent to which a concept map comprises clear or ambiguous multiple hierarchical layers. In the problem-solving context, it seems that the reduction of uncertainty (ambiguity) in successive hierarchical layers makes an important contribution to the discovery of effective solutions. According to our experimental results, EntropyAvg is more effective than centrality for the prediction of problem-solving performance, indicating the merit of our entropy-based approach in comparison with the network analysis-based metric.

Based on our empirical tests using three regression models, Entro-$p y A v g$ is negatively correlated to individuals' problem-solving performance. This <sup>fi</sup>nding corresponds to our basic intuition in problem solving. For example, the degree of information uncertainty embedded in a concept map indicates the extent to which an individual is uncertain how to distinguish some concepts from others. Individuals with a high degree of information uncertainty perform comparatively poorly in problem-solving tasks. Most prior research focuses on analyzing the complexity and integration of a concept map, metrics which re<sup>fl</sup>ect individuals' divergent and convergent thinking, respectively. Nevertheless, little attention is paid to the nature of problem solving, which involves the progressive reduction of information uncertainty during solution development. As this study shows, the shift in an individual's thinking from divergence to convergence is re<sup>fl</sup>ected by the reduction of information uncertainty in the perceived problem space (as represented by the corresponding concept map). Our study sheds light on the fundamental nature of problem solving: reducing information uncertainty by focusing on the most prominent aspects of the given problem. From a practical perspective, we have successfully developed an entropy-based metric that can be used to evaluate the quality of concept maps, which re<sup>fl</sup>ect individuals' cognitive states during problem solving. By gaining better insights into an individual's cognitive state, it is possible to predict the individual's problem-solving performance more accurately. Our research work <sup>fi</sup>lls a gap in the existing concept map evaluation research in general and in the application of concept mapping techniques to predict human problem-solving performance in particular.

As for the fundamental structural properties of concept maps, it was interesting to <sup>fi</sup>nd that integration was positively correlated to individuals' problem-solving performance, whereas complexity was negatively correlated to problem-solving performance. According to assimilation theory [2], integration (the number of cross-links) represents the interconnectedness of a concept map and shapes an individual's cognitive ability in “integrative reconsolidation”. Such cognitive ability is believed to improve an individual's problemsolving performance in general [2]. In contrast, the negative correlation found between complexity and performance in this study needs to be interpreted with caution.

Some researchers have argued that because complexity re<sup>fl</sup>ects the extent of an individual's divergent thinking, the more complex the concept map is, the better the individual's problem-solving performance is likely to be [19]. Divergent thinking involving the recognition of a variety of concepts may be appropriate at the initial stage of problem solving because it helps an individual develop a better understanding of the problem situation. However, such divergent thinking may also increase the level of information uncertainty in the perceived problem space. An individual's ability to <sup>fi</sup>nd an effective solution for a problem does not always depend on how comprehensively the individual understands the problem situation [2]. The more complex the individual's knowledge structure, the less likely the individual will identify the most important issues during the problem diagnosis stage [23]. Consequently, it is more dif<sup>fi</sup>cult for the individual to develop an effective solution for the given problem. Therefore, increasing the complexity of an individual's knowledge structure may actually jeopardize his or her problem-solving performance. As demonstrated by our study, the shift from divergent to convergent thinking, which leads to the reduction of information uncertainty, is crucial at the <sup>fi</sup>nal stage of problem solving.

## 5. Conclusions and future work

Based on the notion of entropy in information theory, we have developed a novel concept map evaluation metric we call EntropyAvg. The proposed metric can be used to measure a unique property (i.e., information uncertainty) which is not captured by existing concept map evaluation metrics. The potential for using our concept map evaluation metric to predict human problem-solving performance has been explored. Our experimental results show that the proposed metric is highly effective in predicting individuals' problem-solving performance, particularly for ill-de<sup>fi</sup>ned problems such as employee recruitment. Our research outcomes have signi<sup>fi</sup>cant practical implications. For instance, our metric could be applied to assess the level of innovation in a business process according to the degree of information uncertainty embedded in concept maps which characterize the prominent aspects of the business process in question. As a whole, our proposed metric can be applied to enterprise-wide knowledge management in general, especially to enterprise-wide knowledge assessment.

We should note several limitations of our study. Firstly, the subjects in our experiment were undergraduate students who had little experience in human resources acquisition. As a result, their concept maps might include a higher level of uncertainty than is usual among human resources professionals. In future studies, we will extend our empirical tests by inviting human resources managers to participate in experiments. Secondly, due to the limited nature of the straightforward problem addressed in our experiment, we will evaluate our entropybased metric across a wider range of scenarios based on both ill-de<sup>fi</sup>ned and well-de<sup>fi</sup>ned real-world problems in the future. Finally, because it may take time for individuals to develop cognitive processes involving a shift from divergent thinking to convergent thinking, a more rigorous evaluation procedure will be implemented to assess the concept maps drawn by subjects at different stages of the problem-solving process.

## Acknowledgements

The authors thank three anonymous referees for their valuable comments and suggestions. The work described in this paper is supported by a Teaching Development Grant, no. 6000177 and a Strategic Research Grant, no. 7001899 of the City University of Hong Kong.

## Appendix A. The problem-solving case — employee recruitmen

An expanding insurance broking <sup>fi</sup>rm wants to recruit a customer services assistant for its front counter. The <sup>fi</sup>rm has put the following recruitment advertisement in a newspaper.

## CUSTOMER SERVICES ASSISTANT

Young customer services assistant needed for front counter in a friendly insurance broking office.

You will be the sort of person who likes a variety of challenges and a busy day. You will find yourself handling telephone calls and personal enquiries via our electronic terminals; advising customers on the range of services we offer, and handling cash and checks. In addition, you will carry out routine office administration and general word processing duties.

We are looking for someone who is 18+, with a good educational background in English and mathematics, and accurate typing. Full training will be offered for our word processing application and database systems — MS Word and MS Access. You will need to have a pleasant, outgoing personality and be capable of working as a member of a team whose workload can be quite hectic at times. In return, we provide an attractive salary, an annual bonus, free life insurance, a profit sharing pension scheme, and 20 days' annual holidays.

<table><tr><td>Amanda Chan</td><td>John Wong</td><td>Natalie Chong</td></tr><tr><td>Age: 18</td><td>Age: 20</td><td>Age: 19</td></tr><tr><td>Education: Undergraduate</td><td>Education: Bachelor&#x27;s Degree In IT</td><td>Education: College Graduate</td></tr><tr><td>Qualifications: Grade B in Hong Kong Certificate of Education English Exam and Grade C in Hong Kong Certificate of Education Mathematics Exam</td><td>Qualifications: Grade E in Hong Kong Advanced Supplementary Level in Use Of English and Diploma in Business and Finance</td><td>Qualifications: Grade B in Hong Kong Certificate of Education English Exam and Grade C in Hong Kong Certificate of Education Mathematics Exam</td></tr><tr><td>Typing speed: 30 wpm</td><td>Typing speed: 60 wpm</td><td>Typing speed: 40 wpm</td></tr><tr><td>Hobbies: Swimming Carpentry</td><td>Hobbies: Computers Volleyball</td><td>Hobbies: Scuba diving Horse riding</td></tr></table>

All the three applicants were called in for an interview. During the interviews, the owner of the <sup>fi</sup>rm made the following notes:

Amanda Chan: Very hesitant; never looks you straight in the eye; dirty <sup>fi</sup>ngernails.

John Wong: Quiet but con<sup>fi</sup>dent; rather serious.

Natalie Chong: Very pleasant manner; smiles a lot; expensive clothes.

According to your assessment, which applicant should be offered the job, or should the vacancy be re-advertised? Explain your reasons in details.

## References

[1] D.J. Armstrong, Causal mapping: a discussion and demonstration, in: V.K. Narayanan, D.J. Armstrong (Eds.), Causal Mapping for Research in Information Technology, Idea Group Publishing, Hershey PA 2005.

[2] D.P. Ausubel, J.D. Novak, H. Hanesian, Educational Psychology: a Cognitive View, Holt, Rinehart and Winston, New York, 1978.

[3] J.B. Biggs, K.F. Collis, Evaluating the Quality of Learning: the SOLO taxonomy Longman, New York, 1982.

[4] J. Bryson, F. Ackermann, C. Eden, C. Finn (Eds.), Visible Thinking: Unlocking Causal Mapping for Practical Business Results, Wiley, Chichester, 2004.

[5] T. Buzan, B. Buzan, The Mind Map, Plume, New York, 1996.

[6] J. Cohen, P. Cohen, S.G. West, L.S. Aiken, Applied Multiple Regression/Correlation Analysis for the Behavioral Sciences 3 ed. Lawrence Erlbaum Associates Mahwah N.J., 2003

[7] R.L. Daft, N.B. Macintosh, A tentative exploration into the amount and equivocality of information processing in organizational work units, Administrative Science Quarterly 26 (1981) 207–224.

[8] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Academic Press, Orlando FL, 2000.

[9] R. Huggett, Business Case Studies, Cambridge University Press, Cambridge, 1990

[10] B.W. Imrie, Assessment for learning: quality and taxonomies, Assessment and Evaluation in Higher Education 20 (2) (1995) 175–189.

[11] L.R. James, R.G. Demaree, G. Wolf, Estimating within-group interrater reliability with and without response bias, Journal of Applied Psychology 69 (1) (1984) 85–98.

[12] D.H. Jonassen, K. Beissner, M. Yacci, Structural Knowledge: Techniques for Representing, Conveying, and Acquiring Structural Knowledge, Lawrence Erlbaum Associates Publishers, Hillsdale, NJ, 1993.

[13] M. Khalifa, R.C.W. Kwok, Remote learning technologies: effectiveness of hypertext and GSS, Decision Support Systems 26 (3) (1999) 195–207.

[14] I.M. Kinchin, D.B. Hay, A. Adams, How a qualitative approach to concept map analysis can be used to aid learning by illustrating patterns of conceptual development, Educational Research 42 (1) (2000) 43–57.

[15] R.C.W. Kwok, M. Khalifa, Effect of GSS on knowledge acquisition, Information & Management 34 (1998) 307–315.

[16] R.C.W. Kwok, J. Ma, D. Vogel, Effects of group support systems and content facilitation on knowledge acquisition, Journal of Management Information Systems 19 (3) (2002–3) 185–229.

[17] D.B. Leake, A. Maguitman, T. Reichherzer, Understanding knowledge models: modeling assessment of concept Importance in concept maps, The Twenty-sixth Annual Conference of the Cognitive Science Society, 2004.

[18] J. McClure, B. Sonak, H. Suen, Concept map assessment of classroom learning: reliability, validity and logistical practicality, Journal of Research in Science Teaching 36 (1999) 475–492.

[19] S. Nadkarni, V.K. Narayanan, Validity of the structural properties of text-based causal maps: an empirical assessment, Organizational Research Methods 8 (1) (2005) 9–40.

[20] V.K. Narayanan, D.J. Armstrong (Eds.), Causal Mapping for Research in Information Technology, Idea Group Publishing, Hershey, PA, 2005.

[21] K.M. Nelson, S. Nadkami, V.K. Narayanan, M. Ghods, Understanding software operations support expertise: a revealed causal mapping approach, MIS Quarterly 24 (3) (2000) 475–507.

[22] A. Newell, H. Simon, Human Problem Solving, Prentice Hall, Englewood Cliffs, NY, 1972.

[23] S.E. Newstead, R.A. Griggs, Thinking about THOG: sources of error in deductive reasoning problem, Psychological Research 54 (1992) 299–305.

[24] J.D. Novak, Learning, Creating, and Using Knowledge: Concept Maps™ as Facilitative Tools in Schools and Corporations, Lawrence Erlbaum, Mahwah, NJ, 1998.

[25] J.D. Novak, A.J. Canas, The theory underlying concept maps and how to construct and use them, Technical Report IHMC CmapTools 2006-01 Rev 01-2008, FloridaInstitute for Human and Machine Cognition, 2008.

[26] J.D. Novak, D.N. Gowin, Learning How to Learn, Cambridge Univ. Press, Cambridge, U.K., 1984.

[27] S. Postrel, Islands of shared knowledge: specialization and mutual understanding in problem-solving teams, Organization Science 13 (3) (2002) 303–320.

[28] P.F.W. Preece, Mapping cognitive structure: a comparison of methods, Journal of Educational Psychology 68 (1) (1976) 1–8.

[29] M.R. Quillian, Semantic memory, in: M. Minsky (Ed.), Semantic Information Processing, MIT Press. Cambridge. MA. 1968.

[30] W.R. Reitman, Cognition and Thought: an Information Processing Approach, Wiley, New York, 1965.

[31] M. Ruiz-Primo, R.J. Shavelson, Problems and issues in the use of concept maps in science assessment, Journal of Research in Science Teaching 33 (6) (1996) 569–600.

[32] M. Ruiz-Primo, R.J. Shavelson, M. Li, S.E. Shchultz, On the validity of cognitive interpretations of scores from alternative concept-mapping techniques, Educational Assessment 7 (2) (2001) 99–141.

[33] C.E. Shannon, A mathematical theory of communication, Bell System Technical Journal 27(7.10) (1948) 379-423. 623-656.

[34] R.J. Shavelson, M.A. Ruiz-Primo, On the psychometrics of assessing science understanding, in: J.J. Mintzes, J. Wandersee, J.D. Novak (Eds.), Assessing Science Understanding, Academic Press, San Diego, 2000, pp. 304–341.

[35] R.J. Sternberg, T. Ben-Zeev, Complex Cognition: The Psychology of Human Thought, Oxford University Press, Oxford, 2001, p. 145.

[36] L.H.T. West, P.J. Fensham, J.E. Garrard, Describing the cognitive structures of learners following instruction in chemistry, Cognitive Structure and Conceptual Change, Academic Press, Orlando, FL, 1985.

[37] Y. Yin, J. Vanides, M.A. Ruiz-Primo, C.C. Ayala, R.J. Shavelson, Comparison of two concept-mapping techniques: implications for scoring, interpretation, and use, Journal of Research in Science Teaching 42 (2) (2005) 166–184.

![](/api/attachments/DCBQUGFJ/fulltext/images/5813105e82aeb5a71a806c49f930c9d34291b6b414c2b50d9304652076920b26.jpg)

Dr. Jin-Xing Hao has received his Ph.D. in Business Information Systems from the City University of Hong Kong and Master in Informatics from Wuhan University. His research interests include Business Intelligence and Analytics, Knowledge Management, e-Learning and Social Search.

![](/api/attachments/DCBQUGFJ/fulltext/images/75cc097d88b7c17521b9e1c4c3a158ba6bf27dabd7ab5eaf88bdd5e2dbefe53f.jpg)

Dr. Ron Chi-Wai Kwok is an Associate Professor in the Department of Information Systems at the City University of Hong Kong. His research interests include technology mediated learning, electronic collaborative games in education, fuzzy GSS, EC collaboration, and e-leadership.

![](/api/attachments/DCBQUGFJ/fulltext/images/a0d2d62dad08abe62486e5276c19b4b9bcf458edacff8959007efe302c6cef90.jpg)

Dr. Raymond Lau, is an Assistant Professor in the Department of Information Systems at the City University of Hong Kong. His research interests include Information Retrieval, Text Mining, and Agent-Mediated e-Commerce. He is a Senior Member of the JEFE and the ACM respectively.

Dr. Angela Yan Yu received her Ph.D. in Information Systems from the City University of Hong Kong in 2009. She received her Master in Management from Peking University in 2005 and received her Dual Bachelor degree in Information Management and Economics from Peking University in 2002. Her research interests include e-Learning, Social network, Virtual community and Enterprise Knowledge Management.

![](/api/attachments/DCBQUGFJ/fulltext/images/f750251cd7a7481d158550181088a5ae4780a152287caed63625e52c9b47ffd4.jpg)
