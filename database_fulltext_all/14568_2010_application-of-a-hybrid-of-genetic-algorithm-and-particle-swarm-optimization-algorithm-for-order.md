---
otero_id: 14568
otero_key: "YMSZ348S"
title: "Application of a hybrid of genetic algorithm and particle swarm optimization algorithm for order clustering"
authors: "R.J. Kuo; L.M. Lin"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.05.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Application of a hybrid of genetic algorithm and particle swarm optimization algorithm for order clustering

R.J. Kuo <sup>a,</sup>⁎, L.M. Lin <sup>b</sup>

<sup>a</sup> Department of Industrial Management, National Taiwan University of Science and Technology, No. 43, Section 4, Kee-Lung Road, Taipei 106, Taiwan, ROC <sup>b</sup> AU Optronics Corporation, No. 1, Li-Hsin Road. 2, Hsinchu Science Park, Hsinchu 300, Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 5 January 2010 Accepted 9 May 2010 Available online 17 May 2010

Keywords: Clustering analysis ART2 neural network Particle swarm optimization algorithm Genetic algorithm

## a b s t r a c t

This study proposes an evolutionary-based clustering algorithm based on a hybrid of genetic algorithm (GA) and particle swarm optimization algorithm (PSOA) for order clustering in order to reduce surface mount technology (SMT) setup time. Simulational results via Iris, Glass, Vowel and Wine benchmark data sets indicate that the proposed evolutionary-based clustering algorithm is more accurate than the GA-based and PSOA-based clustering algorithms. In addition, the model evaluation results which use order information provided by an international industrial personal computer (PC) manufacturer show that the proposed algorithm is also superior to GA-based and PSOA-based clustering algorithms. Through order clustering, scheduling orders that belong to the same cluster together can reduce production time as well as machine idle time.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

In the industrial personal computer (PC) industry, printed circuit board (PCB) assembly is a fundamental manufacturing process, in which surface mount technology (SMT) plays a very important role. By applying an SMT production system, not only are there more components on the limited space of a PCB, but production ef<sup>fi</sup>ciency and product stability are also enhanced. However, the high mix low volume production style presents dif<sup>fi</sup>culties for SMT production systems. In this kind of production system, production line-changes create very serious bottlenecks since before, production labor must prepare for the materials and also bind the materials prior to linechanges, which is very time consuming. If production labor cannot complete these tasks before the next order starts, it causes both idle time for these expensive machines and decreases production capability utilization. Currently, this problem is frequently encountered in SMT production system, and the only way it can be handled is to prepare for more materials and increase the number of binding labors. An alternative is to cluster the orders before scheduling and then schedule similar orders together in order to reduce the materialbinding time.

Clustering analysis is the process of identifying natural groupings or clusters within multidimensional data, based on some similar measures, like Euclidean distance [27]. Basically, as one of the most primitive activities of human beings, clustering plays an important and indispensable role in the long history of human development. In order to learn about a new object or understand a new phenomenon, people always try to seek features that can describe it, and further compare it with other known objects or phenomena, based on similarity or dissimilarity, generalized as proximity, according to certain standards or rules [50].

Thus, this study proposes an evolutionary-based clustering algorithm based on a hybrid of genetic algorithm (GA) and particle swarm optimization algorithm (PSOA) for order clustering. It is named hybrid of GA and PSOA (HGAPSOA). Order features are characterized using bills of materials (BOMs) for all products. Through order clustering, the orders with similar materials are grouped together. The production engineer can schedule the similar orders together based on clustering results in order to reduce the setup time for SMT line-change operations in the industrial PC industry.

For assessing the proposed HGAPSOA, four benchmark data sets are employed, including iris, wine, vowel, and glass. The simulation results show that the proposed HGAPSOA outperforms the GA-based and PSO-based algorithms proposed by previous studies. In addition, evaluation results using data provided by an international industrial PC manufacturer also show that the proposed HGAPSOA is more accurate than other algorithms. By integrating the proposed algorithm with a scheduling method, this study's method can dramatically reduce SMT production system setup time and increase the utilization of machine capability.

The remainder of this study is organized as follows. Section 2 brie<sup>fl</sup>y presents the necessary background, including discussion of clustering analysis and particle swarm optimization algorithms, while the proposed order clustering system is explained in Section 3. Sections 4 and 5 discuss the simulation results using four benchmark data sets and the evaluation results for a real-world problem, respectively. Finally, concluding remarks are made in Section 6.

## 2. Background

This section brie<sup>fl</sup>y presents the general backgrounds of clustering analysis and PSOA.

## 2.1. Clustering analysis

Clustering analysis partitions data into a certain number of clusters. Most researchers describe a cluster by considering internal homogeneity and external separation, i.e., patterns in the same cluster should be similar to each other, while patterns in different clusters should not [50].

Most clustering algorithms are based on two popular techniques known as hierarchical and partitional clustering [24]. Hierarchical clustering algorithms organize data into a hierarchical structure according to the proximity matrix. The results of hierarchical clustering are usually depicted by a binary tree or dendrogram. Hierarchical clustering algorithms are mainly classi<sup>fi</sup>ed as agglomerative methods and divisive methods. Many algorithms have been used in this clustering method, for example, CURE [20], BIRCH [51], ROCK [21], CHAMELEON [28], DIANA [29], AUTOCLUST [16] and AMOEBA [15].

In contrast to hierarchical clustering which yields a successive level of clusters by iterative fusions or divisions, partitional clustering assigns a set of objects into clusters with no hierarchical structure. These algorithms try to minimize certain criteria, like square error function, and can therefore be treated as optimization problems. Partitional clustering aims to optimize cluster centers, as well as the number of clusters [23]. Partitional clustering can be further classi<sup>fi</sup>ed into supervised and unsupervised clustering algorithms. The main difference between these clustering algorithms is that supervised clustering algorithms need to specify the number of clusters. They are discussed in more detail as follows.

## 2.1.1. Supervised clustering algorithms

The most widely used supervised clustering algorithm is the K-means algorithm [17]. The K-means algorithm starts with k cluster centroids, which are initialized to random values. Furthermore, each point of the data set is assigned to the cluster closest to it. The centroids are then recalculated according to their associated points. This process is repeated until convergence is reached. Latter and Bezdek [5] developed a fuzzy version of the K-means algorithm, called the fuzzy C-means algorithm. The object can belong to all of the clusters with a certain degree of membership. Other modi<sup>fi</sup>cations of fuzzy C-means algorithms are the possibilistic-means clustering algorithm [32], fuzzy c-shells [6], and hierarchical unsupervised fuzzy clustering [19].

In addition, evolutionary algorithms are also employed to improve the performance of K-means. Clustering can be regarded as a category of optimization problems that uses evolutionary algorithms, like genetic algorithms (GA), particle swarm optimization algorithms (PSOAs) or ant colony optimization algorithms. Many techniques support this method, such as the genetically guided algorithm [22], the genetic K-means algorithm [31], Tabu search clustering [1], the ant colony clustering algorithm [35], and the particle swarm K-means optimization algorithm [37]. But the main drawback of these clustering algorithms is the process of parameter selection.

## 2.1.2. Unsupervised clustering algorithms

Regarding unsupervised clustering algorithms, arti<sup>fi</sup>cial neural networks are the most representative. An arti<sup>fi</sup>cial neural network (ANN) is a system that has been derived through models of neurophysiology. In general, they consist of a collection of simple nonlinear computing elements whose inputs and outputs are linked to form networks. ANN-based clustering has been dominated by selforganizing feature maps (SOM) and adaptive resonance theory (ART). Some important representative algorithms include SOM [30], ART1 [7], ART2 [8], and fuzzy ART [9].

SYNERACT [26], an alternative approach to ISODATA [3], combines K-means with hierarchical descending approaches. It is not necessary to specify the number of clusters. Based on K-means, other unsupervised clustering algorithms have also been developed, like X-means [46] and G-means [23].

Gath and Geva [18] proposed an unsupervised clustering algorithm based on the combination of fuzzy C-means and fuzzy maximum likelihood estimation. Lorette et al. [41] proposed an algorithm based on fuzzy clustering to dynamically determine the number of clusters in a data set.

Lee and Antonsson [38] applied an evolution strategy to dynamically cluster a data set. The evolution strategy they proposed implemented variable length genomes to search for both the centroids and K. In addition, Omran et al. [45] proposed a new dynamic clustering approach (DCPSO) based on particle swarm optimization algorithm.

## 2.2. Particle swarm optimization algorithm (PSOA)

PSOA shares many similarities with evolutionary computation techniques such as GAs. Systems are initialized with a population of random solutions and searches for optima by updating generations. However, unlike GA, PSOA has no evolutionary operators, such as crossover and mutation. In the PSOA, the potential solutions, called particles, move through the problem space by following the current optimum particles.

