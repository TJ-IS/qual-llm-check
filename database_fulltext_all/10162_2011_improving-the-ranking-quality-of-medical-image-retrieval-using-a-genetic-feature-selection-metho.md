---
otero_id: 10162
otero_key: "EAUZGY6A"
title: "Improving the ranking quality of medical image retrieval using a genetic feature selection method"
authors: "Sérgio Francisco da Silva; Marcela Xavier Ribeiro; João do E.S. Batista Neto; Caetano Traina-Jr.; Agma J.M. Traina"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.01.015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving the ranking quality of medical image retrieval using a genetic feature selection method

Sérgio Francisco da Silva <sup>a,</sup>⁎, Marcela Xavier Ribeiro <sup>b</sup>, João do E.S. Batista Neto <sup>a</sup>, Caetano Traina-Jr. <sup>a</sup>, Agma J.M. Traina <sup>a</sup>

<sup>a</sup> Department of Computer Science, University of Sao Paulo at Sao Carlos, Brazil

<sup>b</sup> Department of Computer Science, Federal University of Sao Carlos, Brazil

## a r t i c l e i n f o

Available online 3 February 2011

Keywords: Feature selection Genetic algorithms Ranking quality Medical image retrieval

## a b s t r a c t

In this paper, we take advantage of single-valued functions that evaluate rankings to develop a family of feature selection methods based on the genetic algorithm approach, tailored to improve the accuracy of content-based image retrieval systems. Experiments on three image datasets, comprising images of breast and lung nodules, showed that developing functions to evaluate the ranking quality allows improving retrieval performance. This approach produces signi<sup>fi</sup>cantly better results than those of other <sup>fi</sup>tness function approaches, such as the traditional wrapper and than <sup>fi</sup>lter feature selection algorithms.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Medical images play a central role in patient diagnosis, therapy, surgical planning, medical reference, and training. With the recent boom in the availability of <sup>fi</sup>lmless radiology equipment, the management of digital medical images is receiving more and more attention. Picture Archiving and Communication Systems (PACS) [29,31] have been successfully introduced in many hospitals and specialized clinics, providing quick access to screening exams and integrating the actors involved in the enterprise's work<sup>fl</sup>ow. The radiological databases originally built for storing digital images have evolved from simple storage servers of past exams, kept for legal reasons, to active and easily accessible repositories for research and decision support [23,24].

The Digital Imaging and Communications in Medicine (DICOM) standard [12] allows storing textual descriptions, known as metadata, along with the images. Currently, most queries in PACS are text-based search based only on the metadata. However, querying images based on their visual characteristics has proven to be a suitable complement to text-based search [23,24,34]. Adequate visual features not only allow retrieving cases where patients have similar diagnoses, but also help the identi<sup>fi</sup>cation of cases with visual similarity, even with different diagnoses [23]. We are interested in answering queries such as: “Return the 5 images most similar to the Jane Doe's Lung X-Ray”. Retrieving similar images is often more useful from the physician's viewpoint than just accessing the classi<sup>fi</sup>cation of the image under analysis. Radiologists invariably feel more comfortable in making a judgment when a set of similar data or cases is given, rather than simply interpreting an outcome produced by a classi<sup>fi</sup>er whose design is often not fully familiar to them. By analyzing past similar cases, the radiologists have more information for decision making.

Content-Based Image Retrieval (CBIR) refers to techniques that retrieve images based on their content, as opposed to based on metadata. In the medical domain, the objective of a CBIR system is to aid the specialist in the medical diagnosis process, retrieving relevant past cases with images revealing proven pathology, along with the corresponding associated clinical diagnoses and other information [23]. Several papers have proposed content-based access to medical images for supporting clinical decision-making (evidence-based practice of medicine) [1,17] and scenarios for the integration of CBIR into PACS [34], as well as into the clinical routine [24].

Image retrieval of past cases is performed by comparing the present case image(s) with those stored in the database, and sorting them according to the similarity criteria employed. Thus, the result of a CBIR operation is a set of images ranked by their similarity to the current case. However, the design of ranking functions considering the importance of each image feature are problem-dependent. In this work we developed a set of evaluation functions for CBIR, the “Fitness coach” (Fc) family, aimed at improving the quality of the query answers by retrieving a larger number of relevant images in the initial positions of the answer ranking. This aspect is quite important, because users expect to get the most relevant images in the beginning of the resulting list (the <sup>fi</sup>rst positions of the ranking).

We employ order-based ranking evaluation functions that share the utility concept [10]. This concept states that a utility function (the ranking evaluation function) must assign a score to each element according to its relevance and its position in a ranking. The relevance is given by a training dataset. Usually, it assumes that the utility of a relevant element decreases according to its position in a certain ranking, i.e., the higher its ranking position, the higher its utility. If an element is not relevant to a query (it does not belong to the expected class according to the training set) its utility score is set to zero. This concept of ranking quality, which is the focus of this work, led us to build the Fc family of <sup>fi</sup>tness functions, employed in the GA-based feature selection algorithm.

To the best of our knowledge, this is the <sup>fi</sup>rst time that ranking evaluation functions are employed for feature selection. Conceptually, performing feature selection for CBIR using a ranking quality measurement as the retrieval effectiveness evaluation is preferred than the current approaches based on classi<sup>fi</sup>cation error [28].

In order to better understand our method, some concepts must be explained, as follows. Given a query element, a similarity search operation returns a set of elements (images in our case) ordered according to a similarity measure. The resulting order is called the ranking of the returned elements. We consider the feature selection as a supervised task that uses a set of pre-labeled samples distributed among a set of different classes. We say that an element is relevant to a query when it belongs to the expected class and it is part of the query answer, regardless of its position in the ranking. A ranking evaluation function provides a score of the quality of the similarity search result.

A CBIR system performs indexing and retrieval tasks using features computed from images as opposed to using the whole images. These features are numerical values computed by image processing algorithms that capture visual images descriptions and store them in feature vectors. During the retrieval or similarity searching process, the images that are most similar to the query image according to some distance measure (e.g. the Euclidean distance), are returned. Knowing what the most relevant and non-redundant features are, according to the application domain, is very important for improving the accuracy of the similarity search. It is well-known that features obtained from only a single extractor is not always the most appropriate way to characterize images, mainly because more than one class of visual features is needed to represent them. However, using several feature extractors usually produces a large number of features, often containing correlated and irrelevant information that leads to the dimensionality curse problem [18] and deteriorates the ef<sup>fi</sup>ciency of the retrieval process. Beyer et al. in [5] showed that increasing the number of features leads to a signi<sup>fi</sup>cant loss of the discriminative power of each feature. Thus, dimensionality reduction methods have been employed to ameliorate the dimensionality curse.

