---
otero_id: 19882
otero_key: "M735A7UZ"
title: "A collaborative decision support system for multi-criteria automatic clustering"
authors: "Mona Jabbari; Shaya Sheikh; Meysam Rabiee; Asil Oztekin"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113671"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A collaborative decision support system for multi-criteria automatic clustering

![](/api/attachments/M735A7UZ/fulltext/images/eab53d099a87c813eba88c5e9c155313271b9a6dc6a9e7f536ab8a755b614c76.jpg)

Mona Jabbari <sup>a</sup>, Shaya Sheikh <sup>b</sup>, Meysam Rabiee <sup>c,\*</sup>, Asil Oztekin <sup>d</sup>

<sup>a</sup> Department of Finance, School of Business, Providence College, Providence, RI, 02918, USA

<sup>b</sup> School of Management, New York Institute of Technology, New York, NY 10023, USA

<sup>c</sup> Lundquist College of Business, University of Oregon, Eugene, OR, USA

<sup>d</sup> Department of Operations & Information Systems, Manning School of Business, University of Massachusetts Lowell, Lowell, MA 01854, USA

## A R T I C L E I N F O

Keywords: Automatic clustering Evolutionary algorithm Multi-objective DEA BWM

## A B S T R A C T

Automatic clustering is a challenging problem, especially when the decision-maker has little or no information about the nature of the dataset and the criteria of interest. There is a lack of generalizability in the current validity indexes (VI) for automatic clustering algorithms, as each considers a limited number of objectives and mostly ignores the other aspects of clustering validation. The proposed framework benefits from collaboration among selected evolutionary algorithms. A mixed-integer non-linear programming model is developed, and a framework is proposed for a six-step decision support system to solve it. The decision-maker (DM) selects the quantitative (primary) VIs and the evolutionary algorithms. Given DM's knowledge on the dataset and VIs, DM can incorporate qualitative (secondary) VIs. DM determines the quality threshold for each VI and runs the evolutionary algorithms separately. The DSS then saves the best obtained value of VIs in order to prepare the input necessary to construct the aggregated function. Based on the selected primary VIs, a new normalized aggregated function is developed and solved repeatedly using the randomly selected or predefined weights of importance. Eventually, DM employs a proper DEA model to define the final clustering output among all possible solutions. Given multiple efficient solutions, the best-worst method and a multi-criteria decision-making approach are applied to find the final output. The applicability of the proposed approach is illustrated on a synthetic and two secondary datasets, and the result at each step is discussed in detail.

## 1. Introduction

Data clustering, also referred to as cluster analysis or unsupervised classification, is the science of assigning data to groups called clusters in which the members of each cluster have the highest similarity (i.e., cohesion) and data in different clusters are quite distinct (i.e., separa tion). In other words, any clustering algorithm is designed based on the trade-off between cohesion and separation. Clustering has been applied by researchers and practitioners in a wide range of applications such as personalized recommendations [1], retail telecommunications [2], forecasting of demand profiles [3], creditworthiness in banking [4], determination of a patient’s risk [5], distribution networks for vaccines [6], segmentation of a pickup and delivery network [7], and pricing of insurance premiums [8].

There are two approaches to clustering: classic clustering, where the number of clusters is a predetermined parameter; and automatic clustering, where the number of clusters is a decision variable that needs to be optimized. One fundamental issue in cluster analysis is deter mining the number of clusters because this has a substantial effect on the clustering results. Determining a suitable number of clusters becomes more difficult in several situations: when the dataset has a large number of dimensions, when the clusters are different in terms of density, size, and shape, or when there is an inherent overlap in clusters. Hence, setting an appropriate value to this parameter is a challenging task for any clustering algorithm [9,10]. Another fundamental issue in cluster analysis is mimicking the behavior of a living organism in such a task. Finally, the presence of subjectivity in clustering needs to be addressed in details. The proposed framework gives us more insights into this seemingly inherent limitation.

Each automatic clustering algorithm has two main outputs: the number of clusters, and the obtained partitions. To validate these out puts, researchers have developed validity indices (VIs) that can be categorized as either external (extrinsic), internal (intrinsic), or relative. Each of these VIs measures the goodness of fit based on the index’s predetermined criteria, which usually assumes a particular geometric structure in the obtained partitions. However, in reality, some datasets can have different cluster structures and the decision-maker has more than one objective while finding the best partition. With such a dataset and multiple objectives, the vast majority of current algorithms and VIs have been bound to fail [9]. We discuss these metrics in detail in section 2.1.

Although there are numerous algorithms for classic clustering, this is not the case for automatic clustering. Here, we focus on multi-objective evolutionary clustering approaches (MOEA) that generates a set of nondominated solutions. In general, obtaining the final solution from these clustering solutions is achieved through one of the methods of inde pendent criteria approach, knee prunning approach, or cluster ensemble approach [16]. Independent criteria approach utilizes an independent VI or a heuristic to find the best clustering solution. Saha and Bandyo padhyay [9] applied a distinctive misclassification VI to identify the best solution from Pareto-optimal solutions. Their method is beneficial for datasets with overlapping clusters and hyper-spherical or symmetrical shapes while the embedded semi-supervised method identifies best so lution from the Pareto-optimal solutions. Wang et al. [14] applied NSGA-II for automatic clustering that minimizes the number of clusters and the sum of squared distances (SSD) between data points and their cluster centroids. Kuo and Zulvia [15] incorporated Pareto ranking assignment to sort the vectors based on their fitness values. Although their method outperforms other evolutionary algorithms, it may not perform well with non-uniform distributions. Dutta et al. [16] utilized nine cluster VIs for finding the best solution from the non-dominated solutions for numeric and categorical datasets with missing features. One drawback of their method is that it only captures spherically shaped clusters. A handful of other papers have applied independent criteria approach [13,27,35–37].

In the knee approach, the objective is to select a solution in which the change of one objective value triggers the maximum change on the other objective, see [12,38,49]. For instance, Handl and Knowles [38] developed a multi-objective clustering technique that is capable of handling clusters with hyperspherical or well-separated structure. The drawbacks reported by authers are in handling data sets with over lapping clusters or dealing with big data.

In the cluster ensemble approach, the motivation is to combine this information of different VIs to obtain a single clustering solution. Barak and Mokfi [11] developed a multi-criteria decision-making (MCDM) framework to evaluate and rank the partitions obtained by six clustering methods, five external VIs and two internal VIs, three MCDM methods and one final aggregating method. Zhu et al. [34] proposed an ensemble strategy for explicit/implicit knowledge discovery to guide the auto matic clustering. Liu et al. [12] proposed a knee-pruning fuzzy ensemble method for MOEA that handles high dimensional clustering problems with no user-defined coefficients. Yin et al. [41] suggested a discrete particle swarm optimization method using normalized mutual infor mation, module degree, and convergence as VIs. Authors reported higher effectiveness and efficiency in modularity for their proposed method. The cited MOEA articles have particular goals that cannot be easily generalized to all multi-objective clustering approaches. Our proposed framework is an attempt to fill this gap.

Multiple-criteria decision making (MCDM) is a process that system atically helps a decision-maker to define a decision-making problem, identify the most important criteria and the preferences of the DM over a set of predefined alternatives, and finally recommend some steps to rank the alternatives. Data envelopment analysis (DEA) is one of the most applied tools among researchers and practitioners in the field of deci sion making where it preprocesses the data and measures the relative efficiency of decision-making units (DMUs). In this setting, DEA’s inputs are VIs whose minimum values are preferred, and DEA’s outputs are the validity indices that are to be maximized. These inputs and outputs VI are usually modeled in ratio form in DEA, e.g., the CCR model proposed by Charnes, Cooper, and Rhodes [17]. For instance, Olanrewaju et al. [18,19] used ANN results as DEA input to rank the results. DEA has also been used to preprocess the data and to identify efficient alternatives. The weights of the criteria play an essential role in any MCDM problem, and they directly affect the MCDM’s output.

Clustering outputs can be utilized as input for other methods in a decision support framework. For example, Irarr´azaval et al. [44] developed a novel DSS for addressing traffic pumping. Authors began by categorizing possible fraud cases into distinct clusters and then used the clustering output as the input to the decision tree method to extract guidelines for identifying cases that involved filing lawsuits against suspicious cases. Biswas et al. [45] presented an empirical method for determining the factors that influence the number of customer reviews received by shared-home.

The abbreviations used in this paper are listed in Table 1. To the best of our knowledge, there is a lack of a generalizable framework for automatic clustering in a way that reflects the DM’s considerations. To address this gap, we develop a comprehensive framework by selecting four VIs: number of clusters, CS index, DB index, and SH index. Since using only one evolutionary algorithm may provide biased results, three evolutionary algorithms (genetic algorithm, particle swarm optimiza tion, and harmony search) were selected to be used as an embedded collaborative information-sharing feature. The list of contributions in this paper is shown here:

• A mixed-integer non-linear programming model (MINLP) is devel oped for the studied problem. This model has three unique features: i. New aggregated validity index (VI). This is the first model to offer a new normalized and multiplication-based aggregated function as a single utility score, to simultaneously consider the quality characteristics of clusters during the search process of developed algorithms.

ii. Generalizability. The model is compatible with any type of VI with any range.

iii. Minimum expectation. The model incorporates the DM’s expec tation for the quality of VIs as a threshold for the final output.

• A novel collaborative multi-objective evolutionary decision support system is used. The advantage of collaborative evolutionary algo rithms over isolated evolutionary algorithms are discussed in details.

• The concept of primary and secondary objectives (or secondary VIs) is proposed for the first time in the literature on automatic clustering.

• An MCDM framework based on DEA and BWM is proposed to eval uate and rank the partitions obtained by algorithms.

Our proposed framework is the only framework in the literature that utilizes all the features in Table 2. We compare the following papers by answering to these six questions: Q . Does framework include both quantitative and qualitative VIs? Q .Does framework include VI threshold? $Q _ { 3 } .$ Does framework work without DM’s expertise on the dataset? $\mathrm { Q } _ { 4 } .$ Can framework deliver Pareto frontier (i.e., handle more than two VIs)? Q . Does framework have an aggregate function? $\scriptstyle Q _ { 6 } .$ Does framework deliver a unique solution as the best partitioning? Q7. Does framework benefit from a collaborative strategy?

Table 1 List of abbreviations.

<table><tr><td>ANN: Artificial Neural Network</td><td>MC: Multi-Criteria</td></tr><tr><td>BWM: Best-Worst Method</td><td>NFS: Number of Feasible Solutions</td></tr><tr><td>CCR: Charnes, Cooper, and Rhodes</td><td>NOC: Number of Clusters</td></tr><tr><td>DB: Davies and Bouldin</td><td>NRU: Normalized Reciprocal Utility</td></tr><tr><td>DEA: Data Envelopment Analysis</td><td>NSGA-II: Non-Dominated Sorting Genetic Algorithm</td></tr><tr><td>DM: Decision Maker</td><td>II</td></tr><tr><td>DMU: Decision-Making Units</td><td>NUI: Normalized Utility Index</td></tr><tr><td>DSS: Decision Support System</td><td>PSO: Particle Swarm Optimization</td></tr><tr><td>GA: Genetic Algorithm</td><td>SH: Silhouette</td></tr><tr><td>HM: Harmony Memory</td><td>SSB: Sum of Squared Error Between Clusters</td></tr><tr><td>HS: Harmony Search</td><td>SSD: Sum of Squared Distances</td></tr><tr><td>MCDM: Multi-Criteria Decision Making</td><td>VC: Visual Compactness</td></tr><tr><td rowspan="2">MINLP: Mixed-Integer Nonlinear Programming Model</td><td>VI: Validity Index</td></tr><tr><td>VN: Visual Connectedness</td></tr></table>

Table 2  
Feature comparison of multi-objective clustering papers.

