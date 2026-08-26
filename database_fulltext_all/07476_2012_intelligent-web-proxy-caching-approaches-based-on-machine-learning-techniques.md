---
otero_id: 7476
otero_key: "SG2E2DVJ"
title: "Intelligent Web proxy caching approaches based on machine learning techniques"
authors: "Waleed Ali; Siti Mariyam Shamsuddin; Abdul Samad Ismail"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent Web proxy caching approaches based on machine learning techniques

Waleed Ali <sup>a,</sup>⁎, Siti Mariyam Shamsuddin <sup>a</sup>, Abdul Samad Ismail <sup>b</sup>

<sup>a</sup> Soft Computing Research Group, Faculty of Computer Science and Information System, Universiti Teknologi Malaysia, 81310 Johor, Malaysia

<sup>b</sup> Department of Communication and Computer Systems, Faculty of Computer Science and Information Systems, Universiti Teknologi Malaysia, 81310 Johor, Malaysia

## a r t i c l e i n f o

Article history: Received 26 May 2011 Received in revised form 12 January 2012 Accepted 29 April 2012 Available online 5 May 2012

Keywords: Web caching Proxy server Cache replacement Classi<sup>fi</sup>cation Support vector machine Decision tree

## a b s t r a c t

In this paper, machine learning techniques are used to enhance the performances of conventional Web proxy caching policies such as Least-Recently-Used (LRU), Greedy-Dual-Size (GDS) and Greedy-Dual-Size-Frequency (GDSF). A support vector machine (SVM) and a decision tree (C4.5) are intelligently incorporated with conventional Web proxy caching techniques to form intelligent caching approaches known as SVM–LRU, SVM–GDSF and C4.5–GDS. The proposed intelligent approaches are evaluated by trace-driven simulation and compared with the most relevant Web proxy caching polices. Experimental results have revealed that the proposed SVM–LRU, SVM–GDSF and C4.5–GDS signi<sup>fi</sup>cantly improve the performances of LRU, GDSF and GDS respectively.

Crown Copyright © 2012 Published by Elsevier B.V. All rights reserved.

## 1. Introduction

Web proxy caching plays a key role in improving Web performance by keeping Web objects that are likely to be visited again in the proxy server close to the user. This Web proxy caching helps in reducing user perceived latency, i.e. delay from the time a request is issued until response is received, reducing network bandwidth utilization, and alleviating loads on the original servers.

Since the space apportioned to a cache is limited, the space must be utilized effectively. Therefore, an intelligent mechanism is required to manage Web cache content ef<sup>fi</sup>ciently. The cache replacement is the core or heart of Web caching. Thus, the design of ef<sup>fi</sup>cient cache replacement algorithms is extremely important and crucial for caching mechanism achievement [7,8,20]. The most common Web caching methods are not ef<sup>fi</sup>cient enough and may suffer from a cache pollution problem, since they consider just one factor and ignore other factors that may have an impact on the ef<sup>fi</sup>ciency of Web proxy caching [11,18,20,29]. Cache pollution means that a cache contains objects that are not frequently visited. This reduces the effective cache size and affects the performance of the Web proxy caching negatively. Many Web proxy caching policies have attempted to combine some factors which can in<sup>fl</sup>uence the performance of Web proxy caching for making decisions about caching. However, this is not an easy task, because one factor in a particular environment may be more important in other environments [8,19]. So far, the dif<sup>fi</sup>culty in determining which ideal Web objects will be re-visited is still a major challenge faced by the existing Web proxy caching techniques. In other words, there is the question of which Web objects should be cached and which Web objects should be replaced to make the best use of available cache space, improve hit rates, reduce network traf<sup>fi</sup>c, and alleviate loads on the original server [3,8,20,22].

In a Web proxy server, Web proxy log <sup>fi</sup>les record the activities of the users and can be considered to contain complete and prior knowledge of future accesses. The availability of Web proxy log <sup>fi</sup>les that can be exploited as training data is the main motivation for utilizing machine learning techniques in adopting intelligent Web caching approaches. The second motivation is that an ef<sup>fi</sup>cient and adaptive scheme is required for the Web environment, which changes and updates rapidly and continuously. The machine learning techniques can adapt to some important changes throughout the training phase.

Recent studies have proposed exploiting machine learning techniques to cope with the above problem [2,11,13,20,29,31]. Most of these studies utilize an arti<sup>fi</sup>cial neural network (ANN) in Web proxy caching, although ANN training may consume considerable amounts of time and require extra computational overheads. More importantly, the integration of intelligent techniques in Web cache replacement is still being researched.

Support vector machine (SVM) and decision tree (C4.5) are two popular supervised learning algorithms that perform classi<sup>fi</sup>cations more accurately and faster than other algorithms [9,17,23,28]. These machine learning algorithms have a wide range of applications such as text classi<sup>fi</sup>cation, Web page classi<sup>fi</sup>cation and bioinformatics applications [9,17,23,28]. Hence, SVM and C4.5 can be utilized to produce promising solutions for Web proxy caching.

This paper combines the most signi<sup>fi</sup>cant factors using common classi<sup>fi</sup>ers for predicting Web objects that can be re-visited later. In this paper, we present new approaches that depend on the capability of SVM and C4.5 to learn from Web proxy logs <sup>fi</sup>les and predict the classes of objects to be re-visited or not. More signi<sup>fi</sup>cantly, the trained SVM and C4.5 classi<sup>fi</sup>ers can be effectively incorporated with traditional Web proxy caching algorithms to present novel intelligent Web proxy caching approaches with good performance in terms of hit ratio and byte hit ratio. The remaining parts of this paper are organized as follows. Material and methods are presented in Section 2. Web proxy caching and the related works, including conventional and intelligent approaches, are discussed in Section 2.1 and Section 2.2. Section 2.3 describes machine learning algorithms, including support vector machine and decision tree. A framework for intelligent Web proxy caching approaches based on machine learning techniques is illustrated in Section 3. Section 4 elucidates implementation and experimental results. Section 5 discusses performance evaluation and discussion. Finally, Section 6 concludes the paper and suggests possible future works in this area.

## 2. Material and methods

## 2.1. Web proxy caching

Web caching is one of the most successful solutions for improving the performance of Web-based systems. In Web caching, the popular Web objects that are likely to be used in the near future are stored on devices closer to the Web user such as client's machine or proxy server. Thus, Web caching has three attractive advantages to Web users. Web caching decreases user perceived latency, reduces network bandwidth usage and reduces load on the origin servers. Typically, a Web cache is located in a browser, proxy server and/or origin server as shown in Fig. 1. The browser cache is located in the client machine. At the origin server, Web pages can be stored in a server-side cache for reducing the redundant computations and the server load.

The proxy cache is found in the proxy server, which is located between the client machines and origin server. It works on the same principle as the browser cache, but on a much larger scale. Unlike the browser cache which deals with only a single user, the proxy server serves hundreds or thousands of users in the same way. As shown in Fig. 1, when a request is received, the proxy server checks its cache. If the object is available, the proxy server sends the object to the client. If the object is not available, or it has expired, the proxy server will request the object from the origin server and send it to the client. The requested object will be stored in the proxy's local cache for future requests.

Web proxy caching is widely utilized by computer network administrators, technology providers, and businesses to reduce both user delays and Internet congestion [18,21,22]. In this study, much emphasis will be placed on Web proxy caching, due to the fact that it is the most common strategy used for caching Web pages.

![](/api/attachments/SG2E2DVJ/fulltext/images/34091e1f63d4b8cb9c957dd3856f1446abf853efde6fb5e4b1c030c40f7d882b.jpg)  
Fig. 1. Web proxy cache.

As Web proxy cache size is limited, a cache replacement policy is needed to handle the cache content. If the cache is full when an object needs to be stored, the replacement policy will determine which object is to be evicted to allow space for the new object. The optimal replacement policy aims to make the best use of available cache space, improve cache hit rates, and reduce loads on the origin server. The cache replacement policy plays an extremely important role in Web proxy caching. Hence, the design of ef<sup>fi</sup>cient cache replacement algorithms is required to achieve highly sophisticated caching mechanism. In general, the Web proxy cache replacement algorithms are also called Web proxy caching algorithms [20]. In fact, there are few important factors (features) of Web objects that can in<sup>fl</sup>uence the Web proxy caching [8,19,26,33]:

a. Recency: time of (since) the last reference to the object.

b. Frequency: number of requests to an object.

c. Size: size of the Web object.

d. Access latency of object.

Most of the proposals in the literature use one or more of these factors into the cache replacement decision. However, combination of these factors to get wise replacement decision is not an easy task since one factor in a particular situation or environment is more important than others in other environments [8,19].

## 2.2. Related works

## 2.2.1. Web proxy caching algorithms

This section reviews conventional proxy caching policies such as Least-Recently-Used (LRU), Least-Frequently-Used (LFU), SIZE, Greedy-Dual-Size (GDS) and Greedy-Dual-Size-Frequency (GDSF). In this paper, we use the terms traditional and conventional proxy caching policies interchangeably to express about the most common Web proxy caching policies. Most Web proxy servers are still based on the conventional caching policies. These conventional policies are suitable in traditional caching like CPU caches and virtual memory systems, but they are not ef<sup>fi</sup>cient in Web caching <sup>fi</sup>eld. This is because they consider just one factor in order to make caching decisions and ignore the other factors that have more impact on the ef<sup>fi</sup>ciency of the Web proxy caching [11,18,20,29]. The simplest and most common cache management approach is the Least-Recently-Used (LRU) algorithm, which removes the least recently accessed objects until there is suf<sup>fi</sup>cient space for the new objects. LRU is easy to implement and pro<sup>fi</sup>cient for uniform size objects such as the memory cache. However, it does not perform well in Web caching since it does not consider the size or the download latency of objects [20]. Least-Frequently-Used (LFU) is another common policy of Web caching that replaces the object with the smallest number of accesses. LFU keeps more popular Web objects and evicts rarely used ones. However, LFU suffers from the cache pollution in objects with the large reference accounts, which are never replaced even if they are not re-accessed again, especially if these objects are large [10,20].

SIZE policy [1] is one of the common Web caching policies that replaces the largest object(s) from a cache when space is needed for a new object. Thus, a cache can be polluted with small objects which will not be accessed again. To alleviate the cache pollution, Cao and Irani [5] suggested Greedy-Dual-Size (GDS) policy as an extension of the SIZE policy. The algorithm integrates several factors and assigns a key value or priority for each Web object stored in the cache. When cache space becomes occupied and new object is required to be stored in cache, the object with the lowest key value is removed. When user requests an object $^ { g , }$ GDS algorithm assigns key value $K ( g )$ of object g as shown in Eq. (1).

