---
otero_id: 26413
otero_key: "NAXPYM7M"
title: "An Evaluation of Self-Organizing Map Networks as a Robust Alternative to Factor Analysis in Data Mining Applications"
authors: "Melody Y. Kiang; Ajith Kumar"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.2.177.9696"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/NAXPYM7M/fulltext/images/fdbffecdd8f4a76c4beb5caf419aacce9ad26053807311f825a0d50f727d51bd.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## An Evaluation of Self-Organizing Map Networks as a Robust Alternative to Factor Analysis in Data Mining Applications

Melody Y. Kiang, Ajith Kumar,

To cite this article:

Melody Y. Kiang, Ajith Kumar, (2001) An Evaluation of Self-Organizing Map Networks as a Robust Alternative to Factor Analysis in Data Mining Applications. Information Systems Research 12(2):177-194. http://dx.doi.org/10.1287/isre.12.2.177.9696

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/NAXPYM7M/fulltext/images/fd686ff1d14ad6648b2fd54e7fd65f33cfa1e798ad4ac7dc0dda2187083912eb.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Evaluation of Self-Organizing Map Networks as a Robust Alternative to Factor Analysis in Data Mining Applications

Melody Y. Kiang • Ajith Kumar

Information Systems Department, College of Business Administration, California State University at Long Beach, Long Beach, California 90840

Department of Marketing, College of Business, Arizona State University, Tempe, Arizona 85287 mkiang@csulb.edu • ajith.kumar@asu.edu

K <sup>ohonen’s</sup> <sup>self-organizing</sup> <sup>map (SOM)</sup> <sup>network</sup> <sup>is</sup> <sup>one</sup> <sup>of</sup> <sup>the</sup> <sup>most</sup> <sup>important</sup> <sup>network</sup> architectures developed during the 1980s. The main function of SOM networks is to map the input data from an n-dimensional space to a lower dimensional (usually one- or twodimensional) plot while maintaining the original topological relations. Therefore, it can be viewed as an analog of factor analysis. In this research, we evaluate the feasibility of using SOM networks as a robust alternative to factor analysis and clustering for data mining applications. Specifically, we compare SOM network solutions to factor analytic and K-Means clustering solutions on simulated data sets with known underlying factor and cluster structures.

The comparisons indicate that the SOM networks provide solutions superior to unrotated factor solutions in general and provide more accurate recovery of underlying cluster structures when the input data are skewed. Our findings suggest that SOM networks can provide robust alternatives to traditional factor analysis and clustering techniques in data mining applications. (Data Mining; Kohonen Networks; Factor Analysis; Data Reductive; Clustering Analysis)

## 1. Introduction

With the increased availability of data collected from the Internet and other sources and the implementation of enterprise-wide databases, the amount of data that companies possess is growing at a phenomenal rate. Hence, it becomes increasingly important for the companies to be able to better manage their databases. Data mining is concerned with identifying interesting patterns and presenting them in a concise and meaningful manner (Piatetsky-Shapiro and Frawley 1991). Data mining tools and techniques that facilitate automated and intelligent database analysis and interpretation have been proposed, and some have been successfully implemented (Fayyad et al. 1996, Westphal & Blaxton 1998, Balachandran et al. 1999).

The widespread availability of data mining software has given practitioners a variety of new alternatives to traditional, statistical data analytic techniques. These alternatives include several techniques based on concepts from machine learning, pattern recognition, and neural networks (Chen et al. 2000, Vanecko and Russo 1999, Spangler et al. 1999, Cooper and Giuffrida 2000). Many of these newer techniques typically serve to achieve the same set of data analytic objectives as those sought to be accomplished by traditional statistical analysis: regression, data reduction, clustering, etc. Often, results obtained using newer data mining techniques are interpreted and utilized in the same manner as those obtained with statistical modeling. For example, the problem of market segmentation involves partitioning a population (of consumers) into relatively homogeneous subsets, so that each subset (segment) can be targeted using a marketing program tailored specifically to the needs of consumers in that subset. In practice, data from a sample of customers (drawn from the relevant population) are analyzed to estimate the segments (number and relative sizes) using a clustering procedure such as K-Means clustering; frequently, the data are preprocessed using factor analysis to reduce dimensionality and facilitate managerial interpretability, and the clustering is done using factor scores (e.g., Dillon et al. 1985, Doyle and Saunders 1985). Now the preprocessing for data reduction and the clustering task can be accomplished using algorithms based on neural networks.

The substitution of neural network–based techniques in the place of statistical modeling techniques needs justification on grounds other than that of novelty. A general a priori justification for preferring neural network–based approaches to statistical ones is that they do not require the invocation of assumptions about the underlying data generating mechanisms (e.g., the distributional assumption of multivariate normality that is invoked to justify the use of several multivariate statistical modeling procedures). On the other hand, statistical techniques provide a wealth of diagnostics that can be used to rigorously evaluate alternative solutions (e.g., error bounds and confidence intervals for parameter estimates, hypothesis testing, etc.). In this paper, we attempt to provide additional justification by presenting preliminary evidence that the SOM network is a robust alternative to factor analysis.