<table><tr><td>Article</td><td>Solution approach</td><td> $Q_1$ </td><td> $Q_2$ </td><td> $Q_3$ </td><td> $Q_4$ </td><td> $Q_5$ </td><td> $Q_6$ </td><td> $Q_7$ </td></tr><tr><td>[9]</td><td>Independent criteria</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>[11]</td><td>Ensemble</td><td></td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td></tr><tr><td>[12]</td><td>Ensemble &amp; knee pruning</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>✓</td><td></td></tr><tr><td>[15]</td><td>Independent criteria</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>[16]</td><td>Independent criteria</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>[38]</td><td>Knee pruning</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>[41]</td><td>Ensemble</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td>[49]</td><td>Knee pruning</td><td></td><td></td><td></td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>Current Paper</td><td>Ensemble</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

The remainder of this paper is organized as follows. Section 2 elab orates on the studied problems and the proposed mathematical model. Section 3 provides all the details of the developed framework. Section 4 implements the developed framework on a synthetic dataset, to show its capability and applicability. Section 5 summarizes the findings and suggests several paths for future research.

## 2. Problem description

A data point in a real problem could be physical coordinates or an abstract structure created by objects. Each data point in a clustering problem is distinguishable by its values in a set of features. Let $Y = \{ Y _ { 1 } ,$ $Y _ { 2 } , . . . , Y _ { I } \}$ be a set of I data points withJ features each. Any data point is shown by a data matrix $Y _ { I \times J }$ with J-dimensional row vectors. $\overrightarrow { Y _ { i } }$ char acterizes the $i ^ { t h }$ object in the setY, and each element $Y _ { i \times j }$ in the $\overrightarrow { Y _ { i } }$ vector corresponds to the $j ^ { t h }$ component $( j = 1 , . . . , | J | )$ of the $i ^ { \dot { t } h }$ data point $( i =$ $1 , . . . , | I | )$ . Given $Y = \{ Y _ { 1 } , Y _ { 2 } , . . . , Y _ { I } \}$ , an automatic clustering algorithm tries to partition these I data points such that its objective function is being optimized. An output of automatic clustering algorithms is |I| data points that are partitioned into $| K |$ groupsG $\dot { \mathbf { \theta } } = \{ G _ { 1 } , G _ { 2 } , . . . , G _ { | K | } \}$ . Since the number of clusters in an automatic clustering problem is a decision variable, |K| can take any integer value between 1 and |I|. So the min imum of clusters is one, and the maximum number of clusters is|I|. The number of feasible solutions (NFS) for any automatic clustering problem is found using Eq. 1:

$$
N F S = 1 + \binom{| I |}{2} + \dots + \binom{| I |}{| I | - 1} + 1 = 1 + \frac {| I | (| I | - 1)}{2} + \dots + | I | + 1\tag{1}
$$

This problem finds the optimal solution for the mathematical objective that evaluates the goodness of partitions. Brucker [20] proved that any clustering problem is NP-hard when the number of clusters is more than three. Since the number of clusters in our study can be any number and having a large data set results in an uncountable number of feasible solutions, the automatic clustering problem will be NP-hard. In this paper, we develop a decision support system for automatic clus tering using a novel collaborative multi-criteria evolutionary approach. This new framework merges any set of VIs into a single score, Before presenting the mathematical model, we briefly review the VIs used for cluster analysis and then review several forms of normalizing aggre gated functions.

## 2.1. Validity indices

The quality of a clustering algorithm is examined using the quality of a single cluster (cohesion or homogeneity) and the interrelationship among clusters (separation). The criterion for cohesion and the criterion for separation are different, depending on the application. These are examples of the criterion for cohesion: minimizing the within-cluster dissimilarities, maximizing the members of any cluster that is repre sented by its centroid, and maximizing the similarity of clusters’ shape into a convex shape. These are examples of the criterion for separation: maximizing the between-cluster dissimilarities and minimizing the standard deviation of the size of clusters.

The output of any clustering algorithm includes a partition of the dataset into clusters with a unique spatial structure. Many VIs have been developed to analyze the results provided by clustering algorithms. These VIs are categorized into three groups:

• External measures such as Hubert’s Correlation, which compares the property of a cluster against true clusters (if any exist);

• Internal measures such as Dunn index [21], Davies and Bouldin (DB) [22], Silhouette (SH) [23], and CS [24], use the spatial distribution and the cluster labels to calculate the properties of generated clusters;

• Relative measures such as Figure of Merit [25] and Stability [26] compute an algorithm’s consistency by comparing the output pro vided under different conditions.

Although the primary goal of the DM in this paper is exploratory data analysis, and there is no true cluster available as a benchmark, our framework can be used for external and relative measures as well as any combination of VIs. If any clustering algorithm corresponds exactly to the criterion of interest, there is no point for further investigation on the method. However, this is not the case in the following situations:

• When the purpose of clustering cannot be fully matched with a specific clustering method.

• When the DM who is in charge of clustering has little or no infor mation over the criterion of interest (exploratory data analysis). This situation is common when the number of clusters is not pre determined and is itself a decision variable in the problem (e.g., automatic clustering).

• When the DM has more than one criterion in place. Even if there are algorithms that can be translated into these criteria, each of these algorithms mostly focuses on one criterion and ignores (or discounts) others. Therefore, there is still confusion for the DM in selecting the most appropriate algorithm.

In this research, a framework is developed to address the above sit uations. The next section describes the ways researchers use to merge several VIs into a single measure.

## 2.2. Normalization methods

Normalizing values of VIs makes it possible to treat all input vari ables in the model the same way by ensuring that the coefficients of a model are not scaled concerning the units of the inputs. Any VI that can be used by our framework can be normalized with the Normalized Utility Index (NUI) and Normalized Reciprocal Utility (NRU), as shown in Table 3. We define $M a x ^ { M }$ as the maximum value and $M \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } m ^ { V I }$ as the minimum value for the considered VI. $O F ^ { U }$ is the corresponding objec tive function’s value for any solution, and $O P ^ { U }$ is the optimal value fo the considered VI.

Table 3  
Normalization formulas.

<table><tr><td>Index</td><td>Condition</td><td>Minimization formula</td><td>Maximization formula</td></tr><tr><td>NUI</td><td> $Max^{VI}$  and  $Min^{VI}$  should be available</td><td> $Max^{VI} - OF^{VI}$  $Max^{VI} - Min^{VI}$ </td><td> $OF^{VI} - Min^{VI}$  $Max^{VI} - Min^{VI}$ </td></tr><tr><td>NRU</td><td>The VI cannot take negative values</td><td> $Min^{VI}$  $OF^{VI}$ </td><td> $OF^{VI}$  $Max^{VI}$ </td></tr></table>

We can convert any validity index to normalized values using NUI and NRU, from which the outputs are unitless numbers between zero and one. The next section describes the mathematical model offered for our proposed framework.

## 2.3. Mathematical model

This section provides the mathematical model for our developed DSS. The notation used in the mathematical model is shown in Table 4. We also provide a brief overview of formulations of selected VIs and the proposed mathematical model, including the normalized aggregated objective function as well as the model’s constraints.

To explain our developed framework, we assume that the DM selects three widely used internal measures: DB, CS, and SH.

DB index: This validity index is a function of the distance within clusters and the distance between clusters. This measure tries to mini mize the distance between members of any cluster and maximize (or differentiate) the distance between clusters. To form the DB index, first, the centroid of a cluster is computed using Eq. 2. Then, we define metrics to calculate the distance between the members of the $k ^ { t h }$ cluster, S (Eq. 3), and the distance between the $k ^ { t h }$ and $q ^ { t h }$ clusters $\left( \operatorname { E q } . \ 4 \right)$

$$
\overrightarrow {C} _ {k} = \frac {\sum_ {Y _ {i} \in C _ {k}} \overrightarrow {Y} _ {i}}{N _ {k}}\tag{2}
$$

Nomenclature of the mathematical model.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td colspan="2">Sets</td></tr><tr><td> $i, l \in I \quad i, l = 1, ..., |I|$ </td><td>Indices used to refer to objects (or data points) in the dataset</td></tr><tr><td> $j \in J \quad j = 1, ..., |J|$ </td><td>Indices used to refer to dimension</td></tr><tr><td> $k, q \in K \quad k, q = 1, ..., |K|$ </td><td>Indices used to refer to each cluster</td></tr><tr><td colspan="2">Decision variable</td></tr><tr><td> $x_{ik}$ </td><td>Binary variable that takes one if  $i^{th}$  data point is a member of  $k^{th}$  cluster</td></tr><tr><td colspan="2">Auxiliary decision variables</td></tr><tr><td> $N_k$ </td><td>Integer variable that defines the number of the  $k^{th}$  cluster&#x27;s members</td></tr><tr><td> $\overrightarrow{C_k}$ </td><td>The centroid of the  $k^{th}$  cluster</td></tr><tr><td> $m_{kj}$ </td><td>The  $j^{th}$  element of the centroid of the $k^{th}$  cluster</td></tr><tr><td> $a_k$ </td><td>1 if the $k^{th}$  cluster is activated (has any member), and 0 otherwise</td></tr><tr><td>A</td><td>Total number of activated clusters</td></tr><tr><td>DB, CS, SH</td><td>VIs that measure the quality of cluster assignment</td></tr><tr><td>NDB, NCS, NSH</td><td>The normalized values for the DB,CS, andSH indices, respectively</td></tr><tr><td colspan="2">Parameters</td></tr><tr><td> $\overline{Y}_i$ </td><td>The vector belongs to the  $i^{th}$  data point in the dataset</td></tr><tr><td> $d_{il}$ </td><td>Distance between the  $i^{th}$  and  $l^{th}$  data points in the dataset (i.e.,  $d(\overrightarrow{Y_i}, \overrightarrow{Y_l})$ )</td></tr><tr><td> $OP^{DB}$ </td><td>The optimal value for the DB index (the smallest obtained value)</td></tr><tr><td> $OP^{CS}$ </td><td>The optimal value for the CS index (the smallest obtained value)</td></tr><tr><td> $Max^{SH}$ </td><td>The maximum obtained value for theSH index</td></tr><tr><td> $Min^{SH}$ </td><td>The minimum obtained value for theSH index</td></tr><tr><td> $\theta^{DB}, \theta^{CS}, \theta^{SH}$ </td><td>The minimum quality percentage threshold for the DB, CS, and SH indices, respectively</td></tr><tr><td> $w^{DB}, w^{CS}, w^{SH}$ </td><td>The importance weights of DB, CS, and SH indices in the aggregated function</td></tr></table>

$$
S _ {k} = \frac {\sum_ {\overrightarrow {Y _ {i}} \in C _ {k}} \left| \overrightarrow {Y} - \overrightarrow {C _ {k}} \right| ^ {2}}{N _ {k}} \quad \forall k \in K\tag{3}
$$

$$
d \left(\overrightarrow {C} _ {k}, \overrightarrow {C} _ {q}\right) = \sum_ {j \in J} \left| m _ {k j} - m _ {q j} \right| ^ {2} = \left\| \overrightarrow {C _ {k}} - \overrightarrow {C _ {q}} \right\| _ {2} \forall k, q \in K\tag{4}
$$

Next, $R _ { k }$ is defined as follows:

$$
R k = \max _ {k \in K, k \neq q} \left\{\frac {S _ {k} + S _ {q}}{d _ {k q}} \right\} \forall k \epsilon K\tag{5}
$$

Finally, the DB index can be measured by Eq. (6); a smaller DB value is desired.

$$
D B = \frac {\sum_ {k \in K} R _ {k}}{| K |}\tag{6}
$$