$$
K (g) = L + \frac {C (g)}{S (g)}\tag{1}
$$

where $C ( g )$ is the cost of fetching object g from the server into the cache; S(g) is the size of object g; and L is an aging factor. L starts at 0 and is updated to the key value of the last replaced object. The key value $K ( g )$ of object g is updated using the new L value since the object g is accessed again. Thus, larger key values are assigned to objects that have been visited recently. If the cost is set to 1, it becomes GDS (1), and when the cost is set to $\mathrm { P } { = } 2 + \mathrm { s i z e } / 5 3 6 ,$ it becomes GDS(P).

Cao and Irani (1997) [5] proved that the GDS algorithm achieved better performance compared with some traditional caching algorithms. However, the GDS algorithm ignores the frequency of the Web object. Cherkasova(1998) [10] enhanced the GDS algorithm by integrating the frequency factor into the key value $K ( g )$ as shown in Eq. (2). The policy is called Greedy-Dual-Size-Frequency (GDSF).

$$
K (g) = L + F (g) * \frac {C (g)}{S (g)}\tag{2}
$$

where $F ( g )$ is the frequency of the visits of object g. Initially, when g is requested by user, $F ( g )$ is initialized to 1. If g is in the cache, its frequency is increased by one. Similar to GDS, we then have GDSF(1) and GDSF(P). Table 1 depicts well-known replacement policies [13,20].

As can be observed from Table 1, the traditional Web caching methods consider just one factor or combine few factors using mathematical equation for predicting revisiting of the Web objects in the future. Since Web environment changes and updates rapidly and continuously, the traditional Web caching methods are not ef<sup>fi</sup>cient enough. Many Web cache replacement policies have been proposed for improving performance of Web caching. However, it is challenging to have an omnipotent policy that performs well in all environments or for all time due to the dif<sup>fi</sup>cult combination of factors that can in<sup>fl</sup>uence performance of the Web proxy caching [8,19]. Hence, there is a need for an effective and adaptive approach, which can incorporate these factors into Web caching decision effectively. This is a motivation in adopting intelligent techniques in solving Web caching problems.

In this paper, intelligent Web proxy caching approaches are suggested for making cache replacement decisions. The conventional Web proxy caching approaches are extended using machine learning to enable the algorithms to adapt intelligently over time. The most signi<sup>fi</sup>cant factors, such as recency, frequency, size, access latency and type of object, are combined using intelligent classi<sup>fi</sup>er to predict whether Web objects will be requested again in the future. Then, this information is effectively incorporated with the traditional Web proxy caching algorithms to present novel intelligent Web proxy caching approaches with good performance in terms of hit ratio and byte hit ratio.

## 2.2.2. Intelligent Web proxy caching algorithms

Although there are many studies of Web caching, research using learning machine techniques in Web caching is still new. Recent studies have shown that the intelligent approaches are more ef<sup>fi</sup>cient and adaptive to Web caching environments compared to other approaches. More details about intelligent Web caching approaches are given in [4].

In our previous work ICWCS [2], client-side cache has been divided into two caches namely short-term cache and long-term cache. The Web objects requested in the <sup>fi</sup>rst time have been stored in short-term cache, while the Web objects visited more than once have been moved to long-term cache. LRU algorithm was used as short-term cache was full. More signi<sup>fi</sup>cantly, when the long-term cache was saturated, the neuro-fuzzy system (ANFIS) has been employed to predict Web objects that can be re-accessed later. Then, the unwanted objects are removed <sup>fi</sup>rst from the long-term cache. ANFIS has been used to combine the timestamp, frequency, delay time and size for predicting revisiting of the Web objects. However, ICWCS has not been taken into consideration the cost and size of the predicted objects in the cache replacement process. Hence, the performance in terms of byte hit ratio was not good enough although ICWCS achieved high hit ratio. Moreover, the training process required a long time and extra computational overheads.

In NNPCR [11] and NNPCR-2 [29], back-propagation neural network (BPNN) has been used for making cache replacement decision. An object is selected for replacement based on the rating returned by BPNN. However, the performance of BPNN in NNPCR or NNPCR-2 was in<sup>fl</sup>uenced by the optimal selection of the network topology and its parameters that are based on trial and error; besides that, BPNN learning process can be time consuming. Moreover, employment of BPNN classi<sup>fi</sup>er in cache replacement decision was not effective enough since it did not take into account the cost and size in replacement decision.

An integrated solution of BPNN as caching decision policy and LRU technique as replacement policy for script data object has been proposed by Farhan (2007) [13]. However, the most important factor in Web caching, i.e., recency, was ignored in caching decision. Sulaiman et al. (2008) [31] enhanced Farhan's approach using particle swarm optimization (PSO) for improving neural network performance. However, the enhanced classi<sup>fi</sup>er was not incorporated in Web caching decision. Multilayer perceptron network (MLP) classi<sup>fi</sup>er was used in Web caching by Koskela et al. (2003) [20]. Koskela et al. (2003) predicted the class of Web object depending on syntactic features from HTML structure of the document and the HTTP responses of the server as inputs of MLP. Then, the class value was integrated with LRU, so called LRU-C, to optimize the Web cache. However, this method ignored the frequency factor in Web cache replacement decision. On the other hand, it hinged on some factors that do not affect the performance of Web caching.

Table 1  
The conventional replacement policies.

<table><tr><td>Policy</td><td>Brief description</td><td>Advantages</td><td>Disadvantages</td></tr><tr><td>LRU</td><td>The least recently used objects are removed first.</td><td>Simple and efficient with uniform size objects, such as the memory cache.</td><td>Ignores download latency and the size of Web objects.</td></tr><tr><td>LFU</td><td>The least frequently used objects are removed first.</td><td>Simplicity</td><td>Ignores download latency and size of objects and may store obsolete Web objects indefinitely.</td></tr><tr><td>SIZE</td><td>Big objects are removed first.</td><td>Prefers keeping small Web objects in the cache, causing high cachet hit ratio.</td><td>■ Stores small Web objects even if these objects are never accessed again.■ Low byte hit ratio.</td></tr><tr><td>GDS</td><td>It assigns a key value to each object in the cache as Eq. (1). Consequently, the object with the lowest key value is replaced when cache space becomes occupied.</td><td>■ Overcomes the weakness of SIZE policy by removing objects which are no longer requested by users.■ High hit ratio.</td><td>■ Does not take into account the previous frequency of Web objects.■ Low byte hit ratio.</td></tr><tr><td>GDSF</td><td>It extends GDS algorithm by integrating the frequency factor into the key value K(p) as shown in Eq. (2).</td><td>■ Overcomes the drawback of GD-size.■ High hit ratio</td><td>■ Does not take into account the predicted accesses in the future.■ Low byte hit ratio.</td></tr></table>

Foong et al. (1999) [14] proposed a logistic regression model (LR) to predict the future request. Then, the objects with the lowest re-access probability value were replaced <sup>fi</sup>rst regardless of cost and size of the predicted object. Recently, Sajeev and Sebastian (2011) [30] have utilized a multinomial logistic regression (MLR) to classify Web objects into multilevel classes. Then, MLR classi<sup>fi</sup>er has been combined with LRU to form a new algorithm called LRU-M. In LRU-M, division of cache into classes-based segments makes storing and organization of the Web objects are more complicated, especially with large objects. Table 2 summarizes the existing intelligent Web caching techniques and their limitations.

From the previous studies, we can observe two dominant approaches. An intelligent technique can be employed in Web caching individually or integrated with LRU algorithm. Both approaches may predict Web objects that can be re-accessed later. However, they do not take into consideration the cost and size of the predicted objects in the cache replacement process. Secondly; some important features of the object are ignored in the above mentioned approaches. Lastly, the training process requires a long time and extra computational overheads.

This study utilizes two common classi<sup>fi</sup>ers to combine the most signi<sup>fi</sup>cant factors, such as recency, frequency, size, access latency and type of object, for predicting Web objects that can be re-visited later. Moreover, we present new intelligent Web proxy caching approaches, which depend on the capability of SVM and C4.5 to learn from Web proxy logs <sup>fi</sup>les and predict the classes of objects to be re-visited or not. The proposed approaches are entirely different from the existing intelligent Web caching works. In our proposed approaches, the trained classi<sup>fi</sup>ers are integrated effectively with conventional Web proxy caching to provide more effective proxy caching policies.

## 2.3. Machine learning

Like human learning from experiences, machine learning techniques enable computers to learn from previous examples. Learning capability of the machine learning techniques can improve the performance of an intelligent system over time. In general, the machine learning algorithm takes the past examples as inputs, analyzes them, and outputs abstract patterns or rules. Thus, the machine learning mechanisms form the basis for adaptive systems.

## 2.3.1. Support vector machine

The support vector machine (SVM) is one of the most robust and accurate methods in all well-known machine learning algorithms. SVM has been used successfully in a wide range of applications such as text classi<sup>fi</sup>cation, Web page classi<sup>fi</sup>cation and bioinformatics applications [23,28].

SVM was invented by Vapnik (1995) [34]. The primary idea of SVM is to use a high dimension space to <sup>fi</sup>nd a liner boundary or hyperplane to do binary division (classi<sup>fi</sup>cation) with two classes, positive and negative samples. The SVM attempts to place hyperplane (solid line in Fig. 2) between the two different classes, and orient it in such a way that the margin (dotted lines in Fig. 2) is maximized. The hyperplane is oriented such that the distance between the hyperplane and the nearest data point in each class is maximal. The nearest data points are used to de<sup>fi</sup>ne the margins and are known as support vectors (SVs) (gray circle and square in Fig. 2). The hyperplane can be expressed as in Eq. (3)

$$
(w. x) + b = 0, w \in R ^ {N}, b \in R\tag{3}
$$

where the vector w de<sup>fi</sup>nes the boundary, x is the input vector of dimension N and b is a scalar threshold. At the margins, where the SVs are located, Eqs. (4) and (5) for positive class and negative class, respectively, are as follows:

$$
(w. x) + b = 1\tag{4}
$$

$$
(w. x) + b = - 1\tag{5}
$$

The intelligent Web caching approaches.

