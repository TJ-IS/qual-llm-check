---
otero_id: 12932
otero_key: "4TGS6395"
title: "Towards high dimensional instance selection: An evolutionary approach"
authors: "Chih-Fong Tsai; Zong-Yao Chen"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.01.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Chih-Fong Tsai ⁎, Zong-Yao Chen

Department of Information Management, National Central University, Taiwan

## a r t i c l e i n f o

Article history: Received 28 March 2013 Received in revised form 23 December 2013 Accepted 28 January 2014 Available online 5 February 2014

Keywords: Data reduction Instance selection Data mining Machine learning Genetic algorithms High dimensional data

## a b s t r a c t

Data reduction is an important data pre-processing step in the KDD process. It can be approached by the application of some instance selection algorithms to <sup>fi</sup>lter out unrepresentative or noisy data from a given (training) dataset. However, the performance of instance selection over very high dimensional data has not yet been fully examined. In this paper, we introduce a novel ef<sup>fi</sup>cient genetic algorithm (EGA), which <sup>fi</sup>ts “biological evolution” into the evolutionary process. In other words, after long-term evolution, individuals <sup>fi</sup>nd the most ef<sup>fi</sup>cient way to allocate resources and evolve. The experimental study is based on four very high dimensional datasets ranging from 200 to 18,236 dimensions. In addition, four state-of-the-art algorithms including IB3, DROP3, ICF, and GA are compared with EGA. The experimental results show that EGA allows the k-NN and SVM classi<sup>fi</sup>ers to provide the most comparable classi<sup>fi</sup>cation performance with the baseline classi<sup>fi</sup>ers without instance selection. Particularly, EGA outperforms the four algorithms in terms of average classi<sup>fi</sup>cation accuracy. Moreover, EGA can produce the largest reduction rates (the same as GA) and it requires relatively less computational time than the other four algorithms

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Nowadays, the datasets collected for some speci<sup>fi</sup>c domains tend to be very large (containing a huge amount of data) and complex (containing a very large number of variables or features), which leads to the so-called ‘big data’ problem [17]. Consequently, data reduction, as a data pre-processing task has became one of the most important steps in data mining or knowledge discovery in databases (KDD). Data reduction is aimed at shrinking the size of the collected dataset to facilitate the later mining analysis step, i.e., model development.

In other words, if the chosen dataset contains too many instances (i.e., data samples) it can result in large memory requirements, slow execution speed, and over-sensitivity to noise. In addition, one problem with using the original data points is that there may not be any located at the precise points that would make for the most accurate and concise concept description [27].

To this end, instance selection can be utilized to <sup>fi</sup>lter out noisy (or unrepresentative) data, which are likely to degrade the data mining performance, from a given dataset [20,30]. The size of the dataset is reduced when some noisy data are removed by a speci<sup>fi</sup>c instance selection algorithm. After this, data mining algorithms can be applied to the reduced dataset, to achieve suf<sup>fi</sup>cient results if the selection strategy is appropriate [28].

Let us now discuss instance selection. Given a dataset D composed of training set T and testing set U, let S T be the subset of selected instances resulting from the execution of an instance selection algorithm. Then, U is used to test a classi<sup>fi</sup>cation technique trained by S [4,6].

A better algorithm can select better quality data from T, which in turn would make the classi<sup>fi</sup>er trained by the reduced dataset S perform better than one trained by T alone, or other reduced datasets containing lower quality data produced by other algorithms. The number of selected instances in the reduced dataset (selected by a better (or effective) algorithm) would not necessarily be smaller than the ones selected by other algorithms. In other words, algorithms that produce larger reduction rates are not necessarily effective because over selection may occur, which would <sup>fi</sup>lter out many representative instances of T. Reduced datasets containing many lower quality data can directly affect the <sup>fi</sup>nal classi<sup>fi</sup>cation accuracy.

There are a number of related studies proposing instance selection methods for obtaining better mining quality in the literature. Specifically, Pradhan and Wu [26] and Jankowski and Grochowski [16] surveyed several relevant selection techniques, which can be divided into three application-type groups: noise <sup>fi</sup>lters, condensation algorithms, and prototype searching algorithms. In addition, Wilson and Martinez [30] and Brighton and Mellish [3] conducted some comparative experiments. They found the Iterative Case Filtering (ICF) and Decremental Reduction Optimization Procedure 3 (DROP3) to be cutting-edge instance selection algorithms, which make the k-NN classi<sup>fi</sup>er provide better performances over other instance selection methods.

The genetic algorithms (GA), one of the most widely used techniques for instance selection, have also been used to improve the performance of data mining algorithms [6]. In particular, Cano et al. [4] showed that better results can be obtained with a GA technique than many traditional and non-evolutionary instance selection methods in terms of better data reduction rates and higher classi<sup>fi</sup>cation accuracy. Similarly, Nanni and Lumini [23] demonstrated the superiority of GA over other instance selection methods, such as fuzzy clustering and particle swarm optimization (PSO).

Recently, García et al. [12] conducted an extensive study of comparing <sup>fi</sup>fty related instance selection algorithms including the above mentioned algorithms over 58 different datasets. In these works, however, the performance of the instance selection algorithms was assessed using datasets from the UCI Machine Learning Repository<sup>1</sup>, where the dimensionalities are very low, less than 100. However, many real world problems contain very high dimensional data, composed of several hundred to several thousands of features. For example, the dataset for text classi<sup>fi</sup>cation will usually contain at least several thousand to over ten thousand representative terms as features, while image classi<sup>fi</sup>cation is based on several hundred low-level features, such as color, texture, and/or shape features. A biological dataset can contain thousands of genes coded for proteins and their locations in various parts of the cells, and so on.

In other words, the major limitation of the afore-mentioned studies is the lack of high dimensional data reduction. The mining performance when performing instance selection over high dimensional datasets has not been fully examined. In this study, four very high dimensional datasets are used, with data dimensionalities of over 200.

GAs basically search for optimal solutions using generation succession. However, reproduction mechanisms, crossover, and mutation calculation can cause optimal chromosomes to disappear over successive generations, thereby making it impossible to fully use previous search experience. Meanwhile, a lack of diversity in chromosome populations produces premature convergence, which limits the search for a local optimum. In addition, to reach the optimal solution, an exhaustive search over the entire solution space must be carried out, which, for many complex problems, is computationally intractable.

Therefore, in this paper, a novel instance selection method for high dimensional data reduction, which we call the ef<sup>fi</sup>cient genetic algorithm (EGA), is introduced. This method is designed to minimize the computational burden and improve the optimal solution, i.e., the instance selection result. EGA simulates the biological evolutionary process and natural rules where, after long-term evolution, individuals <sup>fi</sup>nd the most ef<sup>fi</sup>cient way to allocate resources and evolve [2]. Inspired by nature, EGA is constructed as an ef<sup>fi</sup>cient and effective problem solving method for instance selection.

The major contribution of this study is to introduce a novel evolutionary-based instance selection algorithm, EGA. It is an extension of the genetic algorithm based on biological evolution. Moreover, the results of EGA assessment over high dimensional datasets are compared with those from four well-known and representative instance selection algorithms. The experimental results demonstrate that on average EGA outperforms the chosen baseline instance selection methods, allowing it to provide the highest classi<sup>fi</sup>cation accuracy, the least storage requirement, and the lowest computational complexity.

The rest of this paper is organized as follows. Section 2 describes the concept of GA and its application to instance selection. Section 3 introduces the proposed EGA method for instance selection. In Section 4, the experimental results, based on high dimensional datasets containing various domain problems, are presented. Finally, conclusions are given in Section 5.

## 2. Literature review

The main idea of the evolutionary algorithm (EA) is derived from Darwin's theory of evolution or natural selection, of which the genetic algorithm (GA) is one example [9,13]. The basic idea of a GA is that you have a population of strings (called chromosomes), which encode candidate solutions (called individuals) in an optimization problem. In general, the genetic information (i.e., chromosome) is represented by a bit string (such as binary strings of 0 s and 1 s) and sets of bits encode the solution. Genetic operators are then applied to the individuals in the population for the next generation (i.e., a new population of individuals). There are two main genetic operators: crossover and mutation. Crossover creates two strings of offspring from two parent strings by copying selected bits from each parent, whereas mutation randomly changes the value of a single bit (with small probability). In addition, a <sup>fi</sup>tness function is used to measure the quality of an individual in order to increase the probability that the single bit can survive throughout the evolutionary process.

Basically, using GA for instance selection contains the following steps [15]. First, as the initialization step, a number of individuals are randomly generated, and the length of each individual is m, which is the total number of the training set. Second, as the genetic operation step, it follows the process of the original genetic algorithm, which includes ‘selection’ (i.e. to randomly select a pair of strings from the current population), ‘mating’ (i.e. to select a pair of strings to generate two offspring) and ‘mutation’ (i.e. to randomly change the bit value from 1 to 0 or from 0 to 1). Finally, as the termination step, in this step, if a pre-speci<sup>fi</sup>ed stopping condition is not satis<sup>fi</sup>ed, the instance selection process returns to the second step; otherwise the best string with the largest <sup>fi</sup>tness value is produced, where the reduced set is determined. An example of performing GA for instance selection is shown in Fig. 5.

## 3. The ef<sup>fi</sup>cient genetic algorithm

## 3.1. The basic concept

While GAs have demonstrated success for a diverse set of problems, they are only able to handle simple concepts. Basically, the idea is that if resources are limited, the “individuals” will follow the most reasonable and simplest rules — allowing for a more effective use of resources, or “reproduction of species” [2,24]. By using simple rules, individuals that maximize the “savings cost” will become more ef<sup>fi</sup>cient. While reasonable rules help with this approach, if we can <sup>fi</sup>t the concept of “biological evolution” into the evolutionary process, where the most streamlined process also complies with reasonable rules, we can not only closely simulate the natural evolution of an algorithm, but also the algorithm will be both ef<sup>fi</sup>cient and effective.

