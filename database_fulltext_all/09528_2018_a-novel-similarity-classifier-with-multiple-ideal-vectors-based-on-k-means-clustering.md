---
otero_id: 9528
otero_key: "VT36U6Q9"
title: "A novel similarity classifier with multiple ideal vectors based on k-means clustering"
authors: "Christoph Lohrmann; Pasi Luukka"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.04.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel similarity classi<sup>fi</sup>er with multiple ideal vectors based on k-means clustering

Christoph Lohrmann , Pasi Luukka

Lappeenranta University of Technology, School of Engineering Science, Skinnarilankatu 34, 53850 Lappeenranta, Finland

## A R T I C L E I N F O

Keywords: Supervised classi<sup>fi</sup>cation Jump method Principal component analysis MAP test Parallel Analysi

## A B S T R A C T

In the literature, researchers and practitioners can <sup>fi</sup>nd a manifold of algorithms to perform a classi<sup>fi</sup>cation task. The similarity classi<sup>fi</sup>er is one of the more recently suggested classi<sup>fi</sup>cation algorithms. In this paper, we suggest a novel similarity classi<sup>fi</sup>er with multiple ideal vectors per class that are generated with k-means clustering in combination with the jump method. Two approaches for pre-processing, via simple standardization and via principal component analysis in combination with the MAP test and Parallel Analysis, are presented. On the arti<sup>fi</sup>cial data sets, the novel classi<sup>fi</sup>er with standardization and with transformation power Y = 1 for the jump method results in signi<sup>fi</sup>cantly higher mean classi<sup>fi</sup>cation accuracies than the standard classi<sup>fi</sup>er. The results of the arti<sup>fi</sup>cial data sets demonstrate that in contrast to the standard similarity classi<sup>fi</sup>er, the novel approach has the ability to cope with more complex data structures. For the real-world credit data sets, the novel similarity classi<sup>fi</sup>er with standardization and Y = 1 achieves competitive results or even outperforms the k-nearest neighbour classi<sup>fi</sup>er, the Naive Bayes algorithm, decision trees, random forests and the standard similarity classi<sup>fi</sup>er.

## 1. Introduction

## 1.1. Background

One common type of problem in machine learning is classi<sup>fi</sup>cation, which means using characteristics of observations to assign these observations to discrete classes [4]. Classi<sup>fi</sup>cation algorithms support the decision-making for enterprises and individuals in numerous applications, including medical diagnostics [28], product positioning [26], recommendation systems [21] and sentiment analysis in social media [13]. A common interest in these algorithms in <sup>fi</sup>nance is with respect to the evaluation of the creditworthiness of customers and for the credit granting decision [13,19,42].

In the literature, researchers and practitioners can <sup>fi</sup>nd a manifold of algorithms to conduct a classi<sup>fi</sup>cation tasks, which include, but are not limited to, the well-known neural networks, support vector machines, decision trees, k-nearest neighbours, random forests and numerous more. One of the more recently developed and applied classi<sup>fi</sup>ers is the similarity classi<sup>fi</sup>er [33]. The <sup>fi</sup>rst results for the similarity classi<sup>fi</sup>er were published in Luukka et al. [33]. Since then, the classi<sup>fi</sup>er has been applied to several medical data sets [28,32] and to two bankruptcy data sets [30], showing high classi<sup>fi</sup>cation accuracies. Moreover, Luukka & Leppälampi [32] demonstrated that the similarity classi<sup>fi</sup>er outperforms classi<sup>fi</sup>ers such as linear discriminant analysis, the C4.5 algorithm [36] and multi-layer perceptron neural networks on the medical data sets in their study. Luukka [29] even deployed the classi<sup>fi</sup>er on linguistic statements that were transformed into fuzzy numbers. Overall, the advantages of the similarity classi<sup>fi</sup>er are that it is comparably computationally inexpensive and requires only a small amount of observations to achieve high classi<sup>fi</sup>cation results [28].

The similarity classi<sup>fi</sup>er is premised on the idea to represent each class in the data by one so-called ideal vector, which can be, for instance, determined with a generalized mean. Each ideal vector is essentially a point in the feature space and the class assignment is conducted based on the highest similarity of an observation with one of these points that represent the classes. The idea of similarity is closely related to the concept of distance [14] and the similarity classi<sup>fi</sup>er can be regarded as a distance-based technique. Luukka & Lampinen [31] pointed out that distance-based techniques may face di<sup>fi</sup>culties to classify complex data structures. Hence, Luukka & Lampinen [31] introduced the di<sup>f</sup>erential evolution based multiple vector prototype classi<sup>fi</sup>er (MVDE). Their approach included de<sup>fi</sup>ning multiple vectors that represent each class. This approach demonstrated to be able to handle data structures for which a simple distance-based technique was not su<sup>fi</sup>cient [31]. However, Luukka & Lampinen [31] highlighted that the choice of the number of vectors per each class is pivotal for the accuracy of the classi<sup>fi</sup>er performance. The reason behind this is that too few ideal vectors per class may not be su<sup>fi</sup>cient to appropriately capture the data complexity while too many will result in over<sup>fi</sup>tting. As a <sup>fi</sup>nal remark, these authors stated that a subject for future research is to optimize for a given data structure a suitable number of representative class vectors.

## 1.2. Objectives

In this paper, the idea of using multiple representatives, as presented in Luukka & Lampinen [31] in the context of their MVDE classi<sup>fi</sup>er, will be transferred to the context of the similarity classi<sup>fi</sup>er. The aim is to de<sup>fi</sup>ne a novel similarity classi<sup>fi</sup>er that uses multiple idea vectors for the classi<sup>fi</sup>cation. This should enable to classify more com plex data structure, including those that are characterized by multiple decision regions for each class, better than the standard similarity classi<sup>fi</sup>er as presented in Luukka et al. [33]. As a second contribution, the authors in this paper clearly address the research need mentioned by Luukka & Lampinen [31] to provide a framework for the choice of the number of representatives of a class, which is in case of the simi larity classi<sup>fi</sup>er the number of ideal vectors. The number and position of these ideal vectors is pivotal for the classi<sup>fi</sup>cation since the distancebased classi<sup>fi</sup>er's ability to capture complex data structures but at the same time not to over<sup>fi</sup>t the data depends on it. In this paper, a novel approach for the similarity classi<sup>fi</sup>er will be presented, where k-means clustering in combination with the jump method is conducted to determine suitable multiple deal vectors for each class. The multiple ideal vectors are then used within the similarity classi<sup>fi</sup>er to assign class la bels to observations. The novel similarity classi<sup>fi</sup>er aims to overcome the problem of classifying observations with complex data structures.

In particular, we will illustrate the inability of the standard simi larity classi<sup>fi</sup>er to cope with more complex data structures with arti<sup>fi</sup> cial data sets and contrast its result to the novel similarity classi<sup>fi</sup>er.

The remaining paper is structured as follows: in Section 2 the methods deployed for the novel similarity classi<sup>fi</sup>er approach will be introduced and the arti<sup>fi</sup>cial and real-world data sets will be depicted, on which the standard and the novel classi<sup>fi</sup>er are applied in order to compare their performances. Moreover, the training procedure for the classi<sup>fi</sup>ers will be described. In Section 3, the results of the comparison will be presented, which will subsequently be discussed in detail in Section 4.

## 2. Methods

## 2.1. K-means clustering

Clustering in general is concerned with <sup>fi</sup>nding clusters that en compass observations that are similar to one another and dissimilar to those observations in other clusters [11]. In other words, observations in a cluster have small inter-point distances in relation to the distance to observations in other clusters [4]. The k-means clustering algorithm is one of the <sup>fi</sup>rst and widely applied hard clustering algorithms [11,24]. The process behind k-means clustering is rather simple. Initially, one observation for each cluster is chosen randomly and used as the centroid for the initial cluster [11]. In an iterative procedure, each observation is assigned <sup>fi</sup>rst to the nearest cluster and, second, the cluster centre is adjusted to represent all observations in the cluster [4]. The assignment of an observation i to the cluster with the closest cluster centre can be expressed as [4,12]:

