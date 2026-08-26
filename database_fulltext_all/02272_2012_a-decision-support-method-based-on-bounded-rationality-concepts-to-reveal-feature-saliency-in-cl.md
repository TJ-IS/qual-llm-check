---
otero_id: 2272
otero_key: "4A4YERSX"
title: "A decision support method, based on bounded rationality concepts, to reveal feature saliency in clustering problems"
authors: "Barak Aviad; Gelbard Roy"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.037"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support method, based on bounded rationality concepts, to reveal feature saliency in clustering problems

Barak Aviad, Gelbard Roy ⁎

Information System Program, Graduate School of Business Administration, Bar-Ilan University, Ramat-Gan 52900, Israel

a r t i c l e i n f o

Article history: Received 26 March 2011 Received in revised form 29 April 2012 Accepted 21 May 2012 Available online 6 June 2012

Keywords: Feature selection Feature saliency Data mining Cluster analysis Classi<sup>fi</sup>cation Bounded-rationality

## a b s t r a c t

In many real-life data mining problems, there is no a-priori classi<sup>fi</sup>cation (no target attribute that is known in advance). The lack of a target attribute (target column/class label) makes the division process into a set of groups very dif<sup>fi</sup>cult to de<sup>fi</sup>ne and construct. The end user needs to exert considerable effort to interpret the results of diverse algorithms because there is no pre-de<sup>fi</sup>ned reliable “benchmark”. To overcome this drawback the current paper proposes a methodology based on bounded-rationality theory. It implements an S-shaped function as a saliency measure to represent the end user's logic to determine the features that characterize each potential group. The methodology is demonstrated on three well-known datasets from the UCI machine-learning repository. The grouping uses cluster analysis algorithms, since clustering techniques d not need a target attribute.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

“Data mining (DM) is rapidly becoming a front-runner in the academic and commercial area of managing and utilizing company data resources” [3]. A vast range of models and algorithms is now available as software packages that enable the end user to treat the data-mining model as a black box; i.e. users can create and implement a data-mining model without having a thorough understanding of the “bits and bytes”. However, having a good supply of algorithms is not enough. One of the most challenging issues when approaching a business problem with data mining tools is choosing the right algorithm and parameters for the task. Another crucial issue is analyzing the results and interpreting them correctly. The current paper focuses on a group of unsupervised learning algorithms known as cluster analysis (or clustering) algorithms. Clustering is an important <sup>fi</sup>eld in knowledge discovery, not only for enhanced understandability of datasets but also for the insights gained from clustering outputs and, ultimately, for effective decision making [27]. The goal of clustering techniques is to divide a population into groups (i.e. clusters-classes) that are different from one another (maximal distance between groups) but whose members are similar (minimal distance within each group). Unlike other classi<sup>fi</sup>cation techniques such as Decision Trees, Bayes-Nets, Neural-Nets and others, clustering techniques do not require a-priori information regarding the right classi<sup>fi</sup>cation (i.e. a target attribute-column which is known in advance), and therefore clustering techniques are particularly suitable for problems without a known target attribute and/or without a known number of classes. Such problems, where there is no prior de<sup>fi</sup>nition of the exact number of clusters, are quite common in business applications such as pricing, sales forecasting, CRM, network traf<sup>fi</sup>c, etc. [15,27,34,35,41]. The lack of a target attribute makes it hard for the end user to decide how many clusters should be de<sup>fi</sup>ned and consequently which algorithm will yield the best results. Furthermore, the resulting clusters (groups-classes) are not always meaningful, since they may not have any signi<sup>fi</sup>cant characteristics and therefore do not shed any light on the original business problem.

In order to overcome these dif<sup>fi</sup>culties, the current paper proposes a method based on an S-shape logistic function, which provides a heuristic method for the end user to determine the number of clusters in a way that reveals and pinpoints the signi<sup>fi</sup>cant attribute features as a function of their saliency. It is shown that the S-shape function, like the value function in prospect theory [26], satisfactorily represents the end user's decision logic (bounded-rationality rather than absolute optimization) in terms of detecting the attributefeatures that characterize the clusters. In this way, the proposed method delivers an automatic interpretation of the clustering results.

Currently, the model is designed to handle categorical (binary and nominal) attributes. The model is demonstrated and tested on three well-known datasets taken from the UCI machine learning repository website [18].

## 2. Background overview

## 2.1. Classification and clustering methods

The objective of data mining (DM) is to detect, interpret and predict qualitative and quantitative patterns in data, leading to an incremental level of information and knowledge. A wide variety of models and algorithms are employed from statistics, arti<sup>fi</sup>cial intelligence, neural nets and databases to machine learning [2,10]. In many cases, the goal of the DM model is to divide the dataset into groups. If the groups are pre-known, the problem is considered to be a classi<sup>fi</sup>cation problem. If the groups are not pre-known, the problem is considered to be a clustering problem.

In classi<sup>fi</sup>cation problems the objective is to assign a new object to the right class; in other words, to <sup>fi</sup>nd the correct Y category based on the observed X values [23]. Usually, classi<sup>fi</sup>cation is based on the statistical probability of obtaining each one of the possible values of the target attribute (target column/class label). There are several subgroups of algorithms for addressing classi<sup>fi</sup>cation problems, including:

• Decision trees — Decision trees provide useful solutions for many classi<sup>fi</sup>cation problems related to large datasets that often contain missing values or errors [4]. Typically, decision trees are used to solve classi<sup>fi</sup>cation problems by constructing rules for assigning objects to classes [25]. Despite the strengths of decision trees, generating a signi<sup>fi</sup>cant decision tree model can be impeded by the nature of the dataset. Classi<sup>fi</sup>cation trees can be unstable and sensitive to small variations in the data, such as those caused by randomization [1].

• Neural networks — In data analysis, arti<sup>fi</sup>cial neural networks are a class of <sup>fl</sup>exible nonlinear models used for supervised prediction problems. The basic building blocks of an arti<sup>fi</sup>cial neural network are called hidden units. Each hidden unit receives a linear combination of input variables. An activation function transforms the linear combinations and then outputs them to another unit that can then use them as inputs. The most widely used type of neural network in data analysis is the multilayer perceptron (MLP). An MLP is a feed forward network composed of an input layer, hidden layers composed of hidden units, and an output layer [23].

• Naive Bayes — A Bayes classi<sup>fi</sup>er is a simple probabilistic classi<sup>fi</sup>er based on applying Bayes' theorem with strong (naive) independence assumptions. In general, we simply estimate the probabilities that an object from each class will fall in each cell of the variable vector and then use Bayes' theorem to produce a classi<sup>fi</sup>cation [23].

• Logistic regression — Like the well known linear regression, this is a useful way of describing the relationship between one or more independent variables and a response variable by creating an equation describing the target attribute. In logistic regression the model predicts the probability of a particular level(s) of the target attribute at the given values of the input attributes. Because the predictions are probabilities, which are bounded by 0 and 1 and are not linear in this space, the probabilities must be transformed in order to be adequately modeled [23].

• Classi<sup>fi</sup>cation by clustering — A decision tree construction method based on a preliminary analysis using clustering techniques. The method is dubbed “classi<sup>fi</sup>cation by clustering” (CbC) because the decision rules are based on adjusted cluster analysis; i.e., on similarity functions rather than on the statistical associations between the attributes and the target attribute [6]. This method is new and not as well established as the other methods.

Unlike classi<sup>fi</sup>cation models, clustering algorithms do not use a target attribute. Instead, they attempt to decompose or partition a dataset into groups so that the entities in one group are similar to each other and are as different as possible from the entities in other groups [23]. The partition of the dataset is done by using similarity measures [2,11,17]. Much of the research in the area of clustering is designed to create better algorithms and data representation forms that are more appropriate for the clustering process. For example, Estivill-Castro and Yang [16] and Frey and Dueck [19] presented methods to choose entities as centers in “center approach” algorithms such as the k-means algorithm to improve their performance. Others, such as Erlich et al. [14], Meged and Gelbard [31,32] and Ryu and Eick [37], described representation methods to support improved similarity functions and fuzzy data elements. Studies such as Erman et al. [15] and Ngai et al. [35] applied theoretical concepts to speci<sup>fi</sup>c real-life problems and datasets that tend to experience much more noise and uncertainty than synthetic datasets.

It is well known that cluster analysis involves subjectivity, as does any similarity–distance measure. In addition, the same dataset is often partitioned in different ways by different applications [13]. Different clustering models at times generate very different results, and there is no way of knowing which is the right one or the best [22].

There are various kinds of clustering algorithms, which differ with respect to the similarity measures they use and the logic behind the division process. The two main algorithms (used in this paper) are:

• K-means — A clustering algorithm [30] that is available in many statistical and data mining toolkits. The algorithm divides the dataset into a pre-determined number of clusters according to the following steps: (i) choose k cluster centers randomly from the points (patterns) in the dataset. (ii) Assign each pattern to the closest cluster center. (iii) Re-compute the cluster centers using the current cluster membership. (iv) If a convergence criterion is not met, go to step ii. Typical convergence criteria are: no (or minimal) reassignment of patterns to new clusters, or a minimal decrease in the squared error. Several variations of the k-means algorithm have been reported in the literature [24].

• Two step — A clustering algorithm that consists of two passes over the dataset. The <sup>fi</sup>rst pass divides the dataset into a coarse set of sub-clusters, whereas the second pass groups the sub-clusters into the desired number of clusters. The desired number of clusters can be determined automatically, or it can be a pre-determined <sup>fi</sup>xed number of clusters [22].

Interpreting classi<sup>fi</sup>cation results (i.e. extracting their business insights) of the above-mentioned methods can be done in several ways. Decision tree results, for example, are interpreted based on the attributes and their values as de<sup>fi</sup>ned in each tree branch. Logistic regression results can be interpreted by analyzing the regression equation and its coef<sup>fi</sup>cients. Clustering methods results can be interpreted by exploring and understanding the attribute distribution of each cluster and comparing it to other clusters. However, all these interpretation techniques tend to be unstructured, dif<sup>fi</sup>cult to apply and time consuming. Since understanding the characteristics of each cluster or class is one of the main goals of the knowledge discovery process, a method and a measure for a convenient and structured interpretation of the results is essential as is determining the special characteristics of each class-cluster.

## 2.2. Uses of feature saliency