In other words, the algorithm only pursues the simplest evolutionary process. While in general this is reasonable, as it is able to solve problems fairly ef<sup>fi</sup>ciently, a number of other elements are discarded in the pursuit of ef<sup>fi</sup>ciency in the evolutionary process. This could result in a degradation of performance, and could also cause it to fall into the local optimal solution. To avoid this problem, we introduce a novel algorithm, called the ef<sup>fi</sup>cient genetic algorithm (EGA).

In EGA, we use the individual/organism to represent a solution. In particular, the individual is similar to a gene in GA or a particle in particle swarm optimization (PSO). In addition, the ‘Kings’ represent the best group, containing the top K individuals from each iteration. After the evaluation, EGA will randomly select/choose some individuals for the mating pool. These individuals are able to perform crossover and mutation processes and thus create new individuals. Speci<sup>fi</sup>cally, each iteration of EGA will generate a new generation, which is composed of many individuals including the Kings and other individuals. Migration is a mechanism which can help EGA jump out from the local optima, just like the migration of organisms.

A <sup>fl</sup>ow chart of the EGA process is shown in Fig. 1, in which the white boxes represent the classical GA components and processes, and the gray boxes indicate the additional processes and components of EGA.

![](/api/attachments/4TGS6395/fulltext/images/f42d4673fb08f5bce5bb4c04187802ddd9c74ecd56cd0364ad4544aa099ceb5d.jpg)  
Fig. 1. The <sup>fl</sup>ow chart of EGA.

There are four additional components, speci<sup>fi</sup>cally, “Nonlinear adaptability”, “Inter-generational mating (i.e., King of Genetics)”, “Great migration”, and “New generation” which are described below.

## 3.2. Novel features of EGA

## 3.2.1. Reasonable convergence

In the process of evolution, creatures not only mate within their population, but also mate with other populations. This is the concept of hybridization. Inevitably, when the two parent populations have lived in different environments, the hybrid population will live in the environment of one or both of the parent populations. Thus, the hybrid population will not have the collection of alleles that are the most advantageous for either of those environments, resulting in a substantial loss of <sup>fi</sup>tness, i.e., their likelihood of successfully reproducing is lessened. Hybrids from different populations have better performance than purebreds from their parents in terms of their growth rate, fecundity, and adaptability. In order to maintain the racial differences to produce hybrid populations, there must be differences in some individuals. Recent studies have pointed out that a reduction in the gene pools of various wild and indigenous species results in the loss of genetic diversity [25]. Since the indigenous breeds are often better adapted to local extremes in climate and have immunity to local pathogens, this represents a signi<sup>fi</sup>- cant genetic erosion of the gene pool for future breeding [7,25]. Therefore, in order to achieve continuous evolution of the individual, we must maintain the diversity of the gene pool, and use natural evolution to <sup>fi</sup>nd the most viable species, rather than the local best species.

Due to the limitations of the algorithm (small population numbers), we were unable to provide exotic species for interbreeding. While increasing the mutation rate would allow us to achieve this, in a traditional GA, if the mutation rate is too high, it often leads to a low ef<sup>fi</sup>- ciency for solving the process (similar to random search), while if the mutation rate is too low (loss of genetic diversity), it will cause the algorithm to fall into the local optimal solution. It is dif<sup>fi</sup>cult to effectively escape a local optimal solution. In a biosphere, for example, it is unreasonable to take a long time to escape the local optimum.

Therefore, our plan is to have algorithms with a high mutation rate that can also converge effectively. While in a traditional GA this would probably be unreasonable, in our method, both “Inter-generational mating” and “Nonlinear Adaptability” are used to achieve this goal.

## 3.2.2. Nonlinear adaptability

The phenomenon of protecting vulnerable groups does not appear in the natural world. The “law of the jungle” and the “survival of the <sup>fi</sup>ttest” have always been the most authentic expressions of nature. For instance, if a newborn deer cannot stand up and move about within a short period of time, it will face elimination, as it will easily be eaten by predators. This accelerates the elimination of individuals with lower adaptability, leaving surviving individuals with more resources (e.g., more food, fewer competitors, etc.) to breed the next generations. The natural world does not waste time on those individuals which have a lower adaptability, because this not only cannot help the overall process of evolution (the next generations may not be better), but also reduces the resources available for other individuals, which may even lead to an overall evolution with low ef<sup>fi</sup>ciency. Under the conditions of limited resources, this situation is inevitable.

In other words, in the natural world, when the adaptability (<sup>fi</sup>tness value) of individuals falls below a certain threshold, these individuals will have little access to subsistence. The <sup>fi</sup>tness curve will be like the one shown in Fig. 2(a), in which the y-axis represents the original <sup>fi</sup>tness value, ranging from 0 to 1, and the x-axis represents the probability for genetic selection. Through this transformation, the probability of each individual changes. The middle and upper individuals have greater opportunity to be involved in genetic operators, whereas the lower individuals have less.

Fig. 2(a) shows a line consistent with the hyperbolic tangent function and Fig. 2(b) is Sinc-shaped [21]. For the nonlinear adaptability transformation problem, the hyperbolic tangent function is a better choice, because the Sinc-shape indicates a vibration wave leading a higher probability of selection for a poor individual.

![](/api/attachments/4TGS6395/fulltext/images/1ce7aab7e82324c732ea859ca571730f015d163e15e959edfd0d6a69cc7aa9e6.jpg)

![](/api/attachments/4TGS6395/fulltext/images/5726bc4732cb03b7fb965e68dccb70446082b7ad8e71a0f4d6f3f5f9f842ed2e.jpg)  
Fig. 2. Nonlinear and linear adaptability.

The recently developed core functions for nonlinear adaptability transformation in fuzzy set based systems show the superiority of the hyperbolic tangent functions over many other types of fuzzy sets, such as trapezoidal, triangular, Gaussian, etc. This means that it has a better <sup>fi</sup>tting ability then the other types of functions. Therefore, we consider the hyperbolic tangent function for nonlinear adaptability transformation to <sup>fi</sup>nd a better distribution for EGA <sup>fi</sup>tness.

While individuals with low resilience may provide a few good genes (individuals with a lot of good genes will have a higher adaptability), the individuals having higher adaptability for mutation or <sup>fi</sup>ne-tuning, will provide greater bene<sup>fi</sup>t than those with less. This is where existing algorithms should be improved. The steps used to adjust the <sup>fi</sup>tness f to <sup>fi</sup>t the natural law of evolution, and thus improve the ef<sup>fi</sup>ciency of our algorithm are discussed below. The process of nonlinear adaptability can be de<sup>fi</sup>ned as follows:

F is the <sup>fi</sup>tness matrix;

N is the population size;

$O r _ { i }$ is the i-th individual in the population.

Step 1. Use the <sup>fi</sup>tness function (1) to calculate the <sup>fi</sup>tness value f

$$
f _ {i} = \text { Fitness   function } (O r _ {i}), i = 1, 2,... N\tag{1}
$$

Step 2. Use Eq. (2) to normalize the <sup>fi</sup>tness $f _ { i }$ to fall in [0, 1].

$$
N o _ {i} = \frac {f _ {i} - M i n (F)}{M a x (F) - M i n (F)}, i = 1, 2, \dots , N\tag{2}
$$

Step 3. Put the normalized <sup>fi</sup>tness No into $\operatorname { E q . } \left( 3 \right)$ to obtain the corre sponding nonlinear adaptability Non<sub>i</sub>.

$$
N o n _ {i} = \frac {\text { Hyperbolic\_Tangent } \left(\frac {N o _ {i} - \alpha}{\beta^ {2}}\right) + 1}{2}, i = 1, 2,..., N\tag{3}
$$

The hyperbolic tangent function is used as the mapping model for the nonlinear adaptability. Note that Eq. (3) is a type of membership functions in the neural-fuzzy area, where the parameter α represents the central location of the membership function, and $\beta$ for the breadth of the membership function [14]. However, in this paper the parameter α can be regarded as a threshold between the good and bad genes. On the other hand, β can be seen as a weighting parameter. In our approach, the parameters αand β are set to be 5 and 7, respectively (reasonable distribution and the best results, which are based on the discussion in Section 3.3), resulting in the mapping model shown in Fig. 2(a).

Unlike the non-conversion approach, after conversion, individuals with low adaptability will have a lower mating rate, and individuals with a high adaptability will have a higher mating rate.

## 3.2.3. Genetic King — inter-generational mating

We observe that certain individuals tend to form a group and the spouse's age need not be the same as the King's. As a result of the evolutionary mating process, the distribution of power does not solely rest with the younger individuals, but rather should depend on the strength of the individuals. For example, in the lion species, even if the male lion is older, if he is the strongest, he will be the King. However, age does affect the ability of individuals. In other words, only a few of the very powerful Kings are able to do inter-generational mating. For example, old lions that are strong will be capable of mating longer. Most existing genetic algorithms use the concept of new-generational mating, but our EGA retains a small part of the previous generation, plus the most powerful individuals from the new generation, allowing these Kings to continue to compete with the new generation.

The main process of this component is to select the top K Kings from POP based on nonlinear <sup>fi</sup>tness Noni. Here, Pop is the population, Noni is the non-linear <sup>fi</sup>tness value, King includes the Kings in a generation and K is the size of King (K b N).

## 3.2.4. Hardy–Weinberg law