CS index: This validity index is formed based on worst-case possi bilities of the distance between cluster members (numerator) and the distance between cluster centers (denominator). The centroid of a cluster is calculated by taking the average of those data points that belong to the cluster, using Eq. $2 . \mathop { d } \left( \overline { { Y } } _ { i } , \overline { { Y } } _ { l } \right)$ denotes the distance be tween the $i ^ { t h }$ data point and the $l ^ { t h }$ data point, and $d \bigg ( \overrightarrow { C } _ { k } , \overrightarrow { C } _ { q } \bigg )$ denotes the distance between the centroid of the $k ^ { t h }$ cluster and the centroid of $\mathrm { t h e } q ^ { t h }$ cluster.

$$
C S = \frac {\frac {1}{| K |} \sum_ {k \in K} \left[ \frac {\sum_ {\overrightarrow {Y _ {i}} \in C _ {k}} \max _ {\overrightarrow {Y _ {l}} \in C _ {k}} \left\{d (\overrightarrow {Y _ {i}} , \overrightarrow {Y _ {i}}) \right\}}{N _ {k}} \right]}{\frac {1}{| K |} \sum_ {k \in K} \left[ \sum_ {q \in K} \min _ {q \neq k} \left\{d (\overrightarrow {C _ {k}} , \overrightarrow {C _ {q}}) \right\} \right]} = \frac {\sum_ {k \in K} \left[ \frac {\sum_ {\overrightarrow {Y _ {i}} \in C _ {k}} \max _ {\overrightarrow {Y _ {l}} \in C _ {k}} \left\{d (\overrightarrow {Y _ {i}} , \overrightarrow {Y _ {i}}) \right\}}{N _ {k}} \right]}{\sum_ {k \in K} \left[ \sum_ {q \in K} \min _ {q \neq k} \left\{d (\overrightarrow {C _ {k}} , \overrightarrow {C _ {q}}) \right\} \right]}\tag{7}
$$

As can be seen from Eq. $^ { 7 , }$ the CS index is a function of the ratio of the summation of distance within clusters and the distance between clusters. As with the DB index, a smaller value of CS represents better clustering. Chou et al. [24] pointed out that CS seems to be more efficient for problems with different sizes and densities, compared to other popular VIs.

SH index: This validity index assigns a quality score to each point, which is called the silhouette width. This score is a membership score of the $i ^ { t h }$ data point $\left( \overrightarrow { Y } _ { i } \right)$ to the $k ^ { t h }$ cluster that measures how well this point is assigned to the cluster. For any data point in the $k ^ { t h }$ cluster, let $\alpha _ { i }$ be the average distance between the $i ^ { t h }$ data point $\left( \overrightarrow { Y } _ { i } \right)$ and all other data points in the same cluster (Eq. 8).

$$
\alpha_ {i} = \frac {\sum_ {l \in I , i \neq l} x _ {i k} x _ {l k} d \left(\overrightarrow {Y} _ {i} , \overrightarrow {Y} _ {l}\right)}{N _ {k} - 1}
$$

$$
\forall i \in I\tag{8}
$$

Now, we define $\beta _ { i }$ as a score that captures the dissimilarity of the $i ^ { t h }$ data point $\left( \overrightarrow { \mathbf { Y } } _ { i } \right)$ to all other clusters (Eq. 9).

$$
\beta_ {i} = \min _ {q \neq k} \frac {\sum_ {l \in C _ {q}} x _ {i q} (1 - x _ {l k}) d (\overrightarrow {Y} _ {i} , \overrightarrow {Y} _ {l})}{N _ {k}} \quad \forall i \in I, k \in K\tag{9}
$$

Now, we have everything needed to compute the silhouette value of the $i ^ { t h }$ data point (Eq. 10).

$$
s _ {i} = \frac {\left(\beta_ {i} - \alpha_ {i}\right)}{\max \left(\alpha_ {i} , \beta_ {i}\right)}
$$

$$
\forall i \in I\tag{10}
$$

To compute the silhouette index, we calculate this index for each cluster, using Eq. 11.

$$
\overline {{S}} _ {k} = \frac {\sum_ {\overrightarrow {Y _ {i} \in C _ {k}}} s _ {i}}{N _ {k}}
$$

$$
\forall k \in K; N _ {k} \geq 1\tag{11}
$$

Finally, the SH index is computed, using Eq. 12.

$$
S H = \frac {\sum_ {k \in K} \overline {{S}} _ {k}}{A}\tag{12}
$$

$\overline { { S } } _ { k }$ in Eq. 11 represents the average values for all points that belong to the same cluster. The average value $\overline { { S } } _ { k }$ across all clusters is denoted bySH. For this validity index, in contrast to DB and CS, a higher SH value is more desirable. Since SH’s value is in a range of − 1 to 1, we use the NUI method to normalize the SH value in the aggregated function. The NRU method is used to normalize DB and CS. The normalized values for DB, CS, and SH are shown in Eqs. 13 through 15.

$$
N D B = \frac {O P ^ {D B}}{D B}\tag{13}
$$

$$
N C S = \frac {O P ^ {C S}}{C S}\tag{14}
$$

$$
N S H = \frac {S H - M i n ^ {S H}}{M a x ^ {S H} - M i n ^ {S H}}\tag{15}
$$

Now, we have all the components to form the objective function. Eq. 16 is the normalized and multiplication-based aggregated function that serves as the objective function of our developed model.

Objective function:

$$
\begin{array}{l} \text {Max Z = \left(\frac {DB}{OP^{DB}}\right)^{w ^{DB}} \left(\frac {CS}{OP^{CS}}\right)^{w ^{CS}} \left(\frac {SH - Min^{SH}}{Max^{SH} - Min^{SH}}\right)^{w^{SH}}} \\ = N D B ^ {w ^ {D B}} N C S ^ {w ^ {C S}} N S H ^ {w ^ {S H}} \end{array}\tag{16}
$$

As mentioned by Nanda and Panda [27], a clear and effective defi nition for the objective function in automatic clustering algorithms is the critical factor for having a successful algorithm. To contribute to this area, we borrowed the idea of our developed objective function from Charkhgard et al. [28] and take it one step forward by using normalized functions instead of the raw values of the objective functions. The objective function is the multiplication of normalized functions of VIs to the power of their respective weight of importance where these weights can be a value between zero and one. As a result, a larger weight of importance results in a smaller value for each index. For instance, a weight vector such as (0.5, 0.25, 0.25) for $( w ^ { D B } , w ^ { C S } , w ^ { S H } )$ in Eq. (16) implies that CS and SH indices have the same level of importance while they are both twice as important as DB index. These are the constraint of our developed model:

Constraints:

<table><tr><td> $N_{k} \leq |I|a_{k}$ K</td><td> $\forall k = 1, ...,$ </td><td>Ensures that the maximum number of a cluster&#x27;s members is less than the total number of data points</td><td>(17)</td></tr><tr><td> $N_{k} > a_{k} - 1$ ,..., K</td><td> $\forall k = 1,$ </td><td>Ensures that  $a_{k}$  takes zero if and only if  $N_{k}$  takes zero</td><td>(18)</td></tr><tr><td> $\sum_{i \in I} x_{ik} = N_{k}$ </td><td> $\forall k \in K$ </td><td>Defines the members that are assigned to the  $k^{th}$  cluster</td><td>(19)</td></tr><tr><td> $\sum_{k \in K} x_{ik} = 1$ </td><td> $\forall i \in I$ </td><td>Ensures that each object belongs to only one cluster</td><td>(20)</td></tr><tr><td> $\sum_{k \in K} N_{k} = |I|$ </td><td></td><td>Ensures that the summation of all members of a cluster is equal to the number of data points</td><td>(21)</td></tr><tr><td> $\sum_{k \in K} a_{k} = A$ </td><td></td><td>Defines the number of activated clusters</td><td>(22)</td></tr></table>

(continued on next column)

(continued )

<table><tr><td> $\frac{OP^{DB}}{DB} \leq \theta^{DB}$ </td><td>Ensures the obtained DB index of the current solution is lower than the predetermined acceptable threshold</td><td>(23)</td></tr><tr><td> $\frac{OP^{CS}}{CS} \leq \theta^{CS}$ </td><td>Ensures the obtained CS index of the current solution is lower than the predetermined acceptable threshold</td><td>(24)</td></tr><tr><td> $\frac{SH - Min^{SH}}{Max^{SH} - Min^{SH}} \geq \theta^{SH}$ </td><td>Ensures the obtained SH index of the current solution is above the predetermined acceptable threshold</td><td>(25)</td></tr><tr><td> $x_{ik} \& a_k = 0 \text{ or } 1 \quad \forall i \in I; k \in K$ </td><td>Guarantees that  $x_{ik}$  and  $a_k$  take either zero or one</td><td>(26)</td></tr><tr><td> $N_k, A$  are integer variables</td><td>Guarantees that  $N_k, A$  are integer variables</td><td>(27)</td></tr></table>

## 3. Methodology

Our developed framework has six steps, as described below.

Step 1: Validity indices, distance measure, algorithm selection, solution representation

## a) Selection of validity indices

In this step, the DM should select the VIs that match the primary goal of clustering as well as the data type and the data attributes. Depending on DM’s domain knowledge on the data set and VIs, DM can consider qualitative indices as secondary goals. In this step and parallel with the selection of $V I s ,$ some evolutionary algorithms should be chosen. Due to the generalizability of our developed framework, the DM has the freedom to select any types of VIs with different variations in range. In this study, we assume the DM selects DB, CS, SH, and number of clusters as VIs. Visual Connectedness measures the degree to which data are placed in the same cluster. Connectivity has a value between 0 and in finity and should be minimized. Visual Compactness or cluster cohesion measures how close are the data within the same cluster. More details on connectivity and compactness indices can be found in $[ 4 2 , 4 3 ]$ . Visual analytics can be used in a variety of fields. Park et al. [46] constructed a visual analytic system to assist and optimize supply chain managers decision-making processes. They validated the framework’s function ality and applicability by conducting multi-stage assessment sessions with prototypical users. Lu et al. [33] developed a visual analytics sys tem for detecting patterns of comorbidity progression using temporal and disease clustering.

## b) Distance measure and type of data

The choice of distance measure can have a significant impact on the clustering results. For continuous data, the most commonly used dis tance measure is Euclidean distance which is considered as special case of Minkowski equation. For nominal data, similarity coefficients such as dice index are applied frequently by researchers [47]. For mixed data, measures such as Gower distance are widely used [48].

## c) Algorithm selection and development

As mentioned in the previous section, the automatic clustering problem is an NP-hard problem. Although we developed an MINLP for this problem, a large number of non-linear equations in the model and the multi-objective nature of the problem lead us to use evolutionary algorithms for solution purposes. A survey paper by [29] found that the genetic algorithm (GA) and the particle swarm optimization (PSO) al gorithm are used in about half of the published papers that tackle MINLP problems. Therefore, we chose these two algorithms; besides, we chose the harmony search (HS), which is a powerful algorithm used by many scholars in the last decade. In the following lines, we briefly describe the solution representation that we used and the GA, PSO, and HS algorithms.

## d) Solution representation

A solution representation should be encoded to be fully consistent with the objective function and constraints in a way that all feasible solutions can be generated with no limitation. Since the number of clusters is a decision variable, the solution representation should be designed in such a way that it allows the model to search for each possible number of clusters, ranging from one to the number of data points in the dataset. As shown in Fig. 1, real encoding is used in this study; the solution representation is the same across all algorithms with different names and it is designed based on the centroid’s locations, with two layers. In the first layer, the location of each centroid is defined; in the second layer, it is determined whether this centroid is activated or not. Specifically, if the randomly generated number is less than 0.5, this center is not activated and vice versa. After defining the activated cen troids, all data points in the dataset will be allocated to the closest centroid. The name of solution in GA, PSO, and HS is called a chromo some, particle, and harmony, respectively.