<table><tr><td>Approach name</td><td>Brief description</td><td>Features of training dataset</td><td>Limitations</td></tr><tr><td>ICWCS [10]</td><td>Neuro-fuzzy system (ANFIS) has been employed with LRU algorithm in cache replacement decision.</td><td>Timestamp, frequency, delay time and size.</td><td>■ The training process requires long time and extra computational.■ BHR is not good enough.■ Implemented just in client.</td></tr><tr><td>NNPCR [6] and NNPCR-2 [4]</td><td>BPNN has been used for making cache replacement decision. An object is selected for replacement based on the rating returned by BPNN.</td><td>Recency, frequency and size</td><td>■ It was not effective enough since it did not take into account the cost and size in replacement.■ BPNN training may consume long time and require extra computational overhead.</td></tr><tr><td>Intelligent Web caching architecture [11]</td><td>The author proposed an integrated solution of BPNN as caching decision policy and LRU technique as replacement policy for script data object.</td><td>Bandwidth, script size, number of hits, CPU usage and response time</td><td>■ It ignored recency factor.■ It is similar to SIZE-policies that suffer from cache pollution.■ Limited to VB.Net script</td></tr><tr><td>Intelligent Web caching using neurocomputing and particle swarm optimization algorithm [12]</td><td>The authors enhanced Farhan&#x27;s approach (2007) using PSO for improving neural network performance.</td><td>Time, script size, numbers of hits</td><td>■ In training phase, preparation of training datasets is not clear.■ The classifier is not incorporated in Web caching decision.</td></tr><tr><td>Web cache optimization with nonlinear model using object feature [1]</td><td>Multilayer perceptron network (MLP) classifier was used to predict the class of Web objects. Then, the class value was integrated with LRU, so called LRU-C, to optimize the Web cache.</td><td>Syntactic features from HTML structure of the document and the HTTP responses of the server.</td><td>■ Frequency factor is ignored in Web cache replacement decision.■ It hinged on some factors that do not affect on Web caching.■ ANN training may consume long time and require extra computational overhead.</td></tr><tr><td>Logistic regression in an adaptive Web cache [24]</td><td>The author proposed a logistic regression model (LR) to predict the future request.</td><td>Time since last access, frequency within a backward-looking window, size and type.</td><td>The objects with the lowest re-access probability value are replaced first regardless of cost and size of the predicted object</td></tr><tr><td>A novel content classification scheme for Web caches [25]</td><td>The author utilized a multinomial logistic regression (MLR) to classify Web objects into multilevel classes. Then, MLR classifier was combined with LRU to form a new algorithm called LRU-M.</td><td>Popularity, recency, size, popularity consistency, delay and type of object.</td><td>Division of cache into classes-based segments makes storing and organization of the Web objects are more complicated, especially with large objects.</td></tr></table>

![](/api/attachments/SG2E2DVJ/fulltext/images/aa0e87d4e8644fa2b286f5c6b1a0411c6a22a94422a4b4046851accb2a6fe053.jpg)  
Fig. 2. Classi<sup>fi</sup>cation of data by SVM.

SVs correspond to the extremities of the data for a given class. Therefore, to classify any data point in either positive or negative class, the following decision Eq. (6) can be used:

$$
f (x) = \operatorname{sign} ((w. x) + b)\tag{6}
$$

The optimal hyperplane can be obtained as a solution to the following optimization problem.

Minimize

$$
t (w) = \frac {1}{2} \| w \| ^ {2}\tag{7}
$$

Subject to

$$
y _ {i} ((w. x _ {i}) + b) \geq 1, i = 1,..., l\tag{8}
$$

where l is the number of training sets. The solution of the constrained optimization problem can be obtained using Eq. (9).

$$
w = \sum v _ {i} x _ {i}\tag{9}
$$

where x are SVs obtained from training. Putting Eq. (9) in Eq. (6), the decision function is obtained in Eq. (10).

$$
f (x) = \operatorname{sign} \left(\sum_ {i = 1} ^ {l} v _ {i} \left(x. x _ {i}\right) + b\right)\tag{10}
$$

However, for many real-life problems, it is not easy to <sup>fi</sup>nd a hyperplane to classify the data such as nonlinearly separable data. The nonlinearly separable data is classi<sup>fi</sup>ed with the same principle of the linear case. However, the input data is only transformed from the original space into much higher dimensional space called the feature space. Then, a hyperplane can separate positive and negative examples in feature space as shown in Fig. 3. Thus, the decision function becomes as in Eq. (11).

$$
f (x) = \operatorname{sign} \left(\sum_ {i = 1} ^ {l} v _ {i} (\emptyset (x). \emptyset (x _ {i})) + b\right)\tag{11}
$$

The transformation from input space to feature space is relatively computation-intensive. Therefore, a kernel function can be used to perform this transformation and the dot product in a single step. This helps in reducing the computational load and at the same time retaining the effect of higher-dimensional transformation. The kernel function $K ( x _ { i } . x _ { j } )$ is de<sup>fi</sup>ned as Eq. (12).

![](/api/attachments/SG2E2DVJ/fulltext/images/6015c7530a683f7ed5c0216148133299268ef60d20ec8e85b64c7d10ddf4bd5c.jpg)  
Fig. 3. Transformation from input space to feature space.

$$
K \left(x _ {i}. x _ {j}\right) = \emptyset (x _ {i}). \emptyset \left(x _ {j}\right)\tag{12}
$$

After substituting Eq. (12) in the decision function (11), the basic form of SVM is accordingly obtained as Eq. (13).

$$
f (x) = \operatorname{sign} \left(\sum_ {i = 1} ^ {l} v _ {i} K \left(x. x _ {i}\right) + b\right)\tag{13}
$$

The parameters $\nu _ { i }$ are used as weighting factors to determine which of the input vectors are actually support vectors. Several kernel functions like polynomial, sigmoid and RBF can be used in SVM to solve different problems. In this study, RBF kernel given in Eq. (14) is used as kernel function in SVM training. The parameter γ represents the width of the RBF. In case there is an overlap between the classes with non-separable data, the range of parameters $\nu _ { i }$ can be limited to reduce the effect of outliers on the boundary de<sup>fi</sup>ned by SVs. For non-separable cases, the constraint becomes $( 0 < \nu _ { i } < C )$ For separable cases, C is in<sup>fi</sup>nity while for non-separable cases, it may be varied, depending on the number of allowable errors in the trained solution: high C permits few errors while low C allows a higher proportion of errors in the solution.

$$
k \left(x _ {i}, x _ {j}\right) = \exp \left(- \gamma \left\| x _ {i} - x _ {j} \right\| ^ {2}\right), \gamma > 0\tag{14}
$$

2.3.2. Decision tree

The decision tree is one of the most widely used techniques for classi<sup>fi</sup>cation in many applications such as <sup>fi</sup>nance, marketing, engineering and medicine [23,28]. It has several advantages. It is simple to understand and interpret. It is also able to handle nominal and categorical data and perform well with large dataset in a short time [17].

The most well-know algorithm in the literature for building decision trees is the C4.5 decision tree algorithm, which was proposed by Quinlan (1993) [27]. In general, the C4.5 works as follows. The tree begins with a root node that represents the entire given dataset and it recursively splits the data into smaller subsets by testing for a given attribute at each node. The sub-trees denote the partitions of the original dataset that satisfy speci<sup>fi</sup>ed attribute value tests. This process typically continues until the subsets are pure. That means all instances in the subset fall into the same class, at which time the tree growing is terminated.

In the process of constructing the decision tree, the root node is <sup>fi</sup>rst selected by evaluating each attribute on the basis of an impurity function to determine how well it alone classi<sup>fi</sup>es the training examples. The best attribute is selected and used to test at the root node of the tree. A descendant of the root node is created for each possible value of this selected attribute, and the training examples are sorted to the appropriate descendant node. The process is then repeated using the training examples associated with each descendant node to select the best attribute to test at that point in the tree.

In decision tree learning, the most popular impurity functions used for attributes selection are information gain and information gain ratio. Eq. (15) computes the information gain, Gain(S, A), of an attribute A, relative to a collection of examples S.

$$
G a i n (S, A) = E n t r o p y (S) - \sum_ {v \in V a l u e (A)} \frac {| S _ {v} |}{| S |} E n t r o p y (S _ {v})\tag{15}
$$

where Value(A) is the set of all possible values for attribute A, and $S _ { v }$ is the subset of S for which attribute A has value v. Entropy(S) is de<sup>fi</sup>ned as Eq. (16):

$$
\text { Entropy } (S) = - \sum_ {t = 1} ^ {c} p _ {i} \log_ {2} p _ {i}\tag{16}
$$

where c denotes the number of all possible values for attribute A. The second metric commonly used for attribute selection is called gain ratio as shown in Eq. (17).

$$
\text { Gain   ratio } (S, A) = \frac {\text { Gain } (S , A)}{\text { Split   information } (S , A)}\tag{17}
$$

where Split information is de<sup>fi</sup>ned as Eq. (18).

$$
\text { Split   information } (S, A) = \sum_ {t = 1} ^ {c} \frac {| S _ {i} |}{| S |} \log_ {2} \frac {| S _ {i} |}{| S |}\tag{18}
$$

In C4.5 algorithm, the gain ratio is employed in attribute selection for better performance achievement [27]. Fig. 4 demonstrates an example of the decision tree constructed depending on the proxy dataset. After training of the decision tree, a test pattern of any Web object is classi<sup>fi</sup>ed depending on traversing the tree top-down according to the attribute values of the given test pattern until reaching a leaf node. The leaf node represents the predicted class either objects will be re-visited or not. In addition, probabilities of classes can be obtained by computing the relative frequency of each class in a leaf. At the end of each leaf, the numbers in parentheses tell us the number of examples in this leaf. If one or more leaves were not pure, i.e., not all of the same class, the number of misclassi<sup>fi</sup>ed examples would also be given after a slash.

## 3. The proposed intelligent Web proxy caching approaches

In this section, we will present a framework for intelligent Web proxy caching approaches based on machine learning techniques (see Fig. 5). The framework consists of two functional components: an online and of<sup>fl</sup>ine component. The terms online and of<sup>fl</sup>ine refer to interactive communications between the users and proxy server. In the online component, when the user requests Web page, the user communicates with proxy directly for retrieving that page from proxy cache or from server as shown in Fig. 5. The intelligent caching approaches are executed in the online component. On the other hand, the of<sup>fl</sup>ine component does not deal with user directly. It is just responsible for training the machine learning when proxy server is not busy. Then, the trained classi<sup>fi</sup>ers will be used in online component.