Prior research has shown that, when a population has the following conditions: (1) large population size, (2) random mating, (3) no natural selection or mutation, (4) no great migration and (5) alleles (genome length) are the same, the allele frequency will remain constant and the genotypic frequency will be maintained at a certain level [8,29]. This is known in population genetics as the “Hardy–Weinberg law” or “Hardy–Weinberg Equilibrium”.

The Hardy–Weinberg law can ensure that the characteristics of a species do not disappear entirely (in biological evolution the probability of each genetic characteristics is equal to a constant), but this law can only be applied to stable species. However, our goal is to <sup>fi</sup>nd the best individuals, which have the highest <sup>fi</sup>tness genes in the current environment. Therefore, if we cannot effectively get rid of the Hardy–Weinberg law, bad characteristics (not helpful for gene characteristics) will have the same probability of appearing as the good characteristics. Since this does not meet our expectations, we use the great migration to overcome this problem. Furthermore, the Hardy–Weinberg law also mentions that inter-generational mating (the King mechanism) can also break this rule.

## 3.2.5. Great migration

However, since resources are not unlimited, the <sup>fi</sup>rst condition of the Hardy–Weinberg law does not hold, and conditions (2) and (3) can be achieved by traditional GAs. On the other hand, as condition (5) violates the de<sup>fi</sup>nition of arti<sup>fi</sup>cial evolution, it cannot be achieved in this case. Therefore, we focus on condition (4) to improve traditional GAs.

a) classification accuracyof k-NN (alpha)  
![](/api/attachments/4TGS6395/fulltext/images/b38ecdf2671a32f39885d19b4cd610ab7c16a295421cc5cc032a6be9802b1fad.jpg)  
c) classification accuracy of k-NN (beta)

b) classification accuracy of SVM (alpha)  
![](/api/attachments/4TGS6395/fulltext/images/635b168d5fac00eeba2aa9b917c1b99d6e6b5d4d0c974f61f858e69be2590967.jpg)

![](/api/attachments/4TGS6395/fulltext/images/271129a07a0f374a267d6a1316d433ebd43eb1dc2cdb2985655437c17ac4392e.jpg)

d) classification accuracy of SVM (beta)  
![](/api/attachments/4TGS6395/fulltext/images/11643361d5425df28333399dbfdcbb217295589febb79ce0728b38735a0007b6.jpg)  
Fig. 3. Classi<sup>fi</sup>cation accuracy of k-NN and SVM given different alpha and beta values.

Prior research has demonstrated that great migrations can sometimes produce more species, while some species demonstrate much better adaptability than without migration. Some even become extinct [10,18,22]. The great migration is necessary to help improve biological diversity (giving a stable gene pool the opportunity for hybridization between two populations) and survival rates (hybrid offspring will be better). Accordingly, to improve algorithm performance we modify the processes and conditions to include the great migration:

1. Great migrations are not frequent (when the whole gene pool tends to be stable);

2. Great migrations will divide the population into two parts:

● Foreign population: Higher adaptability can allow an individual to overcome the great migration. (Retain “K” individuals as the foreign population, and do not have any other changes.)

● Local population: Through a high mutation rate, change “M” individuals, where these individuals will be treated as other ethnic groups (achieve genetic diversity).

3. Use the foreign and local population to continue the evolutionary process.

The process of great migration is as follows:

● Step 1: If there is no change in the best <sup>fi</sup>tness GF in G continuous generations, then apply the great migration, in which GF is the best <sup>fi</sup>tness for each generation and G is the threshold of great migration.

● Step 2: Divide the population into foreign and local populations.

● Step 3: Execute the great migration process on a local population.

Note that although the input and output of this component are individuals, the input is the population produced by the great migration component, and the output of this component is new individuals.

## 3.2.6. New generation

This component can help EGA to perform more ef<sup>fi</sup>ciently so that repeated measurements on the known individuals (Kings) are not necessary. In particular, EGA divides the population into new generations and Kings, but uses them as parts of the same population. Therefore, the new individuals still have a chance to mate with Kings and these new individuals are evaluated.

The main process for creating a new generation is to determine if the great migration has been executed, then combine the foreign and local population; otherwise combine Kings and new individuals to create a new generation, NG.

Note that the input and output of the new generation component are the populations, in which the input consists of the Kings and new individuals, and the output is the local population.

## 3.3. A small running example

In this section, we demonstrate how EGA works on a data reduction problem. To perform EGA, there are three parameters which should be set, which are alpha, beta, and the reduction rate.

In order to identify the best alpha and beta parameters (c.f. Eq. (3)) that can allow the classi<sup>fi</sup>er to provide the highest rate of classi<sup>fi</sup>cation accuracy, different alpha and beta values are examined. Fig. 3 shows the average classi<sup>fi</sup>cation accuracy of k-NN and SVM over the ten UCI datasets<sup>2</sup> by the alpha and beta parameters respectively. As we can see that using 5 for alpha and 7 for beta are the optimal parameter settings of EGA and they will be used for the following experiments.

Moreover, it is necessary to set up a target reduction rate to perform instance selection with the EGA. That is, a speci<sup>fi</sup>c dataset reduction rate should be pre-de<sup>fi</sup>ned for a dataset. In other words, EGA can be performed to reduce P% of a given dataset, resulting in a reduced dataset 1— P% requiring less storage space. Speci<sup>fi</sup>cally, the reduction rate can be de<sup>fi</sup>ned by

$$
\frac {N _ {\text { original }} - N _ {\text { reduced }}}{N _ {\text { original }}} \times 100 \%\tag{4}
$$

where $N _ { o r i g i n a l }$ means the number of data samples in the original dataset for instance selection and $N _ { r e d u c e d }$ means the number of data samples in the reduced dataset after instance selection is performed. For the experiments over the ten UCI datasets, the reduction rate P% is set to 90%.

However, the great migration threshold G is chosen experimentally. Based on our experiments, if the best <sup>fi</sup>tness value GF stops changing at the N-th iteration, then the iteration number N can be considered as the threshold for great migration G. The other related parameters for

Table 1  
The parameters of GA and EGA.

<table><tr><td></td><td>Crossover rate</td><td>Mutation rate</td><td>Iterations</td><td>Population size</td><td>K-Kings</td><td>Great migration</td><td>Stop condition</td></tr><tr><td>GA</td><td>0.65978</td><td>0.02285</td><td>200</td><td>20</td><td>-</td><td>-</td><td>200 iterations</td></tr><tr><td>EGA</td><td>0.78</td><td>0.04285</td><td>200, 50</td><td>20</td><td>10</td><td>10 (consecutive iterations)</td><td>200 iterations</td></tr></table>

GA and EGA used in our experiments are listed in Table 1. Note that higher numbers of iterations and population sizes are not considered since the computational time is critical for performing GA and EGA, especially when the data size becomes very large. In addition, these related parameters are tuned based on the Genetic Search class (in the “Select Attributes” module) of WEKA 3.6.10<sup>3</sup>. The default settings are crossover rate: 0.6, mutation rate: 0.03, maximum iterations: 20, and population: 20.

In order to clearly explain how EGA works on the data reduction problem, here we use a hypothetical dataset as a running example. The hypothetical dataset contains 3 different classes, i.e. Smart phone, Pad, and Laptop for classes 1, 2, and 3, respectively. In addition, each class contains 4 data records, in which each contains 4 attributes (i.e. features), which are “Device Extensibility”, “Performance of Touch Screen”, “Degrees of Freedom of Operating System”, and “Physical Keyboard”. In this dataset, a higher score represents a better performance of a feature, and vice versa. Note that the attribute value 0 means that the device does not have that feature. Table 2 shows the information of this dataset. In Table 2, instances 2, 6 and 7 are the best set, which can fully represent (100%) the whole training set. Therefore, the main objective of EGA is to <sup>fi</sup>nd them out to represent the whole train set. Note that the reduction rate is set to 67% over the hypothetical dataset in order for better explanation.

First, the dataset containing 12 records is divided into 3 testing (i.e. instances 10 –12) and 9 training (i.e. instances 1–9) data samples based on a 4-fold cross validation, and then EGA is performed over the training set. Note that the testing set is used for <sup>fi</sup>nal validation and the training set is for data reduction. Binary encoding is used where each bit represents a data sample in the training set, in which 1 represents that the data is used and 0 that it is not used. In this example, the population size $( N _ { P o p } )$ is set to be 20 and the number of Kings is 10 (K).

The process of performing EGA for data reduction is shown in Fig. 4. Due to the reduction rate is set to 67% (meaning that 33% of the training data are used to represent the entire training data) and each class of the training set contains at least one instance, for each individual only 3 bits (33%) can be represented as 1 (used) and the rest are 0 (not used). In Step 0, after initialization, the <sup>fi</sup>rst individual randomly selects the data records 1, 4, and 7 from the training set as the “reduced set”, which are used to train the classi<sup>fi</sup>er. Then, the original whole training set containing 9 data records (i.e. instances 1–9) are used to test the ‘<sup>fi</sup>rst-step accuracy’ of the classi<sup>fi</sup>er, which is trained by the <sup>fi</sup>rst individual (i.e. instances 1, 4, and 7). Note that this is the <sup>fi</sup>rst-step test to evaluate the classi<sup>fi</sup>cation accuracy of the “reduced set”. In Step 1, the <sup>fi</sup>rst-step accuracy of the <sup>fi</sup>rst individual is 77.78% and the reduction rate is set to 67%. Therefore, the <sup>fi</sup>rst individual's <sup>fi</sup>tness is 2.3569 based on Eq. (5). On the other hand, the <sup>fi</sup>rst-step accuracy of the second individual, which selects data records 2, 6, and 7 is 100% and its <sup>fi</sup>tness is 3.0303.