The saliency concept is widespread in various <sup>fi</sup>elds. In data mining a saliency measure is commonly used for feature selection tasks. Features may be unequally useful, some may be just noise, and thus not contribute, or even degrade the clustering process. Feature selection is de<sup>fi</sup>ned as selecting the “best” attribute subset from the entire available attributes [28], and is especially common in classi<sup>fi</sup>cation problems due to the existence of target attributes (target column/class labels). Because of the lack of target attributes in clustering problems, feature selection in such problems is more dif<sup>fi</sup>cult. Another concern in clustering is the determination of the number of clusters, which impacts as well as is in<sup>fl</sup>uenced by the feature selection issue [29]. However, there are methods to estimate feature saliency in clustering problems. Law et al. [29] applied feature saliency by embedding the estimation within an expectation–maximization (EM) algorithm. As in Law et al. [29], Raftery and Dean [36] attempted to determine which attribute contributes most to the overall cluster structure by utilizing the power of <sup>fi</sup>nite mixture models. However, unlike Law et al. [29], the attributes were chosen by model comparison instead of having their [relevance] weight estimated as part of the EM algorithm. Dy and Brodley [12] utilize <sup>fi</sup>nite mixture modeling of multivariate normal distributions to cluster observations. The COSA procedure [20] detects subsets of observations that cluster subsets of the attributes rather than all of them simultaneously. Montanari and Lizzani [33] proposed a feature selection procedure for cluster analysis based on the principles of projection pursuit. Steinley and Brusco's [39] procedure takes advantage of a variable weighting technique that determines the relative clusterability of each variable in the system, which is particularly advantageous in the presence of skewed random noise. The heuristic identi<sup>fi</sup>cation of noisy variables [9] was developed to help isolate potentially noisy variables prior to clustering, especially when using the K-means clustering algorithm. Brusco and Cradit [8] presented a variable-selection heuristic for nonhierarchical (K-means) cluster analysis based on the adjusted Rand index for measuring cluster recovery. A method for simultaneous key phrase extraction and generic text summarization was proposed by Zha H. [42] that uses clustering algorithms to partition sentences into topical groups and saliency scores for key phrases and sentence rankings.

A large-scale test and comparison of some of the above methods was conducted by Steinley and Brusco [40] based on 20,412 generated datasets. This overview showed that although some of the methods perform less well when non-informative variables (i.e., random noise) are included in the model, most of them are useful and yield improvements in clustering results.

The current paper presents an additional approach to feature saliency. Unlike the saliency measures used for feature selection techniques, which are applied before or during the creation of clusters, the proposed method uses the saliency measure only after the clusters have been determined. This is because its objective is different: whereas the aim of feature selection is to determine the best or most parsimonious set of variables for the algorithm, the goal of the proposed model is to determine the features that lead to maximal differentiation of each cluster on the basis of its members.

## 2.3. Bounded rationality and prospect theory

The term “bounded rationality” refers to the fact that most people are only partly rational in their daily decision-making. This contrasts with the dominant early 20th century economic theory that assumed that decision-making was the fully rational process of <sup>fi</sup>nding an optimal choice given the available information. Herbert Simon [38] <sup>fi</sup>rst suggested that we use heuristics to make our decisions rather than a strict rigid rule of optimization. Kahneman and Tversky [26] proposed a normative model that can be formalized mathematically. They argued that since decision-makers usually do not have the ability or resources to reach an optimal solution, they tend to settle for a satisfactory solution instead. Prospect theory describes decision-making between alternatives with uncertain outcomes; i.e., ones that involve an element of risk, with known probabilities. The theory is considered to be a psychologically realistic alternative to expected utility theory, in which values and probabilities are assigned to gains and losses rather than to <sup>fi</sup>nal assets. The value function is normally concave for gains, commonly convex for losses, and is generally steeper for losses than for gains. Decision weights are generally lower than the corresponding probabilities, except in the range of low probabilities.

The formula for the utility evaluation is:

$$
\mathrm{U} = \sum_ {\mathrm{i} = 1} ^ {\mathrm{n}} \mathrm{w} (\mathrm{p} _ {\mathrm{i}}) v (\mathrm{x} _ {\mathrm{i}}) = \mathrm{w} (\mathrm{p} _ {1}) v (\mathrm{x} _ {1}) + \mathrm{w} (\mathrm{p} _ {2}) v (\mathrm{x} _ {2}) + \dots + \mathrm{w} (\mathrm{p} _ {\mathrm{n}}) v (\mathrm{x} _ {\mathrm{n}})
$$

where:

<table><tr><td>U</td><td>the utility</td></tr><tr><td>Xi</td><td>the potential outcomes (n possible outcomes)</td></tr><tr><td>Pi</td><td>the respective probabilities</td></tr><tr><td>V</td><td>the value function</td></tr><tr><td>W</td><td>the probability weighting function.</td></tr></table>

Unlike expected utility theory, the prospect theory value function (V) measures losses and gains and not absolute wealth. For that reason, it is S-shaped and passes through a reference point. The reason it is asymmetric is the larger impact of losses than gains. The probability weighting function (W) expresses the fact that people tend to overreact to events with low probabilities but under-react to events with medium and high probabilities.

## 2.4. The S-shaped logistic function and its uses

The logistic function is an S-shaped mathematical function and although various forms of the function may involve using several parameters that control its behavior, its simplest form is de<sup>fi</sup>ned by the following equation: $\begin{array} { r } { \mathsf { y } = \frac { 1 } { 1 + \mathsf { e } ^ { - \mathrm { x } } } } \end{array}$

The y values of the function have two asymptotes, 0 for negative x values and 1 for positive x values. However, in a good approximation, the function has values between 0 and 1 for x inputs that vary between −10 and 10. The logistic function has many uses in various <sup>fi</sup>elds of science. One of these is the logistic regression that was mentioned above. The logistic function is suitable for this purpose because it can take any value from negative in<sup>fi</sup>nity to positive in<sup>fi</sup>nity as input, whereas the output is con<sup>fi</sup>ned to values between 0 and 1. The input variables are a set of independent variables, whereas the function output represents the probability of a particular outcome, given that set of explanatory variables. Another common use of the logistic function can be found in item response theory (IRT) which is nowadays the preferred concept for high stake tests such as the Graduate Record Examination (GRE) and the Graduate Management Admission Test (GMAT). This method is based on the application of mathematical models to the testing data and is used for the design, analysis and scoring of tests, questionnaires, and similar instruments that measure abilities, attitudes, or other variables. For a certain item (question) on a test, the probability of a correct response is near zero at the lowest levels of ability. It increases to the highest levels of ability, at which point the probability of a correct response approaches 1. This S-shaped curve describes the relationship between the probability of a correct response to an item and the ability scale of the person being tested. In item response theory, the S curve is known as the item characteristic curve [5]. Under item response theory, the standard mathematical model for the item characteristic curve is the cumulative form of the logistic function. It de<sup>fi</sup>nes a family of curves having the general shape of the item characteristic curves. It was <sup>fi</sup>rst used as a model for the item characteristic curve in the late 1950s and, because of its simplicity, has become the preferred model [5].

## 2.5. Determining the number of clusters

Unsupervised learning (clustering); i.e., a problem without a prior de<sup>fi</sup>nition of the exact number of clusters, arises in diverse business applications. The lack of target attribute (target column/class labels) makes it dif<sup>fi</sup>cult for the user to decide how many clusters should be created and consequently which algorithm will yield the best results. A popular method for visualizing the decision-space for the determination of the number of clusters is the dendrogram. A dendrogram is a tree graph that represents the arrangement of the clusters according to the similarity levels measured among samples and sub-groups of two or more samples. The dendrogram can be broken at different levels to yield different clusterings of the data [24]. Although the dendrogram is a popular tool, it is important to note that a dendrogram can only represent a single algorithm at a time and cannot compare or utilize multiple algorithms simultaneously [7]. Another visualization tool that can also be used to determine the number of clusters is Multi‐Algorithm Voting (MAV) proposed by Bittmann and Gelbard [7]. MAV enables a cross algorithm presentation in which all clusters are presented together in a “tetris-like format” in which each column represents a speci<sup>fi</sup>c algorithm, each line represents a speci<sup>fi</sup>c sample case, and each color represents a “vote” (i.e. decision suggestion, formed by a speci<sup>fi</sup>c algorithm for a speci<sup>fi</sup>c sample case). MAV methodology helps determine the <sup>fi</sup>nal clusters after taking into consideration all the clustering algorithms tested, and resolves the problem of arbitrary decision-making concerning the number of clusters in that it determines where to “cut” the dendrogram.

```txt
i attribute index  
j attribute value index  
Ji number of possible values for attribute i  
k cluster index  
Rij the % of entities with value j of attribute i in the total population  
Rijk the % of entities with value j of attribute i in cluster k  
Pijk the probability for a user to decide that cluster k is characterized by entities with value j for attribute i.
```

Since all the methods mentioned above rely on inner similarity measures to determine the number of clusters, none of them ensure the saliency of the results (i.e. that the clusters created by the model have speci<sup>fi</sup>c and meaningful characteristics). By using the model proposed in this paper, it is possible to determine the desired number of clusters based on the desired attribute saliency and therefore achieve meaningful and useful results.

## 3. The proposed model

## 3.1. Model aims

The proposed model enables a user to select a suitable clustering algorithm and determine the number of clusters in a way that reveals and pinpoints the signi<sup>fi</sup>cant attribute features in the dataset according to their saliency. To do so, it has to <sup>fi</sup>nd the attributes that characterize each of the clusters; in other words, those attributes that describe the entities of the cluster. Since the main reason for using clustering techniques is to detect special and well-de<sup>fi</sup>ned sub-groups in the dataset, we also expect the proposed model to provide a measure to assess the ability of the clustering results to produce clusters which have these special characteristics, and thus help the user choose between different clustering algorithms and determine the number of clusters desired.

## 3.2. Model factors — the probability function

The desired probability function should represent the probability of a typical user to decide that a certain cluster is characterized by a speci<sup>fi</sup>c attribute. This function is mainly dependent on two features: (i) the distribution of the attribute within the cluster; (ii) the distribution of the attribute in the entire dataset. For example, imagine the following scenario: assume a dataset containing the gender attribute (male/ female) which is evenly distributed in the entire dataset population (50% each). In one of the clusters produced by a clustering algorithm, the percentage of males is 55%. It is obvious that the probability of determining that this cluster is characterized by males is low because 55% is close to the general population distribution. However, if the percentage of males in a cluster is 95%, the probability of determining that this cluster is characterized by males is much higher. In addition, it is possible to say that gender is a signi<sup>fi</sup>cant attributefeature of this cluster. The association between the attribute's distribution within a cluster and its distribution in the entire population determines our perception of whether a cluster is characterized by a speci<sup>fi</sup>c attribute. For this reason, we want to create a probability function that returns values between 0 and 1 according to an attribute's saliency. In other words, its rate should increase as the distance between the distributions of the attribute within a cluster and in the entire population increases.

The function needed for this task should be very similar to the value function used in prospect theory depicted in Fig. 1. The reference point is the total distribution of the attribute in the entire population and instead of losses and gains we measure the distance between the cluster attribute's distribution and the distribution of the entire population. The user actually assigns a value to this difference and the result represents the probability that the user will decide that a certain attribute characterizes a certain cluster. The desired function should be S-shaped because its slope must be maximal around the reference point and minimal around the edges. The only difference between the desired function in our case and the prospect theory value function is the fact that our function should be symmetric because there is no reason to give more or less value to positive or negative distances in relation to the reference point. A mathematical function suitable for this purpose is the logistic function (as described in Section 2) because it has all the desired qualities and built-in parameters for the task. In all of the equations below we use the following notations:

![](/api/attachments/4A4YERSX/fulltext/images/3d77d272c5fb1cc4fbe5ad0d7fe2cc021e820965bd094d8dec74aed39735f753.jpg)  
Fig. 1. A value function.

The probability for a user to decide that cluster k is characterized by entities with value j in attribute i can be written as:

$$
\mathrm{P} _ {\mathrm{ijk}} = \frac {1}{1 + \mathrm{e} ^ {- (\alpha + \beta \mathrm{x})}}.\tag{1}
$$

The x value in Eq. (1) is the difference between Rijk and Rij (which ranges between −1 and 1) multiplied by 10 to get values between −10 and 10 (in this range the logistic function returns values between 0 and 1). This manipulation is equivalent to setting beta to a constant value of 10.

$$
\mathrm{x} = 1 0 \cdot \left(\mathrm{R} _ {\mathrm{ijk}} - \mathrm{R} _ {\mathrm{ij}}\right)\tag{2}
$$

This logistic based function returns values between 0 and 1 and ensures a steep slope for x values close to 0 (Rijk is close to Rij) because this is the range where every change in Rijk (the inner distribution of a certain cluster) impacts the probability substantially. For x values closer to the edges (Rijk far from Rij) the slope of the function is much more moderate because in this area changes in Rijk have a small effect on the probability.

## 3.3. Model factors — alpha and beta

The next step is to describe the appropriate behavior of the function along its possible x values. The two parameters that affect this are alpha and beta. Alpha has a strong correlation to the intercept of the function and the Y-axis, and beta affects the slope of the function around the curve point. As mentioned above, beta was set to a constant value of 10 (Eq. (1)); thus only alpha is used as a dynamic parameter.

Table 1  
Lenses dataset clustering results.

<table><tr><td>Attribute name</td><td>Attribute value</td><td>Cluster 1</td><td>Cluster 2</td><td>Cluster 3</td><td>Rij</td></tr><tr><td>Age</td><td>1</td><td>0.50</td><td>0.40</td><td>0.27</td><td>0.33</td></tr><tr><td>Age</td><td>2</td><td>0.25</td><td>0.40</td><td>0.33</td><td>0.33</td></tr><tr><td>Age</td><td>3</td><td>0.25</td><td>0.20</td><td>0.40</td><td>0.33</td></tr><tr><td>Spectacle</td><td>1</td><td>0.75</td><td>0.40</td><td>0.47</td><td>0.50</td></tr><tr><td>Spectacle</td><td>2</td><td>0.25</td><td>0.60</td><td>0.53</td><td>0.50</td></tr><tr><td>Astigmatic</td><td>1</td><td>0.00</td><td>1.00</td><td>0.47</td><td>0.50</td></tr><tr><td>Astigmatic</td><td>2</td><td>1.00</td><td>0.00</td><td>0.53</td><td>0.50</td></tr><tr><td>Tear</td><td>1</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.50</td></tr><tr><td>Tear</td><td>2</td><td>1.00</td><td>1.00</td><td>0.20</td><td>0.50</td></tr><tr><td>No. of entities</td><td></td><td>4</td><td>5</td><td>15</td><td>24</td></tr></table>

In order to obtain the behavior of the function for our purposes, the intercept with the Y-axis should relate to the distribution of the entire population (Rij). To see this, take the imaginary example mentioned above (a population of evenly distributed males and females, $\mathrm { i . e . \ R i j } = 0 . 5 )$ . Since there is only one attribute in this example, the notation Rij can conveniently be replaced by R. If one cluster of people has 50% males, there is no reason to favor any gender when deciding whether males or females characterize the cluster. In this case the probability of deciding that the cluster is characterized by males (or females) is 50% $( \mathrm { R } = 0 . 5 , \mathrm { X } = 0 , \mathrm { Y } = 0 . 5 )$ . If the cluster contains 60% males, the probability to decide that it is characterized by males should be higher and increase with a rise in the percentage of males in the cluster $( \mathrm { R } = 0 . 5 , \ \mathrm { X } > 0 , \ \mathrm { Y } > 0 . 5 )$ . If the cluster contains 40% males, the probability of deciding that it is characterized by males should be lower than 50% and decrease with the rise in the percentage of females in the cluster $( \mathtt { R } = 0 . 5 , \mathtt { X } { < } 0 , \mathtt { Y } { < } 0 . 5 )$

Now let's assume that the total population contains 80% males. In a cluster which also contains 80% males, despite the fact that the male percentage is no different than the entire population, we can no longer say that there is no reason to favor either gender when deciding which gender characterizes the cluster. We cannot ignore the fact that there are many more males in the cluster and therefore the probability must be greater than 50%, up to 80% $( \mathtt { R } = 0 . 8 , \mathtt { X } = 0 , \mathtt { Y } \approx 0 . 8 )$ . The same rationale can be applied in a case where the male percentage in the total population is 20%. In this case, the probability of deciding that a cluster with 20% males is characterized by males must be lower than 50%, down to 20% $( \mathrm { R } = 0 . 2 , \mathrm { X } = 0 , \mathrm { Y } \approx 0 . 2 )$

A practical way to extract the above described behavior from the probability function is by the intercept with the Y-axis; i.e. when ${ \tt X } = 0 , { \tt Y } = { \tt R i j }$ , that is R (Rij).

$$
\frac {1}{1 + \mathrm{e} ^ {- \alpha}} = R _ {\mathrm{ij}} \rightarrow \alpha = - \ln \left(\frac {1}{R _ {\mathrm{ij}}} - 1\right)\tag{3}
$$

Lenses dataset probability matrix.

<table><tr><td rowspan="2">Serial number</td><td rowspan="2">Attribute name</td><td rowspan="2">Attribute value</td><td>A</td><td>B</td><td>C</td></tr><tr><td>Cluster 1</td><td>Cluster 2</td><td>Cluster 3</td></tr><tr><td>1</td><td>Age</td><td>1</td><td>0.73</td><td>0.49</td><td>0.20</td></tr><tr><td>2</td><td>Age</td><td>2</td><td>0.18</td><td>0.49</td><td>0.33</td></tr><tr><td>3</td><td>Age</td><td>3</td><td>0.18</td><td>0.12</td><td>0.49</td></tr><tr><td>4</td><td>Spectacle</td><td>1</td><td>0.92</td><td>0.27</td><td>0.42</td></tr><tr><td>5</td><td>Spectacle</td><td>2</td><td>0.08</td><td>0.73</td><td>0.58</td></tr><tr><td>6</td><td>Astigmatic</td><td>1</td><td>0.00</td><td>1.00</td><td>0.42</td></tr><tr><td>7</td><td>Astigmatic</td><td>2</td><td>1.00</td><td>0.00</td><td>0.58</td></tr><tr><td>8</td><td>Tear</td><td>1</td><td>0.00</td><td>0.00</td><td>0.95</td></tr><tr><td>9</td><td>Tear</td><td>2</td><td>1.00</td><td>1.00</td><td>0.05</td></tr></table>

![](/api/attachments/4A4YERSX/fulltext/images/575c86ab9249321a4e460a0abf3ced208bf1b0df82307eb77e39248b153c37f3.jpg)  
Fig. 2. What-if analysis results for cell A4 in Table-2.

Since the basis of the association between alpha and R is psychological, as described by Kahneman and Tversky in 1979, it can only be empirically supported, not mathematically. As an illustration, we used the Lenses dataset taken from the UCI machine learning repository web site [18]. The dataset contains only 24 records (and therefore is very useful for demonstration purposes) with four attributes:

• Age of the patient: (1) young, (2) pre-presbyopic and (3) presbyopic

• Spectacle prescription: (1) myope and (2) hypermetrope

• Astigmatic: (1) no and (2) yes

• Tear production rate: (1) reduced and (2) normal.

There are three known sub-groups in the dataset. After applying a clustering algorithm on the dataset (K-Means with 3 clusters), we obtained the results shown in Table 1 (the table contains the inner distribution of the attributes for each cluster with respect to the distribution of the entire dataset, Rij).

By using the probability function, we obtain the probability matrix shown in Table 2 (each cell represents the probability of deciding that cluster k is characterized by the value j of attribute i).

The results in cells A6–B9 (the black cells) are trivial. Since all the records in Cluster 2 have a value $\mathrm { o f } ^ { \cdots } 1 ^ { \mathfrak { n } }$ in the astigmatic attribute, we expect the function to return a probability of 100% to decide that this cluster is characterized by entities with a value of $" 1 "$ in this attribute. Similarly, if there are no entities of a certain value in a cluster, the function returns a probability value of 0%, as we would expect it to do.

The gray cells (A4 and C8) represent a case in which there is a signi<sup>fi</sup>cant difference between the inner distribution of an attribute in a cluster and the total population. In this case the function returns a high value (close to 100%) because the probability the user will decide this cluster is characterized by this attribute is very high. All of the other cells in the probability matrix indicate the same thing; thus the probability function returns higher values for clusters and attributes with a signi<sup>fi</sup>cant difference in distribution compared to the total population.

![](/api/attachments/4A4YERSX/fulltext/images/92b732d799cf9622f43e045d6598bee132da0c320bc1488e41a9dd22650d5c3a.jpg)  
Fig. 3. What-if analysis results for cell B4 in Table-2.

![](/api/attachments/4A4YERSX/fulltext/images/3ffed8699ebf24000cb67fc2e4c11a689bf87ba2ea57a6a95a5ba31e62446812.jpg)

![](/api/attachments/4A4YERSX/fulltext/images/0c3de76165c25edcb15f3d72c9f72f936ef0bcf2b39e8a84b8f9928ba9d520f2.jpg)  
Fig. 4. Saliency values of train data and test data for Dataset 1.

Note that the sum of the probabilities of the various values of a certain attribute in a certain cluster (for example, cells A1–A3) may not be exactly 1. This is because the probability function curve (as shown in Eqs. (1)–(3)) is dependent on Rij (the percentage of entities with value j of attribute i in the total population). Therefore, each cell represents the output of a different probability curve, based on the relevant Rij.

## 3.4. Model factors — relations between alpha and the probability function

Using the probability matrix in Table 2 we can con<sup>fi</sup>rm that the alpha value calculated in Eq. (3) is appropriate for a probability function that describes a rational user's decision rule. For example, cell A4 describes the probability for a user to decide that Cluster no. 1 is characterized by records with value $" 1 "$ in the spectacle attribute. We can see that 75% of the entities in this cluster are $" 1 "$ whereas the total $" 1 "$ rate in the population is 50%. Given these terms we should expect the probability function to return a high value because the $" 1 "$ rate in the cluster is high both absolutely (close to 100%) and relatively (higher than the total population rate). In fact, the probability function returns a high value of 92% for this cell. The alpha value calculated by Eq. (3) is 0 (because $\mathrm { R i j } = 0 . 5 )$ . Next, let's conduct a what-if analysis by changing the alpha values and explore the results returned by the probability function (shown in Fig. 2).