There are two broad classes of methods to reduce dimensionality: feature extraction and feature selection. Feature extraction typically changes the feature space providing a lower dimensional but transformed space. None of the original dimensions are kept, reducing the “interpretability” of the results. Moreover, it is usual that some of the automatically extracted features are highly uncorrelated to the analysis target, thus distorting the results. Those attributes, which are not removed by the extraction methods, reduces the discriminative power of the relevant ones. Feature selection (FS) methods search for the most relevant feature subset, belonging to the original feature space, according to a user-de<sup>fi</sup>ned criterion. Therefore, in this paper we chose feature selection methods instead of the feature extraction ones as the preferred approach to help improving CBIR techniques.

Feature selection (FS) is one of the most important and frequently used preprocessing techniques for data mining [19]. FS reduces the number of features by removing irrelevant, redundant, and/or noisy data. Some direct bene<sup>fi</sup>ts are: (a) faster data mining algorithms convergence; and (b) more accurate results. Although many successful applications have bene<sup>fi</sup>ted from feature selection approaches [2,7,22,38], there is still no method of choice for the CBIR community. Moreover, there are no results of FS solutions speci<sup>fi</sup>cally tailored to CBIR (i.e., a CBIR-wrapper approach). Existing approaches are mainly based on <sup>fi</sup>lter algorithms [7] or wrapper approaches intended to optimize the classi<sup>fi</sup>cation accuracy [22].

Genetic algorithms (GAs) are among the most used techniques to perform feature selection due to GAs ability to obtain either exact or approximate solutions in very large search spaces within tractable time. GAs perform adaptive searching, following the standard concepts from natural genetics and evolution based on natural selection [11]. Due to their potential, we employed GA in this work to perform feature selection speci<sup>fi</sup>c for the CBIR domain.

In the present work, we investigate the applicability of <sup>fi</sup>tness functions on a speci<sup>fi</sup>c-purpose GA, especially tailored for FS in Content-Based Medical Image Retrieval (CBMIR) context. These algorithms were brie<sup>fl</sup>y introduced in a preliminary work [28]. The analysis built over Precision and Recall (P&R) curves shows that the proposed methods, based on ranking quality maximization, outperform all the other methods evaluated and compared to.

The remainder of this paper is structured as follows. Section 2 gives the main concepts concerning this work. Section 3 presents related work. Section 4 describes the proposed framework for feature selection. Section 5 details the experimental evaluation. Finally, Section 6 addresses the conclusions and points out future directions for this research.

## 2. Background

This Section discusses the main concepts necessary to follow this paper.

## 2.1. Content-Based Image Retrieval

Content-Based Image Retrieval (CBIR) is centered on the notion of image similarity. Given an image database, CBIR retrieves the subset of images which are most “similar” to the query image. Similarity computation relies on the feature vectors, which encode visual characteristics of an image, such as color distribution, shape or texture. Features obtained for speci<sup>fi</sup>c domains, such as medical images, often also embody characteristics that are speci<sup>fi</sup>c of these domains. The similarity between two images is computed by measuring the distance between the corresponding feature vectors, using a distance function.

Two kinds of queries are usually available in CBIR systems [33], which are described as follows. The k-nearest neighbor (k-NN) query receives the number k of images to be retrieved and the query center – and gives the k most similar images to the supplied query center. For example: “Find the 3 images which are the most similar ones to the Jane Doe's Lung X-Ray”. The range query (RQ) receives a search radius r – and retrieves all the images whose distance to the query center is less or equal to r. For example: “Find the images that differ from the John Doe's Lung X-Ray up to 10 units”.

Another important issue related to a CBIR system is how to evaluate its ef<sup>fi</sup>cacy. A standard approach to evaluate similarity search accuracy uses the precision and recall (P&R) graphs [3]. Precision and recall are de<sup>fi</sup>ned in Eqs. (1) and (2) respectively.

$$
p r e c i s i o n = \frac {\text { number   of   relevant   images   retrieved }}{\text { number   of   images   retrieved }}\tag{1}
$$

$$
\text { recall } = \frac {\text { number   of   relevant   images   retrieved }}{\text { number   of   relevant   images   in   the   dataset }}\tag{2}
$$

To build the P&R graphs, one typically executes a set of k-nearest neighbor (k-NN) queries, using randomly selected query images from the dataset as query centers. The value of k, which corresponds to the number of images retrieved, must be adjusted according to the user or the application requirements. A rule of thumb to analyze P&R curves is: the closer the curve is to the top of the graph, the better the technique is [3]. That is, the best method is the one that gives the curve with the highest precision for a range of recall values.

## 2.2. Feature Selection

Feature Selection (FS) algorithms aim at choosing a reduced number of features that preserves the most relevant information of the dataset. FS is usually applied as a preprocessing step in data mining tasks by removing irrelevant or redundant features (dealing with the dimensionality curse), therefore leading to more ef<sup>fi</sup>cient (reducing the computational cost and the amount of memory required) and accurate classi<sup>fi</sup>cation, clustering and similarity searching processes.

A typical FS process consists of four basic steps, namely, subset generation, subset evaluation, stopping criterion, and result validation [19]. Subset generation is a search procedure that produces candidate feature subsets for evaluation based on a certain searching strategy. Each candidate subset is evaluated and compared to the previous best subsets according to a certain evaluation criterion. If new subsets turn out to be better, they replace the previous ones. The process of subset generation and evaluation is repeated until a given stopping criterion is satis<sup>fi</sup>ed. Then, the selected best subset usually needs to be validated using a test dataset. Depending on whether an inductive algorithm is used for feature subset evaluation, FS algorithms can be categorized into two groups: <sup>fi</sup>lter and wrapper [19].

Filter algorithms evaluate the “properness” of the feature subset by using intrinsic characteristics of the data. Popular criteria employed are distance, information, dependency and consistency measurements [16]. Consistency measurements aim at <sup>fi</sup>nding a minimum number of features that separate classes as consistently as the full set of features does. Inconsistency occurs when two instances with the same feature values have different class labels. Filter methods are computationally not expensive, since they do not involve induction algorithms. However, they can select subsets of features that may not perform well with the algorithm embedded in the user application. Wrapper methods, on the other hand, use the <sup>fi</sup>nal mining algorithm (classi<sup>fi</sup>cation, clustering and others) itself to evaluate the candidate feature subsets. Wrapper methods generally select features which are more suited to the mining task than the <sup>fi</sup>lter methods, but they generally present a higher computational cost.

Representative <sup>fi</sup>lter FS algorithms are presented as follows. The correlation-based feature selection algorithm (CFS) [13] evaluates feature subsets using a correlation-based heuristic search algorithm. Subsets containing features that are highly correlated with the class, yet uncorrelated with each other, are considered “good” [13]. The CFS algorithm employs Pearson's correlation as evaluation criterion of feature subsets. The fast correlation-based <sup>fi</sup>lter (FCBF) algorithm [39] measures correlations between features and classes and correlations between feature pairs as well. It selects the features that are highly correlated with the class and eliminates redundant features one-byone in descending order, according to the approximate Markov blanket concept de<sup>fi</sup>ned by the authors. ReliefF [27] estimates the quality of a feature set computing how well they discriminate instances that are near to each other. The minimal redundancy maximal relevance (mRMR) algorithm [25] selects features that have the highest relevance with the target class and are also maximally dissimilar to each other. An implementation of CFS, FCBF and ReliefF is available in the Weka tool (see Witten [37]). An implementation of the mRMR is provided by the authors of the mRMR algorithm [25] in http://www.public.asu.edu/\~huanliu/. Some <sup>fi</sup>lter algorithms, such as mRMR, do not work with continuous data, requiring data discretization – a process of splitting continuous values into discrete intervals. In our experiments Chi2 algorithm [20] was used to that purpose. The Chi2 algorithm [20] uses the $\chi ^ { 2 }$ statistics to merge consecutive intervals, fusing the consecutive intervals that lead to the smallest $\chi ^ { 2 }$ value at each step.