For the reduction problem, we use the <sup>fi</sup>rst-step accuracy and the reduction rate as the <sup>fi</sup>tness values for the EGA. Since this is a maximization problem, the <sup>fi</sup>tness function of EGA can be de<sup>fi</sup>ned as follows:

$$
F i t n e s s = \frac {f i r s t \_ s t e p \_ a c c u r a c y}{1 - r e d u c t i o n \_ r a t e}.\tag{5}
$$

In Step 2, the non-linear function is used, which can change the <sup>fi</sup>tness value into the non-linear type. In this case, EGA will select the top 10 individuals as the Kings (i.e., Step 3). Therefore, only 10 new individuals need to be generated in Step 4. These 10 new individuals will then go through Steps 5 and 6, which are the same as the crossover and mutation steps in the GA process. In Step 7, if the great migration condition is met, EGA will make a great migration for these 10 individuals. Next, these two new individuals will combine with the Kings to form a new generation (Step 8). Finally, when the stop condition is met (i.e., 200 iterations), the best solution will be used to select the representative data samples to reduce the original training set. In this case, the best solution (or the best reduced set) is based on the data records 2, 6, and 7 to represent the original training set since the classi<sup>fi</sup>cation accuracy of the classi<sup>fi</sup>er trained by the best solution is 100% over the testing set (not the original training set containing instances 1–9 but the real test set containing instances 10, 11, and 12). This is the second-step test to validate that the selected data records are the best solution. Note that the pseudo code of EGA is shown in Appendix A.

It should be noted that in Fig. 4 the white boxes represent the classical GA components and processes, and the gray boxes the additional processes and components of EGA. The difference between EGA and GA is highlighted in Fig. 5 which shows the process of performing GA over the same dataset. The differences between EGA and GA are discussed further in the next section.

## 3.4. Discussion

The primary differences between the EGA and a traditional GA are summarized in Table 3 and also explained further in the following subsections.

## 3.4.1. Evaluation and new generation

In EGA, the <sup>fi</sup>tness value is mapped to a nonlinear model which enables us to achieve nonlinear adaptability. This differs from traditional linear adaptability which can accelerate the evolutionary process and remove the poor individuals, in that it provides more mating opportunities for the high-end individuals. Based on this mechanism, bad genes will not be selected repeatedly. As a result, the good genes have more chances to be <sup>fi</sup>ne-tuned.

The evaluation process shows the performance of EGA to be more ef<sup>fi</sup>cient than that of classical GA, because of the evaluation of the “Kings”, meaning that the evaluation process just needs to focus on the new individuals. While this can improve the EGA's performance, the opportunity of trying K individuals for evolution in each iteration is missed.

To overcome this problem, the mutation and mating rates can be increased. In particular, a high mutation rate on a part of the population is used rather than a lower mutation rate on all of the genes in the population (as GAs do). Traditional GAs are not able to accept a higher mutation rate, because this will cause a random search and convergence is dif<sup>fi</sup>cult.

Furthermore, the composition of each generation in the EGA is different from that in the GA. When a non-overlapping generation model is used, each new generation in the GA is a whole new generation. However, the EGA uses an overlap-like generation, where the new generation is composed of Kings and new individuals. This mechanism will improve the performance of EGA in terms of higher ef<sup>fi</sup>ciency. This is because new individuals can obtain some good genes from the

Table 2 The hypothetical dataset.

<table><tr><td>Instance</td><td>Device Extensibility</td><td>Performance of Touch screen</td><td>Degrees of freedom of OS</td><td>Physical keyboard</td><td>Class Label</td><td>Train/Test</td><td>Best set</td></tr><tr><td>1</td><td>0.8</td><td>0.9</td><td>0</td><td>0</td><td>1 (Phone)</td><td>Training set</td><td></td></tr><tr><td>2</td><td>0.75</td><td>0.75</td><td>0</td><td>0</td><td>1 (Phone)</td><td>Training set</td><td>★</td></tr><tr><td>3</td><td>0.35</td><td>0.75</td><td>0.75</td><td>0</td><td>1 (Phone)</td><td>Training set</td><td></td></tr><tr><td>4</td><td>0</td><td>0.85</td><td>0.77</td><td>0</td><td>2 (Pad)</td><td>Training set</td><td></td></tr><tr><td>5</td><td>0</td><td>0.95</td><td>0.65</td><td>0</td><td>2 (Pad)</td><td>Training set</td><td></td></tr><tr><td>6</td><td>0.1</td><td>0.48</td><td>0.77</td><td>0.88</td><td>2 (Pad)</td><td>Training set</td><td>★</td></tr><tr><td>7</td><td>0</td><td>0</td><td>0.9</td><td>0.78</td><td>3 (Laptop)</td><td>Training set</td><td>★</td></tr><tr><td>8</td><td>0</td><td>0</td><td>0.85</td><td>0.99</td><td>3 (Laptop)</td><td>Training set</td><td></td></tr><tr><td>9</td><td>0.83</td><td>0</td><td>0.85</td><td>0.72</td><td>3 (Laptop)</td><td>Training set</td><td></td></tr><tr><td>10</td><td>0.68</td><td>0.85</td><td>0</td><td>0</td><td>1 (Phone)</td><td>Testing set</td><td>-</td></tr><tr><td>11</td><td>0</td><td>0.85</td><td>0.78</td><td>0</td><td>2 (Pad)</td><td>Testing set</td><td>-</td></tr><tr><td>12</td><td>0</td><td>0</td><td>0.99</td><td>0.85</td><td>3 (Laptop)</td><td>Testing set</td><td>-</td></tr></table>

Kings when the new individuals contain poor genes. The Kings can be regarded as the milestone that helps the EGA to <sup>fi</sup>nd more possible solutions rather than a repeated search.

## 3.4.2. Selection of kings and mating

Since it incorporates the concept of intergenerational mating, EGA just needs to calculate the <sup>fi</sup>tness for each newborn individual, rather than the entire population (because there are always a small number of individuals from the previous generation). In this new generation process for EGA, the n-Kings and the newborn individuals are joined to form the next generation. Therefore, in the mating process, n-Kings have the opportunity to mate with the new generation, so that even when the high mutation rate means that there is no individual similar to the Kings, their genes have the opportunity to be passed down. Consequently, the n-Kings will have more opportunities for <sup>fi</sup>netuning and evolution.

In each iteration of the EGA process, the top K individuals are selected as the Kings, and they are retained directly (without mutation and mating). Therefore, these Kings can mate with the individuals of a new generation. If the new generation is worse than the old one, the Kings can be used as the basis of the next evolution, and thus reconvergence as occurs is traditional GAs is usually not necessary. Consequently, the Kings have more opportunities for <sup>fi</sup>ne-tuning and evolution.

To overcome this problem, the mutation and mating rates are increased. Speci<sup>fi</sup>cally, we use a high mutation rate for a part of the population rather than a lower mutation rate for all of genes in the population (GA). Traditional GAs are not able to accept a higher mutation rate, because it will cause a random search and lack of convergence.

Relatively speaking, the Kings mechanism can guarantee that the <sup>fi</sup>tness value of each generation is not worse than the ones of previous generations, and the high mutation and mating rates can help EGA to <sup>fi</sup>nd more possible solutions.

The mating process in EGA functions the same way as in the GAs. However, the composition of the new generation in EGA and GAs is different. The new individuals in EGA can mate with the Kings (the best individuals of previous generation).

## 3.4.3. Great migration

In this section, we will explain the difference between the great migration and the high migration rate. First, the great migration is a mechanism which helps EGA escape from a stable evolution while the high migration rate means that EGA applies a higher migration rate than GA.

![](/api/attachments/4TGS6395/fulltext/images/3311bb95cf74496855c318ac81831557855f1d35f3ca6fdb5ac1a77d84a699f9.jpg)  
Fig. 4. The process of performing EGA for data reduction with the 67% reduction rate

Table 3  
![](/api/attachments/4TGS6395/fulltext/images/3a2919b372c4947023aabe2f6d03d5148b3f5215bf4a20e80a8b5f5a784d91fc.jpg)  
Fig. 5. The process of performing GA for data reduction with the 67% reduction rate

Although the traditional GAs have a mechanism to preclude falling into local optima, there are still some restrictions. Convergence causes the GA to be able to <sup>fi</sup>nd a better solution than a random search, therefore if the GA undergoes more iteration, the changes of <sup>fi</sup>tness become smaller and smaller until eventually becoming continuously unchanging. EGA uses the great migration to avoid this problem, establishing a threshold to decide if it will perform the great migration or not. If there is no sustained change in the <sup>fi</sup>tness value, then the great migration mechanism will be triggered.

In our EGA design, a higher migration and mating rate is applied than in the GA, because it is hoped that those new individuals will be subject to change. In the traditional GA setting, some individuals have the opportunity to become a new individual without any changes, however, the repeated measurements on the known individuals (Kings) are not necessary and waste time, while retaining these good individuals directly is a good mechanism. Therefore, EGA applies a higher migration and mating rate to allow new individuals to be subject to change, and using the King mechanism to retain top individuals.

## 3.4.4. Time complexity analysis

Here, we analyze the computational complexity or time complexity of the EGA and GA. In this case, the genetic operations (crossover, selection, mutation, matting, etc.) can be negligible. This is because the complexity of the objective function is much larger than the genetic operation, so that the complexity analysis just needs to focus on the complexity of evaluation (i.e., objective function).

The differences between GA and EGA