The Genetic Algorithm’s phases and the operator used at each phase are as follows: initial population (random), fitness function evaluations (same as objective function for minimization problems and reciprocal function for maximization ones such as SH), selection for crossover and mutation, crossover procedure (uniform crossover), mutation procedure (uniform mutation), and next-generation selection (Elitism). Particle swarm optimization (PSO) is a population-based metaheuristic algo rithm developed by Kennedy and Eberhart [30]. It has been imple mented successfully to solve a wide range of optimization problems $[ 3 1 , 3 2 ]$ . In PSO, each solution (particle) has its position vector and fitness value. Generally, these particles explore the solution space in a direction (i.e., velocity in PSO) that is determined based on three com ponents. The first component is the information on the current position of the particle. The second component is the location of the best found personal solution, and the third component is the direction of the global best (i.e., the best solution among all the best personal solutions). Each particle in the initial population uses the personal best solution and the global best solution to reach a hypothetically better position. These steps will be continued until the stopping criterion is met. PSO’s major steps are initialization, determination of personal best, determination of global best, and updating the particle’s position. A harmony search al gorithm can be defined as a meaningful relationship among sound waves with different frequencies. The harmony search (HS) algorithm is inspired by this relationship and the point that the aim of any musician (the DM in optimization problems) is creating music that has a perfect state of harmony. The other feature of HS relies on the fact that a so lution can improve by search from iteration to iteration in the same way as the quality of music played by a band can improve by repetitive re hearsals. Harmony in HS is similar to the chromosome’s concept in GA. The best-obtained solutions will be stored in a place called harmony memory (HM); the actual size of this memory is predetermined by harmony memory size. If DM is aware of quality VIs that can help to differentiate and rank clusters, these quality indices can be added as the secondary criteria at this step.

## Step 2: Determining the quality thresholds.

In the second step, the DM will be asked to set reasonable minimum expectations regarding the quality of selected VIs in the final selected output. Before starting the third step, we should have a clear under standing of the possible values and the availability of lower bounds and upper bounds for the selected VIs. The selected quality threshold for each validity index should be set as a number between zero (i.e., no restriction) to 1 (or 100%, exact optimal value). If the resulted solution space turns out to be empty (no solution), the DM should revise the quality threshold to relax the constraints. DM can examine a set of thresholds ranging from 0 (most relaxed) to 1 (most strict) values depending on the needs of the problem. The number of generated so lutions has an inverse relationship with the threshold value.

## Step 3: Preparing input needed to form the aggregated function.

This step defines the inputs required to form the aggregated function. If the optimal value for the selected validity index is available and the validity index cannot take negative values, the selected algorithms will be called ten times to solve the single-objective $( \mathrm { i . e . , }$ the aforementioned VIs) problem and to find the optimal (or sub-optimal) value. In other cases, if the maximum and minimum values of the selected validity index are achievable, we let the selected algorithms solve the maximi zation problem and minimization problem ten times separately to find Max<sup>VI</sup> andMin<sup>VI</sup>. The parameter values for the three evolutionary algorithms are reported in Table A.6.

## Step 4: Formation of the aggregated function.

In this step, we have the inputs needed to form the aggregated function of our MINLP model. At the beginning of this step, the collab orative feature of our developed framework appears. Specifically, the selected evolutionary algorithms share their information to set a global value forOP<sup>VI</sup>, Max<sup>VI,</sup> and $M \mathrm { i } n ^ { U }$ parameters in the MINLP model. The utilized collaborative approach is offline meaning that each algorithm with single-objective is run sequentially before sharing information among each other. The result is used to form the aggregate function while the dominancy of the results are checked. Then, the selected VIs are normalized using the NUI and NRU approaches. The aggregated objective function is formed using the multiplication of normalized functions, each to the power of the corresponding importance weight.

## Step 5: Preparation of input for DEA.

In this step, the DM selects a combination of importance weights for the selected VIs; the summation of importance weights equals one. The details of the assigned weights for the SH, DB, and CS in the aggregated function are provided in Appendix Table A.1. The dataset will be tackled three times (once for each of the selected algorithms), and the number of clusters in the final output as well as the value of SH, DB, CS are recorded. SH values are used as the output and DB, CS, and number of clusters (NOC) are used as input for the CCR model.

![](/api/attachments/M735A7UZ/fulltext/images/b3fc86fa5343af6172951e7d34dc77e0bc98e943e40aa2ceae81f6f46dcc0338.jpg)  
Fig. 1. Solution representation by real encoding with |J| = 2 and $\left| K \right| = 5 .$

## Step 6: Determination of best partitioning.

The weights generated by DEA are the aggregated performance of proposed clustering indices, where DEA aggregates the VIs and returns an efficiency score. Given multiple efficient solutions in the DEA result, we use a multi-criteria technique such as BWM to rank the efficient re sults concerning secondary (qualitative) measures. BWM in this frame work works as human intervention (subjective) for having an effective aggregated score since the DEA finds the efficiency score based on raw input and output. Eq. (28) is used to rank the efficient DEA solutions, where the DEA scores are the bases and the weights generated by BWM are the exponents of this equation. Similar to Eq. (16), the larger exponent value implies a smaller weight of importance for the corre sponding index. The final Z values are then ranked in decreasing order.

(28)

![](/api/attachments/M735A7UZ/fulltext/images/3ea9884d5a47668243e03335ca1797da678c112a084468b34e34ce6880a6ac61.jpg)  
Fig. 2. Schematic view of the developed decision support system.

The schematic view of our developed framework is illustrated in Fig. 2.

## 4. Experiment results

As mentioned in the introduction section, the main goal of this research is to develop a decision-support framework that DMs can use to find the best clustering result. This framework is especially useful when the DM has little or no information about the criteria of interest (when more than one criterion is in place). We use synthetic data as well as Professional Golfers’ Association Tour Statistics (PGATS) for 2016–2017 season [40] to evaluate the robustness of the proposed framework considering different types of data. In the last decade, the Professional Golfers’ Association (PGA) Tour has seen emerging players who have revolutionized the game by becoming more athletic and nimble. In contrast, the veteran players utilize accurate and astute style of play to keep up with the young players. This creates a tour consisting of players with distinctly contrasting styles. Quantifying these different styles can help to identify and contrast the effectiveness of these two approaches to the game. This dataset includes the statistics of golf players including but not limited to #of wins, top 10s, driving accuracy and so on. The details of this dataset is accessible through the link in reference section. The experimental result of this dataset is included in Section 4.2.

## 4.1. DSS implementation

Steps 1 and 2: Off-line collaborative approach is applied for each evolutionary algorithm and for every VI in the single objective phase of the proposed framework. For instance, for DB validity index, we run the algorithms 10 times for GA, PSO, and HS algorithms, which result in 30 solutions and then select the best solution among these 30 solutions (the minimum DB value) and the same approach applies for other VIs. The collaborative feature of selected algorithms shares the best-found solu tions and sets global values for the $O P ^ { \boldsymbol { U } }$ $M a x ^ { W , }$ and $M \mathrm { { } } \mathrm { { } } \mathrm { { } } \mathrm { { } } m ^ { V I }$ parameters. The aggregated objective function is formed using the multiplication of normalized functions, each to the power of the corresponding impor tance weight. For future research, we encourage readers to apply other collaborative approaches in the utilized methodology. To shape the synthetic dataset, we generate 480 coordinates (points) by randomly generating 80 coordinates around each of six distinctive centroids in Table 5, using a multivariate normalized function with the mean of center points and the standard deviation of 0.6. These random co ordinates can be assigned to different clusters depending on the selected VIs (e.g., standard deviation). For example, given a small threshold for standard deviation, six distinctive clusters can be identified (i.e., a cluster will be formed around each centroid). Comparing different VIs, two-cluster selection appear to occur more frequently than other cluster selections.

Step 3: In this step, we run each of the GA, PSO, and HS algorithms ten times to find the best possible solution for CS, DB, and SH indices. The reported results are shown in Appendix Tables A.2-A.4, where NOC represents the resulting number of clusters after running each evolu tionary algorithm. For HS, the pitch adjusting rate (PAR) and damp ratio (FW damp) were set as 0.3 and 0.95. The bandwidth (FW) which is used to modify the harmony vector and plays a crucial role in pitch adjust ment step was set as the half of the distance between maximum and minimum population variance. Also, harmony memory considering rate (HMCR) was set as 0.3. The details of single-objective runs are provided below. The parameter values and the algorithms setup for $\mathrm { G A } ,$ PSO, and HS are provided in Table A.6.

Table 5  
Six randomly generated centroids.

<table><tr><td>Center</td><td>Coordinates</td></tr><tr><td>M1</td><td>(1,1)</td></tr><tr><td>M2</td><td>(3,4)</td></tr><tr><td>M3</td><td>(5,2)</td></tr><tr><td>M4</td><td>(8,5)</td></tr><tr><td>M5</td><td>(10,3)</td></tr><tr><td>M6</td><td>(12,4)</td></tr></table>

Minimizing CS Index: We identify a clustering pattern that mini mizes CS. For each CS minimization problem, the corresponding values for DB and SH are also reported. According to Table A.2, the minimum reported CS value among all three algorithms is 0.656.

Minimizing DB Index: The resulting DB values for the DB minimi zation problem using the three algorithms are reported in Table A.3. The minimum reported DB value among the three algorithms is 0.546. It is worth mentioning that PSO outperforms the other algorithms: the DB values for all 10 PSO runs are equal to the minimum reported DB value of 0.546.

Maximizing SH Index: The corresponding results for the SH maxi mization problem are reported in Table A.4. This VI ranges between − 1 and 1, with a maximum reported value of 0.722. Fig. 3 shows a com parison of the confidence intervals of the three VIs using the three al gorithms; the descriptive statistics are provided in Table 6. According to Fig. 3, the HS algorithm generates significantly better results on the CS and SH indices, whereas GA and PSO results are superior to HS on the DB index. Since the GA, PSO, and HS algorithms work collaboratively to find the values of VIs, there is no necessity to compare their results against each other in further detail. Instead, we emphasize the devel oped and implemented framework for finding the best clustering result.

The correlations in Table 7 reveal that there is a significant positive correlation coefficient between SH and CS, as well as some level of positive correlation between SH and DB. This means that maximizing SH conflicts with minimizing CS and DB.

Table 8 represents the % deviation of the evolutionary algorithms results comparing with the average result found by the collaborative approach. In the first step, we calculate the average deviation of GA, PSO, and HS results from the solution obtained by these three algo rithms, for each VI and, each data set, and then find the average % de viation over 10 runs. This table shows that the collaborative approach can improve the clustering results by as low as 0.75% in the synthetic data and as high as 10.2% in PGATS data.

Steps 4 and 5: The preference measures among the VIs and weights of importance are given randomly. However, a domain expert as the DM can choose these parameters based on his/her judgement. To calculate the multi-objective solutions, we define 16 sets of uniformly distributed weights between 0 and 1, where each set is composed of three weights $( \mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } ,$ and w ), and each weight corresponds to a validity-index result. Each set of weights is then repeated three times $( \mathbf { R } _ { 1 }$ through R ) to reflect the impact of three single-objective results on the objective function (Eq. 16). We perform this by taking the normalized validity index values to the power of these weights and calculating the resulting Z value for each evolutionary algorithm. The distributed weights and the final Z values are shown in Table A.5. There are $4 8 ^ { * } 3 = 1 4 4$ resulting solutions; each solution represents a certain number of clusters for the final solution. In Step 5, we extract the unique solutions by removing the repetitive solutions and the dominated solutions from Table $_ { \mathrm { A . 5 . } }$ We use standard definition of non-dominated solutions in Table 9. According to the definition, for maximization problems, solution $F _ { p }$ is efficient if and only if there does not exist another solution $F _ { q }$ in the set of solutions such that $f _ { i q } \geq f _ { i p }$ for all i, and $f _ { i q } > f _ { i p }$ for at least one i where p and q represent distinct solutions and i represents the solution dimension. The final 16 non-dominated unique solutions are presented in Table 9

