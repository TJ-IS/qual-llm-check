---
otero_id: 4746
otero_key: "63YTMG5Z"
title: "Robust ensemble learning for mining noisy data streams"
authors: "Peng Zhang; Xingquan Zhu; Yong Shi; Li Guo; Xindong Wu"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Robust ensemble learning for mining noisy data streams

Peng Zhang <sup>a,</sup>⁎, Xingquan Zhu <sup>b</sup>, Yong Shi <sup>c,d</sup>, Li Guo <sup>a</sup>, Xindong Wu <sup>e,f</sup>

<sup>a</sup> Institute of Computing Technology, Chinese Academy of Sciences, Beijing, 100190, China

<sup>b</sup> Centre for Quantum Computation & Intelligent Systems, University of Technology Sydney, Broadway, NSW 2007, Australia

<sup>c</sup> Research Center on Fictitious Economy and Data Science, Chinese Academy of Sciences, Beijing, China

<sup>d</sup> College of Information Science & Technology, Univ. of Nebraska at Omaha, Omaha, NE 68182, USA

<sup>e</sup> School of Computer Science & Information Eng., Hefei University of Technology, Hefei 230009, China

<sup>f</sup> Department of Computer Science, University of Vermont, Burlington, VT 05405, USA

## a r t i c l e i n f o

Article history: Received 1 August 2009 Received in revised form 9 October 2010 Accepted 1 November 2010 Available online 5 November 2010

Keywords: Data stream Classi<sup>fi</sup>cation Ensemble learning Noise Concept drifting

## a b s t r a c t

In this paper, we study the problem of learning from concept drifting data streams with noise, where samples in a data stream may be mislabeled or contain erroneous values. Our essential goal is to build a robust prediction model from noisy stream data to accurately predict future samples. For noisy data sources, most existing works rely on data preprocessing techniques to cleanse noisy samples before the training of decision models. In data stream environments, these data preprocessing techniques are, unfortunately, hard to apply, mainly because the concept drifting in a data stream may make it very dif<sup>fi</sup>cult to differentiate noise from samples of changing concepts. Accordingly, we propose an aggregate ensemble (AE) learning framework. The aim of AE is to build a robust ensemble model that can tolerate data errors. Theoretical and empirical studies on both synthetic and real-world data streams demonstrate that the proposed AE learning framework is capable of building accurate classi<sup>fi</sup>cation models from noisy data streams.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Recent advances in networking, data collection, storage, and transmission have promoted a new type of data-intensive applications which rely on data streams for decision making [7,30]. Examples of such applications include wireless sensor networks, traf<sup>fi</sup>c management, telephone call records, online transactions, web servers' logs and so on. In order to discover knowledge from data streams, many stream mining based methods have been proposed. These methods, depending on the data characteristics and data collection objectives, can be roughly distinguished into three categories: continuous query and clustering data streams [2,6,8,9,12,20,22,27], frequent pattern mining from data streams [13,25,26,28,39], and generating predictive models for data streams [1,17–19,24,34,41,43–46].

From the classi<sup>fi</sup>cation perspective, building classi<sup>fi</sup>cation models on data streams usually confronts two challenges: (1) tremendous volumes of streaming data; and (2) continuous change of the decision concepts underneath the stream data, which is commonly referred to as concept drifting. In data stream environments, concept drifting usually happens in different ways: (1) gradual and moderate changes, and (2) abrupt and severe changes, which are illustrated in Fig. 1. From Fig. 1(a) to (b), the classi<sup>fi</sup>cation boundary $c _ { 1 }$ gradually changes to $c _ { 2 } ;$ on the other hand, from Fig. 1(b) to (c), the classi<sup>fi</sup>cation boundary abruptly changes from $c _ { 2 } \ t _ { 0 } \ c _ { 3 } ,$ and there is no connection (or correlations), at the observed moment, between these two boundaries (i.e., c and $c _ { 3 } )$

The challenges from large volumes of data and concept drifting raise the needs of designing effective classi<sup>fi</sup>cation models with high accuracy and good ef<sup>fi</sup>ciency. Motivated by the above challenges, existing classi<sup>fi</sup>cation models in the <sup>fi</sup>eld can be roughly categorized into two groups: online incremental learning [16,23,31,37] and ensemble learning [24,34,35,38,47]. The incremental learning strategy tries to design a single learning model to represent an entire data stream by continuously updating the model with the newly arriving data, such that the model can always capture the most recent decision logics in the data stream. On the other hand, ensemble learning regards a data stream as separated data chunks, and builds several base classi<sup>fi</sup>ers from separated data chunks to generate an ensemble classi<sup>fi</sup>er for prediction. Although these models were proved to be effective and accurate, an inherent limitation is that they were mainly designed for quality stream data without an explicit consideration of the data errors. Consequently, these learning frameworks are likely to suffer a great loss when handling real-world data streams containing erroneous data values.

Indeed, in traditional data mining tasks, a large number of methods exist for tackling noise or erroneous attribute errors [10,29,32,36,49]. These methods can be roughly categorized into two types: (1) data preprocessing methods, and (2) robust learning methods. Data preprocessing focuses on identifying and cleansing noisy data, such that the cleansed data can be used to build accurate prediction models. For instance, Brodley and Friedl [10] concluded that identifying and removing mislabeled training examples can help generate more accurate prediction models than the ones trained from raw data. Quinlan [32] and Zhu et al. [49] studied the impact of data errors on inductive learning and asserted that data errors are the main sources of the classi<sup>fi</sup>cation errors, and data cleansing is an effective tool to help a learning algorithm achieve performance gain. On the other hand, a robust learning method tries to build robust models that can greatly, if not completely, reduce the noise impact. Two representative robust learning approaches include pruning for decision trees and prototype selection for instance-based learning [3]. The essential idea behind these approaches is to simplify the prediction models and prevent the learner from over<sup>fi</sup>tting to the noisy data. In addition to the single learner based approach, classi<sup>fi</sup>er ensembling [4,15,21] is another type of robust learning which shows good performance on noisy data.

![](/api/attachments/63YTMG5Z/fulltext/images/cb22f78277ae6061e16c9b10171ef6085955283c79d629d95f147b937f46b705.jpg)  
Fig. 1. A conceptual view of concept drifting in data streams. In three consecutive time stamps, the classi<sup>fi</sup>cation boundary drifts from $c _ { 1 } \ t _ { 0 } \ c _ { 2 } ,$ , and <sup>fi</sup>nally to $c _ { 3 } .$ From $T _ { 1 }$ to $T _ { 2 } ,$ the classi<sup>fi</sup>cation boundary changes gradually, while from $T _ { 2 }$ to $T _ { 3 } ,$ the classi<sup>fi</sup>cation boundary changes abruptly

For noisy data streams, most existing research focuses on designing effective data preprocessing algorithms to cleanse noise from data streams, such that the cleansed data can be used to build accurate models. For example, Chu et al. [14] proposed a statistical estimation framework to identify outliers in data streams. Zhu et al. [50] proposed a maximum variance margin (MVM) based <sup>fi</sup>ltering framework to cleansing noise. Wang et al. [40] proposed a clusteringbased method to wipe off noise. Although these methods are effective in their own problem de<sup>fi</sup>nitions, most of them share two common disadvantages. First, most of them implicitly make some statistical assumptions to describe data streams, whereas the assumed statistical models may not always exist in reality. Second, all these methods usually employ a multi-scan learning approach to cleanse noise, and then learn from the cleansed data. In dynamic data stream environments, it is urged that the training of prediction models should only require one scanning of the stream data.

The above observations motivate our research on robust learning from noisy data streams using a new aggregate ensemble (AE) framework. In our proposed design, AE <sup>fi</sup>rst trains base classi<sup>fi</sup>ers using different learning algorithms on different data chunks. It then combines all the base classi<sup>fi</sup>ers to form a classi<sup>fi</sup>er ensemble through model voting. By doing so, AE is supposed to be robust for both concept drifting and noisy data problems. Experimental results on both synthetic and real-world data streams show that the AE framework is superior to other ensemble-based learning frameworks for noisy data streams.

The remainder of this paper is structured as follows. Section 2 describes noise in data streams in general. Section 3 introduces the proposed AE framework. Section 4 provides theoretical studies on the AE framework. Section 5 empirically studies the AE framework on both synthetic and real-world data streams. We conclude the paper in Section 6.

## 2. Noisy description for data streams

According to the characteristics of the stream data, existing work roughly describes data streams into the following two styles:

stationary data streams [16,23,38,43] and dynamic data streams [18,44–46].

According to the stationary description, if data streams are divided into data chunks as shown in Fig. 2, then training data chunks (which include both historical data chunks and the up-to-date chunk) will have a similar or identical distribution to the yet-to-come data chunk. So classi<sup>fi</sup>ers built from the training data chunks will have reasonably good performance in classifying data from the yet-to-come data chunk. The advantage of the stationary description is that we may directly apply traditional classi<sup>fi</sup>cation techniques to the data streams. For example, since the up-to-date data chunks have the same distribution as the yet-to-come data chunk, we can collect all historical classi<sup>fi</sup>ers to build a classi<sup>fi</sup>er ensemble. However, this stationary description takes no consideration of the concept drifting in stream data, so it can hardly, if not impossible, be used to describe most real-world data streams.