<table><tr><td>Process</td><td>Traditional GAs</td><td>EGA</td></tr><tr><td>Evaluation</td><td>Reckoning of a fitness value for each gene in this generation</td><td>Reckoning of a nonlinear fitness value for each gene in new generation</td></tr><tr><td>Select Kings</td><td>-</td><td>Find the Kings of this generation (Inter-generational mating)</td></tr><tr><td>Mating</td><td>Selection, crossover and mutation (only for a new generation)</td><td>Selection, Crossover and Mutation (new generation and Kings of the last generation)</td></tr><tr><td>Great migration</td><td>-</td><td>Great migration</td></tr><tr><td>New generation</td><td>Population: a whole new generation</td><td>Combine the new generation and the Kings of the last generation</td></tr></table>

For the GA method, its time complexity is $O ( N _ { P o p } \times L \times C E ( D ) )$ where $N _ { p o p }$ represents the number of genes (population size), L as the maximum number of iterations and the complexity of an evolutionary algorithm (EGA and GA) is CE. In particular, for each individual in EGA, since it will be tested by a classi<sup>fi</sup>er for the <sup>fi</sup>rst-step-accuracy during each iteration, the complexity O(CE(D)) represents the complexity of a classi<sup>fi</sup>er (i.e., the k-NN classi<sup>fi</sup>er in this paper) over a D dimension dataset. This is because in order to evaluate a high dimensional dataset, we require large computational time and much memory. Although O(CE(D)) can be ignored over the small scale problems, for high dimensional datasets, data dimensionality becomes a critical issue. Therefore, we think that the complexity of classi<sup>fi</sup>er O(CE(D)) should be considered in the high dimensional problem.

Some mechanisms have been integrated into the EGA such as Nonlinear Adaptability, Kings and the Great Migration. The time complexity of each mechanism is explained as follows. First, the process of nonlinear adaptability is used to map the <sup>fi</sup>tness value to the nonlinear model. This is a very simple process, so the complexity of nonlinear adaptability can be ignored. Second, the effort used in the great migration process is similar to the genetic operation, thus the complexity of the great migration process can also be ignored. Third, K represents the number of Kings, in which repeat assessment of the K individuals is unnecessary. Therefore, the time complexity of EGA can be de<sup>fi</sup>ned as ${ \cal O } ( ( N _ { P o p } - K ) \times L \times C E ( D ) ^ { } .$ ).

More speci<sup>fi</sup>cally, in our experiments the parameters of GA are set as follows: $N _ { P o p }$ and L are set by 20 and 200, respectively. In EGA, $N _ { P o p }$ and L are set to be the same as in GA, and K is 10. Consequently, the computational time of EGA is more than twice as fast as for GA.

## 3.4.5. Classification Accuracy and Storage Requirements

Table 4 shows the classi<sup>fi</sup>cation results of k-NN and SVM obtained with EGA and GA over the ten UCI datasets based on different reduction rates.

According to these results, in most cases, no matter how many reduction rates are attempted, the reduced datasets created by EGA using 50 and 200 iterations individually can allow the SVM and k-NN

## Table 4

Classi<sup>fi</sup>cation results of SVM and k-NN obtained by EGA and GA over the ten UCI dataset

<table><tr><td rowspan="2"></td><td rowspan="2">Baseline</td><td colspan="3">50% reduction</td><td colspan="3">90% reduction</td></tr><tr><td>EGA (50)</td><td>EGA (200)</td><td>GA</td><td>EGA (50)</td><td>EGA (200)</td><td>GA</td></tr><tr><td>SVM</td><td>80.32%</td><td>79.67%</td><td>80.14%</td><td>77.30%</td><td>76.87%</td><td>78.65%</td><td>75.87%</td></tr><tr><td>k-NN</td><td>79.45%</td><td>76.58%</td><td>77.40%</td><td>75.20%</td><td>73.91%</td><td>75.47%</td><td>72.13%</td></tr></table>

![](/api/attachments/4TGS6395/fulltext/images/e782653ce1128fc03bc00fff52b6e0a5a1b05cb1a70fdb3af8879c1a549d966c.jpg)

![](/api/attachments/4TGS6395/fulltext/images/9219a080fac59e39a68e1c6e25009aef9b0245728863063e3ebde3c0b09a66d1.jpg)  
Fig. 6. Average classi<sup>fi</sup>cation accuracy of k-NN and SVM

classi<sup>fi</sup>ers to perform better than the ones created by GA. More speci<sup>fi</sup>- cally, EGA (200) signi<sup>fi</sup>cantly outperforms GA in terms of k-NN and SVM for 50% and 90% dataset reductions (i.e., p b 0.05)<sup>4</sup>. In other words, EGA (50) and EGA (200) can make k-NN and SVM perform the more comparable results with the baseline classi<sup>fi</sup>ers without instance selection than GA does.

From the performances of EGA (50) and EGA (200), we can observe that the EGA provides better solution when a larger number of iterations (i.e., 200) are used than a smaller number (i.e., 50). However, the differences in performance between the 50% dataset reduction and 90% dataset reduction are less than 1% and 2%, respectively. In other words, they do not perform in a very signi<sup>fi</sup>cantly different manner (i.e., p b 0.1).

On the other hand, Fig. 6 shows some degradation in the average classi<sup>fi</sup>cation accuracy of k-NN and SVM from the 50% reduction rate to the 90% reduction rate. This indicates that although <sup>fi</sup>ltering out larger numbers of data samples from a given training set can reduce the amount of storage space (i.e., lower storage requirement), it can lead to the reduced training set having lower quality, which makes the classi<sup>fi</sup>ers perform more poorly than when <sup>fi</sup>ltering out fewer data samples.

Comparison of the computation times for 50% and 90% reduction rates shows that it takes longer to reduce the dataset size when performing a 50% reduction than when performing a 90% reduction. This is because both EGA and GA need to search for more spaces (i.e. data samples) to determine whether to remove the data samples or not. In other words, the criterion for data removal is much stricter for 50% reduction than for 90% reduction. This phenomenon is similar to the other state-of-the-art algorithms (c.f. Section 4.5).

In short, the initial study results demonstrate that EGA performs better than GA. The reduced dataset created by EGA contains higher quality data allowing the classi<sup>fi</sup>ers to provide higher classi<sup>fi</sup>cation accuracy. Moreover, EGA is a more ef<sup>fi</sup>cient instance selection algorithm than GA. This provides evidence that the novel components of EGA can speed up the instance selection process as discussed in Section 3.4.

## 4. Experiments

## 4.1. Experimental Setup

In this experiment, four very high dimensional datasets are used, namely the TechTC-100 dataset<sup>5</sup> [5,11] for text classi<sup>fi</sup>cation, KDD Cup'01<sup>6</sup> for predicting gene/protein functions and localization (UCSD Competition)<sup>7</sup> for E-commerce customer identi<sup>fi</sup>cation, and Caltech 101<sup>8</sup> for image classi<sup>fi</sup>cation.

The TechTC-100 dataset includes 100 different two-class datasets, in which the largest and smallest datasets contain 165 and 125 documents, respectively. In addition, the feature dimensionality of each pair ranges from 12,813 to 29,260. On the other hand, each image in the Caltech 101 dataset had to be preprocessed in order to extract the 200 dimensional bag-of-words (BoW) feature [19]. Table 5 shows the information in these four chosen datasets.

For the TechTC-100 dataset, we follow the same experimental setup as in Davidov et al. [5] and Gabrilovich and Markovitch [11], dividing each dataset into training and testing sets via 4-fold cross validation. For the other three datasets, 10-fold cross validation is used.

Four state-of-the-art algorithms were considered for EGA performance comparison: GA, IB3 [1], DROP3 [30], and ICF [3]. According to García et al. [12], these algorithms are hybrid methods, aimed at <sup>fi</sup>nding the smallest subset which maintains or even increases the generalization accuracy of the test data. On average, hybrid methods are able to provide the largest data reduction rates and can make the classi<sup>fi</sup>er provide higher classi<sup>fi</sup>cation accuracy than without instance selection.

## 4.2. Classification accuracy

Tables 6 and 7 show the classi<sup>fi</sup>cation accuracy of k-NN and SVM based on the <sup>fi</sup>ve instance selection algorithms and the baseline without instance selection. Note that the value in brackets indicates the difference in performance between the classi<sup>fi</sup>er with instance selection and the baseline classi<sup>fi</sup>er.

These results demonstrate that no matter which classi<sup>fi</sup>er is used, EGA based on 200 iterations for 50% dataset reduction performs best and EGA based on 200 iterations for 90% dataset reduction performs second best. In addition, they both signi<sup>fi</sup>cantly outperform the GA, ICF, DROP3, and IB3 algorithms over high dimensional datasets (p b 0.05). The only exception was that the classi<sup>fi</sup>cation accuracy of SVM by DROP 3 over the KDD Cup'01 dataset was the same as that with EGA (50, 50%) and EGA (200, 50%).

On average, only EGA (200, 50%) and EGA (200, 90%) allow the k-NN classi<sup>fi</sup>er to provide slightly better and similar classi<sup>fi</sup>cation accuracy to the baseline k-NN classi<sup>fi</sup>er. On the other hand, when SVM is used as the classi<sup>fi</sup>er, EGA (200, 50%) and EGA (200, 90%) consistently perform best

## Table 5

Dataset information.

<table><tr><td>Datasets</td><td>No. of features</td><td>No. of samples</td><td>No. of classes</td></tr><tr><td>TechTC-100</td><td>18,236 (avg.)</td><td>149 (avg.)</td><td>2</td></tr><tr><td>KDD Cup&#x27;01</td><td>2197</td><td>779</td><td>15</td></tr><tr><td>UCSD Competition</td><td>334</td><td>11,742</td><td>2</td></tr><tr><td>Caltech 101</td><td>200</td><td>9146</td><td>101</td></tr></table>

## Table 7

Table 6  
Classi<sup>fi</sup>cation accuracy of k-NN with and without instance selection.