## 3.1. Offline component

The of<sup>fl</sup>ine component is responsible for training machine learning techniques. In real environment, the training should be achieved only in off-peak periods of proxy server to ensure the proposed approaches will be more adaptive with Web environment that changes rapidly and continuously. The off-peak-periods of proxy server are the periods when the proxy is not busy; for example, the last hour of the night.

The training datasets in NNPCR [11] were collected during a few hours, 2 h for training and then 2 h for testing. Similarly, in our previous work ICWCS [2], 4 h has been used in a training phase but with random division into training data (70%) and testing data (30%). However, training and testing should be for longer periods to ensure a better performance [29]. Romano and El Aarag (2011) in NNPCR-2 [29] recommended a day as enough time for training. Therefore, in this paper, the proxy logs <sup>fi</sup>le during one day was used for training the intelligent classi<sup>fi</sup>ers. Then, each proxy dataset was then divided randomly into training data (70%) and testing data (30%).

In order to prepare the training dataset, the desired features of Web objects are extracted from trace and logs proxy <sup>fi</sup>les. The important features of Web objects that indicate the user interest are extracted for preparing the training dataset. These features consist of URL ID, timestamp, elapsed time, size and type of Web object. Subsequently, these features are converted to the input/output dataset or training patterns in the format $< x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } , x _ { 5 } , x _ { 6 } , y > . \ x _ { 1 } , . . . , x _ { 6 }$ represent the inputs and y represents target output of the requested object. Table 3 shows the inputs and their meanings for each training pattern. x and x are extracted based on sliding window as suggested by [12]. The sliding window of a request is the time before and after when the request was made. In other words, the sliding window should be around the mean time that an object generally stays in a cache. In a similar way to $[ 1 4 ] , x _ { 6 }$ is classi<sup>fi</sup>ed into <sup>fi</sup>ve categories: HTML with value 1, image with value 2, audio with value 3, video with value 4, application with value 5 and others with value 0. The value of y will be assigned to 1 if the object is re-requested again within the forward-looking sliding window. Otherwise, the target output will be assigned to 0.

![](/api/attachments/SG2E2DVJ/fulltext/images/75df429782ad2de2917ef6f0d8164edad0c90109fbfe7b912d576cfb79e73601.jpg)  
Fig. 4. An example of building decision tree for Web proxy dataset

![](/api/attachments/SG2E2DVJ/fulltext/images/f3b47f3aaa9443c7fdfb8939e1d84927ffc49b767ebb8543cec421aece9e6257.jpg)  
Fig. 5. A framework for intelligent Web proxy caching approaches based on machine learning techniques.

Once the dataset is prepared, the machine learning techniques are trained depending on the <sup>fi</sup>nalized dataset to classify the Web objects into objects that will be re-visited or not.

In SVM training, several kernel functions like polynomial, sigmoid and RBF can be used. However, in this study, RBF kernel has been used, since it can achieve a better performance compared to other kernel functions [16]. Depending on recommendations of Hsu et al. (2009) [16], SVM is trained as follows: prepare and normalize the dataset, consider the RBF kernel, use cross-validation to <sup>fi</sup>nd the best parameters C (margin softness) and γ (RBF width), use the best parameters to train the whole training dataset, and test.

In decision tree training, we used the J48 decision tree based on the C4.5 algorithm suggested in [27]. It is constructed in a top-down recursive manner. Initially, all the training patterns are at the root. Then, the training patterns are partitioned recursively based on attributes selected on the basis of an impurity function (information gain). Partitioning continues until all the patterns for a given node belong to the same class. After training, a test instance of any Web object is classi<sup>fi</sup>ed depending on traversing the tree top-down according to the attribute values of the given test instance until reaching a leaf node. The leaf node represents the predicted class whether an object will be revisited or not.

The inputs and their meanings.

<table><tr><td>Input</td><td>Meaning</td></tr><tr><td> $x_{1}$ </td><td>Recency of Web object based on sliding window</td></tr><tr><td> $x_{2}$ </td><td>Frequency of Web object</td></tr><tr><td> $x_{3}$ </td><td>Frequency of Web object based sliding window</td></tr><tr><td> $x_{4}$ </td><td>Retrieval time of Web object</td></tr><tr><td> $x_{5}$ </td><td>Size of Web object</td></tr><tr><td> $x_{6}$ </td><td>Type of Web object</td></tr></table>

## 3.2. Online component

In the online component, the intelligent caching strategies are achieved for managing the proxy cache content. When the cache buffer is full and a new Web object is fetched from the server, the proposed intelligent caching approaches are used to identify unwanted Web objects for replacement. In this section, we present intelligent Web proxy caching approaches which depend on integrating intelligent techniques with traditional Web caching algorithms to provide more effective caching policies. Three intelligent Web proxy caching approaches are proposed, and are known as SVM–GDSF, C4.5–GDS and SVM–LRU.

## 3.2.1. SVM–GDSF

One advantage of the GDSF policy is that it performs well in terms of the hit ratio. However, the byte hit ratio of GDSF policy is too low. Therefore, the SVM classi<sup>fi</sup>er is integrated with GDSF for improving the performance in terms of the byte hit ratio of GDSF. The proposed intelligent proxy caching approach is called SVM–GDSF.

In SVM–GDSF, a trained SVM classi<sup>fi</sup>er is used to predict the classes of Web objects either objects may be re-visited later or not. After this, the classi<sup>fi</sup>cation decision is integrated into cache replacement policy (GDSF) to give a key value for each object in the cache buffer, as in Eq. (19). Consequently, the objects with the lowest values are removed <sup>fi</sup>rst.

$$
K (g) = L + F (g) * \frac {C (g)}{S (g)} + W (g)\tag{19}
$$

where $W ( g )$ represents the value of predicted class of object g, based on SVM classi<sup>fi</sup>er. $W ( g )$ will be assigned to 1 if object g is classi<sup>fi</sup>ed by SVM as an object to be re-visited, otherwise W(g)will be assigned to 0. This means that the key value of object g is determined not just by its past occurrence frequency, but also by the class predicted depending on the six factors mentioned in Section 3.1.

The rationale behind the proposed SVM–GDSF approach is that we can enhance the priority of those cached objects that may be revisited in the near future, according to the SVM classi<sup>fi</sup>er, even if they are large or not accessed frequently enough. Fig. 6 explains the algorithm of the SVM–GDSF.

## 3.2.2. C4.5–GDS

As mentioned in Subsection 2.2.1, Cherkasova (1998) [10] introduced GDSF as an enhancement of the GDS algorithm by integrating the frequency factor into the key value K(g). Although the frequency is an important indicator for predicting the revisiting of Web objects in the future, several other factors can also contribute in predicting the revisiting of object in the future. Therefore, the frequency is replaced by probability of revisiting of object in the future as proposed enhancement of GDS algorithm. Hence, the proposed policy is called C4.5–GDS. In the proposed C4.5–GDS, GDS is enhanced by incorporating the accumulative scores or probabilities W(g) that object g will be revisited in the future depending on C4.5 classi<sup>fi</sup>er as shown in Eq. (20).

$$
K (g) = L + W (g) * \frac {C (g)}{S (g)}\tag{20}
$$

The idea behind the C4.5–GDS approach is as follows. Instead of object frequency, the probabilities or membership scores of belonging to a class of objects that may be revisited are accumulated and incorporated into caching priority. The object with more scores has higher priority in caching. Hence, the scores predicted by C4.5 can contribute effectively to improving caching priority, compared with the priority with just the frequency factor. The proposed C4.5–GDS algorithm is illustrated in Fig. 7. In this study, both SVM–GDSF and C4.5–GDS are proposed for improving the performance of GDSF(1) and GDS(1) since they are widely used in a real and simulation environment. Thus, the cost C(g) is set to 1 for all polices: GDS, GDSF, SVM–GDSF and C4.5–GDS.

## 3.2.3. SVM–LRU

LRU policy is the most common proxy caching policy among all the Web proxy caching algorithms [11,18,21,29]. However, LRU policy suffers from cold cache pollution, which means that unpopular objects will remain in the cache for a long time. In other words, in LRU, a new object is inserted at the top of the cache stack. If the object is not requested again, it will take some time to be moved down to the bottom of the stack before removing it from the cache.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Begin
Initialize L=0;
For each web object g requested by user
    Begin
    If g in cache
    Begin
    Cache hit occurs
    Update information of g
    // update priority of g based on SVM
    W(g) = apply_SVM( common features)
    K(g) = L + F(g) * $\frac{C(g)}{S(g)}$ + W(g)
    End
    Else
    Begin
    Cache miss occurs
    While no enough space in cache buffer for g
    Begin
    L = min(K(q)), for each q in cache
    Evict q such that K(q)=L
    End
    Fetch g into cache from origin server.
    End
End
</div>

Fig. 6. The intelligent proxy cache SVM–GDSF algorithm.

![](/api/attachments/SG2E2DVJ/fulltext/images/08389e2195df2b4f81403a89910b246138a73b2fedd7a07f11fb99b88acc9e35.jpg)  
Fig. 7. The intelligent proxy cache C4.5–GDS algorithm

For reducing cache pollution in LRU, a SVM classi<sup>fi</sup>er is combined with LRU to form a new algorithm called SVM–LRU. The proposed SVM–LRU works as follows. When the Web object g is requested by the user, SVM predicts whether the class of that object will be revisited again or not. If the object g is classi<sup>fi</sup>ed by SVM as an object to be re-visited again, the object g will be placed at the top of the cache stack. Otherwise, the object g will be placed in the middle of the cache stack. Hence, SVM–LRU can ef<sup>fi</sup>ciently remove the unwanted objects at an early stage to make space for the new Web objects. By using this mechanism, cache pollution can be reduced and the available cache space can be utilized more effectively. The algorithm for SVM– LRU is illustrated in Fig. 8.

## 4. Implementation and experimental results

## 4.1. Raw data collection