Wrapper FS algorithms, as opposed to <sup>fi</sup>lter algorithms, are taskspeci<sup>fi</sup>c. When dealing with wrapper FS algorithms, a key issue is how the search in the feature space is performed, given that a subset evaluation is normally expensive and the search space grows exponentially with the number of features. For a survey on different search methods (e.g., complete search, heuristic search, and random search) used for FS algorithms, the reader is referred to [19]. These methods have shown promising results in a number of real-world applications. However, whenever the number of features is typically very large, most of these existing methods face the problem of very long computational times.

Another approach for FS is the use of statistical association rules, which led to the development of the StARMiner algorithm [26]. The goal of StARMiner is to implement statistical association rule mining to <sup>fi</sup>nd features that best discriminate images into categorical classes. It is also employed as a baseline for comparison with our method.

The Genetic algorithm approach [11] is one of the most commonly used modern stochastic global search techniques and has the wellknown ability to produce high-quality solutions within tractable time, even on complex problems. It has been used for FS and has shown promising performance [22,28,36,38,40].

## 2.3. Genetic Algorithms – GA

Genetic Algorithms [11,14] are based on the principles of biological inheritance and evolution. Each potential solution is called an individual (i.e. a chromosome) in a population. GAs work iteratively, applying the genetic operations of selection, crossover and mutation to a population of individuals, aimed at creating better adapted individuals in subsequent generations. For each category of problems solved by a GA, a <sup>fi</sup>tness function must be provided. This choice is crucial to maximize the GA's performance. The <sup>fi</sup>tness function assigns a <sup>fi</sup>tness value for each individual called the individual score, and it is well-known to play an essential role in the genetic evolution [21]. This is because this score is used in the selection processes of parents for crossover and of survivals for each next generation. Thus, the highest probabilities to reproduce and survive must be given to the best adapted individuals, that is, the ones who provide the best features for an accurate query process. Due to its importance to GA, the <sup>fi</sup>tness function must be tailored to the problem at hand. Thus, a <sup>fi</sup>tness function should model the solution space in such a way that, when solving a maximization problem, better solutions receive higher scores.

Associated with the characteristics of exploitation and exploration, GAs can ef<sup>fi</sup>ciently deal with large search spaces, and hence are less prone to get stuck into a local optimum solution when compared to other algorithms. This derives from the GAs ability to handle multiple concurrent solutions (individuals) in the search space and apply probabilistic genetic operators [11,14].

## 2.4. Multistart Search

The Multistart (MS) Search is a heuristic one that generates various random initial solutions and returns the best one according to a given measure. MS search may be naturally compared with GA search, since both employ random mechanisms. This paper compares the GA-based FS with a MS-based FS in the experiments section.

## 2.5. Ranking evaluation functions

Ranking evaluation functions assess the ranking accuracy. Ranking is de<sup>fi</sup>ned as a set of elements sorted according to a similarity measure. Ranking evaluation functions belong to two categories: order-based and non order-based. Non order-based ranking evaluation functions state that the score of an element in the ranking has a fragile relationship to its position. An example is the R-precision measure. In this work, this measure is given as:

$$
\mathrm{FR} - \text { Precision } (q, C) = \frac {\sum_ {i = 1} ^ {R} r (i)}{R}\tag{3}
$$

where FR−Precision(q,C) denotes the score value of the individual C (given by the chromosome coding, explained in Section 4) for the image query q. For example, consider a feature vector of 4 dimensions. A chromosome $C = ( 1 , 1 , 0 , 0 )$ means that the dimensions (features) one and two, which are equal to one, are relevant and dimensions three and four, which are equal to zero, are not. R represents the number of images retrieved, r(i) returns the relevance of the retrieved image i, where $r ( i ) = 1$ if the image i is relevant for that query q and $r ( i ) = 0$ otherwise. In summary, this equation measures the rate of relevant images between the <sup>fi</sup>rst R retrieved images.

Order-based ranking evaluation functions are based on the utility concept, where the score value of a relevant element in the ranking is usually inversely proportional to its position. The fact that users would rather see relevant elements appearing in the initial positions of the ranking suggests that order-based ranking evaluation functions are more likely to be successful.

Various ranking evaluation functions have been proposed in the literature. However, to the best of our knowledge, ranking evaluation functions have never been applied to the FS domain. A ranking evaluation function that presents promising results, presented in [8] is the following:

$$
F r (q, C) = \sum_ {\forall i \in I} \left(r (i) \frac {1}{A} \left(\frac {(A - 1)}{A}\right) ^ {(p o s (i) - 1)}\right)\tag{4}
$$

where $F r ( q , C )$ denotes the score value of the individual C (given by the chromosome coding, explained in Section 4) for the image query q, I represents the entire image dataset, and r(i) is the relevance of the image i, de<sup>fi</sup>ned in the same way as for Eq. (3). A is a user-de<sup>fi</sup>ned parameter with values larger than or equal to 2. It states the relative importance of the element position pos(i) in the ranking. For small values of A, greater importance is given to relevant elements better positioned in the ranking (i.e. those at the initial positions). When A takes higher values, the factor $\frac { ( A - 1 ) } { A }$ leads to values closer to 1, and thus the relative element position in the ranking is not strongly re<sup>fl</sup>ected in the <sup>fi</sup>nal score value. We have set A to 10, which empirically leads to an intermediate behavior for the score value $F r ( q , C )$ . That is, the score computed for all relevant elements at increasing positions leads to uniformly distributed values of $F r ( q , C )$ in the range [0,1], well discriminating different rankings according to their accuracy.

## 3. Related work

Several researches in the data mining <sup>fi</sup>eld known as wrapper FS techniques focus on maximizing the classi<sup>fi</sup>cation accuracy [2,19,22,38,40]. Works on improving information retrieval mainly employ relevance feedback approaches [3,4,6,15,21,30,41] and similarity function learning (or ranking function learning) [9,32]. There are works employing evolutionary approaches to perform FS [7,19,35,36,38] as well as others for improving the information retrieval (IR) [6,9,32]. A review on the application of evolutionary computation to boost information retrieval is found in [6].