While Kohonen’s self-organizing networks have been successfully applied as a classification tool to various problem domains, including speech recognition (Zhao and Rowden 1992, Leinonen et al. 1993), image data compression (Manikopoulos 1993), image or character recognition (Bimbo et al. 1993, Sabourin and Mitiche 1993), robot control (Walter and Schulen 1993, Ritter et al. 1989), and medical diagnosis (Vercaute\`ren et al. 1990), its potential as a robust substitute for factor analysis and clustering tool remains relatively unresearched. Murtagh and Hernandez-Pajares (1995) examined a number of properties of SOM networks and compared them with various methods of data analysis including principal components and K-Means clustering. Clustering technique is considered an important data mining algorithm that can be applied to various problem domains. However, when the dimensionality of the problem is high—there is very large number of attributes (variables) involved—the size of the search space for model induction grows in a combinatorially explosive manner. Moreover, it increases the chances that a data mining algorithm will find spurious patterns that are not valid. Approaches to this problem include methods to reduce the effective dimensionality of the problem and the use of prior knowledge to identify irrelevant variables (Fayyad et al. 1996). The application of SOM networks as an alternative to factor analysis can reduce the problem space from several to few dimensions.

Factor analytic techniques are typically used to capture information in a set of k variables using a smaller set of new variables (called factors). While several methods are available in the statistical literature for extracting factors, these fall into one of two categories, depending on certain underlying assumptions about the relationships between the (high-dimensional) set of input variables and the (low-dimensional) set of output variables (i.e., the factors). Some methods (e.g., the principal components approach to factor estimation) assume that the statistical information in the input data (i.e., variation) can be adequately captured by a smaller set of variables that are hypothesized to be linear combinations of the input variables. Other methods (e.g., maximum likelihood estimation–based procedures) are based on the assumption that certain statistical relationships found in the input data (e.g., correlations among the variables) occur because the input variables are linear functions of a smaller set of unobserved variables (i.e., common factors). The common theme underlying both sets of methods is one of reducing the dimensionality of the data with minimal loss of information. This provides one basis for suggesting that SOM networks may be used to extract factors. In essence, SOM networks map a set of, say, N p-variate data points (i.e., cases) into a smaller (typically one or two) dimensional array. This mapping is usually interpreted as providing a classification or clustering of the N data points, because the number of elements in the array tends to be much smaller than N. On the other hand, the coordinates of the array elements can be viewed as analogs of factor scores because each k-dimensional input data point is associated with an element in the array characterized by a reduced (i.e., smaller than k) set of coordinates. Van Hulle (2000) provides an empirical basis for considering SOM networks as an alternative to factor analysis. Using a single sample of simulated data, he demonstrates that the SOM algorithm can be used for principal curve extraction. A principal curve is a one-dimensional nonlinear generalization of a principal component (Hastie and Stuetzle 1989). Van Hulle’s (2000) demonstration, however, is limited to showing that the empirical principal curve generated by the SOM algorithm closely approximates the theoretical principal curve.

In this paper we explore three issues using simulated data. First, we address the question of whether SOM-generated coordinate scores are related to the input variables in the same fashion as factor scores are in traditional factor analysis—an important issue because factors need to be interpreted appropriately in business applications if they are to be useful to managers. Second, we examine the consequences of substituting SOM output for factor scores as input into the K-Means clustering procedure. Third, we cluster SOM output using a contiguity-constrained clustering approach suggested by Murtagh (1995) as a preferable way for interpreting the SOM feature map. The balance of the paper is organized as follows: § 2 reviews data mining tasks and techniques. Section 3 presents the basic concepts of the SOM network and illustrates its use as a data-reduction tool (analogous to factor analysis). Section 4 describes the experimental procedure that was used to generate the data sets and determine the network configurations. In § 5 we compare the performance of SOM and factor analysis using the simulated data sets. The paper concludes with a summary of our findings.

## 2. Data Mining Tasks and Techniques

Data mining is the process of automated discovery of interesting patterns, trends, and correlations hidden in a corporate database by sifting through large amount of data. It provides a means of extracting new nonobvious information from the growing base of data warehouses to create competitive advantages for organizations. A survey by both Bose and Sugumaran (1999) has shown that data mining is being used for broad decision making instead of tactical solution with the emphasis on macro decisions.

Data mining tasks can be broadly categorized into four dimensions: classification, estimation, segmentation/ clustering, and description/summarization (Westphal and Blaxton 1998). Depending on the primary goal of the task, the outcome of the data mining process can be predictive models or descriptive information. The predictive models produced by data mining process are good for classification or estimation tasks, while the descriptive information is used for segmentation/ clustering and summarization type of problems. Predictive data mining is a learning process that finds trends, patterns, and subtle relationships in data that allow the prediction of future results. Descriptive data mining process focuses on exploring and visualizing the data to find interesting patterns or relationships (Linoff 1999). Each data mining application has different goals and circumstances and, hence, requires different sets of data mining techniques. The most widely used data mining techniques come from a variety of fields, including query tools; statistical methods such as regression, discriminant analysis, logistic models, multidimensional analysis, factor analysis, and data visualization; also machine learning techniques such as decision trees, expert systems, association rules, neural networks, fuzzy logic, and genetic algorithms. Each technique has advantages and disadvantages (Sung et al. 1999, Chung and Gray 1999, Bose and Sugumaran 1999, Westphal and Blaxton 1998, Yoon 1999, Peacock 1998). The most dominant data mining tool/techniques at present are neural networks (Sung et al. 1999). The application of neural networks techniques to data mining has the advantage of freeing the process from predetermined models and to detect nonlinear relationships automatically. Table 1 summarizes the goals, tasks, and the popular techniques implemented by data mining applications.

Data visualization is a discovery technique that is particularly effective for interpreting large amounts of data because it takes advantage of the human natural

ability to recognize and distinguish between patterns of observable characteristics. Visualization techniques are effective for condensing large amounts of multidimensional data down to a concise and comprehensible form (Sung et al. 1999). Although discovering new knowledge from databases is considered an essential aspect of data mining, how to present the findings in meaningful and user-friendly format via advanced visualization tools is of equal importance. Existing visualization techniques used in data mining range from common statistical-analysis tools such as simple histogram, box plots, and scatter charts, various landscape visual display tools, to more advanced tools such as rotating 3D surface plots (Westphal and Blaxton 1998, Sung et al. 1999). SOM networks are especially good at accepting multidimensional input and transforming it into a map of fewer dimensions, such as a two-dimensional plot. The two-dimensional plot provides an easy-to-use graphical user interface to help the decision maker visualize the relationships among inputs. The map is then used to group inputs into clusters. Clustering is often used as a preprocessor in data mining analysis. Once the groups are identified, they can be used as the starting point for exploring further relationships through link analysis. Data mining tools will continue to grow in power, analytical sophistication, and user friendliness. The introduction of SOM networks as an alternative tool for clustering/ segmentation tasks will enhance the visualization capability and user friendliness of the data mining tools.

Table 1 Summary of Data Mining Goals, Tasks, and Techniques/ Tools

<table><tr><td>Goals</td><td>Tasks</td><td>Techniques/Tools</td></tr><tr><td rowspan="2">Predictive</td><td>Classification</td><td>logit models, discriminant analysis, K-nearest neighbor (Knn), decision trees, neural networks, and genetic algorithm.</td></tr><tr><td>Estimation</td><td>regression, logit models, neural networks, and genetic algorithm</td></tr><tr><td rowspan="2">Descriptive</td><td>Segmentation/Clustering</td><td>K-Means analysis, neural networks, and genetic algorithm.</td></tr><tr><td>Summarization/Link Analysis</td><td>association rules, query tools (SQL), ANOVA, simple cross-tabs, visualization techniques such as pie charts and histograms, and multidimensional analysis (OLAP).</td></tr></table>

## 3. Self-Organizing Map (SOM) Networks

The Self-Organizing Map (SOM) network, a variation of neural computing networks, is a categorization network developed by Kohonen (1984, 1989). The main function of SOM networks is to map the input data from an n-dimensional space to a lower dimensional (usually one- or two-dimensional) plot while maintaining the original topological relations.

The SOM network typically has two layers of nodes, the input layer and the Kohonen layer. The input layer is fully connected to a two-dimensional Kohonen layer (see Figure 1). The Kohonen layer functions similar to biological systems in that it can compress the representation of sparse data and spread out dense data using a two-dimensional map. This is done by assigning different subareas of the Kohonen layer to the different categories of information, so that the location of the processing element in a network becomes specific to a certain characteristic feature in the set of input data. Figure 1 shows how the Kohonen SOM network reduces a problem from an eight-dimensional (eight vectors) to a two-dimensional representation.

During the training process, input data are fed to the network through the processing elements (nodes) in the input layer. An input pattern $x _ { v } \ ( v = 1 , \ldots , V )$ is denoted by a vector of order m as $x _ { v } = ( x _ { v 1 } , x _ { v 2 } , \ldots ,$ $x _ { v m } )$ , where $x _ { v i }$ is the ith input signal in the pattern, and m is the number of input signals in each pattern. An input pattern is simultaneously incident on the nodes of a two-dimensional Kohonen layer. Associated with each of the N nodes in the nxn $( N = n x n )$ Kohonen layer is a weight vector, also of order m, denoted by $w _ { i }$ $\mathbf { \Omega } = { ( w _ { i 1 } , w _ { i 2 } , \dots , w _ { i m } ) }$ , where $w _ { i j }$ is the weight value associated with Node i corresponding to the jth signal of an input vector. As the training process proceeds, the nodes adjust their weight values according to the topological relations in the input data. The node with the minimum distance is the winner and adjusts its weights along with the weights of the nodes in its neighborhood to be closer to the value of the input pattern.

Figure 1 A 33 Kohonen SOM Network with an Input Vector of Orde Eight  
![](/api/attachments/NAXPYM7M/fulltext/images/931aecb7cf0ed928e2c715b768f2b755e85b6f19c62af32e4ae6b059b85a2695.jpg)

## The Self-Organization Process

The network undergoes a self-organization process through a number of training cycles, starting with randomly chosen $w _ { i } s .$ During each training cycle, every input vector is considered in turn and the winner node is determined such that

$$
\| x _ {v} - w _ {i} \| = \min \| x _ {v} - w _ {i} \|, (i = 1, \dots , N),
$$

where . indicates Euclidean distance, which is the most common way of measuring distance between vectors. The weight vectors of the winning nodes, and the nodes in the neighborhood, are updated using the adaptation function

$$
\begin{array}{l} w _ {i} (t + 1) = w _ {i} (t) + h (t r) [ w _ {i} (t) - x _ {y} ], \\ \text { for } i \in N _ {i} (t), 0 <   = r <   = R (t) \\ w _ {i} (t + 1) = w _ {i} (t), \text { otherwise }. \end{array}
$$

Nodes within Radius R are considered for adaptation at Time t, where r is the radial distance of such nodes from the winner node. $N _ { i }$ contains all nodes that are within a certain radius from Node i. Kohonen (1989) suggests that the initial size of the neighborhood should be the size of the network itself to minimize the effect of initial random weights assigned to the nodes. We followed his recommendation and set the initial value of R large enough to cover the whole network.

## Weight Adaptation Function

A Gaussian type of neighborhood adaptation function, which decreases both in the spatial domain and the time domain, has been proposed (Cottrell and Fort 1986, Ritter and Schulten 1986, Lo and Bavarian 1991). Lo and Bavarian (1991) have shown that an algorithm that uses the Gaussian-type function will enforce ordering in the neighborhood set for every training iteration, yielding faster convergence. We use a Gaussian type neighborhood adaptation function h(t, r), similar to the one used by Mitra and Pal (1994):

$$
h (t, r) = \frac {\alpha (1 - r ^ {*} f)}{\left[ 1 + \left(\frac {t}{c d e n o m}\right) ^ {2} \right]}.
$$

This function decreases in both spatial and time domains. In the spatial domain, its value is the largest when Node i is the winner node, and it gradually decreases with increasing distance from i. Parameter a determines the initial value of |h|, while the parameter $f ( 0 < f < 1 / r )$ determines the rate of decrease of |h| in the spatial domain. In the time domain, t controls the value of |h|, whereas the parameter cdenom determines the rate of its decay.

The training is conducted in many stages; at each stage, we reduce R by one. Note that R affects the number of nodes in the set N . To determine the number of training cycles to be run at each stage, we use the index of disorder D proposed by Mitra and Pal (1994). Essentially, D measures the “improvement” in the “state” of the network at discrete time intervals. When this index falls below a certain threshold (D  convergence coefficient d), the next stage of training begins with a reduced R value. The reader may refer to Mitra and Pal (1994) for the detailed algorithm.

## Conscience Mechanism

A further sophistication of the SOM algorithm is achieved by introducing a conscience mechanism. In a self-organized map, a few nodes may end up representing too much of the input data due to the effect of the initial random weight values assigned to them. To avoid this, we use a “conscience” mechanism that prevents the nodes with higher winning frequency from winning repeatedly and makes the nodes with lower winning frequency more likely to win. The purpose of this mechanism is to give each node in the Kohonen layer an opportunity to represent approximately equal information about the input data.

The conscience mechanism that we use is proposed by DeSieno (1988). It adjusts the Euclidean distance between a node’s weight vector and the input vector $\| \boldsymbol { x } _ { v } \mathrm { ~ - ~ } \boldsymbol { w } _ { i } \|$ by a bias $B _ { i } . ~ B _ { i }$ is proportional to the difference between the node’s winning frequency and the average winning frequency

$$
B _ {i} = \gamma \left(\frac {1}{N} - F _ {i}\right).
$$

$F _ { i }$ is the winning frequency of Node i and is updated at every iteration of the training process. Initially, $F _ { i }$ is assigned the average value $1 / N ;$ thus $B _ { i } = 0$ . The winning frequencies are updated as

for the winning node: $F _ { i , t + 1 } = F _ { i , t } + \beta ( 1 . 0 - F _ { i , t } ) ,$

for all other nodes: $F _ { i , t + 1 } = F _ { i , t } + \beta ( 0 . 0 - F _ { i , t } ) ,$

where $\beta$ is a small positive fraction. We followed the suggestion in NeuralWare (1990) and set the value of $\beta$ fixed at 0.1. In this study, we tried the values of $\gamma$ (gamma) coefficient at both zero (when no conscience mechanism was implemented) and four (a number in the range of appropriate values suggested in NeuralWare (1990)).

## The Contiguity-Constrained Clustering (CCC) Method

Sometimes it is hard to visually group the output from SOM especially when the map is highly populated. Hence, a more scientific approach, which can help the user to group the output from SOM network based on certain objective criteria, is needed. To automate the segmentation process to complement the usage of the Kohonen SOM networks, Murtagh (1995) proposed an agglomerative contiguity-constrained clustering method. The method groups the output from SOM based on a minimal distance criterion to merge the neighboring nodes together. The rationale is that the SOM networks will maintain the original topological relations; therefore, the nodes that are closely located on the representational grid should have similar cluster centers. Murtagh also stated that a minimal variance criterion might be used in place of the minimal distance one. To test our cases, we have implemented both approaches. After a few preliminary runs, we found that the minimal variance criterion consistently outperformed the minimal distance approach using our sample cases. Hence, we decided to use the minimal variance criterion for our contiguity-constrained clustering method. The criterion we implemented is modified from Murtagh’s (1985) and tries to minimize the overall within-cluster variance at each step of the process. Each output node of the SOM is represented by the centroid of the input vectors associated with that node. We start with each node in the map representing one group, and calculate the centroid of each group. Then, we try to merge two neighboring groups, so the result of the merge will maintain the global minimal variance for that number of clusters. The merge process is repeated until a user-specified number of clusters is derived or when only one cluster remains. Readers should refer to Appendix A for a detailed step-by-step procedure to implement the algorithm.

## 4. The Experimental Design

Because this study is a preliminary investigation of the performance of SOM versus factor analysis, we decided to first focus attention on artificially constructed data. Knowledge of the true data-generating mechanisms (true factor structure underlying the input variables, the correct cluster membership for each observation) is essential for valid comparisons with respect to the accuracy with which different techniques recover the true factor and cluster structures.

A priori we had no reason to believe that one approach would be uniformly superior to another (i.e., in all circumstances). At the same time, it is beyond the scope of any single study to fully explore all the circumstances that may affect the relative performance of SOM vis-a´-vis factor analysis. Therefore, we selected a few conditions of variation that would be most insightful in identifying situations in which SOM might be preferable to factor analysis and vice-versa. Accordingly, we constructed a set of scenarios characterized by variations in the input data and parameters of the SOM network. These variations were chosen systematically to conform to a multifactorial experimental design format, which we describe below.

## The Statistical Model Underlying the Clustering Problem

Let the population of interest contain C clusters. We assume that each member of the population belongs exclusively to one of the C clusters. Let $\pi _ { c }$ denote the probability that a respondent sampled at random from the population belongs to the cth cluster. Let x denote the $( p \times 1 )$ vector of observations used as input into the factor analysis and p(x; h) its probability distribution in the population, where h denotes a vector containing the parameters of the distribution. Let $p _ { c } ( x ; 6 _ { c } )$ denote the probability distribution of x in the cth cluster (i.e., the conditional distribution of x, given that it comes from the cth cluster). Then, the statistical model for x in the population can be expressed as

$$
p (x; \theta) = \sum_ {c = 1} ^ {C} \pi_ {c} p _ {c} (x; \theta_ {\mathrm{c}})
$$

The observed vector x is assumed to be generated by a set of $q \ ( < p )$ latent factors. This translates to the reparametrization of each $\theta _ { c }$ in terms of the parameters the factor-analytic model (i.e., the model relating the latent factors to x).

## Sample Generation

Random samples of observations from $p ( \boldsymbol { x } ; \boldsymbol { \theta } )$ can be generated in two steps. First, generate an observation from a multinomial distribution with C categories. If the observation belongs to, say, the kth category of the multinomial, then generate an observation for x from $p _ { k } ( x ; \ell _ { \mathrm { k } } )$ . This method of sample generation facilitates assessments of accuracy of cluster membership assignments, because the true cluster membership of each sample observation is known.

Across all scenarios the number of observed variables (p) was fixed at eight, the number of segments (clusters) at three, the number of latent factors $( q )$ at two, and the sample size at 800. In statistical terms, this becomes equivalent to generating samples of 800 observations from a finite mixture of three multivariate distributions. In all scenarios, we specified factorloadings values so that the first four variables $( x _ { 1 } – x _ { 4 } )$ had nonzero loadings only on one factor, and the remaining variables $( x _ { 5 } – x _ { 8 } )$ had nonzero loadings only on the other factor. The factor loadings were chosen to be approximately equal, so that results could be presented by averaging within each subset of four variables. In addition, the two factors were specified to be approximately orthogonal.

## Multivariate Normal Versus Skewed Data

This source of variation in the data is perhaps the most intuitive candidate for inclusion given the state of the knowledge concerning certain fundamental properties of SOM, and given the assumptions underlying the application of factor-analytic techniques and the high levels of skewness commonly found in the “real-world” input data. An appealing feature of SOM is its putative ability to map high-dimensional data into a lower dimensional space, while preserving the topological relations observed in the higher dimensional space. There is no inherent requirement that the input data be multivariate normal, in contrast to commonly used methods of factor analysis.<sup>1</sup> We generated the two types of data as follows. The specific procedure was determined by the PRELIS2 software we used (Joreskog and Sorbom 1989).

The common factor model (with linear factors) for the cth cluster can be represented as

$$
x = \mu_ {c} + \Lambda_ {c} f + e,
$$

where x denotes a $( p \times 1 )$ ) vector of observed variables; $\mu _ { c }$ is a $( p \times 1 )$ vector of constants; f is a $( q \times 1 )$ vector of latent factors; $\Lambda _ { c }$ is a $( p \times q )$ matrix of coefficients relating the latent factors to the observed variables, and e is a $( p \times 1 )$ vector of error terms. It is typically assumed that

$$
E (f) = E (e) = 0,
$$

where E(.) denotes the expectation operator. Then, $\mu _ { c }$ represents the mean vector for the cth cluster. In PRELIS 2 the basic, random variate generators are for the univariate, standard, normal, and uniform probability distributions. We simulated draws from multivariate, normal distributions by first drawing observations from independent, univariate, standard normals corresponding to the elements of f and e and, then, combining these using $\mu _ { c }$ and $\Lambda _ { c }$ to get x. It is possible $^ { \mathrm { t o , } }$ thus, generate variates from multivariate, normal populations with any (permissible) mean and covariance structure, by varying the values of the elements in $\mu _ { c }$ and $\Lambda _ { c } ,$ , respectively.

To generate skewed data, we specified the model relating the observed variables to the underlying latent factors as

$$
x = \mu_ {c} + \Lambda_ {c} f + \Gamma_ {c} g + e,
$$

where $\Gamma _ { c }$ and $g$ have the same dimensions as $\Lambda _ { c }$ and $f ,$ respectively, and each element of g equaled the square of the corresponding element of $f ( { \bf i . e . } , g _ { 1 } = f _ { 1 } ^ { 2 } , g _ { 2 } = f _ { 2 } ^ { 2 }$ $\cdot \cdot \cdot ) .$ . In effect, the elements of x were generated as linear combinations of (symmetric) standard, normal distributions and (skewed) chi-square distributions. The parameters in $\mu _ { c } , \Lambda _ { c } ,$ and $\Gamma _ { c }$ were specified $\mathbf { s o }$ that a two-factor (linear) model would still fit the data in the factor analysis stage (for comparability with the linear scenarios, and because standard statistical software such as SPSS and SAS do not incorporate procedures for nonlinear-factor analysis).

## Cluster Sizes

We included data with both equal and unequal cluster sizes. Some preliminary research we did suggested that SOM networks combined with K-Means analysis tend to perform better when the underlying cluster sizes are approximately equal. On the other hand, unequal clusters tend to arise quite frequently in actual empirical applications.

## Network Size

This refers to the number of nodes in each dimension of the Kohonen layer. We chose three levels of network size $( n \ = \ 1 1 , \ 1 5 , \ 1 7 ) _ { \scriptscriptstyle , }$ , all of which exceed the typical range of “anchor” points in commonly used evaluative rating scales (typically between 5 and 10)—the typical input data for factor analysis. In addition, these sizes encompass the range of our artificially constructed data sets.

## The Gamma Parameter

In this research, we included two levels of the gamma parameter in scenarios with values of zero and four to test the effect of the conscience mechanism on the performance of the network.

We fixed the initial values of all other parameters (e.g.,   0.25, cdenom  1,000) in the network to simplify the network tuning process (Mitra and Pal 1994). Previous research has shown that the performance of SOM networks is less sensitive to changes in the parameter settings relative to other types of neural networks (Kohonen 1995). Based on our experience with

SOM, the network parameters we selected consistently perform satisfactorily (with data samples from various problem domains) on the following criteria: the ability to converge properly and the ability to produce meaningful clusters or maps. Proper convergence is characterized by a monotonically decreasing value of a measurement of the mean-square distance between the input vectors and the weight vectors of the nodes in the set $N _ { i } ,$ so that the network does not keep oscillating between a set of states and never converging to a final state. A too sudden convergence may indicate the possibility of a suboptimal state attained by the network. Meaningful maps are those that do not exhibit problems such as one or two nodes representing too many entities, or a majority of winning nodes bunching into a small portion of the map, prohibiting any meaningful clustering.

In summary, we examined 24 scenarios in detail. These scenarios corresponded to four types of data (normal/nonnormal crossed with equal/unequal cluster sizes), each estimated using six types of SOM networks (three levels of network sizes crossed with two values for the gamma parameter). Details of the characteristics of the populations from which random samples were drawn are given in Appendix B.

As the first step in this study, we implemented the algorithm in C. This language was selected for its object-oriented approach and its generality to other object-oriented algorithms. The code was verified by independently testing specific components and comparing computer-generated results with hand calculations. Each processing unit in the network and each input pattern were implemented using objects. All calculations are performed through message passing between objects in the program. Small networks were used to verify the overall program, again by comparing computer-generated results with hand calculations. The network training for the experiments was performed on a cluster of IBM RS/6000 minicomputers. Version 6.11 of the SAS Statistical package was used to run the factor analysis, K-Means, and other related statistics. For K-Means analysis, we used Proc FASTCLUS (in SAS), with the default procedure for generating starting solutions. The data sets were generated using SAS (to generate multinomial distributions corresponding to the segments) and PRELIS 2 (to generate multivariate observations corresponding to an underlying factor model).

## 5. The Comparative Study

We developed specific quantitative and qualitative criteria for the comparative analysis. Accuracy of respondent assignments to clusters was quantified in two ways. The cluster membership assignments made by the K-Means clustering algorithm were cross-tabulated with the known cluster membership (i.e., the multinomial category for that observation). The rows and columns of this square table were permuted, so as to maximize the sum of the joint frequencies in the diagonal cells of the table. This sum, expressed as a percentage of the total sample size, provides one measure of clustering accuracy. We refer to this as the trace criterion. Another method we used was to compute the Rand measure (Hubert and Arabie 1985) for agreement between two partitions of the same data set. This measure varies between zero and one, with one indicating perfect agreement between the two partitions. The interpretability of the SOM-generated coordinates was assessed qualitatively by correlating each coordinate with the input variables. Because the factor loadings were specified to be approximately equal, we used the average correlations for $x _ { 1 } - x _ { 4 }$ and $x _ { 5 } – x _ { 8 }$ for comparing different solutions. Both the factor analysis of the sample data and the cluster analysis of factor scores were done on standardized data. The neural-net coordinates, in contrast, were not standardized, either for K-Means or contiguity-constrained clustering. We provide a brief sketch of the Rand index and the rationale underlying its development in Appendix C. For a more detailed exposition, the reader is referred to Hubert and Arabie (1985).

## Analysis of the Results

First, we examine the relative interpretability of the factor analysis and SOM solutions with respect to their relationships with the input variables $( \mathrm { i . e . } , x _ { 1 } – x _ { 8 } )$ . Recall that input variables are associated with those factors with which they have substantial correlations. Table 2 reports the correlations between the two subsets of observed variables $( x _ { 1 } - x _ { 4 }$ and $x _ { 5 } – x _ { 8 } )$ with the coordinates of the SOM and factor-analytic outputs. Typically, factor solutions are rotated to enhance interpretability. Accordingly, we report correlations both for the unrotated and VARIMAX-rotated solutions.<sup>2</sup> In our scenarios, each subset should have substantially higher loadings on (or equivalently, correlations with) one of the two coordinates compared to the other. In addition, the two subsets should not have large loadings on the same factor/coordinate. Across the scenarios, interpretability of the SOM output coordinates is substantially better than those for the corresponding unrotated factor solutions but worse than those for the corresponding VARIMAX-rotated solutions. This is in line with expectations because the VARIMAX rotation is performed specifically to enhance solution interpretability, whereas the criterion for deriving the SOM coordinates is topological proximity. While the SOMbased solutions do clearly indicate that input variables $x _ { 1 } { - } x _ { 4 }$ are associated with one factor and $x _ { 5 } – x _ { 8 }$ are associated with the other, it nonetheless seems desirable to develop techniques to rotate or modify SOM output to optimize some criterion of congruence with the input variables to further enhance interpretability. None of the factors varied across the scenarios (normal versus skewed sample data, equal/unequal cluster sizes, network size, or gamma value) appear to have any systematic influence on the interpretability of the SOMbased results. Therefore, in the following we only report the average performance derived from the six network designs (3 network sizes  2 gamma values). Readers should refer to Table 2 for detailed performance results.

We now turn to comparisons of factor scores versus SOM-generated coordinates as input into a K-Means clustering procedure to segment the population. Figures 2 and 3 summarize (average across 3 network sizes $\times ~ 2$ gamma values) the results for comparing solutions from the two types of input based on trace

Table 2 Results for Factor/SOM Analysis (Correlations Between Input Variables and Factor/SOM Coordinates)

<table><tr><td rowspan="2">Data Type</td><td rowspan="2">Cluster Sizes</td><td rowspan="2">Network Size</td><td rowspan="2">Gamma Value</td><td colspan="2">First Coordinate</td><td colspan="2">Second Coordinate</td></tr><tr><td> $X_1-X_4$ </td><td> $X_5-X_8$ </td><td> $X_1-X_4$ </td><td> $X_5-X_8$ </td></tr><tr><td rowspan="16">Normal</td><td rowspan="8">Unequal</td><td colspan="2">Factor Analysis (Unrotated)</td><td>0.76</td><td>-0.66</td><td>0.51</td><td>0.58</td></tr><tr><td colspan="2">Factor Analysis (Rotated)</td><td>0.90</td><td>-0.11</td><td>-0.12</td><td>0.87</td></tr><tr><td>11</td><td>0</td><td>0.83</td><td>-0.44</td><td>0.28</td><td>0.65</td></tr><tr><td>11</td><td>4</td><td>0.82</td><td>-0.44</td><td>0.29</td><td>0.65</td></tr><tr><td>15</td><td>0</td><td>0.82</td><td>-0.44</td><td>-0.28</td><td>-0.66</td></tr><tr><td>15</td><td>4</td><td>-0.87</td><td>0.14</td><td>0.14</td><td>-0.86</td></tr><tr><td>17</td><td>0</td><td>0.83</td><td>-0.44</td><td>0.27</td><td>0.66</td></tr><tr><td>17</td><td>4</td><td>-0.28</td><td>-0.66</td><td>0.82</td><td>-0.44</td></tr><tr><td rowspan="8">Equal</td><td colspan="2">Factor Analysis (Unrotated)</td><td>0.72</td><td>-0.71</td><td>0.55</td><td>0.56</td></tr><tr><td colspan="2">Factor Analysis (Rotated)</td><td>0.90</td><td>-0.12</td><td>-0.12</td><td>0.89</td></tr><tr><td>11</td><td>0</td><td>-0.09</td><td>0.85</td><td>0.87</td><td>-0.18</td></tr><tr><td>11</td><td>4</td><td>-0.88</td><td>0.21</td><td>-0.09</td><td>0.85</td></tr><tr><td>15</td><td>0</td><td>-0.05</td><td>0.83</td><td>-0.87</td><td>0.23</td></tr><tr><td>15</td><td>4</td><td>0.87</td><td>-0.15</td><td>0.15</td><td>-0.86</td></tr><tr><td>17</td><td>0</td><td>-0.06</td><td>0.84</td><td>0.87</td><td>-0.21</td></tr><tr><td>17</td><td>4</td><td>-0.87</td><td>0.17</td><td>-0.11</td><td>0.85</td></tr><tr><td rowspan="16">Skewed</td><td rowspan="8">Unequal</td><td colspan="2">Factor Analysis (Unrotated)</td><td>0.76</td><td>-0.66</td><td>0.51</td><td>0.58</td></tr><tr><td colspan="2">Factor Analysis (Rotated)</td><td>0.90</td><td>-0.11</td><td>-0.12</td><td>0.87</td></tr><tr><td>11</td><td>0</td><td>0.80</td><td>-0.45</td><td>-0.28</td><td>-0.64</td></tr><tr><td>11</td><td>4</td><td>0.81</td><td>-0.43</td><td>-0.25</td><td>-0.66</td></tr><tr><td>15</td><td>0</td><td>0.78</td><td>-0.46</td><td>0.30</td><td>0.63</td></tr><tr><td>15</td><td>4</td><td>0.79</td><td>-0.44</td><td>0.29</td><td>0.63</td></tr><tr><td>17</td><td>0</td><td>0.78</td><td>-0.46</td><td>0.29</td><td>0.63</td></tr><tr><td>17</td><td>4</td><td>0.78</td><td>-0.45</td><td>0.28</td><td>0.64</td></tr><tr><td rowspan="8">Equal</td><td colspan="2">Factor Analysis (Unrotated)</td><td>0.73</td><td>-0.69</td><td>0.53</td><td>0.56</td></tr><tr><td colspan="2">Factor Analysis (Rotated)</td><td>0.90</td><td>-0.12</td><td>-0.12</td><td>0.88</td></tr><tr><td>11</td><td>0</td><td>-0.72</td><td>0.56</td><td>-0.36</td><td>-0.58</td></tr><tr><td>11</td><td>4</td><td>-0.38</td><td>-0.59</td><td>0.72</td><td>-0.58</td></tr><tr><td>15</td><td>0</td><td>0.34</td><td>0.60</td><td>-0.72</td><td>0.55</td></tr><tr><td>15</td><td>4</td><td>0.72</td><td>-0.55</td><td>0.34</td><td>0.60</td></tr><tr><td>17</td><td>0</td><td>0.35</td><td>0.60</td><td>0.72</td><td>-0.57</td></tr><tr><td>17</td><td>4</td><td>0.34</td><td>0.61</td><td>0.72</td><td>-0.55</td></tr></table>

criterion and Rand index, respectively. The cluster analysis was done using the standardized VARIMAXrotated factor scores to conform to common practice. The results reveal some interesting contrasts. When the data are generated from multivariate, normal distributions, the factor analysis-based approach performs better than the SOM-based one in recovering the correct segment membership. However, even in this setting, the two approaches yield comparable results when the underlying segment sizes are approximately equal. When the sample data are skewed, SOM clearly outperforms the factor score–based approach. However, the performance of SOM is better when the underlying cluster sizes are approximately equal. Neither the network size nor the gamma value systematically affects the results. Independent of the performance of SOM, the results show that the factor score–based approach may yield severely biased cluster solutions even while accurately recovering the correct underlying factor structure when the sample data are skewed.

Figure 2 Summary of Results Based on Trace Criterion Trace Criterion  
![](/api/attachments/NAXPYM7M/fulltext/images/0371237ad7ed9456a69d942a317428ffe7b0e55115875fc31ea33d1a52857fcd.jpg)

<table><tr><td></td><td>Normal-Unequal</td><td>Normal-Equal</td><td>Skewed-Unequal</td><td>Skewed-Equal</td></tr><tr><td>□SOM+CCC</td><td>82.15</td><td>83.8</td><td>89.07</td><td>88.07</td></tr><tr><td>■SOM+K-means</td><td>55.24</td><td>83.49</td><td>62.88</td><td>69.82</td></tr><tr><td>□Factor+K-means</td><td>85.76</td><td>86.38</td><td>51.63</td><td>51.89</td></tr></table>

Accuracy of Segment/Cluster Recovery

Figure 3 Summary of Results Based on Rand Index Rand Index  
![](/api/attachments/NAXPYM7M/fulltext/images/5f400d8bd20db16fb0e4e2e8f535340bb330985b745d68ade41e29c8267584e8.jpg)

<table><tr><td></td><td>Normal-Unequal</td><td>Normal-Equal</td><td>Skewed-Unequal</td><td>Skewed-Equal</td></tr><tr><td>□SOM+CCC</td><td>0.791</td><td>0.812</td><td>0.857</td><td>0.85</td></tr><tr><td>■SOM+K-means</td><td>0.675</td><td>0.808</td><td>0.677</td><td>0.715</td></tr><tr><td>□Factor+K-means</td><td>0.828</td><td>0.838</td><td>0.439</td><td>0.582</td></tr></table>

Figures 2 and 3 also include the results obtained when the SOM coordinates were subject to a form of contiguity-constrained cluster (CCC) analysis instead of the traditional K-Means procedure. This approach to clustering substantially improves cluster recovery across all scenarios, except for normal data with equal cluster sizes where the results are comparable to those obtained using the K-Means procedure. As with the other results, neither network size nor variations in the gamma parameter value had any systematic impact on the results.

Table 3 presents the results for cluster size recovery using both K-Means and contiguity-constrained clustering to group the neural net output coordinates. When the data are normal and the K-Means algorithm is used to cluster the NN coordinates, the traditional factor analytic approach provides better estimates of cluster sizes. However, the traditional approach breaks down completely when the data are skewed. Across all scenarios, the performance of NN output improves dramatically when contiguity-constrained clustering is substituted for K-Means. Overall, when SOM is used in conjunction with contiguity-constrained clustering, its performance is either comparable to or far exceeds the factor analysis-based approach.

## A Small-Scale Follow-Up Study

As a follow-up to our experimental design, we conducted a second study on four new samples of size 800. The four samples were (1) four clusters with equal group sizes, (2) four clusters with unequal group sizes, (3) five clusters with equal group sizes, and (4) five clusters with unequal group sizes. Each sample contained 12 variables with a three-factor model as the data-generating mechanism. In all four samples the data were generated with moderate levels of skewness, compared to the skewed data generated in the first experimental design. Given the results of the first study, the network size and gamma parameter value were kept constant.

With respect to the relationship between the three neural net coordinates and the 12 variables in the sample data, we found relationships similar to those in the first experimental design: The pattern of correlations between the output coordinates and the input variables were more similar to the corresponding unrotated factor solution compared to the Varimax-rotated solution. Figures 4 and 5 and Appendix D present the results for cluster recovery for all three techniques: clustering with the neural net coordinates using K-Means clustering and contiguity-constrained clustering, and clustering with factor scores using K-Means clustering. As in the first study, contiguity-constrained clustering of neural-net coordinates recovers the true cluster structure most accurately. On the other hand, the traditional approach of clustering factor scores gives better results compared to clustering the neuralnet coordinates using the K-Means procedure. The latter result is consistent with the results of the first study, given that the data in the four samples were less skewed compared to the skewed data in the first study (i.e., the performance of the traditional approach improves as the data become less skewed).

Table 3 Results for Cluster Sizes (Recovery of Cluster Proportions)

<table><tr><td>Data Type</td><td>Cluster Sizes</td><td>Network Size</td><td>Gamma Value</td><td>K-Means Clustering</td><td>Contiguity Clustering</td></tr><tr><td rowspan="14">Normal</td><td rowspan="7">Unequala</td><td colspan="2">Factor Analysis</td><td>0.49, 0.26, 0.24,</td><td></td></tr><tr><td>11</td><td>0</td><td>0.41, 0.30, 0.28,</td><td>0.43, 0.40, 0.18</td></tr><tr><td>11</td><td>4</td><td>0.40, 0.31, 0.28,</td><td>0.43, 0.40, 0.18</td></tr><tr><td>15</td><td>0</td><td>0.38, 0.35, 0.27</td><td>0.50, 0.27, 0.22</td></tr><tr><td>15</td><td>4</td><td>0.37, 0.36, 0.27</td><td>0.43, 0.34, 0.24</td></tr><tr><td>17</td><td>0</td><td>0.36, 0.36, 0.28</td><td>0.55, 0.26, 0.19</td></tr><tr><td>17</td><td>4</td><td>0.38, 0.35, 0.27</td><td>0.43, 0.41, 0.16</td></tr><tr><td rowspan="7">Equalb</td><td colspan="2">Factor Analysis</td><td>0.39, 0.35, 0.26</td><td></td></tr><tr><td>11</td><td>0</td><td>0.36, 0.34, 0.30</td><td>0.41, 0.37, 0.22</td></tr><tr><td>11</td><td>4</td><td>0.38, 0.33, 0.29</td><td>0.36, 0.34, 0.32</td></tr><tr><td>15</td><td>0</td><td>0.38, 0.36, 0.26</td><td>0.42, 0.31, 0.27</td></tr><tr><td>15</td><td>4</td><td>0.37, 0.36, 0.28</td><td>0.45, 0.35, 0.20</td></tr><tr><td>17</td><td>0</td><td>0.37, 0.34, 0.29</td><td>0.40, 0.34, 0.26</td></tr><tr><td>17</td><td>4</td><td>0.39, 0.33, 0.28</td><td>0.42, 0.37, 0.21</td></tr><tr><td rowspan="14">Skewed</td><td rowspan="7">Unequal</td><td colspan="2">Factor Analysis</td><td>0.90, 0.05, 0.05</td><td></td></tr><tr><td>11</td><td>0</td><td>0.35, 0.34, 0.30</td><td>0.46, 0.38, 0.16</td></tr><tr><td>11</td><td>4</td><td>0.36, 0.35, 0.30</td><td>0.46, 0.38, 0.16</td></tr><tr><td>15</td><td>0</td><td>0.36, 0.34, 0.29</td><td>0.46, 0.36, 0.18</td></tr><tr><td>15</td><td>4</td><td>0.36, 0.34, 0.30</td><td>0.43, 0.40, 0.17</td></tr><tr><td>17</td><td>0</td><td>0.38, 0.33, 0.30</td><td>0.48, 0.37, 0.16</td></tr><tr><td>17</td><td>4</td><td>0.37, 0.33, 0.30</td><td>0.42, 0.40, 0.17</td></tr><tr><td rowspan="7">Equal</td><td colspan="2">Factor Analysis</td><td>0.67, 0.30, 0.03</td><td></td></tr><tr><td>11</td><td>0</td><td>0.42, 0.31, 0.26</td><td>0.43, 0.29, 0.28</td></tr><tr><td>11</td><td>4</td><td>0.37, 0.36, 0.26</td><td>0.42, 0.31, 0.27</td></tr><tr><td>15</td><td>0</td><td>0.39, 0.33, 0.28</td><td>0.42, 0.33, 0.25</td></tr><tr><td>15</td><td>4</td><td>0.40, 0.32, 0.28</td><td>0.41, 0.32, 0.27</td></tr><tr><td>17</td><td>0</td><td>0.36, 0.36, 0.29</td><td>0.46, 0.30, 0.24</td></tr><tr><td>17</td><td>4</td><td>0.36, 0.34, 0.30</td><td>0.52, 0.24, 0.24</td></tr></table>

<sup>a</sup>The actual sample distribution is 0.50, 0.31, 0.19 for both normal and skewed data.  
<sup>b</sup>The actual sample distribution is 0.35, 0.33, 0.32 for both normal and skewed data.

## 6. Discussion

Despite the obvious limitations of the scope of our investigations, the results strongly support the case for considering SOM as an alternative to factor analysis for data reduction. Independent of any comparisons with SOM, the factor score–based approach to clustering can severely bias cluster solutions when the sample data are skewed (as is frequently observed in “realworld” data). In particular, this bias can occur even when the true underlying factor structure is adequately recovered in the factor-analysis stage.

Figure 4 Summary of Results Based on Trace Criterion for the Follow-Up Study  
![](/api/attachments/NAXPYM7M/fulltext/images/aefc588126d58151e6a1427d86fe33b18dc77c13690cfdce7998a8eccacfad7d.jpg)

<table><tr><td></td><td>4-Unequal</td><td>4-Equal</td><td>5-Unequal</td><td>5-Equal</td></tr><tr><td>□SOM+CCC</td><td>94.14</td><td>94.52</td><td>95.01</td><td>93.27</td></tr><tr><td>■SOM+K-means</td><td>80.51</td><td>69.39</td><td>62.13</td><td>51.76</td></tr><tr><td>□Factor+K-means</td><td>78.76</td><td>73.64</td><td>82.5</td><td>78.76</td></tr></table>

Accuracy of Segment/Cluster Recovery

Figure 5 Summary of Results Based on Rand Index for the Follow-Up Study  
![](/api/attachments/NAXPYM7M/fulltext/images/1160f3f9a039805e497dfdeeafcd5f2c48af7c2d9906094b65d0a367435d3c32.jpg)

<table><tr><td></td><td>4-Unequal</td><td>4-Equal</td><td>5-Unequal</td><td>5-Equal</td></tr><tr><td>□ SOM+CCC</td><td>0.947</td><td>0.949</td><td>0.947</td><td>0.962</td></tr><tr><td>■ SOM+K-means</td><td>0.846</td><td>0.772</td><td>0.789</td><td>0.775</td></tr><tr><td>□ Factor+K-means</td><td>0.85</td><td>0.837</td><td>0.902</td><td>0.88</td></tr></table>

Accuracy of Segment/Cluster Recovery

While SOM output generally performs better than factor scores when the data are skewed, using alternatives to traditional K-Means clustering can further enhance the performance of SOM. In this research, we modified Murtagh’s approach and developed a contiguity-constraint clustering procedure that groups the nodes by minimizing the overall variance within clusters.

A major criticism with the applications of neural networks to real-world problems is the need to tune the network for each data set to achieve better performance. The tuning process usually involves a series of trial-and-error steps to arrive at an appropriate set of network parameters. The process is, thus, greatly reliant on the modeler’s previous experience in both the problem domain and with neural networks. Moreover, a network that is well tuned for a specific sample may not do well when a new case is presented. This may be due to changes in the underlying data characteristics. Discussion of the possible causes for network performance deterioration is beyond the scope of this paper.

Another issue that would need to be considered in practical applications is determining the correct number of dimensions for the reduced-space representation of input data, which is analogous to determining the correct number of factors in factor analysis. In this study, we first used a two-dimensional map, the most common Kohonen network, to capture the two-factor problems we generated. An advantage of the twodimensional network is that it allows the users to visualize the data distribution on a plot. However, in real-world settings, often we do not have a priori knowledge regarding the number of factors that exist in the sample data and would not be able to determine the type of network (i.e., number of dimensions) to use. One approach to this problem is to use factor analysis as a preprocessor to determine the number of factors that exist in the data, then use the information to select the appropriate network dimension. We have also tested the SOM network using three-factor problems in the follow-up study, and the results were consistent with that of the two-factor problems.

In this study, we have fixed most of the network parameters and only allow the network size and gamma value to change. There is no trial-and-error process performed and the same network configuration has been applied throughout the experiments. We have presented all the experiment results we derived. The data generation and the network training were conducted independently by each coauthor, and the person who trained the SOM network has no knowledge about the distribution or the composition of the sample. The only information given at the time of training was the number of clusters needed. The different network sizes and gamma values had neither significant nor systematic effects on the performance of the network; suggesting that the performance of the SOM network is less prone to the change in network settings and, hence, is a more robust tool than other types of neural networks. In our future research, we hope to develop modifications of SOM networks whose output would more closely approximate rotated (rather than unrotated) factor solutions.

Table A1 Correlations, Means, and Standard Deviations for Six Population

<table><tr><td>Cluster</td><td> $x_1$ </td><td> $x_2$ </td><td> $x_3$ </td><td> $x_4$ </td><td> $x_5$ </td><td> $x_6$ </td><td> $x_7$ </td><td> $x_8$ </td><td>SD</td><td>M</td></tr><tr><td colspan="11">1</td></tr><tr><td> $x_1$ </td><td>1.000</td><td>0.510</td><td>0.563</td><td>0.559</td><td>0.003</td><td>0.003</td><td>0.006</td><td>0.001</td><td>1.497</td><td>5.608</td></tr><tr><td> $x_2$ </td><td>0.501</td><td>1.000</td><td>0.521</td><td>0.516</td><td>0.001</td><td>0.004</td><td>0.002</td><td>0.000</td><td>1.371</td><td>5.511</td></tr><tr><td> $x_3$ </td><td>0.481</td><td>0.452</td><td>1.000</td><td>0.562</td><td>0.003</td><td>0.000</td><td>0.003</td><td>0.000</td><td>1.547</td><td>5.613</td></tr><tr><td> $x_4$ </td><td>0.495</td><td>0.461</td><td>0.445</td><td>1.000</td><td>-0.001</td><td>0.000</td><td>-0.002</td><td>-0.002</td><td>1.607</td><td>5.811</td></tr><tr><td> $x_5$ </td><td>0.003</td><td>0.006</td><td>0.008</td><td>0.005</td><td>1.000</td><td>0.556</td><td>0.506</td><td>0.555</td><td>1.588</td><td>2.799</td></tr><tr><td> $x_6$ </td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.001</td><td>0.445</td><td>1.000</td><td>0.512</td><td>0.561</td><td>1.536</td><td>2.592</td></tr><tr><td> $x_7$ </td><td>0.003</td><td>0.002</td><td>0.001</td><td>0.004</td><td>0.459</td><td>0.474</td><td>1.000</td><td>0.502</td><td>1.359</td><td>2.498</td></tr><tr><td> $x_8$ </td><td>0.000</td><td>0.000</td><td>0.004</td><td>0.002</td><td>0.478</td><td>0.490</td><td>0.560</td><td>1.000</td><td>1.489</td><td>2.601</td></tr><tr><td>SD</td><td>1.471</td><td>1.374</td><td>1.324</td><td>1.360</td><td>1.334</td><td>1.361</td><td>1.401</td><td>1.454</td><td></td><td></td></tr><tr><td>M</td><td>4.992</td><td>4.991</td><td>4.996</td><td>4.993</td><td>1.993</td><td>1.996</td><td>1.994</td><td>1.998</td><td></td><td></td></tr><tr><td colspan="11">2</td></tr><tr><td> $x_1$ </td><td>1.000</td><td>0.504</td><td>0.558</td><td>0.554</td><td>-0.001</td><td>-0.001</td><td>0.001</td><td>-0.002</td><td>1.489</td><td>2.602</td></tr><tr><td> $x_2$ </td><td>0.508</td><td>1.000</td><td>0.516</td><td>0.507</td><td>-0.004</td><td>-0.002</td><td>-0.001</td><td>-0.005</td><td>1.362</td><td>2.502</td></tr><tr><td> $x_3$ </td><td>0.486</td><td>0.456</td><td>1.000</td><td>0.557</td><td>-0.003</td><td>0.000</td><td>-0.001</td><td>-0.005</td><td>1.533</td><td>2.602</td></tr><tr><td> $x_4$ </td><td>0.495</td><td>0.465</td><td>0.445</td><td>1.000</td><td>-0.006</td><td>-0.004</td><td>-0.001</td><td>-0.006</td><td>1.588</td><td>2.797</td></tr><tr><td> $x_5$ </td><td>0.004</td><td>0.004</td><td>0.002</td><td>0.004</td><td>1.000</td><td>0.556</td><td>0.512</td><td>0.554</td><td>1.585</td><td>5.801</td></tr><tr><td> $x_6$ </td><td>-0.003</td><td>-0.001</td><td>-0.001</td><td>0.000</td><td>0.446</td><td>1.000</td><td>0.516</td><td>0.556</td><td>1.537</td><td>5.601</td></tr><tr><td> $x_7$ </td><td>0.006</td><td>0.004</td><td>0.002</td><td>0.002</td><td>0.460</td><td>0.472</td><td>1.000</td><td>0.501</td><td>1.360</td><td>5.499</td></tr><tr><td> $x_8$ </td><td>0.003</td><td>0.005</td><td>0.002</td><td>0.004</td><td>0.476</td><td>0.489</td><td>0.505</td><td>1.000</td><td>1.483</td><td>5.603</td></tr><tr><td>SD</td><td>1.470</td><td>1.382</td><td>1.334</td><td>1.358</td><td>1.330</td><td>1.356</td><td>1.402</td><td>1.452</td><td></td><td></td></tr><tr><td>M</td><td>1.998</td><td>1.999</td><td>2.004</td><td>2.001</td><td>5.001</td><td>5.004</td><td>5.009</td><td>4.999</td><td></td><td></td></tr><tr><td colspan="11">3</td></tr><tr><td> $x_1$ </td><td>1.000</td><td>0.505</td><td>0.561</td><td>0.553</td><td>0.005</td><td>0.000</td><td>-0.003</td><td>0.007</td><td>1.493</td><td>5.595</td></tr><tr><td> $x_2$ </td><td>0.501</td><td>1.000</td><td>0.521</td><td>0.507</td><td>0.000</td><td>-0.002</td><td>-0.003</td><td>0.004</td><td>1.368</td><td>5.500</td></tr><tr><td> $x_3$ </td><td>0.484</td><td>0.454</td><td>1.000</td><td>0.557</td><td>-0.002</td><td>-0.003</td><td>-0.005</td><td>0.000</td><td>1.539</td><td>5.592</td></tr><tr><td> $x_4$ </td><td>0.497</td><td>0.466</td><td>0.448</td><td>1.000</td><td>0.000</td><td>-0.001</td><td>-0.002</td><td>0.003</td><td>1.593</td><td>5.793</td></tr><tr><td> $x_5$ </td><td>0.003</td><td>0.001</td><td>0.004</td><td>0.005</td><td>1.000</td><td>0.559</td><td>0.510</td><td>0.0560</td><td>1.594</td><td>5.799</td></tr><tr><td> $x_6$ </td><td>-0.003</td><td>0.001</td><td>0.005</td><td>0.008</td><td>0.447</td><td>1.000</td><td>0.513</td><td>0.565</td><td>1.539</td><td>5.601</td></tr><tr><td> $x_7$ </td><td>-0.003</td><td>-0.002</td><td>-0.001</td><td>0.002</td><td>0.465</td><td>0.474</td><td>1.000</td><td>0.505</td><td>1.365</td><td>5.501</td></tr><tr><td> $x_8$ </td><td>0.003</td><td>0.002</td><td>0.001</td><td>0.004</td><td>0.477</td><td>0.490</td><td>0.507</td><td>1.000</td><td>1.497</td><td>5.608</td></tr><tr><td>SD</td><td>1.470</td><td>1.375</td><td>1.334</td><td>1.358</td><td>1.328</td><td>1.358</td><td>1.403</td><td>1.449</td><td></td><td></td></tr><tr><td>M</td><td>5.005</td><td>5.003</td><td>5.008</td><td>5.005</td><td>5.003</td><td>5.001</td><td>5.000</td><td>5.003</td><td></td><td></td></tr></table>

## Acknowledgment

This research was supported in part by a grant from the Information Technology and Organizations Program of the National Science Foundation (NSF), IRI-9505715, to M. Kiang. The opinions are of the authors.

## Appendix A

The detailed process for implementing the contiguity-constrained clustering method is described in the following:

Step 1. For each node , calculate the centroid (C ) of node as

$$
C _ {i} = \frac {1}{| n o d e _ {i} |} \sum_ {x \in n o d e _ {i}} \bar {x},
$$

where |node<sub>i</sub>| is the number of input vectors associated with the node.

Step 2. Assign a group number $( G _ { k } )$ to each node<sub>i</sub> if |node<sub>i</sub>| - 0, and update the corresponding centroid value.

Step 3. Calculate the overall variance of the map:

(a) Sum the square distance between input Vector x and the group centroid $C _ { k }$ for all x in $G _ { k } .$ Calculate for every group k.

$$
V _ {k} = \sum \| x - C _ {k} \|, x \in G _ {k}.
$$

(b) Total the variances from all groups. This will give us the global variance of the map:

$$
V _ {T o t a l} = \sum V _ {k}.
$$

Step 4. For each pair of neighboring groups, calculate the total variance of the map if the two groups were merged. Merge the two groups that result in the minimum global variance.

(a) Calculate the new centroid for $G _ { p q } \mathrm { i f } G _ { p }$ and $G _ { q }$ were merged:

$$
C _ {p q} = (| G _ {p} | ^ {*} \bar {G} _ {p} + | G _ {q} | ^ {*} \bar {G} _ {q}) / | G _ {p} | + | G _ {q} |.
$$

(b) Calculate the new variance if $G _ { p }$ and $G _ { q }$ were merged (modified from Murtagh 1985):

$$
V _ {p q} = \sum \| x - C _ {n e w} \|, \text {   for   all   } x, x \in G _ {p} \text {   or   } x \in G _ {q}.
$$

(c) Calculate the new global variance for merging $G _ { p }$ and $G _ { q } \mathrm { : }$

$$
V _ {p q T o t a l} = V _ {T o t a l} + V _ {p q} - V _ {p} - V _ {q}.
$$

(d) Calculate the $V _ { p q T o t a l }$ for every pair of $p$ and q on the map. For each iteration, groups p and q must be within a fixed radius distance on the grid. We start with radius distance  1, hence, for each node there are eight neighboring nodes within that distance. We increase the radius distance by one each time if there is no neighboring group within current radius distance for all groups k. Finally, we merge the two groups that result in global minimal variance.

(e) Update $V _ { T o t a l }$ and the group number and group centroid of the two newly merged groups.

Step 5. Repeat Step 4 until only one cluster or the prespecified number of clusters has been reached.

## Appendix B

## Data Characteristics

As discussed in the paper, samples were generated in two stages. First, an observation was drawn from a multinomial population with three categories, corresponding to three clusters. For the context with unequal cluster sizes, the (population) multinomial proportions were specified to be 0.2, 0.5, and 0.3. For (approximately) equal cluster sizes, the corresponding proportions were specified to be 0.33, 0.33, and 0.34. In the actual samples drawn, the cluster proportions were 0.19, 0.50, and 0.31 in the unequal cluster size scenario, and 0.32, 0.33, and 0.35 in the equal cluster size scenario.

In the second stage, depending on the specific outcome obtained in the draw from the multinomial population, a multivariate observation was drawn from the population with a specific mean and covariance structure corresponding to that category. This observation was drawn either from a multivariate normal distribution or from a skewed distribution. Thus, in this stage, observations were drawn from one of six populations (three clusters crossed with normal/skewed distributions). We give the means, correlations, and standard deviations for all six populations, generated assuming a sample size of 100,000 for each in Table A1. Samples of this size yield statistics that are virtually indistinguishable from the corresponding population parameters. The data are presented for each segment separately. Values above the diagonal are for skewed populations, while those below are for multivariate normal populations. It can be verified easily that in all scenarios, a two-factor solution will adequately account for the correlations in the data. In addition, variables $x _ { 1 }$ through $x _ { 4 }$ would load on one factor (with approximately equal loadings), while $x _ { 5 }$ through $x _ { 8 }$ would load similarly on the second factor. Note that the (smaller) samples generated for the study will not have exactly the same mean and covariance structures shown below due to sampling fluctuations.

## Appendix C. Note on the Rand Index

We use the Rand Index to assess quantitatively the accuracy with which the K-Means and SOM network–based clustering procedures recover known cluster structures. Formally, this means that the set of data being analyzed is partitioned in two different ways—the first partition is associated with the data-generating mechanism used for drawing samples (i.e., each data point is drawn from one of C different clusters), while the second partition is associated with the clusters to which the data points are assigned by a clustering procedure (i.e., the assignment of each data point to one of C clusters).

The two partitions of the data can be used to assign each data point to a specific cell in a two-way contingency table formed by the cross-classification of the membership categories denoting the clusters from which the data are drawn and those categories denoting the clusters to which the data are assigned by a clustering procedure.

![](/api/attachments/NAXPYM7M/fulltext/images/41f84e945feceb1402a734c13430d06779a780266587d5d0aacc8586e631ff3c.jpg)

We now consider all possible pairs of data points in a specific sample of size, say, N. The total number of distinct pairs is denoted by $\phantom { } _ { N } C _ { 2 } .$ That is,

$$
{ } _ { N } C _ { 2 } = \frac { N * ( N - 1 ) } { 2 } \text {   if   } N \geq 2 .
$$

Otherwise, it is defined to be zero.

With respect to the two partitions of the data (i.e., generation and assignment), each pair can be assigned to (exactly) one of the following four classes:

(1) Both members of the pair are drawn from the same cluster and assigned to the same cluster;

(2) Members of the pair are drawn from the same cluster, but assigned to different clusters;

(3) Members of the pair are drawn from different clusters, but assigned to the same cluster; and

(4) Members of the pair are drawn from different clusters, and assigned to different clusters

Pairs belonging to these four classes can be conceptually treated as data points that can be assigned to the following $( 2 \times 2 )$ contingency table.

<table><tr><td></td><td>Assigned to same class</td><td>Assigned to different classes</td></tr><tr><td>Drawn from same class</td><td>A</td><td>B</td></tr><tr><td>Drawn from different classes</td><td>C</td><td>D</td></tr></table>

A, B, C, and D denote the number of pairs in classes (1), (2), (3), and (4), respectively. The sum $\mathrm { ~ A ~ } + \mathrm { ~ D ~ }$ can be considered a measure of the extent to which the two partitions of the data are “in agreement.”

The Rand Index is derived to provide a normalized measure of agreement between the two partitions (i.e., the index has an upper bound of 1) that is also corrected for agreements that may arise due to chance. It is derived as follows.

Let $n _ { i j }$ denote the number of data points drawn from the ith cluster and assigned to the jth cluster $( \mathrm { i . e . } ,$ the frequency for the cell corresponding to the ith row and the jth row of the first $( C \times C )$ twoway table shown above. Further, let $n _ { i }$ and $n _ { j }$ denote the marginal frequencies for ith row and jth column, respectively (i.e., ith row total and jth column total). That is,

$$
n _ {i.} = \sum_ {j} n _ {i j}
$$

and

$$
n _ {. j} = \sum_ {i} n _ {i j},
$$

where the two summations are done over the columns and rows of the $( C \times C )$ table, respectively. Then

Appendix D. Results for Both K-Means Cluster Analysis and Contiguity-Constrained Cluster (CCC) Analysis of Neural Net Output (Accuracy of Cluster Recovery)

<table><tr><td rowspan="2">Data Type</td><td rowspan="2">Cluster Sizes</td><td rowspan="2">Network Size</td><td rowspan="2">Gamma Value</td><td colspan="2">K-Means</td><td colspan="2">Contiguity-Constrained</td></tr><tr><td>Trace Criterion</td><td>Rand Index</td><td>Trace Criterion</td><td>Rand Index</td></tr><tr><td rowspan="14">Normal</td><td rowspan="7">Unequal</td><td>Factor Analysis</td><td></td><td>85.76</td><td>0.828</td><td></td><td></td></tr><tr><td>11</td><td>0</td><td>51.51</td><td>0.685</td><td>82.88</td><td>0.791</td></tr><tr><td>11</td><td>4</td><td>49.75</td><td>0.683</td><td>82.88</td><td>0.791</td></tr><tr><td>15</td><td>0</td><td>56.38</td><td>0.669</td><td>84.25</td><td>0.829</td></tr><tr><td>15</td><td>4</td><td>58.13</td><td>0.672</td><td>77.26</td><td>0.751</td></tr><tr><td>17</td><td>0</td><td>55.26</td><td>0.669</td><td>83.50</td><td>0.806</td></tr><tr><td>17</td><td>4</td><td>60.38</td><td>0.670</td><td>82.13</td><td>0.778</td></tr><tr><td rowspan="7">Equal</td><td>Factor Analysis</td><td></td><td>86.38</td><td>0.838</td><td></td><td></td></tr><tr><td>11</td><td>0</td><td>83.76</td><td>0.810</td><td>83.13</td><td>0.807</td></tr><tr><td>11</td><td>4</td><td>85.39</td><td>0.826</td><td>85.63</td><td>0.829</td></tr><tr><td>15</td><td>0</td><td>85.26</td><td>0.825</td><td>83.38</td><td>0.802</td></tr><tr><td>15</td><td>4</td><td>76.64</td><td>0.746</td><td>86.38</td><td>0.839</td></tr><tr><td>17</td><td>0</td><td>85.25</td><td>0.825</td><td>83.51</td><td>0.804</td></tr><tr><td>17</td><td>4</td><td>84.63</td><td>0.818</td><td>80.76</td><td>0.788</td></tr><tr><td rowspan="14">Skewed</td><td rowspan="7">Unequal</td><td>Factor Analysis</td><td></td><td>51.63</td><td>0.439</td><td></td><td></td></tr><tr><td>11</td><td>0</td><td>64.88</td><td>0.684</td><td>84.75</td><td>0.800</td></tr><tr><td>11</td><td>4</td><td>63.13</td><td>0.678</td><td>90.64</td><td>0.877</td></tr><tr><td>15</td><td>0</td><td>64.38</td><td>0.679</td><td>91.13</td><td>0.882</td></tr><tr><td>15</td><td>4</td><td>64.76</td><td>0.687</td><td>88.63</td><td>0.851</td></tr><tr><td>17</td><td>0</td><td>60.26</td><td>0.665</td><td>91.26</td><td>0.889</td></tr><tr><td>17</td><td>4</td><td>59.88</td><td>0.666</td><td>88.01</td><td>0.843</td></tr><tr><td rowspan="7">Equal</td><td>Factor Analysis</td><td></td><td>51.89</td><td>0.582</td><td></td><td></td></tr><tr><td>11</td><td>0</td><td>61.26</td><td>0.670</td><td>88.26</td><td>0.852</td></tr><tr><td>11</td><td>4</td><td>59.26</td><td>0.660</td><td>90.75</td><td>0.881</td></tr><tr><td>15</td><td>0</td><td>72.26</td><td>0.723</td><td>88.50</td><td>0.858</td></tr><tr><td>15</td><td>4</td><td>73.13</td><td>0.731</td><td>91.13</td><td>0.886</td></tr><tr><td>17</td><td>0</td><td>77.89</td><td>0.762</td><td>87.26</td><td>0.840</td></tr><tr><td>17</td><td>4</td><td>75.13</td><td>0.741</td><td>82.51</td><td>0.782</td></tr></table>

$$
\mathrm{A} = \sum_ {i} \sum_ {j} \frac {n _ {i j} (n _ {i j} - 1)}{2},
$$

$$
\mathrm{A} + \mathrm{B} = \sum_ {j} \frac {n _ {i .} (n _ {i .} - 1)}{2},
$$

$$
\mathrm{A} + \mathrm{C} = \sum_ {j} \frac {n _ {. j} (n _ {. j} - 1)}{2},
$$

from which the numerical values of B and C can be computed. By definition,

$$
\mathrm{A} + \mathrm{B} + \mathrm{C} + \mathrm{D} = _ {N} C _ {2},
$$

which in conjunction with the equations for $\mathrm { A } , \mathrm { A } \ + \ \mathrm { B } ,$ , and $\mathrm { ~ A ~ } + \mathrm { ~ C ~ } ,$ allows us to compute C and D. Then the Rand Index (R) is defined as

$$
R = \frac {(A + D) - [ (A + B) (A + C) + (C + D) (B + D) ] / _ {N} C _ {2}}{_ {N} C _ {2} - [ (A + B) (A + C) + (C + D) (B + D) ] / _ {N} C _ {2}}.
$$

The first term in the denominator represents the maximum possible value that $( \mathrm { ~ A ~ } + \mathrm { ~ D ~ } )$ can attain, which provides the required normalization. The second term with the negative sign in the numerator and the denominator represents the correction for chance agreement, which can be interpreted as follows. For the $2 \times 2$ table shown, where A, B, C, and D denote the cell counts in the four cells of the table, the count expected in cell (1, 1) under the hypothesis of independence between the row and column variables is the product of Row 1 marginal total times Column 1 marginal total divided by the total count for the entire table $( \mathrm { i . e . , ( A \mathrm { ~ + ~ } B ) ^ { * } ( A \mathrm { ~ + ~ } C ) / } _ { N } C _ { 2 } )$ . Similarly, the quantity $( \mathrm { C } ~ + ~ \mathrm { D } ) ^ { * } ( \mathrm { B } ~ + ~ \mathrm { D } ) / { } _ { N } C _ { 2 }$ gives the expected cell count for cell (2,2) under the independence hypothesis. Thus, the second term in the numerator and denominator is the count expected for the number of pairs in Classes (1) and (4), purely by chance (i.e., under the independence hypothesis).

## References

Balachandran, K., J. Buzydlowski, G. Dworman, S. O. Kimbrough. 1999. MOTC: An interactive aid for multidimensional hypothesis generation. J. Management Inform. Systems. 16(1) 17–36.

Bimbo, A. D., L. Landi, S. Santini. 1993. Three-dimensional planarfaced object classification with Kohonen maps. Optical Engrg. 32(6) 1222–1234.

Bose, Ranjit, V. Sugumaran. 1999. Application of intelligent agent technology for managerial data analysis and mining. Database for Advances in Inform. Systems. 30(1) 77–94.

Chen, L. D., T. Sakaguchi, M. N. Frolick. 2000. Data mining methods, applications, and tools. Inform. Systems Management. 17(1) 65– 70.

Chung, Michael, P. Gray, eds. 1999. Special section: Data mining. J. Management Inform. Systems. 16(1).

Cooper, Lee G., G. Giuffrida. 2000. Turning data mining into a management science tool: New algorithms and empirical results. Management Sci. 46(2) 249–264.

Cottrell, M., J. C. Fort. 1986. A stochastic model of retinotopy: A selforganizing process. Biol. Cybernetics 53 405–411.

DeSieno, D. 1988. Adding a conscience to competitive learning. Proc. Internat. Conf. Neural Networks. IEEE Press, New York, 117–124.

Dillon, W. R., D. G. Frederick, V. Tangpanichdee. 1985. Decision issues in building perceptual product spaces with multiattribute rating data. J. Consumer Res. 12(1) 47–63.

Doyle, Peter, John Saunders. 1985. Market segmentation and positioning in specialized industrial markets. J. Marketing. 49(2) 24– 32.

Fayyad, U. M., G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy, eds. 1996. Advances in Knowledge Discovery and Data Mining, AAAI Press/The MIT Press, American Association for Artificial Intelligence, Menlo Park, CA.

Hastie, T., Stuetzle, W. 1989. Principal curves. J. Amer. Statist. Assoc. 84 502–516.

Hubert, L., P. Arabie. 1985. Comparing partitions. J. Classification. 2(2/3) 193–218.

Joreskog, K. G., D. Sorbom. 1989. PRELIS 2 User’s Reference Guide. Scientific Software International, Chicago, IL.

Kohonen, T. 1984. Cybernetic Systems: Recognition, Learning, Self-Organization, E. R. Caianiello, G. Musso, eds. Research Studies Press, Ltd., Letchworth, Herfordshire, UK3.

——. 1989. Self-Organization and Associative Memory. 3rd ed. Springer-Verlag, New York, Berlin, Heidelberg.

——. 1995. Self-Organizing Maps, Springer-Verlag, New York, Berlin, Heidelberg.

Leinonen, L., T. Hiltunen, K. Torkkola, J. Kangas. 1993. Selforganized acoustic feature map in detection of fricative-vowel coarticulation. J. Acoustical Soc. America. 93(6) 3468–3474.

Linoff, Gordon. 1999. Data mining. Inform. 13(9) 18–24.

Lo, Z.-P., B. Bavarian. 1991. On the rate of convergence in topology preserving neural networks. Biol. Cybernetics 65 55–63.

Manikopoulos, C. N. 1994. Finite state vector quantisation with neural network classification of states. IEEE Proc.-F, New York 140(3) 153–161.

Mitra, S., S. K. Pal. 1994. Self-organizing neural network as a fuzzy classifier. IEEE Trans. Systems, Man, and Cybernetics. 24(3) 385– 399.

Murtagh, F. 1985. Multidimensional Clustering Algorithms, Physica-Verlag, Wurzburg, Germany.

——. 1995. Interpreting the Kohonen self-organizing feature map using contiguity-constrained clustering. Pattern Recognition Lett. 16(4) 399–408.

——, Hernandez-Pajares. 1995. The Kohonen self-organizing map method: An assessment. J. Classification. 12 165–190.

Neural Ware Reference Guide. 1990. NeuralWare, Inc., Pittsburgh, PA.

Peacock, Peter R. 1998. Data mining in marketing: Part 1. Marketing Management. 6(4) 8–18.

Piatetsky-Shapiro, G., W. J. Frawley, eds. 1991. Knowledge Discovery in Databases. AAAI Press/The MIT Press, Cambridge, MA.

Ritter, H., K. Schulten. 1986. On the stationary state of Kohonen’s self-organizing sensory mapping. Biol. Cybernetics 54 99–106.

——, Martinetz, K. Schulten. 1989. Topology-conserving maps for learning visuo-motor-coordination. Neural Networks. 2 159–168.

Michael Shaw, Associate Editor. This paper was received on March 13, 1998, and was with the authors 14 months for 3 revisions.

Sabourin, M., A. Mitiche. 1993. Modeling and classification of shape using a kohonen associative memory with selective multiresolution. Neural Networks. 6(2) 275–283.

Spangler, W. E., J. H. May, L. G. Vargas. 1999. Choosing data-mining methods for multiple classification: Representational and performance measurement implications for decision support, J. Management Inform. Systems. 16(1) 37–62.

Sung, Tae Kyung, N. Chang, G. Lee. 1999. Dynamics of modeling in data mining: Interpretive approach to bankruptcy prediction. J. Management Inform. Systems. 16(1) 63–85.

Van Hulle, M. M. 2000. Faithful Representations and Topographic Maps: From Distortion—Information-Based Self-Organization, John Wiley & Sons, Inc. New York.

Vanecko, J. J., A. W. Russo. 1999. Data mining and modeling as a marketing activity. Direct Marketing. 62(5) 52–55.

Vercauteren, L., G. Sieben, M. Praet, G. Otte, R. Vingerhoeds, L. Boullart, L. Calliauw, H. Roels. 1990. The classification of brain tumours by a topological map. Proc. Internat. Neural Networks Conf. Paris, France 387–391.

Walter, J. A., K. J. Schulten. 1993. Implementation of self-organizing neural networks for visuo-motor control of an industrial robot. IEEE Trans. Neural Networks. 4(1) 86–95.

Westphal, C., T. Blaxton. 1998. Data Mining Solutions—Methods and Tools for Solving Real-World Problems. Wiley Computer Publishing.

Yoon, Younghoc. 1999. Discovering knowledge in corporate data bases. Inform. Systems Management. 16(2) 64–71.

Zhao, Z., C. G. Rowden. 1992. Use of Kohonen self-organizing feature maps for HMM parameter smoothing in speech recognition. IEEE Proc.-F, New York 139(6) 385–390.