We obtained data for the proxy logs <sup>fi</sup>les and traces of the Web objects requested in several proxy servers located around the United States of the IRCache network for <sup>fi</sup>fteen days [25]. Five proxy datasets were collected between 21st August and 4th September, 2010 except SD proxy dataset that were collected between 21st and 28th August, 2010. In this study, the proxy logs <sup>fi</sup>les of 21st August, 2010 were used in the training phase, while the proxy logs <sup>fi</sup>les of the following days were used in the simulation and implementation phase to validate and evaluate the proposed approaches against existing works (see Table 4). An access proxy log entry usually consists of the following ten <sup>fi</sup>elds: timestamp, elapsed time, client address, log tag and HTTP code, size, request method, URL, user identi<sup>fi</sup>cation, hierarchy data and hostname, and content type.

![](/api/attachments/SG2E2DVJ/fulltext/images/654fe2033d8968325533ff1a2b3b4b08980aecfbe9a6452fba8cdcdf7e64aed4.jpg)  
Fig. 8. The intelligent proxy cache SVM–LRU algorithm.

## 4.2. Data pre-processing

In Web proxy caching, the proxy logs <sup>fi</sup>les must be undergone some pre-processing before simulation works. In the data preprocessing, irrelevant and not valid requests are removed from the logs proxy <sup>fi</sup>les. The data pre-processing is carried out as follows:

• Parsing: this involves identifying the boundaries between successive records in logs <sup>fi</sup>le as well as the distinct <sup>fi</sup>elds within each record.

• Filtering: this includes elimination of irrelevant entries such as the un-cacheable requests (i.e., queries with a question mark in the URLs and cgi-bin requests) and entries with unsuccessful HTTP status codes. We only consider successful entries with 200 status codes.

• Finalizing: this involves removing unnecessary <sup>fi</sup>elds. Moreover, each unique URL is converted to a unique integer identi<sup>fi</sup>er for reducing time of simulation.

The pre-processing, including parsing, <sup>fi</sup>ltering and <sup>fi</sup>nalizing, has a strong in<sup>fl</sup>uence on the performance; therefore, a correct preparation is required in order to obtain results re<sup>fl</sup>ecting the behavior of the algorithms. In this paper, the proxy logs <sup>fi</sup>les have been prepared in above steps for getting results re<sup>fl</sup>ecting accurately the performance of the Web proxy caching algorithms. After the preprocessing, the <sup>fi</sup>nal format of our data consists of URL ID, timestamp, elapsed time, size and type of Web object as shown in Table 5.

Table 4  
Proxy datasets and names of proxy servers that datasets came from.

<table><tr><td>Proxy dataset</td><td>Proxy server name</td><td>Location</td><td>Duration of collection</td></tr><tr><td>UC</td><td>uc.us.ircache.net</td><td>Urbana-Champaign, Illinois</td><td>21/8-4/9/2010</td></tr><tr><td>BO2</td><td>bo.us.ircache.net</td><td>Boulder, Colorado</td><td>21/8-4/9/2010</td></tr><tr><td>SV</td><td>sv.us.ircache.net</td><td>Silicon Valley, California (FIX-West)</td><td>21/8-4/9/2010</td></tr><tr><td>SD</td><td>sd.us.ircache.net</td><td>San Diego, California</td><td>21/8-28/8/2010</td></tr><tr><td>NY</td><td>ny.us.ircache.net</td><td>New York, NY</td><td>21/8-4/9/2010</td></tr></table>

An example of the pre-processed data extracted from proxy logs <sup>fi</sup>le.

<table><tr><td>URL_ID</td><td>Timestamp</td><td>Elapsed time (milliseconds)</td><td>Size(bytes)</td><td>Type</td></tr><tr><td>1</td><td>1282348905.73</td><td>33</td><td>33070</td><td>application/octet-stream</td></tr><tr><td>2</td><td>1282348907.41</td><td>703</td><td>14179</td><td>image/jpeg</td></tr><tr><td>3</td><td>1282348908.47</td><td>284</td><td>1276</td><td>image/jpeg</td></tr><tr><td>4</td><td>1282349578.75</td><td>154</td><td>24612</td><td>text/html</td></tr><tr><td>1</td><td>1282349661.61</td><td>31</td><td>33070</td><td>application/octet-stream</td></tr><tr><td>5</td><td>1282349675.35</td><td>203</td><td>5592</td><td>text/html</td></tr><tr><td>6</td><td>1282349688.90</td><td>231</td><td>34796</td><td>text/html</td></tr><tr><td>4</td><td>1282349753.72</td><td>375</td><td>24612</td><td>text/html</td></tr><tr><td>4</td><td>1282350464.01</td><td>133</td><td>24612</td><td>text/html</td></tr><tr><td>1</td><td>1282351887.76</td><td>135</td><td>33070</td><td>application/octet-stream</td></tr><tr><td>4</td><td>1282352609.09</td><td>55</td><td>24612</td><td>text/html</td></tr><tr><td>1</td><td>1282352861.56</td><td>111</td><td>33070</td><td>application/octet-stream</td></tr></table>

## 4.3. Training phase

Since the proxy logs <sup>fi</sup>les are pre-processed as mentioned in Section 4.2, the training datasets are prepared as explained in Section 3.1. Table 6 shows an example of the training dataset extracted from Table 5. In this study, 30 min (1800 s) are used as the sliding window length (SWL) for all datasets. Table 5 contains twelve requests for six Web objects. As can be observed from Tables 5 and 6, Web objects with URL IDs=2, 3, 5 and 6 are requested just one time. So the target values of these objects are 0.0, since these objects would not be requested within forward-looking SWL. On the other hands, Web objects with URL IDs=1 and 4 are requested many times at different times (see the highlighted requests in Tables 5 and 6). Therefore, each request for one of these Web objects represents a pattern with different features. Moreover, the target outputs are based on the future requests. The requests for URL IDs=1 and 4 are highlighted in Tables 5 and 6 for understanding how their features and targets can be updated. For instance, the Web object with URL ID=4 can be requested four times at different times so that information about recency and frequency can be updated in Table 6. More importantly, the target outputs of requests for URL ID=4 may be different depending on the future requests for that Web object within forward-looking SWL. The target value is 1.0 if there is another request for the object within forward-looking SWL; otherwise the target value would be 0.0. This clearly indicates the last request for an object will always have a target value of 0.0.

Each proxy dataset is then divided randomly into training data (70%) and testing data (30%). Subsequently, the dataset is normalized accordingly into the range [0, 1]. Once the dataset is prepared and normalized, the machine learning techniques are implemented using MATLAB and WEKA. We train the SVM model using the libsvm library [6]. The generalization capability of SVM can be controlled through a few parameters like the term C and the kernel parameter like RBF width γ. To decide which values to choose for parameters C and γ, a grid search algorithm is implemented as suggested in [16]. We keep the parameters that obtain the best accuracy using a 10-fold cross validation on the training set. Then, a SVM model is trained depending on the optimal parameters to predict and classify the Web objects whether the objects will be re-visited or not.

An example of a training dataset extracted from a preprocessed <sup>fi</sup>le.

<table><tr><td colspan="6">Inputs</td><td rowspan="2">Target</td></tr><tr><td>Recency</td><td>Frequency</td><td>SWL frequency</td><td>Retrieval time</td><td>Size</td><td>Type</td></tr><tr><td>1800</td><td>1</td><td>1</td><td>33</td><td>33070</td><td>5</td><td>1</td></tr><tr><td>1800</td><td>1</td><td>1</td><td>703</td><td>14179</td><td>2</td><td>0</td></tr><tr><td>1800</td><td>1</td><td>1</td><td>284</td><td>1276</td><td>2</td><td>0</td></tr><tr><td>1800</td><td>1</td><td>1</td><td>154</td><td>24612</td><td>1</td><td>1</td></tr><tr><td>1800</td><td>2</td><td>2</td><td>31</td><td>33070</td><td>5</td><td>0</td></tr><tr><td>1800</td><td>1</td><td>1</td><td>203</td><td>5592</td><td>1</td><td>0</td></tr><tr><td>1800</td><td>1</td><td>1</td><td>231</td><td>34796</td><td>1</td><td>0</td></tr><tr><td>1800</td><td>2</td><td>2</td><td>375</td><td>24612</td><td>1</td><td>1</td></tr><tr><td>1800</td><td>3</td><td>3</td><td>133</td><td>24612</td><td>1</td><td>0</td></tr><tr><td>2226.15</td><td>3</td><td>1</td><td>135</td><td>33070</td><td>5</td><td>1</td></tr><tr><td>2145.08</td><td>4</td><td>1</td><td>55</td><td>24612</td><td>1</td><td>0</td></tr><tr><td>1800</td><td>4</td><td>2</td><td>111</td><td>33070</td><td>5</td><td>0</td></tr></table>

Regarding C4.5 training, a J48 learning algorithm has been used, which is a Java re-implementation of C4.5 and provided with WEKA tool. The default values of parameters and settings are used as determined in WEKA. After training and veri<sup>fi</sup>cation, the trained classi<sup>fi</sup>ers can be saved in the <sup>fi</sup>les to be utilized in improving the performance of the conventional Web proxy caching policies.

In order to benchmark the classi<sup>fi</sup>ers, SVM and C4.5 can be compared to both back-propagation neural network (BPNN) and neuro-fuzzy system (ANFIS) since these intelligent techniques produce good performance in several existing works in Web caching [2,12,13,20,29,31,32]. In this study, a 3-layer ANN is developed using MATLAB. By changing the BPNN parameters depending on some previous works [2,13], we found that the following parameter produces good results: learning rate=0.7; momentum rate=0.9; number of nodes in hidden layer=13; and minimum error=0.005. Regarding ANFIS, the parameter settings for ANFIS training will be based on previous work [2]: type of input member function (MF) is bell function; number of MFs=2 for each input; type of output MF is linear; and training method is hybrid.

## 4.4. Web proxy cache simulation

The simulator WebTraff [24] can be modi<sup>fi</sup>ed to meet our proposed proxy caching approaches. WebTraff is a trace-driven simulator for evaluating different replacement policies such as LRU, LFU, GDS, FIFO, and RAND policies. The trained classi<sup>fi</sup>ers are integrated with WebTraff to simulate the proposed intelligent Web proxy caching approaches. The WebTraff simulator receives the prepared log proxy <sup>fi</sup>le as input and generates <sup>fi</sup>les containing performance measures as outputs. In addition, the maximum cache size should be determined in the simulator. The simulator starts automatically with a cache size of 1 MB, and scales it up by a factor of two for each run until the maximum desired cache size is reached. The output reported by the simulator shows cache size (in MB), hit ratio, and byte hit ratio for each cache size simulated.

## 5. Performance evaluation and discussion