Step 6: In this step, we apply DEA on the non-dominated unique solutions that we obtained in the previous step. SH is the output in our DEA model; DB, CS, and number of clusters (NOC) are DEA’s inputs. Since NOC is the most important factor among $\begin{array} { r } { { V I s , } } \end{array}$ the priority is given for minimizing input and then maximizing SH output. Therefore, we adopt an input-oriented DEA radial (i.e., a ratio-type DEA) approach to find the efficient point where CS, DB, and NOC are in the denominator and SH is in the numerator of DEA’s objective. The resulting input oriented CCR model leads to six efficient solutions (solutions 7–11, and 13), which are shown in Table 10.

![](/api/attachments/M735A7UZ/fulltext/images/658b0daefd3fb6f7a4f81bcf956e12dd2b41708bba0fb96f4a03ce5fe90f0bde.jpg)  
Fig. 3. Comparison of confidence intervals for CS, DB, and SH indices using GA, PSO, and HS.

Table 6  
Descriptive statistics of validity measures using GA, PSO, HS.

<table><tr><td rowspan="2"></td><td colspan="3">CS</td><td colspan="3">DB</td><td colspan="3">SH</td></tr><tr><td>GA</td><td>PSO</td><td>HS</td><td>GA</td><td>PSO</td><td>HS</td><td>GA</td><td>PSO</td><td>HS</td></tr><tr><td>Average</td><td>0.8232</td><td>0.8294</td><td>0.7220</td><td>0.5458</td><td>0.5458</td><td>0.5580</td><td>0.6272</td><td>0.6179</td><td>0.6715</td></tr><tr><td>Standard Deviation</td><td>0.0198</td><td>0.0000</td><td>0.0423</td><td>0.0000</td><td>0.0000</td><td>0.0063</td><td>0.0443</td><td>0.0413</td><td>0.0248</td></tr><tr><td>Best</td><td>0.7670</td><td>0.8294</td><td>0.6559</td><td>0.5458</td><td>0.5458</td><td>0.5509</td><td>0.7218</td><td>0.6756</td><td>0.7196</td></tr><tr><td>Confidence Interval</td><td>0.0122</td><td>0.0000</td><td>0.0262</td><td>0.0000</td><td>0.0000</td><td>0.0039</td><td>0.0275</td><td>0.0256</td><td>0.0154</td></tr></table>

Table 7  
Correlation among validity measures.

<table><tr><td></td><td>SH</td><td>DB</td><td>CS</td></tr><tr><td>SH</td><td>1</td><td></td><td></td></tr><tr><td>DB</td><td>0.442859</td><td>1</td><td></td></tr><tr><td>CS</td><td>0.852311</td><td>0.352354</td><td>1</td></tr></table>

Table 8  
Average deviation (in percentage) of the results of evolutionary algorithms from collaborative approach.

<table><tr><td></td><td>DB</td><td>CS</td><td>SH</td></tr><tr><td>Synthetic</td><td>0.75</td><td>9.60</td><td>6.02</td></tr><tr><td>PGATS</td><td>8.28</td><td>10.2</td><td>1.13</td></tr></table>

Table 9  
Non-dominated unique solutions; (I) and (O) represent input and output.

<table><tr><td colspan="9">Solutions 1–8</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>(I)NOC</td><td>4</td><td>3</td><td>4</td><td>5</td><td>3</td><td>3</td><td>2</td><td>2</td></tr><tr><td>(O)SH</td><td>0.72</td><td>0.72</td><td>0.72</td><td>0.68</td><td>0.66</td><td>0.66</td><td>0.6</td><td>0.59</td></tr><tr><td>(I)DB</td><td>9.99</td><td>22.58</td><td>5.23</td><td>2.94</td><td>1.59</td><td>2.37</td><td>3.55</td><td>0.56</td></tr><tr><td>(I) CS</td><td>1.24</td><td>1.25</td><td>1.32</td><td>1.24</td><td>1.15</td><td>1.12</td><td>0.73</td><td>0.83</td></tr><tr><td colspan="9">Solutions 9–18</td></tr><tr><td></td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td></tr><tr><td>(I)NOC</td><td>2</td><td>2</td><td>2</td><td>2</td><td>3</td><td>4</td><td>3</td><td>3</td></tr><tr><td>(O)SH</td><td>0.59</td><td>0.59</td><td>0.58</td><td>0.58</td><td>0.54</td><td>0.53</td><td>0.5</td><td>0.48</td></tr><tr><td>(I)DB</td><td>0.55</td><td>0.55</td><td>0.55</td><td>0.55</td><td>2.8</td><td>1.06</td><td>3.64</td><td>2.38</td></tr><tr><td>(I) CS</td><td>0.83</td><td>0.83</td><td>0.83</td><td>0.83</td><td>0.66</td><td>0.77</td><td>0.66</td><td>0.68</td></tr></table>

The best-worst method (BWM) is a recently developed multi-criteria technique for weight determination [20]. The rationale behind this method originated by eliminating duplications that usually occur in pairwise comparisons. In this method, each criterion needs to be compared with the most important criterion and the most unimportant criterion. Since multiple efficient results are reported in Table 10, we apply BWM to rank these efficient solutions concerning qualitative measures.

Table 10  
Ranking of solutions by CCR DEA model based on primary VIs.

<table><tr><td>Solution #</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>13</td><td>12</td><td>14</td></tr><tr><td>Score</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.99</td><td>0.95</td></tr><tr><td>Rank</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>7</td><td>8</td></tr><tr><td>Solution #</td><td>15</td><td>16</td><td>2</td><td>5</td><td>6</td><td>4</td><td>1</td><td>3</td></tr><tr><td>Score</td><td>0.93</td><td>0.87</td><td>0.80</td><td>0.79</td><td>0.79</td><td>0.72</td><td>0.71</td><td>0.68</td></tr><tr><td>Rank</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td></tr></table>

Table 11  
Comparison of best and worst outputs with resulting weights of importance

<table><tr><td></td><td>NOC</td><td>SH</td><td>DB</td><td>CS</td><td>VP</td><td>VN</td></tr><tr><td>Best criteria to others</td><td>2</td><td>1</td><td>3</td><td>2</td><td>1</td><td>1</td></tr><tr><td>Others to worst criteria</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>3</td></tr><tr><td>Weights of importance</td><td>0.12</td><td>0.23</td><td>0.07</td><td>0.12</td><td>0.23</td><td>0.23</td></tr></table>

BWM ranks the resulting clusters based on two qualitative measures (visual compactness (VC) and visual connectedness (VN)) and four quantitative indices (NOC, DB, SH, and CS). The rates (on the scale of 1–9) for qualitative measures of VN and VC for efficient clusters are shown in Table 11. According to the DM who provided the ranks of VIs, the most important criterion is SH, and the least important criterion is DB. The preference relationships between the best and worst criteria and others together with the resulting weights of importance are reported in Table 11. The weights of importance for NOC, SH, DB, CS, VP, and VN are 0.12, 0.23, 0.07, 0.12, 0.23, and 0.23, respectively. In the next step, we utilize Eq. (28) to find the final scores for DEA solutions. The higher values for BWM weights correlate with a higher level of importance for the corresponding validation score. However, there is an inverse rela tionship between weights of importance and the resulting score in Eq. (28). To preserve the preference relationship among the weights, we obtain the reciprocal of these values and divide them by their summation. Table 12 shows the final ranking of efficient solutions using the inverted and scaled weights of importance. According to Table 12, clustering No. 10 is the best clustering result, considering all six validity and qualitative measures. Clustering No. 10 is shown at the lower left in Fig. 4.

Table 12  
The validity index values for efficient solutions together with final ranking.

<table><tr><td>Solution#</td><td></td><td>NOC</td><td>SH</td><td>DB</td><td>CS</td><td>VP</td><td>VN</td><td>Score</td><td>Rank</td></tr><tr><td>BWM Weights</td><td></td><td>0.12</td><td>0.23</td><td>0.07</td><td>0.12</td><td>0.23</td><td>0.23</td><td></td><td></td></tr><tr><td>Inverted and scaled BWM weights</td><td></td><td>0.19</td><td>0.10</td><td>0.32</td><td>0.19</td><td>0.10</td><td>0.10</td><td></td><td></td></tr><tr><td></td><td>7</td><td>1.00</td><td>1.00</td><td>0.15</td><td>0.90</td><td>1.00</td><td>1.00</td><td>0.53</td><td>5</td></tr><tr><td></td><td>8</td><td>1.00</td><td>0.98</td><td>0.98</td><td>0.80</td><td>0.29</td><td>0.43</td><td>0.77</td><td>4</td></tr><tr><td></td><td>9</td><td>1.00</td><td>0.98</td><td>1.00</td><td>0.80</td><td>0.71</td><td>0.86</td><td>0.91</td><td>2</td></tr><tr><td></td><td>10</td><td>1.00</td><td>0.98</td><td>1.00</td><td>0.80</td><td>1.00</td><td>0.71</td><td>0.92</td><td>1</td></tr><tr><td>Normalized Solutions</td><td>11</td><td>1.00</td><td>0.98</td><td>1.00</td><td>0.80</td><td>0.71</td><td>0.57</td><td>0.87</td><td>3</td></tr><tr><td>From DEA</td><td>13</td><td>0.67</td><td>0.90</td><td>0.19</td><td>1.00</td><td>0.43</td><td>0.29</td><td>0.44</td><td>6</td></tr></table>

![](/api/attachments/M735A7UZ/fulltext/images/a73858175a0771d40e83b10e492841167c4115740ca11ea4eb21e7cee262ccb4.jpg)

![](/api/attachments/M735A7UZ/fulltext/images/e8f052f253f36f2621f8b5e6c568b09682d52517827f3e07e5adc36f8138cdb8.jpg)

![](/api/attachments/M735A7UZ/fulltext/images/9b524e4eb9f0ad7a67ad1fdb5f649cb7f2eee873706418cf29eadcf6c5912618.jpg)

![](/api/attachments/M735A7UZ/fulltext/images/08153d1bf396610c1ae76057dcac5f55a195695105a2ec2ab15b3b71fa38775b.jpg)

![](/api/attachments/M735A7UZ/fulltext/images/781e27aff94b410db977678a33313cb044c143839e1bc2fe09f6112d93118660.jpg)

![](/api/attachments/M735A7UZ/fulltext/images/8a01e53a4284531044b782c79aa32557897b9fa2f5abc2fb737936e2b60ce7ba.jpg)  
Fig. 4. Illustration of six efficient clustering results using four quantitative and two qualitative indices.

Our framework can be extended to more than two dimensions. In this case, after obtaining final solutions, we can convert the solutions to combination of pairs of features, $\mathrm { C } \left( { \scriptstyle { \frac { n } { 2 } } } \right)$ and find out how they look like in terms of connectivity and connectedness and assign a score to each of these pairs of selected features and report the average as the final qualitative score. For higher dimensions, due to impracticality of visu alizing all of combinations, dimension reduction techniques can be applied.

## 4.2. Sensitivity analysis

Changes on relative preference values in BWM: We perform a comprehensive sensitivity analysis of final solution ranks concerning the changes in ranking permutation and relative preference values of four quantitative and two qualitative indices. The final rankings of solutions turn out to be robust concerning these changes except for two conditions that influence the final rankings. The first condition occurs when DB and NOC are the most important and the least important criteria, respec tively. Under this condition, and considering any combination of rela tive preferences for the other four criteria, the ranking for at least one solution (solution 7 is among them) differs from other solution rankings.

## Table 13

Comparison of non-dominated solutions for EAs and CAs in different threshold values.

<table><tr><td rowspan="2">Threshold %</td><td colspan="2">Synthetic data</td><td colspan="2">PGATS</td></tr><tr><td>NEA $^{1}$ </td><td>NCA $^{2}$ </td><td>NEA</td><td>NCA</td></tr><tr><td>0%</td><td>16</td><td>5</td><td>10</td><td>4</td></tr><tr><td>20%</td><td>8</td><td>1</td><td>9</td><td>1</td></tr><tr><td>40%</td><td>6</td><td>1</td><td>6</td><td>0</td></tr><tr><td>60%</td><td>5</td><td>1</td><td>1</td><td>0</td></tr></table>