The main focus of our proposed work is to provide effective information retrieval (IR), speci<sup>fi</sup>cally medical image retrieval, with FS. An image retrieval system can be affected by any of the three following issues: images' representations, queries' representations and similarity functions. Various works propose relevance feedback (RF) techniques [4,15,30,41], which allow adjusting image retrieval systems in many ways. However, RF processes are tiresome for the users, as they typically require many rounds of user feedback in order to provide satisfactory results. Also, the inductive procedure of RF is often time-consuming. Compared with RF techniques, our approach is more user-friendly, as it allows improvement on CBIR results with no user effort to provide feedback.

Similarity functions learning and developing have received much attention from researchers. According to [32], an image descriptor is a pair composed of an image feature extractor and a dissimilarity function (distance function). Many distance functions have been developed and applied to Web information retrieval, as well as to image retrieval. However, recent studies show that these functions do not perform consistently well across different contexts [9,32].

The approaches described in [9] and [32], presented solutions involving the identi<sup>fi</sup>cation of similarity functions that combine multiple similarity measures in the Web and multiple image descriptors in the CBIR context, respectively. Both use evolutionary optimization that rely on evaluation criteria based on the ranking quality. According to [9] and [32], there is no such a thing as the best Web similarity function or descriptor, on the contrary, the similarity functions and descriptors are problem-oriented. In our work, instead of learning the best measure for combination of distance functions, we employ a specialized GA that relies on ranking evaluation functions to choose the best set of features to represent images in a CBIR context.

## 4. The proposed framework

Our framework employs a GA using an evaluation function based on the ranking concept to perform FS for CBIR. This solution stemmed from three considerations: (i) the large size of the search space in FS; (ii) previous successful usage of GA for FS; and (iii) the existence of no prior work on FS based on ranking quality optimization applied to CBIR.

Fig. 1 illustrates the steps from the pipeline that represents the implementation of the proposed framework. The FS process is supervised. In the training phase, image features are extracted from the training image dataset and submitted to the FS process. The FS process itself is a GA that searches for the best feature subset according to an evaluation criteria based on the ranking quality. The ranking quality is given by a single valued ranking evaluation function (Fc). In the test phase, the selected features corresponding to the best chromosome chosen by the GA is used over the images from the test dataset. Similarity searches were computed for each image from the test dataset, and the average Precision and Recall (P&R) curve was built, which allows assessing the accuracy of the method. In a real operation system, the specialist submits queries to the system, which will return the most similar images associated to the case information. This characteristic can be used to support decision-making or evidence-based decision. The proposed GA-based feature selector is described as follows.

## 4.1. The chromosome coding

In order to apply a GA to a given problem, it is necessary to de<sup>fi</sup>ne the genotype required by the problem, i.e. the chromosome representation. In other words, a decision must be made on how the parameters of the problem will be mapped into a <sup>fi</sup>nite string of symbols (genes), encoding a possible solution in the problem space. In this work, a chromosome was coded by an n-bit string (n is the initial number of features) $C = ( g _ { 1 } , g _ { 2 } , . . . , g _ { n } )$ , where g takes value 0, if the i<sup>th</sup> feature is excluded from the subset, and 1, if it is kept in the subset.

## 4.2. The genetic operators

A GA searches for the best solutions using genetic operations that include selection, crossover and mutation. The selection operation strengthens the high-<sup>fi</sup>tted individuals, according to a user-de<sup>fi</sup>ned <sup>fi</sup>tness measure. High-<sup>fi</sup>tted individuals have a higher probability of surviving and reproducing, while the low-<sup>fi</sup>tted are likely to disappear. Note that high-<sup>fi</sup>tted individuals are those who provide the highest accuracies in the retrieval process. Crossover and mutation operations represent an analogy to natural reproduction and explore the solution space to <sup>fi</sup>nd the best solution. The genetic operations used in this study are:

![](/api/attachments/EAUZGY6A/fulltext/images/6677f6c253c94e9240caa33f1e1d593886da6b2ab73ceb3b7612a9cc0563177d.jpg)  
Fig. 1. Pipeline of the proposed method.

• Selection for recombination: applied to select pairs of individuals that will go on reproducing (mating pool). Linear Ranking Selection has been used here: the individuals are sorted according to their <sup>fi</sup>tness and the last position is assigned to the best individual, while the <sup>fi</sup>rst position is allocated to the worst one. The selection probability is linearly assigned to the individuals according to their ranks.

• Selection for reinsertion: a total of $( S _ { p } - 2 )$ best offsprings and 2 best parents according to their <sup>fi</sup>tness values survive from one generation to the next. $S _ { p }$ is the population size.

• Crossover: represents the mating of two individuals to form two new individuals (offsprings). Uniform crossover was used in this work. Uniform crossover is a sort of multiple points crossover taken to the extreme, where instead of randomly selecting the crossover points, a mask with the size of the chromosome that indicates which Chromosome-Parent will supply each gene to Offspring 1 is randomly built. Offspring 2 is generated by the complement of the mask.

• Mutation: a gene selected for mutation is replaced by its complement, i.e. each chosen bit will be changed from 0 to 1 and vice-versa. This is known as uniform mutation.

## 4.3. Fitness function

The <sup>fi</sup>tness function plays a very important role in guiding the GA to obtain the best solutions within a large search space. Good <sup>fi</sup>tness functions help the GA to explore the search space more effectively and ef<sup>fi</sup>ciently. On the other hand, inappropriate <sup>fi</sup>tness functions can easily weaken the GA search ability and result in getting stuck into a local optimum solution. Two main <sup>fi</sup>tness function designs were analyzed in this work: classi<sup>fi</sup>cation error and <sup>fi</sup>tness functions based on ranking evaluation functions.

From the order-based ranking evaluation function $F r ( q , C )$ stated as Eq. (4), we devised a mechanism to derive a function acting as a “Fitness coach” Fc(Q,C), providing a score for the chromosomes in the GA. In $\operatorname { E q . }$ (5), the $F c ( Q , C )$ function is given by the average score obtained from each image q of the training dataset Q as an image query center, considering the remaining images as the reference dataset for image searching. $n _ { Q }$ is the number of images in the dataset Q. This approach is similar to the leave-one-out method and was adopted to avoid over<sup>fi</sup>tting.

$$
F c (Q, C) = \frac {\sum_ {\forall q \in Q} F r (q , C)}{n _ {Q}}\tag{5}
$$

The output of the <sup>fi</sup>tness function is normalized within range [0,1], where 1 indicates maximum accuracy. According to this criterion, the problem consists of seeking to maximize the <sup>fi</sup>tness function. On the other hand, this can also be seen as a minimization problem if the output is subtracted from 1 (1 – output). This is the approach adopted in this work.

We recall that the fundamental principle in wrapper FS approaches is the minimization of the number of features, while optimizing (or preserving) the quality of the result [5]. For a CBIR system, the best approach is to retrieve images with a minimum number of features keeping the highest accuracy. This concept led to the proposal of two distinct <sup>fi</sup>tness functions FcA(Q,C) and FcB(Q,C) (Eqs. (6) and (7) respectively), which combine two optimization criteria. The <sup>fi</sup>rst criterion indicates the quality of the query results given by function $F c ( Q , C )$ evaluated in both Eqs. (6) and (7). The second criterion, the minimization of the number of features, is given by the fractions $\frac { ( | C | - d ) } { n }$ and $\frac { | C | } { n }$ in Eqs. (6) and (7), respectively.