PSOA was <sup>fi</sup>rst designed by Kennedy and Eberhart in 1995. In the original PSOA, particles are represented as $X _ { i } { = } ( x _ { i 1 } , x _ { i 2 } , { \ldots } , X _ { i D } )$ , which represents a potential solution to a problem in D-dimensional space. Each particle keeps a memory of its previous best position Pbest, and a velocity along each dimension, represented as $V _ { i } = ( \nu _ { i 1 } , \nu _ { i 2 } , . . . , \nu _ { i D } ) .$ At each iteration, the position of the particle with the best <sup>fi</sup>tness value in the search space, designated as g, and the P vector of the current particle are combined to adjust the velocity along each dimension, and that velocity is then used to compute a new position for the particle [14]. This method can be divided into the GBEST and LBEST versions [14], whose main difference is their de<sup>fi</sup>nition of what is the best. In the GBEST version, the particle swarm optimizer keeps track of the overall best value, and its location, obtained thus far by any particle in the population, which is called gbest $( P _ { g d } )$ . For the LBEST version, in addition to gbest, each particle keeps track of the best solution, called lbest $( P _ { g d } )$ , attained within a local topological neighborhood of particles. However, the particle velocities in each dimension are held to a maximum velocity, $V _ { \mathrm { m a x } } ,$ , and the velocity in that dimension is limited to $V _ { \mathrm { m a x } } .$ The updating rule is as follows:

$$
V _ {i d} ^ {n e w} = V _ {i d} ^ {o l d} + c _ {1} \cdot r a n d _ {1} \cdot (P _ {i d} - X _ {i d}) + c _ {2} \cdot r a n d _ {2} \cdot (P _ {g d} - X _ {i d})\tag{1}
$$

$$
X _ {i d} ^ {n e w} = X _ {i d} ^ {o l d} + V _ {i d} ^ {n e w}\tag{2}
$$

where $c _ { 1 }$ and $c _ { 2 }$ determine the relative in<sup>fl</sup>uence of the social and cognitive components (learning factors), while rand and rand denote two random numbers uniformly distributed in the interval [0,1].

In the original version, the maximum velocity $V _ { \mathrm { m a x } }$ serves as a constraint to control the global exploration ability of a particle swarm. As stated above, a larger $V _ { \mathrm { m a x } }$ facilitates global exploration, while a smaller $V _ { \mathrm { m a x } }$ encourages local exploitation. The concept of an inertia weight was developed to better balance exploration and exploitation in order to eliminate the needs of $V _ { \mathrm { m a x } } .$ . The inclusion of an inertia weight in the particle swarm optimization algorithm was <sup>fi</sup>rst reported by Shi and Eberhart in 1998 [47]. The authors proposed two de<sup>fi</sup>nitions of inertia weight: the <sup>fi</sup>rst one de<sup>fi</sup>nes inertia weight as a positive constant; the second de<sup>fi</sup>nes it as variably decreasing with time. This is because the larger inertia weight has more exploration ability at the beginning to <sup>fi</sup>nd a good seed, and the later small inertia weight has more exploitation ability to search the local area around the seed. The experimental result shows that weight decreasing with time has more potential. The updating rule is as follows.

$$
V _ {i d} ^ {\text {new}} = W \cdot V _ {i d} ^ {\text {old}} + c _ {1} \cdot r a n d _ {1} \cdot (P _ {i d} - X _ {i d}) + c _ {2} \cdot r a n d _ {2} \cdot (P _ {g d} - X _ {i d})\tag{3}
$$

$$
X _ {i d} ^ {n e w} = X _ {i d} ^ {o l d} + V _ {i d} ^ {n e w}\tag{4}
$$

where W is an inertia weight.

Shi and Ebherhart [48] subsequently explored what impact the inertia weight and maximum velocity have on the performance of the particle swarm optimizer, and provided guidelines for selecting these two parameters.

When we lack knowledge regarding the selection of $V _ { \mathrm { m a x } } ,$ it is also a good choice to set $V _ { \mathrm { m a x } }$ equal to $X _ { \mathrm { m a x } }$ . Furthermore, if a time-varying inertia weight is employed, even better performance can be expected. Because particle swarm optimization originated from efforts to model social systems, a thorough mathematical foundation of the methodology was not developed along with the algorithm. Recent work done by Clerc indicates that the use of a constriction factor may be necessary to ensure convergence of the PSOA [11]. The updating rule is as follows.

$$
V _ {i d} ^ {\text { new }} = K \times \left[ V _ {i d} ^ {\text { old }} + c _ {1} \times r a n d _ {1} \times \left(P _ {i d} - X _ {i d} ^ {\text { old }}\right) + c _ {2} \times r a n d _ {2} \times \left(P _ {g d} - X _ {i d} ^ {\text { old }}\right) \right]\tag{5}
$$

$$
X _ {i d} ^ {n e w} = X _ {i d} ^ {o l d} + V _ {i d} ^ {n e w}\tag{6}
$$

$$
K = \frac {2}{\left| 2 - \varphi - \sqrt {\varphi^ {2} - 4 \varphi} \right|}, \quad \varphi = c _ {1} + c _ {2} \text {   and   } \varphi > 4\tag{7}
$$

where K is a constriction factor.

If particles' previous velocities are very close to zero, then all the particles will stop moving once they catch up with the global best particle, which may lead to premature convergence of the algorithm. Thus van den Bergh and Engelbrecht [4] suggest a new velocity update equation in order to keep the global best particle moving until it has reached a local minimum. The updating rule is as follows:

$$
V _ {i d} ^ {n e w} = W \times V _ {i d} ^ {o l d} - X _ {i d} ^ {o l d} + P _ {g d} + \rho^ {o l d} \times (1 - 2 r a n d _ {2})\tag{8}
$$

$$
X _ {i d} ^ {n e w} = W \times V _ {i d} ^ {n e w} + P _ {g d} + \rho^ {o l d} \times (1 - 2 r a n d _ {2})\tag{9}
$$