The second condition occurs when DB and SH are the most important and the least important criteria, respectively. Under this condition any combination of relative preferences for the other four criteria, the ranking for at least one solution (solution 7 is among them again) changes. Solution 7 tends to get a relatively high final score in every scenario, which in turn changes the final ranking of solutions. We conjecture that any corner point (i.e. a solution with extreme values) can be the possible reason for influencing the robustness of final rankings.

Threshold impact on the number of unique solutions: The first and the second values in every cell of Table 13 represent the number of obtained solutions by evolutionary algorithm (NEA) and classical algo rithm (NCA), respectively. According to this table, the cooperative evolutionary algorithm outperforms the three classical algorithms (Mean Shift, DBSCAN, and Affinity Propagation) in terms of number generated solutions, under every threshold % and for all three studied datasets. For instance, 0% quality threshold leaves us with 16 points from evolutionary algorithm and 1 point from DBSCAN. Other points generated by classic algorithms were dominated by these 16 points.

Depending on the level of tightness that DM incorporates on the threshold and the decision making process, DM can start from one end of the threshold to the other end and observe the changes in the number of generated solutions. A strict approach starts from a high threshold (e.g., 1) moving toward the lower % thresholds until DM obtains the desired number of feasible solutions. In contrast, a relaxed approach can start from 0 and progressively increases until it results in the desired number of solutions. This table also reveals that with a 40% quality threshold, we will have six non-dominated solutions for PGATS data after removing the repetitive solutions. A more restrictive quality threshold, such as 60%, will generate only one solution for this dataset.

## 4.3. Efficiency of the proposed collaborative evolutionary algorithm

To show why the proposed collaborative evolutionary approach is superior, we compare the performance of the evolutionary algorithms with three classical algorithms using three datasets with different cluster structures. The three classical clustering algorithms that we apply for comparing their efficiency with our proposed algorithm are: DBSCAN, Affinity Propagation, and Mean Shift.

DBSCAN is one of the most commonly used density-based clustering algorithms. It groups together data that are close to each other based on a distance measurement (usually Euclidean distance) and a minimum number of points. It also marks as outliers the points that are in lowdensity regions. Two main parameters of DBSCAN algorithm eps which specifies how close points should be to each other to be consid ered a part of a cluster and minPoints which defines the minimum number of points to form a dense region.

The mean shift algorithm is a nonparametric clustering technique that does not require prior knowledge of the number of clusters and does not constrain the shape of the clusters. Mean shift builds upon the concept of kernel density estimation. It is a partitioning algorithm similar to k-means that assigns points to the nearest cluster centroid. The output of mean shift does not depend on any explicit assumptions on the shape of the point distribution, the number of clusters, or any form of random initialization.

Affinity propagation (AP) is a graph-based clustering algorithm that does not require the estimation of the number of clusters before running the algorithm. The algorithm is based on finding iteratively how well one point is suited to be a representative of another point by gaining information about other prospective representatives in the data and checking the appropriateness of a point to find its representative based on the support gained from other points.

Table 14 compares the best and average values of evolutionary al gorithms (GA, PSO, HS) with the ones generated by the best classical algorithm (Mean shift, DBSCAN and Affinity Propagation) in each of the VIs. Bold values shows the winning algorithm for each dataset and each validity index. Please note that “BEA” refers to the best algorithm among evolutionary algorithms (GA, PSO, and HS) and “BCA” refers to the best algorithm among classic algorithms used in this paper (Mean Shift, DBSCAN, Affinity Propagation). Using CS and SH, the evolutionary al gorithms are outperforming in all datasets. Using DB, the evolutionary algorithms outperform better using synthetic datasets. However, in PGATS dataset the average value of DB for classical algorithms turns out to be better than evolutionary algorithms. PGATS dataset does not show a significant difference between evolutionary and classical algorithms. The reason behind this change among algorithms’ performance is due to the approach in identifying centers of clusters. In some practices, re searchers first identify starting center points whereas, in other practices, assignment of points to clusters is performed first and then the centers are calculated.

During evolutionary algorithms coding, we define the center of clusters as well as the number of clusters as decision variables. If we change this decision variable representation to a binary variable (to identify the number of required clusters in the first step and then dis tributes the possible solutions among those using binary coding), then evolutionary algorithms will outperform in all instances including DB index. We encourage researchers to perform a binary approach for obtaining clustering solutions and compare the validity index results with the current procedure as future research.

Table 14  
Comparison of the BEA and BCA in different datasets and different VIs

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Synthetic</td><td colspan="2">PGATS</td></tr><tr><td>Avg</td><td>Best</td><td>Avg</td><td>Best</td></tr><tr><td rowspan="2">CS</td><td>BEA</td><td>0.721</td><td>0.655</td><td>0.675</td><td>0.37</td></tr><tr><td>BCA</td><td>1.542</td><td>0.824</td><td>1.134</td><td>1.07</td></tr><tr><td rowspan="2">DB</td><td>BEA</td><td>0.545</td><td>0.545</td><td>1.499</td><td>0.64</td></tr><tr><td>BCA</td><td>0.787</td><td>0.560</td><td>1.138</td><td>0.963</td></tr><tr><td rowspan="2">SH</td><td>BEA</td><td>0.671</td><td>0.721</td><td>0.669</td><td>0.88</td></tr><tr><td>BCA</td><td>0.500</td><td>0.617</td><td>0.144</td><td>0.299</td></tr></table>

## 5. Conclusions and future works

The current single-objective clustering algorithms usually work well for partitioning linearly distinguishable clusters. However, they do not work well with non-linearly separable clusters, and they even ignore other important objective functions. Thus, single-criteria clustering al gorithms are inadequate for the multi-criteria nature of business prob lems that urges decision-makers to incorporate conflicting criteria into the solution. In this paper, we provide a mixed-integer non-linear pro gramming model for our automatic clustering problem with a quality threshold. This model considers a new aggregated validity index that benefits from a variety of existing VIs. Unlike existing approaches, our developed framework is sufficiently generalizable that it can easily be used for any type of automatic clustering problem, even in cases like these: 1) when the purpose of clustering is not fully consistent with available clustering methods: 2) when the decision-maker who is in charge of clustering has little or no information about the criterion of interest (exploratory data analysis); 3) when there is more than one criterion in place. Besides, our developed framework allows a decision: maker to set a minimum expectation for each validity index considered, as a quality threshold. Furthermore, the decision-maker classifies the selected VIs into primary and secondary VIs that are quantitative and qualitative, respectively. In this research, we incorporated four primary quantitative measures (the number of clusters and three VIs [DB, CS, and HS]) as well as two secondary qualitative measures (compactness and connectedness). We embedded an information-sharing feature in three evolutionary algorithms (GA, PSO, and HS) to improve the reliability of our results. Then, we considered different combinations of weights for the selected primary VIs, to create a pool of solutions. In the next step, our framework removed the dominated solutions: the non-dominated solutions were used as input for the selected DEA model. We devel oped a multi-criteria method using the best-worst method to determine the final output of clustering, in case the DEA’s output turns out to be more than one efficient solution. This framework ensures a unique clustering partitioning as the best result, and it effectively uses the hybrid collaborative evolutionary DEA approach to find the best clus tering result considering quantitative and qualitative measures.

We examined the applicability of our proposed framework by testing it on a randomly generated dataset; our results show the effectiveness of our proposed framework. Moreover, we embedded an informationsharing feature in our proposed approach to a solution. However, the focus of this paper is framework development, and subsequent research papers should focus on tackling the mentioned gaps by designing effi cient algorithms. The literature in decision support systems for auto matic clustering is very narrow; future research should expand this area by designing advanced decision support systems. Another research avenue would be to find the best combination of VIs including internal,

external, and relative indices, to improve the effectiveness of the developed decision support system in tackling different types of data sets. Research could also focus on developing more specialized multi criteria algorithms to enhance the capability of the developed decision support system to detect datasets with different shapes, inputs, and densities. Researchers can explore the impact of different distance measures in the final clustering outputs as well as other collaborative approaches in the utilized methodology. Regarding the decision support dimension, the proposed system can be tested such that it incorporates different DM’s perspectives while measuring the utility of the clusters.

## Acknowledgments

We sincerely thank the Editor In Chief of Decision Support Systems, Prof. James R. Marsden, and two anonymous reviewers for their valu able and constructive feedbacks throught the review process.

## Appendix

Table A.1  
Weights used in aggregated function for SH, DB and CS in synthetic and secondary data sets.

<table><tr><td>Row#</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td></tr><tr><td> $w^{SH}$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0.25</td><td>0</td><td>0.25</td><td>0.75</td><td>0.75</td><td>0.5</td><td>0.5</td><td>0</td><td>0.25</td><td>0.25</td><td>0.5</td><td>1/3</td></tr><tr><td> $w^{DB}$ </td><td>0</td><td>1</td><td>0</td><td>0.25</td><td>0</td><td>0.75</td><td>0.75</td><td>0.25</td><td>0</td><td>0.5</td><td>0</td><td>0.5</td><td>0.25</td><td>0.5</td><td>0.25</td><td>1/3</td></tr><tr><td> $w^{CS}$ </td><td>1</td><td>0</td><td>0</td><td>0.75</td><td>0.75</td><td>0.25</td><td>0</td><td>0</td><td>0.25</td><td>0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.25</td><td>0.25</td><td>1/3</td></tr></table>

Table A.2  
Validity index values using GA, PSO, and HS for CS minimization.

<table><tr><td rowspan="2"></td><td colspan="4">GA</td><td colspan="4">PSO</td><td colspan="4">HS</td></tr><tr><td>CS</td><td>DB</td><td>SH</td><td>NOC</td><td>CS</td><td>DB</td><td>SH</td><td>NOC</td><td>CS</td><td>DB</td><td>SH</td><td>NOC</td></tr><tr><td>1</td><td>0.767</td><td>1.056</td><td>0.531</td><td>4</td><td>0.829</td><td>1.894</td><td>0.583</td><td>2</td><td>0.741</td><td>1.681</td><td>0.483</td><td>3</td></tr><tr><td>2</td><td>0.829</td><td>0.603</td><td>0.583</td><td>2</td><td>0.829</td><td>1.914</td><td>0.583</td><td>2</td><td>0.685</td><td>2.380</td><td>0.475</td><td>3</td></tr><tr><td>3</td><td>0.829</td><td>0.683</td><td>0.583</td><td>2</td><td>0.829</td><td>1.374</td><td>0.583</td><td>2</td><td>0.721</td><td>2.567</td><td>0.534</td><td>4</td></tr><tr><td>4</td><td>0.829</td><td>0.714</td><td>0.583</td><td>2</td><td>0.829</td><td>1.374</td><td>0.583</td><td>2</td><td>0.774</td><td>3.015</td><td>0.503</td><td>3</td></tr><tr><td>5</td><td>0.829</td><td>1.170</td><td>0.583</td><td>2</td><td>0.829</td><td>0.807</td><td>0.583</td><td>2</td><td>0.734</td><td>1.627</td><td>0.522</td><td>5</td></tr><tr><td>6</td><td>0.829</td><td>7.362</td><td>0.583</td><td>2</td><td>0.829</td><td>0.561</td><td>0.583</td><td>2</td><td>0.656</td><td>3.637</td><td>0.500</td><td>3</td></tr><tr><td>7</td><td>0.829</td><td>0.822</td><td>0.583</td><td>2</td><td>0.829</td><td>2.458</td><td>0.583</td><td>2</td><td>0.771</td><td>2.333</td><td>0.516</td><td>5</td></tr><tr><td>8</td><td>0.829</td><td>0.576</td><td>0.583</td><td>2</td><td>0.829</td><td>1.020</td><td>0.583</td><td>2</td><td>0.663</td><td>2.805</td><td>0.542</td><td>3</td></tr><tr><td>9</td><td>0.829</td><td>0.910</td><td>0.583</td><td>2</td><td>0.829</td><td>1.278</td><td>0.583</td><td>2</td><td>0.718</td><td>5.466</td><td>0.543</td><td>3</td></tr><tr><td>10</td><td>0.829</td><td>3.632</td><td>0.583</td><td>2</td><td>0.829</td><td>1.368</td><td>0.583</td><td>2</td><td>0.757</td><td>1.762</td><td>0.551</td><td> $^4$ </td></tr></table>