Noticing the limitations of the stationary description, a recent work [18] describes the data streams in a dynamic scenario where training chunks have different distributions p(x,y) (where x denotes the feature vector and y denotes the class label) from that of the yetto-come data chunk, and classi<sup>fi</sup>ers built on the training set may perform only slightly better than random guessing or simply predicting all examples to belong to one single class. Comparing to the stationary description, the dynamic description emphasizes on the situation that training data chunks do not necessarily have the same distribution as the yet-to-come data chunk. Under this description, building classi<sup>fi</sup>ers from the up-to-date data chunk to predict the yetto-come data chunk is better than building classi<sup>fi</sup>ers from the aggregation of all historical chunks because the buffered chunks (probably outdated with respect to the newly arrived data chunk) will deteriorate the ensemble performance. In a narrow sense, this dynamic description is much looser than the stationary description, which makes it more applicable for mining concept drifting data streams. However, the disadvantage of the dynamic description is also obvious, in the sense that it doesn't discriminate concept drifting from data errors. If the up-to-date data chunk contains noisy samples, building classi<sup>fi</sup>ers on this noisy data chunk to predict the yet-tocome data chunk may cause more errors than using a classi<sup>fi</sup>er ensemble built on previously buffered data chunks. Consequently, although the dynamic description is more reasonable than the stationary description for data streams, in practice, it is still not capable of describing all the realistic data streams.

Consider a data stream management system whose buffer contains <sup>fi</sup>ve consecutive data chunks as shown in Fig. 3. The stationary description can only cover the process from $D _ { 1 }$ to $D _ { 2 } ,$ , where the distribution $p _ { 1 } ( x , y )$ remains unchanged. The dynamic description covers the process from $D _ { 2 }$ to $D _ { 3 } ,$ where the concept drifts from $p _ { 1 } ( x , y )$ to $p _ { 2 } ( x , y )$ without being interrupted by noisy data chunks. A more general situation, as depicted in the process from $D _ { 3 }$ to $D _ { 5 } ,$ , is that the concept drifting $( p _ { 2 } ( x , y )$ evolves to $p _ { 3 } ( x , y ) )$ is mixed with noise (a noisy data chunk $D _ { 4 }$ is observed). To explicitly describe this type of data streams, we de<sup>fi</sup>ne a noisy description of data streams as follows:

![](/api/attachments/63YTMG5Z/fulltext/images/16dc19640729950ca6f4a4ab790326376d013ff562788db8ae75c9a3da7f08c3.jpg)  
Fig. 2. An illustration of the “historical”, “up-to-date” and “yet-to-come” data chunks. A data stream can be split into two parts: the observed data stream (which is denoted by the solid lines) and the unobserved data stream (which is denoted by the dotted lines). Assume the data stream is processed chunk-by-chunk. The observed data stream can be further categorized into two types: the latest data chunk is called the “up-to-date” chunk, while the remaining data chunks are called the “historical” data chunks. Besides, the “yet-to-come” data chunk is the <sup>fi</sup>rst data chunk of the unobserved data streams.

Noisy description for data streams: Mining from real-world data streams may confront the challenges of concept drifting and data errors simultaneously.

The noisy description addresses both concept drifting and data errors in a data stream management system. It is much more general than the stationary and dynamic descriptions. So it can be adapted for generic data streams.

## 3. Ensemble frameworks for mining data streams

The nature of continuous volumes of the stream data raises the needs of designing effective classi<sup>fi</sup>ers with high accuracy in predicting future testing instances as well as good ef<sup>fi</sup>ciency in handling massive volumes of training instances. In the past few years, many solutions have been proposed to build prediction models from data streams. An early solution is to build model by using online incremental methods [16,23] which update a single model by incorporating newly arrived data. During the learning process, incremental methods continuously revise the model to discover new patterns in the most recent data chunk. For example, Domingos and Hulten [16] introduced an ultra fast decision tree learner VFDT which incrementally builds Hoeffding trees from the high-volume data streams. Similar approach was extended to CVFDT [23] which handles time changing and concept drifting streams. By doing so, most of the incremental methods violate the ef<sup>fi</sup>ciency rule because updating a classi<sup>fi</sup>er according to the newly arrived data can be a time-consuming process. An alternative solution is to build a single and simple classi<sup>fi</sup>er on the up-to-date chunk without considering historical data chunks, i.e., discarding old classi<sup>fi</sup>ers and rebuilding a new classi<sup>fi</sup>er on the new data chunk. This build-then-discard method, unfortunately, may not work well because of the important loss incurred by the discarded classi<sup>fi</sup>ers. To overcome this challenge, a number of ensemble methods have been proposed.

Different from the incremental learning where the goal is to deliver a single model, ensemble learning intends to produce a number of models and relies on their voting for <sup>fi</sup>nal predictions. Such design brings two advantages for ensemble learning to handle data streams: (1) because models are trained from a small portion of stream data, it can ef<sup>fi</sup>ciently handle streams with fast growing data volumes; and (2) because the <sup>fi</sup>nal predictions are the voting of a number of base models, the concept drifting in the stream can be adaptively and rapidly addressed by changing the weight value of each voting member. For example, Street and Kim [35] proposed a SEA algorithm, which combines decision tree models using majorityvoting. Kolter and Maloof [24] proposed an ensemble method by using weighted online learners to handle drifting concepts. Wang et al. [38] proposed a weighted ensemble, in which they assign each classi<sup>fi</sup>er a weight reversely proportional to the classi<sup>fi</sup>er's accuracy on the most recent data chunk. Yang et al. [43] proposed proactive learning where concepts (models) learnt from previous chunks are used to foresee the best model to predict data in the current chunk. Zhu et al. [48] proposed an active learning framework to selectively label instances for concept drifting data streams. Gao et al. [18] proposed to build different base classi<sup>fi</sup>ers on a most recent data chunk to construct the classi<sup>fi</sup>er ensemble.

![](/api/attachments/63YTMG5Z/fulltext/images/1b8eb79f722a0d0f75629c705ff280ca869e9c6d20ef324a857c803bd0770aa6.jpg)  
Fig. 3. A conceptual view of noisy data in data stream management system. The data stream management system can be separated into <sup>fi</sup>ve parts: a stream buffer subsystem, a stream loading subsystem, a stream query subsystem, a stream mining subsystem, and a stream scheduler subsystem. In the stream buffer subsystem, there are <sup>fi</sup>ve buffered data chunks, $D _ { 1 } , D _ { 2 } , . . . , D _ { 5 } ,$ , of which D is a noise data chunk. D and D share the same distribution $P _ { 1 } ( x , y )$ . From $D _ { 2 }$ to $D _ { 3 } ,$ the underlying concept changes from $P _ { 1 } ( x , y )$ to P (x,y). From D to $D _ { 4 }$ and <sup>fi</sup>nally to $D _ { 5 } ,$ the concept changes from $P _ { 2 } ( x , y ) \ \mathrm { t o } P _ { 3 } ( x , y )$ , meanwhile, a noisy chunk $D _ { 4 }$ is observed between $D _ { 3 }$ and $D _ { 5 } .$ . The stationary description of data streams can only cover the process from $D _ { 1 } \ \mathrm { t o } \ D _ { 2 } ,$ while the dynamic description of data streams only covers the process from $D _ { 2 }$ to $D _ { 3 } .$ Our noisy description covers a much more common process from $D _ { 3 }$ to $D _ { 5 } .$

In summary, the above ensemble frameworks for stream data mining can be roughly categorized into the following two categories, according to their ways of forming the base classi<sup>fi</sup>ers: horizontal ensemble (including weighted ensemble) frameworks which build base classi<sup>fi</sup>ers using several buffered data chunks (as illustrated in Fig. 4(a)), and vertical ensemble framework which build base classi<sup>fi</sup>ers on the up-to-date data chunk using different algorithms (as illustrated in Fig. 4(b)).

## 3.1. Horizontal ensemble and weighted ensemble frameworks

Consider a data stream containing an in<sup>fi</sup>nite number of data chunks $\{ D _ { i } \} _ { i = 1 } ^ { + \infty }$ . Due to the limitation of the storage space, the system buffer can only accommodate at most n consecutive chunks each of which contains a certain number of instances. Assume at the current time stamp we are observing the nth chunk $D _ { n } ,$ and the buffered data chunks are denoted by $D _ { 1 } , D _ { 2 } , . . . , D _ { n } .$ In order to predict data in a newly arrived chunk $D _ { n + 1 } ,$ one can choose a learning algorithm L to build a base classi<sup>fi</sup>er $\cdot f _ { i }$ from each of the buffered data chunks $D _ { i } ,$ say $f _ { i } = \mathcal { L } ( D _ { i } )$ , and then predict each instance x in $D _ { n + 1 }$ <sub>1</sub> by combining the predictions of the base classi<sup>fi</sup>ers $f _ { i } ( i { = } 1 , 2 , . . . , N )$ to form a classi<sup>fi</sup>er ensemble through the model averaging mechanism shown in Eq. (1) [15,24,38,48].

(a) Horizontal Ensemble Framework  
![](/api/attachments/63YTMG5Z/fulltext/images/e763f6f91683fd1b5622d564afecffc1663b5912b94a49a572ea474313a53ada.jpg)

(b) Vertical Ensemble Framework  
![](/api/attachments/63YTMG5Z/fulltext/images/af3edeb20181441897b443976c8ae0350f6db1e638bac7bffc1f8b689d92661b.jpg)