## 5.1. Classifier evaluation

A correct classi<sup>fi</sup>cation rate (CCR) is a measure for evaluating a model or classi<sup>fi</sup>er. However, CCR alone is insuf<sup>fi</sup>cient for measuring the performance of a classi<sup>fi</sup>er, especially if the data is imbalanced. In an imbalanced data case, where the dataset contains signi<sup>fi</sup>cantly more majority class than minority class instances, one can always select the majority class and obtain good CCR. Therefore, in this case, the sensitivity and speci<sup>fi</sup>city measures are also used to measure the performance [15,28].

Table 7  
The measures used for evaluating performance of machine learning techniques.

<table><tr><td>Measure name</td><td>Formula</td></tr><tr><td>Correct classification rate</td><td> $CCR = \frac{TP+TN}{TP+FP+FN+TN} (\%)$ </td></tr><tr><td>True positive rate</td><td> $TPR = \frac{TP}{TP+FN} (\%)$ </td></tr><tr><td>True negative rate</td><td> $TNR = \frac{TN}{TN+FP} (\%)$ </td></tr><tr><td>Geometric mean</td><td> $GM = \sqrt{TPR * TNR} (\%)$ </td></tr></table>

Table 8 Confusion matrix.

<table><tr><td></td><td>Predicted positive</td><td>Predicted negative</td></tr><tr><td>Actual positive</td><td>True positive (TP)</td><td>False negative (FN)</td></tr><tr><td>Actual negative</td><td>False positive (FP)</td><td>True negative (TN)</td></tr></table>

In this study, we consider that the object will belong to the positive class if the object is re-requested again within the forwardlooking SWL. Otherwise, the Web object will belong to the negative class. From proxy log <sup>fi</sup>les, we can observe that most Web objects are visited just one time by the users. Hence, the negative class represents the majority class, while the positive class represents the minority class, which is the most important class in Web caching. Therefore, the true positive rate (TPR) or sensitivity, the true negative rate (TNR) or speci<sup>fi</sup>city, and Geometric mean (GM) can also be used to evaluate the performance of machine learning techniques, as shown in Tables 7 and 8.

Table 9 shows a comparison among the performance measures of SVM, C4.5, BPNN and ANFIS for <sup>fi</sup>ve different proxy datasets in the testing phase. As can be observed from Table 9, all of SVM, C4.5, BPNN and ANFIS produce good performance. It is obvious that both SVM and C4.5 achieve a higher CCR compared to BPNN and ANFIS. SVM and C4.5 achieved the averages of CCR around 94.33% and 94.55% respectively, while BPNN and ANFIS achieved the averages of CCR around 87.39% and 93.93% respectively.

In terms of GM, Table 9 clearly shows that the SVM achieves the best TPR and GM for all datasets. On the contrary, BPNN achieves the worst TPR and GM for all datasets. This is because BPNN tends to classify most of the patterns as the majority class. This contributes to getting the highest TNR of BPNN. On the other hand, SVM is trained with a penalty (weight) option, which can be useful in dealing with imbalanced data. A higher weight is set to a positive class, while less weight is set to a negative class. Thus, SVM has better TPR and GM when compared to other approaches. This indicates that SVM can predict the positive or minority class, which includes the objects that will be re-visited in the near future.

In addition to above measures, the computational time for training SVM, C4.5, BPNN and ANFIS can be calculated on the same computer for different datasets, as shown in Table 10. As expected, C4.5 is the fastest when compared to the other intelligent techniques used. SVM is slower than C4.5 but faster than BPNN and ANFIS for all datasets. Thus, we can conclude that the applications of SVM and C4.5 in Web proxy caching are more practical and effective when compared to other algorithms.

Table 9  
The performance measures of testing datasets.

<table><tr><td></td><td></td><td>BO2</td><td>NY</td><td>UC</td><td>SV</td><td>SD</td><td>Average</td></tr><tr><td rowspan="4">SVM</td><td>CCR</td><td>95.30</td><td>91.19</td><td>95.54</td><td>93.76</td><td>95.84</td><td>94.326</td></tr><tr><td>TPR</td><td>86.41</td><td>91.95</td><td>92.76</td><td>91.16</td><td>89.17</td><td>90.29</td></tr><tr><td>TNR</td><td>96.16</td><td>90.95</td><td>95.93</td><td>94.36</td><td>96.83</td><td>94.846</td></tr><tr><td>GM</td><td>91.15</td><td>91.45</td><td>94.33</td><td>92.97</td><td>92.92</td><td>92.564</td></tr><tr><td rowspan="4">C4.5</td><td>CCR</td><td>95.68</td><td>91.26</td><td>95.88</td><td>94.02</td><td>95.91</td><td>94.55</td></tr><tr><td>TPR</td><td>68.54</td><td>89.36</td><td>78.27</td><td>87.87</td><td>83.81</td><td>81.57</td></tr><tr><td>TNR</td><td>98.30</td><td>91.86</td><td>98.29</td><td>95.74</td><td>97.72</td><td>96.382</td></tr><tr><td>GM</td><td>82.08</td><td>90.60</td><td>87.71</td><td>91.72</td><td>90.50</td><td>88.522</td></tr><tr><td rowspan="4">BPNN</td><td>CCR</td><td>94.08</td><td>75.90</td><td>90.36</td><td>87.95</td><td>88.65</td><td>87.388</td></tr><tr><td>TPR</td><td>32.62</td><td>0.00</td><td>20.07</td><td>45.69</td><td>12.77</td><td>22.23</td></tr><tr><td>TNR</td><td>100.00</td><td>100.00</td><td>99.99</td><td>99.73</td><td>99.98</td><td>99.94</td></tr><tr><td>GM</td><td>57.12</td><td>0.00</td><td>44.79</td><td>67.50</td><td>35.73</td><td>41.028</td></tr><tr><td rowspan="4">ANFIS</td><td>CCR</td><td>95.30</td><td>91.23</td><td>94.75</td><td>92.94</td><td>95.43</td><td>93.93</td></tr><tr><td>TPR</td><td>61.55</td><td>84.94</td><td>62.46</td><td>76.53</td><td>74.77</td><td>72.05</td></tr><tr><td>TNR</td><td>98.56</td><td>93.22</td><td>99.17</td><td>97.52</td><td>98.52</td><td>97.398</td></tr><tr><td>GM</td><td>77.89</td><td>88.98</td><td>78.71</td><td>86.39</td><td>85.83</td><td>83.56</td></tr></table>

Table 11  
Table 10  
The computational time (in seconds) for training SVM, C4.5, BPNN and ANFIS.

<table><tr><td rowspan="2">Dataset</td><td colspan="4">Training time (seconds)</td></tr><tr><td>SVM</td><td>C4.5</td><td>BPNN</td><td>ANFIS</td></tr><tr><td>BO2</td><td>9.11</td><td>0.36</td><td>146.59</td><td>41436.63</td></tr><tr><td>NY</td><td>69.41</td><td>0.85</td><td>316.34</td><td>89057.09</td></tr><tr><td>UC</td><td>280.30</td><td>3.36</td><td>701.18</td><td>202033.64</td></tr><tr><td>SV</td><td>52.20</td><td>0.69</td><td>303.40</td><td>85753.53</td></tr><tr><td>SD</td><td>291.51</td><td>2.90</td><td>693.36</td><td>205294.87</td></tr></table>

## 5.2. Evaluation of intelligent Web proxy caching approaches

## 5.2.1. Performance measures

In Web proxy caching, hit ratio (HR) and byte hit ratio (BHR) are two widely used metrics for evaluating the performance of Web proxy caching policies [2,11,19,20,29]. HR is de<sup>fi</sup>ned as the ratio of the number of requests served from the proxy cache and the total number of requests. BHR refers to the number of bytes served from the cache, divided by the total number of bytes served. It is important to note that HR and BHR work in somewhat opposite ways. It is very dif<sup>fi</sup>cult for one strategy to achieve the best performance for both metrics [5,29,35]. This is due to the fact that the strategies that increase HR typically give preference to small objects, but these strategies tend to decrease BHR by giving less consideration to larger objects. On the contrary, the strategies that do not give preference to small objects tend to increase BHR at the expense of HR [5,29,35].

## 5.2.2. Performance measures of infinite cache

An in<sup>fi</sup>nite cache is a cache with enough space to store all requested objects without the need to replace any object. The in<sup>fi</sup>nite cache size is de<sup>fi</sup>ned as the total size of all unique requests. Therefore, it is unnecessary to consider any replacement policy for an in<sup>fi</sup>nite cache. In an in<sup>fi</sup>nite cache, HR and BHR reach their maximum values. In reality, the caches cannot be designed as in<sup>fi</sup>nite. A replacement policy is needed when the cache is full, and this has a great effect on the performance of Web caching systems. However, in our simulation the in<sup>fi</sup>nite cache is required to determine the maximum cache size in the simulator, which represents the stop point during the simulation. Table 11 shows some statistical information for the maximum HR and BHR of a Web proxy cache with an in<sup>fi</sup>nite size for the different proxy datasets used in the simulation.

## 5.2.3. Impact of cache size on performance measures

In this section, the proposed approaches are compared to LRU, GDS and GDSF policies that are the most common policies in squid software and which form the basis of other Web cache replacement algorithms [29]. Figs. 9 and 10 show HR and BHR of different policies for the <sup>fi</sup>ve proxy datasets with varying cache sizes. As it can be seen in Figs. 9 and 10, when the cache size increases, the HR and BHR boost as well for all algorithms. However, the percentage of increase is reduced when the cache size increases. When the cache size is close to the size of the in<sup>fi</sup>nite cache, the performance becomes stable and close to its maximum level.

In terms of HR, the results of Fig. 9 clearly indicate that C4.5–GDS and SVM–LRU improve the performance in terms of HR for GDS and LRU respectively for all proxy datasets. On the contrary, the HR of GDSF–SVM is similar or slightly worse than the HR of GDSF. This is primarily due to the fact that GDSF tends to store the small object for increasing HR but at the expense of BHR. From Fig. 9, it can be observed that C4.5–GDS achieves the best HR among all the algorithms, while LRU achieves the worst HR among all the algorithms across the <sup>fi</sup>ve proxy datasets.