$$
u _ {i j} = \left\{ \begin{array}{l l} 1 & \text { if } \| x _ {i} - \mu_ {j} \| ^ {2} <   \| x _ {i} - \mu_ {j ^ {\prime}} \| ^ {2} \text { for   all } j ^ {\prime} \neq j \\ 0 & \text { Otherwise } \end{array} \right.\tag{1}
$$

For the second step, the centre of the closest cluster is adapted fo the new additional observation. A cluster centre μ is updated as [4]:

$$
\mu_ {j} = \frac {\sum_ {i} u _ {i j} x _ {i}}{\sum_ {i} u _ {i j}}\tag{2}
$$

The objective function that will be minimized with respect to the membership coe<sup>fi</sup>cients and cluster centres is [4,24]:

$$
J = \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {k} u _ {i j} x _ {i} - \mu_ {j} ^ {2}\tag{3}
$$

This function represents the sum of squared distances of each observation to its cluster centre [4].

## 2.2. Jump method

An essential aspect of the k-means algorithm is that the data is partitioned into K clusters. However, K, the number of clusters, has to be speci<sup>fi</sup>ed in order to conduct the clustering and the choice of K is nontrivial [4]. The problem for choosing K arises from the fact that the total squared distance, which is commonly used in the evaluation of a clustering, will always prefer more clusters to less. Therefore, using this way of evaluating clusters will end up choosing as many clusters as observations are available [47]. In the literature, many approaches to determine a suitable number of clusters can be found. These include the ‘Elbow method’, the ‘Gap statistic’ [40], the ‘Jump method’ [39] and the ‘Calinski-Harabasz index’ [6]. For the novel similarity classi<sup>fi</sup>er, the k-means with the jump method is chosen since this approach is theoretically motivated, applicable for a wide range of problems and mixture distributions, and even performs well when clusters are overlapping to a large extent [39]. The ‘jump method’ developed by Sugar & Gareth [39] is related to rate distortion theory. Distortion is a measure for the dispersion within clusters [11]. The minimum distortion $d _ { k }$ obtainable with K cluster centres is [39]:

$$
d _ {K} = \frac {1}{p ^ {c _ {1} , . . . , c _ {K}}} \min E [ (X - c _ {X}) ^ {T} \Gamma^ {- 1} (X - c _ {X}) ]\tag{4}
$$

where X is a p-dimensional random variable with a mixture distribution with G components and covariance matrix Γ for X. In addition, $c _ { 1 } , . . . , c _ { K }$ are the candidates for the K cluster centres, $c _ { X }$ is the cluster centre that is closest to $X ,$ and T indicates the transpose. For the use in practice, the distortion $d _ { K }$ can be estimated based on the minimum distortion $\widehat { d } _ { K }$ obtained in the k-means clustering [39]. The covariance matrix Γ might in practice not be known. However, Sugar & Gareth [39] stress that the identity matrix can be used as a simpli<sup>fi</sup>cation, which makes $\widehat { d } _ { K }$ the mean squared error. They deployed this approach and found it to be robust concerning the shape of the distortion curve for di<sup>f</sup>erent covariance matrices [39]. Consequently, the minimum distortions can easily be obtained given the observations and K clusters. The ‘jump method’ can be stated as follows [39]:

1. Conduct k-means clustering with a di<sup>f</sup>erent number of clusters from 1 to K and determine the values for ${ \widehat { d } } _ { K } ,$ , the distortions that correspond to the number of clusters

2. Choose the parameter called ‘transformation power’ denoted by ${ \cal Y } ,$ where $Y > 0 ,$ , which is required for the calculation of the ‘jumps’ in the next step. A common choice is ${ \tt Y } = { \tt p } / 2$

3. Transform the distortions with the transformation power Y by computing $\widehat { d } _ { K } ^ { - Y }$ . Calculate ‘jumps’ as $J _ { K } = \widehat { d } _ { K } ^ { - Y } - \widehat { d } _ { K - 1 } ^ { - Y }$ , which is the di<sup>f</sup>erence between the transformed distortions of k-means clustering with K clusters compared to K-1 clusters

4. Determine the estimated number of clusters denoted $K ^ { * }$ as the k corresponding to the largest ‘jump’, which is the maximum $J _ { K } .$ . In order to be able to obtain as a result $K = 1$ , the distortion for no clusters is de<sup>fi</sup>ned as $\widehat { d } _ { 0 } ^ { - Y } = 0$

The choice of the Y parameter, the transformation power, is no straight forward. For uncorrelated features and Gaussian clusters, Sugar & Gareth [39] suggest choosing $Y = { \mathsf { p } } / 2 ,$ , where p is the number of dimensions of the data. However, features are often correlated to a certain extent and do not need to be in Gaussian clusters. If it is impractical to analyse the cluster distribution, Sugar & Gareth [39] recommend to either use a relatively low value for the transformation power Y (e.g. 1 or even lower) or to determine Y with the help of the ‘e<sup>f</sup>ective’ dimension of the data set. In this paper, two approaches will be considered, selecting Y premised on the ‘e<sup>f</sup>ective’ dimensionality or simply setting it to 1.

## 2.3. ‘Efective dimensionality’

In an example, Sugar & Gareth [39] explain that the e<sup>f</sup>ective dimensionality of a data set is lower than the dimensionality of the feature space if there are features that are highly correlated. In this paper, we will use principal component analysis to transform the data into uncorrelated principal components [1,20]. We will keep only a subset of all principal components, since the <sup>fi</sup>rst principal components are often enough to represent the overall data set and its variance well [11]. Since the new features are uncorrelated, their e<sup>f</sup>ective dimension should be equal to their dimension. Yet, the choice of how many of the principal components should be retained is not trivial [35,43]. Ex tracting too few principal components will result in a loss of information while extracting too numerous principal components might include irrelevant information or noise [7,51].

In the literature, various methods to determine a suitable number of principal components can be found [7]. These methods include, but are not limited to, the modi<sup>fi</sup>ed broken stick model [7], the Guttman-Kaiser criterion [17,22], the SCREE test [8], the Minimum Partial Average (MAP) test [43], Bartlett's test [2] and Parallel Analysis [18]. Of these methods, the MAP and Parallel Analysis demonstrated the highest performance across di<sup>f</sup>erent data complexities [35,50,51]. The minimum average partial (MAP) test is based on conducting a PCA and subsequently analyse the matrix of partial correlations $[ 7 , 3 5 , 4 3 , 5 0 ]$ The idea behind this procedure is that the average squared partial correlation will decline until a ‘unique’ component would be removed [43,50]. Therefore, the stopping point is reached at the minimum average squared partial correlation [44,50]. According to Velicer [43] the method results in an exact stopping point for the selection of principal components. Velicer et al. [44] <sup>fi</sup>nd that the average of the partial correlations to the fourth power outperforms the initial ap proach with average squared partial correlations for continuous data. A disadvantage of the MAP is that it can in certain situations under estimate the number or principal components to select [50].

The second highly recommended approach is Parallel Analysis developed by Horn [18] [44,50]. It is based on the criticism that the proof for another well-known approach for choosing the number of principal components, the Guttman-Kaiser criterion (also referred to as K1 rule), is concerned with population statistics and, therefore, not applicable for samples [15,18]. Essentially, Parallel Analysis is concerned with <sup>fi</sup>nding those principal components that account for a larger amount of variance than a counterpart based on random data [35]. An alternative approach for Parallel Analysis is to deploy an upper percentile (com monly the 95th) for the distribution of the eigenvalues as explained by Glorfeld [16]. Using this approach decreases the tendency of Parallel Analysis to extract too numerous components [16].

MAP and Parallel Analysis usually lead to the selection of the same principal components to retain [35]. However, since results may di<sup>f</sup>er, applying both approaches is bene<sup>fi</sup>cial since MAP and Parallel Analysis complement each other given that the <sup>fi</sup>rst may extract too few components and the second too many [35,51].

## 2.4. Novel classification algorithm

The idea of the similarity classi<sup>fi</sup>er originates in fuzzy theory. Fuzzy theory is based on the idea that a number of non-mathematical properties cannot be re<sup>fl</sup>ected by crisp sets since they solely indicate whether a certain property is present or not [23]. In contrast to that, fuzzy sets re<sup>fl</sup>ect a membership degree to a class or property [49]. Using membership degrees allows to model partial memberships. This is of interest for classi<sup>fi</sup>cation since it allows partial membership of an ob servation to classes [33]. As a consequence, the similarity measure can be used as a classi<sup>fi</sup>er using the partial membership values of an observation to classes in order to assign an observation to the class it is most similar to. This type of classi<sup>fi</sup>cation is referred to as supervised classi<sup>fi</sup>cation since the class label of observations is known [4,45].

The similarity classi<sup>fi</sup>er presented by Luukka et al. [33] was premised on the idea to compute for each class one so-called ‘ideal vector’ that is supposed the represent that class well. There are several ways of computing ideal vectors, of which arithmetic mean is one of the earliest methods used. To classify an observation, it is compared to the ideal vector of each class and, eventually, a similarity value is calculated. The similarity embodies a membership degree for an observation to a class. The class assignment is then simply conducted based on the highest similarity, meaning that the observation is assigned to the class for which is shows the highest membership degree (between [0,1]). For more details, please see Luukka et al. [33] and Luukka [28].

The novel similarity classi<sup>fi</sup>er algorithm is premised on the idea to represent each class by multiple ideal vectors. The k-means clustering algorithm with the jump method will be deployed in order to determine the ideal vectors per class and gives a clear answer to the question how many ideal vectors per class should be constructed. An observation is then assigned to the class that corresponds to the ideal vector it is closest to. This approach seems suitable in case that classes have one or more decision regions that can be represented by one or more clusters. It should be even adequate when the clusters representing the decision regions overlap since using the jump method has demonstrated to perform well even when clusters overlap to a large extent [39]. The idea is related to the K-Nearest Neighbour (KNN) algorithm but attempts to be more robust for classi<sup>fi</sup>cation by <sup>fi</sup>nding the nearest cluster instead of the nearest neighbours to conduct the class assignment. Opposed to KNN, it is not necessary to de<sup>fi</sup>ne the number of nearest neighbours/ clusters, since the nearest cluster aims at representing the nearest region where observations of a class are located.

The novel algorithm can be characterized by several distinct steps, which are illustrated in a <sup>fl</sup>ow chart in Fig. 1 and depicted in detail subsequently.

Step 1: Data pre-processing. Before the novel similarity classi<sup>fi</sup>er algorithm is applied, the input data require pre-processing. We examined two di<sup>f</sup>erent setups: one based on simple standardization to the compact interval [0,1] and using the original features of the data set, and, a second one, based on normalization of the raw data, so that that they follow a standard normal distribution and using PCA to extract new features from the existing features in the data. For the second approach, a combination of MPA and PA can be used to select a suitable number of principal components, as recommended by O'Connor [35], and subsequently standardize them to the compact interval [0,1] in order for the similarity classi<sup>fi</sup>er to be applicable.

Step 2: Division of the data set. The available data is divided into a training set and a test set via the hold-out method (e.g. 70% training samples and 30% test samples).

Step 3: Conduct k-means clustering for each class. For the training data, the k-means clustering is performed for each class. The clustering is performed for each suggested number of clusters from 1 to $K ,$ where $K$ is a user-speci<sup>fi</sup>ed number. For each number of clusters $K ,$ the average distortion over the observations $x _ { i }$ from i = 1 to N is estimated as:

$$
\widehat {d} _ {K} = \frac {1}{N} \sum_ {i = 1} ^ {N} \sum_ {k = 1} ^ {K} \frac {u _ {i k} ^ {*} (x _ {i} - c _ {k}) ^ {T} \Gamma^ {- 1} (x _ {i} - c _ {k})}{p}\tag{5}
$$

![](/api/attachments/VT36U6Q9/fulltext/images/6a746459d443b8e6640536ad93877324933b344b4eb6bc59fb2e5b2b478e663e.jpg)  
Fig. 1. Flowchart of the similarity classi<sup>fi</sup>er with multiple ideal vectors.

where $u _ { i k }$ shows the membership of an observation $x _ { i }$ to cluster $c _ { k } ,$ which takes for the cluster with the closest cluster centre the value 1 and otherwise 0:

$$
u _ {i k} = \left\{ \begin{array}{l l} 1 & \text { if } \| x _ {i} - c _ {k} \| ^ {2} <   \| x _ {i} - c _ {k ^ {\prime}} \| ^ {2} \text { for   all } k ^ {\prime} \neq k \\ 0 & \text { Otherwise } \end{array} \right.\tag{6}
$$

This notation di<sup>f</sup>ers in certain elements from the one presented above from Sugar & Gareth [39]. First, the minimization of the dis tortion with respect to the cluster centres for a given K is conducted already in the k-means algorithm, so that is not present in this formula any more. Second, we use the membership to a cluster in our formula and include all clusters in it since it appeared more straight-forward for the implementation then using $c _ { X }$ for the notation as the closest cluster centre. The x denotes a p-dimensional observation and is the covar iance matrix for $X ,$ the data set, but can for reasons of simplicity be the identity matrix, as explained before. The cluster centre candidates are denoted $c _ { 1 } , . . . , c _ { K }$ and T indicates the transpose. The distortion estimate $\widehat { d } _ { K }$ is obtained by summing for each observation $x _ { i }$ over the cluster centres from 1 to K and then summing over the observations themselves and taking the average over the observations. The outcome for the class-speci<sup>fi</sup>c clustering is a distortion vector with each element being a value of $\widehat { d } _ { K }$ corresponding to a speci<sup>fi</sup>c number of clusters K.

Step 4: Determine optimal number of clusters for each class. For the jump method, the transformation power Y is then used in the exponent of the distortions $\widehat { d } _ { K }$ to obtain $\widehat { d } _ { K } ^ { - Y }$ . Afterwards, the ‘jumps’, meaning the di<sup>f</sup>erences between subsequent values of these transformed distortions $\widehat { d } _ { K } ^ { - Y }$ , are calculated as:

$$
J _ {K} = \widehat {d} _ {K} ^ {- Y} - \widehat {d} _ {K - 1} ^ {- Y}\tag{7}
$$

where $J _ { K }$ is the jump between the distortions of using K and K-1 clusters on the training data. The number of clusters where the maximum jump J<sub>K</sub> can be observed, is the candidate for the optimal number of clusters. The cluster centres that correspond to the candidate for the optimal number of clusters is recorded/saved. To choose the optimal number of clusters for each class, the k-means clustering (Step 3) and the Jump method (Step 4) are repeated n times (e.g. n = 10). This eventuates in n candidates for the optimal number of clusters for the class. The number of clusters for a class is then chosen as the most frequent candidate number of clusters suggested (mode-value).

Step 5: Record ideal vector candidates. For future steps, the cluster centres of all of the n repetitions of Step 3 and Step 4 that also led to the optimal number of clusters are recorded/saved. Therefore, for each class, there are one or more sets of ideal vector candidates.

Step 6: Training with ideal vector candidates. For each class, a randomly selected set of ideal vector candidates from those saved in the previous step is chosen and they are used together for the similarity classi<sup>fi</sup>er. The calculations in this step correspond to a large extent to those of the original similarity classi<sup>fi</sup>er with the di<sup>f</sup>erence that each set of ideal vector candidates contains multiple ideal vectors. First, for each feature d the similarity between each ideal vector candidate $\nu _ { o }$ and each sample (vector), for simplicity of the index notation denoted x instead of $x _ { i } ,$ of the training set is calculated as:

$$
S (x _ {d}, v _ {o, d}) = \sqrt [ p ]{1 - | x _ {d} ^ {p} - v _ {o , d} ^ {p} |}\tag{8}
$$

where $x _ { d }$ denotes the d-th element of the vector of observation x and $\nu _  o , $ $d$ is the d-th element of the ideal vector $\nu _ { o } .$ Moreover, p is a parameter for the similarity that is in the most basic case set to 1. Afterwards, the generalized mean from this similarity vector is computed by summing over all features d and then dividing by the number of features denoted by D to obtain the similarity of the observation x with the entire ideal vector candidate $\nu _ { o } .$

$$
S (x, v _ {o}) = \left(\frac {1}{D} \sum_ {d = 1} ^ {D} S (x _ {d}, v _ {o, d}) ^ {m}\right) ^ {\frac {1}{m}}\tag{9}
$$

where m is a parameter for the applied mean function and $S ( x , \nu _ { o } )$ represents the scalar similarity value of the observation x with the ideal vector $\nu _ { o } .$ . This is repeated for all ideal vectors to obtain for the observation x the similarity with all clusters (for all classes). Finally, observation x is assigned to a cluster based on the highest similarity value that the observation has with the ideal vector (candidate) of a cluster:

$$
C l (x) = \underset {o = 1, \ldots , O} {\arg \max} S (x, v _ {o})\tag{10}
$$

Since the cluster to which x is assigned, belongs to one of the classes, the observation is assigned to the corresponding class. This can be formally expressed as a simple mapping from the cluster Cl of the observation x to the class C:

$$
C (x) = f (C l (x))\tag{11}
$$

Repeating these calculations of Step 6 for each observation gives all the predicted class labels. These are compared to the target class labels in the training data set and the classi<sup>fi</sup>cation accuracy (or another evaluation criterion) is calculated. The evaluation criterion can be speci<sup>fi</sup>ed by the user, for instance also the False-Positive-Rate (FPR) or the False-Negative-Rate (FNR) on the training set can be chosen as evaluation criterion. For the given combination of sets of ideal vector candidates for each class, this evaluation criterion is computed. The calculations in this step are repeated (e.g. 50 times) and for each run a di<sup>f</sup>erent combination of sets of ideal vectors are used and the value for the evaluation criterion and the corre sponding ideal vector candidates (for all classes) are recorded.

Step 7: Choice of ideal vectors. The combination of sets of ideal vector candidates that resulted in the best value for the evaluation criterion for the training set, e.g. the highest performance, are chosen as the ideal vectors for the similarity classi<sup>fi</sup>er. This allows to customize the choice of ideal vectors to the evaluation criterion. The authors suggest for instance to choose the ideal vectors to maximise the mean accuracy or minimize the False-Negative-Rate or False Positive-Rate, depending on the application and objective.

Step 8: Calculation of the test set performance. The ideal vectors obtained from the previous Step 7 are deployed with the similarity classi<sup>fi</sup>er on the test data set from Step 2. The calculation of the similarities, the assignment of classes and of the performance are conducted with the formulas (8) to (11) from Step 6.

## 2.5. Data

For this paper, three arti<sup>fi</sup>cial data sets are generated to investigate the di<sup>f</sup>erence between the original and novel similarity classi<sup>fi</sup>er approaches. In addition to that, three real-world data sets were obtained from the UCI Machine Learning Repository [27] to compare the performance of these approaches with other well-known supervised clas si<sup>fi</sup>cation algorithms.

The three arti<sup>fi</sup>cially composed data sets are all characterized by multiple decision regions for each class. This setup is supposed to demonstrate the novel similarity classi<sup>fi</sup>er's ability to use multiple ideal vectors to cope with more complex decision regions than the original similarity classi<sup>fi</sup>er using only a single ideal vector. Moreover, the performance with di<sup>f</sup>erent pre-processing and Y parameters is in vestigated. The speci<sup>fi</sup>c features for each of the three arti<sup>fi</sup>cial datasets A, B and C is depicted in Table 1.

The <sup>fi</sup>rst data set, Case A, normally distributed features with small variations are generated that form two-dimensional clusters for each class. In this data set small overlap of classes is present, but the feature space can almost distinctly be divided into the multiple decision regions for each class. The second arti<sup>fi</sup>cial data set, referred to as Case B, is related to the binary XOR problem with the three-dimensional feature space being divided into two distinct decision regions for each class (overall 4 decision regions). The last case, Case C, is characterized by a three-dimensional feature space for a 4-class classi<sup>fi</sup>cation problem. For each class, there exist two clusters, one cluster with small variation in the data and the other with moderate variation. None of the cluster shows an overlap with another cluster of the same or another class. All

## Table 1

Characteristics of the three arti<sup>fi</sup>cial data sets.

<table><tr><td>Cases</td><td>Observations</td><td>Class</td><td>Feature 1</td><td>Feature 2</td><td>Feature 3</td></tr><tr><td rowspan="9">Case A</td><td rowspan="9">900</td><td>1</td><td>N(1,0.2)</td><td>N(1,0.2)</td><td>-</td></tr><tr><td>1</td><td>N(2,0.2)</td><td>N(2,0.2)</td><td>-</td></tr><tr><td>1</td><td>N(3,0.2)</td><td>N(3,0.2)</td><td>-</td></tr><tr><td>2</td><td>N(3,0.2)</td><td>N(2,0.2)</td><td>-</td></tr><tr><td>2</td><td>N(2,0.2)</td><td>N(1,0.2)</td><td>-</td></tr><tr><td>2</td><td>N(1,0.2)</td><td>N(3,0.2)</td><td>-</td></tr><tr><td>3</td><td>N(3,0.2)</td><td>N(1,0.2)</td><td>-</td></tr><tr><td>3</td><td>N(1,0.2)</td><td>N(2,0.2)</td><td>-</td></tr><tr><td>3</td><td>N(2,0.2)</td><td>N(3,0.2)</td><td>-</td></tr><tr><td rowspan="4">Case B</td><td rowspan="4">1000</td><td>1</td><td>[0, 0.5)</td><td>[0, 0.5)</td><td>[0, 1]</td></tr><tr><td>1</td><td>[0.5, 1]</td><td>[0.5, 1]</td><td>[0, 1]</td></tr><tr><td>2</td><td>[0, 0.5)</td><td>[0.5, 1]</td><td>[0, 1]</td></tr><tr><td>2</td><td>[0.5, 1]</td><td>[0, 0.5)</td><td>[0, 1]</td></tr><tr><td rowspan="8">Case C</td><td rowspan="8">1000</td><td>1</td><td>N(2,0.1)</td><td>N(2,0.1)</td><td>N(2,0.1)</td></tr><tr><td>1</td><td>N(6,0.5)</td><td>N(6,0.5)</td><td>N(6,0.5)</td></tr><tr><td>2</td><td>N(6,0.1)</td><td>N(6,0.1)</td><td>N(2,0.1)</td></tr><tr><td>2</td><td>N(2,0.5)</td><td>N(2,0.5)</td><td>N(6,0.5)</td></tr><tr><td>3</td><td>N(2,0.5)</td><td>N(6,0.5)</td><td>N(2,0.5)</td></tr><tr><td>3</td><td>N(6,0.1)</td><td>N(2,0.1)</td><td>N(6,0.1)</td></tr><tr><td>4</td><td>N(6,0.5)</td><td>N(2,0.5)</td><td>N(2,0.5)</td></tr><tr><td>4</td><td>N(2,0.1)</td><td>N(6,0.1)</td><td>N(6,0.1)</td></tr></table>

features are scaled into the compact interval [0,1]. The three arti<sup>fi</sup>cial data sets are plotted in Fig. 2.

The real-world data sets discussed in this paper are all related to the approval and quality of credit borrowers. It seemed reasonable to use these data sets since we assumed that distinct decision regions for good and bad applicants exist and that they can be characterized rather well in form of multiple clusters. Moreover, the class imbalance that is common for many credit default/approval problems, meaning that one class can be considerably larger than the other, is assumed to be more e<sup>f</sup>ectively addressed with a classi<sup>fi</sup>er based on clusters than e.g. simply based on nearest neighbours. However, we want to remark, that our selection for real-world data sets is by no means exhaustive and knowing in advance in what real-world data sets this is useful is not possible.

The subject of credit approval is essential for <sup>fi</sup>nancial institute since they require approaches to support the decision-making for loan applications as well as for the ongoing monitoring of the <sup>fi</sup>nancial situation of their clients [42,46]. The credit granting decision copes with the risk of granting credits to not suitable applicants and the non-acceptance of credits for solvent clients [25]. The classi<sup>fi</sup>cation of clients is particularly important since a credit scoring that is conducted effectively will most likely lead to savings in the future [48].

The <sup>fi</sup>rst credit data set is available at the UCI Machine Learning Repository as ‘Credit Approval Data Set’. It is listed as a ‘Financial’ data set and neither the date of donation nor the author is known. The data set contains 690 observations of 15 features related to credit card applications. Six features are continuous. The remaining attribute values in the data set have been adjusted to meaningless symbols by the donor. We changed these symbols for the similarity classi<sup>fi</sup>er into discrete in teger values. The class label is binary and indicates whether a credit was granted to a client or if the credit proposal was rejected. The features characterize the client and represent properties of the credit decision. The ‘Credit Approval’ data set contains missing values, which have been removed for this study, which leaves 653 complete observations for the classi<sup>fi</sup>cation task.

The second real-world data set is the numeric version of the ‘Statlog (German Credit Data) Data Set’. The original data set was donated by Professor Dr. Hans Hofmann in 1994 and adjusted by Strathclyde University by changing categorical features into numeric integer-valued ones. This data set encompasses 1000 observations with 24 numeric features. It does not contain any missing values. The data are characterized by two classes, which represent the evaluation if a person is a good or bad credit-taker and the 24 features embody characteristics of the credit borrower. In contrast to all other data set, the imbalance in this data set was high with 70% belonging to the <sup>fi</sup>rst group and 30% to the second.

The third and last real-world data set is the ‘Statlog (Australian Credit Approval) Data Set’, which is an adapted form of the ‘Credit Approval Data Set . Neither the donor nor the date of donation for this data set is known. This <sup>fi</sup>nancial data set is also related to credit card applications. The data set contains 690 observations without missing values. The 14 features, of which 6 are continuous and 8 are discrete, represent the characteristics of a credit applicant. The binary class label indicates whether the credit decision was positive or negative.

## 2.6. Data pre-processing and training process

As mentioned above, one out of two approaches for the pre-pro cessing in this paper is based on principal component analysis and choosing a suitable number of principal components as new features. For the choice of the number of principal components, Parallel Analysis (with 1000 random data sets) as the upper bound for the number of components, and MAP will be used. If the result di<sup>f</sup>ers between MAP [44] and PA, it will be investigated whether the MAP decision was ‘close’. Since the authors did not <sup>fi</sup>nd a speci<sup>fi</sup>cation for what con stitutes a ‘close call’ [35], it is de<sup>fi</sup>ned as an increase of the average partial correlations per step of < 70% points. The reasoning behind this choice is that in the regarded cases in this paper, changes per additional component that showed a di<sup>f</sup>erence of up to 70% points appeared small compared to larger changes that were characterized by increases of at least 100% for an additional component. Therefore, the 70% points threshold for an additional component appears to be justi<sup>fi</sup>ed.

![](/api/attachments/VT36U6Q9/fulltext/images/3d41184aadc45b6cbbca7f0c9cebaf579884f679b06284cc4c614387499257ee.jpg)

![](/api/attachments/VT36U6Q9/fulltext/images/4990b71f66f2ddba25352b3162c73ba14c3b9ffc07779fa7f94b59d5a8b0bb92.jpg)  
Fig. 2. Arti<sup>fi</sup>cial data sets.  
compared to the K-nearest neighbour algorithm [10], the Naive Bayes classi<sup>fi</sup>er [38], decision trees [37] and the ensemble learning algorithm called random forest [5]. All calculations are implemented with the MATLAB™- software. The code for the MAP and PA are based on Matlab-<sup>fi</sup>les provided by O'Connor [34].

For the k-means clustering, we suggest K, the maximum number of clusters that k-means is performed with, to be set as the maximum of, <sup>fi</sup>rst, 10 clusters and, second, of the number of observations contained in the smallest class divided by 20. This should ensure that the number of clusters K is only set larger than 10 if on average 20 or more observations will be contained in a cluster. If the data set is small or the minority class(es) encompass few observations, the minimum number of clusters might have to be reduced below 10 to avoid a potential over<sup>fi</sup>t. On the other hand, if the data set is large, the average number of observations per cluster to allow additional clusters can be set higher to capture all pattern contained in the data.

For the classi<sup>fi</sup>cation, the data is divided with the holdout method and using strati<sup>fi</sup>ed sampling. For all algorithms in this paper the ob servations were split into 70% training data and the remaining 30% for testing. For all classi<sup>fi</sup>ers, despite the standard and novel similarity classi<sup>fi</sup>ers, 1000 iterations are performed during the training of the classi<sup>fi</sup>ers.

For the standard and novel similarity classi<sup>fi</sup>ers, the entire algorithm is run for di<sup>f</sup>erent combinations of the p- (varied from 1 to 8) and m-parameter (varied from 1 to 6) to <sup>fi</sup>nd the values for p and m with which highest mean accuracy for the given dataset can be reached. This is referred to as ‘optimal value search’ and for each combination of p and m, 100 iterations of the algorithm are performed before the mean performances are computed. In general, conducting the optimal value search increases the number of required computations to improve the mean classi<sup>fi</sup>cation accuracy. In order to avoid increasing the computational complexity notably, 100 iterations are conducted with optimal value search as opposed to 1000 iterations for the remaining classi<sup>fi</sup>- cation algorithms.

For the novel similarity classi<sup>fi</sup>er, the number of clusterings n (in Step 3 and 4 of the algorithm) was set to 10 and the random combinations for the ideal vector candidates was chosen to be 50 (Step 6 of the algorithm).

For the simpli<sup>fi</sup>ed arti<sup>fi</sup>cial data sets with known structure using the standard parameters p = 1 (parameter for similarity) and $\mathbf { m } = 1$ (parameter for the generalized mean) for all similarity classi<sup>fi</sup>ers is su<sup>fi</sup>cient, since the data structures are simple enough to <sup>fi</sup>nd very good solutions without an optimal value search. For the real-world data sets, the performance of the novel and original similarity classi<sup>fi</sup>ers is

## 3. Results

## 3.1. Results for the artificial data sets

First. the results for the artificial datasets are presented in Table 2. For the <sup>fi</sup>rst arti<sup>fi</sup>cial dataset, Case A, the standard classi<sup>fi</sup>er in the three-class problem shows a mean accuracy of only 32.47%. In contrast to that, the mean accuracy of the novel similarity classi<sup>fi</sup>ers is 96.97% and 96.87% respectively. It has to be stressed, that for the two-dimensional Case A transformation power ${ \tt Y } = { \tt p } / { 2 }$ is also equal 1 (since p is in the context of the jump method the dimensionality). Consequently, the results in Case A are for both novel classi<sup>fi</sup>ers essentially equal. Using the one-sided version of the Welch's test with unequal variance to test whether one population mean is larger than another, the means for the novel similarity classi<sup>fi</sup>er with both transformation powers are highly signi<sup>fi</sup>cantly larger than that of the standard classi<sup>fi</sup>er (with > 99.99% con<sup>fi</sup>dence). Clearly, for the two remaining 3-dimensional cases, ${ \tt Y } = { \tt p } / { 2 }$ and Y = 1 do not take the same values. For Case B the highest result is accomplished with the novel similarity classi<sup>fi</sup>er with Y = 1 with 96.53%. For the novel similarity classi<sup>fi</sup>er with transformation power of ${ \mathrm { Y } } = { \mathbf { p } } / 2$ the mean accuracy is 90.49%, which is highly signi<sup>fi</sup>cantly lower than that of the same classi<sup>fi</sup>er with Y = 1. However, only the standard classi<sup>fi</sup>er reaches a mean accuracy of close to 50%. On account of this, the novel similarity classi<sup>fi</sup>ers both perform highly signi<sup>fi</sup>cantly better on Case B than the original similarity classi<sup>fi</sup>er with a single ideal vector. For the last data set, Case C, the standard similarity classi<sup>fi</sup>er reaches for the four-class problem a mean accuracy of 34.93% while the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1$ and ${ \mathrm { Y } } = { \mathbf { p } } / 2$ accomplishes a 100% performance on the non-overlapping class clusters of the data set. This result is once again highly signi<sup>fi</sup>cant compared to the standard classi<sup>fi</sup>er $( \mathrm { w i t h } > 9 9 . 9 9 \%$ con<sup>fi</sup>dence).

Table 2  
Performance for arti<sup>fi</sup>cial data sets with standard parameters.

<table><tr><td>Data set</td><td>Similarity</td><td>Mean accuracy</td><td>Variance</td><td>runs</td><td>Y</td></tr><tr><td>Case A</td><td>Standard</td><td>0.3247</td><td>0.0037</td><td>100</td><td>-</td></tr><tr><td>Case A</td><td>Novel</td><td>0.9697</td><td>0.0001</td><td>100</td><td>p/2</td></tr><tr><td>Case A</td><td>Novel</td><td>0.9687</td><td>0.0001</td><td>100</td><td>1</td></tr><tr><td>Case B</td><td>Standard</td><td>0.5142</td><td>0.0006</td><td>100</td><td>-</td></tr><tr><td>Case B</td><td>Novel</td><td>0.9049</td><td>0.0009</td><td>100</td><td>p/2</td></tr><tr><td>Case B</td><td>Novel</td><td>0.9653</td><td>0.0004</td><td>100</td><td>1</td></tr><tr><td>Case C</td><td>Standard</td><td>0.3493</td><td>0.0081</td><td>100</td><td>-</td></tr><tr><td>Case C</td><td>Novel</td><td>1</td><td>0</td><td>100</td><td>p/2</td></tr><tr><td>Case C</td><td>Novel</td><td>1</td><td>0</td><td>100</td><td>1</td></tr></table>

Table 3  
Performance for arti<sup>fi</sup>cial data sets after optimal value search.

<table><tr><td>Data set</td><td>Similarity</td><td>PC</td><td>Mean accuracy</td><td>Variance</td><td>Y</td></tr><tr><td>Case A</td><td>Standard-PCA</td><td>2</td><td>0.3116</td><td>0.0039</td><td>-</td></tr><tr><td>Case A</td><td>Novel - PCA</td><td>2</td><td>0.9912</td><td>0.0000</td><td>p/2</td></tr><tr><td>Case A</td><td>Novel - PCA</td><td>2</td><td>0.9913</td><td>0.0000</td><td>1</td></tr><tr><td>Case B</td><td>Standard-PCA</td><td>3</td><td>0.4824</td><td>0.0005</td><td>-</td></tr><tr><td>Case B</td><td>Novel - PCA</td><td>3</td><td>0.9028</td><td>0.0011</td><td>p/2</td></tr><tr><td>Case B</td><td>Novel - PCA</td><td>3</td><td>0.9613</td><td>0.0001</td><td>1</td></tr><tr><td>Case C</td><td>Standard-PCA</td><td>3</td><td>0.3135</td><td>0.0085</td><td>-</td></tr><tr><td>Case C</td><td>Novel - PCA</td><td>3</td><td>1</td><td>0</td><td>p/2</td></tr><tr><td>Case C</td><td>Novel - PCA</td><td>3</td><td>1</td><td>0</td><td>1</td></tr></table>

The performance of the novel similarity classi<sup>fi</sup>er and the standard similarity classi<sup>fi</sup>er are also tested with the suggested pre-processing with PCA. The mean accuracies obtained with this pre-processing are highlighted in Table 3. The magnitude of the performances for the ar ti<sup>fi</sup>cial data sets is comparable with those without PCA. For Case 3 both transformation powers for the novel classi<sup>fi</sup>er eventuate in a 100% mean accuracy. Overall, the results for all arti<sup>fi</sup>cial data sets show that the novel similarity classi<sup>fi</sup>er with and without PCA as pre-processing clearly outperforms the standard similarity classi<sup>fi</sup>er with the mean accuracy being in all cases highly signi<sup>fi</sup>cantly larger (with > 99.99% con<sup>fi</sup>dence). However, the di<sup>f</sup>erence in the performances with the two transformation powers Y can be signi<sup>fi</sup>cant, as was observed for Case B. Overall, these arti<sup>fi</sup>cially created classi<sup>fi</sup>cation problems clearly show the advantage of the proposed novel method compared to the standard similarity classi<sup>fi</sup>er.

The results for the arti<sup>fi</sup>cial data sets are calculated only for the default parameters for the similarity of $\mathsf { p } = 1$ and $\mathbf { m } = 1$ , since the results of the novel similarity classi<sup>fi</sup>er are already high and only a marginal improvement could be expected for these data sets.

## 3.2. Results for the real-world data sets

In this next step, the results of the real-world credit data sets achieved with the similarity classi<sup>fi</sup>ers and di<sup>f</sup>erent pre-processing methods are presented and compared with the performances of the KNN algorithm, the Naive Bayes classi<sup>fi</sup>er, decision trees and random forests on these credit data sets.

The performance of all classi<sup>fi</sup>ers on the <sup>fi</sup>rst real-world data sets, the ‘Credit Approval’ data set, is highlighted in Table 4. The <sup>fi</sup>rst seven classi<sup>fi</sup>ers presented there are the standard and novel similarity classi-<sup>fi</sup>er with di<sup>f</sup>erent pre-processing methods. The remaining 9 classi<sup>fi</sup>ers are di<sup>f</sup>erent setups for the remaining benchmark algorithms. For KNN the result on the test set with a single nearest neighbour, the 10 nearest neighbours and for the optimal number k are displayed. To obtain the optimal number for $k ,$ the KNN algorithm was run for all k from 1 to the training sample size and the result on the test data set for the setup leading to the best mean accuracy on the training data set was chosen and is displayed in the table. For the Naive Bayes classi<sup>fi</sup>er two setups were used: the <sup>fi</sup>rst assumed normal Gaussian distributions, the second used a kernel with normal smoothing. The random forest is composed of 50 decision trees and is implemented in the <sup>fi</sup>rst setup with minimum leafsize of 1. The second setup displays the mean performance on the test data set based on the minimum leafsize (from 10 to 100 by steps of 10) that showed the highest mean training performance. The same procedure was deployed for the two decision tree setups. The di<sup>f</sup>erent leafsizes are tried since too small leafsizes may incorporate noise and harm the generalization ability while too large leafsizes can result in a classi<sup>fi</sup>er that only captures the broadest patterns.

For the ‘Credit Approval’ data set, the highest performance of 87.33% is reached with the ensemble learning algorithm random decision forest with minimum leafsize = 1. This performance is closely followed by the random decision forest with minimum leafsize = 10 with mean accuracy 87.08% and the novel similarity classi<sup>fi</sup>er with transformation power $\mathrm { Y } = 1$ leading to mean performance of 87.06%. Three aspects of this result are noteworthy. First, the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1$ achieves a performance that is competitive to the one of the ensemble learning algorithm, random forest, and possesses the highest mean accuracy for all classi<sup>fi</sup>ers that are based on a single learning algorithm. Second, using the Welch's test (with unequal variances), it can be demonstrated that the mean accuracy accomplished with the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1$ is highly signi<sup>fi</sup>cantly larger than that of the standard similarity classi<sup>fi</sup>er (p-value $< 0 . 0 0 1 )$ . Thirdly, in comparison with all other single learning algorithm-based classi<sup>fi</sup>ers, the mean accuracy of the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1$ shows a highly signi<sup>fi</sup>cant positive di<sup>f</sup>erence in the mean performance. The classi<sup>fi</sup>er mean accuracies with the 4 selected principal components (PCs) in the pre-processing are between 5.42% to 8.09% lower than its direct counterpart without PCA and only standardized initial features.

In credit scoring and for the evaluation of credit applications, the consequences of misclassi<sup>fi</sup>cation are unequal. Consequently, it appears suitable to evaluate the classi<sup>fi</sup>ers' performances also with respect to the False-Negative-Rate (FNR) and the False-Positive-Rate (FPR). For all real-world data sets, the FNR represents the proportion of falsely rejected customers to the sum of falsely rejected customers and the rightfully accepted customers. In other words, it is the share of custo mers that is falsely classi<sup>fi</sup>ed as bad compared to all customers that are actually good. Opposed to that, the FPR is the proportion of falsely accepted customers to the sum of falsely accepted customers and the rightfully rejected ones. The FPR is with respect to credit decisions more relevant than the FNR. In particular, classifying a bad customer falsely as a good one and giving him/her a credit that may not be repaid (as focused on by FPR) outweighs the potential forgone pro<sup>fi</sup>t of assigning a good customer to the bad customer class (as emphasized by FNR) [3,9,41].

Since the FPR is of additional relevance for credit scoring, for each real-world data set one novel similarity classi<sup>fi</sup>er was customized in the choice of ideal vectors with respect to the FNR rate. This classi<sup>fi</sup>er is referred to as ‘Novel Similarity Classi<sup>fi</sup>er (Minimize FPR)’. The lowest FPR rate for the Credit Approval data set of 7.2% is achieved for the standard similarity classi<sup>fi</sup>er. On the other hand, the FNR for this setup belongs with 19.6% to one of the higher rates and is above the mean and median of all classi<sup>fi</sup>ers. The FNR of the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1$ is with 5.6% one of the lowest, while the FPR with 19.0% is above the median of all algorithms. Comparing FPR and FNR stressed that the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1$ performs very well with respect to avoiding allocating good customers in the ‘bad’ class and foregoing pro<sup>fi</sup>ts but worse than the average in recognizing customers that should not be assigned to the ‘good’ class and, therefore, avoiding credit default. The Novel Similarity Classi<sup>fi</sup>er (Minimize FPR) with $\mathrm { Y } = 1$ leads to a slight improvement of the FPR from 19.0% to 15.5% compared to the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1$ that was customized with respect to the mean accuracy. This improvement in FPR was accomplished as a trade-o<sup>f</sup> to the mean accuracy. However, for this data set the ensemble learner random forest still achieved a better FPR and at the same time a higher classi<sup>fi</sup>cation accuracy. The result of the optimal parameter value search for the ‘Credit Approval’ data set with the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1$ is illustrated in Fig. 3.

The surface for the mean accuracy for the novel similarity classi<sup>fi</sup>er appears smooth and high accuracies are achieved and seem robust with respect to several di<sup>f</sup>erent setups of the p and m parameter.

The classi<sup>fi</sup>cation performances for the ‘German Credit’ data set are presented in Table 5. The best mean accuracy for the ‘German Credit’ data set of 75.84% is again reached with the random forest algorithm. Notwithstanding, the highest classi<sup>fi</sup>cation accuracies of single classi <sup>fi</sup>er algorithms is once more accomplished with the novel similarity classi<sup>fi</sup>er with Y = 1. Compared to the remaining single classi<sup>fi</sup>er al gorithms, the novel similarity classi<sup>fi</sup>er's mean classi<sup>fi</sup>cation accuracy is highly signi<sup>fi</sup>cant with the single exception of the standard similarity classi<sup>fi</sup>er based on 8 PCs. Notably, the performance of the standard similarity classi<sup>fi</sup>er with and without PCA belongs to the best mean accuracies for all algorithms on this data set. However, the novel similarity classi<sup>fi</sup>er's mean accuracy is signi<sup>fi</sup>cantly larger than that of the standard similarity classi<sup>fi</sup>er (p-value = 0.0193).

Table 4  
Results for the ‘Credit Approval’ data set (the highest mean accuracy, the lowest FNR and the lowest FPR are highlighted in bold).

<table><tr><td>Classification algorithm</td><td>Mean accuracy</td><td>Variance</td><td>Mean FNR</td><td>Mean FPR</td><td>p</td><td>m</td><td>Y</td></tr><tr><td>Standard similarity classifier</td><td>0.8599</td><td>0.0004</td><td>0.196</td><td>0.072</td><td>6</td><td>4</td><td>-</td></tr><tr><td>Novel similarity classifier</td><td>0.8525</td><td>0.0005</td><td>0.133</td><td>0.160</td><td>1</td><td>1</td><td>p/2</td></tr><tr><td>Novel similarity classifier</td><td>0.8706</td><td>0.0005</td><td>0.056</td><td>0.190</td><td>6</td><td>5</td><td>1</td></tr><tr><td>Novel similarity classifier (minimize FPR)</td><td>0.8615</td><td>0.0003</td><td>0.119</td><td>0.155</td><td>2</td><td>6</td><td>1</td></tr><tr><td>Standard similarity classifier (PCA, 4 PCs)</td><td>0.8057</td><td>0.0005</td><td>0.010</td><td>0.284</td><td>1</td><td>1</td><td>-</td></tr><tr><td>Novel similarity classifier (PCA, 4 PCs)</td><td>0.7716</td><td>0.0008</td><td>0.243</td><td>0.216</td><td>1</td><td>2</td><td>p/2</td></tr><tr><td>Novel similarity classifier (PCA, 4 PCs)</td><td>0.8076</td><td>0.0005</td><td>0.324</td><td>0.085</td><td>4</td><td>4</td><td>1</td></tr><tr><td>K-nearest neighbours, k = 1</td><td>0.8184</td><td>0.0005</td><td>0.207</td><td>0.161</td><td>-</td><td>-</td><td>-</td></tr><tr><td>K-nearest neighbours, k = 10</td><td>0.8608</td><td>0.0004</td><td>0.142</td><td>0.137</td><td>-</td><td>-</td><td>-</td></tr><tr><td>K-nearest neighbours, best k = 1</td><td>0.8184</td><td>0.0005</td><td>0.207</td><td>0.161</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Naive Bayes (normal Gaussian distribution)</td><td>0.8039</td><td>0.0006</td><td>0.321</td><td>0.093</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Naive Bayes (kernel with normal smoothing)</td><td>0.6823</td><td>0.0012</td><td>0.425</td><td>0.230</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Random decision forest (min leafsize = 1)</td><td>0.8733</td><td>0.0004</td><td>0.129</td><td>0.125</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Random decision forest (min leafsize = 10)</td><td>0.8708</td><td>0.0004</td><td>0.126</td><td>0.132</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Decision tree (min leafsize = 1)</td><td>0.8322</td><td>0.0007</td><td>0.194</td><td>0.147</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Decision tree (min leafsize = 10)</td><td>0.8561</td><td>0.0005</td><td>0.157</td><td>0.133</td><td>-</td><td>-</td><td>-</td></tr></table>

For the ‘German credit’ data set, the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1 $ , eventuates in a FPR of 67.4%, which is in absolute terms high but compared to all other algorithms not far from the mean FPR. For the FNR, this classi<sup>fi</sup>er ends up with a value of 9.5%, which belongs to the better results for FNR, being well below the median value. The most accurate classi<sup>fi</sup>ers, the random forests, show FPR values of 58.1% and 66.8%. The tendency of most algorithms to result in high FP rates and lower FN rates appears to be the consequence of the high class imbalance with the positive class being with 70% the apparent majority. However, the novel similarity classi<sup>fi</sup>er that was customized to result in lower FPR values shows the opposite behaviour, being with a low FPR of 17% good at avoiding to give credits to ‘bad’ customers while with 53.5% FNR being worse at not giving credits to ‘good’ customers. Given that the FPR for credit decisions is of higher relevance, this algorithm seems very suitable to reduce potential losses. The result of the optimal parameter value search for the ‘German Credit’ data set of the novel similarity classi<sup>fi</sup>er with Y = 1, is illustrated in Fig. 4. It again shows a rather stable and smooth surface for the mean classi<sup>fi</sup>cation depending on the p and m parameter showing that good classi<sup>fi</sup>cation performances can be reached with di<sup>f</sup>erent setups of these parameters.

The classi<sup>fi</sup>cation results on the third real-world data set, the ‘Australian Credit’ data set, are presented in Table 6. The highest mean accuracy on the ‘Australian Credit’ data set is $8 7 . 3 7 \% ,$ which is achieved with the novel similarity classi<sup>fi</sup>er with transformation power Y = 1. The performance of the standard similarity classi<sup>fi</sup>er with 87.27% embodies the second highest mean accuracy. It is remarkable, that the mean performance of the novel similarity classi<sup>fi</sup>er with Y = 1 not only exceeds the mean performance of the ensemble learner random forest, but this di<sup>f</sup>erence is even highly signi<sup>fi</sup>cant. On top of that, the mean accuracy of the novel similarity classi<sup>fi</sup>er with Y = 1 is highly signi<sup>fi</sup>cantly larger than that of almost all other algorithms - the KNN classi<sup>fi</sup>ers, decision trees, random decision forests, Naive Bayes and the novel similarity classi<sup>fi</sup>ers – with the sole exception of the standard similarity classi<sup>fi</sup>er.

The lowest FPR rate for the ‘Credit Approval’ data set of 9.0% is accomplished with the novel similarity classi<sup>fi</sup>er that was customized to result in low FPR rates. Also, this algorithm still leads to a performance that is competitive or higher than that of the KNN algorithms, the Naive Bayes and the decision trees. The novel similarity classi<sup>fi</sup>er with Y = 1, the best performing algorithm on this data set, is with a FPR of 13.3% still below the average FPR rate of all classi<sup>fi</sup>ers. The FPR of the random forests is with 12.4% and 12.0% in magnitude comparable to that of the novel similarity classi<sup>fi</sup>er with Y = 1. The result of the optimal parameter value search for the Australian Credit data set and the novel similarity classi<sup>fi</sup>er with Y = 1 is illustrated in Fig. 5.

Overall, the novel similarity classi<sup>fi</sup>er achieved for all arti<sup>fi</sup>cial data sets superior classi<sup>fi</sup>cation results to the standard similarity classi<sup>fi</sup>er with only a single ideal vector per class. For the real-world data sets, the novel similarity classi<sup>fi</sup>er with Y = 1 was performing at least as accurate as the standard classi<sup>fi</sup>er, in two data sets it was signi<sup>fi</sup>cantly more accurate than the standard similarity classi<sup>fi</sup>er, in one of them the di<sup>f</sup>erence was even highly signi<sup>fi</sup>cant. Compared to the remaining benchmark algorithms, the novel similarity classi<sup>fi</sup>er showed in most cases competitive result, often even outperforming the benchmark classi<sup>fi</sup>ers.

![](/api/attachments/VT36U6Q9/fulltext/images/42043b6735688e29aa9d0ce9b43994d34c9f7604084360da040857fe7697133d.jpg)

![](/api/attachments/VT36U6Q9/fulltext/images/407fc3d9929d6d371509b93d4c3b480f13bcba5dd247dfe552523b604028fe7f.jpg)  
Fig. 3. Optimal value search for the novel similarity classi<sup>fi</sup>er with Y = 1 (‘Credit Approval’ data set)

Table 5  
Results for the ‘German Credit’ data set (the highest mean accuracy, the lowest FNR and the lowest FPR are highlighted in bold).

<table><tr><td>Classification algorithm</td><td>Mean Accuracy</td><td>Variance</td><td>Mean FNR</td><td>Mean FPR</td><td>p</td><td>m</td><td>Y</td></tr><tr><td>Standard similarity classifier</td><td>0.7263</td><td>0.0003</td><td>0.099</td><td>0.683</td><td>4</td><td>1</td><td>-</td></tr><tr><td>Novel similarity classifier</td><td>0.6822</td><td>0.0005</td><td>0.158</td><td>0.691</td><td>8</td><td>1</td><td>p/2</td></tr><tr><td>Novel similarity classifier</td><td>0.7314</td><td>0.0003</td><td>0.095</td><td>0.674</td><td>4</td><td>1</td><td>1</td></tr><tr><td>Novel similarity classifier (minimize FPR)</td><td>0.5750</td><td>0.0012</td><td>0.535</td><td>0.170</td><td>2</td><td>6</td><td>1</td></tr><tr><td>Standard similarity classifier (PCA, 8 PCs)</td><td>0.7299</td><td>0.0004</td><td>0.142</td><td>0.570</td><td>3</td><td>5</td><td>-</td></tr><tr><td>Novel similarity classifier (PCA, 8 PCs)</td><td>0.6966</td><td>0.0008</td><td>0.281</td><td>0.355</td><td>3</td><td>1</td><td>p/2</td></tr><tr><td>Novel similarity classifier (PCA, 8 PCs)</td><td>0.6998</td><td>0.0006</td><td>0.298</td><td>0.304</td><td>2</td><td>1</td><td>1</td></tr><tr><td>K-nearest neighbours, k = 1</td><td>0.6715</td><td>0.0005</td><td>0.237</td><td>0.543</td><td>-</td><td>-</td><td>-</td></tr><tr><td>K-nearest neighbours, k = 10</td><td>0.7164</td><td>0.0005</td><td>0.162</td><td>0.568</td><td>-</td><td>-</td><td>-</td></tr><tr><td>K-nearest neighbours, best k = 1</td><td>0.6715</td><td>0.0005</td><td>0.237</td><td>0.543</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Naive Bayes (normal Gaussian distribution)</td><td>0.7233</td><td>0.0006</td><td>0.229</td><td>0.388</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Naive Bayes (kernel with normal smoothing)</td><td>0.7068</td><td>0.0001</td><td>0.013</td><td>0.947</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Random decision forest (min leafsize = 1)</td><td>0.7584</td><td>0.0003</td><td>0.096</td><td>0.581</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Random decision forest (min leafsize = 10)</td><td>0.7516</td><td>0.0003</td><td>0.069</td><td>0.668</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Decision tree (min leafsize = 1)</td><td>0.6946</td><td>0.0007</td><td>0.218</td><td>0.510</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Decision tree (min leafsize = 10)</td><td>0.7197</td><td>0.0006</td><td>0.167</td><td>0.545</td><td>-</td><td>-</td><td>-</td></tr></table>

![](/api/attachments/VT36U6Q9/fulltext/images/b470082865b87e34050d3d63c920cb830d47543525733c3383166973110e8f46.jpg)

![](/api/attachments/VT36U6Q9/fulltext/images/ad6e71fe3e1dd89e3123459eb6a968fd98bf28f8a43254e708022db37e187083.jpg)  
Fig. 4. Optimal value search for the novel similarity classi<sup>fi</sup>er with Y = 1 (‘German Credit’ data set).

## 4. Discussion

In this paper, the authors designed a novel similarity classi<sup>fi</sup>er based on k-means clustering. The k-means clustering is deployed in combination with the jump method to determine the number of clusters and also the cluster centres themselves for each class. These clusters are then used as the multiple ideal vectors for each class in the similarity classi<sup>fi</sup>er. It is also possible to a certain extent to customize the classi<sup>fi</sup>er by the choice of the evaluation criterion during the training to focus on the mean accuracy, the False-Positive-Rate (FPR) or another metric. In this research, two methods for pre-processing and for the choice of the transformation power Y are proposed. The <sup>fi</sup>rst one is premised on a simple standardization to $^ { [ 0 , 1 ] }$ and using simple transformation power $\mathrm { Y } = 1$ . This method led on the arti<sup>fi</sup>cial and real-world data sets in most cases to the highest performance accuracy. The second approach based on the ‘e<sup>f</sup>ective dimensionality’ eventuated in the majority of cases in lower mean accuracies than the <sup>fi</sup>rst method. Therefore, the authors suggest, premised on the observed results, to use the novel similarity classi<sup>fi</sup>er on standardized data with transformation power $\mathrm { Y } = 1$ since it showed superior results compared to the standard similarity classi<sup>fi</sup>er. On the real-world data sets, the novel similarity classi<sup>fi</sup>er with trans formation power Y set to 1 achieved in most cases competitive mean accuracies and on the Australian Credit Data set even the highest mean accuracy. Except for the ensemble learning technique random forest, the novel similarity classi<sup>fi</sup>er with $\mathrm { Y } = 1$ was often signi<sup>fi</sup>cantly or highly signi<sup>fi</sup>cantly more accurate than the benchmark algorithms in this study. Moreover, the novel similarity classi<sup>fi</sup>er customized to achieve small FPR reached comparably low FPR values, in two out of three cases even accomplishing the lowest FPR of all algorithms. Finally, a future research need is a systematic analysis of the transfor mation power for the novel similarity classi<sup>fi</sup>er for di<sup>f</sup>erent data sets.

Results for the Australian Credit data set (the highest mean accuracy, the lowest FNR and the lowest FPR are highlighted in bold)

<table><tr><td>Classification algorithm</td><td>Mean accuracy</td><td>Variance</td><td>Mean FNR</td><td>Mean FPR</td><td>p</td><td>m</td><td>Y</td></tr><tr><td>Standard similarity classifier</td><td>0.8727</td><td>0.0004</td><td>0.144</td><td>0.114</td><td>3</td><td>3</td><td>-</td></tr><tr><td>Novel similarity classifier</td><td>0.8469</td><td>0.0005</td><td>0.151</td><td>0.155</td><td>1</td><td>1</td><td>p/2</td></tr><tr><td>Novel similarity classifier</td><td>0.8737</td><td>0.0004</td><td>0.118</td><td>0.133</td><td>2</td><td>3</td><td>1</td></tr><tr><td>Novel similarity classifier (minimize FPR)</td><td>0.8478</td><td>0.0005</td><td>0.229</td><td>0.090</td><td>2</td><td>6</td><td>1</td></tr><tr><td>Standard similarity classifier (PCA, 3 PCs)</td><td>0.8283</td><td>0.0005</td><td>0.268</td><td>0.094</td><td>1</td><td>2</td><td>-</td></tr><tr><td>Novel similarity classifier (PCA, 3 PCs)</td><td>0.7940</td><td>0.0006</td><td>0.273</td><td>0.152</td><td>1</td><td>3</td><td>p/2</td></tr><tr><td>Novel similarity classifier (PCA, 3 PCs)</td><td>0.8273</td><td>0.0004</td><td>0.228</td><td>0.128</td><td>1</td><td>1</td><td>1</td></tr><tr><td>K-nearest neighbours, k = 1</td><td>0.7997</td><td>0.0005</td><td>0.223</td><td>0.182</td><td>-</td><td>-</td><td>-</td></tr><tr><td>K-nearest neighbours, k = 10</td><td>0.8513</td><td>0.0004</td><td>0.177</td><td>0.126</td><td>-</td><td>-</td><td>-</td></tr><tr><td>K-nearest neighbours, best k = 1</td><td>0.7997</td><td>0.0005</td><td>0.223</td><td>0.182</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Naive Bayes (normal Gaussian distribution)</td><td>0.8016</td><td>0.0005</td><td>0.329</td><td>0.093</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Naive Bayes (kernel with normal smoothing)</td><td>0.6877</td><td>0.0015</td><td>0.417</td><td>0.228</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Random decision forest (min leafsize = 1)</td><td>0.8676</td><td>0.0004</td><td>0.143</td><td>0.124</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Random decision forest (min leafsize = 10)</td><td>0.8653</td><td>0.0004</td><td>0.153</td><td>0.120</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Decision tree (min leafsize = 1)</td><td>0.8307</td><td>0.0006</td><td>0.194</td><td>0.149</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Decision tree (min leafsize = 10)</td><td>0.8483</td><td>0.0005</td><td>0.164</td><td>0.142</td><td>-</td><td>-</td><td>-</td></tr></table>

![](/api/attachments/VT36U6Q9/fulltext/images/90109540b1266f5a0ee6382a64c9efe6900da81c11979944dd32dc95589d72ba.jpg)

![](/api/attachments/VT36U6Q9/fulltext/images/7cca2cb86cec2c278ccb44e88a287f205e05d83d3fa3a374e5c4edfe49b73f5f.jpg)  
Fig. 5. Optimal value search for the novel similarity classi<sup>fi</sup>er with Y = 1 (‘Australian Credit’ data).

## References

[1] H. Abdi, L.J. Williams, Principal component analysis, Wiley Interdisciplinary Reviews: Computational Statistics 2 (2010) 433–459.

[2] M.S. Bartlett, Tests of signi<sup>fi</sup>cance in factor analysis, British Journal of Statistical Psychology 3 (2) (1950) 77 85

[3] V.L. Berardi, G.Q. Zhang, The e<sup>f</sup>ect of misclassi<sup>fi</sup>cation costs on neural network classi<sup>fi</sup>ers, Decision Sciences Institute, 1997 Annual Meeting, Proceedings, Vols. 1–3, 30(3) 1997, pp. 364–366.

[4] C.M. Bishop, Pattern Recognition and Machine Learning, Springer ScienceBusines Media, New York, 2006.

[5] L. Breiman, Random forests, Machine Learning 45 (1) (2001) 5–32.

[6] T. Calinski, J. Harabasz, A dendrite method for cluster analysis, Communications in Statistics - Theory and Methods 3 (1) (1974) 1–27

[7] R. Cangelosi. A. Goriely. Component retention in principal component analysis with application to cDNA microarrav data. Biology Direct 2 (2o07) 2.

[8] R.B. Cattell, The scree test for the number of factors, Multivariate Behavioral Research 1 (2) (1966) 245–276.

[9] C.-L. Chuang, S.-T. Huang, A hybrid neural network approach for credit scoring, Expert Systems 28 (2) (2011) 185–196.

[10] T. Cover, P. Hart, Nearest neighbor pattern classification, JEEE Transactions or Information Theory 13 (1) (1967) 21–27.

[11] G. Dougherty, Pattern Recognition and Classi<sup>fi</sup>cation: An Introduction, Springer ScienceBusiness Media, New York, 2013.

[12] R.O. Duda, P.E. Hart, D.G. Stork, Pattern Classi<sup>fi</sup>cation, John Wiley, Section, New York, 2000.

[13] S. Figini, F. Bonelli, E. Giovannini, Solvency prediction for small and medium en terprises in banking, Decision Support Systems 102 (2017) 91 97.

[14] F. Formato, G. Gerla, L. Scarpati, Fuzzy subgroups and similarities, Soft Computing 3 (1999) 1 6.

[15] L.E. Garrido, F.J. Abad, V. Ponsoda, A new look at Horn's parallel analysis with

ordinal variables, Psychological Methods 18 (4) (2013) 454–474.

[16] L.W. Glorfeld, An improvement on Horn's parallel analysis methodology for se lecting the correct number of factors to retain, Educational and Psychological Measurement 55 (3) (1995) 377–393.

[17] L. Guttman, Some necessary conditions for common-factor analysis, Psychometrika 19 (2) (1954) 149–161.

[18] J.L. Horn, A rationale and test for the number of factors in factor analysis, Psychometrika 30 (2) (1965) 179–185.

[19] Z. Huang, H. Chen, C.-J. Hsu, W.-H. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[20] J.E. Jackson, A User's Guide to Principal Components, John Wiley & Sons, Inc., 1991.

[21] Y. Jiang, J. Shang, Y. Liu, Maximizing customer satisfaction through an online re commendation system: a novel associative classi<sup>fi</sup>cation model, Decision Support Systems 48 (3) (2010) 470–479.

[22] H.F. Kaiser, A note on Guttman's lower bound for the number of common factors, British Journal of Psychology 14 (1961) 1–2.

[23] F. Klawoon, J.L. Castro, Similarity in fuzzy reasoning, Mathware and Soft Computing, 2 1995, pp. 197–228.

[24] S. Koutroumbas, K. Theodoridis, Pattern recognition, Pattern Recognition 8 (2003).

[25] T.-S. Lee. C.-C. Chiu. Y.-C. Chou, C.-J. Lu. Mining the customer credit using clas: si<sup>fi</sup>cation and regression tree and multivariate adaptive regression splines, Computational Statistics and Data Analysis 50 (4) (2006) 1113 1130.

[26] N. Lei, S.K. Moon, A decision support system for market-driven product positioning and design, Decision Support Systems 69 (2015) 82 91

[27] M. Lichman, UCI machine learning repository, Retrieved from, 2013. http:// archive.ics.uci.edu/ml, .

[28] P. Luukka, Similarity classi<sup>fi</sup>er in diagnosis of bladder cancer, Computer Methods and Programs in Biomedicine 89 (2008) 43 49.

[29] P. Luukka, PCA for fuzzy data and similarity classi<sup>fi</sup>er in building recognition system for post-operative patient data, Expert Systems with Applications 36 (2 Part 1) (2009) 1222 1228.

[30] P. Luukka, Nonlinear fuzzy robust PCA algorithms and similarity classi<sup>fi</sup>er in bankruptcy analysis, Expert Systems with Applications 37 (12) (2010) 8296–8302.

[31] P. Luukka, J. Lampinen, Di<sup>f</sup>erential evolution based multiple vector prototype classi<sup>fi</sup>er, Computing and Informatics 34 (5) (2015) 1151 1167.

[32] P. Luukka, T. Leppälampi, Similarity classi<sup>fi</sup>er with generalized mean applied to medical data, Computers in Biology and Medicine 36 (2006) 1026–1040.

[33] P. Luukka, K. Saastamoinen, V. Könönen, A classi<sup>fi</sup>er based on the maximal fuzzy similarity in the generalized Lukasiewicz-structure. 10th JEEE International Conference on Fuzzy Systems, 2001.

[34] B.P. O'Connor, Code for minimum average partial correlation test and parallel analysis, Retrieved from, 2000. https://people.ok.ubc.ca/brioconn/nfactors/ nfactors.html.

[35] B.P. O'Connor, SPSS and SAS programs for determining the number of components using parallel analysis and Velicer's MAP test. Behavior Research Methods Instruments. & Computers 32 (3) (2000) 396–402.

[36] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann Publishers, San Mateo. 1992

[37] J.R. Quinlan, Induction of decision trees, Machine Learning 1 (1) (1986) 81–106.

[38] S. Russell, P. Norvig, Arti<sup>fi</sup>cial Intelligence: A Modern Approach, 3rd edition, Prentice Hall. 2009, pp. 1–1132

[39] C. Sugar, J. Gareth, Finding the number of clusters in a data set: an information theoretic approach, Journal of the American Statistical Association 98 (2003) 750-763.

[40] R. Tibshirani, G. Walther, T. Hastie, Estimating the number of clusters in a data set via the gap statistic, Journal of the Royal Statistical Society, Series B (Statistical Methodology) 63 (2) (2001) 411 423.

[41] C.-F. Tsai. J.-W. Wu. Using neural network ensembles for bankruptcy prediction and credit scoring, Expert Systems with Applications 34 (4) (2008) 2639–2649.

[42] R. Tsaih, Y.J. Liu, W. Liu, Y.L. Lien, Credit scoring system for small business loans, Decision Support Systems 38 (1) (2004) 91 99.

[43] W.F. Velicer, Determining the number of components from the matrix of partial correlations, Psychometrika 41 (3) (1976) 321 327.

[44] W.F. Velicer, C.A. Eaton, J.L. Fava, Construct explication through factor or component analysis: a review and evaluation of alternative procedures for determining the number of factors or components, Problems and Solutions in Human Assessment, vol. 1998, 2000, pp. 41–71.

[45] A.R. Webb, Statistical Pattern Recognition, John Wiley Sons, Malvern, 2002

[46] D. West, S. Dellana, J. Qian, Neural network ensemble strategies for <sup>fi</sup>nancial decision applications, Computers and Operations Research 32 (10) (2005) 2543–2559.

[47] I.H. Witten, E. Frank, Data mining: practical machine learning tools and techniques, Machine Learning, 2005.

[48] L. Yu, S. Wang, K.K. Lai, L. Zhou, Bio-inspired credit risk analysis, Bio-inspired Credit Risk Analysis: Computational Intelligence With Support Vector Machines, 2008.

[50] W.R. Zwick, W.F. Velicer, Factors in<sup>fl</sup>uencing four rules for determining the numbe of components to retain, Multivariate Behavioral Research 17 (2) (1982) 253.

[49] L.A. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338–353.

[51] W.R. Zwick, W.F. Velicer, Comparison of <sup>fi</sup>ve rules for determining the number of components to retain, Psychological Bulletin 99 (3) (1986) 432.

Christoph Lohrmann received the M.Sc. degree with Distinction in Banking and Financial Management in 2016 from the Institute for Financial Services, University of Liechtenstein, Liechtenstein. He is currently PhD student in Computational Engineering with the School of Engineering Science, Lappeenranta University of Technology. His research interests include data analysis, classi<sup>fi</sup>cation, feature selection, decision-making and <sup>fi</sup>nancial markets

Pasi Luukka received the M.Sc. degree in 1999 from the Department of Information Technology, Lappeenranta University, Finland, where he also received the D.Sc. degree in Applied Mathematics in 2005 from the Department of Mathematics and Physics. He is currently Full Professor with the School of Business and Management, Lappeenranta University of Technology. His research interests include fuzzy data analysis, classi<sup>fi</sup>ca tion, feature selection and fuzzy decision-making