(c) Aggregate Ensemble Framework  
![](/api/attachments/63YTMG5Z/fulltext/images/2ff7efb015918cf74693391fc7af1dd5d4eb7844d8397909a7fcf5c51639a8b2.jpg)  
Fig. 4. A conceptual <sup>fl</sup>owchart of the classi<sup>fi</sup>er ensemble framework for stream data mining where (a) shows the horizontal ensemble framework, which builds different classi<sup>fi</sup>ers on different data chunks; (b) shows the vertical ensemble framework, which builds different classi<sup>fi</sup>ers on the up-to-date data chunk with different learning algorithms; and (c) shows the aggregate ensemble framework, which builds classi<sup>fi</sup>ers on different data chunks using different learning algorithms.

$$
f _ {H E} (x) = \frac {1}{N} \sum_ {i = 1} ^ {N} f _ {i} (x)\tag{1}
$$

An alternative version of the horizontal ensemble is to add weight values to the base classi<sup>fi</sup>ers [38,48]. Different from the model averaging, a weighted ensemble minimizes the variance error $e _ { v }$ of each base classi<sup>fi</sup>er on the up-to-date data chunk, then assigns each classi<sup>fi</sup>er a weight that is reversely proportional to the error rate $e _ { v \cdot }$ The advantage of the horizontal ensemble and weighted ensemble is twofold: (1) they can reuse information of the buffered data chunks, which may be bene<sup>fi</sup>cial for the testing data chunk; and (2) they are robust to noisy streams because the <sup>fi</sup>nal decisions are based on the classi<sup>fi</sup>ers trained from different chunks. Even if noisy data chunks may deteriorate some base classi<sup>fi</sup>ers, the ensemble can still maintain relatively stable prediction accuracy. The disadvantage of such an ensemble framework, however, lies in the fact that if the concepts of the stream continuously change, information contained in previously buffered classi<sup>fi</sup>ers may be invalid to the current data chunk. As a result, combining old-fashioned classi<sup>fi</sup>ers may not improve the overall prediction accuracy. In summary, both horizontal and weighted ensembles, in fact, are based on the stationary description of the data streams that buffered data chunks share similar or identical distributions to the yet-to-come data chunk, such that information in the buffered data chunks can be used to predict the yet-to-come data chunk.

## 3.2. Vertical ensemble framework

Assume we have m learning algorithms $L _ { j } \left( j = 1 , 2 , . . . , m \right)$ , a vertical ensemble [18,45] builds base classi<sup>fi</sup>ers using each algorithm on the up-to-date data chunk $D _ { n }$ as $f _ { j } = \mathcal { L } _ { j } ( D _ { n } )$ , and then combines all base classi<sup>fi</sup>ers through model averaging as given in Eq. (2),

$$
f _ {V E} ^ {n} (x) = \frac {1}{m} \sum_ {i = 1} ^ {m} f _ {i n} (x).\tag{2}
$$

In the case that prior knowledge of the yet-to-come data chunk is unknown, model averaging on the most recent chunk can achieve minimum expectation error on the test set. In other words, building classi<sup>fi</sup>ers using different learning algorithms can decrease the expected bias error compared to any single classi<sup>fi</sup>ers. For example, assuming a data stream whose joint probability $p ( x , y )$ evolves continuously, if we only use a stable learner such as SVM, then SVM may perform better than an unstable classi<sup>fi</sup>er when $p ( x )$ changes while p(y|x) remains unchanged. On the other hand, if we only use an unstable learner such as decision trees, then decision trees may perform better than SVM when $p ( x )$ does not evolve much but $p ( y | x )$ changes dramatically. When we have no prior knowledge on whether the evolving of $p ( x , y )$ is triggered by $p ( x )$ or p(y|x), it is dif<sup>fi</sup>cult to determine whether a stable classi<sup>fi</sup>er or an unstable classi<sup>fi</sup>er is better, so combining these two types of classi<sup>fi</sup>ers is likely to be a better solution than simply choosing either of them. Although the vertical ensemble has a much looser condition (distribution $p ( x , y )$ may continuously change) than the stationary description (distribution p $\left( x , y \right)$ remains unchanged), it also has a severe pitfall for realistic data streams. The vertical ensemble builds classi<sup>fi</sup>ers only on a single upto-date data chunk, but as we have discussed before, a realistic data stream system may contain data errors. If the up-to-date data chunk is a noisy data chunk, the results may suffer from severe performance deterioration. Without realizing the noise problems, the vertical ensemble limits itself merely to the concept drifting scenarios, but not to the realistic data streams.

## 3.3. Aggregate ensemble framework

The disadvantages of the above two ensemble frameworks motivate the proposed aggregate ensemble framework (which is illustrated in Fig. 4(c)). We <sup>fi</sup>rst use m learning algorithms $L _ { i } ( i = 1 , 2$ $\ldots , m )$ to build classi<sup>fi</sup>ers on n buffered data chunks j $( j = 1 , . . . , n )$ , and then train m-by-n base classi<sup>fi</sup>ers $f _ { i j } = \mathcal { L } _ { i } ( D _ { j } )$ , where i denotes the ith algorithm, and j denotes the jth data chunk. Then we combine these base classi<sup>fi</sup>ers to form an aggregate ensemble through model averaging de<sup>fi</sup>ned in Eq. (3), which indicates that the aggregate ensemble is a mixture of the horizontal ensemble and vertical ensemble, and its base classi<sup>fi</sup>ers constitute a classifier matrix (CM) in Eq.(4).

$$
f _ {A E} = \frac {1}{m n} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} f _ {i j} (x)\tag{3}
$$

$$
C M = \left[ \begin{array}{c c} f _ {1 1} & f _ {1 2} \dots .. f _ {1 n} \\ f _ {2 1} & f _ {2 2} \dots .. f _ {2 n} \\ \dots \dots \\ f _ {m 1} & f _ {m 2} \dots .. f _ {m n} \end{array} \right] _ {m * n}\tag{4}
$$

In Eq. (4), each element $f _ { i j }$ in CM represents a base classi<sup>fi</sup>er built by using algorithm i on data chunk j. As we have mentioned in the vertical ensemble, classi<sup>fi</sup>ers on each column of CM (i.e., classi<sup>fi</sup>ers built on the same data chunk using different learning algorithms) are used to reduce the expected classi<sup>fi</sup>er bias error on unknown test data. Classi<sup>fi</sup>ers on each row of CM (i.e., classi<sup>fi</sup>ers built on different data chunks using the same learning algorithm) are used to reduce the impact of noisy data chunks. For example, when the up-to-date training chunk is a noisy chunk, combining classi<sup>fi</sup>ers built from the historical data chunks may alleviate the noisy impact. By building a classi<sup>fi</sup>er matrix CM, the aggregate ensemble is capable of solving a realistic data stream containing both concept drifting and data errors.

## 4. Theoretical studies of the aggregate ensemble

## 4.1. Performance study of AE framework

In this subsection, we explore why and when AE performs better than HE and VE methods. As we have described in the earlier section, on each data chunk, the aggregate ensemble builds m classi<sup>fi</sup>ers by using m different learning algorithms. For a speci<sup>fi</sup>c test instance x in the yet-to-come data chunk, the horizontal ensemble uses classi<sup>fi</sup>ers on a row in matrix CM to predict x, i.e., if we choose learning algorithm $i ( 1 \leq i \leq m )$ , then the horizontal ensemble can be denoted by $\operatorname { E q . }$ (5)

$$
f _ {H E} ^ {i} (x) = \frac {1}{n} \sum_ {j = 1} ^ {n} f _ {i j} (x).\tag{5}
$$

The vertical ensemble can be denoted by model averaging on the last column (column n) of the Matrix CM, which is given in Eq. (6)

$$
f _ {V E} ^ {n} (x) = \frac {1}{m} \sum_ {i = 1} ^ {m} f _ {i n} (x).\tag{6}
$$

An aggregate ensemble combines all classi<sup>fi</sup>ers in CM as base classi<sup>fi</sup>ers, through the averaging rule de<sup>fi</sup>ned by Eq. (2). Accordingly, the horizontal ensemble and vertical ensemble are, in fact, two special cases of the aggregate ensemble. Gao et al. [18] proved that in data stream scenario, the performance of a single classi<sup>fi</sup>er within a classi<sup>fi</sup>er ensemble is expected to be inferior to the performance of the entire classifier ensemble, The horizontal ensemble and vertical ensemble, as special cases of the aggregate ensemble, are not expected as good as the aggregate ensemble. For example, when combining each column in CM, one can have a variant of CM as ${ C M } _ { c } =$ $\left[ g _ { 1 } , g _ { 2 } , . . . , g _ { n } \right]$ , where each $g _ { i } = [ f _ { 1 i } , f _ { 2 i } , . . . , f _ { m i } ] ^ { T }$ is independent of each other and shares the same distribution, say p(g). Then the mean squared error of the horizontal ensemble (with the ith learning algorithm) on a test instance x (with class label y) can be denoted by

$$
M S E _ {H E} ^ {i} (x) = E _ {p (g)} (y - g _ {i} (x)) ^ {2} = y ^ {2} - 2 y \cdot E _ {p (g)} g _ {i} (x) + E _ {p (g)} g _ {i} ^ {2} (x).\tag{7}
$$

For the aggregate ensemble, the mean squared error on x can be calculated as

$$
M S E _ {A E} (x) = E _ {p (g)} \left(y - E _ {p (g)} g _ {i} (x)\right) ^ {2} = y ^ {2} - 2 y \cdot E _ {p (g)} g _ {i} (x) + E _ {p (g)} ^ {2} g _ {i} (x).\tag{8}
$$

So the difference between Eqs. (7) and (6) is denoted by Eq. (9),