For alpha values higher than 1, the results do not change dramatically because they only increase the probability of deciding that the cluster is characterized by entities with a value $\mathrm { o f } ^ { \cdots } 1 ^ { \ " }$ in the spectacle attribute (which was high to begin with). However, alpha values lower than 0 will rapidly decrease the probability to decide that the cluster is characterized by entities with a value $\mathrm { o f } ^ { \cdots } 1 ^ { \ " }$ in the spectacle attribute. For example, if alpha $= - 2$ , the probability of deciding that the cluster is characterized by $" 1 "$ values is about 60% and if alpha= −3 it is as low as 40%. It is obvious that such a low probability is erroneous and does not accurately describe the actual decision a user will make in this case.

![](/api/attachments/4A4YERSX/fulltext/images/aff38866f2990eaf9f53365bf884c1f49d67627adbab7b4d89e52b16805f07fa.jpg)  
Fig. 5. Number of clusters and the saliency measure for Dataset 1.

Another example is cell B4 that describes the probability of deciding that Cluster no. 2 is characterized by entities with a value of $" 1 "$ in the spectacle attribute. We can see that 40% of the records in this cluster are $" 1 "$ whereas the total $" 1 "$ rate in the population is 50%. Given the circumstances we expect that the probability function will return a low value because the $" 1 "$ rate in the cluster is low both absolutely (smaller than 50%) and relatively (lower than the total population). In fact, the probability function returns a low value of only 27%. The alpha value calculated by Eq. (3) is 0 (because Rij=0.5). Fig. 3 shows the results of the what-if analysis, using the same method as explained above.

It is clear that alpha values lower than −1 do not change the results dramatically because they only decrease the probability of deciding that the cluster is characterized by value $" 1 "$ entities (which was low to begin with). However, an alpha value higher than 0 will rapidly increase the probability of deciding the cluster is characterized by value $" 1 "$ entities. For example, if alpha=2, the probability of deciding the cluster is characterized by value $" 1 "$ entities is about 75% and if alpha=3 it is as high as 90%. It is obvious that such a high probability is erroneous and does not describe the actual decision a user will make in this case.

The probability function does not depend speci<sup>fi</sup>cally on Rij or Rijk; rather, it depends on the distance between them (as denoted in Eq. (2)). Therefore, the what-if analysis presented here is applicable to every combination of Rij and Rijk, and under the assumptions of prospect theory regarding the S-shape of a user's decision making logic, the alpha values as calculated in Eq. (3) are good approximation for that behavioral rationale. However, for signi<sup>fi</sup>cantly different alpha values, the probability results can change rapidly, become illogical, and not capture the user's decision logic.

Dataset 1 clustering results.

<table><tr><td>Attribute name</td><td>Attribute value</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>Rij</td></tr><tr><td rowspan="7">a1</td><td>36</td><td>0.17</td><td>0.25</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.08</td></tr><tr><td>37</td><td>0.39</td><td>0.58</td><td>0.00</td><td>0.40</td><td>0.00</td><td>0.25</td></tr><tr><td>38</td><td>0.17</td><td>0.17</td><td>0.00</td><td>0.60</td><td>0.21</td><td>0.21</td></tr><tr><td>39</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.21</td><td>0.04</td></tr><tr><td>40</td><td>0.06</td><td>0.00</td><td>0.48</td><td>0.00</td><td>0.14</td><td>0.16</td></tr><tr><td>41</td><td>0.22</td><td>0.00</td><td>0.48</td><td>0.00</td><td>0.36</td><td>0.24</td></tr><tr><td>42</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.00</td><td>0.07</td><td>0.03</td></tr><tr><td rowspan="2">a2</td><td>Yes</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.26</td></tr><tr><td>No</td><td>1.00</td><td>1.00</td><td>0.00</td><td>1.00</td><td>1.00</td><td>0.74</td></tr><tr><td rowspan="2">a3</td><td>Yes</td><td>0.72</td><td>0.00</td><td>1.00</td><td>0.00</td><td>1.00</td><td>0.60</td></tr><tr><td>No</td><td>0.28</td><td>1.00</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.40</td></tr><tr><td rowspan="2">a4</td><td>Yes</td><td>0.00</td><td>1.00</td><td>0.57</td><td>1.00</td><td>1.00</td><td>0.66</td></tr><tr><td>No</td><td>1.00</td><td>0.00</td><td>0.43</td><td>0.00</td><td>0.00</td><td>0.34</td></tr><tr><td rowspan="2">a5</td><td>Yes</td><td>0.00</td><td>1.00</td><td>1.00</td><td>0.53</td><td>0.00</td><td>0.51</td></tr><tr><td>No</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.47</td><td>1.00</td><td>0.49</td></tr><tr><td rowspan="2">a6</td><td>Yes</td><td>0.00</td><td>1.00</td><td>0.14</td><td>0.00</td><td>1.00</td><td>0.36</td></tr><tr><td>No</td><td>1.00</td><td>0.00</td><td>0.86</td><td>1.00</td><td>0.00</td><td>0.64</td></tr><tr><td>No. of entities</td><td></td><td>18</td><td>12</td><td>21</td><td>15</td><td>14</td><td>80</td></tr></table>

Table 4  
Dataset 1 probability matrix.

<table><tr><td>Attribute name</td><td>Attribute value</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td></tr><tr><td rowspan="7">a1</td><td>36</td><td>0.17</td><td>0.32</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>37</td><td>0.57</td><td>0.90</td><td>0.00</td><td>0.60</td><td>0.00</td></tr><tr><td>38</td><td>0.15</td><td>0.15</td><td>0.00</td><td>0.93</td><td>0.22</td></tr><tr><td>39</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.19</td></tr><tr><td>40</td><td>0.06</td><td>0.00</td><td>0.82</td><td>0.00</td><td>0.14</td></tr><tr><td>41</td><td>0.21</td><td>0.00</td><td>0.77</td><td>0.00</td><td>0.51</td></tr><tr><td>42</td><td>0.00</td><td>0.00</td><td>0.03</td><td>0.00</td><td>0.04</td></tr><tr><td rowspan="2">a2</td><td>Yes</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.00</td></tr><tr><td>No</td><td>1.00</td><td>1.00</td><td>0.00</td><td>1.00</td><td>1.00</td></tr><tr><td rowspan="2">a3</td><td>Yes</td><td>0.84</td><td>0.00</td><td>1.00</td><td>0.00</td><td>1.00</td></tr><tr><td>No</td><td>0.16</td><td>1.00</td><td>0.00</td><td>1.00</td><td>0.00</td></tr><tr><td rowspan="2">a4</td><td>Yes</td><td>0.00</td><td>1.00</td><td>0.44</td><td>1.00</td><td>1.00</td></tr><tr><td>No</td><td>1.00</td><td>0.00</td><td>0.56</td><td>0.00</td><td>0.00</td></tr><tr><td rowspan="2">a5</td><td>Yes</td><td>0.00</td><td>1.00</td><td>1.00</td><td>0.56</td><td>0.00</td></tr><tr><td>No</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.44</td><td>1.00</td></tr><tr><td rowspan="2">a6</td><td>Yes</td><td>0.00</td><td>1.00</td><td>0.06</td><td>0.00</td><td>1.00</td></tr><tr><td>No</td><td>1.00</td><td>0.00</td><td>0.94</td><td>1.00</td><td>0.00</td></tr></table>

## 3.5. Model factors — the saliency measure

After showing that the proposed probability function can accurately describe a rational decision rule, it is now possible to use it to assess the results of the clustering division and its ability to produce clusters with signi<sup>fi</sup>cant characteristics. As mentioned above, clustering techniques are used to divide a certain population into meaningful clusters with unique characteristics. Therefore, a useful clustering result is one that creates a set of clusters with a maximal number of signi<sup>fi</sup>- cant attribute features. For this purpose the saliency measure is de<sup>fi</sup>ned as follows:

$$
D _ {i j k} = \left\{ \begin{array}{l l} 1 & P _ {i j k} \geq T \\ 0 & P _ {i j k} <   T \end{array} \right.\tag{4}
$$

$$
S = \frac {1}{\sum_ {\mathrm{i}} \mathrm{J} _ {\mathrm{i}}} \sum_ {\mathrm{i}} \sum_ {\mathrm{j}} \left(\frac {\sum_ {\mathrm{k}} D _ {\mathrm{ijk}} \cdot R _ {\mathrm{ijk}} \cdot N _ {\mathrm{k}}}{R _ {\mathrm{ij}} \cdot N}\right)\tag{5}
$$

where:

S the saliency measure

T the threshold value: if Pijk is greater than this threshold, value j of attribute i is considered to be a characteristic of cluster k

Dijk a binary value that becomes 1 if value j of attribute i is considered to be a characteristic of cluster k

Nk the number of entities in cluster k

N the total number of entities.

The saliency measure is de<sup>fi</sup>ned as the total average of the percentages of signi<sup>fi</sup>cant entities, for all possible values of all attributes. A signi<sup>fi</sup>cant entity percentage for attribute i with value j is the number of entities belonging to a cluster which is characterized by value j of attribute i, divided by the total number of entities with value j of attribute i. For example, S=0.5 means that the average percentage of signi<sup>fi</sup>cant entities for all possible values of all attributes is 50%. A high saliency value ensures that the clustering results are signi<sup>fi</sup>cant and useful because it enables the user to describe the special characteristics of each cluster using large numbers of attributes.

Table 5  
Dataset 1 salient features in each cluster.

<table><tr><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td></tr><tr><td>a2 = no</td><td>a1 = 37</td><td>a2 = yes</td><td>a1 = 38</td><td>a2 = no</td></tr><tr><td>a4 = no</td><td>a2 = no</td><td>a3 = yes</td><td>a2 = no</td><td>a3 = yes</td></tr><tr><td>a5 = no</td><td>a3 = no</td><td>a5 = yes</td><td>a3 = no</td><td>a4 = yes</td></tr><tr><td>a6 = no</td><td>a4 = yes</td><td>a6 = no</td><td>a4 = yes</td><td>a5 = no</td></tr><tr><td></td><td>a5 = yes</td><td></td><td>a6 = no</td><td>a6 = yes</td></tr><tr><td></td><td>a6 = yes</td><td></td><td></td><td></td></tr></table>

Table 6  
Dataset 1 comparison of classi<sup>fi</sup>cation errors.

<table><tr><td>Model</td><td>Disease 1 Classification errors</td><td>Disease 2 Classification errors</td></tr><tr><td>C5 decision tree</td><td>0</td><td>0</td></tr><tr><td>Logistic regression</td><td>0</td><td>0</td></tr><tr><td>K-means5 (saliency)</td><td>1</td><td>0</td></tr></table>

The saliency measure values range from 0 (when the distributions of the attributes in all clusters are similar to their distribution in the entire population) to 1 (when the distributions of attributes in all clusters are signi<sup>fi</sup>cantly far from their distribution in the entire population). It is obvious that as the number of clusters provided by the clustering algorithm increases, the saliency measure rises as well. Therefore, the measure can be used in two ways: (i) relatively, by comparing results of different clustering algorithms which divide the population into an identical number of clusters; (ii) as a stop rule in a clustering process, to determine the required number of clusters needed to achieve the desired saliency level.

## 3.6. Model stages

The following sequence outlines the stages in the proposed model:

1. Run the candidate algorithms on the dataset (the algorithms and number of clusters in each are not restricted as long as they are suitable for the dataset).

2. Calculate the inner distribution (Rijk) for each attribute value of each attribute of every cluster.

3. Calculate the probability function value (Pijk) for each attribute value of each attribute of every cluster (the probability matrix).

4. Set a threshold for the desired Pijk value according to the user's demands and the dataset.

5. Calculate the saliency measure for every algorithm and compare the results.

6. Choose the most suitable algorithm and number of clusters.

7. Analyze the results by <sup>fi</sup>nding the characterizing attributes in each cluster (by comparing the value of the probability function to the threshold de<sup>fi</sup>ned in step 4).

The threshold setting can be done as an iterative process. In case the results are unsatisfying the threshold can be re-set and the procedure goes back to stage 4.

## 4. Research method and model evaluation

## 4.1. The datasets

The proposed model was tested and evaluated on two well-known datasets taken from the UCI machine learning repository [18] which is considered to be a common source for “real world” datasets. Although both of these datasets were originally used for classi<sup>fi</sup>cation problems (i.e. there is a target attribute), in this case we ignored the target attribute because the goal was to create clusters based on the data. The <sup>fi</sup>rst dataset, Acute Inflammations, contains medical data such as temperature, occurrence of nausea, lumbar pain, etc. of 120 patients.

![](/api/attachments/4A4YERSX/fulltext/images/ce09acdb302c1a9c9ce005b98f68e7619ec0d7fbe6a7016a35649b931f2a145a.jpg)

![](/api/attachments/4A4YERSX/fulltext/images/fa87e707fc1b48c1528641bc6b6de8b983aae36290169879c223e5d06f57adbc.jpg)  
Fig. 6. Saliency values of train data and test data for Dataset 2

The temperature values, which originally were continuous, were modi<sup>fi</sup>ed to create discrete categories. There are diverse discretization techniques for continuous data [21], but for the current evaluation purposes categorical values are suf<sup>fi</sup>cient. The original goal of the dataset was to <sup>fi</sup>nd a link between these results and two possible diseases of the urinary system. The second dataset, Congressional Voting Records, includes votes for each member of the US House of Representatives on 16 key votes identi<sup>fi</sup>ed by the CQA. The possible vote values are yea (y), nay (n) or unknown disposition (x). The dataset contains 435 records and its original goal was to <sup>fi</sup>nd a connection between the votes and the political party of the voter, Republican or Democrat.

## 4.2. The evaluation method

The evaluation was conducted in steps as follows:

1. Two different clustering algorithms (K-means and two-step) were used to divide the datasets into various numbers of clusters.

2. The threshold for Pijk was set to 90%.

3. Both datasets were randomly divided into train and test subsets in a ratio of 2:1 respectively. The test group was used to show that for any algorithm and number of clusters, the saliency measure of the train and test data are correlated; i.e. once a suitable algorithm is found and the desired number of clusters determined, future results (based on a “new” set of data) will provide similar saliency.

4. A chart depicting the association between the number of clusters and the saliency measure was created for each algorithm in order to choose a speci<sup>fi</sup>c division.

5. After choosing a speci<sup>fi</sup>c division, the resulting characterizing attributes were displayed to examine the simplicity of the proposed technique for interpretation of the clustering results.

![](/api/attachments/4A4YERSX/fulltext/images/41e9734fc13f8d928e8f0e1814fc5c441439ef5b39dc5956fde3b623efa287b5.jpg)  
Fig. 7. Number of clusters and the saliency measure for Dataset 2.

## 4.3. Dataset 1 — acute inflammations

The charts in Fig. 4 show the correlation between the saliency values of train set and test set for 5 to 20 clusters (steps size of 5) produced by the two algorithms (the labels denote the number of clusters).

The correlation between the saliency of the train and test data is obvious and therefore shows that after having selected an algorithm and a desired number of clusters, it is possible to obtain similar saliency values for “new” data, not originally entered into the model. Fig. 5 shows the relationship between the number of clusters and the saliency measure of the clustering results for each algorithm.

It is obvious that both algorithms provide very similar results for this speci<sup>fi</sup>c dataset and therefore it is possible to arbitrarily choose either of them. The number of clusters should be decided based on the user's desired saliency value. If we assume that saliency of 50% is satisfactory, the K-means algorithm with <sup>fi</sup>ve clusters can be selected for further analysis. Table 3 shows the distribution of all attribute values for the results of the chosen clustering algorithm (the notation C stands for cluster).

If we use the probability function, we can easily obtain the probability matrix as shown in Table 4. The cells highlighted represent probabilities that exceed the threshold (90%) and therefore are signi<sup>fi</sup>cant for determining the attributes characterizing each cluster (the notation C stands for cluster).

By exploring the probability matrix, we can identify the distinctive salient features in each cluster as shown in Table 5 (the notation C stands for cluster).

It is clear that each of the clusters has a unique combination of signi<sup>fi</sup>cant attribute values which can be used to describe and characterize its entities. To sum up, by using the proposed model it was possible to create a tool for selecting a suitable algorithm for the task and the desired number of clusters (Fig. 5) and obtain a quick and accurate interpretation of the results that highlights the special characteristics of each cluster (Table 5).

As mentioned above the dataset contains target attributes for possible diseases. Although clustering does not use target attribute, it is interesting to compare the clustering results (based on the saliency measure) to those achieved by classifying methods which use the target attribute, such as decision tree and logistic regression. Table 6 shows the number of errors made by the models when classifying the entities to the target variables (based on a test set of 40 cases out of the 120 cases).

## 4.4. Dataset 2 — congressional voting

The charts in Fig. 6 show the correlation between the saliency values of the train set and test set for 10 to 50 clusters (step size of 10) produced by the two algorithms (the labels denote the number of clusters).

Table 9  
Dataset 2 salient features of each cluster.

<table><tr><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td><td>C8</td><td>C9</td><td>C10</td></tr><tr><td>a1 = n</td><td>a1 = y</td><td>a1 = x</td><td>a2 = n</td><td>a1 = y</td><td>a1 = n</td><td>a1 = x</td><td>a2 = n</td><td>a1 = n</td><td>a1 = x</td></tr><tr><td>a3 = n</td><td>a3 = y</td><td>a2 = x</td><td>a3 = y</td><td>a4 = n</td><td>a2 = y</td><td>a2 = x</td><td>a4 = y</td><td>a3 = y</td><td>a2 = x</td></tr><tr><td>a4 = y</td><td>a4 = n</td><td>a3 = x</td><td>a4 = n</td><td>a5 = y</td><td>a3 = y</td><td>a3 = x</td><td>a5 = y</td><td>a4 = n</td><td>a3 = y</td></tr><tr><td>a5 = y</td><td>a5 = n</td><td>a4 = x</td><td>a5 = n</td><td>a6 = y</td><td>a6 = y</td><td>a4 = x</td><td>a7 = y</td><td>a5 = n</td><td>a4 = n</td></tr><tr><td>a6 = y</td><td>a6 = n</td><td>a5 = x</td><td>a7 = y</td><td>a7 = n</td><td>a11 = y</td><td>a5 = n</td><td>a10 = y</td><td>a7 = y</td><td>a5 = n</td></tr><tr><td>a7 = n</td><td>a7 = y</td><td>a6 = x</td><td>a8 = y</td><td>a8 = n</td><td>a12 = n</td><td>a6 = y</td><td>a11 = n</td><td>a8 = y</td><td>a6 = n</td></tr><tr><td>a8 = n</td><td>a8 = y</td><td>a7 = x</td><td>a9 = y</td><td>a11 = y</td><td>a13 = y</td><td>a7 = n</td><td>a12 = y</td><td>a9 = y</td><td>a7 = y</td></tr><tr><td>a9 = n</td><td>a9 = y</td><td>a8 = x</td><td>a10 = y</td><td>a13 = y</td><td></td><td>a8 = y</td><td>a13 = y</td><td>a10 = y</td><td>a8 = y</td></tr><tr><td>a11 = n</td><td>a10 = n</td><td>a9 = y</td><td>a13 = n</td><td>a14 = y</td><td></td><td>a9 = y</td><td>a14 = y</td><td>a11 = y</td><td>a9 = x</td></tr><tr><td>a12 = y</td><td>a12 = n</td><td>a10 = x</td><td>a14 = y</td><td>a15 = n</td><td></td><td>a10 = n</td><td>a16 = y</td><td>a12 = n</td><td>a10 = n</td></tr><tr><td>a13 = y</td><td>a13 = n</td><td>a11 = x</td><td>a16 = y</td><td></td><td></td><td>a11 = n</td><td></td><td>a13 = n</td><td>a11 = x</td></tr><tr><td>a14 = y</td><td>a14 = n</td><td>a12 = x</td><td></td><td></td><td></td><td>a12 = y</td><td></td><td>a14 = n</td><td>a12 = x</td></tr><tr><td>a15 = n</td><td>a15 = y</td><td>a13 = x</td><td></td><td></td><td></td><td>a13 = y</td><td></td><td>a15 = y</td><td>a13 = x</td></tr><tr><td></td><td></td><td>a14 = x</td><td></td><td></td><td></td><td>a14 = n</td><td></td><td></td><td>a14 = x</td></tr><tr><td></td><td></td><td>a15 = x</td><td></td><td></td><td></td><td>a15 = n</td><td></td><td></td><td>a15 = x</td></tr><tr><td></td><td></td><td>a16 = x</td><td></td><td></td><td></td><td>a16 = x</td><td></td><td></td><td>a16 = x</td></tr></table>

The correlation between the saliency of the train and test data is obvious and therefore shows that after having selected an algorithm and the desired number of clusters, it is possible to obtain similar saliency values for “new” data. Fig. 7 shows the relationship between the number of clusters and the saliency measure of the clustering results for both algorithms.

It is obvious that the K-means algorithm provides better saliency results regardless of the number of clusters. The desired number of clusters should be determined based on the user's desired saliency value. If we assume that saliency of 50% is satisfactory, the K-means algorithm with 10 clusters can be chosen for further analysis. Table 7 (see Appendix A) shows the distribution of all attribute values for the results of the chosen clustering algorithm. Via the probability function, we obtain the corresponding probability matrix, presented in Table 8 (see Appendix B). The cells highlighted represent probabilities that exceed the determined threshold (90%) and therefore are signi<sup>fi</sup>cant for determining the attributes characterizing each cluster. Exploring the probability matrix (Table 8 in Appendix B), shows the distinctive salient features in each cluster as presented in Table 8.

We can see that each of the clusters has a unique combination of signi<sup>fi</sup>cant attribute values which can be used to describe and characterize its entities. To sum up, by using the proposed model it was possible to create a tool for selecting a suitable algorithm for the task and the desired number of clusters (Fig. 7) and make a quick and accurate interpretation of the results which points to the special characteristics of each cluster (Table 9).

As done for Dataset 1, Table 10 shows the number of errors made by three algorithms when classifying the entities to the target attribute (based on test set of 145 cases out of the 435 records).

Using both datasets, we thus showed the effectiveness of the proposed methodology in choosing a suitable clustering algorithm and number of clusters for the dataset. The simplicity of the interpretation makes it possible to see the consistent and meaningful characteristics of the clusters produced. Furthermore, the results obtained by a combination of saliency measure and clustering, without using the target attribute, were as good and precise as the results obtained by classi<sup>fi</sup>cation models that used a target attribute.

Table 10  
Dataset 2 comparison of classi<sup>fi</sup>cation errors.

<table><tr><td>Model</td><td>Party Classification errors</td></tr><tr><td>C5 decision tree</td><td>8</td></tr><tr><td>Logistic regression</td><td>11</td></tr><tr><td>K-means10 (saliency)</td><td>9</td></tr></table>

## 5. Summary, conclusions and further research

The availability of data mining algorithms and tools is attracting considerable attention because they enable the end user to treat data mining tools as black boxes. Users can pay less attention to technical details and devote more time to understanding and interpreting the results. This paper focused on cluster analysis techniques since in many real-life data mining problems, there is no a-priori classi<sup>fi</sup>cation (no target attribute which is known in advance), and it is hard to determine the right number of clusters, or properly interpret the results.

The proposed model, which is an adjustment of the mathematical logistic S-shape function, supports a saliency measure enabling the end user to select a suitable clustering algorithm and determine the right number of clusters. The model was illustrated and evaluated using three well-known datasets taken from the UCI machinelearning web site [18]. The results obtained by the combination of the saliency measure and clustering, without using a target attribute, were as good and precise as the results obtained by classi<sup>fi</sup>cation models that used an a-priori known target attribute.

It was shown that the S-shape function, like the value function in prospect theory [26], satisfactorily represents the end user's decision logic (bounded-rationality rather than absolute optimization) in terms of detecting the attribute features that characterize the clusters. In this way, the proposed method delivers an automatic interpretation of the clustering results, thus pinpointing meaningful hidden insights.

Further research is planned in two directions: A) currently the model is designed to handle categorical attributes. Although it is possible to convert any data item into a categorical representation, future research will focus on adjustment to support ordinal and continuous data. B) Shedding more light on the probability function. The parameters and thresholds used in the current research were determined in a semi-heuristic fashion and required formalization and <sup>fi</sup>ne-tuning. Empirical tests comparing actual users' decisions to the results should be conducted for this task.