$$
\rho_ {0} = 1. 0, \rho^ {\text { new }} = \left\{ \begin{array}{c c} 2 \rho^ {\text { old }} & \text { if   \#   successes } > s _ {c} \\ 0. 5 \rho^ {\text { old }} & \text { if   \#   failures } > f _ {c} \\ \rho^ {\text { old }} & \text { otherwise } \end{array} \right.\tag{10}
$$

where $\rho$ is a scaling factor.

Social interaction is an important factor to improve PSOA performance. To enhance the social interactions in the algorithm, Zhao et al. [52] put forward a new method of improved PSOA. They propose the use of an improved adaptation strategy with enhanced social interactions for PSOA. This adaptation strategy uses the information of more particles to control the mutation operation. It also extends the original formulas of PSOA to search for the global optimal solution more effectively. This is similar to the human society in that a group of leaders can make better decisions. The updating rule is as follows:

$$
V _ {i d} ^ {\text {new}} = W \times V _ {i d} ^ {\text {old}} + c _ {1} \times r a n d _ {1} \times \left(P _ {i d} - X _ {i d} ^ {\text {old}}\right) + \sum_ {i = 1} ^ {n} c _ {2, i} \times r a n d _ {2, i} (t) \times \left(\hat {P} _ {i, t} - X _ {i d} ^ {\text {old}}\right)\tag{11}
$$

$$
X _ {i d} ^ {n e w} = X _ {i d} ^ {o l d} + V _ {i d} ^ {n e w}\tag{12}
$$

$$
W = w _ {\max} - \frac {w _ {\max} - w _ {\min}}{i t e r _ {\max}} \times i t e r\tag{13}
$$

Xiao et al. [49] proposed a hybrid clustering approach based on a selforganizing map (SOM) neural network. The proposed algorithm uses a PSOA to evolve weights for the SOM neural network. The weights are trained by the SOM neural network in the <sup>fi</sup>rst stage, and in the second stage they are optimized by the PSOA. The experimental results show that the hybrid method tries to tune the original SOM such that it can achieve a better tradeoff between the average quantization error and the topographic error. van der Merwe and Engelbrecht [44] proposed two new approaches using PSOA to cluster data. The <sup>fi</sup>rst method, called the PSO clustering algorithm, shows how the PSOA can be used to <sup>fi</sup>nd the centroids of a user-speci<sup>fi</sup>ed number of clusters. The second method, called hybrid PSOA, <sup>fi</sup>rst uses K-means clustering to seed the initial swarm and then uses PSOA to re<sup>fi</sup>ne the clusters formed by K-means. These new PSOAs were evaluated on six data sets, and compared with the performance of K-means clustering. Results show that both PSOAs have a great deal of potential. Chen and Ye also proposed a clustering analysis algorithm based on PSOA [10]. However, the concept behind their algorithm is similar to [44], and the main difference is in <sup>fi</sup>tness function only. Finally, the experimental results obtained using four arti<sup>fi</sup>cial data sets show the algorithm proposed in this study performs better than Kmeans and fuzzy C-means. Cohen and de Castro [12] presented a modi<sup>fi</sup>ed PSOA with self-organization in the updating rule for clustering analysis. In their PSOA, it is not necessary to calculate <sup>fi</sup>tness value. The results show that it is better than the K-means method. Kuo et al. (2008) proposed a PSKO which combined PSO clustering [44] with K-means. The PSKOA was evaluated on four data sets, and compared with the performance of Kmeans clustering, PSO clustering and hybrid PSO. The experimental results show that the PSKO algorithms outperform other algorithms.

## 2.3. Genetic algorithm (GA)

Holland [25] proposed Genetic Algorithm in “Adaptation in Natural and Arti<sup>fi</sup>cial Systems” published in 1975, and its basic view is based on survival of the <sup>fi</sup>ttest in natural selection — Charles Darwin. Based on the survival and reproduction of the <sup>fi</sup>ttest, GA adopts a group of simulated encoded chromosomes and calculates the <sup>fi</sup>tness of chromosomes. Each chromosome undergoes crossover and mutation to produce next generation. This evolution process continues until the stopping criteria are reached. GA is appropriate for large-sized, nonlinear space problems which solution is unpredictable. Relying on multi-point search and algorithmic features, it is not easy to fall into local optimal solution but can converge to universal optimal solution.

Since GA is good at searching, they are used to solve the clustering problem. Murthy and Chowdhury [43] proposed a GA-based method to solve the clustering problem and used three experiments on synthetic and real life data sets to evaluate the performance. The results show that the GA-based method may improve the <sup>fi</sup>nal output of K-means. Al-Sultan and Maroof [2] studied several algorithms that include the Kmeans algorithm, the simulated annealing algorithm, the Tabu search algorithm, and the genetic algorithm and compare the performance for the clustering problems from the literature. In general, the result of the Kmeans algorithm is the worst. Krishna and Murty [31] proposed the GKA algorithm for clustering, and proved that the algorithm can converge to an optimal solution. In Ujjwal and Bandyopadhyay's experiments, the GAclustering algorithm surpasses the K-means algorithm [42]. Also, Kuo et al. [33,36] presented different coding methods for genetic clustering. Above methods have a prerequisite that the clusters must be a <sup>fi</sup>xed number, but in real world the number of clusters is unknown. Lin and Shiueng [40] propose a genetic-algorithm-based approach that can automatically <sup>fi</sup>nd the proper number of clusters, and the recovery of their algorithm surpasses K-means with the IRIS data.

## 3. Methodology

This section presents the proposed order clustering system which consists of three components: (1) data collection and transformation, (2) principle component analysis, and (3) clustering analysis, as shown in Fig. 1. The following subsections brie<sup>fl</sup>y discuss these three components.

![](/api/attachments/YMSZ348S/fulltext/images/c3ece5cfd661dee8d1d94023966dc5426968f138b3ef1dde2e9c163910453fb1.jpg)  
Fig. 1. Order clustering system

## 3.1. Data collection and transformation

In order to classify the coming orders for their corresponding clusters, all previous orders must <sup>fi</sup>rst be collected and clustered. These data can be retrieved from a company's enterprise resources planning system. Then, the bill of materials (BOM) for each order is used as the features for each order, or product.

## 3.2. Principle component analysis

Due to the vast number of materials used for each order, it is very time consuming to directly use these data for clustering analysis, and it is more feasible to reduce the dimensionality for these data in advance. A statistical method, principle component analysis, is employed for this purpose so that each order has a limited number of features. This can result in shorter computational time without in<sup>fl</sup>uencing the computational outcome.

## 3.3. Clustering analysis

After implementing principle component analysis, the data obtained is applied for clustering analysis. Since the proposed clustering algorithm belongs to the supervised clustering method, an ART2 neural network is <sup>fi</sup>rst employed to determine the number of clusters.

## 3.3.1. ART2 neural network

ART2 neural network architecture is designed for processing analog as well as binary input patterns [8]. An ART2 neural network consists of F1 and F2 layers. There are seven nodes in the F1 layer (W, X, U, V, P, Q). The input signal is processed by the F1 layer and then is passed from the bottom to the top value $( b _ { i j } ) .$ . The result of the bottom-to-top value is an input signal of the F2 layer. The nodes of the F2 layer compete with each other to produce a winning unit and the winning unit returns the signal to the F1 layer. The match value is then calculated with the top to bottom value $( t _ { j i } )$ in the F1 layer and compared with the vigilance value. If the match value is greater than the vigilance value, then the weight of b<sub>ij</sub> and $t _ { j i }$ is updated. Otherwise, the reset signal is sent to the F2 layer and the winning unit is inhibited. After inhibition, the other winning unit is found in the F2 layer. If all of the F2 layer nodes are inhibited, the F2 layer produces a new node and generates the initial corresponding weights to the new node.

3.3.2. Hybrid of genetic algorithm and particle swarm optimization algorithm (HGAPSOA) for clustering

PSOA, like GA, is a population-based stochastic search process. The algorithm maintains a population of particles, where each particle represents a potential solution to an optimization problem. Thus, we propose a new technique, a hybrid of genetic algorithm and particle swarm optimization algorithm (HGAPSOA) for clustering problems. The HGAPSOA integrates particle swarm optimization, genetic algorithm and the K-means method.

The HGAPSOA randomly initializes a population of size 2N. These individuals may be regarded as chromosomes in the case of GA, or as particles in the case of PSOA. 2N individuals are fed into the real-coded GA to create 2N new individuals by reproduction, crossover and mutation operators. Then the 2N individuals are sorted by <sup>fi</sup>tness, and the top N individuals are applied to Improved PSOA. Thus Improved PSOA can use better-performing individuals as the initial population to search for the optimum solution. In addition, the individuals with poor performance remain in order to escape the solution and avoid premature convergence. At the end of the HGAPSOA, the K-means algorithm is used for the purpose of fast convergence. The framework of the HGAPSOA is represented as shown in Fig. 2.

Improved PSOA in Fig. 2 is a modi<sup>fi</sup>ed particle swarm optimization algorithm based on NPSO [39]. In Improved PSOA, there is a crossover of $P _ { i d }$ and $P _ { g d }$ for every particle. Then we can get two child particles. After comparison, let the particle with the smaller <sup>fi</sup>tness value be the <sup>fi</sup>nal child particle. Therefore, Improved PSOA can use betterperforming $P _ { i d }$ and $P _ { g d }$ to lead all particles to search for the optimum solution. Then, the $V _ { i d }$ is updated according to Eq. (14):

$$
V _ {i d} ^ {\text { new }} = W ^ {*} V _ {i d} ^ {\text { old }} + c _ {1} ^ {*} \operatorname{rand} _ {1} ^ {*} \left(P _ {i d} - X _ {i d}\right) + c _ {2} ^ {*} \operatorname{rand} _ {2} ^ {*} \left(P _ {g d} - X _ {i d}\right),\tag{14}
$$

![](/api/attachments/YMSZ348S/fulltext/images/0fe7ceede0bf32e42c50f5e484d829e01b0fbb22e8b78e54464fd9e55b0f3a24.jpg)  
Fig. 2. The framework of the HGAPSOA

![](/api/attachments/YMSZ348S/fulltext/images/b42e8ccb447c80f9041c9b1aa1fd44ae8cda09139ecc79da71834ea8593ae947.jpg)  
Fig. 3. HGAPSOA computational <sup>fl</sup>ow chart.

and mutated. Then $X _ { i d }$ can be obtained using Eq. (15) as shown below:

$$
X _ {i d} ^ {\text { new }} = X _ {i d} ^ {\text { old }} + V _ {i d} ^ {\text { new }}.\tag{15}
$$

The next section will introduce the procedure to the clustering problem.

3.3.3. HGAPSOA computational procedure

The computational procedures for the proposed HGAPSOA are as follows:

Step 1 Set up parameters including population size 2N (number of particles), inertia weight, $W ,$ maximum velocity, $V _ { \mathrm { m a x } } ,$ and two learning factors, $c _ { 1 }$ and $c _ { 2 } .$

Table 1  
The corresponding information for each data set.

<table><tr><td>Name</td><td>Number of data</td><td>Number of features</td><td>Number of clusters</td></tr><tr><td>Iris</td><td>150</td><td>4</td><td>3</td></tr><tr><td>Wind</td><td>178</td><td>13</td><td>3</td></tr><tr><td>Vowel</td><td>990</td><td>10</td><td>11</td></tr><tr><td>Glass</td><td>214</td><td>9</td><td>6</td></tr></table>

Step 2 Initialize each particle randomly with initial position, $X _ { i d }$ and velocity, $V _ { i d } .$ In PSO clustering, we need to know the number of clusters, k, in advance. In this study, an ART2 neural network will provide this information to HGAPSOA. Since each particle is a vector containing k cluster centroids, each cluster's position, $X _ { i d }$ can be represented as:

$$
X _ {i d} = \left(x _ {i 1}, \dots , x _ {i j}, \dots , x _ {i k}\right)\tag{16}
$$

where $x _ { i j }$ denotes the jth cluster's centroid for the ith particle. Step 3 Calculate <sup>fi</sup>tness value for each particle in order to adjust suitabilities.

$$
F i t n e s s v a l u e = \sum_ {j = 1} ^ {k} \left| \sum_ {\forall x \in c _ {i j}} \left\| x - z _ {i j} \right\| \right|\tag{17}
$$

where

k denotes the cluster number

x denotes data vectors to be clustered

$c _ { i j }$ denotes the number of data vectors of the ith particle in cluster j and

$\left| \left| x - z _ { i j } \right| \right|$ denotes the Euclidean distances between data vectors and cluster centroids

Table 2  
The parameter setup for each algorithm.

<table><tr><td colspan="2">PSOA related parameter setup</td></tr><tr><td></td><td>PSO clustering, PSKO algorithm, GA-PSO algorithm, and GA-PSKO algorithm</td></tr><tr><td>Number of particles</td><td>20</td></tr><tr><td>Number of generations</td><td>100</td></tr><tr><td>W</td><td>1.2 decrease to 0.4</td></tr><tr><td> $c_1$ and  $c_2$ </td><td>2</td></tr><tr><td> $X_{\text{max}}$ </td><td>Yes</td></tr><tr><td> $V_{\text{max}}$ </td><td>Yes</td></tr><tr><td colspan="2">GA related parameter setup</td></tr><tr><td></td><td>GA algorithms, GKA algorithm, GA-PSO algorithm, and GA-PSKO algorithm</td></tr><tr><td>Number of particles</td><td>20</td></tr><tr><td>Number of generations</td><td>100</td></tr><tr><td>Crossover rule</td><td>100% (one-point crossover)</td></tr><tr><td>Mutation probability</td><td>5%</td></tr><tr><td></td><td>HGAPSOA</td></tr><tr><td>Number of particles</td><td>10</td></tr><tr><td>Number of generations</td><td>100</td></tr><tr><td>W</td><td>1.2 decrease to 0.4</td></tr><tr><td> $c_1$ and  $c_2$ </td><td>2</td></tr><tr><td> $X_{\text{max}}$ </td><td>Yes</td></tr><tr><td> $V_{\text{max}}$ </td><td>Yes</td></tr><tr><td>Crossover rule</td><td>100% (one-point crossover)</td></tr><tr><td>Mutation probability</td><td>5%</td></tr></table>

![](/api/attachments/YMSZ348S/fulltext/images/52875724021b7967f4d0d261b520309d1005500aabf0fc24ba3d32a3a164c067.jpg)  
Fig. 4. The converged curves for Iris data.

(3a) Calculate the Euclidean distance $d ( x , z _ { i j } )$ to all cluster centroids according to the equation below:

$$
d (x, z _ {i j}) = \left\| x - z _ {i j} \right\|\tag{18}
$$

(3b) Assign x to cluster $z _ { i j }$ such that $d ( x , z _ { i j } ) = \tt M i n \forall { c } _ { 1 , \ldots , N c } \{ d ( x , z _ { i j } ) \} .$

(3c) Calculate the <sup>fi</sup>tness using Eq. (17)

Setp 4 Apply real-coded GA operators (reproduction, crossover and mutation) to the 2N population and create another 2N population.

(4a) Reproduction: From the population, select the 2N's best individuals according to <sup>fi</sup>tness.

(4b) Crossover: Apply two-parent crossover to update the 2N individuals.

(4c) Mutation: Apply mutation with 5% mutation probability to the 2N chromosomes according to the equation below:

$$
x ^ {\prime} = x + \text { rand } \times N (0, 1)\tag{19}
$$

Setp 5 Evaluate the <sup>fi</sup>tness of each of the 2N individuals. Rank them on the basis of the <sup>fi</sup>tness values.

Step 6 Update the global best $( P _ { g d } )$ and local best positions $( P _ { i d } ) _ { \ l }$

Setp 7 Crossover: Based on NPSO [39], we apply every $P _ { i d }$ and $P _ { g d }$ crossover and get two child particles, compare them and let the particle with smaller <sup>fi</sup>tness value be the <sup>fi</sup>nal child of the predecessors.

Step 8 (8a) Update the velocity $( V _ { i d } )$ using Eq. (20).

$$
\begin{array}{c} V _ {\text {old}} ^ {\text {new}} = W \times V _ {i d} ^ {\text {old}} + c _ {1} \times r a n d _ {1} \times \left(P _ {i d} - X _ {i d} ^ {\text {old}}\right) \\ + c _ {2} \times r a n d _ {2} \times \left(P _ {g d} - X _ {i d} ^ {\text {old}}\right) \end{array}\tag{20}
$$

where

$c _ { 1 }$ and $c _ { 2 }$ are two positive constant ran $d _ { 1 }$ and $r a n d _ { 2 }$ are two random functions in the range [0,1] and

![](/api/attachments/YMSZ348S/fulltext/images/987e35f5bb1182185ce3dd8aa075a0d356b8c01fe8173967062590be5d26bb54.jpg)  
Fig. 5. The converged curves for Wine data.

![](/api/attachments/YMSZ348S/fulltext/images/50f9be68c9eccaaaad8079e74c25fe6ac21d16a447e1ab3a5ec3406c1f8ee0f4.jpg)  
Fig. 6. The converged curves for Vowel data.

W is the inertia weight.

(8b) Mutation: Update the $V _ { i d }$ utilizing Eq. (21).

$$
V _ {o l d} ^ {n e w ^ {\prime}} = V _ {o l d} ^ {n e w} + r a n d \times N (0, 1)\tag{21}
$$

Step 9 (9a) Update the position vector $( X _ { i d } )$ of the top N individuals using Eq. (22).

$$
X _ {i d} ^ {n e w} = X _ {i d} ^ {o l d} + V _ {i d} ^ {n e w}\tag{22}
$$

(9b) Mutation: Update the $X _ { i d }$ of the top N individuals utilizing Eq. (23).

$$
X _ {i d} ^ {n e w ^ {\prime}} = X _ {i d} ^ {o l d} + r a n d \times N (0, 1)\tag{23}
$$

Step 10 Apply K-means operators to the 2N population and create another 2N population using Eq. (24).

$$
z _ {i j} = \frac {1}{c _ {i j}} \sum_ {\forall x \in c _ {i j}} x\tag{24}
$$

Step 11 If one of the stopping criteria is satis<sup>fi</sup>ed then go to Step 12. Otherwise, go to Step 3.

Step 12 Output the particle with the minimum <sup>fi</sup>tness value in the last generation.

Fig. 3 illustrates the computation <sup>fl</sup>owchart of HGAPSOA.

## 3.3.4. Algorithm validation

To examine HGAPSOA's performance, this study compares various clustering methods with the proposed clustering algorithm. These algorithms include GA [42], GKA [31], PSO [44], PSKO (Kuo et al.,

![](/api/attachments/YMSZ348S/fulltext/images/a31eafbb54c705aff32d12bec5287c8edb13a877981eb9c19d54b27f7a6fe36f.jpg)  
Fig. 7. The converged curves for Glass data

<table><tr><td rowspan="3">Data set</td><td colspan="13">Algorithm</td></tr><tr><td colspan="2">GA</td><td colspan="2">GKA</td><td colspan="2">PSO</td><td colspan="2">PSKO</td><td colspan="2">GA-PSO</td><td colspan="2">GA-PSKO</td><td>HGAPSOA</td></tr><tr><td>Average</td><td>Best</td><td>Average</td><td>Best</td><td>Average</td><td>Best</td><td>Average</td><td>Best</td><td>Average</td><td>Best</td><td>Average</td><td>Best</td><td>Average</td></tr><tr><td>Iris</td><td>29.835 + 1.657</td><td>29.180</td><td>29.262 + 0.016</td><td>29.235</td><td>29.790 + 0.240</td><td>29.523</td><td>29.206 + 0.006</td><td>29.128</td><td>35.375 + 2.032</td><td>31.682</td><td>29.226 + 0.011</td><td>29.212</td><td>29.190 + 0.008</td></tr><tr><td>Glass</td><td>52.465 + 1.288</td><td>50.529</td><td>51.769 + 2.323</td><td>49.859</td><td>57.485 + 2.045</td><td>54.089</td><td>50.021 + 0.738</td><td>49.604</td><td>59.132 + 1.718</td><td>56.633</td><td>51.268 + 0.816</td><td>50.378</td><td>49.710 + 0.286</td></tr><tr><td>Vowel</td><td>391.611 + 5.155</td><td>380.665</td><td>363.487 + 1.240</td><td>361.786</td><td>421.443 + 6.035</td><td>410.691</td><td>386.578 + 21.567</td><td>362.431</td><td>446.479 + 6.498</td><td>428.878</td><td>394.069 + 7.728</td><td>377.568</td><td>362.449 + 0.788</td></tr><tr><td>Wine</td><td>93.129 + 3.734</td><td>89.862</td><td>88.712 + 0.007</td><td>88.695</td><td>97.885 + 5.242</td><td>92.236</td><td>88.695 + 4.34E-14</td><td>88.695</td><td>111.943 + 4.948</td><td>104.388</td><td>88.695 + 4.336E-14</td><td>88.695</td><td>88.671 + 0.009</td></tr></table>

Clustering results for seven algorithms. Table 3

Table 4  
The multivalence test in Iris data set.

<table><tr><td>Data set: Iris</td><td>HGAPSOA vs. PSO</td><td>HGAPSOA vs. PSKO</td><td>HGAPSOA vs. GA</td><td>HGAPSOA vs. GKA</td><td>HGAPSOA vs. GA-PSO</td><td>HGAPSOA vs. GA-PSKO</td></tr><tr><td>Mann-Whitney U</td><td>.000</td><td>51.000</td><td>64.000</td><td>.000</td><td>.000</td><td>.000</td></tr><tr><td>Wilcoxon W</td><td>465.000</td><td>516.000</td><td>529.000</td><td>465.000</td><td>465.000</td><td>465.000</td></tr><tr><td>Z</td><td>-6.653</td><td>-5.913</td><td>-5.707</td><td>-6.661</td><td>-6.653</td><td>-6.656</td></tr><tr><td>Asymp.sig.(2-tailed)</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td></tr></table>

2008), GA-PSO [13] and GA-PSKO. GA-PSKO is a clustering algorithm which combines GA-PSO with K-means.

## 4. Simulation

This section applies some benchmark data sets to assess the proposed algorithm, HGAPSOA, in comparison with GA, GKA, PSO, PSKO, GA-PSO and GA-PSKO. A detailed discussion is presented as follows.

## 4.1. Data set

This section adopts four data sets provided by the website of the Department of Information and Computer Science, University of California (http://archive.ics.uci.edu/ml/datasets.html). Table 1 lists the corresponding information including data set name, number of data, number of features, and number of clusters, for each data set.

## 4.2. Data preprocessing and parameter setup

The features in each data set may have different value ranges. If these ranges are quite different from each other, then even a good clustering algorithm still cannot obtain good clustering results. Thus, this study normalizes raw data into the same value range. The basic goal of normalization is to <sup>fi</sup>nd the largest and smallest values for each feature. And then each data in the feature is divided by the difference of the largest and smallest values. Basically, this is a very common normalization method.

It is necessary to determine the parameter values for our proposed HGAPSOA and other clustering algorithms. We can easily classify them into three categories, PSOA-based algorithm, GA-based algorithm and HGAPSOA. The corresponding information is summarized in Table 2.

## 4.3. Algorithm evaluation indicator

Although mean square error (MSE), or within variance, is a commonly used indicator for evaluating clustering ef<sup>fi</sup>ciency, we employed the sum of Euclidean distances (SED), as presented by Kaufman and Rousseuw [29], since they showed that SED is more robust than MSE in evaluating clustering results. Basically, the smaller the SED is, the better the result, and SED is represented as:

$$
S E D = \sum_ {i = 1} ^ {n} \sum_ {j = 1, x _ {i} \in c _ {j}} ^ {k} d \left(x _ {i}, m _ {j}\right)\tag{25}
$$

where

$$
\begin{array}{l l} n & \text { total   number   of   data, } \\ C _ {j} & \text { the   jth   cluster, } \end{array}
$$

K the number of clusters, D Euclidean distance, $x _ { i }$ the dimension of the ith data, and $m _ { j }$ the coordinate of the jth cluster's center.

## Table 5

## 4.4. Result analysis

## 4.4.1. Converge speed analysis

Figs. 4 to 7 illustrate the converged curves for four data sets, respectively. The proposed method integrates the Improved PSOA, GA and K-means algorithm. Thus, Improved PSOA has better-performing $P _ { i d }$ and $P _ { g d }$ which leads all particles to search for the optimum solution. Moreover, the K-means converges fast. As a result, HGAPSOA can converge without exceeding 20 iterations. Also, it can converge faster than the other six methods, GA, GKA, PSO, PSKO, GA-PSO and GA-PSKO.

## 4.4.2. Clustering accuracy analysis

In this study, we select SED as the performance indicator and a smaller SED value indicates better performance. In addition, each experiment is conducted thirty times and the average and standard deviation are calculated as the <sup>fi</sup>nal result. The average SED and the corresponding standard deviation for each experiment are listed in Table 3.

Among these seven clustering algorithms, the proposed method, HGAPSOA, has the best performance in four data sets, including iris, wine, vowel, and glass. By examining the computational results for thirty runs, we found that HGAPSOA overcomes the problem of premature convergence.

## 4.4.3. Multivalence test

In order to verify the difference of the average value between HGAPSOA and other clustering algorithms, we apply Mann–Whitney U to test the difference at a 95% con<sup>fi</sup>dence level. The null hypothesis is listed as follow:

Ho The average value of two independent samples has no difference.

H1 The average value of two independent samples has difference.

The Cochran test statistic is as follows:

$$
Z = \frac {U - \frac {n _ {1} (n _ {1} + n _ {2} + 1)}{2}}{\sqrt {\frac {1}{1 2} n _ {1} n _ {2} (n _ {1} + n _ {2} + 1)}}, U = \left| U _ {1}, U _ {2} \right|\tag{26}
$$

where $\begin{array} { r } { U _ { 1 } = n _ { 1 } n _ { 2 } - \frac { n _ { 1 } ( n _ { 1 } + 1 ) } { 2 } - W _ { 1 } } \end{array}$ and $\begin{array} { r } { U _ { 2 } = n _ { 1 } n _ { 2 } - \frac { n _ { 2 } ( n _ { 2 } \ + \ 1 ) } { 2 } - W _ { 2 } . } \end{array}$

The test results are listed in Tables 4 to 7 and show that HGAPSOA mostly shows the difference (Pb0.05). Thus we could conclude that HGAPSOA has more remarkable performance than other methods.

The multivalence test in Glass data set

<table><tr><td>Data set: Glass</td><td>HGAPSOA vs. PSO</td><td>HGAPSOA vs. PSKO</td><td>HGAPSOA vs. GA</td><td>HGAPSOA vs. GKA</td><td>HGAPSOA vs. GA-PSO</td><td>HGAPSOA vs. GA-PSKO</td></tr><tr><td>Mann-Whitney U</td><td>.000</td><td>234.000</td><td>2.000</td><td>44.000</td><td>.000</td><td>3.000</td></tr><tr><td>Wilcoxon W</td><td>465.000</td><td>699.000</td><td>467.000</td><td>509.000</td><td>465.000</td><td>468.000</td></tr><tr><td>Z</td><td>-6.653</td><td>-3.194</td><td>-6.623</td><td>-6.003</td><td>-6.653</td><td>-6.609</td></tr><tr><td>Asymp.sig.(2-tailed)</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td></tr></table>

Table 6  
The multivalence test in vowel data set.

<table><tr><td>Data set: Vowel</td><td>HGAPSOA vs. PSO</td><td>HGAPSOA vs. PSKO</td><td>HGAPSOA vs. GA</td><td>HGAPSOA vs. GKA</td><td>HGAPSOA vs. GA-PSO</td><td>HGAPSOA vs. GA-PSKO</td></tr><tr><td>Mann-Whitney U</td><td>.000</td><td>20.000</td><td>.000</td><td>196.000</td><td>.000</td><td>.000</td></tr><tr><td>Wilcoxon W</td><td>465.000</td><td>485.000</td><td>465.000</td><td>661.000</td><td>465.000</td><td>465.000</td></tr><tr><td>Z</td><td>-6.653</td><td>-6.357</td><td>-6.653</td><td>-3.755</td><td>-6.653</td><td>-6.653</td></tr><tr><td>Asymp.sig.(2-tailed)</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td></tr></table>

## 5. Model evaluation results

Section 4 has demonstrated the capability of the proposed HGAPSOA to outperform GA, GKA, PSO, PSKO, GA-PSO and GA-PSKO. This section applies HGAPSOA for order clustering in order to reduce SMT production system setup time. Advantech Company provided the related data for assessment. The setup of production line-change for different orders has become a critical bottleneck in SMT production systems because it is very time consuming in production line-change to implement material-preparation and material-binding tasks by hand. Failure to complete this process prior to the start of production of the next order causes machine idle time and results in low production capability utilization. Therefore, we apply a two-stage clustering method [34] to group similar products or orders together and <sup>fi</sup>nd the same materials (shared materials) that will be used for all the products in the same group. This enables the production engineers to put the same needed materials in the same material positions for SMT retrieval equipment, so production engineers can arrange for similar products to be produced together. Thus, the material-preparation operation can be simpli<sup>fi</sup>ed in order to reduce SMT setup time.

## 5.1. Order clustering system framework

The main procedures of the order clustering system framework are illustrated in Fig. 8.

A material report is provided by an industrial PC company. Using ACCESS SQL query, there are a total of 2826 different products, or orders, and a total of 2516 materials used. In order to cluster these products, it is necessary to <sup>fi</sup>lter the noise of the products and material data and then transform them into a 2826×2516 two-dimensional matrix.

## 5.2. Data preprocessing

Since there are 2516 features for the product feature matrix, it is very time consuming for clustering analysis with so many features. In order to reduce the computational time while also maintaining solution quality, this study uses Matlab 7.0 to make the principle component analysis for the product feature matrix in order to extract the dimensions for the principle component factors. The selection of factors is based on the Eigenvalue which should be larger than 1. After analysis, there are a total of 200 principle component factors. The cumulative explanation variance is 81.98%.

Principle component analysis reduces the original feature matrix to a size of 2826×2516 to 2826×200. The proposed method, ART2+ HGAPSOA algorithm can be applied for clustering analysis. These two parts are shown in the following subsections.

## 5.3. Clustering analysis

In order to apply our proposed clustering algorithm, HGAPSOA, it is necessary to know the number of clusters in advance. Based on our previous research [34], this study applies a two-stage clustering method, ART2+ HGAPSOA which is a kind of method that processes gray value in the <sup>fi</sup>rst stage, ART2 automatically <sup>fi</sup>nds the number of clusters, while the second stage uses the HGAPSOA algorithm to <sup>fi</sup>nd the <sup>fi</sup>nal solution.

## 5.3.1. Determination of cluster number

The ART2 algorithm was coded by using Matlab 7.0. Since the number of clusters in ART2 algorithm is determined by the vigilance value, once it is well determined, ART2 can automatically cluster the data. Thereafter, the second stage employs GA, GKA, PSO, PSKO, GA-PSO, GA-PSKO and HGAPSOA to <sup>fi</sup>nd the <sup>fi</sup>nal solutions. Since the vigilance value dramatically affects the clustering outcome, this study uses Wilk's Lambda value as the indicator for determining the number of clusters. Wilk's Lambda is frequently applied by MANOVA as the indicator for determining the number of clusters. If Wilk's Lambda value suddenly increases in two different numbers of clusters, then the number of clusters prior to variance can be treated as the best number of clusters. Theoretically, Wilk's Lambda value is de<sup>fi</sup>ned as:

$$
W i l k ^ {\prime} s L a m b d a = \frac {S S _ {w i t h i n}}{S S _ {t o t a l}}\tag{27}
$$

where $S S _ { \mathrm { w i t h i n } }$ and $S S _ { \mathrm { t o t a l } }$ are the within-cluster and total variances, respectively.

We set up different vigilance values to obtain different cluster numbers from 30 to 80. Fig. 9 depicts the corresponding Wilk's Lambda values for different vigilance values. If the incremental range is 10, cluster numbers from 50 to 60 have sudden variance in Wilk's Lambda value. For further investigation, from cluster 55 to 57, there is also similar phenomenon. Thus, cluster number 57 is the best number of clusters.

## 5.3.2. Comparison of different clustering algorithms

Based on the ART2 algorithm's result, GA, GKA, PSO, PSKO, GA-PSO, GA-PSKO and HGAPSOA are further used to <sup>fi</sup>nd the <sup>fi</sup>nal solution for comparison. Table 8 depicts the sum of Euclidean distances (SEDs) of these algorithms. Each algorithm is run ten times and average and standard deviation are calculated, respectively. Table 8 indicates that the ART2+ HGAPSOA has the smallest SED value, 2234.629.

## 5.4. Shared materials

According to the clustering results of ART2+ HGAPSOA, the products are grouped into <sup>fi</sup>fty seven clusters. The corresponding number of products and number of shared materials for these clusters with the number of shared materials over one hundred are presented in Table 9.

Table 7  
The multivalence test in Wine data set

<table><tr><td>Data set: Wine</td><td>HGAPSOA vs. PSO</td><td>HGAPSOA vs. PSKO</td><td>HGAPSOA vs. GA</td><td>HGAPSOA vs. GKA</td><td>HGAPSOA vs. GA-PSO</td><td>HGAPSOA vs. GA-PSKO</td></tr><tr><td>Mann-Whitney U</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td></tr><tr><td>Wilcoxon W</td><td>465.000</td><td>465.000</td><td>465.000</td><td>465.000</td><td>465.000</td><td>465.000</td></tr><tr><td>Z</td><td>-6.654</td><td>-7.112</td><td>-6.653</td><td>-6.655</td><td>-6.653</td><td>-7.112</td></tr><tr><td>Asymp.sig.(2-tailed)</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td><td>.000</td></tr></table>

![](/api/attachments/YMSZ348S/fulltext/images/f659663bd74db80baffb4a8d6f05b5a7e165eec42c2555224b61e880752ad211.jpg)  
Fig. 8. Order clustering system.

## 5.5. Order classification

A feedforward neural network with an error backpropagation learning algorithm will learn the clustering results from ART2+ HGAPSOA. Since there are a total of 2516 data, they are divided into 1696 training samples, 564 testing samples, and 565 evaluation samples. The network topology includes 200 input nodes and 57 output nodes, respectively. Regarding the number of hidden nodes, trial and error method is applied. After testing, the hidden layer with 179 nodes has the lowest mean square error as the training rate and momentum rate are 0.5 and 0.9, respectively.

## 5.6. Performance evaluation for production line-changes

This study simulates production line-change ef<sup>fi</sup>ciency through the on-<sup>fi</sup>eld collection of the production plan. In order to simplify the variables which may occur in the practical applications, this study makes the following assumptions:

1. There is no stock-out condition.

2. The machines do not have problems of shutdown or malfunction.

3. There is no human error (e.g. material-binding error or materialpreparation miss) which may affect the production plan during the material-preparation process of material-preparation work.

Through job-shop measuring, the material-binding per material is 50 s, while material-preparation time is 0.5 h. Table 10 lists the production plan for the SMT production line from May 4, 2005 to May 5, 2005. These orders' corresponding clusters are listed as well.

According to our assumptions, the actual production time consists of two parts: material-binding time and mounting time. In addition, it should be noted that all the boards produced by the SMT need to <sup>fi</sup>rst implement the material-binding operation, which is then followed by the mounting operation. In other words, if the material-binding operation is completed as the next product is going to be produced, then the product can be smoothly mounted; otherwise, mounting cannot be started until the material-binding operation is completed. However, this would result in machine idle time.

Next, two scheduling rules, <sup>fi</sup>rst-come <sup>fi</sup>rst-served (FCFS) and shortest processing time (SPT), are applied for production scheduling in order to evaluate the proposed ART2+ HGAPSOA's performance.

## 5.6.1. Production model before improvement

5.6.1.1. FCFS. Using the FCFS rule for scheduling the production process before improvement, the material-preparation time is 23.9 h, while the total production time is 34.3 h. In addition, the total machine idle time is $2 . 8 ( 0 . 5 + 0 . 7 + 1 . 6 )$ h.

![](/api/attachments/YMSZ348S/fulltext/images/b988450942bc99c2ef27ef650afc84e72827b4578c08e1ffaae693af45b2bc30.jpg)

![](/api/attachments/YMSZ348S/fulltext/images/45d5fe9c09aa03fe7da5a46ebe89c562169a7e3a6cb214de6875ea32e79cbb75.jpg)  
Fig. 9. Wilk's Lambda values

Table 10  
Table 9  
Table 8  
The SED values for every clustering algorithms.

<table><tr><td colspan="8">Average and standard deviation results of SED For 10 runs</td></tr><tr><td>Algorithms</td><td>ART2 ± GA</td><td>ART2 ± GKA</td><td>ART2 ± PSO</td><td>ART2 ± PSKO</td><td>ART2 ± GA-PSO</td><td>ART2 ± GA-PSKO</td><td>ART2 ± HGAPSOA</td></tr><tr><td>Average and standard deviation</td><td>3403.891 ± 103.856</td><td>2247.473 ± 30.480</td><td>2336.318 ± 16.589</td><td>2331.605 ± 19.064</td><td>2321.627 ± 19.511</td><td>2329.585 ± 17.657</td><td>2234.629 ± 18.606</td></tr><tr><td>Best solution</td><td>3305.202</td><td>2209.569</td><td>2308.792</td><td>2295.650</td><td>2284.499</td><td>2300.389</td><td>2201.899</td></tr></table>

5.6.1.2. SPT. Similarly, using the SPT rule to schedule the production process before improvement, the material-preparation time is 23.9 h. Total production time and total machine idle time are 34.9 h and 5.6 $( 0 . 5 + 0 . 6 + 2 . 1 + 1 . 1 + 0 . 8 + 0 . 5 )$ h, respectively.

## 5.6.2. Production model after improvement

This subsection employs ART2+ HGAPSOA to classify the orders <sup>fi</sup>rst and arrange that the orders belonging to the same cluster are scheduled together. Table 9 indicates that cluster 2 and cluster 24 have 111 shared materials and 183 shared materials. Due to effect of shared materials, the shared materials only need to be prepared once. This can save material-preparation time and reduce the SMT linechange time.

5.6.2.1. FCF. Using the FCFS rule to schedule the production process after improvement, the material-preparation time is 19.7 h, while the total production time and total machine idle time are 31.5 h and 0 h.

5.6.2.2. SPT. The material-preparation time, total production time and total machine idle time are 19.9 h, 31.3 h, and $2 ( 0 . 1 + 1 + 0 . 3 + 0 . 6 ) \mathrm { h } ,$ respectively.

For the purpose of comparison, the above results are summarized in Table 11. This indicates that the material-preparation time is reduced from 23.9 h to 19.9 h. This is a 16.74% decrease. In regard to total production time, there are 8.16% and 10.32% decreases with the FCFS rule and the SPT rule, respectively. The effect on total machine idle time is especially dramatic. The FCFS rule improved from 2.8 h to 0 h, while it improved from 5.6 h to 2 h for SPT. Thus, no matter what kind of scheduling rules is employed, using clustering analysis to arrange similar orders together really does save production time and idle time.

## 6. Conclusions

This study has proposed a two-stage clustering algorithm, ART2+ HGAPSOA, for clustering analysis. The simulation results have shown that HGAPSOA outperforms GA, GKA, PSO, PSKO, GA-PSO and GA-PSKO algorithms in four data sets.

Some clusters and their corresponding numbers of shared materials.

<table><tr><td>Cluster</td><td>Number of products</td><td>Number of shared materials</td><td>Cluster</td><td>Number of products</td><td>Number of shared materials</td></tr><tr><td>2</td><td>16</td><td>111</td><td>30</td><td>5</td><td>133</td></tr><tr><td>3</td><td>6</td><td>112</td><td>31</td><td>18</td><td>158</td></tr><tr><td>6</td><td>6</td><td>101</td><td>32</td><td>2</td><td>157</td></tr><tr><td>8</td><td>8</td><td>110</td><td>34</td><td>13</td><td>148</td></tr><tr><td>15</td><td>3</td><td>155</td><td>37</td><td>13</td><td>128</td></tr><tr><td>16</td><td>8</td><td>158</td><td>38</td><td>38</td><td>106</td></tr><tr><td>18</td><td>11</td><td>134</td><td>39</td><td>36</td><td>101</td></tr><tr><td>21</td><td>30</td><td>143</td><td>44</td><td>12</td><td>106</td></tr><tr><td>24</td><td>6</td><td>183</td><td>45</td><td>6</td><td>117</td></tr><tr><td>25</td><td>15</td><td>112</td><td>48</td><td>16</td><td>120</td></tr><tr><td>26</td><td>35</td><td>130</td><td>51</td><td>38</td><td>131</td></tr><tr><td>27</td><td>32</td><td>109</td><td>57</td><td>21</td><td>137</td></tr></table>

Two-day production plan of SMT production system.

<table><tr><td colspan="4">Original production system</td><td colspan="4">Improved production system</td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td></tr><tr><td>1</td><td>9498968300</td><td>70</td><td> $4.9 = 4.4 + 0.5$ </td><td>4.4</td><td>27</td><td>188</td><td> $2.6 = 188 \times (50/60/60)$ </td></tr><tr><td>2</td><td>9496064000</td><td>10</td><td> $1.2 = 0.7 + 0.5$ </td><td>0.7</td><td>27</td><td>204</td><td> $2.8 = 204 \times (50/60/60)$ </td></tr><tr><td>3</td><td>9496074410</td><td>30</td><td> $2.6 = 2.1 + 0.5$ </td><td>2.1</td><td>38</td><td>205</td><td> $2.8 = 205 \times (50/60/60)$ </td></tr><tr><td>4</td><td>9496074430</td><td>15</td><td> $1.5 = 1 + 0.5$ </td><td>1</td><td>38</td><td>198</td><td> $2.8 = 198 \times (50/60/60)$ </td></tr><tr><td>5</td><td>9498968000</td><td>50</td><td> $3.6 = 3.1 + 0.5$ </td><td>3.1</td><td>27</td><td>186</td><td> $2.6 = 186 \times (50/60/60)$ </td></tr><tr><td>6</td><td>9493650000</td><td>96</td><td> $1.3 = 0.8 + 0.5$ </td><td>0.8</td><td>17</td><td>26</td><td> $0.4 = 26 \times (50/60/60)$ </td></tr><tr><td>7</td><td>9493650010</td><td>96</td><td> $2.5 = 2 + 0.5$ </td><td>2</td><td>17</td><td>63</td><td> $0.9 = 63 \times (50/60/60)$ </td></tr><tr><td>8</td><td>9498968600</td><td>35</td><td> $1.6 = 1.1 + 0.5$ </td><td>1.1</td><td>1</td><td>95</td><td> $1.3 = 95 \times (50/60/60)$ </td></tr><tr><td>9</td><td>9496687102</td><td>40</td><td> $2.5 = 2 + 0.5$ </td><td>2</td><td>28</td><td>149</td><td> $2.1 = 194 \times (50/60/60)$ </td></tr><tr><td>10</td><td>9496074210</td><td>110</td><td> $8.1 = 7.6 + 0.5$ </td><td>7.6</td><td>14</td><td>205</td><td> $2.8 = 205 \times (50/60/60)$ </td></tr><tr><td>11</td><td>9496074230</td><td>60</td><td> $4.6 = 4.1 + 0.5$ </td><td>4.1</td><td>14</td><td>201</td><td> $2.8 = 201 \times (50/60/60)$ </td></tr></table>

A: Production sequence.  
B: Product type.  
C: Quantity.  
D: Predicted labor time (h)=mounting time+material-preparation time.  
E: Mounting time (h).  
F: Cluster belonged.  
G: Number of materials used.  
H: Material-binding time (h)=number of materials used×per material-binding time.

Model evaluation results.

<table><tr><td></td><td>Scheduling rule</td><td>Material-preparation time (h)</td><td>Total production time (h)</td><td>Machine idle time (h)</td></tr><tr><td rowspan="2">FCFS</td><td>Before improvement</td><td>23.9</td><td>34.3</td><td>2.8</td></tr><tr><td>After improvement</td><td>19.9</td><td>31.5</td><td>0</td></tr><tr><td rowspan="2">SPT</td><td>Before improvement</td><td>23.9</td><td>34.9</td><td>5.6</td></tr><tr><td>After improvement</td><td>19.9</td><td>31.3</td><td>2</td></tr></table>

The proposed method was also applied to cluster orders to improve production performance. The model evaluation results show that both production time and machine idle time can be reduced since similar products are scheduled for production together. The production engineers can simplify the binding process since only different materials in the same cluster should be bound during product change. The results show that the machine idle time decreases from 2.8 h to 0 h for the FCFS rule and from 5.6 h to 2 h for SPT rule. In addition, total production time has around 8.16% decrease for FCFS rule and 10.32% decrease for the SPT rule. Thus, if the proposed method can be integrated with other advanced scheduling methods, the improvements in performance can be more signi<sup>fi</sup>cant.

A possible direction for future research would be to adopt different updating rules in order to get more adequate results. Furthermore, combining Tabu search clustering or simulated annealing clustering algorithms may be feasible. From the two-stage point of view, other clustering algorithms like the adaptive double SOM network can be used to decide the number of clusters. The proposed algorithm can also be utilized for many different areas of applications, like customer relationship management, market segmentation, and others.

## Acknowledgements

This study was supported by the National Science Council of the Taiwan Government under contract number NSC 96-2416-H-011-018- MY3. The support is greatly appreciated. In addition, acknowledgements are owed to the case company for providing the related data.

## References

[1] K. Al-Sultan, A Tabu search approach to the clustering problem, Pattern Recognition 28 (9) (1995) 1443–1451.

[2] Khaled S. Al-Sultan, Khan M. Maroof, Computational experience on four algorithms for the hard clustering problem, Pattern Recognition Letters 17 (3) (1996) 295–308 March 6.

[3] G. Ball, D. Hall, A clustering technique for summarizing multivariate data, Behavioral Science 12 (1967) 153–155.

[4] F. van den Bergh, A.P. Engelbrecht, A new locally convergent particle swarm optimiser, Proceedings of IEEE International Conference on Systems,Man and Cybernetics, 3, 2002.

[5] J. Bezdek, A convergence theorem for the fuzzy ISO-DATA clustering algorithm, IEEE Transactions on Pattern Analysis and Machine Intelligence 2 (1980) 1–8.

[6] J. Bezdek, R. Hathaway, Numerical convergence and interpretation of the fuzzy cshells clustering algorithms, IEEE Transactions on Neural Networks 3 (5) (1992) 787–793.

[7] G. Carpenter, S. Grossberg, A massively parallel architecture for a self-organizing neural pattern recognition machine, Computer Vision, Graphics, and Image Processing 37 (1987) 54–115.

[8] G. Carpenter, S. Grossberg, ART2: self-organization of stable category recognition codes for analog input patterns, Applied Optics 26 (23) (1987) 4919–4930.

[9] G. Carpenter, S. Grossberg, D. Rosen, Fuzzy ART: fast stable learning and categorization of analog patterns by an adaptive resonance system, Neural Networks 4 (1991) 759–771.

[10] C.Y. Chen, F. Ye, Particle swarm optimization algorithm and its application to clustering analysis, IEEE International Conference on Networking, sensing and Control (2004) 789–794.

[11] M. Clerc, The swarm and the queen: towards a deterministic and adaptive particle swarm optimization, Evolutionary Computation (1999) 1951–1957.

[12] S.C.M. Cohen, L.N. de Castro, Data clustering with particle swarms, IEEE Congress on Evolutionary Computations (2006) 1792–1798.

[13] S. Du, W. Li, K. Cao, A learning algorithm of arti<sup>fi</sup>cial neural network based on GA-PSO, Proceedings of the 6th World Congress on Intelligent Control and Automation, 2006 Dalian, China.

[14] R. Eberhart, J. Kennedy, A new optimizer using particle swarm theory, Proceedings of the Sixth International Symposium on Micro Machine and Human Science, 1995, pp. 39–43.

[15] V. Estivill-Castro, I. Lee, AMOEBA: hierarchical clustering based on spatial proximity using Delaunay diagram, Proceedings 9th International Spatial Data Handling (SDH2000), 2000, pp. 10–12.

[16] V. Estivill-Castro, I. Lee, AUTOCLUST: automatic clustering via boundary extraction for massive point data sets, Proceedings 5th International Conference Geo-Computation, 2000, pp. 23–25.

[17] E. Forgy, Clustering analysis of multivariate data: ef<sup>fi</sup>ciency versus interpretability of classi<sup>fi</sup>cation, Biometrics 21 (1965) 768–769.

[18] I. Gath, A. Geva, Unsupervised optimal fuzzy clustering, IEEE Transactions on Pattern Analysis and Machine Intelligence 11 (7) (1989) 773–781.

[19] A.B. Geva, Hierarchical unsupervised fuzzy clustering, IEEE Transactions on Fuzzy Systems 7 (6)(1999) 723–733

[20] S. Guha, R. Rastogi, K. Shim, CURE: an ef<sup>fi</sup>cient clustering algorithm for large databases, Proceedings ACM SIGMOD International Conference Management of Data (1998) 73–84.

[21] S. Guha, R. Rastogi, K. Shim, ROCK: a robust clustering algorithm for categorical attributes, Information Systems 25 (5) (2000) 345–366.

[22] L. Hall, I. Özyurt, J. Bezdek, Clustering with a genetically optimized approach, IEEE Transactions on Evolutionary Computation 3 (2) (1999) 103–112.

[23] G. Hamerly, C. Elkan, Learning the K in K-means, Proceedings of 7th Annual Conference on Neural Information Processing Systems, 2003.

[24] J. Han, M. Kamber, Data Mining: Concepts and Techniques, 2nd ed.Morgan Kaufmann, 2006.

[25] J. Holland, Adaptation in Natural and Arti<sup>fi</sup>cial System, University of Michigan Press, Ann Arbor, MI, 1975.

[26] K. Huang, A synergistic automatic clustering technique (Syneract) for multispectral image analysis, Photogrammetric Engineering Remote Sensing 1 (1) (2002) 33–40.

[27] A.K. Jain, M.N. Murty, P.J. Flynn, Data clustering: a review, ACM Computing Surveys 31 (3) (1999) 264–323.

[28] G. Karypis, E. Han, V. Kumar, Chameleon: hierarchical clustering using dynamic modeling, IEEE Computer 32 (8) (1999) 68–75.

[29] L. Kaufman, P. Rousseeuw, Finding groups in data: an introduction to cluster analysis, Wiley (1990).

[30] T. Kohonen, The self-organizing map, Proceedings IEEE 78 (9) (1990) 1464–1480.

[31] K. Krishna, M.N. Murty, Genetic K-means algorithm, IEEE Transactions on Systems, Man, and Cybernetics 29 (3) (1999) 433–439.

[32] R. Krishnapuram, J. Keller, A possibilistic approach to clustering, IEEE Transactions Fuzzy Systems 1 (2) (1993) 98–110

[33] R.J. Kuo, K. Chang, S.Y. Chien, Integration of self-organizing feature maps and genetic-algorithm-based clustering method for market segmentation, Journal of Organizational Computing and Electronic Commerce 14 (1) (2004) 43–60

[34] R.J. Kuo, J.L. Liao, C. Tu, Integration of ART2 neural network and genetic K-means algorithm for analyzing Web browsing paths in electronic commerce, Decision Support Systems 40 (2) (2005) 355–374.

[35] R.J. Kuo, H.S. Wang, T.L. Hu, S.H. Chou, Application of ant K-means on clustering analysis in data mining, International Journal of Computers and Mathematics with Applications 50 (2005) 1709–1724 November–December.

[36] R.J. Kuo, Y.L. An, H.S. Wang, W.J. Chung, Integration of self-organizing feature maps neural network and genetic K-means algorithm for market segmentation, Expert Systems with Applications 30 (2) (February, 2006) 313–324.

[37] Kuo, R.J., Wang, M.J., and Huang, T.W., “An application of particle swarm optimization algorithm to clustering analysis”, Journal of Soft Computing, 2010. (in press), doi:10.1007/S00500-009-00539-5.

[38] C.Y. Lee, E.K. Antonsson, Dynamic partitional clustering using evolution strategies, The Third Asia-Paci<sup>fi</sup>c Conference on Simulated Evolution and Learning, 2000.

[39] Z. Lian, X. Gu, B. Jiao, A novel particle swarm optimization algorithm for permutation <sup>fl</sup>ow-shop scheduling to minimize makespan, Chaos, Solitons & Fractals 35 (5) (2008) 851–861

[40] Y.T. Lin, B.Y. Shiueng, A genetic approach to the automatic clustering problem, Pattern Recognition 34 (2) (2001) 415–424.

[41] A. Lorette, X. Descombes, J. Zerubia, Fully unsupervised fuzzy clustering with entropy criterion, International Conference on Pattern Recognition, 3, 2000, pp. 3998–4001.

[42] U. Maulik, S. Bandyopadhyay, Genetic algorithm-based clustering technique, Pattern Recognition 33 (9) (2000) 1455–1465.

[43] C.A. Murthy, N. Chowdhury, In search of optimal clusters using genetic algorithms, Pattern Recognition Letters 17 (8) (1996) 825–832.

[44] D.W. van der Merwe, A.P. Engelbrecht, Data clustering using particle swarm optimization, The Congress on Evolutionary Computation (2003) 215–220.

[45] M.G.H. Omran, A. Salman, A.P. Engelbrecht, Dynamic clustering using particle swarm optimization with application in image segmentation, Pattern Analysis and Applications 8 (2006) 332–344.

[46] D. Pelleg, A. Moore, X-means: extending K-means with ef<sup>fi</sup>cient estimation of the number of clusters, Proceedings of the 17th International Conference on Maching Learning, Morgan Kaufmann, San Francisco, CA, 2000 pp. 727–734.

[47] Y. Shi, R. Eberhart, A modi<sup>fi</sup>ed particle swarm optimizer, Proceedings of the IEEE International Conference on Evolutionary Computation (1998) 69–73

[48] Y. Shi, R. Eberhart, Parameter Selection in Particle Swarm Optimization, Evolutionary Programming, New York, 1998 pp. 591–600.

[49] X. Xiao, E.R. Dow, R. Eberhart, Z.B. Miled, R.J. Oppelt, Gene clustering using selforganizing maps and particle swarm optimization, Proceedings of the International Parallel and Distributed Processing Symposium, 2003, pp. 22–28.

[50] R. Xu, D. Wunsch, Survey of clustering algorithms, IEEE Transactions on Neural Networks 16 (3) (2005) 645–678.

[51] T. Zhang, R. Ramakrishnan, M. Livny, BIRCH: an ef<sup>fi</sup>cient data clustering method for very large databases, Proceedings ACM SIGMOD Conference Management of Data (1996) 103–114.

[52] B. Zhao, C.X. Guo, B.R. Bai, Y.J. Cao, An improved particle swarm optimization algorithm for unit commitment, International Journal of Electrical Power & Energy Systems 28 (7) (2006) 482–490.

![](/api/attachments/YMSZ348S/fulltext/images/bce4dfa9dfcbfa1d59601d2b29b35c0401681d31d6e7049682d8101385c25ae8.jpg)  
R.J. Kuo received the MS degree in Industrial and Manufacturing Systems Engineering from Jowa State University, Ames, IA, in 1990 and the PhD degree in Industrial and Management Systems Engineering from the Pennsylvania State University, University Park, PA, in 1994. Currently, he is a Professor in the Department of Industrial Management at National Taiwan University of Science and Technology, Taiwan. His research interests include architecture issues of computational intelligence and their applications in forecasting, electronic business, logistics, supply chain management and decision support systems.

![](/api/attachments/YMSZ348S/fulltext/images/b5ed73c1339b7becb7152f4a2b6e23fce1628218ed963fe67f81057811548ec7.jpg)

L.M. Lin received the MS degree in Industrial Engineering and Management from National Taipei University of Technology, Taiwan. Currently, she is an engineer of AU Optronics Corporation Taiwan. Her research interests include architecture issues of computational intelligence and their applications in production management.