$$
M S E _ {A E} (x) - M S E _ {H E} ^ {i} (x) = E _ {p (g)} ^ {2} g _ {i} (x) - E _ {p (g)} g _ {i} ^ {2} (x) \leq 0. (\text { since } E ^ {2} (x) \leq E \left(x ^ {2}\right))\tag{9}
$$

Accordingly, we assert that the error rate of the aggregate ensemble is expected to be less or equal to the error rate of the horizontal ensemble. Similarly, if we regard CM as a column vector where each element is a combination of different rows in CM, we can show that the mean squared error of the aggregate ensemble is also expected to be less or equal to that of the vertical ensemble.

In the following we provide some intuitive explanations on why and when AE performs better than HE and VE by using two toy examples in Figs. 5 and 6. Note that our comparisons here are rather intuitive and qualitative, and rigorous numeric comparisons will be reported in the experimental results in the next section. As shown in Fig. 5, assume that AE is trained using three learning algorithms M , $M _ { 2 } ,$ and $M _ { 3 } ,$ where HE(M ) denotes an HE model trained using learning algorithm $M _ { i \cdot }$ For each model, we list three results: (1) training accuracy at time A, (2) test accuracy at time A, and (3) test accuracy at time B which immediately follows A. We can observe that for concept drifting data streams, it is dif<sup>fi</sup>cult to <sup>fi</sup>nd a single “optimal” learning algorithm with the best performance across the whole stream. For example, model $\mathrm { H E } ( M _ { 2 } )$ has the best prediction accuracy at time stamp A, but unfortunately, it has the worst performance at the next time stamp B. Model HE $\left( M _ { 3 } \right)$ has the worst performance at time A, but it performs the best at time stamp B. On the other hand, AE can guarantee the most reliable performance by combining different learning algorithms. This is because in dynamic data stream environments it is essentially dif<sup>fi</sup>cult to know which learning algorithm performs the best at a particular time point. By integrating different learning algorithms as a uni<sup>fi</sup>ed model, we can expect AE to have the smallest variance error and thus have the best prediction accuracy.

![](/api/attachments/63YTMG5Z/fulltext/images/e05803f8abb7c7e9b96408dc7870c09a1e6b84a69ce5d1dbf310a53584a3d3b5.jpg)  
Fig. 5. A toy example for comparisons between AE and three HE ensemble methods trained with different learning algorithms (i.e., algorithms M , M , and M ). For each ensemble method, three results (bars) are listed for comparisons. The left bar denotes the training accuracy at time A, the bar in the middle denotes the test accuracy at time A, and the bar on the right denotes the test accuracy at time B which follows time stamp A. It is obvious that at time A, the higher the training accuracy, the better the prediction result. However, this result doesn't hold when the concept drifts at the next time stamp B

![](/api/attachments/63YTMG5Z/fulltext/images/1a287a7c520e438e3f3783625748242d2a3be5a223f1357648daea3ba7f6af37.jpg)  
Fig. 6. A toy example for comparison between AE and VE. The concept (i.e., the classi<sup>fi</sup>cation boundary) drifts marginally from chunk $D _ { 1 }$ to $D _ { 2 } ,$ and <sup>fi</sup>nally to $D _ { 4 } .$ Notice that the up-to date chunk $D _ { 3 }$ is a noisy chunk that carries useless or erroneous information when predicting the yet-to-come data chunk $D _ { 4 } .$

AE performs better than VE when the concept drifts marginally and the up-to-date training chunk contains a signi<sup>fi</sup>cant amount of noisy samples. As illustrated in Fig. 6, assume that the concept drifts slightly along data chunks, and the up-to-date chunk $D _ { 3 }$ is a noisy chunk. VE built on the up-to-date chunk $D _ { 3 }$ will show deteriorated performance in predicting $D _ { 4 } .$ On the other hand, AE can largely avoid such a limitation by incorporating information from classi<sup>fi</sup>ers trained from the historical data chunks $D _ { 1 }$ and $D _ { 2 } .$

Although we have demonstrated that AE, on average, outperforms HE and VE, we are not claiming that AE always performs the best in data stream scenarios. For example, HE may outperform AE if the concept drifts marginally in data streams. In this case, the joint probability distribution p(x,y) will stay stable across the data streams, and thus we can select a strong learning algorithm (i.e., SVM) to construct HE and expect HE to outperform AE. On the other hand, VE may outperform AE if the concept drifts signi<sup>fi</sup>cantly and the up-todate chunk contains very few noisy samples. In such a case, oldfashioned historical information in AE will deteriorate the learner performance even worse.

## 4.2. Time complexity analysis

In this subsection, we study the time complex of the AE framework and discuss whether it is a suitable model, from computational cost perspective, for mining noisy data streams. As discussed earlier, compared to its peers, AE combines much more base classi<sup>fi</sup>ers to build an ensemble predictor. This raises the concern on the ef<sup>fi</sup>ciency of AE due to its additional cost for training extra base classi<sup>fi</sup>ers.

To study AE's time complexity, let's consider the following example. Assume the buffer of the system contains d data chunks, each of which contains N instances. Assume further that m learning algorithms are used to build models. Each time when a new data chunk arrives, we need to follow two steps to update an ensemble: (1) build new base classi<sup>fi</sup>er(s) on the new data chunk; and (2) update classi<sup>fi</sup>er ensemble by incorporating new base classi<sup>fi</sup>er(s). Without loss of generality, we assume that training a new base classi<sup>fi</sup>er needs O(N lg N) time on average, while updating the classi<sup>fi</sup>er ensemble to include one base classi<sup>fi</sup>er requires O(Γ) time, where Γ is related to the dimensionality of attributes. Then the updating of the HE ensemble for each new data chunk needs to (1) build a new base classi<sup>fi</sup>er (which costs O(N lg N) time), and then (2) combine the most recent d base classi<sup>fi</sup>ers (which costs O(dΓ) time) together for prediction. The total time cost can be calculated by Eq. (10),

$$
O (H E) = O (N l g N) + O (d \Gamma).\tag{10}
$$

Since training a base classi<sup>fi</sup>er dominates the total cost (i.e., $O ( \Gamma ) \ll O ( N l g N ) )$ , and the number of data chunks d in the buffer is rather small. The time complexity of the HE ensemble can be simpli<sup>fi</sup>ed as in Eq. (11),

$$
O (H E) = O (N l g N) + O (d \Gamma) = O (N l g N).\tag{11}
$$

In comparison, VE builds m base classi<sup>fi</sup>ers for each new data chunk. Accordingly, its time complexity O VE can be calculated by Eq. (12),

$$
O (V E) = O (m) * (O (N l g N) + O (\Gamma)) = O (m N l g N).\tag{12}
$$

For AE, it <sup>fi</sup>rst builds m classi<sup>fi</sup>ers when a new data chunk arrives, and combines all the d\*m base classi<sup>fi</sup>ers to build an ensemble. So its time complexity can be calculated by Eq. (13),

$$
O (A E) = O (m N l g N) + O (d m \Gamma) = O (m N l g N).\tag{13}
$$

Combining Eqs. (11), (12), and (13), we have the following two conclusions: (1) AE is, asymptotically, as ef<sup>fi</sup>cient as VE. Both of them have the same time complexity O mN lg N ; (2) AE requires more time complexity than HE because AE needs to train m base classi<sup>fi</sup>ers for each new data chunk. This limitation, in practice, can be alleviated by using a multi-core or multi-processor computing system, where base classi<sup>fi</sup>ers can be dispatched and trained on different computation units in parallel.

## 5. Experiments

To evaluate the performance of AE, we carry out experimental studies on both synthetic and real-world data streams, by implementing all algorithms in Java and the WEKA [42] data mining package. Unless speci<sup>fi</sup>ed otherwise, we use Decision Tree (Tree) [33], Logistic Regression (LR) classi<sup>fi</sup>er, and Libsvm (SVM) [11] to build AE. All tests are carried out on a PC machine with a 1.7 G CPU and 2 GB memory.

## 5.1. Assessment criteria