These follow-up studies will also make it possible to test the proposed model on larger and more complex datasets so as to demonstrate its validity for general large real-world problems.

Table 7 Dataset 2 clustering results.

<table><tr><td>Attribute name</td><td>Attribute value</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td><td>C8</td><td>C9</td><td>C10</td><td>Rij</td></tr><tr><td rowspan="3">a1</td><td>y</td><td>0.09</td><td>0.85</td><td>0.00</td><td>0.52</td><td>0.76</td><td>0.23</td><td>0.00</td><td>0.32</td><td>0.22</td><td>0.00</td><td>0.43</td></tr><tr><td>n</td><td>0.91</td><td>0.14</td><td>0.00</td><td>0.45</td><td>0.21</td><td>0.77</td><td>0.00</td><td>0.68</td><td>0.75</td><td>0.00</td><td>0.54</td></tr><tr><td>x</td><td>0.00</td><td>0.01</td><td>1.00</td><td>0.03</td><td>0.03</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.03</td><td>1.00</td><td>0.02</td></tr><tr><td rowspan="3">a2</td><td>y</td><td>0.55</td><td>0.40</td><td>0.00</td><td>0.03</td><td>0.66</td><td>0.92</td><td>0.00</td><td>0.18</td><td>0.66</td><td>0.00</td><td>0.46</td></tr><tr><td>n</td><td>0.31</td><td>0.46</td><td>0.00</td><td>0.94</td><td>0.31</td><td>0.08</td><td>0.00</td><td>0.77</td><td>0.25</td><td>0.00</td><td>0.43</td></tr><tr><td>x</td><td>0.14</td><td>0.14</td><td>1.00</td><td>0.03</td><td>0.03</td><td>0.00</td><td>1.00</td><td>0.05</td><td>0.09</td><td>1.00</td><td>0.11</td></tr><tr><td rowspan="3">a3</td><td>y</td><td>0.03</td><td>0.96</td><td>0.00</td><td>0.82</td><td>0.62</td><td>0.85</td><td>0.00</td><td>0.45</td><td>0.97</td><td>1.00</td><td>0.59</td></tr><tr><td>n</td><td>0.95</td><td>0.03</td><td>0.00</td><td>0.18</td><td>0.31</td><td>0.08</td><td>0.00</td><td>0.55</td><td>0.03</td><td>0.00</td><td>0.39</td></tr><tr><td>x</td><td>0.01</td><td>0.01</td><td>1.00</td><td>0.00</td><td>0.07</td><td>0.08</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.02</td></tr><tr><td rowspan="3">a4</td><td>y</td><td>0.98</td><td>0.00</td><td>0.00</td><td>0.06</td><td>0.21</td><td>0.23</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.40</td></tr><tr><td>n</td><td>0.02</td><td>1.00</td><td>0.00</td><td>0.94</td><td>0.79</td><td>0.62</td><td>0.00</td><td>0.00</td><td>1.00</td><td>1.00</td><td>0.58</td></tr><tr><td>x</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.15</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td></tr><tr><td rowspan="3">a5</td><td>y</td><td>0.99</td><td>0.00</td><td>0.00</td><td>0.03</td><td>0.90</td><td>0.54</td><td>0.00</td><td>0.95</td><td>0.03</td><td>0.00</td><td>0.49</td></tr><tr><td>n</td><td>0.00</td><td>0.99</td><td>0.00</td><td>0.94</td><td>0.03</td><td>0.31</td><td>1.00</td><td>0.05</td><td>0.88</td><td>1.00</td><td>0.48</td></tr><tr><td>x</td><td>0.01</td><td>0.01</td><td>1.00</td><td>0.03</td><td>0.07</td><td>0.15</td><td>0.00</td><td>0.00</td><td>0.09</td><td>0.00</td><td>0.04</td></tr><tr><td rowspan="3">a6</td><td>y</td><td>0.95</td><td>0.06</td><td>0.00</td><td>0.70</td><td>0.97</td><td>0.92</td><td>1.00</td><td>0.68</td><td>0.44</td><td>0.00</td><td>0.62</td></tr><tr><td>n</td><td>0.05</td><td>0.90</td><td>0.00</td><td>0.30</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.32</td><td>0.50</td><td>1.00</td><td>0.36</td></tr><tr><td>x</td><td>0.00</td><td>0.04</td><td>1.00</td><td>0.00</td><td>0.03</td><td>0.08</td><td>0.00</td><td>0.00</td><td>0.06</td><td>0.00</td><td>0.03</td></tr><tr><td rowspan="3">a7</td><td>y</td><td>0.03</td><td>0.96</td><td>0.00</td><td>0.88</td><td>0.21</td><td>0.38</td><td>0.00</td><td>0.91</td><td>0.94</td><td>1.00</td><td>0.56</td></tr><tr><td>n</td><td>0.94</td><td>0.04</td><td>0.00</td><td>0.09</td><td>0.69</td><td>0.62</td><td>1.00</td><td>0.05</td><td>0.06</td><td>0.00</td><td>0.41</td></tr><tr><td>x</td><td>0.02</td><td>0.00</td><td>1.00</td><td>0.03</td><td>0.10</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.00</td><td>0.00</td><td>0.03</td></tr><tr><td rowspan="3">a8</td><td>y</td><td>0.01</td><td>0.99</td><td>0.00</td><td>1.00</td><td>0.14</td><td>0.62</td><td>1.00</td><td>0.50</td><td>1.00</td><td>1.00</td><td>0.56</td></tr><tr><td>n</td><td>0.95</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.83</td><td>0.31</td><td>0.00</td><td>0.41</td><td>0.00</td><td>0.00</td><td>0.41</td></tr><tr><td>x</td><td>0.03</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.03</td><td>0.08</td><td>0.00</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.03</td></tr><tr><td rowspan="3">a9</td><td>y</td><td>0.01</td><td>0.90</td><td>1.00</td><td>0.82</td><td>0.21</td><td>0.31</td><td>1.00</td><td>0.50</td><td>0.75</td><td>0.00</td><td>0.48</td></tr><tr><td>n</td><td>0.98</td><td>0.04</td><td>0.00</td><td>0.09</td><td>0.69</td><td>0.69</td><td>0.00</td><td>0.45</td><td>0.13</td><td>0.00</td><td>0.46</td></tr><tr><td>x</td><td>0.01</td><td>0.06</td><td>0.00</td><td>0.09</td><td>0.10</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.13</td><td>1.00</td><td>0.06</td></tr><tr><td rowspan="3">a10</td><td>y</td><td>0.44</td><td>0.21</td><td>0.00</td><td>0.73</td><td>0.41</td><td>0.31</td><td>0.00</td><td>0.73</td><td>0.84</td><td>0.00</td><td>0.47</td></tr><tr><td>n</td><td>0.56</td><td>0.78</td><td>0.00</td><td>0.27</td><td>0.59</td><td>0.69</td><td>1.00</td><td>0.23</td><td>0.16</td><td>1.00</td><td>0.52</td></tr><tr><td>x</td><td>0.00</td><td>0.01</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.00</td><td>0.00</td><td>0.01</td></tr><tr><td rowspan="3">a11</td><td>y</td><td>0.12</td><td>0.25</td><td>0.00</td><td>0.42</td><td>0.83</td><td>0.77</td><td>0.00</td><td>0.00</td><td>0.69</td><td>0.00</td><td>0.34</td></tr><tr><td>n</td><td>0.84</td><td>0.71</td><td>0.00</td><td>0.58</td><td>0.17</td><td>0.15</td><td>1.00</td><td>1.00</td><td>0.22</td><td>0.00</td><td>0.62</td></tr><tr><td>x</td><td>0.05</td><td>0.04</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.08</td><td>0.00</td><td>0.00</td><td>0.09</td><td>1.00</td><td>0.04</td></tr><tr><td rowspan="3">a12</td><td>y</td><td>0.90</td><td>0.01</td><td>0.00</td><td>0.39</td><td>0.31</td><td>0.00</td><td>1.00</td><td>0.77</td><td>0.03</td><td>0.00</td><td>0.41</td></tr><tr><td>n</td><td>0.05</td><td>0.93</td><td>0.00</td><td>0.58</td><td>0.62</td><td>1.00</td><td>0.00</td><td>0.23</td><td>0.78</td><td>0.00</td><td>0.52</td></tr><tr><td>x</td><td>0.06</td><td>0.06</td><td>1.00</td><td>0.03</td><td>0.07</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.19</td><td>1.00</td><td>0.07</td></tr><tr><td rowspan="3">a13</td><td>y</td><td>0.88</td><td>0.04</td><td>0.00</td><td>0.21</td><td>0.72</td><td>0.85</td><td>1.00</td><td>0.77</td><td>0.13</td><td>0.00</td><td>0.48</td></tr><tr><td>n</td><td>0.05</td><td>0.93</td><td>0.00</td><td>0.73</td><td>0.28</td><td>0.00</td><td>0.00</td><td>0.23</td><td>0.75</td><td>0.00</td><td>0.46</td></tr><tr><td>x</td><td>0.07</td><td>0.03</td><td>1.00</td><td>0.06</td><td>0.00</td><td>0.15</td><td>0.00</td><td>0.00</td><td>0.13</td><td>1.00</td><td>0.06</td></tr><tr><td rowspan="3">a14</td><td>y</td><td>0.95</td><td>0.01</td><td>0.00</td><td>0.82</td><td>0.93</td><td>0.31</td><td>0.00</td><td>1.00</td><td>0.13</td><td>0.00</td><td>0.58</td></tr><tr><td>n</td><td>0.01</td><td>0.96</td><td>0.00</td><td>0.15</td><td>0.07</td><td>0.54</td><td>1.00</td><td>0.00</td><td>0.84</td><td>0.00</td><td>0.39</td></tr><tr><td>x</td><td>0.03</td><td>0.03</td><td>1.00</td><td>0.03</td><td>0.00</td><td>0.15</td><td>0.00</td><td>0.00</td><td>0.03</td><td>1.00</td><td>0.04</td></tr><tr><td rowspan="3">a15</td><td>y</td><td>0.05</td><td>0.75</td><td>0.00</td><td>0.42</td><td>0.14</td><td>0.62</td><td>0.00</td><td>0.18</td><td>0.88</td><td>0.00</td><td>0.40</td></tr><tr><td>n</td><td>0.92</td><td>0.18</td><td>0.00</td><td>0.48</td><td>0.83</td><td>0.23</td><td>1.00</td><td>0.73</td><td>0.13</td><td>0.00</td><td>0.54</td></tr><tr><td>x</td><td>0.03</td><td>0.07</td><td>1.00</td><td>0.09</td><td>0.03</td><td>0.15</td><td>0.00</td><td>0.09</td><td>0.00</td><td>1.00</td><td>0.06</td></tr><tr><td rowspan="3">a16</td><td>y</td><td>0.50</td><td>0.58</td><td>0.00</td><td>0.79</td><td>0.45</td><td>0.62</td><td>0.00</td><td>1.00</td><td>0.72</td><td>0.00</td><td>0.61</td></tr><tr><td>n</td><td>0.40</td><td>0.01</td><td>0.00</td><td>0.03</td><td>0.17</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.14</td></tr><tr><td>x</td><td>0.10</td><td>0.40</td><td>1.00</td><td>0.18</td><td>0.38</td><td>0.38</td><td>1.00</td><td>0.00</td><td>0.28</td><td>1.00</td><td>0.25</td></tr><tr><td>No. of entities</td><td></td><td>86</td><td>72</td><td>1</td><td>33</td><td>29</td><td>13</td><td>1</td><td>22</td><td>32</td><td>1</td><td>290</td></tr></table>