<table><tr><td rowspan="2"></td><td colspan="4">EGA (iteration, reduction rate)</td><td colspan="2">GA</td><td rowspan="2">ICF</td><td rowspan="2">DROP3</td><td rowspan="2">IB3</td></tr><tr><td>(50, 50%)</td><td>(50, 90%)</td><td>(200, 50%)</td><td>(200, 90%)</td><td>(200, 50%)</td><td>(200, 90%)</td></tr><tr><td>TechTC-100</td><td>74.27%</td><td>74.27%</td><td>75.52%</td><td>74.27%</td><td>67.02%</td><td>66.77%</td><td>68.82%</td><td>71.47%</td><td>73.10%</td></tr><tr><td>74.01%</td><td>(+0.26%)</td><td>(+0.26%)</td><td>(+1.51%)</td><td>(+0.26%)</td><td>(-6.99%)</td><td>(-7.24%)</td><td>(-5.62%)</td><td>(-2.97%)</td><td>(-1.34%)</td></tr><tr><td>KDD Cup&#x27;01</td><td>52.38%</td><td>52.38%</td><td>53.05%</td><td>51.92%</td><td>31.17%</td><td>26.89%</td><td>24.27%</td><td>49.97%</td><td>50.58%</td></tr><tr><td>54.14%</td><td>(-1.76%)</td><td>(-1.76%)</td><td>(-1.09%)</td><td>(-2.22%)</td><td>(-22.97%)</td><td>(-27.25%)</td><td>(-29.87%)</td><td>(-4.17%)</td><td>(-3.56%)</td></tr><tr><td>UCSD</td><td>84.6%</td><td>84.6%</td><td>87.33%</td><td>84.42%</td><td>84.25%</td><td>83.53%</td><td>32.10%</td><td>80.53%</td><td>51.12%</td></tr><tr><td>84.10%</td><td>(+0.5%)</td><td>(+0.5%)</td><td>(+3.23%)</td><td>(+0.32%)</td><td>(+0.15%)</td><td>(-0.57%)</td><td>(-52%)</td><td>(-3.57%)</td><td>(-32.98%)</td></tr><tr><td>Caltech 101</td><td>39.2%</td><td>36.11%</td><td>39.31%</td><td>36.33%</td><td>33.33%</td><td>33.06%</td><td>21.37%</td><td>35.74%</td><td>6.89%</td></tr><tr><td>37.97%</td><td>(+1.23%)</td><td>(-1.86%)</td><td>(+1.34%)</td><td>(-1.64%)</td><td>(-4.64%)</td><td>(-4.91%)</td><td>(-16.6%)</td><td>(-2.23%)</td><td>(-31.08%)</td></tr><tr><td>Avg.</td><td>62.61%</td><td>61.84%%</td><td>63.8%</td><td>61.74%</td><td>53.94%</td><td>52.56%</td><td>36.64%</td><td>59.43%</td><td>45.42%</td></tr><tr><td>62.56%</td><td>(+0.05%)</td><td>(-0.72%)</td><td>(+0.24%)</td><td>(-0.82%)</td><td>(-8.62%)</td><td>(-10%)</td><td>(-25.92%)</td><td>(-3.13%)</td><td>(-17.14%)</td></tr></table>

Classi<sup>fi</sup>cation accuracy of SVM with and without instance selection.

<table><tr><td rowspan="2"></td><td colspan="4">EGA (iteration, reduction rate)</td><td colspan="2">GA</td><td rowspan="2">ICF</td><td rowspan="2">DROP3</td><td rowspan="2">IB3</td></tr><tr><td>(50, 50%)</td><td>(50, 90%)</td><td>(200, 50%)</td><td>(200, 90%)</td><td>(200, 50%)</td><td>(200, 90%)</td></tr><tr><td>TechTC-100</td><td>58.75%</td><td>58.75%</td><td>60%</td><td>58.75%</td><td>57.5%</td><td>51.5%</td><td>40%</td><td>56.25%</td><td>57.5%</td></tr><tr><td>66.25%</td><td>(-7.5%)</td><td>(-7.5%)</td><td>(-6.25%)</td><td>(-7.5%)</td><td>(-8.75%)</td><td>(-14.75%)</td><td>(-26.25%)</td><td>(-10%)</td><td>(-8.75%)</td></tr><tr><td>KDD Cup&#x27;01</td><td>42.84%</td><td>37.59%</td><td>42.84%</td><td>37.59%</td><td>42.84%</td><td>35.59%</td><td>6.06%</td><td>42.84%</td><td>39.59%</td></tr><tr><td>42.84%</td><td>(+0%)</td><td>(-4.25%)</td><td>(+0%)</td><td>(-4.25%)</td><td>(+0%)</td><td>(-6.25%)</td><td>(-36.78%)</td><td>(+0%)</td><td>(-3.22%)</td></tr><tr><td>UCSD</td><td>90.81%</td><td>90.81%</td><td>90.81%</td><td>90.81%</td><td>90.81%</td><td>90.81%</td><td>84.16%</td><td>90.53%</td><td>87.07%</td></tr><tr><td>90.73%</td><td>(+0.08%)</td><td>(+0.08%)</td><td>(+0.08%)</td><td>(+0.08%)</td><td>(+0.08%)</td><td>(+0.08%)</td><td>(-6.57%)</td><td>(-0.2%)</td><td>(-3.66%)</td></tr><tr><td>Caltech 101</td><td>42.89%</td><td>39.8%</td><td>43%</td><td>40.02%</td><td>11.5%</td><td>3.33%</td><td>2.78%</td><td>35.74%</td><td>0.63%</td></tr><tr><td>44.66%</td><td>(-1.77%)</td><td>(-4.86%)</td><td>(-1.66%)</td><td>(-4.64%)</td><td>(-33.16%)</td><td>(-41.33%)</td><td>(-41.88%)</td><td>(-8.92%)</td><td>(-44.03%)</td></tr><tr><td>Avg.</td><td>58.82%</td><td>56.74%</td><td>59.16%</td><td>56.79%</td><td>51.16%</td><td>45.31%</td><td>33.25%</td><td>56.34%</td><td>46.2%</td></tr><tr><td>61.12%</td><td>(-2.3%)</td><td>(-4.38%)</td><td>(-1.96%)</td><td>(-4.33%)</td><td>(-9.96%)</td><td>(-15.81%)</td><td>(-27.87%)</td><td>(-4.78%)</td><td>(-14.92%)</td></tr></table>

and second best, respectively. However, only with EGA (200, 50%) is the SVM classi<sup>fi</sup>er performance similar to that of the SVM baseline.

In short, the classi<sup>fi</sup>cation results demonstrate the applicability of EGA on instance selection. More speci<sup>fi</sup>cally, EGA (200, 50%) can allow the k-NN and SVM classi<sup>fi</sup>ers to provide the most similar performance to the baseline k-NN and SVM. Moreover, we also <sup>fi</sup>nd that k-NN is a better classi<sup>fi</sup>er for instance selection than SVM. In other words, k-NN instance selection performs better than SVM instance selection.

## 4.3. Storage requirements

Besides examining the classi<sup>fi</sup>cation accuracy, reduction rates are obtained. Table 8 shows the reduction rates obtained using the <sup>fi</sup>ve instance selection algorithms over each of the training datasets. For the comparisons of ICF, DROP3, and IB3, we can observe that, on average, ICF produces the largest reduction rate, but it makes k-NN and SVM perform the worst. This means that over selection occurs when ICF is used. In other words, it <sup>fi</sup>lters out too many sets of representative (or good quality) data, which can better distinguish between different classes.

From this point of view, DROP3 produces the least reduction rate, making it likely to retain more representative data compared with GA (including 50% and 90% reduction rates), ICF, or IB3. Consequently, it makes k-NN and SVM perform better than GA, ICF, or IB3 individually.

For EGA (200 iterations), however, despite the fact that 90% dataset reduction is produced, it makes k-NN perform very similar to the

## Table 8

Average numbers of selected instances (reduction rate).

<table><tr><td rowspan="2"></td><td rowspan="2">Baseline</td><td colspan="2">EGA/GA</td><td rowspan="2">ICF</td><td rowspan="2">DROP3</td><td rowspan="2">IB3</td></tr><tr><td>(50%)</td><td>(90%)</td></tr><tr><td>TechTC-100</td><td>112</td><td>56</td><td>11</td><td>67 (40.32%)</td><td>66 (40.99%)</td><td>56 (50.17%)</td></tr><tr><td>KDD Cup&#x27;01</td><td>701</td><td>351</td><td>70</td><td>127 (81.89%)</td><td>406 (43.72%)</td><td>525 (25.13%)</td></tr><tr><td>UCSD</td><td>10,568</td><td>5284</td><td>1057</td><td>67 (99.43%)</td><td>10,429 (11.19%)</td><td>1983 (83.12%)</td></tr><tr><td>Caltech 101</td><td>7809</td><td>3905</td><td>781</td><td>861 (88.97%)</td><td>3033 (61.16%)</td><td>101 (98.71%)</td></tr><tr><td>Avg.</td><td>4798.5</td><td>2399</td><td>479.75</td><td>280.5 (77.65%)</td><td>3483.5 (39.27%)</td><td>66.25 (64.28%)</td></tr></table>

## Table 9

Average execution time (sec.).