In terms of BHR, Fig. 10 shows that BHR of LRU is better than BHR of C4.5–GDS, GDS and GDSF for the <sup>fi</sup>ve proxy datasets. This is expected, since LRU policy removes the old objects regardless of their sizes. However, the results in Fig. 10 clearly indicate that SVM–LRU improves LRU performance in terms of BHR in all proxy datasets with different cache sizes. This is mainly due to the capability of SVM–LRU for storing the preferred objects predicted by SVM classi<sup>fi</sup>er and removing the unwanted objects at an early stage. This eventually reduces the pollution of the LRU cache. Consequently, the performance in terms of HR and BHR can be improved by using the SVM–LRU. From Figs. 10, it can be observed that SVM–LRU achieves the best BHR among all algorithms, while GDS and GDSF attain the worst BHR among all the algorithms across the <sup>fi</sup>ve proxy datasets.

Although GDS and GDSF have better performance in terms of HR compared to LRU, it is not surprising that the BHR of GDS and GDSF are the worst among all algorithms (see Figs. 9 and 10). This is due to GDS and GDSF discriminating against large objects, allowing for small and recent objects to be cached. Fig. 10 shows that both SVM–GDSF and C4.5–GDS can produce signi<sup>fi</sup>cant improvements in the BHR of GDSF and GDS respectively, especially with a small cache. When the cache size is small, the replacement of objects is frequently required. Hence, the effect of the performance of a replacement policy appears clearly. In SVM–GDSF, the value of the class predicted by SVM is added as extra weight to give more priority of those cached objects that may be revisited soon even if their sizes are large. In C4.5–GDS, the accumulative scores or probabilities of revisiting of the Web object in the future are added to the GDS policy, instead of the frequency factor. That means that some large objects may have higher accumulative scores or probabilities of revisiting compared to small objects. This explains the signi<sup>fi</sup>cant improvement in BHR for GDS and GDSF. From Figs. 9 and 10, it can be also observed that SVM–GDSF achieves a HR which is close to the best HR achieved by C4.5–GDS, and achieves a BHR which is close to the best BHR achieved by SVM–LRU. That means SVM–GDSF is able to make better balance between HR and BHR than other algorithms.

The averages of HR and BHR for the <sup>fi</sup>ve proxy datasets in each particular cache size are calculated to clarify the bene<sup>fi</sup>ts of the proposed approaches. Then, the improvement ratios (IR) of the performances in terms of HR and BHR which are achieved using the proposed approaches are concluded and summarized in Table 12. In Table 12, the improvement ratio (IR) is calculated as Eq. (21)

$$
I R = \frac {(P M - C M)}{C M} \times 1 0 0 (\%)\tag{21}
$$

Statistics for different proxy datasets used in simulation.

<table><tr><td></td><td>BO2</td><td>NY</td><td>UC</td><td>SV</td><td>SD</td></tr><tr><td>#Total requests</td><td>1,210,693</td><td>3,248,452</td><td>8,891,764</td><td>2,496,001</td><td>29,871,204</td></tr><tr><td>#Cacheable requests</td><td>594,989</td><td>1,518,232</td><td>2,827,904</td><td>1,194,098</td><td>6,059,349</td></tr><tr><td>#Cacheable bytes</td><td>23,204,930,341</td><td>68,402,036,319</td><td>469,362,584,083</td><td>48,043,794,224</td><td>230,326,816,876</td></tr><tr><td>#Unique requests</td><td>530,192</td><td>1,144,885</td><td>2,402,406</td><td>1,012,355</td><td>5,284,441</td></tr><tr><td>Total size of unique requests (bytes)</td><td>18,690,093,450</td><td>56,147,903,761</td><td>156,538,171,752</td><td>38,364,029,432</td><td>190,539,902,251</td></tr><tr><td>#Hits</td><td>64,797</td><td>373,347</td><td>425,498</td><td>181,743</td><td>774,908</td></tr><tr><td>#Byte hits</td><td>4,514,836,891</td><td>12,254,132,558</td><td>312,824,412,331</td><td>9,679,764,792</td><td>39,786,914,625</td></tr><tr><td>Max HR (%)</td><td>10.89</td><td>24.59</td><td>15.05</td><td>15.22</td><td>12.79</td></tr><tr><td>Max BHR (%)</td><td>19.46</td><td>17.91</td><td>66.65</td><td>20.15</td><td>17.27</td></tr></table>

![](/api/attachments/SG2E2DVJ/fulltext/images/ac9647d5b679a205232c244672401ca269ee3ba34e5e7b356afdd90053808b27.jpg)

![](/api/attachments/SG2E2DVJ/fulltext/images/6892303dde8559bb3a903478c4ee0c8cba68e8a1489e4d881b0a40ed179a0ae7.jpg)

![](/api/attachments/SG2E2DVJ/fulltext/images/3a9afc86f2bfc99c17df6a651a708bc69e34d34d560919304359d6d01dd657f5.jpg)

![](/api/attachments/SG2E2DVJ/fulltext/images/5f79f56a046af7bf35d33304de5488f8224440f554bbc360a439a1e82a8471e5.jpg)

![](/api/attachments/SG2E2DVJ/fulltext/images/81521dc45a1265f826c8f49237975a7ea57c89b65d08ed8f89524583c7f80b31.jpg)  
Fig. 9. Impact of cache size on HR for different proxy datasets.

where IR is the percent of improvement achieved by the proposed method (PM) over the conventional method (CM). $\texttt { A } ^ { \bar { \boldsymbol { * } } } - \bar { \boldsymbol { * } }$ sign means that the proposed method was on average worse than the conventional method. The results in Table 12 indicate that C4.5–

GDS improves GDS performance in terms of HR up to 18.90% and in terms of BHR by up to 102.56%. The results also show that the HR of SVM–GDSF is slightly worse than the HR of GDSF. In the worst case, SVM GDSF loses 12.72% from HR compared to GDSF. However, the

![](/api/attachments/SG2E2DVJ/fulltext/images/9992c569152f56f4f8baf30a831268a05aafb2e6b4b436a7bede73347dd4a5e4.jpg)

![](/api/attachments/SG2E2DVJ/fulltext/images/96949f3475438e750a2ccfe03ffc0145b960746492f4e07504d1439e5836d8d9.jpg)

![](/api/attachments/SG2E2DVJ/fulltext/images/02a2b264f9246590312bffc6066df0b39dae3051924397ddff3700a5c8b7cf8a.jpg)

![](/api/attachments/SG2E2DVJ/fulltext/images/1960ebfb042a5acba4835560461e34f9ac56d2ddcbaacc7d8b6dc2f3e0fa3489.jpg)

![](/api/attachments/SG2E2DVJ/fulltext/images/5563d32445d191ee48208e09db913350ff07a81c1e6e44e4b2c5b27278c7daa8.jpg)  
Fig. 10. Impact of cache size on BHR for different proxy datasets.

BHR of SVM–GDSF has doubled many times and reached up to 310.4%, as can be observed from Table 12. Lastly, Table 12 shows that the percentage of performance improvement achieved by SVM–LRU over LRU is up to 26.64% in terms of HR and up to 33.49% in terms of BHR.

## 6. Conclusion and future works

This study has proposed three Intelligent Web proxy caching approaches, namely C4.5–GDS, SVM–LRU and SVM–GDSF for improving the performance of the conventional Web proxy caching algorithms. Initially, SVM and C4.5 learn from Web proxy logs <sup>fi</sup>le to predict the classes of objects to be re-visited or not. Experimental results have revealed that SVM and C4.5 can produce a competitive correct classi<sup>fi</sup>cation rate compared to BPNN and ANFIS. However, both SVM and C4.5 achieve much better true positive rates and GM than BPNN and ANFIS. Also, SVM and C4.5 perform much faster than BPNN and ANFIS in all proxy datasets. More signi<sup>fi</sup>cantly, the trained classi<sup>fi</sup>ers are integrated effectively with conventional Web proxy caching to provide more effective proxy caching policies. From the simulation results, we can conclude with some remarks as follows: <sup>fi</sup>rstly, C4.5– GDS, SVM–LRU and SVM–GDSF would signi<sup>fi</sup>cantly improve the performances of GDS, LRU and GDSF respectively. Secondly, C4.5–GDS achieves the best HR among all algorithms across the <sup>fi</sup>ve proxy datasets. Thirdly, SVM–LRU achieves the best BHR among all algorithms across the <sup>fi</sup>ve proxy datasets. Lastly, SVM–GDSF achieves the best balance between HR and BHR among all algorithms across the <sup>fi</sup>ve proxy datasets.

Table 12  
Improvements ratios (IR) achieved by the proposed approaches over conventional policies.

<table><tr><td rowspan="2">Cache size (MB)</td><td colspan="2">C4.5-GDS Over GDS</td><td colspan="2">SVM-GDSF Over GDSF</td><td colspan="2">SVM-LRU over LRU</td></tr><tr><td>HR</td><td>BHR</td><td>HR</td><td>BHR</td><td>HR</td><td>BHR</td></tr><tr><td>1</td><td>18.90</td><td>33.01</td><td>-1.69</td><td>18.83</td><td>26.64</td><td>20.17</td></tr><tr><td>2</td><td>17.19</td><td>37.46</td><td>-2.77</td><td>30.52</td><td>21.87</td><td>27.68</td></tr><tr><td>4</td><td>14.17</td><td>34.69</td><td>-3.68</td><td>36.07</td><td>15.04</td><td>33.49</td></tr><tr><td>8</td><td>13.43</td><td>57.96</td><td>-4.95</td><td>128.8</td><td>13.70</td><td>27.95</td></tr><tr><td>16</td><td>10.94</td><td>95.46</td><td>-5.53</td><td>133.91</td><td>10.77</td><td>18.53</td></tr><tr><td>32</td><td>9.61</td><td>96.66</td><td>-6.00</td><td>116.08</td><td>8.86</td><td>14.06</td></tr><tr><td>64</td><td>9.27</td><td>58.77</td><td>-5.50</td><td>310.4</td><td>11.08</td><td>16.38</td></tr><tr><td>128</td><td>6.66</td><td>102.56</td><td>-6.48</td><td>146.6</td><td>4.77</td><td>8.41</td></tr><tr><td>256</td><td>4.73</td><td>82.80</td><td>-12.72</td><td>84.83</td><td>4.47</td><td>4.87</td></tr><tr><td>512</td><td>2.64</td><td>68.49</td><td>-5.17</td><td>52.17</td><td>5.18</td><td>3.44</td></tr><tr><td>1024</td><td>1.83</td><td>52.12</td><td>-3.95</td><td>25.48</td><td>5.14</td><td>1.92</td></tr><tr><td>2048</td><td>0.72</td><td>47.75</td><td>-2.39</td><td>13.45</td><td>4.14</td><td>0.57</td></tr><tr><td>4096</td><td>0.33</td><td>26.53</td><td>-2.26</td><td>5.64</td><td>2.64</td><td>0.56</td></tr><tr><td>8192</td><td>0.17</td><td>8.29</td><td>-0.33</td><td>1.56</td><td>1.31</td><td>0.19</td></tr><tr><td>16,384</td><td>0.04</td><td>1.43</td><td>-0.04</td><td>0.66</td><td>0.60</td><td>0.14</td></tr><tr><td>32,768</td><td>0</td><td>0.56</td><td>0</td><td>0.01</td><td>0.32</td><td>0.09</td></tr></table>