## Appendix B

Table 8 Dataset 2 probability matrix.

<table><tr><td>Attribute name</td><td>Attribute value</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td><td>C8</td><td>C9</td><td>C10</td></tr><tr><td rowspan="3">a1</td><td>y</td><td>0.03</td><td>0.98</td><td>0.00</td><td>0.64</td><td>0.95</td><td>0.09</td><td>0.00</td><td>0.20</td><td>0.08</td><td>0.00</td></tr><tr><td>n</td><td>0.98</td><td>0.02</td><td>0.00</td><td>0.33</td><td>0.04</td><td>0.92</td><td>0.00</td><td>0.82</td><td>0.90</td><td>0.00</td></tr><tr><td>x</td><td>0.00</td><td>0.02</td><td>1.00</td><td>0.03</td><td>0.03</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.03</td><td>1.00</td></tr><tr><td rowspan="3">a2</td><td>y</td><td>0.67</td><td>0.33</td><td>0.00</td><td>0.01</td><td>0.86</td><td>0.99</td><td>0.00</td><td>0.05</td><td>0.86</td><td>0.00</td></tr><tr><td>n</td><td>0.19</td><td>0.49</td><td>0.00</td><td>0.99</td><td>0.18</td><td>0.02</td><td>0.00</td><td>0.96</td><td>0.11</td><td>0.00</td></tr><tr><td>x</td><td>0.14</td><td>0.14</td><td>1.00</td><td>0.05</td><td>0.05</td><td>0.00</td><td>1.00</td><td>0.06</td><td>0.09</td><td>1.00</td></tr><tr><td rowspan="3">a3</td><td>y</td><td>0.01</td><td>0.98</td><td>0.00</td><td>0.94</td><td>0.67</td><td>0.95</td><td>0.00</td><td>0.28</td><td>0.98</td><td>1.00</td></tr><tr><td>n</td><td>0.99</td><td>0.02</td><td>0.00</td><td>0.07</td><td>0.22</td><td>0.03</td><td>0.00</td><td>0.75</td><td>0.02</td><td>0.00</td></tr><tr><td>x</td><td>0.02</td><td>0.02</td><td>1.00</td><td>0.00</td><td>0.04</td><td>0.04</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td rowspan="3">a4</td><td>y</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.09</td><td>0.11</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.00</td></tr><tr><td>n</td><td>0.01</td><td>1.00</td><td>0.00</td><td>0.98</td><td>0.92</td><td>0.66</td><td>0.00</td><td>0.00</td><td>1.00</td><td>1.00</td></tr><tr><td>x</td><td>0.00</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.05</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td rowspan="3">a5</td><td>y</td><td>0.99</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.98</td><td>0.61</td><td>0.00</td><td>0.99</td><td>0.01</td><td>0.00</td></tr><tr><td>n</td><td>0.00</td><td>0.99</td><td>0.00</td><td>0.99</td><td>0.01</td><td>0.14</td><td>1.00</td><td>0.01</td><td>0.98</td><td>1.00</td></tr><tr><td>x</td><td>0.03</td><td>0.03</td><td>1.00</td><td>0.04</td><td>0.05</td><td>0.11</td><td>0.00</td><td>0.00</td><td>0.06</td><td>0.00</td></tr><tr><td rowspan="3">a6</td><td>y</td><td>0.98</td><td>0.01</td><td>0.00</td><td>0.78</td><td>0.98</td><td>0.97</td><td>1.00</td><td>0.75</td><td>0.21</td><td>0.00</td></tr><tr><td>n</td><td>0.02</td><td>0.99</td><td>0.00</td><td>0.25</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.28</td><td>0.70</td><td>1.00</td></tr><tr><td>x</td><td>0.00</td><td>0.03</td><td>1.00</td><td>0.00</td><td>0.03</td><td>0.04</td><td>0.00</td><td>0.00</td><td>0.04</td><td>0.00</td></tr><tr><td rowspan="3">a7</td><td>y</td><td>0.01</td><td>0.99</td><td>0.00</td><td>0.97</td><td>0.04</td><td>0.18</td><td>0.00</td><td>0.98</td><td>0.98</td><td>1.00</td></tr><tr><td>n</td><td>0.99</td><td>0.02</td><td>0.00</td><td>0.03</td><td>0.92</td><td>0.84</td><td>1.00</td><td>0.02</td><td>0.02</td><td>0.00</td></tr><tr><td>x</td><td>0.03</td><td>0.00</td><td>1.00</td><td>0.03</td><td>0.06</td><td>0.00</td><td>0.00</td><td>0.03</td><td>0.00</td><td>0.00</td></tr><tr><td rowspan="3">a8</td><td>y</td><td>0.01</td><td>0.99</td><td>0.00</td><td>1.00</td><td>0.02</td><td>0.69</td><td>1.00</td><td>0.41</td><td>1.00</td><td>1.00</td></tr><tr><td>n</td><td>0.99</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.98</td><td>0.20</td><td>0.00</td><td>0.40</td><td>0.00</td><td>0.00</td></tr><tr><td>x</td><td>0.03</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.03</td><td>0.04</td><td>0.00</td><td>0.05</td><td>0.00</td><td>0.00</td></tr><tr><td rowspan="3">a9</td><td>y</td><td>0.01</td><td>0.98</td><td>1.00</td><td>0.96</td><td>0.06</td><td>0.14</td><td>1.00</td><td>0.53</td><td>0.93</td><td>0.00</td></tr><tr><td>n</td><td>0.99</td><td>0.01</td><td>0.00</td><td>0.02</td><td>0.90</td><td>0.90</td><td>0.00</td><td>0.45</td><td>0.03</td><td>0.00</td></tr><tr><td>x</td><td>0.04</td><td>0.06</td><td>0.00</td><td>0.08</td><td>0.09</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.11</td><td>1.00</td></tr><tr><td rowspan="3">a10</td><td>y</td><td>0.40</td><td>0.06</td><td>0.00</td><td>0.92</td><td>0.34</td><td>0.15</td><td>0.00</td><td>0.92</td><td>0.97</td><td>0.00</td></tr><tr><td>n</td><td>0.61</td><td>0.93</td><td>0.00</td><td>0.08</td><td>0.68</td><td>0.86</td><td>1.00</td><td>0.05</td><td>0.03</td><td>1.00</td></tr><tr><td>x</td><td>0.00</td><td>0.01</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.00</td></tr><tr><td rowspan="3">a11</td><td>y</td><td>0.05</td><td>0.17</td><td>0.00</td><td>0.55</td><td>0.99</td><td>0.97</td><td>0.00</td><td>0.00</td><td>0.94</td><td>0.00</td></tr><tr><td>n</td><td>0.94</td><td>0.80</td><td>0.00</td><td>0.52</td><td>0.02</td><td>0.02</td><td>1.00</td><td>1.00</td><td>0.03</td><td>0.00</td></tr><tr><td>x</td><td>0.05</td><td>0.04</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.06</td><td>0.00</td><td>0.00</td><td>0.07</td><td>1.00</td></tr><tr><td rowspan="3">a12</td><td>y</td><td>0.99</td><td>0.01</td><td>0.00</td><td>0.37</td><td>0.20</td><td>0.00</td><td>1.00</td><td>0.96</td><td>0.02</td><td>0.00</td></tr><tr><td>n</td><td>0.01</td><td>0.98</td><td>0.00</td><td>0.65</td><td>0.75</td><td>1.00</td><td>0.00</td><td>0.05</td><td>0.94</td><td>0.00</td></tr><tr><td>x</td><td>0.06</td><td>0.06</td><td>1.00</td><td>0.05</td><td>0.07</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.20</td><td>1.00</td></tr><tr><td rowspan="3">a13</td><td>y</td><td>0.98</td><td>0.01</td><td>0.00</td><td>0.06</td><td>0.91</td><td>0.97</td><td>1.00</td><td>0.94</td><td>0.03</td><td>0.00</td></tr><tr><td>n</td><td>0.01</td><td>0.99</td><td>0.00</td><td>0.93</td><td>0.12</td><td>0.00</td><td>0.00</td><td>0.08</td><td>0.94</td><td>0.00</td></tr><tr><td>x</td><td>0.07</td><td>0.04</td><td>1.00</td><td>0.06</td><td>0.00</td><td>0.14</td><td>0.00</td><td>0.00</td><td>0.11</td><td>1.00</td></tr><tr><td rowspan="3">a14</td><td>y</td><td>0.98</td><td>0.00</td><td>0.00</td><td>0.94</td><td>0.98</td><td>0.09</td><td>0.00</td><td>1.00</td><td>0.01</td><td>0.00</td></tr><tr><td>n</td><td>0.01</td><td>0.99</td><td>0.00</td><td>0.06</td><td>0.03</td><td>0.74</td><td>1.00</td><td>0.00</td><td>0.98</td><td>0.00</td></tr><tr><td>x</td><td>0.04</td><td>0.03</td><td>1.00</td><td>0.04</td><td>0.00</td><td>0.11</td><td>0.00</td><td>0.00</td><td>0.04</td><td>1.00</td></tr><tr><td rowspan="3">a15</td><td>y</td><td>0.02</td><td>0.96</td><td>0.00</td><td>0.46</td><td>0.05</td><td>0.85</td><td>0.00</td><td>0.07</td><td>0.99</td><td>0.00</td></tr><tr><td>n</td><td>0.98</td><td>0.03</td><td>0.00</td><td>0.41</td><td>0.95</td><td>0.05</td><td>1.00</td><td>0.89</td><td>0.02</td><td>0.00</td></tr><tr><td>x</td><td>0.05</td><td>0.07</td><td>1.00</td><td>0.08</td><td>0.05</td><td>0.14</td><td>0.00</td><td>0.08</td><td>0.00</td><td>1.00</td></tr><tr><td rowspan="3">a16</td><td>y</td><td>0.34</td><td>0.54</td><td>0.00</td><td>0.90</td><td>0.24</td><td>0.62</td><td>0.00</td><td>1.00</td><td>0.82</td><td>0.00</td></tr><tr><td>n</td><td>0.68</td><td>0.04</td><td>0.00</td><td>0.05</td><td>0.18</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>x</td><td>0.07</td><td>0.61</td><td>1.00</td><td>0.15</td><td>0.55</td><td>0.56</td><td>1.00</td><td>0.00</td><td>0.31</td><td>1.00</td></tr></table>