<table><tr><td rowspan="2"></td><td colspan="4">EGA (iteration, reduction rate)</td><td colspan="2">GA</td><td rowspan="2">ICF</td><td rowspan="2">DROP3</td><td rowspan="2">IB3</td></tr><tr><td>(50, 50%)</td><td>(50, 90%)</td><td>(200, 50%)</td><td>(200, 90%)</td><td>(200, 50%)</td><td>(200, 90%)</td></tr><tr><td>TechTC-100</td><td>0.1</td><td>0.04</td><td>0.4</td><td>0.17</td><td>0.71</td><td>0.36</td><td>12.16</td><td>155.5</td><td>2.1</td></tr><tr><td>KDD Cup&#x27;01</td><td>3.48</td><td>0.57</td><td>13.93</td><td>2.29</td><td>25.75</td><td>4.57</td><td>54.7</td><td>69.76</td><td>35.54</td></tr><tr><td>UCSD</td><td>1817.06</td><td>302.14</td><td>7268.23</td><td>1208.56</td><td>14482.14</td><td>3097.9</td><td>1403.14</td><td>20,482</td><td>1768</td></tr><tr><td>Caltech 101</td><td>643.47</td><td>125.31</td><td>2573.89</td><td>501.23</td><td>5238.45</td><td>999.57</td><td>379.59</td><td>1766.9</td><td>61.96</td></tr><tr><td>Avg.</td><td>616.03</td><td>107.02</td><td>2464.11</td><td>428.06</td><td>4936.76</td><td>1025.6</td><td>462.4</td><td>5618.54</td><td>466.9</td></tr></table>

Table 10  
The average classi<sup>fi</sup>cation accuracy (by k-NN), reduction rate, and computational costs of EGA, GA, ICF, DROP3, and IB3.

<table><tr><td></td><td></td><td>Accuracy</td><td>Reduction</td><td>Cost</td></tr><tr><td rowspan="4">EGA</td><td>(50, 50%)</td><td>62.61% (2)</td><td>50% (6)</td><td>616.03 (5)</td></tr><tr><td>(200, 50%)</td><td>63.8% (1)</td><td>50% (6)</td><td>2464.11 (7)</td></tr><tr><td>(50, 90%)</td><td>61.84% (3)</td><td>90% (1)</td><td>107.02 (1)</td></tr><tr><td>(200, 90%)</td><td>61.74% (4)</td><td>90% (1)</td><td>428.06 (2)</td></tr><tr><td rowspan="2">GA</td><td>(200, 50%)</td><td>53.94% (6)</td><td>50% (6)</td><td>4936.76 (8)</td></tr><tr><td>(200, 90%)</td><td>52.563% (7)</td><td>90% (1)</td><td>1025.6 (6)</td></tr><tr><td>ICF</td><td></td><td>36.64% (9)</td><td>77.65% (4)</td><td>462.4 (3)</td></tr><tr><td>DROP3</td><td></td><td>59.43% (5)</td><td>39.27% (9)</td><td>5618.54 (9)</td></tr><tr><td>IB3</td><td></td><td>45.42% (8)</td><td>64.28% (5)</td><td>466.9 (4)</td></tr></table>

baseline (i.e. 61.74% vs. 62.56%), which outperforms the other four instance algorithms. Therefore, among these algorithms EGA performs optimally in terms of the reduction rate and classi<sup>fi</sup>cation accuracy.

## 4.4. Computational cost

The <sup>fi</sup>nal evaluation metric for assessing the performance of these <sup>fi</sup>ve instance selection algorithms is based on the computational cost required during instance selection. Table 9 shows the average execution time for EGA, GA, ICF, DROP3, and IBS for each of the datasets.

The comparative results for ICF, DROP3, and IB3 indicate that DROP3 requires the longest time to complete the instance selection task. On the other hand, ICF and IB3 are relatively ef<sup>fi</sup>cient state-ofthe-art algorithms.

Both GA and EGA can pre-de<sup>fi</sup>ne the reduction rate, but EGA performs more than two times as ef<sup>fi</sup>ciently as GA, regardless of whether the 50% or 90% reduction rate is considered. More speci<sup>fi</sup>cally, for 90% dataset reduction, EGA takes the least time to select representative data. However, the classi<sup>fi</sup>cation accuracy, reduction rate, and computational cost are affected by each other (see the discussion below).

## 4.5. Discussion

To facilitate examination of the relationship between the performance of these instance selection algorithms in terms of classi<sup>fi</sup>cation accuracy, reduction rate, and computational cost, the average performance of these algorithms is listed altogether in Table 10. Note that the numbers in brackets indicate the ranking for each speci<sup>fi</sup>c performance.

For the state-of-the-art algorithms, on average, ICF and IB3 take about 460 s to produce about 78% and 64% reduction rates. Although they are relatively ef<sup>fi</sup>cient for performing instance selection and can provide good reduction rates, they have the worst and second worst <sup>fi</sup>nal classi<sup>fi</sup>cation performances (i.e., 36.64% and 45.42%, respectively).

On the other hand, GA and DROP3 require the longest and the second longest time to complete the instance selection tasks (the reduction rates are about 50% and 39% respectively), but they can provide better classi<sup>fi</sup>cation accuracy than ICF or IB3.

To sum up, we recommend using EGA with different settings for different circumstances. For example, if classi<sup>fi</sup>cation accuracy is the most important issue, but the reduction rate and computational cost are not a big concern, then EGA (200, 50%) is the best choice. However, if classi<sup>fi</sup>cation accuracy and reduction rate are both important, EGA (50, 90%) and EGA (200, 90%) are suitable. On the other hand, when one needs an algorithm that can produce the largest reduction rate with the least computational cost, while providing reasonable classi<sup>fi</sup>cation accuracy, EGA (50, 90%) would be the optimal solution.

Here, we further provide two performance analyses for the relationships between (1) the dataset dimension and time cost and (2) the dataset dimension and classi<sup>fi</sup>cation accuracy. 14 datasets are used in this analysis<sup>9</sup>. As shown in Fig. 7, when the dataset dimension increases, the time cost of GA exponentially grows. In other words, the time cost of EGA is stably lower than GA. Moreover, when EGA and GA are used by the same number of iterations (200), the time cost of EGA (200) is much lower than GA (200) when the dataset dimension is larger than 10,000. Fig. 8 also shows that even performing EGA by a smaller number of iterations than GA, the classi<sup>fi</sup>cation accuracy of EGA is still slightly higher or similar to GA. These results indicate that EGA is the better choice than GA for instance selection, especially when high dimensional datasets are used.

a) Reduction rate: 50%  
![](/api/attachments/4TGS6395/fulltext/images/2075f75d8ce26f9594b77be2adb2272a275c6744386d37e57d22840fa08eb017.jpg)

b) Reduction rate: 90%  
![](/api/attachments/4TGS6395/fulltext/images/6e399c9c816bfa8dd1e142d3add75f5ca1c7dd9635da20dbda7eb470c9407569.jpg)  
Fig. 7. The relationship between the time cost and dataset dimension

a) Reduction rate: 50%  
![](/api/attachments/4TGS6395/fulltext/images/78eeb54189239ac29d84ff168bac3dfd11ac21060a362312fa438a26bc988ea9.jpg)

b) Reduction rate: 90%  
![](/api/attachments/4TGS6395/fulltext/images/a1d363816cbc271d7082612385eaf44d93d4e68e7bf6d269d933e8132cade46e.jpg)  
Fig. 8. The relationship between the classi<sup>fi</sup>cation accuracy and dataset dimension.

In summary, the proposed EGA approach has the following characteristics that outperform the other algorithms. First, the nonlinear adaptability can help EGA to reduce the incidence of some bad solutions. Second, the King mechanism can reduce the computation load of EGA. Third, the great migration keeps the diversity of the solution. Therefore, EGA can provide the satisfactory result with a higher reduction rate and a lower time cost over the high dimensional instance selection (or data reduction) problem.

## 5. Conclusion

Many of the current state-of-the-art instance selection algorithms cannot perform well over very high dimensional problems. In other words, performing instance selection in high dimensional feature space is very challenging. In this paper, the experiments are based on four high dimensional datasets and the experimental results show that our proposed ef<sup>fi</sup>cient genetic algorithm (EGA) performs better than four state-of-the-art instance selection algorithms (i.e. GA, ICF, DROP3, and IB3) in terms of having the highest classi<sup>fi</sup>cation accuracy and possessing a relatively low computational cost. Moreover, EGA can produce the largest reduction rate (90%), which is the same as GA.

Several issues can be considered in future work. The <sup>fi</sup>rst would be to integrate both feature selection and instance selection. That is, given a high dimensional dataset, feature selection can be performed <sup>fi</sup>rst to reduce the dataset's dimensionality. Then, the processed dataset can be used for instance selection. The second one would be the information fusion issue, which is based on combining multiple selection results produced by different instance selection algorithms individually to produce the <sup>fi</sup>nal selection result as a reduced dataset.

Third, according to Section 3.4.4 as the big O analysis, although the time cost of EGA is lower than GA, they are basically in the same level. Although EGA is originally designed for the general searching problems where instance selection is chosen as a speci<sup>fi</sup>c domain problem for examination, further analyses about the EGA's ability in the high dimensional feature space should be made.

Finally, one major problem with the current instance selection algorithms, including EGA, is the scalability issue. For example, for the KDD Cup 2004 dataset, which contains 74 features and 145,751 data samples, it was found that EGA and IB3 (as one of the most ef<sup>fi</sup>cient state-ofthe-art algorithms) took about two weeks to complete the instance selection task. DROP3, on the other hand, required about four weeks.

To alleviate this problem and to ensure optimal EGA performance in terms of classi<sup>fi</sup>cation accuracy and computational cost over very large scale datasets, a divide-and-conquer strategy can be applied. First of all, each dataset can be divided into several non-duplicated and smaller sub sets where EGA can be performed over these subsets respectively (in parallel). Then, similar to the information fusion approach described above, multiple selection results corresponding to the divided subsets can be combined to form the <sup>fi</sup>nal reduced dataset.

## Appendix A