Table A.3  
Validity index values using GA, PSO, and HS for DB minimization.

<table><tr><td rowspan="2"></td><td colspan="4">GA</td><td colspan="4">PSO</td><td colspan="4">HS</td></tr><tr><td>CS</td><td>DB</td><td>SH</td><td>NOC</td><td>CS</td><td>DB</td><td>SH</td><td>NOC</td><td>CS</td><td>DB</td><td>SH</td><td>NOC</td></tr><tr><td>1</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.830</td><td>0.558</td><td>0.585</td><td>2</td></tr><tr><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.853</td><td>0.565</td><td>0.585</td><td>2</td></tr><tr><td>3</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.860</td><td>0.561</td><td>0.585</td><td>2</td></tr><tr><td>4</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.860</td><td>0.551</td><td>0.585</td><td>2</td></tr><tr><td>5</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.841</td><td>0.565</td><td>0.585</td><td>2</td></tr><tr><td>6</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.555</td><td>0.586</td><td>2</td></tr><tr><td>7</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.832</td><td>0.555</td><td>0.585</td><td>2</td></tr><tr><td>8</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.831</td><td>0.551</td><td>0.584</td><td>2</td></tr><tr><td>9</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.836</td><td>0.567</td><td>0.579</td><td>2</td></tr><tr><td>10</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.546</td><td>0.586</td><td>2</td><td>0.833</td><td>0.551</td><td>0.586</td><td> $^2$ </td></tr></table>

Table A.4  
Validity index values using GA, PSO, and HS for SH maximization.

<table><tr><td rowspan="2">—</td><td colspan="4">GA</td><td colspan="4">PSO</td><td colspan="4">HS</td></tr><tr><td>CS</td><td>DB</td><td>SH</td><td>NOC</td><td>CS</td><td>DB</td><td>SH</td><td>NOC</td><td>CS</td><td>DB</td><td>SH</td><td>NOC</td></tr><tr><td>1</td><td>0.833</td><td>0.994</td><td>0.586</td><td>2</td><td>0.833</td><td>3.380</td><td>0.586</td><td>2</td><td>1.203</td><td>2.052</td><td>0.661</td><td>3</td></tr><tr><td>2</td><td>1.643</td><td>2.557</td><td>0.650</td><td>5</td><td>0.833</td><td>2.421</td><td>0.586</td><td>2</td><td>1.118</td><td>2.367</td><td>0.663</td><td>3</td></tr><tr><td>3</td><td>0.833</td><td>0.659</td><td>0.586</td><td>2</td><td>1.147</td><td>3.916</td><td>0.665</td><td>3</td><td>1.323</td><td>5.231</td><td>0.717</td><td>4</td></tr><tr><td>4</td><td>0.978</td><td>4.937</td><td>0.626</td><td>4</td><td>0.833</td><td>1.875</td><td>0.586</td><td>2</td><td>1.160</td><td>2.418</td><td>0.656</td><td>3</td></tr><tr><td>5</td><td>1.147</td><td>4.764</td><td>0.665</td><td>3</td><td>0.833</td><td>0.791</td><td>0.586</td><td>2</td><td>1.245</td><td>22.577</td><td>0.720</td><td>3</td></tr><tr><td>6</td><td>1.224</td><td>1.580</td><td>0.631</td><td>4</td><td>0.833</td><td>0.674</td><td>0.586</td><td>2</td><td>1.077</td><td>3.732</td><td>0.662</td><td>4</td></tr><tr><td>7</td><td>1.240</td><td>9.998</td><td>0.722</td><td>4</td><td>0.833</td><td>0.591</td><td>0.586</td><td>2</td><td>1.299</td><td>3.800</td><td>0.652</td><td>3</td></tr></table>

(continued on next page)

Table A.4 (continued )

<table><tr><td rowspan="2">—</td><td colspan="4">GA</td><td colspan="4">PSO</td><td colspan="4">HS</td></tr><tr><td>CS</td><td>DB</td><td>SH</td><td>NOC</td><td>CS</td><td>DB</td><td>SH</td><td>NOC</td><td>CS</td><td>DB</td><td>SH</td><td>NOC</td></tr><tr><td>8</td><td>0.833</td><td>1.056</td><td>0.586</td><td>2</td><td>1.292</td><td>1.887</td><td>0.657</td><td>5</td><td>1.112</td><td>2.994</td><td>0.662</td><td>3</td></tr><tr><td>9</td><td>0.833</td><td>0.761</td><td>0.586</td><td>2</td><td>1.235</td><td>2.941</td><td>0.676</td><td>5</td><td>1.110</td><td>5.761</td><td>0.662</td><td>3</td></tr><tr><td>10</td><td>1.389</td><td>0.944</td><td>0.635</td><td>3</td><td>1.147</td><td>1.591</td><td>0.665</td><td>3</td><td>1.114</td><td>2.464</td><td>0.661</td><td> $^3$ </td></tr></table>

Table A.5  
Multi-objective problem considering three VIs for synthetic data.

<table><tr><td colspan="5"></td><td colspan="4">GA</td><td colspan="4">PSO</td><td colspan="4">HS</td></tr><tr><td></td><td></td><td>W1</td><td>W2</td><td>W3</td><td>NOC</td><td>SH</td><td>DB</td><td>CS</td><td>NOC</td><td>SH</td><td>DB</td><td>CS</td><td>NOC</td><td>SH</td><td>DB</td><td>CS</td></tr><tr><td>1</td><td> $R_1$ </td><td>0</td><td>0</td><td>1</td><td>4</td><td>0.53</td><td>1.06</td><td>0.77</td><td>2</td><td>0.58</td><td>0.561</td><td>0.83</td><td>3</td><td>0.47</td><td>2.38</td><td>0.68</td></tr><tr><td>2</td><td> $R_2$ </td><td>0</td><td>0</td><td>1</td><td>2</td><td>0.58</td><td>0.68</td><td>0.83</td><td>2</td><td>0.58</td><td>0.81</td><td>0.83</td><td>3</td><td>0.50</td><td>3.64</td><td>0.66</td></tr><tr><td>3</td><td> $R_3$ </td><td>0</td><td>0</td><td>1</td><td>2</td><td>0.58</td><td>0.82</td><td>0.83</td><td>2</td><td>0.58</td><td>1.020</td><td>0.83</td><td>3</td><td>0.54</td><td>2.80</td><td>0.66</td></tr><tr><td>⋮</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>46</td><td> $R_1$ </td><td>0.33</td><td>0.33</td><td>0.33</td><td>2</td><td>0.58</td><td>0.55</td><td>0.83</td><td>2</td><td>0.58</td><td>0.55</td><td>0.83</td><td>2</td><td>0.58</td><td>0.55</td><td>0.83</td></tr><tr><td>47</td><td> $R_2$ </td><td>0.33</td><td>0.33</td><td>0.33</td><td>2</td><td>0.58</td><td>0.55</td><td>0.83</td><td>2</td><td>0.58</td><td>0.55</td><td>0.83</td><td>2</td><td>0.58</td><td>0.55</td><td>0.83</td></tr><tr><td>48</td><td> $R_3$ </td><td>0.33</td><td>0.33</td><td>0.33</td><td>2</td><td>0.58</td><td>0.55</td><td>0.83</td><td>2</td><td>0.58</td><td>0.55</td><td>0.83</td><td>2</td><td>0.58</td><td>0.55</td><td>0.83</td></tr></table>

Table A.6  
Parameters for evolutionary algorithms.

<table><tr><td colspan="2">GA</td><td colspan="2">PSO</td><td colspan="2">HS</td></tr><tr><td>Parameter</td><td>Value</td><td>Parameter</td><td>Value</td><td>Parameter</td><td>Value</td></tr><tr><td>MaxIt</td><td>300</td><td>MaxIt</td><td>300</td><td>MaxIt</td><td>300</td></tr><tr><td>nPop</td><td>100</td><td>nPop</td><td>100</td><td>nNew</td><td>100</td></tr><tr><td>pc</td><td>0.9</td><td>phi1</td><td>2.05</td><td>HMS</td><td>30</td></tr><tr><td>pm</td><td>0.2</td><td>phi2</td><td>2.05</td><td>HMCR</td><td>0.3</td></tr><tr><td>nc</td><td>90</td><td>w</td><td>0.73</td><td>PAR</td><td>0.3</td></tr><tr><td>nm</td><td>20</td><td>wdamp</td><td>1</td><td>FW</td><td>0.5*(VarMax-VarMin)</td></tr><tr><td></td><td></td><td>c1</td><td>1.5</td><td>FW_damp</td><td>0.95</td></tr><tr><td></td><td></td><td>c2</td><td>1.5</td><td></td><td></td></tr><tr><td></td><td></td><td>VelMax</td><td>0.1*(VarMax-VarMin)</td><td></td><td></td></tr><tr><td></td><td></td><td>VelMin</td><td>-VelMax</td><td></td><td></td></tr></table>

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.dss.2021.113671.

## References

[1] L.R. Divvaa, N. Pervin, Towards generating scalable personalized recommendations: integrating social trust, social bias, and geo-spatial clustering, Decis. Support. Syst. 122 (2019) 113066.

[2] S.T. Wang, Integrating KPSO and C5.0 to analyze the omnichannel solutions for optimizing telecommunication retail, Decis. Support. Syst. 109 (2018) 39–49.

[3] R.M. Van Steenbergen, M.R.K. Mes, Forecasting demand profiles of new products, Decis. Support. Syst. 113401 (2020).

[4] C. Bai, B. Shi, F. Liu, J. Sarkis, Banking credit worthiness: evaluating the complex relationships. Omega 83 (2019) 26–38.

[5] S. Simsek, A. Dag, T. Tiahrt, A. Oztekin, A Bayesian Belief Network-based probabilistic mechanism to determine patient no-show risk categories, Omega 102296 (2020).

[6] Y. Yang, H. Bidkhori, J. Rajgopal, Optimizing vaccine distribution networks in low and middle-income countries. Omega 102197 (2020).

[7] A.I. Jarrah, J.F. Bard, Pickup and delivery network segmentation using contiguous geographic clustering, J. Oper, Res, Soc, 62 (10) (2011) 1827–1843.

[8] A.C. Yeo, K.A. Smith, R.J. Willis, M. Brooks, A mathematical programming approach to optimise insurance premium pricing within a data mining framework, J. Oper. Res. Soc. 53 (11) (2002) 1197–1203.

[9] S. Saha. S. Bandvopadhvay. A generalized automatic clustering algorithm in a multiobjective framework, Appl. Soft Comput. 13 (1) (2013) 89–108.

[10] H. He, Y. Tan, A two-stage genetic algorithm for automatic clustering, Neurocomputing 81 (2012) 49–59.

[11] S. Barak, T. Mokfi, Evaluation and selection of clustering methods using a hybrid group MCDM, Expert Syst. Appl. 138 (2019) 112817.

[12] C. Liu, Y. Li, Q. Zhao, C. Liu, Reference vector-based multi-objective clustering for high-dimensional data, Appl. Soft Comput. 78 (2019) 614–629.