## References

[1] T. Adhanom, Classi<sup>fi</sup>cation Trees, Retrieved January 2010, from Weka Docs website: http://wekadocs.com/node/2, (2005).

[2] P. Adriaans, D. Zantinge, Data Mining, Addison-Wesley, MA, 1996.

[3] R. Agarwal, Data mining: crossing the chasm, Proceedings of ACM SIGKDD Conference on Knowledge Discovery and Data Mining, San Diego, Aug 15–18, 1999.

[4] M.J. Aitkenhead, A co-evolving decision tree classi<sup>fi</sup>cation method, Expert Systems with Applications 34 (1) (2008) 18–25.

[5] F.B. Baker, The Basics of Item Response Theory, ERIC Clearinghouse on Assessment and Evaluation, USA, 2001.

[6] A. Barak, R. Gelbard, Classi<sup>fi</sup>cation by clustering decision tree-like classi<sup>fi</sup>er based on adjusted clusters, Expert Systems with Applications 38 (7) (2011) 8220–8228.

[7] R.M. Bittmann, R. Gelbard, Visualization of multi-algorithm clustering for better economic decisions — the case of car pricing, Decision Support Systems 47 (1) (2009) 42–50.

[8] M.J. Brusco, J.D. Cradit, A variable-selection heuristic for K-means clustering, Psychometrika 66 (2001) 249–270.

[9] F.J. Carmone, A. Kara, S. Maxwell, HINoV: a new model to improve market segment de<sup>fi</sup>nition by identifying noisy variables, Journal of Marketing Research 36(1999).501-509

[10] H.M. Chung, P. Gray, Data mining, Journal of Management Information Systems 16 (1) (1999) 11–16.

[11] R.O. Duda, P.E. Hurt, Pattern Classi<sup>fi</sup>cation and Scene Analysis, Wiley & Sons, NY, 1973.

[12] J.G. Dy, C.E. Brodley, Feature selection for unsupervised learning, Journal of Machine Learning Research 5 (2004) 845–889.

[13] J.F. Elder, D. Pregibon, A statistical perspective on knowledge discovery in databases, in: U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy (Eds.), Advances in Knowledge Discovery and Data Mining, MIT Press, 1996, pp. 83–113.

[14] Z. Erlich, R. Gelbard, I. Spiegler, Data mining by means of binary representation: a model for similarity and clustering, Information Systems Frontiers 4 (2) (2002) 187–197.

[15] J. Erman, M. Arlitt, A. Mahanti, Traf<sup>fi</sup>c classi<sup>fi</sup>cation using clustering algorithms, ACM SIGCOMM Workshops, Pisa, Italy, September 11–15, 2006, pp. 281–286.

[16] V. Estivill-Castro, J. Yang, Fast and robust general purpose clustering algorithms, Data Mining and Knowledge Discovery 8 (1) (2004) 127–150.

[17] B. Everitt, Cluster Analysis, 2nd edition New York, USA, Halsted Press, 1980.

[18] A. Frank, A. Asuncion, UCI Machine Learning Repository, Retrieved February 2011, from, http://archive.ics.uci.edu/ml, (2012).

[19] B.J. Frey, D. Dueck, Clustering by passing massages between data points, Science 315 (1) (2007) 972–976.

[20] J.H. Friedman, J.J. Meulman, Clustering objects on subsets of variables, Journal of the Royal Statistical Society 66 (2004) 1–25 (B).

[21] R. Gelbard, Padding bitmaps to support similarity and mining, Information Systems Frontiers (2011), http://dx.doi.org/10.1007/s10796-011-9318-9 (July, 1–12.).

[22] R. Gelbard, O. Goldman, I. Spiegler, Investigating diversity of clustering methods: an empirical comparison, Data & Knowledge Engineering 63 (1) (2007) 155–166

[23] D. Hand, H. Mannila, P. Smyth, Principles of Data Mining, MIT Press, 2001.

[24] A.K. Jain, M.N. Murty, P.J. Flynn, Data clustering: a review, ACM Computing Surveys 31 (3) (1999) 264–323.

[25] A. Jamain, D.J. Hand, Mining supervised classi<sup>fi</sup>cation performance studies: a meta-analytic investigation, Journal of Classification 25 (1) (2008) 87–112

[26] D. Kahneman, A. Tversky, Prospect theory: an analysis of decision under risk, Econometrica 47 (2) (1979) 263–292.

[27] Y. Kim, Weighted order-dependent clustering and visualization of web navigation patterns, Decision Support Systems 43 (4) (2007) 1630–1645.

[28] M.H.C. Law, A.K. Jain, M.A.T. Figueiredo, Feature selection in mixture-based clustering, Advances in Neural Information Processing Systems 15 (2003) 625–632.

[29] M.H.C. Law, M.A.T. Figueiredo, A.K. Jain, Simultaneous feature selection and clustering using mixture models. IEEE Transactions on Pattern Analysis and Machine Intelligence 26 (2004) 1154-1166.

[30] J. MacQueen, Some methods for classi<sup>fi</sup>cation and analysis of multivariate observations, 5th Berkeley Symposium on Mathematical Statistics and Probability, 1 (1), 1967, pp. 281–297.

[31] A. Meged, R. Gelbard, Adjusting fuzzy similarity functions for use with standard data mining tools, Journal of Systems and Software 84 (2011) 2374–2383.

[32] A. Meged, R. Gelbard, A uni<sup>fi</sup>ed fuzzy data model: representation and processing, Journal of Database Management 23 (1) (2012) 78–102.

[33] A. Montanari, L. Lizzani, A projection pursuit approach to variable selection, Computational Statistics & Data Analysis 35 (2001) 463–473.

[34] E. Natividade-Jesus, J. Coutinho-Rodrigues, C.H. Antunes, A multi-criteria decision support system for housing evaluation, Decision Support Systems 43 (3) (2007) 779–790.

[35] E.W.T. Ngai, L. Xiu, D.C.K. Chau, Application of data mining techniques in customer relationship management: a literature review and classi<sup>fi</sup>cation, Expert Systems with Applications 36 (1) (2009) 2592–2602.

[36] A.E. Raftery, N. Dean, Variable selection for model-based clustering, Journal of the American Statistical Association 101 (2006) 168–178.

[37] T.W. Ryu, C.F. Eick, A database clustering methodology and tool, Information Sciences 171 (1) (2005) 29–59.

[38] H. Simon, A behavioral model of rational choice, Quarterly Journal of Economics 69 (1) (1955) 99–118.

[39] D. Steinley, M.J. Brusco, A new variable weighting and selection procedure for K-means cluster analysis, Multivariate Behavioral Research 43 (1) (2008) 77–108.

[40] D. Steinley, M.J. Brusco, Selection of variables in cluster analysis: an empirical comparison of eight procedures, Psychometrika 73 (1) (2008) 125–144.

[41] S. Thomassey, A. Fiordaliso, A hybrid sales forecasting system based on clustering and decision trees, Decision Support Systems 42 (1) (2006) 408–421.

[42] H. Zha, Generic summarization and keyphrase extraction using mutual reinforcement principle and sentence clustering, Proceedings of the 25th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 2002, pp. 113–120.

Barak Aviad is a doctoral student at the Information System program, at the Graduate School of Business Administration, Bar-Ilan University. He holds a B.Sc. degree in Industrial Engineering and M.Sc in Information Systems, both from Tel-Aviv University. In addition, Aviad has over a decade of experience in the IT industry, especially in business intelligence and data mining profession. Currently he serves as a VP Analytics in a tier-one firm

Gelbard Roy is head of the Information System program at the Graduate School of Business Administration, Bar-Ilan University. He received his Ph.D. and M.Sc. degrees in Information Systems from Tel-Aviv University. His work involves two main areas of information systems: (i) knowledge discovery in which he focuses on data and knowledge representation, data mining and recommendation systems and (ii) ICT development in which he focuses on integration of software engineering and project management tool.