For ease of comparisons, we <sup>fi</sup>rst summarize the assessment criteria of the ensemble-based data stream mining models. Due to the importance of prediction accuracy in assessing a classi<sup>fi</sup>cation model, many existing ensemble-based models [34,35,45,48] compare the average prediction accuracy to its peers. Recently, Gao et al. [18] proposed to provide chunk-by-chunk comparisons and proposed several other measurements such as the average ranking (AR), number of wins (#W) and loses (#L). On the other hand, considering that a good ensemble classi<sup>fi</sup>er should have high prediction accuracies and low computational overhead, Wang et al. [38] evaluated their method with respect to both the prediction accuracy and system training time. Similar work can be found in many other data stream classi<sup>fi</sup>cation methods [17,19,23,34,35]. In our experiments, we <sup>fi</sup>rst compare the ensemble-based models with respect to the prediction accuracy on a synthetic data stream and the real-world KDDCUP'99 network intrusion data set. We then compare the models on another real-world wireless sensor data stream with respect to both prediction accuracy and the system runtime performance.

Three assessment criteria employed in our experimental study are as follows. Suppose a data stream has n data chunks, $D _ { 1 } , D _ { 2 } , . . . . , D _ { n } .$ We aim to build a classi<sup>fi</sup>er to predict all instances' labels in the yet-tocome chunk $D _ { i + 1 } .$ Consider an instance x in $D _ { i + 1 } ,$ if the predicted class label of x is the same as the label of x with the highest posterior probability, we regard x as a correctly classi<sup>fi</sup>ed instance. Accordingly, we de<sup>fi</sup>ne Accuracy (acc) as the percentage of the number of correctly classi<sup>fi</sup>ed instances in $D _ { i + 1 }$ . Furthermore, we rank all algorithms in an order from 1 to 5 according to their accuracies, with the most accurate algorithm ranked as 1 and the least accurate algorithm ranked as 5. In the case that two classi<sup>fi</sup>ers or more have the same accuracy, we will assign the same ranking order to them. In addition, we de<sup>fi</sup>ne the other two measures, number of wins (#W) and losses (#L) as follows: if a classi<sup>fi</sup>er is ranked as 1, then we increase its #W by 1; on the contrary, if a classi<sup>fi</sup>er is ranked as 5, we add its #L by 1. Following the above process for n−1 times, we have the average accuracy (Aacc), average ranking (AR), standard deviation of the ranks (SR), and the total numbers of #W and #L for all the algorithms. Ideally, a good classi<sup>fi</sup>er should have a high prediction accuracy, a ranking order close to 1, a large #W, a small #L, and a small SR value.

## 5.2. Experiments on synthetic data streams

We create synthetic data streams using Matlab 7.0 as follows. Firstly, we generate instances x<sub>t</sub> at time stamp t by using a Gaussian distribution $x _ { t } { \sim } N ( \mu _ { t } , \Sigma _ { t } )$ , where μ denotes the distribution center and Σ is the covariance matrix (in our experiments, each instance has two dimensions, with μ starting from [π,π] and $\Sigma _ { t } = \left\lceil { \boldsymbol { \pi } , \boldsymbol { 0 } } \right\rceil$ for each time stamp t). Then we de<sup>fi</sup>ne the potential pattern $p ( y | x )$ at time stamp t as follows,

$$
y _ {t} = \frac {1}{r} \sum_ {i = 1} ^ {r} a _ {t} \sin (x _ {t}) + \frac {1}{r} \sum_ {i = 1} ^ {r} b _ {t} x _ {t} ^ {2} + \varepsilon\tag{14}
$$

where r is the number of dimensions, at and bt are r-dimensional vectors. The <sup>fi</sup>rst two nonlinear terms are used to generate a complex nonlinear classi<sup>fi</sup>cation boundary. To simulate real-world data streams, we generate stream data containing both concept drifting and noise, where ε accounts for noise with a Gaussian distribution $\varepsilon { \sim } N ( 0 , 0 . 3 ^ { 2 } )$ . To simulate the concept drifting, we let p(x,y) change randomly. Since $p ( x , y ) { = } p ( x ) \cdot p ( y | x )$ , changing p(x,y) is equivalent to changing p(x) or p(y|x). To evolve p(x), we let x's distribution center μt vary with time as $\mu _ { t + 1 } = \mu _ { t } + ( - 1 ) ^ { s } d$ , where s denotes the direction (which has 10% of chance to reverse its direction), and d denotes the step length (which is set to be 0.1). To evolve p(y|x), we let b have 50% of chance to become $b _ { t + 1 } = b _ { t } + 1$ . On the other hand, to add noise into the data, we let y have 20% of chance to change its label. For twoclass classi<sup>fi</sup>cation at time stamp t, the decision boundary is set using the rules that, if $\begin{array} { r } { y _ { t } { \ge } \frac { 1 } { r } \sum _ { i } b _ { t } x _ { t } ^ { 2 } } \end{array}$ , the class label $\mathrm { i } s \ ^ { \mathsf { \tiny ~ \ d ~ } } + 1 \mathrm { \ i } ^ { \mathsf { \tiny ~ \ d ~ } } ;$ otherwise the class label $\mathrm { i } s \ifmmode \cdots \else \textqquad- 1 \textdegree$ . For multi-class classi<sup>fi</sup>cation, supposing there are l classes $\{ c _ { 1 } , c _ { 2 } , . . . , c _ { 1 } \}$ , we can assign class labels by equally dividing y into l parts. For better understanding, major notations used to generate our data streams are summarized in Table 1.

Table 2 Binary data stream, p(x,y) evolves with 20% noisy data chunks.  
Table 1  
Major parameters used to generate synthetic data streams.

<table><tr><td>Variable</td><td>Description</td></tr><tr><td> $r$ </td><td>Number of attributes</td></tr><tr><td> $x_{t}$ </td><td>Example generated at time stamp  $t$ </td></tr><tr><td> $y_{t}$ </td><td>Class label of example  $x_{t}$ </td></tr><tr><td> $a_{t}, b_{t}$ </td><td>Coefficient vectors for generating label  $y_{t}$ </td></tr><tr><td> $\varepsilon$ </td><td>Noise</td></tr><tr><td> $\mu_{t}$ </td><td>Distribution center of  $x_{t}$ </td></tr><tr><td> $\Sigma_{t}$ </td><td>Covariant matrix of  $x_{t}$ </td></tr><tr><td> $s$ </td><td>Controls concept drifting direction</td></tr><tr><td> $d$ </td><td>Controls concept drifting step length</td></tr></table>

In Tables 2 and 3, we report the experimental results for binary and multi-class streams, where the <sup>fi</sup>rst row in the table shows the number of chunks (N) and the chunk size (B). From the results in Tables 2 and 3, it is clear that among the <sup>fi</sup>ve stream mining algorithms, AE always has the highest average prediction accuracy, the best ranking, and the least number of losses. When comparing <sup>fi</sup>ve algorithms based on their average accuracies, we can observe that VE follows AE as the second best method, HE and WE have the same accuracy, both of them are listed as the third best methods together, and the single tree is the least accurate method. Accordingly, the order of the average prediction accuracies suggests the ranking of all methods as: $A a c c _ { \mathrm { A E } } { > } A a c c _ { \mathrm { V E } } { > } A a c c _ { \mathrm { W E } } { = } A a c c _ { \mathrm { H E } } { > } A a c c _ { \mathrm { T r e e } } .$ When considering the ranking measures (AR and SR), we <sup>fi</sup>nd that AE is listed at the <sup>fi</sup>rst place, followed by VE, HE and WE, and the single decision tree, respectively. As for the standard deviation of the ranking orders, we <sup>fi</sup>nd that HE and WE have the minimal AR. When comparing AE with HE, we can observe that AE is much more stable than HE. The single tree is ranked at the bottom with the most unstable ranking $( A R _ { \mathrm { A E } } < A R _ { \mathrm { V E } } < A R _ { \mathrm { H E } } = A R _ { \mathrm { W E } } < A R _ { \mathrm { T r e e } } )$ . When considering the measures #W and #L, we <sup>fi</sup>nd that VE always has the most frequent wining chance, while AE follows after VE as the second, HE and WE have the same winning chance, and the single tree has the smallest chance of winning. Based on the above observations, we can conclude that: among the <sup>fi</sup>ve algorithms, AE performs the best, VE performs the second best, HE and WE are considered the third tier with a tie, and the single tree is the least accurate method for stream data.

In summary, the above observations suggest the following conclusions: (1) Using the same base learners, HE and WE appear to perform similarly, and including weight values to each base classi<sup>fi</sup>er does not seem to be very helpful; (2) HE and WE mostly have the least average ranking, and they are consistently ranked inferior to AE and VE, but superior to the single tree; (3) VE always has the best winning chance, whereas AE always has the least chance to lose; and (4) compared to other four methods, the single decision tree is the least accurate method for stream data mining, which has the lowest accuracy, lowest ranking, minimal winning chance and maximum chance to lose.

Intuitively, we suspect that AE should perform the best for all the measures, whereas, in practice, VE appears to have a better chance of winning (#W) than AE. This is because VE is suitable for the dynamic description, which only considers concept drifting but no data errors. In our synthetic data stream, we generate 20% noisy data chunks, whereas the remaining 80% data chunks are clean. Consequently, VE has a much better winning chance. However, even if VE has a better winning chance than AE, VE is still inferior to AE because VE will suffer from the decreasing of the prediction accuracy when building model on noisy chunks (as shown in Table 5, which will be discussed shortly).

<table><tr><td rowspan="2">Measure</td><td colspan="5">N = 100, B = 100</td><td colspan="5">N = 1000, B = 100</td></tr><tr><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td></tr><tr><td>Aacc</td><td>0.572</td><td>0.575</td><td>0.575</td><td>0.596</td><td>0.614</td><td>0.680</td><td>0.679</td><td>0.679</td><td>0.701</td><td>0.704</td></tr><tr><td>AR</td><td>3.192</td><td>2.697</td><td>2.697</td><td>2.505</td><td>2.495</td><td>3.323</td><td>3.010</td><td>3.010</td><td>2.392</td><td>2.194</td></tr><tr><td>SR</td><td>0.033</td><td>0.001</td><td>0.001</td><td>0.023</td><td>0.003</td><td>0.028</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.020</td></tr><tr><td>#W</td><td>9</td><td>14</td><td>14</td><td>45</td><td>33</td><td>8</td><td>9</td><td>9</td><td>54</td><td>35</td></tr><tr><td>#L</td><td>33</td><td>31</td><td>31</td><td>26</td><td>20</td><td>30</td><td>37</td><td>37</td><td>23</td><td>12</td></tr></table>

Table 3  
Multi-class data stream, p(x,y) evolves with 20% noisy data chunks.

<table><tr><td rowspan="2">Measure</td><td colspan="5">N = 100, B = 100</td><td colspan="5">N = 1000, B = 100</td></tr><tr><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td></tr><tr><td>Aacc</td><td>0.401</td><td>0.422</td><td>0.422</td><td>0.476</td><td>0.485</td><td>0.572</td><td>0.616</td><td>0.616</td><td>0.602</td><td>0.646</td></tr><tr><td>AR</td><td>3.768</td><td>2.849</td><td>2.849</td><td>2.081</td><td>2.071</td><td>3.091</td><td>3.030</td><td>3.030</td><td>2.404</td><td>2.394</td></tr><tr><td>SR</td><td>0.006</td><td>0.013</td><td>0.013</td><td>0.012</td><td>0.012</td><td>0.037</td><td>0.000</td><td>0.000</td><td>0.020</td><td>0.002</td></tr><tr><td>#W</td><td>7</td><td>12</td><td>12</td><td>48</td><td>39</td><td>8</td><td>10</td><td>10</td><td>53</td><td>29</td></tr><tr><td>#L</td><td>51</td><td>36</td><td>36</td><td>15</td><td>11</td><td>15</td><td>48</td><td>48</td><td>26</td><td>9</td></tr></table>

To investigate the situations where concept drifting and noise interruption occur simultaneously, we report the accuracies across 100 data chunks in Fig. 7. We can observe that there is always a signi<sup>fi</sup>cant drop in the accuracy once a noisy data chunk emerges. To study the reasons behind, we take two typical data chunks as an example: chunk 6, a normal chunk followed by a noisy chunk 7; and chunk 7, a noisy chunk followed by a normal chunk 8. As shown in Table 4, when using the normal chunk (chunk 6) to predict the noisy chunk (chunk 7), all <sup>fi</sup>ve methods receive poor performance, which explains the “sudden drop” in Fig. 7. In fact, none of the <sup>fi</sup>ve methods are able to predict a noisy chunk with a high accuracy, so there is always a sudden decrease of the accuracy. Table 5 shows the second typical situation that a noisy up-to-date chunk 7 is followed by a normal yet-to-come data chunk 8. We can observe that AE has the best performance. This is because in addition to the current noisy chunk 7, AE still uses other normal chunks in the buffer, i.e., the 5th and 6th chunks to predict the 8th chunk (similar to HE and WE), but VE only depends on the 7th noisy chunk (similar to the single tree), so AE, HE and WE, which have used historical data chunks in the buffer, will perform better than VE and the single tree. In summary, classi<sup>fi</sup>ers built on a single data chunk may suffer signi<sup>fi</sup>cant loss in prediction accuracies for noisy chunks, and this explains why they are not suitable for realistic data streams. On the other hand, classi<sup>fi</sup>ers built on several consecutive data chunks may preserve valuable information, which can help reduce the negative impact of the noisy chunks.

![](/api/attachments/63YTMG5Z/fulltext/images/fae28c3879df3f181237815bfdcdf7a14a27093b221ca82829728933176eadb8.jpg)  
Fig. 7. The two-group synthetic data stream, each chunk has 1000 instances; there are total 100 data chunks

## 5.3. Experiments on KDDCUP'99 data stream

In this subsection, we compare all ensemble methods on the KDDCUP'99 intrusion detection dataset, which is a popularly used test bed for stream data mining [5]. Since many research works have reported that concepts underlying this dataset appear to be linearly separable (the average prediction accuracy is over 97% on 10% sampled instances), we complicate the learning task by using the following four approaches to build different types of data streams: (1) random selection — we randomly select 100 data chunks, each of which contains 1000 instances with an equal class distribution (50% of instances in each class); (2) random noisy selection — we randomly select 20% data chunks from (1), and then arbitrarily assign each instance a class label which does not equal its original class label, and <sup>fi</sup>nally we put these noisy data chunks back into the stream; (3) rearranged selection — given a training set, we <sup>fi</sup>rst <sup>fi</sup>nd the most informative attribute by using the information gain [22] measure (i.e., the 30th attribute), then we sort all instances according to the values on this attribute, and the sorted instances are <sup>fi</sup>nally put into 100 data chunks each of which contains 1000 instances; and (4) rearranged noisy selection — we add 20% noisy data chunks in Eq. (3) in a similar way to the procedure in Eq. (2). Major notations of the parameters of this data set are listed in Table 6.

Table 5 lists the results of a random selection of the KDDCUP'99 dataset. We can observe that AE performs the best in terms of the average prediction accuracy (0.995), AR (average ranking 1.475), #W (73 wins) and #L (11 loses). Taking all evaluation criteria into consideration, VE, with an average accuracy of 0.994, 62 wins and 16 loses is the second best method. HE and WE perform the same, with an average accuracy of 0.993, 34 wins and 39 loses. The single decision tree, with an average performance of 0.991, and 21 wins and 70 loses, is the least preferred method.

Table 7 lists the comparison results on a random selection schema. It validates our hypothesis that under realistic data stream scenarios, the weighted ensemble does not have any difference from the horizontal ensemble, and the order of accuracy is still Aacc NAacc-$_ { \mathrm { A E } } { > } A a c c _ { \mathrm { V E } } { > } A a c c _ { \mathrm { H E } } { = } A a c c _ { \mathrm { W E } } { > } A a c c _ { \mathrm { T r e e } } ,$ . Since random selection selects data chunks from the raw data set without any revisions, we can regard it as a realistic data stream. It is safe to say that AE performs the best on this realistic data stream.

Table 8 reports a random selection with 20% noise and we can observe that AE also performs the best, with the highest average accuracy and ranking, the most winning and least losing chances. The order of accuracy is $A a c c _ { \mathrm { A E } } { > } A a c c _ { \mathrm { H E } } { = } A a c c _ { \mathrm { W E } } { > } A a c c _ { \mathrm { V E } } { > } A a c c _ { \mathrm { T r e e } } .$ We can see that VE and the single tree are more vulnerable to noise. Compared with Table 5, the accuracy of VE and the single tree signi<sup>fi</sup>cantly drops, while AE, HE and WE marginally drops. This tells us that buffering a small number of data chunks can prevent a signi<sup>fi</sup>cant drop of accuracy caused by noise.

Table 4  
Using the 6th normal data chunk to predict the 7th noisy data chunk

<table><tr><td>Alg.</td><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td></tr><tr><td>Acc.</td><td>0.118</td><td>0.123</td><td>0.123</td><td>0.100</td><td>0.070</td></tr></table>

Table 8  
Table 5  
Using the 7th noisy data chunk to predict the 8th normal data chunk.

<table><tr><td>Alg.</td><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td></tr><tr><td>Acc.</td><td>0.158</td><td>0.767</td><td>0.767</td><td>0.071</td><td>0.808</td></tr></table>

Table 9 lists the results of a rearranged method, and we can observe that VE performs the best on all of the <sup>fi</sup>ve measurements. It has the largest average accuracy, the smallest AR, the most winning chance and the least losing chance. The single tree is the second best method. AE is the third best, and HE and WE are listed as the last. The rearrangement procedure, in fact, generates a special data stream according to the dynamic description. So the classi<sup>fi</sup>er ensemble built on the most recent data chunk is better than the classi<sup>fi</sup>er ensemble built with several buffered data chunks. That is why VE and the single tree perform better than others.

Table 10 reports the results of a rearranged noise selection method, with 20% noise in addition to the change of p(x,y). This is the most dif<sup>fi</sup>cult situation. We can observe that all the <sup>fi</sup>ve algorithms suffer a signi<sup>fi</sup>cant drop of accuracy. VE drops the most, from 0.926 to 0.670, the single decision tree drops from 0.911 to 0.669, HE and WE drops from 0.825 to 0.676, and AE drops from 0.879 to 0.682. Among them, AE achieves the best. This is because the rearranged noise selection method generates a data stream that experiences concept drifting and data errors simultaneously, and AE, as we discussed earlier, performs the best under this circumstance.

## 5.4. Experiments on wireless sensor stream

In this subsection, we carry out experiments and comparisons on a real-world wireless sensor data stream, which is publically available (http://www.cse.fau.edu/\~xqzhu/stream.html) and popularly used as the test bed for data stream mining models. The purpose is to address the following two concerns: (1) Whether AE performs better than all its individual learning algorithms, as well as the HE trained using different learning algorithms as the base learners? and (2) How many learning algorithms should be used in AE? To answer the above two questions, we <sup>fi</sup>rst introduce the wireless sensor stream, and then report the algorithm performance in terms of average prediction accuracy and the system runtime.

The wireless sensor stream contains information (temperature, humidity, light, and sensor voltage) collected from 54 sensors deployed in a lab environment. The data are read every 1–3 min from all sensors, and the whole stream contains information recorded over a two month period. The learning task is to correctly identify the sensor ID (1 out of 54 sensors) purely based on the reading of the sensor data and the recording time. It should be noticed that the concept underlying the sensor stream may change with time. For example, the lighting during the working hours is generally stronger than that in the night, and the temperature of speci<sup>fi</sup>c sensors (i.e., sensors in a conference room) may suddenly rise during the meeting time. In addition, the wireless sensor stream may also contain random errors. For example, when communication channels of sensor nodes are blocked by moving objects, or the sensor node's hardware may experience malfunction, the data stream generated from the sensor node may contain erroneous or missing values. In our experiments, for simplicity, the stream is transferred into a binary-class classi<sup>fi</sup>cation problem by splitting the 54 IDs into two classes (i.e., if a sensor's ID is less than 28, then it belongs to class “−1”; otherwise, it belongs to class “+1”). Besides, we split this data stream into data chunks, with each chunk containing 100 examples.

Table 6  
A list of parameters in the KDDCUP'99 data set.

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>Random selection</td><td>We randomly pick 100 data chunks, each data chunk containing 1000 examples with balance class labels</td></tr><tr><td>Random noisy selection</td><td>Based on the random selection, we again randomly choose 20% data chunks and assign wrong class labels to every example in this chunks</td></tr><tr><td>Rearranged selection</td><td>Based on the random selection, we sort all the examples by the 30th attribute, and then the sorted examples are put into 100 data chunks</td></tr><tr><td>Rearranged noisy selection</td><td>Based on the rearranged selection, we randomly choose 20% data chunks as noisy data chunks</td></tr></table>

Table 7  
Random selection results.

<table><tr><td></td><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td></tr><tr><td>Aacc</td><td>0.991</td><td>0.993</td><td>0.993</td><td>0.994</td><td>0.995</td></tr><tr><td>AR</td><td>3.232</td><td>2.192</td><td>2.192</td><td>1.778</td><td>1.475</td></tr><tr><td>SR</td><td>0.015</td><td>0.000</td><td>0.000</td><td>0.006</td><td>0.126</td></tr><tr><td>#W</td><td>21</td><td>34</td><td>34</td><td>62</td><td>73</td></tr><tr><td>#L</td><td>70</td><td>39</td><td>39</td><td>16</td><td>11</td></tr></table>

In Fig. 8(a), we report the experimental comparisons among AE, AE's component algorithms, and HE trained with different learning algorithms. For example, the symbol “HE(SVM)” denotes that HE is trained with SVM. From the results, we can observe that compared to its individual classi<sup>fi</sup>er and HE trained with different learning algorithms, AE has the best prediction accuracy on average. This is because when the data distribution of the yet-to-come test chunk is unknown, we cannot always <sup>fi</sup>nd an “optimal” algorithm with the best prediction accuracies across the stream. As a result, combining different learning algorithms is likely to reduce the average prediction error.

In Fig. 8(b), we report the system training time comparisons across different methods. Not surprisingly, AE is the most time-consuming method among all benchmark approaches, mainly because AE has to train more base classi<sup>fi</sup>ers than its peers. To reduce AE's runtime, a possible solution is to employ multi-core or multi-processor computing systems to train base classi<sup>fi</sup>ers in parallel.

To test AE's performance under different numbers of learning algorithms, we exam AE's performance by using six well-known learning algorithms, including the Decision Tree (Tree), Logistic Regression (LR), SVM, NaïveBayes, K-NN, and Multiple Perceptron, as the base learners. For ease of description, we use symbol “+M” to denote that an extra learning algorithm M is added to AE. For example, “+LR” after “Tree” means that in addition to the Decision Trees, we also add a Logistic Regression model as AE's base learning algorithms. From Fig. 9(a), we can observe that when we use Tree, LR, and SVM as base classi<sup>fi</sup>ers, the prediction accuracy increases continuously. After that, the prediction accuracy <sup>fl</sup>uctuates with the inclusion of additional learning algorithms. For example, adding NaïveBayes and Multiple Perceptron actually reduce AE's performance. Under this observation, we adjust the order of the learning algorithms and report the new results in Fig. 9(b). We can observe that AE's performance is still unstable with different numbers of learning algorithms. In other words, there does not seem have a single “optimal” number of classi<sup>fi</sup>ers for AE. The number of based classi<sup>fi</sup>ers should be used in AE may vary, depending on the data characteristics of the underlying data streams. For example, when the concept drifts marginally, a practical solution is to combine several strong algorithms (such as the LR, SVM, and KNN) together to construct the AE framework.

Random selection with noise.

<table><tr><td></td><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td></tr><tr><td>Aacc</td><td>0.694</td><td>0.822</td><td>0.822</td><td>0.695</td><td>0.823</td></tr><tr><td>AR</td><td>2.929</td><td>2.263</td><td>2.263</td><td>2.182</td><td>2.121</td></tr><tr><td>SR</td><td>0.009</td><td>0.001</td><td>0.001</td><td>0.000</td><td>0.013</td></tr><tr><td>#W</td><td>20</td><td>29</td><td>29</td><td>54</td><td>54</td></tr><tr><td>#L</td><td>45</td><td>35</td><td>35</td><td>29</td><td>26</td></tr></table>

Table 9  
Rearranged selection results.

<table><tr><td></td><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td></tr><tr><td>Aacc</td><td>0.911</td><td>0.825</td><td>0.825</td><td>0.926</td><td>0.879</td></tr><tr><td>AR</td><td>1.525</td><td>2.000</td><td>2.000</td><td>1.475</td><td>2.267</td></tr><tr><td>SR</td><td>0.022</td><td>0.010</td><td>0.010</td><td>0.002</td><td>0.016</td></tr><tr><td>#W</td><td>74</td><td>58</td><td>58</td><td>74</td><td>59</td></tr><tr><td>#L</td><td>17</td><td>35</td><td>35</td><td>8</td><td>26</td></tr></table>

## 6. Conclusions

Data errors pose a great challenge to data mining models. Such a challenge becomes much more severe in dynamic data stream environments where the erroneous data may mix with the concept drifting problem. In order to build accurate prediction models from noisy data streams, existing solutions largely rely on some data preprocessing algorithms to cleanse noise from data streams, such that the cleansed stream data can be used to build accurate prediction models. Nevertheless, all existing stream data preprocessing models share two disadvantages. First, most of them implicitly make some statistical assumptions, through which noisy data can be differentiated from data of drifting concepts. In practice, such statistical assumptions may not hold in many real-world applications. Second, most existing algorithms require multiple scanning to <sup>fi</sup>rst cleanse a noisy data stream and then build models from the cleansed data. Such a multi-scan manner may not be appropriate for fast <sup>fl</sup>owing data streams. Alternatively, in this paper, we proposed a robust aggregate ensemble (AE) learning model to assist the knowledge discovery for noisy data streams. AE <sup>fi</sup>rst trains base classi<sup>fi</sup>ers using different learning algorithms on different data chunks, and then combines all the base classi<sup>fi</sup>ers to form an ensemble classi<sup>fi</sup>er through model averaging. By doing so, AE is capable of handling the concept drifting challenge, as well as tolerating the data errors. Theoretical and empirical studies demonstrated that AE is superior to existing ensemble-based models, such as the horizontal ensemble, the weighted ensemble, and the vertical ensemble models, for noisy data streams.

## Acknowledgements

This research was partially supported by the National Science Foundation of China (NSFC) grants (61003167, 60828005, 70621001, and 70921061), a China 973 Project (2007CB311100), a Chinese Academy of Sciences grant (Overseas Collaboration Group), a US National Science Foundation grant (CCF-0905337), and an Australian ARC grant (DP1093762).

Table 10  
Rearranged selection with noise.

<table><tr><td></td><td>Tree</td><td>HE</td><td>WE</td><td>VE</td><td>AE</td></tr><tr><td>Aacc</td><td>0.669</td><td>0.676</td><td>0.676</td><td>0.670</td><td>0.682</td></tr><tr><td>AR</td><td>2.424</td><td>1.899</td><td>1.8990</td><td>1.838</td><td>1.737</td></tr><tr><td>SR</td><td>0.025</td><td>0.008</td><td>0.0082</td><td>0.047</td><td>0.006</td></tr><tr><td>#W</td><td>54</td><td>54</td><td>54</td><td>62</td><td>65</td></tr><tr><td>#L</td><td>30</td><td>33</td><td>33</td><td>27</td><td>20</td></tr></table>

(a) Average prediction accuracy  
![](/api/attachments/63YTMG5Z/fulltext/images/75f85fa6e6fd88899c957e14e2395febd3dfa89b41a6c6bd8b9dde4da2687898.jpg)

(b) Training time cost  
![](/api/attachments/63YTMG5Z/fulltext/images/fc2804f59552866a1fe5f0d3e2f511289a14f47f6983d7eaac17185b92c3fd3f.jpg)  
Fig. 8. Comparison results with respect to (a) average accuracy, and (b) system runtime. The wireless sensor stream is divided into successive data chunks, with each chunk containing 100 data records. Besides, both HE and AE use the latest three data chunks to build up the ensemble framework.

(a) Learning order A  
![](/api/attachments/63YTMG5Z/fulltext/images/41b7a85b1593098d56f90662b045a371a3a270e96ca73eaf80d0c79413d93f24.jpg)

(b) Learning order B  
![](/api/attachments/63YTMG5Z/fulltext/images/f4744497e5ad7522aad9b7ae84d7520246115084b1c6bbdf6e66100325f10e78.jpg)  
Fig, 9. The results of applving different numbers of learning algorithms to AE on the wireless sensor stream data. The data stream is split into continuous data chunks, with each chunk having 100 data records. AE uses the most recent three data chunks to construct the ensemble framework. It is obvious that the prediction accuracy does not always improve with the number of learning algorithms increase. So <sup>fi</sup>nding the “optimal” number of m in AE is essentially dif<sup>fi</sup>cult, if not impossible. When the concept drifts marginally, a practical solution is to combine several learning algorithms (such as the LR SVM and KNN) to construct AE.

## References

[1] C. Aggarwal, On classi<sup>fi</sup>cation and segmentation of massive audio data streams, Knowledge and Information Systems: An International Journal 20 (2) (2009) 137–156.

[2] C. Aggarwal, J. Han, J. Wang, Y. Philip, A framework for clustering evolving data streams, Proc. of VLDB (2003) 81–92.

[3] D. Aha, D. Kibler, M. Albert, Instance-based learning algorithms, Machine Learning (1991) 37–66.

[4] K. Ali, M. Pazzani, Error reduction through learning multiple descriptions, Machine Learning (1996).

[5] A. Asuncion, D. Newman, UCI Machine Learning Repository, Irvine, CA, 2007.

[6] R. Avnur, J. Hellerstein, Eddies: Continuously Adaptive Query Processing, Proc. of SIGMOD (2000) 261–272.

[7] B. Babcock, S. Babu, M. Datar, R. Motwani, J. Widom, Models and issues in data streams, Proc. of PODS (2002) 1–16.

[8] S. Babu, J. Widom, Continuous queries over data streams, ACM SIGMOD Record 30 (3) (2001) 109–120.

[9] D. Barbara, The New Jersey data reduction report, IEEE Data Engineering Bulletin 20 (4) (1997) 3–45.

[10] C. Brodley, M. Friedl, Identifying Mislabeled Training Data, Journal of Arti<sup>fi</sup>cial Intelligence Research 11 (1999) 131–167.

[11] C. Chang, and C. Lin, LIBSVM Toolbox, Available online: http://www.csie.ntu.edu. tw/\~cjlin/libsvm/.

[12] Y. Chen, L. Tu, Density-based clustering for real-time stream data, Proc. of KDD (2007) 133–142.

[13] Y. Chi, H. Wang, P. Yu, R. Muntz, Moment, Maintaining closed frequent itemsets over a stream sliding window data streams, Proc. of IEEE ICDM (2004) 59–66.

[14] F. Chu, Y. Wang, C. Zaniolo, An Adaptive Learning Approach for Noisy Data Streams, Proc. of IEEE ICDM (2004) 351–354.

[15] T. Dietterich, Ensemble methods in machine learning, Proc. of the <sup>fi</sup>rst Workshop on Multiple Classi<sup>fi</sup>er Systems (2000) 1–15.

[16] P. Domingos, G. Hulten, Mining high-speed data streams, Proc. of KDD (2000) 71–80

[17] W. Fan, Systematic data selection to mine concept-drifting data streams, Proc. of KDD (2004) 128–137.

[18] J. Gao, W. Fan, J. Han, On appropriate assumptions to mine data streams: Analysis and Practice, Proc. of IEEE ICDM (2007) 143–152.

[19] M. Gaber, P. Yu, Detection and Classi<sup>fi</sup>cation of Changes in Evolving Data Streams, International Journal of Information Technology and Decision Making (IJITDM) 5 (4) (2006) 659–670.

[20] S. Guha, A. Meyerson, N. Mishra, R. Motwani, Clustering Data Streams: Theory and Practice, IEEE Transactions on Knowledge and Data Engineering 15 (3) (2003) 515-528.

[21] T. Ho, J. Hull, S. Srihari, Decision combination in multiple classi<sup>fi</sup>er systems, IEEE Transactions on PAMI 16 (1) (1994) 66–75.

[22] P. Hore, L. Hall, D. Goldgof, A Fuzzy C Means Variant For Clustering Evolving Data Streams, Proc. of IEEE International Conference on Systems, Man and Cybernetics (2007) 360–365.

[23] G. Hulten, L. Spencer, P. Domingos, Mining time-changing data streams, Proc. of KDD (2001) 97–106.

[24] J. Kolter, M. Maloof, Using additive expert ensembles to cope with concept drift, Proc. of ICML (2005) 449–456.

[25] S. Laxman, P. Sastry, K. Unnikrishnan, A fast algorithm for <sup>fi</sup>nding frequent episodes in event streams, Proc. of KDD (2007) 410–419.

[26] H. Li, et al., Ef<sup>fi</sup>cient Maintenance and Mining of Frequent Itemsets over Online Data Streams with a Sliding Window, Proc. of IEEE International Conference on Systems, Man and Cybernetics (2006) 2672–2677.

[27] G. Luo, K. Wu, P. Yu, Answering linear optimization queries with an approximate stream index, Knowledge and Information Systems: An International Journal 20 (1) (2009) 95–121.

[28] G. Manku, R. Motwani, Approximate frequency counts over data streams, Proc. of VLDB (2002) 346–357.

[29] M. Mannino, Y. Yang, Y. Ryu, Classi<sup>fi</sup>cation Algorithm Sensitivity to Training Data with Non Representative Attribute Noise, Decision Support Systems 46 (3) (2009) 743–751.

[30] D. Olson, Y. Shi, Introduction to Business Data Mining, McGraw-Hill/Irwin, 2005.

[31] S. Pang, S. Ozawa, N. Kasabov, Incremental Linear Discriminant Analysis for Classi<sup>fi</sup>cation of Data Streams, IEEE Transactions on Systems, Man, and Cybernetics, Part B: Cybernetics 35 (5) (2005) 905–914.

[32] J. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, 1993.

[33] J. Quinlan, The Effect of Noise on Concept Learning, Machine Learning (1986).

[34] M. Scholz, R. Klinkenberg, An ensemble classi<sup>fi</sup>er for drifting concepts, Proc. of ECML/PKDD Workshop on Knowledge Discovery in Data Streams (2005) 53–64.

[35] W. Street, Y. Kim, A streaming ensemble algorithm (SEA) for large-scale classi<sup>fi</sup>cation, Proc. of KDD (2001) 377–382.

[36] K. Su, H. Huang, X. Wu, S. Zhang, A logical Framework for Identifying Quality Knowledge from Different Data Sources, Decision Support Systems 42 (3) (2006) 1673–1683.

[37] N. Syed, H. Liu, K. Sung, Handling concept drifts in incremental learning with support vector machines, Proc. of KDD (1999) 317–321.

[38] H. Wang, W. Fan, P. Yu, J. Han, Mining concept-drifting data streams using ensemble classi<sup>fi</sup>ers, Proc. of KDD (2003) 226–235.

[39] X. Wang, H. Liu, J. Han, Finding Frequent Items in Data Streams Using Hierarchical Information, Proc. of IEEE International Conference on Systems, Man and Cybernetics (2007) 431–436.

[40] Y. Wang, Z. Li, Y. Zhang, Classifying Noisy Data Streams, Fuzzy Systems and Knowledge Discovery (2006) 548–549.

[41] G. Widmer, M. Kubat, Learning in the presence of concept drift and hidden contexts, Machine Learning 23 (1996) 69–101.

[42] I. Witten, E. Frank, Data mining: practical machine learning tools and techniques, Morgan Kaufmann (2005).

[43] Y. Yang, X. Wu, X. Zhu, Combining proactive and reactive predictions of data streams, Proc. of KDD (2005) 710–715.

[44] P. Zhang, X. Zhu, L. Guo, Mining Data Streams with Labeled and Unlabeled Training Examples, Proc. of IEEE ICDM (2009) 627–636.

[45] P. Zhang, X. Zhu, Y. Shi, Categorizing and Mining Concept Drifting Data Streams, Proc. of KDD (2008) 820–821.

[46] P. Zhang, X. Zhu, Y. Shi, X. Wu, An Aggregate Ensemble for Mining Concept Drifting Data, Proc. of PAKDD (2009) 1021–1029.

[47] D. Zhu, A Hybrid Approach for Ef<sup>fi</sup>cient Ensembles, Decision Support Systems 48 (3) (2010) 480–487.

[48] X. Zhu, P. Zhang, X. Lin, Y. Shi, Active Learning from Stream Data Using Optimal Weight Classi<sup>fi</sup>er Ensemble, IEEE Transactions on System, Man, Cybernetics, Part B 40 (4) (2010) 1–15.

[49] X. Zhu, X. Wu, Class Noise vs Attribute Noise: A Quantitative Study, Arti<sup>fi</sup>cial Intelligence Review 22 (3) (2004) 177–210.

[50] X. Zhu, X. Wu, C. Zhang, Cleansing Noisy Data Streams, Proc. of IEEE ICDM (2008) 1139–1144.

Peng Zhang is an Assistant Professor with the Institute of Computing Technology, Chinese Academy of Sciences, Beijing (China). He received his Ph.D. (2009) in computer science from the Graduate University of the Chinese Academy of Sciences, Beijing, China. His research interests include data stream mining, information <sup>fi</sup>ltering, and information security.

Xingquan Zhu is an Associate Professor with the Faculty of Engineering and Information Technology, University of Technology, Sydney (UTS), Sydney, Australia. He has been an Associate Editor of the IEEE Transactions on Knowledge and Data Engineering (TKDE) since 2009.

Yong Shi is the Charles W. and Margre H. Durham Distinguished Professor of Information Technology, College of Information Science and Technology, Peter Kiewit Institute, University of Nebraska, USA. He is also the Executive Deputy Director of the Fictitious Economy and Data Science Research Center, Chinese Academy of Sciences, Beijing, China. He is the Editor-in-Chief of International Journal of Information Technology and Decision Making (SCI), an Area Editor of International Journal of Operations and Quantitative Management, a member of Editorial Board for a number of academic journals, including International Journal of Data Mining and Business Intelligence.

Li Guo is the director of the Information Security Research Center, Institute of Computing Technology, Chinese Academy of Sciences. Her research interests include data stream management and information security.

Xindong Wu is a Yangtze River Scholar in the School of Computer Science and Information Engineering at the Hefei University of Technology (China), and a Professor of Computer Science at the University of Vermont (USA). He is the Editor-in-Chief of Knowledge and Information Systems (KAIS). He was the Editor-in-Chief of the IEEE Transactions on Knowledge and Data Engineering (TKDE, by the IEEE Computer Society) between January 1, 2005 and December 31, 2008.