[13] R. Shang, W. Zhang, F. Li, L. Jiao, R. Stolkin, Multi-objective artificial immune algorithm for fuzzy clustering based on multiple kernels, Swarm Evolut. Comput 50 (2019) 100485.

[14] R. Wang. S. Lai, G. Wu, L.. Xing. L. Wang. H. Ishibuchi, Multi-clustering via evolutionary multi-obiective optimization. Inf. Sci. 450 (2018) 128–140

[15] R.J. Kuo, F.E. Zulvia, Multi-objective cluster analysis using a gradient evolution algorithm, Soft. Comput. (2020) 1–15.

[16] D. Dutta, J. Sil, P. Dutta, Automatic clustering by multi-objective genetic algorithm with numeric and categorical features, Expert Syst, Appl. 137 (2019) 357–379

[17] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the efficiency of decision making

[18] O. Olanrewaju, A. Jimoh, P. Kholopan, Energy Efficiency Assessment Using Artificial Neural Network Combined with Data Envelopment Analysis. JEEE Africon. 2011, pp. 13–15.

[19] O. Olanrewaiu. A. Jimoh. P. Kholopan, Integrated IDA-ANN-DEA for assessment and optimization of energy consumption in industrial sectors. Energy 46 (2012 629–635.

[20] Jafar Rezaei, Best-worst multi-criteria decision-making method. Omega 53 (2015) (2015) 49–57.

[21] J.C. Dunn, Well-separated clusters and optimal fuzzy partitions, J. Cybern. 4 (1) (1974) 95–104.

[22] D.L. Davies, D.W. Bouldin, A cluster separation measure, IEEE Trans. Pattern Anal. Mach, Intell, 2 (1979) 224–227.

[23] P.J. Rousseeuw, Silhouettes: a graphical aid to the interpretation and validation of cluster analysis, J. Comput. Appl. Math. 20 (1987) 53–65.

[24] C.H. Chou, M.C. Su, E. Lai, A new cluster validity measure and its application to image compression, Pattern. Anal. Applic. 7 (2) (2004) 205–220.

[25] K.Y. Yeung, D.R. Haynor, W.L. Ruzzo, Validating clustering for gene expression data, Bioinformatics 17 (4) (2001) 309–318.

[26] V. Roth, M.L. Braun, T. Lange, J.M. Buhmann, Stability-based model order selection in clustering with applications to gene expression data, in: International Conference on Artificial Neural Networks, Springer, Berlin, Heidelberg, 2002, pp. 607–612.

[27] S.J. Nanda, G. Panda, Automatic clustering algorithm based on multi-objective immunized PSO to classify actions of 3D human models, Eng. Appl. Artif. Intell. 26 (5–6) (2013) 1429–1441.

[28] H. Charkhgard, K. Keshanian, R. Esmaeilbeigi, P. Charkhgard, The Magic of Nash Social Welfare in Optimization: Do Not Sum, Just Multiply! Working Paper No. 15- 019, Available at, http://www.optimization-online.org/DB HTML/2020/03/7688 html. 2020 (Accessed: 31 Augest 2020).

[29] A. Jos´e-García, W. Gomez-Flores, ´ Automatic clustering using nature-inspired metaheuristics: a survey, Appl. Soft Comput. 41 (2016) 192–213.

[30] J. Kennedy, R. Eberhart, Particle swarms optimization, in: IEEE International Conference on Neural Networks, vol. 4, 1995

[31] R.C. Brasileiro, V.L. Souza, A.L. Oliveira, Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization with validation, Decis. Support. Syst. 104 (2017) 79–91.

[32] M.D. Bailey, D. Michaels, An optimization-based DSS for student-to-teacher assignment: classroom heterogeneity and teacher performance measures, Decis. Support. Syst. 119 (2019) 60–71.

[33] Y. Lu, S. Chen, Z. Miao, D. Delen, A. Gin, Clustering temporal disease networks to assist clinical decision support systems in visual analytics of comorbidity progression, Decision Support Systems 148 (2021) 113583.

[34] S. Zhu, L. Xu, E.D. Goodman, Evolutionary multi-objective automatic clustering enhanced with quality metrics and ensemble strategy, Knowl.-Based Syst. 188 (2020) 105018.

[35] I. Heloulou, M.S. Radjef, M.T. Kechadi, Automatic multi-objective clustering based on game theory, Expert Syst. Appl. 67 (2017) 32–48.

[36] M.G. Martínez-Penaloza, ˜ E. Mezura-Montes, N. Cruz-Ramírez, H.G. Acosta-Mesa, H.V. Ríos-Figueroa, Improved multi-objective clustering with automatic determination of the number of clusters, Neural Comput. & Applic. 28 (8) (2017) 2255–2275.

[37] M. Orouskhani, D. Shi, Y. Orouskhani, Multi-objective evolutionary clustering with complex networks, Expert Syst, Appl, 165 (2021) 113916.

[38] J. Handl, J. Knowles, An evolutionary approach to multiobjective clustering, IEEE Trans. Evol. Comput. 11 (1) (2007) 56–76.

[40] Professional Golfers’ Association Tour Statistics. https://www.espn.com/golf/sta tistics/\_/year/2017.

[41] Y. Yin, Y. Zhao, H. Li, X. Dong, Multi-objective evolutionary clustering for largescale dynamic community detection. Inf. Sci, 549 (2021) 269–287.

[42] S. Saha, S. Bandyopadhyay, Some connectivity based cluster validity indices, Appl. Soft Comput, 12 (5) (2012) 1555–1565

[43] A.I. Hammouri, S. Abdullah, Comparison between compactness and connectedness criteria in data clustering, Int. J. Data Analysis Techn, Strat. 8 (4) (2016) 281–295

[44] M.E. Irarrazaval, ´ S. Maldonado, J. P´erez, C. Vairetti, Telecom traffic pumping analytics via explainable data science, Decis. Support. Syst. 113559 (2021)

[45] B. Biswas, P. Sengupta, D. Chatterjee, Examining the determinants of the count of customer reviews in peer-to-peer home-sharing platforms using clustering and count regression techniques, Decis. Support. Syst. 135 (2020) 113324.

[46] H. Park, M.A. Bellamy, R.C. Basole, Visual analytics for supply network management: system design and evaluation, Decis. Support. Syst. 91 (2016) 89–102.

[47] H. Finch, Comparison of distance measures in cluster analysis with dichotomous data, J. Data Sci. 3 (1) (2005) 85–100.

[48] J.C. Gower, A general coefficient of similarity and some of its properties, Biometrics (1971) 857–871.

[49] S. Shirakawa, T. Nagao, Evolutionary image segmentation based on multiobjective clustering, in: 2009 JEEE Congress on Evolutionary Computation, JEEE, 2009, Mav. pp. 2466–2473.

Mona Jabbari is an Assistant Professor in Operations and Business Analytics at Finance department of Providence College School of Business (PCSB). Her research interests lie primarily in the area of operations management and business analytics in the Healthcare and Supply Chain Management. She is also interested in the methodologies of data mining, mathematical modeling, game theory, multi-obiective optimization. and multi-criteria decision making. She has presented her research in several national and international conferences. She obtained her PhD from University of Oregon in 2021.

Professor Shaya Sheikh obtained his Ph.D. from Case Western Reserve University in 2013. He worked as a scheduling and optimization scientist at Lancaster Laboratories and as a visiting professor at University of Baltimore before joining New York Institute of Technology. He is currently serving as associate professor of supply chain management at NYIT School of Management. His research interests include energy supply chain, sched uling, and application of state-of-the-art data-driven models in a variety of business problems.

Sheikh has authored over 40 research papers in highly ranked peer-reviewed journals and conference proceedings such as Energy, International Journal of Production Research, Applied Mathematical Modeling, Computers & Industrial Engineering, Journal of Intelli gent Manufacturing, International Journal of Advanced Manufacturing Technology, Op erations Research Perspective, Energy, International Journal of Communication Systems, Journal of Wireless Networks and IEEE International Conferences.

Sheikh serves as editorial board member and guest editor for several management and supply chain journals. He also serves as session chair for top international conferences such as INFORMS and POMS and as conference co-chair, conference organizer, and committee member at international conferences. Sheikh is regularly invited as speaker to interna tional conferences or as reviewer/panelist to Grant and Award Funding Agencies such as NSF. He also serves as invited and ad-hoc reviewer for more than 15 top journals in energy, scheduling, and supply chain management field.

Meysam Rabiee is a PhD candidate in Operations and Business Analytics at the University of Oregon. He has served as a faculty member and the Program Director of the Industrial Engineering Department at the Bu-Ali Sina University in Iran prior his current appoint ment at University of Oregon. His research has appeared in major journals including In ternational Journal of Production Economics and International of Production Research, among others. His research interests include Decision Support Systems. Sustainable Supply Chain, Multi-Criteria Decision Making, Multi-Objective Optimization, Data Analytics and Scheduling

Dr. Asil Oztekin is an Associate Professor of Operations and Information Systems Department, Manning School of Business and a participating faculty member for the Biomedical Engineering & Biotechnology Program at UMass Lowell. Oztekin is also serving as the contributing associate member of the Management Analytics & Decision Making Group at Massey University, New Zealand. He received his Ph.D. degree from Oklahoma State University, Industrial Engineering and Management department. Oztekin is certified by SAS® as a Predictive Modeling and Data Mining expert. He is a member of INFORMS and Decision Sciences Institute. His work has been published in top tier outlets such as Decision Support Systems, European Journal of Operational Research, International Journal of Production Research, OMEGA: the International Journal of Management Science, and Annals of Operations Research among others. One of his publications entitled “An RFID Network Design Methodology for Asset Tracking in Healthcare” has been listed among the Most Cited journal articles at Decision Support Systems in 2015. Oztekin has edited four special issues as a guest co-editor: “Data Mining & Decision Analytics” at the Decision Sciences journal, “Business Analytics: Defining the field and identifying a research agenda” at the Europegn Journgl of Operational Resegrch. “Data Mining & Analytics" at the Annals of Operations Research journal, and “Intelligent Computational Techniques in Science, Engi neering, and Business” at the Expert Systems with Applications journal. Asil Oztekin is serving as the Associate Editor of the Decision Support Systems journal and the Journal of Modeling in Management. He is listed as an official Editorial Review Board member for the Industrial Management & Data Systems, Journal of Computer Information Systems, Service Business: an International Journal. International Journal of Medical Engineering & Informatics International Journal of RF Technologies: Research and Applications among others. He frequently serves as an ad-hoc reviewer for Decision Support Systems. Decision Sciences OMEGA. International Journal of Forecasting. International Journal of Production Research International Journal of Production Economics, Annals of Operations Research, Computers & Industrial Engineering, Information Technology & Management, Applied Mathematical Modeling, Journal of Manufacturing Systems, INFOR: Information Systems and Operational Research journal. Computer Methods & Programs in Biomedicine, and Computers in Biology & Medicine journals among others, Oztekin often leads mini-tracks and sessions at INFORMs and HICSS conferences such as Data, Text, & Web Mining for Business Analytics, Data Mining in Decision Making. Predictive Analytics & Big Data, Data Mining & Analytics and etc. He has chaired the INFORMS 2015 Data Mining & Analytics Workshop and the IN-FORMS 2016 Data Mining & Decision Analytics Workshop. Asil Oztekin has been selected as the“Faculty Honoree of 29 Who Shine" in May 2014 by the Governor and Department of Higher Education in Massachusetts. Dr. Oztekin received the Teaching Excellence Award in April 2014 and has been the Outstanding Recognized Researcher of the Manning School of Business awarded by the Vice Provost for Research of UMass Lowell in February 2014 and in March 2016. Additionally, he has been recognized on the Faculty Honors & Awards Wall of UMass Lowell in Summer 2016. He was also the recipient of the Alpha Pi Mu Outstanding Industrial Engineering & Management Research Assistant Award from Oklahoma Stat University in 2009.