$$
F c A (Q, C) = \alpha (F c (Q, C)) + (1 - \alpha) \left(\frac {(| C | - d)}{n}\right)\tag{6}
$$

$$
F c B (Q, C) = \alpha (F c (Q, C)) + (1 - \alpha) \left(\frac {| C |}{n}\right)\tag{7}
$$

In both Eqs. (6) and (7), |C | is the number of selected features coded by chromosome C, Q is the training dataset, d is the userspeci<sup>fi</sup>ed number of features, and n is the dataset dimensionality (number of features). The fraction $\frac { ( | C | - d ) } { n }$ in Eq. (6) yields high values when the number of selected features |C| widely differs from the number of desired features d. The fraction $\frac { | C | } { n }$ , in Eq. (7), is also a penalizing factor that only takes into account the number of selected features. Finally, α∈[0,1] is an adjustment parameter allowing to assess the importance assigned to each criterion, in a complementary way.

## 4.4. Control parameters

The experiments described in this work employed the crossover probability $p _ { c } = 1$ and the mutation probability $p _ { m } = 0 . 0 1$ for each gene.

## 5. Experiments and discussion

In this section, we present three representative experiments where the proposed method was employed to perform content-based medical image retrieval (CBMIR) tasks. The datasets were randomly split into training and test subsets. FS was performed on the training subsets and evaluated on the test ones. Performance evaluation was conducted through average precision and recall (P&R) curves, taking the average of evaluating each image from the test subsets as the query center and the training subsets as the references to answer the queries.

The FS techniques evaluated were grouped as:

• (a) our proposed Genetic Algorithm (GA) and the Multistart Search (MS) algorithm, each combined with the <sup>fi</sup>tness functions presented in Section 4 (FcA, FcB and Fc) and Subsection 2.5 (FR-Precision). Hereafter, their combinations will be referred to as: GA-FcA, GA-FcB, GA-Fc, GA-FR-Precision and MS-Fc;

• (b) GAs combined with <sup>fi</sup>tness functions based on classi<sup>fi</sup>cation error minimization of traditional classi<sup>fi</sup>ers (1NN, C4.5, SVM and Naive Bayes – NB), hereafter denoted by GA-1NN, GA-C4.5, GA-SVM and GA-NB, respectively;

• (c) the FS algorithm based on statistical association rules mining (StARMiner algorithm) and all features combined (no feature selection);

• (d) <sup>fi</sup>lter algorithms – FCBF, ReliefF, CFS, mRMR (see Section 2.2); and

• (e) the most accurate method of each group.

Results for FCBF, ReliefF and CFS were performed using the Weka environment with default parameters. Results for mRMR were produced using the code provided by their authors. The features were discretized by Chi2 method prior to applying the mRMR method.

The evolutionary search was set to 100 individuals, evolving along 400 generations in experiments 1, and 3. Experiment 2 employed 50 individuals and 250 generations. The FcA parameter d (Eq. (6)) was set to 50 in the <sup>fi</sup>rst experiment, to 20 in the second one and to 100 in the third one. Parameter α was set constant to 0.9. The candidate solutions of MS search were represented by n-bit strings, where n is the dataset dimensionality. To be fair, the number of MS random solutions was set to the same number of <sup>fi</sup>tness evaluations performed by the GA in all the comparative experiments.

Our key objective is to develop techniques to support medical decisions by effectively retrieving relevant past cases with proven pathology along with the associated clinical diagnoses and other information, by searching for visually similar cases. When a specialist analyzes a new image, he or she can submit the image as a query center to a CBIR system, which will return the most similar images together with the associated diagnoses, treatments, or other speci<sup>fi</sup>c information. Fig. 2 illustrates a CBIR output, from a ground truth dataset comprising malign and benign masses. In this example, the specialist wants to <sup>fi</sup>nd evidence to help classifying the current image as a malign or a benign mass. As shown in this <sup>fi</sup>gure, the retrieved images and the associated information on the past diagnoses provided information to help the specialist diagnosing the current image as malignant.

![](/api/attachments/EAUZGY6A/fulltext/images/963dc85c25607cbfdd74b051f25289d41f1fbe2f672c4bf03d7a99cdc7c4ad3d.jpg)  
Fig. 2. Medical decision support through a CBIR outcome.

## 5.1. Experiment 1: ROI-250 image dataset