POP is the population N is the population size Or is the i-th individual

F is the <sup>fi</sup>tness matrix f is the <sup>fi</sup>tness value of each individual Non is the non-linear <sup>fi</sup>tness value of i-th individual Non is the non-linear <sup>fi</sup>tness matrix King is the kings of a generation K is the size of King (K b N) $K O _ { k }$ is the k-th member of the King MP is the mating pool $M P O _ { m } \in M P , m = 1 , 2 , . . . M$ M is the size of MP (M = N-K) f ∈ F, i = 1,2,…N $O r _ { i } \in P O P , i = 1 , 2 , . . . N$ $K O _ { k } \in K i n g , k = { 1 , 2 , . . . K }$ GF is the best <sup>fi</sup>tness of each generation G is the threshold for the great migration NG is the new generation

## 1. Initialize the population

Randomly generate N-individuals Or<sub>i</sub> to compose the population POP

Create an empty set of kings King

For i = 1,2,…N

POP ← Randomly generate $O r _ { i }$

End

Ø = King

## 2. Evaluate each individual from the new generation

Calculate the <sup>fi</sup>tness f for each individual, and then convert it to the non-linear <sup>fi</sup>tness Non

For i = 1,2,…N

f<sub>i</sub> ← Fitness function (Or<sub>i</sub>)

$$
N o _ {i} = \frac {f _ {i} - M i n (F)}{M a x (F) - M i n (F)}, i = 1, 2, \dots N
$$

$$
N o n _ {i} = \frac {\text { Hyperbolic\_Tangent } \left(\frac {N o _ {i} - \alpha}{\beta^ {2}}\right) + 1}{2}, i = 1, 2,... N
$$

End

## 3. Inter-generational mating

Select the top K individuals from POP based on the nonlinear <sup>fi</sup>tness Non to compose the King (Note that these K Kings do not participate in genetic operations)

For $k = 1 , 2 , . . . K$

King ← Select the $K O _ { k }$ from POP based on nonlinear <sup>fi</sup>tness Non (Top K)

End

## 4. Selection

Randomly select M-individuals $O r _ { m }$ from the population POP to be in the mating pool MP based for nonlinear <sup>fi</sup>tness Non (note that these individuals will participate in genetic operations)

For $m = 1 , 2 , . . . M$

MP ← Select the $O r _ { m }$ from POP based on nonlinear <sup>fi</sup>tness Non End

## 5. Mating

Crossover for each pair of the mating pool MP to generate the New Generation NG

For m = 1,2,…(M/2)

NG ← Crossover the $M P O _ { m }$ and $M P O _ { ( m \mathrm { ~ + ~ } M / 2 ) }$

End

## 6. Mutation

Random mutation for each individual $M P O _ { m }$ of the mating pool MP For m = 1,2,…M

$M P O _ { m } =$ Random Mutation the $M P O _ { m }$

End

7. Great migration

If the best <sup>fi</sup>tness value is stable then apply the great migration If there is no change in the best <sup>fi</sup>tness GF in G continuous generations then

Do a strong mutation for the new individuals NG (Local population) End

## 8. New generation

If the great migration is not applied in this generation then Combine the King and the new individuals NG to replace the existing population

Pop ← King∪NG

Else

Combine the foreign population (King) and the local population End

9. If stop conditions (iterations = 200) are met then stop; else return to step 2.

## References

[1] D.W. Aha, D. Kibler, M.K. Albert, Instance-based learning algorithms, Machine Learning 6 (1) (1991) 37–66.

[2] P. Ball, Natural strategies for the molecular engineer, Nanotechnology 13 (2002) (2002) R15–R28.

[3] H. Brighton, C. Mellish, Advances in instance selection for instance-based learning algorithms, Data Mining and Knowledge Discovery 6 (2002) 153–172.

[4] J.R. Cano, F. Herrera, M. Lozano, Using evolutionary algorithms as instance selection for data reduction: an experimental study, IEEE Transactions on Evolutionary Computation 7 (6) (2003) 561–575.

[5] D. Davidov, E. Gabrilovich, S. Markovitch, Parameterized generation of labeled datasets for text categorization based on a hierarchical directory, Proceedings of the ACM SIGIR Conference on Research and Development in Information Retrieval 2004, pp. 250–257.

[6] J. Derrac, S. García, F. Herrera, A survey on evolutionary instance selection and generation, International Journal of Applied Metaheuristic Computing 1 (1) (2010) 60–92.

[7] N.C. Ellstrand, Dangerous Liaisons: When Cultivated Plants Mate with Their Wild Relatives, Johns Hopkins University Press, 2003.

[8] T.H. Emigh, Comparison of tests for Hardy–Weinberg equilibrium, Biometrics 36 (4) (1980) 627-642

[9] P.G. Espejo, S. Ventura, F. Herrera, A survey on the application of genetic programming to classi<sup>fi</sup>cation, IEEE Transactions on Systems, Man, and Cybernetics – Part C: Applications and Reviews 40 (2) (2010) 121–144

[10] J.J. Flynn, A.R. Wyss, Recent advances in South American mammalian paleontology, Trends in Ecology and Evolution 13 (11) (1998) 449–454

[11] E. Gabrilovich, S. Markovitch, Text categorization with many redundant features: using aggressive feature selection to make SVMs competitive with C4.5, Proceedings of the International Conference on Machine Learning, 2004, pp. 321–328.

[12] S. García, J. Derrac, J.R. Cano, F. Herrera, Prototype selection for nearest neighbor classi<sup>fi</sup>cation: taxonomy and empirical study, IEEE Transactions on Pattern Analysis and Machine Intelligence 34 (3) (2012) 417–435.

[13] D.E. Goldberg, Genetic and evolutionary algorithms come of age, Communications of the ACM 37 (3) (1994) 113-119.

[14] D. Guo, R. Guo, C. Thiart, Predicting air pollution using fuzzy membership grade Kriging, Computers, Environment and Urban Systems 31 (2007) 33–51.

[15] H. Ishibuchi, T. Nakashima, M. Nii, Genetic-algorithm-based instance and feature selection, in: H. Liu, H. Motoda (Eds.), Instance Selection and Construction for Data Mining, Kluwer Academic, 2001.

[16] N. Jankowski, M. Grochowski, Comparison of instances selection algorithms I: algorithms survey, Proceedings of the International Conference on Arti<sup>fi</sup>cial Intelligence and, Soft Computing, 2004, pp. 598–603.

[17] A. Jacobs, The pathologies of big data, ACMQueue 7 (6) (2009) (Available at: http:// queue.acm.org/detail.cfm?id=1563874).

[18] K.P. Koep<sup>fl</sup>i, M.E. Gompper, E. Eizirik, C.C. Ho, L. Linden, J.E. Maldonado, R.K. Wayne, Phylogeny of the Procyonidae (Mammalia: Carvnivora): molecules, morphology and the Great American Interchange, Molecular Phylogenetics and Evolution 43 (3) (2007).1076-1095

[19] S. Lazebnik, C. Schmid, J. Ponce, Beyond bags of features: spatial pyramid matching for recognizing natural scene categorization, Proceedings of the JEEF International Conference on Computer Vision and Pattern Recognition, 2006, pp. 2169–2178.

[20] X.-B. Li, V.S. Jacob, Adaptive data reduction for large-scale transaction data, European Journal of Operational Research 188 (3) (2008) 910–924.

[21] S. Mitaim, B. Kosko, What is the best shape for a fuzzy set in function approximation? Proceedings of the IEEE International Conference on Fuzzy Systems, 1996, pp. 1237-1243.

[22] G.S. Morgan, Late Rancholabrean mammals from southernmost Florida and Neotropical influence in Florida Pleistocene Faunas, Smithsonian Contributions to Paleobiology 93 (2002) 15–38

[23] L. Nanni, A. Lumini, Prototype reduction techniques: a comparison among different approaches, Expert Systems with Applications 38 (2011) 11820–11828.

[24] H.T. Odum, Ecological and General Systems: An Introduction to Systems Ecology University Press of Colorado, 1994.

[25] M. Pollan, The year in ideas: A–Z, Genetic Pollution, The New York Times, December 9, 2001.

[26] S. Pradhan, X. Wu, Instance selection in data mining, Technical Report, Department of Computer Science University of Colorado at Boulder, 1999.

[27] D. Pyle, Data Preparation for Data Mining, Morgan Kaufmann, 1999.

[28] T. Reinartz, A unifying view on instance selection, Data Mining and Knowledge Discovery 6 (2002)191–210

[29] C. Stern, Wilhelm Weinberg, Genetics 47 (1962) 1–5.

[30] D.R. Wilson, T.R. Martinez, Reduction techniques for instance-based learning algorithms, Machine Learning 38 (2000) 257–286.

[31] I.H. Witten, E. Frank, M. Hall, Data Mining: Practical Machine Learning Tools and Techniques, Morgan Kaufmann, San Francisco, CA, 2011.

Dr. Chih-Fong Tsai received a PhD at School of Computing and Technology from the University of Sunderland, UK in 2005. He is now an associate professor at the Department of Information Management, National Central University, Taiwan. He has published more than 50 technical publications in journals, book chapters, and international conference proceedings. He received the Highly Commended Award (Emerald Literati Network 2008 Awards for Excellence) from Online Information Review (“A Review of Image Retrieval Methods for Digital Cultural Heritage Resources”), and the award for top 10 cited articles in 2008 from Expert Systems with Applications (“Using Neural Network Ensembles for Bankruptcy Prediction and Credit Scoring”). His current research focuses on multimedia information retrieval and data mining.

Mr. Zong-Yao Chen is currently a PhD student at the Department of Information Management, National Central University. His research interests cover machine learning evolutionary computing, and image processing