There are some limitations in this study. One of the limitations is the classi<sup>fi</sup>ers in the proposed approaches that are trained once and then are used to predict the classes of Web object over the next one or two weeks. A regular retraining of classi<sup>fi</sup>ers would ensure adaptively of the proposed intelligent caching approaches. Another limitation is the preparation of the target outputs in training phase that requires extra computational overhead when looking for the future requests. Therefore, clustering algorithms can be used for enhancing the performance of Web caching policies since the clustering algorithms do not need any preparation for the target output. In the future, other intelligent classi<sup>fi</sup>ers can be utilized to improve the performance of traditional Web caching policies. Finally, several intelligent Web proxy caching approaches can be proposed to help in improving both the hit ratio and the byte hit ratio.

## Acknowledgments

This work is supported by Ministry of Higher Education (MOHE) and Universiti Teknologi Malaysia (UTM) under Research University Grant (VOT Q.J130000.7128.00H71). The authors would like to thank the Research Management Center (RMC) for the research activities and Soft Computing Research Group (SCRG) for their support and incisive comments in making this study a success. The authors are also grateful to the National Laboratory of Applied Network Research (NLANR), which is located in the United States, for providing us with access to traces and proxy logs <sup>fi</sup>les.

## References

[1] M. Abrams, C.R. Standridge, G. Abdulla, E.A. Fox, S. Williams, Removal Policies in Network Caches for World-Wide Web Documents, ACM, 1996, pp. 293–305.

[2] W. Ali, S. Shamsuddin, Intelligent client-side web caching scheme based on least recently used algorithm and neuro-fuzzy system, in: W. Yu, H. He, N. Zhang (Eds.), Advances in Neural Networks — ISNN 2009, Springer, Berlin/Heidelberg, 2009, pp. 70–79.

[3] W. Ali, S.M. Shamsuddin, A.S. Ismail, Web proxy cache content classi<sup>fi</sup>cation based on support vector machine, Journal of Arti<sup>fi</sup>cial Intelligence 4 (2011) 100–109.

[4] W. Ali, S.M. Shamsuddin, A.S. Ismail, A survey of Web caching and prefetching, International Journal of Advances in Soft Computing and Its Applications 3 (2011) 18.

[5] P. Cao, S. Irani, Cost-aware WWW proxy caching algorithms, Proceedings of the 1997 Usenix Symposium on Internet Technology and Systems, Monterey, CA, 1997.

[6] C.C. Chang, C.J. Lin, LIBSVM: A library for support vector machines, http://www. csie.ntu.edu.tw/\~cjlin/libsvm 2001

[7] T. Chen, Obtaining the optimal cache document replacement policy for the caching system of an EC website, European Journal of Operational Research 181 (2007) 828–841.

[8] H.T. Chen, Pre-Fetching and Re-Fetching in Web Caching Systems: Algorithms and Simulation, Trent University, Peterborough, Ontario, Canada, Peterborough Ontario, Canada, 2008.

[9] R.-C. Chen, C.-H. Hsieh, Web page classi<sup>fi</sup>cation based on a support vector machine using a weighted vote schema, Expert Systems with Applications 31 (2006) 427–435.

[10] L. Cherkasova, Improving WWW Proxies Performance with Greedy-Dual-Size-Frequency Caching Policy, HP Technical Report, Palo Alto, 1998

[11] J. Cobb, H. ElAarag, Web proxy cache replacement scheme based on back-propagation neural network, Journal of Systems and Software 81 (2008) 1539–1558

[12] H. ElAarag, S. Romano, Improvement of the neural network proxy cache replacement strategy, Proceedings of the 2009 Spring Simulation Multiconference, Society for Computer Simulation International, San Diego, California, 2009, pp. 1–8.

[13] Farhan, Intelligent Web Caching Architecture, Faculty of Computer Science and Information System, UTM University, Johor, Malaysia, 2007.

[14] A.P. Foong, H. Yu-Hen, D.M. Heisey, Logistic regression in an adaptive Web cache, IEEE Internet Computing 3 (1999) 27–36.

[15] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Morgan Kaufmann, 2001.

[16] C.W. Hsu, C.C. Chang, C.J. Lin, A practical guide to support vector classi<sup>fi</sup>cation, A Online Guild for Using LIBSVM Tools, 2009.

[17] C.-J. Huang, Y.-W. Wang, T.-H. Huang, C.-F. Lin, C.-Y. Li, H.-M. Chen, P.C. Chen, J.-J. Liao, Applications of machine learning techniques to a sensor-network-based prosthesis training system, Applied Soft Computing 11 (2011) 3229–3237.

[18] C.C. Kaya, G. Zhang, Y. Tan, V.S. Mookerjee, An admission-control technique for delay reduction in proxy caching, Decision Support Systems 46 (2009) 594–603.

[19] W. Kin-Yeung, Web cache replacement policies: a pragmatic approach, IEEE Network 20 (2006) 28–34.

[20] T. Koskela, J. Heikkonen, K. Kaski, Web cache optimization with nonlinear model using object features, Computer Networks 43 (2003) 805–817.

[21] C. Kumar, Performance evaluation for implementations of a network of proxy caches, Decision Support Systems 46 (2009) 492–500.

[22] C. Kumar, J.B. Norris, A new approach for a proxy-level web caching mechanism, Decision Support Systems 46 (2008) 52–60.

[23] B. Liu, Web Data Mining: Exploring Hyperlinks, Contents, and Usage Data, Springer, 2007.

[24] N. Markatchev, C. Williamson, WebTraff: a GUI for Web proxy cache workload modeling and analysis, Proceedings of the 10th IEEE International Symposium on Modeling, Analysis, and Simulation of Computer and Telecommunication Systems, IEEE Computer Society, 2002, p. 356.

[25] NLANR, National Lab of Applied Network Research(NLANR), Sanitized Access Logs: Available at http://www.ircache.net/2010.

[26] S. Podlipnig, L. Böszörmenyi, A survey of Web cache replacement strategies, ACM Computing Surveys 35 (2003) 374–398.

[27] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, 1993.

[28] L. Rokach, O.Z. Maimon, Data Mining with Decision Trees : Theory and Applications, World Scienti<sup>fi</sup>c, Singapore; Hackensack, NJ, 2008

[29] S. Romano, H. ElAarag, A neural network proxy cache replacement strategy and its implementation in the Squid proxy server, Neural Computing and Applications 20 (2011) 59–78.

[30] G. Sajeev, M. Sebastian, A novel content classi<sup>fi</sup>cation scheme for web caches, Evolving Systems 2 (2011) 101–118.

[31] S. Sulaiman, S.M. Shamsuddin, F. Forkan, A. Abraham, Intelligent Web caching using neurocomputing and particle swarm optimization algorithm, Modeling & Simulation 2008. AICMS 08. Second Asia International Conference on, 2008, pp. 642–647.

[32] S. Sulaiman, S.M. Shamsuddin, A. Abraham, Rough Neuro-PSO Web caching and XML prefetching for accessing Facebook from mobile environment. Nature & Biologically Inspired Computing, 2009. NaBIC 2009. World Congress on, 2009, pp. 884–889.

[33] A. Vakali, Evolutionary techniques for Web caching, Distributed and Parallel Databases 11 (2002) 93-116

[34] V. Vapnik, The Nature of Statistical Learning Theory, Springer, New York, 1995

[35] Q. Yang, J.Z. Huang, M. Ng, A data cube model for prediction-based Web prefetching, Journal of Intelligent Information Systems 20 (2003) 11–30.

![](/api/attachments/SG2E2DVJ/fulltext/images/3e80e88b27cc27959f3c312a89662aad1d6999ab0cb9317ff3329b5344db750c.jpg)

![](/api/attachments/SG2E2DVJ/fulltext/images/eb781243d1b812a5bbdf6f833aa6a2366ef19fd6c511e5e8b50af8a9918b0b5a.jpg)

Waleed Ali is a PhD researcher at Faculty of Computer Science and Information Systems, Universiti Teknologi Malaysia (UTM), Malaysia. He obtained his B.Sc (Computer Science) from Taiz University, Yemen, and his M.Sc (Computer Science) from Universiti Teknologi Malaysia, Skudai, Johor, Malaysia. He is a member of Soft Computing Research Group, UTM. He has published several papers on international journals, conferences and book chapters. His research interests include Web caching, Web prefetching, Web usage mining, and machine learning techniques and their applications.

Siti Mariyam Shamsuddin is a Professor at Faculty of Computer Science and Information Systems, Universiti Teknologi Malaysia (UTM), Malaysia. She received her Bachelor and Master degree in Mathematics from New Jersey USA, and her PhD in Pattern Recognition & Arti<sup>fi</sup>cial Intelligence from Universiti Putra Malaysia (UPM), Malaysia. Currently, she is a Head of Soft Computing Research Group, k-Economy Research Alliance, Universiti Teknologi Malaysia (UTM), Johor Malaysia. Her research interests include the fundamental aspects of soft computing and its application, pattern recognition, forensic document analysis, and geometric modeling.

![](/api/attachments/SG2E2DVJ/fulltext/images/007fbfe53e8cad1d7628ad5fa50687b9a4b169725cbcfcf77634c1bcdf9c8103.jpg)

Abdul Samad Ismail is an Associate Professor at Faculty of Computer Science and Information Systems, Universiti Teknologi Malaysia (UTM), Malaysia. He received a Ph.D degree in Collaborative Environments from University of Wales Swansea, Swansea, UK in 2002, and MSc Computer Science Central Michigan from University Mt. Pleasant, Michigan, USA. His current research area is Wireless sensor network.