This experiment investigates the performance of the proposed technique over a 250-image mammography dataset with ROIs (Regions of Interest) comprising lesions, taken from the Digital Database for Screening Mammography at the University of South Carolina (http://marathon.csee.usf.edu/Mammography/). The dataset comprises two classes: benign and malign mass. A 739-dimensional feature vector was computed for each sample, including features generated by Haralick descriptors (140 features), Zernike moments (255 features), histogram (256 features), features of <sup>fi</sup>rst order derived from histogram (6 features), Run length (44 features) and invariant moments (38). The dataset was divided into a 166-image training subset and a 64-image test subset. Fig. 3 shows the Precision and Recall (P&R) curves obtained and also the number of features selected by each method.

The plots of Fig. 3 show that the proposed methods (GA-FcA, GA-FcB and GA-Fc) increased the query precision in approximately 15% in the region of 10% of recall in comparison with the other methods, while decreasing the number of features from 739 to 50. That is, even with approximately 7% of the original memory space required, the proposed evaluation function FcB yields the best result. These results indicate that the Fc family of evaluation functions are well-suited for GA-based FS in the CBIR task, as they not only do improve the precision of the results, but also demand less computational effort and memory space.

## 5.2. Experiment 2: Mammograms-1080 image dataset

This experiment employed a dataset with 1080 images from mammograms collected at the Clinical Hospital at University of Sao Paulo in Ribeirao Preto. The dataset was previously classi<sup>fi</sup>ed by radiologists into 4 levels of breast tissue density: (1) mostly fatty (362 images); (2) partly fatty (446 images); (3) partly dense (200 images); and (4) mostly dense (72 images).

(a)  
![](/api/attachments/EAUZGY6A/fulltext/images/cebdf28b074bab2f1a785e19946ca38dfc84bd919979855d2c6f5b1bc9163fd6.jpg)

(b)  
![](/api/attachments/EAUZGY6A/fulltext/images/072dbc1347df21db55d551e9fbce3177175ced1572b1f525b7260b1fbce5acff.jpg)

(c)  
![](/api/attachments/EAUZGY6A/fulltext/images/9bc630545c09c35938ed3dbdc098ba6130400bd5995e8da88ebf2e6d5e164d69.jpg)

(d)  
![](/api/attachments/EAUZGY6A/fulltext/images/f1804105a7aa5a45adcace22b7e71250e2072ffcd250c9063bef00ffeb6b5e9d.jpg)

(e)  
![](/api/attachments/EAUZGY6A/fulltext/images/0996d04c58f372901ab504ce82cd0be58c5dfa55a7c7f4c705ad9517e4a223ed.jpg)  
Fig. 3. Precision and Recall curves for the ROI-250 image dataset: (a) GA and MS combined with our Fc family of <sup>fi</sup>tness functions and FR-Precision; (b) GA combined with <sup>fi</sup>tness functions based on classi<sup>fi</sup>cation error minimization of traditional classi<sup>fi</sup>ers; (c) FS based on statistical association rules and no feature selection; (d) <sup>fi</sup>lter algorithms, and (e) the most accurate method of each group.

Breast density is an important risk factor in the development of breast cancer. In this experiment, images are represented by the feature set proposed in [17], yielding a vector of 85 features, including shape and size of the breast, the conditions of the breast contour; nipple position, and the distribution of <sup>fi</sup>broglandular tissue. The dataset was divided into a 720-image training dataset and a 360- image test dataset.

Fig. 4 shows the P&R curves for the test dataset and also the number of features selected in each method. Again, the proposed methods produced the highest values of precision, up to 10% for recall levels smaller than 50%,and selected the reduced number of features, up to 9.5%.

## 5.3. Experiment 3: Lung ROI-3258 image dataset

This dataset consists of 3,258 images containing ROIs of images from Computed Tomography (CT) of lung exams. It is grouped in 6 classes, being 1 of normal and 5 of abnormal patterns (emphysema, consolidation, thickness, honeycombing and ground-glass opacity). A 707-dimensional feature vector was computed for each image, including features generated by Haralick descriptors (140 features),

Zernike moments (255 features), histogram (256 features), features of <sup>fi</sup>rst order derived from histogram (6 features), Run length (44 features) and Tamura features (6 features). The dataset was divided into a 978-image training dataset and a 2,280-image test dataset.

Fig. 5 shows the P&R curves for the test dataset and also the number of features selected in each method. From such curves one can observe that the proposed Fc family of <sup>fi</sup>tness functions are effective in providing higher precision mainly for low recall levels. This is a very important aspect, because users commonly emphasize the analysis on the initial retrieved images (top of the ranking). This human behavior is the main motivation to employ ranking theory in FS for image retrieval. Again, the proposed Fc family of <sup>fi</sup>tness functions provide a signi<sup>fi</sup>cant dimensionality reduction, selecting about 15% of the original features.

Fig. 6 illustrates two screenshots of the 6-nearest neighbor query results over the ROI-250 image dataset, using the same query image. The samples on the left of both screenshots are the query images, which comprise the same malignant tumor. Fig. 6(a) shows the results with no feature selection for a 739-dimensional feature vector. Fig. 6(b) shows the results for the proposed method GA-FcB, with a reduced 50- dimensional feature vector (a reduction of 93% of the original feature

(a)  
![](/api/attachments/EAUZGY6A/fulltext/images/8b6a8d9d56e097c7d1a523c530a6b8f01081a0359af4325c4e6ac8f4d7764624.jpg)

(b)  
![](/api/attachments/EAUZGY6A/fulltext/images/b9db1139bfb4ab6eedfce16067c94394e53af601cc35894f89513d3ce00cd6d0.jpg)

(c)  
![](/api/attachments/EAUZGY6A/fulltext/images/3a8962d6a8cc081157b119096cd328efe74ecd1119df809260c9a71f699f9904.jpg)

(d)  
![](/api/attachments/EAUZGY6A/fulltext/images/f07a2289da021f185b776e994e05155df64f3d6b2a7aee52c48f36089b7c90e6.jpg)

(e)  
![](/api/attachments/EAUZGY6A/fulltext/images/2b43458e5a71194774342dea03e1510eae92c8c473dea444d5a44fea054d523c.jpg)  
Fig. 4. Precision and Recall curve for the Mammography-1080 image dataset: (a) GA and MS combined with our Fc family of <sup>fi</sup>tness functions and FR-Precision; (b) GA combined with <sup>fi</sup>tness functions based on classi<sup>fi</sup>cation error minimization of traditional classi<sup>fi</sup>ers; (c) FS based on statistical association rules and no feature selection; (d) <sup>fi</sup>lter algorithms, and (e) the most accurate method of each group

![](/api/attachments/EAUZGY6A/fulltext/images/ed0c57e016a38d4b64c5d80b4515b10a95f91a7fe744432eca62fb00da101bdb.jpg)

(b)  
![](/api/attachments/EAUZGY6A/fulltext/images/3b489e3f971595928f5834b0300caf7547cbd465874140cd1e0c649b3b36e8f0.jpg)

![](/api/attachments/EAUZGY6A/fulltext/images/22af5f64b60bd2f5d96247dfba7c6ef0afed83d768a820aef59405440a9203c8.jpg)

(d)  
![](/api/attachments/EAUZGY6A/fulltext/images/8f9352ee6948791892a6ad03e9767621bfee2bc7acf158a06f7a5e5adc094510.jpg)

(e)  
![](/api/attachments/EAUZGY6A/fulltext/images/5dffafcd523b397abb3123b25b6b96d7a7ccab3bf2f82f318bfef0ec321943f3.jpg)  
Fig. 5. Precision and Recall curves for the Lung-3258 image dataset: (a) GA and MS combined with our Fc family of <sup>fi</sup>tness functions and FR-Precision; (b) GA combined with <sup>fi</sup>tness functions based on classi<sup>fi</sup>cation error minimization of traditional classi<sup>fi</sup>ers; (c) FS based on statistical association rules and no feature selection; (d) <sup>fi</sup>lter algorithms, and (e)the most accurate method of each group.

vector). For this query, the precision with the proposed method is signi<sup>fi</sup>cantly higher (100% – all returned images are malignant) than the precision provided without FS (33% – only 2 in the 6 returned images are of the same class of the query image). This result shows that the usage of a large number of features to represent a medical image can highly reduce the precision of the content-based search. This emphasizes the “dimensionality curse” that CBIR systems face when the number of features becomes large: as the number of features increases, the signi<sup>fi</sup>cance of each feature decreases. Moreover, some features may work as noise, worsening the query results. This experiment shows how crucial it can be for a CBIR system to employ appropriate FS techniques to avoid dimensionality curse drawbacks.

## 6. Conclusions and future work

Content-based visual information retrieval de<sup>fi</sup>nitely has a large potential in the medical domain. However, its acceptance by the physicians will depend mainly on their ef<sup>fi</sup>cacy and ef<sup>fi</sup>ciency. This work proposed a novel GA-based FS framework to improve both ef<sup>fi</sup>cacy and ef<sup>fi</sup>ciency in content-based image retrieval (CBIR) systems. It employs a wrapper strategy that searches for the best reduced feature set, while improving (or at least preserving) the quality of the results of similarity searches. From a ranking evaluation function, three new <sup>fi</sup>tness functions namely, FcA, FcB and Fc were proposed and evaluated.

The proposed functions were embedded into a GA, generating the GA-FcA, GA-FcB and GA-Fc FS algorithms. They were compared with (a) the GA-based FS algorithms looking for error minimization of traditional classi<sup>fi</sup>ers (1NN, C4.5, SVM and Naive Bayes); (b) the StARMiner algorithm for association rule-based feature selection; (c) the FCBF, ReliefF, CFS and mRMR <sup>fi</sup>lter algorithms; and, (d) to all features combined (no feature selection). The results showed that the proposed method signi<sup>fi</sup>cantly outperforms all the others, including the multistart search.

By combining the quality of the query results with the criterion of minimization of the number of selected features, FcA and FcB answered queries more accurately and provided a more ef<sup>fi</sup>cient feature reduction mechanism than the <sup>fi</sup>tness function Fc alone. As a result, the <sup>fi</sup>nal query processing cost is always reduced.

Summarizing, the proposed FS techniques increase the precision of similarity searches and signi<sup>fi</sup>cantly decrease the data dimensionality, improving both the ef<sup>fi</sup>ciency of the access methods and the effectiveness of the CBIR system. Future work include: (1) enhancing the ef<sup>fi</sup>ciency of the proposed methods by introducing the local search into GA and exploring the synergy between <sup>fi</sup>lter methods and the GA wrapper methods for CBIR usage and, (2) integrating the textual information of patient clinical history and exams into the similarity search mechanism.

(a)  
![](/api/attachments/EAUZGY6A/fulltext/images/64f1aa631dbdcbe30004a53ed35e019b563b12d22671bb78bff127a0d628fb7d.jpg)

(b)  
![](/api/attachments/EAUZGY6A/fulltext/images/61d4682da26714fe097973d02210a3c92ef7d56c910f6cbecb2af6ed288b955c.jpg)  
Fig. 6. Results for ROI-250 image dataset: (a) 6-nearest neighbor query without feature selection and (b) 6-nearest neighbor query using feature selection by GA-FcA method

## Acknowledgments

We thank CNPq (Process: 306726 2009-2), CAPES, FAPESP, STIC-AmSud and Microsoft Research for the <sup>fi</sup>nancial support.

## References

[1] A. Aisen, L. Broderick, H. Winer-Muram, C. Brodley, A. Kak, C. Pavlopoulou, J. Dy, C.-R. Shyu, A. Marchiori, Automated storage and retrieval of thin-section CT images to assist diagnosis: system description and preliminary assessment, Radiology 228 (2003) 265–270

[2] M. Bacauskienea, A. Verikasa, A. Gelzinisa, D. Valinciusa, A feature selection technique for generation of classi<sup>fi</sup>cation committees and its application to categorization of laryngeal images, Pattern Recognition 42 (2009) 645–654.

[3] R. Baeza-Yates, B. Ribeiro-Neto, Modern information retrieval, Addison-Wesley, Essex, UK, 1999.

[4] B. Bartell, G. Cottrell, R. Belew, Optimizing similarity using multi-query relevance, Journal of the American Society for Information Science 49 (1998) 742–761.

[5] K. Beyer, J. Goldstein, R. Ramakrishnan, U. Shaft, When is “nearest neighbour” meaningful? Proceedings of the 7th International Conference on Data Theory, LNCS, 1540, Springer-Verlag, 1999, pp. 217–235.

[6] O. Cordón, E. Herrera-Viedma, C. López-Puljalte, M. Luque, C. Zarco, A review on the application of evolutionary computation to information retrieval, International Journal of Approximate Reasoning 34 (July 2003) 241–264

[7] J.G. Dy, C.E. Brodley, A. Kak, L.S. Broderick, A.M. Aisen, Unsupervised feature selection applied to content-based retrieval of lung images, IEEE Transactions on Pattern Analysis and Machine Intelligence 25 (3) (2003) 373-378

[8] W. Fan, E.A. Fox, P. Pathak, H. Wu, The effects of <sup>fi</sup>tness functions on genetic programming-based ranking discovery for web search, Journal of the American Society for Information Science and Technology 55 (7) (2004) 628–636.

[9] W. Fan, P. Pathak, M. Zhou, Genetic-based approaches in ranking function discovery and optimization in information retrieval – a framework, Decision Support Systems 47 (2009) 398–407.

[10] P. Fishburn, Non-linear preference and utility theory, Johns Hopkins University Press, 1998.

[11] D.E. Golberg, Genetic algorithms in search, optimization and machine learning Addison Wesley, 1989.

[12] R. Graham, R. Perriss, A. Scarsbrook, Dicom demysti<sup>fi</sup>ed: A review of digital <sup>fi</sup>le formats and their use in radiological practice, Clinical Radiology 60 (2005) 1133–1140.

[13] M.A. Hall, Correlation-based feature selection for discrete and numeric class machine learning Proceedings of the Seventeenth International Conference on Machine Learning, 2000, pp. 359–366.

[14] R.L. Haupt, S.E. Haupt, Practical Genetic Algorithms, second edition, John Wiley & Sons, New Jersey, United States, 2004.

[15] J. Horng, C. Yeh, Applying genetic algorithms to query optimization in document retrieval, Information Processing and Management 36 (2000) 737–759.

[16] S. Huang, L. Wulsin, H. Li, J. Guo, Dimensionality reduction for knowledge discovery in medical claims database: application to antidepressant medication utilization study, Computer Methods and Programs in Biomedicine 93 (2009) 115–123.

[17] S.K. Kinoshita, P.M.d. Azevedo-Marques, R.R. Pereira Jr., J.A.H. Rodrigues, R.M. Rangayyan. Content-based retrieval of mammograms using visual features related to breast density patterns, Journal of Digital Imaging 20 (2) (2007) 172–190.

[18] F. Korn, B. Pagel, C. Faloutsos, On the ‘dimensionality curse’ and the ‘self-similarity blessing’, IEEE Transactions on Knowledge and Data Engineering 13 (1) (2001) 96–111.

[19] H. Liu, L. Yu, Toward integrating feature selection algorithms for classi<sup>fi</sup>cation and clustering, IEEE Transactions on Knowledge and Data Enginnering 17 (4) (2005) 491–502.

[20] H. Liu, F. Hussain, C.L. Tan, M. Dash, Discretization: an enabling technique, Data Mining and Knowledge Discovery 6 (4) (2002) 393–423.

[21] C. López-Pujalte, V.P. Guerrero-Bote, F. Moya-Anegón, Order-based <sup>fi</sup>tness functions for genetic algorithms applied to relevance feedback, Journal of the American Society for Information Science 54 (2) (2003) 152–160.

[22] J. Lu, T. Zhao, Y. Zhang, Feature selection based-on genetic algorithm for image annotation, Knowledge-Based Systems 21 (2008) 887–891.

[23] H. Müller, N. Michoux, D. Bandon, A. Geissbuhler, A review of content-based image retrieval systems in medical applications – clinical bene<sup>fi</sup>ts and future directions, International Journal of Medical Informatics - IJMI 73 (1) (2004) 1–23.

[24] M. Oliveira, W. Cirne, P. Azevedo-Marques, Towards applying content-based image retrieval in the clinical routine, Future Generation Computer Systems 23 (2007) 466–474.

[25] H. Peng, F. Long, C. Ding, Feature selection based on mutual information: criteria of max-dependency, max-relevance, and min-redundancy, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (8) (2005) 1226–1238.

[26] M.X. Ribeiro, A.G.R. Balan, J.C. Felipe, A.J.M. Traina, Traina Jr., Mining statistical association rules to select the most relevant medical image features, Mining Complex Data, 165, Springer Berlin, Heidelberg, 2009, pp. 113–131.

[27] M. Robnic-Sikonja, I. Kononenko, Theoretical and empirical analysis of relieff and rrelieff, Machine Learning 53 (1–2) (2003) 23–69.

[28] S.F. Silva, A.J.M. Traina, M.X. Ribeiro, J.E.S. Batista-Neto, C. Traina Jr., Ranking evaluation functions to improve genetic feature selection in content-based image retrieval of mammograms, 22nd IEEE International Symposium on Computer-Based Medical Systems, CBMS, 2009, pp. 1–8.

[29] R. Taira, H. Huang, A picture archiving and communication system module for radiology, Computer Methods and Programs in Biomedicine 30 (1989) 229–237.

[30] L.C.C. Tamine, M. Boughanem, Multiple query evaluation based on an enhanced genetic next term algorithm, Information Processing and Management 39 (2) (2003) 215–231.

[31] S. Tan, R. Lewis, Picture archiving and communication systems: a multicentre survey of users experience and satisfaction, European Journal of Radiology 75 (3) (2010) 406–410.

[32] R.S. Torres, A.X. Falcão, M.A. Gonçalves, J.P.B.Z. Papa, W. Fan, E.A. Fox, A genetic programming framework for content-based image retrieval, Journal of the American Society for Information Science and Technology 42 (2) (2009) 283–292.

[33] A. Traina, C. Traina Jr., Similarity search in multimedia databases, in: B. Furht, O. Marques (Eds.), Handbook of Video Databases – Design and Applications, 1, CRC Press, 2003, pp. 711–738.

[34] C. Traina Jr., A. Traina, M. Araujo, J. Bueno, F. Chino, H. Razente, P. Azevedo-Marques, Using an image-extended relational database to support content-based image retrieval in a pacs, Computer Methods and Programs in Biomedicine 80 (1) (2005) s71–s83.

[35] A. Tsymbal, P. Cunningham, M. Pechenizkiy, S. Puuronen, Search strategies for ensemble feature selection in medical diagnostics, Proceedings of the 16th IEEE Symposium on Computer-Based Medical Systems, June 2003, pp. 124–129.

[36] C.-M. Wanga, Y.-F. Huang, Evolutionary-based feature selection approaches with new criteria for data mining: a case study of credit approval data, Expert Systems with Applications 36 (3 - Part 2) (2009) 5900–5908.

[37] I. Witten, E. Frank, Data mining: practical machine learning tools and techniques, second editionJMorgan Kaufmann, San Francisco, United States, 2005

[38] H. Yan, J. Zheng, Y. Jiang, C. Peng, S. Xiao, Selecting critical clinical features for heart diseases diagnosis with a real-coded genetic algorithm, Applied Soft Computing 8 (2008) 1105–1111.

[39] L. Yu, H. Liu, Ef<sup>fi</sup>cient feature selection via analysis of relevance and redundancy Journal of Machine Learning Research 5 (2004) 1205–1224.

[40] T. Zhao, J. Lu, Y. Zhang, Q. Xiao, Feature selection based on genetic algorithm for cbir, IEEE Congress on Image and Signal Processing, 2, 2008, pp. 495–499.

![](/api/attachments/EAUZGY6A/fulltext/images/d41c047a9f16501caccaaf0fea9eab64ac33af4e51c9d9a0a867d48f37d698b8.jpg)

![](/api/attachments/EAUZGY6A/fulltext/images/25e84a6fb2cac1d51c7bda6ead3fc2b89691f43825bd184a26c68bd5c00dd42a.jpg)

[41] Z. Zhu, X. Chen, Q. Zhu, Q. Xie, A ga-based query optimization method for web information retrieval, Applied Mathematics and Computation 185 (2007) 919–930.

![](/api/attachments/EAUZGY6A/fulltext/images/af9b1301ed6526754f714cc94ca1a6cd8da4683519bfc9ea77e914a01b1b6b7d.jpg)

![](/api/attachments/EAUZGY6A/fulltext/images/d0ff9394e998ab4ecb89430a5e6559a74d0b4e5f5f02605ca2331783a28fbadb.jpg)  
Sergio F. Silva received the B.Sc. degree in computer science from the Federal University of Goias, Brazil, in 2004. He received the the M.Sc. degree in computer science at the Faculty of Computation of the University of Uberlandia, Brazil, in 2007 and is pursuing the Ph.D. degree in computer science at the Mathematics and Computer Science Institute, University of Sao Paulo at Sao Carlos, Brazil. His research interests include multimedia data mining, computer-aided diagnosis and content-based image retrieval with special attention for optimization techniques based on evolutionary computation.

![](/api/attachments/EAUZGY6A/fulltext/images/061ff0edc17dbfd35f74876093f46f82db681c1a79ad618a8e53ee5f51b86632.jpg)

Marcela X. Ribeiro received the B.Sc. degree in computer engineering and the M.Sc. in computer science from the Federal University of Sao Carlos, Brazil, in 2002 and 2004, respectively. She received the Ph.D. degree in computer science at the Mathematics and Computer Science Institute of the University of Sao Paulo at Sao Carlos, Brazil, in 2008. She is currently a professor with the Computer Science Department of the Federal University of Sao Carlos. Brazil. Her research interests include multimedia data mining, visual data mining, visualization, computer-aided diagnosis and content-based image retrieval.

Joao Batista Neto is Assistant Professor at ICMC (the Institute for Mathematics and Computer Science), University of Sao Paulo, Sao Carlos/SP, Brazil. He received his Ph.D. degree in biomedical engineering from the University of London, Imperial College, U.K., in 1997. His current research interests are image processing and pattern recognition, especially feature extraction and selection.

Caetano Traina Jr. received the B.Sc. degree in electrical engineering, the M.Sc. and Ph.D. degrees in computer science from the University of Sao Paulo, Brazil, in 1978 1982 and 1987, respectively. He is currently a full professor with the Computer Science Department of the University of Sao Paulo at Sao Carlos, Brazil. His research interests include access methods for complex data, data mining, similarity searching and multimedia databases.

Agma J. M. Traina received the B.Sc., the M.Sc. and Ph.D. degrees in computer science from the University of Sao Paulo, Brazil, in 1983, 1987 and 1991, respectively. She is currently a full Professor with the Computer Science Department of the University of Sao Paulo at Sao Carlos Brazil. Her research interests include image databases, image mining, indexing methods for multidimensional data, information visualization, image processing for medical applications and optimization techniques based on evolutionary computation.
