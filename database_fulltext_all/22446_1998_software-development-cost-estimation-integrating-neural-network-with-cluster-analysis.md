---
otero_id: 22446
otero_key: "SPWCQACG"
title: "Software development cost estimation: Integrating neural network with cluster analysis"
authors: "Anita Lee; Chun Hung Cheng; Jaydeep Balakrishnan"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00041-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Software development cost estimation: Integrating neural network with cluster analysis

Anita Lee $^{a,*}$ , Chun Hung Cheng $^{1,b}$ , Jaydeep Balakrishnan $^{2,c}$

$^{a}$ Decision Science and Information Systems Area, School of Management, Gatton College of Business and Economics, University of Kentucky, Lexington, KY 40506-0034, USA

$^{b}$ Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Shatin, New Territories, Hong Kong

$^{c}$ Faculty of Management, University of Calgary, 2500 University Drive N.W., Calgary, Alberta T2N 1N4, Canada

Received 19 March 1997; accepted 15 March 1998

## Abstract

For software project planning control and management, an accurate estimate of software development cost is important. Past research has focused on using parametric models to predict development cost based on attributes such as lines of code or function points. This requires researchers to identify the set of factors that influence cost estimation before the system is constructed. We propose a non-parametric approach that integrates a neural network method with cluster analysis to estimate development cost. The integration of the two techniques not only allows for a more accurate cost estimate but also leads to an increase in the training efficacy of the network. © 1998 Elsevier Science B.V. All rights reserved

Keywords: Software development cost; Neural network; Cluster analysis; Machine learning

## 1. Introduction

Accurate cost estimation of a software development effort is critical for good management decision making; the estimate must include software project control, budgeting, personnel allocation, and bidding for contracts. An accurate cost estimation is important, because a low cost estimate may either cause loss or compromise the quality of the software developed, resulting in partially functional or insufficiently tested software that requires later high maintenance costs. However, if the cost estimate is too high, many useful projects may not be funded, resulting in misallocation of resources and a backlog of needed software. An early cost estimate is equally important because the result will have value for project management and control only if it is provided in the early phases of the software development life cycle, preferably during the planning and requirement analysis rather than the coding and testing phases. Thus, from an organizational perspective, an early and accurate cost estimate will reduce the possibility of organizational conflict during the later stages.

This paper is intended to provide software managers with a decision support tool for early cost estimation of software development efforts. The work is motivated by the need to explore innovative ways to estimate software development cost in the 1990s due to the increasing complexity of the problem space as a result of advances in computer technologies, expert system applications, and interorganizational systems $[2, 21]$ . A new technique integrating a neural network method with cluster analysis is implemented and tested using historical data and demonstrated to show how it improves network performance. Unlike prior approaches to software development cost estimation such as size-based, function-based, or decision-tree learning based models, the new technique is capable of distinguishing relevant cost estimation factors from irrelevant ones. This relieves the need to specify the set of cost estimation factors beforehand. In addition, the cost estimated by our technique yields higher accuracy in our experimental study.

## 2. Literature review

Software cost is growing at an annual rate of 12% and is expected to reach \$400 billion by the year 2000 [4]. However, a significant amount of the cost, 40% or more, is devoted to the maintenance of existing software instead of developing much needed new products [5]. In addition, software cost is related closely to software quality and productivity. Unrealistically low cost estimates frequently lead to poor product quality and low project productivity [11]. Therefore, the importance of understanding software cost has motivated considerable research to identify factors that influence software costs. This has yielded a number of software cost estimation models.

## 2.1. Size-based models

Size-based models consider project size measured in lines of code (LOC) or thousands of lines of code (KLOC) to be the primary factor affecting software cost estimation. There are two parts to these cost estimation models. One provides a base estimate of development effort as a function of software size; it is of the form:

$$
E = A + B \times (\mathrm{KLOC}) ^ {c}
$$

Table 1  
An overview of size-based models

<table><tr><td rowspan="2">Model name</td><td colspan="3">Base estimate</td></tr><tr><td>A</td><td>B</td><td>C</td></tr><tr><td>Walston-Felix</td><td></td><td>5.2</td><td>0.91</td></tr><tr><td>Bailey-Basili</td><td>5.5</td><td>0.73</td><td>1.16</td></tr><tr><td>Boehm basic</td><td></td><td>3.2</td><td>1.05</td></tr><tr><td>Boehm intermediate</td><td></td><td>3</td><td>1.12</td></tr><tr><td>Boehm advanced</td><td></td><td>2.8</td><td>1.2</td></tr><tr><td>Doty</td><td></td><td>5.288</td><td>1.047</td></tr></table>

where E is the estimated effort in man-months; A, B, and C are constants.

The second modifies the base estimate by taking into account such environmental factors as the method used in top-down design, structured code, personnel experience and ability, etc..

Typical models of this kind include the Walston–Felix model $[20]$ , Doty model $[8]$ , Bailey–Basili model $[1]$ , and Boehmn's Constructive Cost model (COCOMO) $[3]$ . Among these models, COCOMO is the most widely known and studied. Table 1 provides an overview of each of these models in its base estimate form.

The problems with using LOC as an estimate of project size include:

1. there is no accepted definition of LOC and few researchers specified the line-counting rules used, resulting in variations and uncertainty;

2. LOC is language dependent; fewer LOC may be required for a higher-level language than a lower-level language and yet the time per line is greater, resulting in difficulty in directly comparing projects using different languages;

3. it is difficult to estimate LOC. An experiment performed by Yourden where the size of 16 projects was estimated by experienced managers based on the specification of each project, showed a discrepancy between estimated and actual project size ranging from $-210\%$ to $83\%$ , as shown in Table 2 [10];

4. LOC places undue emphasis on coding, which accounts for only 10 to 15% of the total effort in software development [6]. Hence, factors other than size should be considered in estimating software development cost.

Table 2  
The discrepancy between estimated and actual project size

<table><tr><td>Project</td><td>Actual</td><td>Predicted</td><td>Actual–predicted</td><td>% Difference</td></tr><tr><td>1</td><td>70900</td><td>34700</td><td>36200</td><td>51%</td></tr><tr><td>2</td><td>129000</td><td>32100</td><td>96900</td><td>75%</td></tr><tr><td>3</td><td>23000</td><td>22000</td><td>1000</td><td>4%</td></tr><tr><td>4</td><td>34600</td><td>9100</td><td>25500</td><td>74%</td></tr><tr><td>5</td><td>23000</td><td>12000</td><td>11000</td><td>48%</td></tr><tr><td>6</td><td>25000</td><td>7300</td><td>17700</td><td>71%</td></tr><tr><td>7</td><td>52100</td><td>28500</td><td>23600</td><td>45%</td></tr><tr><td>8</td><td>7650</td><td>8000</td><td>-350</td><td>-5%</td></tr><tr><td>9</td><td>25900</td><td>30600</td><td>-4700</td><td>-18%</td></tr><tr><td>10</td><td>16300</td><td>2720</td><td>13580</td><td>83%</td></tr><tr><td>11</td><td>17400</td><td>15300</td><td>2100</td><td>12%</td></tr><tr><td>12</td><td>33900</td><td>105000</td><td>-71100</td><td>-210%</td></tr><tr><td>13</td><td>57200</td><td>18500</td><td>38700</td><td>68%</td></tr><tr><td>14</td><td>21000</td><td>35400</td><td>-14400</td><td>-69%</td></tr><tr><td>15</td><td>8640</td><td>3650</td><td>4990</td><td>58%</td></tr><tr><td>16</td><td>17500</td><td>2950</td><td>14550</td><td>83%</td></tr></table>

## 2.2. Function-based models

Function-based models use other counts than LOC in estimating software development cost. 'Function Points' as defined by Albrecht of IBM in 1979 involve a process called function point analysis (FPA) [14]. Albrecht's FPA involves the following steps:

1. Identify the major system components: external inputs, external outputs, logical internal files, external interface files, and external inquiries.

2. Classify each component as ‘simple’, ‘average’, or ‘complex’ depending on the number of interacting data elements and other factors.

3. Calculate the unadjusted function points (UFP) using the following table, which includes weights:

<table><tr><td></td><td colspan="4">Complexity</td></tr><tr><td>Function type</td><td>Simple</td><td>Average</td><td>Complex</td><td>Total</td></tr><tr><td>External input</td><td>—×3</td><td>—×4</td><td>—×6</td><td></td></tr><tr><td>External output</td><td>—×4</td><td>—×5</td><td>—×7</td><td></td></tr><tr><td>Logical internal file</td><td>—×7</td><td>—×10</td><td>—×15</td><td></td></tr><tr><td>External interface filex</td><td>—5×7</td><td>—×10</td><td></td><td></td></tr><tr><td>External inquiry</td><td>—×3</td><td>—×4</td><td>—×6</td><td></td></tr><tr><td></td><td>Total unadjusted function points</td><td></td><td></td><td></td></tr></table>

4. Adjust the unadjusted function points for application and environment complexity through a measure called the complexity adjustment factor (CAF), i.e., function points=UFP×CAF.

CAF is calculated by using the formula:

$$
\mathrm{CAF} = 0. 6 5 + 0. 0 1 N
$$

where N is the total degree of influence (DI) of 14 characteristics which are data communications, distributed processing, performance objective, configuration load, transaction rate, on-line data entry, end-user efficiency, on-line update, complex processing, reusability, installation ease, operational ease, multiple sites, and change facilitation. DI takes a value from 0 (no influence) to 5 (strongest influence).

There are several problems with using FPA, including:

1. it is designed for business applications and is not appropriate for scientific or technical applications in which complex algorithms are involved;

2. the validity of the method for general objective assessment of system costs is questionable because many elements such as the weighting factors, component complexity, complexity factors, and degree of influence are subjectively developed for a particular environment only; and

3. systems of high internal complexity are not adequately considered.

## 2.3. Learning-based models

Both size-based and function-based models are parametric; they use a function/formula of fixed form for software cost estimation $[18]$ . Assumptions about the form of the function are needed. Also, the function developed is static, i.e., the factors and their corresponding degree of influence on cost estimation are fixed. More importantly, the set of influential factors on cost estimation is identified before the model can be constructed. Learning-based models are developed to overcome these problems. These models make no assumptions about the form of the function under study and they are capable of learning incrementally as new data are provided over time. In addition, the availability of historical data on this problem domain makes it particularly suitable for the application of a type of machine learning technique called ‘learning by example'. Learning by example attempts to infer or generalize regularities from specific instances of a concept. Thus, the success of applying this type of example-driven learning technique requires the provision of domain-specific knowledge in the form of training and testing data sets. The background of this learning technique and a review of its recent applications can be found in Refs. [19, 9], respectively.

## 2.3.1. Decision tree learning models

These models construct a decision tree for software cost estimation $[15, 16]$ . The nodes of the tree represent attributes that best divide the data into disjoint groups. The leaves of the tree represent the average cost of software development. By descending the tree along an appropriate path, the cost of software development can be determined.

Relevant attributes for cost estimation are identified from previous efforts. Data on these attributes is accumulated to allow the construction of a decision tree through a process called recursive-partitioning regression in which the best ‘divisive’ attribute is selected to partition the data into subsets. The process is recursively repeated on these subsets as the tree is expanded until no further partitioning is feasible. Various attribute selection measures have been proposed. For example, ID3 selects the most informative attribute based on a measure that minimizes the following function:

$$
E (A) = - \sum_ {i = 1} ^ {V} \frac {S _ {i}}{S} \sum_ {j = 1} ^ {N} \frac {k _ {j i}}{S _ {i}} \log_ {2} \frac {k _ {j i}}{S _ {i}}
$$

where V is the number of values for attribute A, $k_{ji}$ the number of examples in the jth category with the ith value for attribute A, S the total number of examples, $S_{i}$ the number of examples with the ith value for attribute A, and N the number of categories.

One problem with this type of learning model is that the set of relevant attributes must be identified beforehand. A neural network, with its ability to differentiate relevant from irrelevant attributes, offers a more flexible approach to estimating software development cost. Moreover, empirical evidence suggests that a learning procedure based on a neural network often outperforms decision tree in terms of prediction accuracy $[17]$ .

## 2.3.2. Neural network learning models

These models are built on networks of processing units called neurons that are arranged in layers and are connected to one another by restricted links (see $[12]$ ). Links between neurons have associated weights. Each neuron in the network computes a non-linear function of its inputs; these are called activation functions. The most common one of the activation function is:

$$
\frac {1}{1 + \exp [ - \sum W _ {\mathrm{i}} I _ {\mathrm{i}} ]}
$$

where $W_{i}I_{i}$ is a weighted sum of the inputs, $I_{i}$ , to neuron ‘i’. The resultant value is passed along to the next layer after being multiplied by the connecting weight. This process is repeated all the way from the input layer to the output layer. The goal here is to generate an accurate mapping between input (project attributes) and output (software development cost) patterns.

Different learning procedures have been proposed to train the network to generate appropriate output patterns for corresponding input patterns. One of the most commonly used is called back-propagation, in which the weights are modified in such a way as to reduce the error between actual and correct outputs on sample patterns. The error is determined by comparing the network's actual output pattern with an a priori known output pattern. The difference or error between the two is 'back-propagated' through the net by modifying the weights (see [7, 13] for recent business applications of back-propagation neural networks).

Srinivasan and Fisher point out that the performance of neural network approaches is very sensitive to configuration choices, such as the number of hidden units, the stopping criteria, and the initial weight settings. The appropriate settings of these choices can only be determined empirically. Thus, the manner in which the network should be trained is a concern. We give here a new approach that integrates neural network methods with cluster analysis to improve both training efficacy and network performance.

## 3. The approach

Our approach involves two phases: the first groups similar projects together by cluster analysis to facilitate the training of the neural network in the second phase. Cluster analysis is designed to identify similar objects in an n-dimensional space, where n is the number of descriptive attributes of the object. When applied to the problem domain of software development cost estimation, it is assumed that similar projects share similar development cost. The similarity among different projects, once computed, can then be used as a valuable piece of input information to enhance the training efficiency of the network.

## 3.1. Cluster analysis

Projects are grouped together into clusters based on a similarity measure termed a resemblance coefficient. Two kinds of coefficients are computed, depending on the types of attributes. For quantitative attributes, the average Euclidean or RMS distance between two projects in an n-dimensional space is used. It is defined as:

$$
d _ {j k} = \sqrt {\frac {\sum_ {i = 1} ^ {n} (x _ {i j} - x _ {i k}) ^ {2}}{n}}
$$

where $d_{jk}$ is the average Euclidean distance between projects j and k, $x_{ij}$ the value of project j's attribute i, $x_{ik}$ the value of project k's attribute i, and n the number of quantitative attributes. The average Euclidean distance is, in fact, a measure of dissimilarity between two projects: the smaller the value of the coefficient, the more similar are the two projects.

For nominal attributes, the Jaccard coefficient is used and is defined as:

$$
C _ {j k} = - 1 \times \frac {N (1 - 1)}{2 \times N (\text { Data }) - N (1 - 1)}
$$

where $C_{jk}$ is the Jaccard coefficient of projects j and k, $N(1-1)$ the number of matches between projects j and k over all nominal attributes and N(Data) the total number of nominal attributes. Like the average Euclidean distance, a smaller value of the Jaccard coefficient indicates a higher similarity between two projects. Since the two coefficients have different ranges of values, the two coefficients are converted to standard deviations using the standard score method before combining them.

A tree is then constructed based on the combined resemblance coefficients by using a hierarchical clustering analysis technique, the unweighted pair-group method. This iteratively selects the two most similar objects to cluster into one new ‘object’ until all objects are clustered. Various ways of forming the clusters can be read off from the tree. Our strategy is to cut the tree at the point where the range of the resemblance coefficient is the highest, because a large range in the value of the resemblance coefficient indicates that the resulting clusters are well separated in the attribute space.

## 3.2. Neural network

In phase two, a neural network is first trained, based only on attributes given from the project description to determine the appropriate settings for the following network configuration: (1) the number of neurons per layer; (2) the size and selection of training and testing data; and (3) the choice of the activation function. These network configuration parameters can only be determined empirically as different problem domains require different settings. Hence, the network is trained twice with the intent that the best configuration choice will be decided in the first round. Then the information from phase one – the cluster analysis and the preliminary neural network – is fed as input to a second round of neural network training to complete the task of software development cost estimation. Our experimental study indicates that the proposed approach can lead to improved network performance.

## 4. Experimental study

The approach was tested by using the COCOMO dataset. Based on a regression analysis of 63 projects, Boehm developed three forms of COCOMO: the basic, intermediate, and advanced. The basic model produces a base estimate of development effort using KLOC only; the intermediate model adds 15 qualitative cost drivers to improve the base estimate. These cost drives are classified into four categories: software product attributes; computer attributes; personnel attributes; and project attributes, as shown in Table 3. The advanced model assesses the cost drives at each development phase. In addition to the 15 cost drivers, the COCOMO dataset also has other attributes, giving a total of 39 descriptive project attributes. A complete list is included in the Appendix A.

Table 3  
Cost drivers in intermediate COCOMO

<table><tr><td>Product attributes</td><td>Required software reliabilityDatabase sizeProduct complexity</td></tr><tr><td>Computer attributes</td><td>Execution time constraintMain storage constraintVirtual machine volatilityComputer turnaround time</td></tr><tr><td>Personnel attributes</td><td>Analyst capabilityApplications experienceProgrammer capabilityVirtual machine experienceProgramming language experience</td></tr><tr><td>Project attributes</td><td>Modern programming practicesUse of software toolsRequired development schedule</td></tr></table>

## 4.1. Cluster analysis

In phase one, 24 of the 39 attributes were selected as critical cost-determining factors for cluster analysis. These attributes are ones that are used in the intermediate and advanced models of COCOMO. The 63 projects were selected in six different ways (as shown in Table 4) to serve as data for cluster analysis.

These six ways of clustering were compared using a common set of testing data. Assuming that two projects sharing similar project attributes will have similar software development cost, each project in the testing set was matched with a cluster and its software development cost was estimated as the ranked-sum-mean of all the cost of the projects in that cluster. The error between the estimated cost and the actual cost could then be measured. The average percentage estimation error was then used as the basis for selecting the 'best' way of clustering all 63 projects of the COCOMO data. According to the results reported in Table 5, the projects should be clustered in ways suggested by using DATA25-3, which yields the lowest average error in testing. This additional clustering information, i.e., to which cluster each project belonged, was passed to phase two.

## 4.2. Neural network

The appropriate network configuration choices and its sensitivity to various input data and activation functions were then analyzed in a series of four experiments. The first determined the best network configuration among six different settings. The settings are denoted by three numbers of the form, m:n:o, where m is the number of neurons in the input layer, n the number of neurons in the hidden layer, and o the number of neurons in the output layer. The same set of training and testing data (involving all 63 projects) were used. Of all the projects, 50 were randomly selected as training data and the remaining 13 were used for testing. All 39 project attributes could be used without screening, since the neural network approach has the ability to discern relevant attributes from irrelevant ones. The second experiment determined the sensitivity of the network towards input data by training the network using three different sets of training and testing data. The last combined the results of the first two to finalize the best setting of the network configuration. The results of each experiment are shown in Tables 6–8. The best configuration is found to be 20:15:1 trained by using 41 projects (34 for training and 7 for testing). The 41 projects are selected from the original 63 by eliminating extreme cases so that the range of the actual development effort is reduced from 11400 to 440 man-months.

Table 4  
Six datasets for cluster analysis

<table><tr><td>Dataset</td><td>Means of selection</td></tr><tr><td>DATA50</td><td>Select 50 projects randomly</td></tr><tr><td>DATA34</td><td>Select 41 projects, excluding extreme cases based on actual man-months</td></tr><tr><td>DATA25-1</td><td>Select 25 projects from DATA34 randomly</td></tr><tr><td>DATA25-2</td><td>Select 25 projects from DATA34 randomly</td></tr><tr><td>DATA25-3</td><td>Select 25 projects from DATA34 randomly</td></tr><tr><td>DATA25-4</td><td>Select 25 projects from DATA34 randomly</td></tr></table>

Table 5  
Performance comparison of the cluster analysis datasets

<table><tr><td>Dataset</td><td>Average % error</td></tr><tr><td>DATA50</td><td>57%</td></tr><tr><td>DATA34</td><td>39%</td></tr><tr><td>DATA25-1</td><td>37%</td></tr><tr><td>DATA25-2</td><td>29%</td></tr><tr><td>DATA25-3</td><td>26%</td></tr><tr><td>DATA25-4</td><td>36%</td></tr></table>

Table 6  
Result of Experiment 1

<table><tr><td>Network configuration (i : j : k)</td><td>Best average % error</td><td>No. of iteration</td></tr><tr><td>10 : 0 : 1</td><td>495%</td><td>100000</td></tr><tr><td>15 : 0 : 1</td><td>346%</td><td>40000</td></tr><tr><td>20 : 0 : 1</td><td>494%</td><td>1000</td></tr><tr><td>10 : 5 : 1</td><td>148%</td><td>9000</td></tr><tr><td>15 : 10 : 1</td><td>238%</td><td>5000</td></tr><tr><td>20 : 15 : 1</td><td>382%</td><td>1000</td></tr></table>

Note: i is the number of neurons in the input layer, j the number of neurons in the hidden layer, and k the number of neurons in the output layer.

Table 7  
Result of Experiment 2

<table><tr><td rowspan="2">Network configuration</td><td colspan="3">Best average % error</td></tr><tr><td>63 Projects (50 training, 13 testing)</td><td>47 Projects (38 training, 9 testing)</td><td>41 Projects (34 training, 7 testing)</td></tr><tr><td>10:0:1</td><td>495%</td><td>77%</td><td>281%</td></tr><tr><td>15:0:1</td><td>346%</td><td>321%</td><td>186%</td></tr><tr><td>20:0:1</td><td>494%</td><td>92%</td><td>101%</td></tr><tr><td>10:5:1</td><td>148%</td><td>78%</td><td>62%</td></tr><tr><td>15:10:1</td><td>238%</td><td>65%</td><td>42%</td></tr><tr><td>20:15:1</td><td>382%</td><td>109%</td><td>36%</td></tr></table>

Table 8  
Result of Experiment 3

<table><tr><td>Network configuration</td><td>Best average % error (41 projects)</td></tr><tr><td>10:0:1</td><td>281%</td></tr><tr><td>15:0:1</td><td>186%</td></tr><tr><td>20:0:1</td><td>101%</td></tr><tr><td>10:5:1</td><td>62%</td></tr><tr><td>15:10:1</td><td>42%</td></tr><tr><td>20:15:1</td><td>36%</td></tr><tr><td>30:20:1</td><td>178%</td></tr><tr><td>40:30:1</td><td>67%</td></tr><tr><td>50:40:1</td><td>156%</td></tr></table>

The cost estimates obtained from both the cluster analysis and preliminary network analysis were used as additional input attributes to train the neural network a second time using the best configuration choices found earlier. In other words, the 41 project cases (34 training and 7 testing) were used to train a neural network of configuration 20:15:1. The performance of the integrated network was compared to the one without integration by using four different sets of testing data. Significant improvement in network performance in terms of estimation accuracy was found in all four cases, as show in Table 9.

Table 9  
Network performance comparisons on best average % error

<table><tr><td>Testing cases</td><td>Pure NN</td><td>NN+cluster</td><td>Improvement</td></tr><tr><td>Set 1</td><td>36%</td><td>32%</td><td>12%</td></tr><tr><td>Set 2</td><td>37%</td><td>23%</td><td>37%</td></tr><tr><td>Set 3</td><td>62%</td><td>30%</td><td>51%</td></tr><tr><td>Set 4</td><td>52%</td><td>35%</td><td>33%</td></tr></table>

## 5. Conclusion

We demonstrated in this paper that integrating neural network with cluster analysis is a viable and promising approach to provide relatively accurate estimates of software development cost. By integrating neural network with cluster analysis, one can increase the training efficacy of the network, resulting in a more accurate cost estimate than by using a pure neural network approach. The estimates are derived early on in the software development life cycle so that appropriate software project management and control can be exercised.

## Acknowledgements

Dr. Balakrishnan's research is supported by the Natural Sciences and Engineering Research Council (NSERC) of Canada.

## Appendix A

## Project attributes in the COCOMO dataset

Project attributes
1 Project type
2 Year developed
3 Programming languages
4 Required software reliability
5 Database size
6 Product complexity
7 Adaptation adjustment factor

8 Execution time constraint  
9 Main storage constraint  
10 Virtual machine volatility  
11 Computer turnaround time  
12 Type of computer used  
13 Analyst capability  
14 Project team experience  
15 Programmer capability  
16 Virtual machine experience  
17 Programming language experience  
18 Personnel continuity on project  
19 Modern programming practices  
20 Software tools  
21 Required development schedule  
22 Requirement volatility effort multipliers  
23 Effort multipliers  
24 Software development mode  
25 Total delivered source instructions in thousands  
26 Adjusted delivered source instructions in thousands  
27 Nominal man-months  
28 Intermediate estimated man-months  
29 Percentage estimation error in man-months estimation  
30 Project productivity  
31 Estimated development time in months  
32 Percentage estimation errors for months estimation  
33 Detailed estimated man-months  
34 Percentage estimation error for detailed estimated man-months  
35 Normalized effort parameter  
36 Basic estimated man-months  
37 Basic estimation error ratio  
38 Thousands of pages of project documentation  
39 Pages of documentation per thousand source instruction

## References

[1] J.W. Bailey, V.R. Basili, A meta-model for source development resource expenditures, Proceedings of the Fifth International Conference on Software Engineering, 1981, pp. 107–116.

[2] F. Bergeron, J. St-Arnaud, Estimation of information systems development efforts: Pilot study, Information and Management 22(4), 1992, pp. 239–254.

[3] B.W. Boehm, Software Engineering Economics, Englewood Cliffs, Prentice-Hall, NJ, 1981.

[4] B.W. Boehm, P.N. Papaccio, Understanding and controlling software costs, IEEE Transactions on Software Engineering 14(10), 1988, pp. 1462–1477.

[5] F.P. Brooks, The Mythical Man-Month: Essays on Software Engineering, Reading, Addison-Wesley, MA, 1982.

[6] R.D. Ermick, In search of a better metric for measuring productivity of application development, Proceedings of Function Point Users Group Conference, 1987.

[7] D. Fletcher, E. Goss, Forecasting with neural networks: An application using bankruptcy data, Information and Management 24(3), 1993, pp. 159–167.

[8] J.R. Herd, J.N. Postak, W.E. Russel, K.R. Stewart, Software Cost Estimation Study-Study Result. Technical Report RADC-TR-77-220, Doty Associates, Inc., Rockville, MD, 1977.

[9] P. Langley, H.A. Simon, Applications of Machine Learning and Rule Induction, Communications of the ACM 38(11) 55–64.

[10] L.A. Laranjeira, Software size estimation of object-oriented systems, IEEE Transactions on Software Engineering 16(5), 1990, pp. 510–522.

[11] W.E. Lehder Jr., D.P. Smith, W.D. Yu, Software estimation technology, AT & T Technical Journal (1988) 10–18.

[12] E.Y. Li, Artificial neural networks and their business applications, Information and Management 27, 1994, pp. 303–313.

[13] R.W. Lodewyck, P.S. Deng, Experimentation with a backpropagation neural network: An application to planning and user system development, Information and Management 24(1), 1993, pp. 1–9.

[14] G.C. Low, D.R. Jeffery, Function points in the estimation and evaluation of the software process, IEEE Transactions on Software Engineering 16(1), 1990, pp. 64–71.

[15] A. Porter, R. Selby, Empirically-guided software development using metric-based classification tree, IEEE Software 7(5), 1990, pp. 46–54.

[16] R. Selby, A. Porter, Learning from examples: Generation and evaluation of decision trees for software resource analysis, IEEE Transactions on Software Engineering 14, 1988, pp. 1743–1757.

[17] J.W. Shavlik, R.J. Mooney, G.G. Towell, Symbolic and neural learning algorithms: An experimental comparison, Machine Learning 6(2), 1991, pp. 111–143.

[18] K. Srinivasan, D. Fisher, Machine learning approaches to estimating software development effort, IEEE Transactions on Software Engineering 21(2), 1995, pp. 126–136.

[19] K.Y. Tam, Automated construction of knowledge-bases from examples, Information Systems Research 1(2), 1990, pp. 144–167.

[20] C.E. Walston, C.P. Felix, A method of programming measurement and estimation, IBM Systems Journal 16(1), 1977, pp. 54–73.

[21] Y. Yoon, T. Guimaraes, Selecting expert system development techniques, Information and Management 24(4), 1993, pp. 209–223.

![](/api/attachments/SPWCQACG/fulltext/images/c7cec2b86272c1dde23fbcba0a42363457c90c7920225749b254bbd3ee0f53f1.jpg)  
Anita Lee is an Associate Professor of the Decision Science and Information Systems area at the University of Kentucky. She received her Ph.D. in Business Administration from the University of Iowa in 1990. Her research interests include artificial intelligence, machine learning, knowledge-based systems, computer integrated manufacturing, and group technology. She has published extensively in numerous refereed jour-

nals including Annals of Operations Research, Expert Systems, IEEE Expert, International Journal of Production Research, etc..

She is currently an associate editor for Journal of Database Management.

![](/api/attachments/SPWCQACG/fulltext/images/58d4fc6f18de02cedb95b3ca64e086d803c8a1fa7c2db50ec426ebfc662a1073.jpg)

Chun Hung Cheng obtained his Ph.D. in Business Administration from the University of Iowa and started his teaching career at Kentucky State University. He returned to Hong Kong in 1994 and is now an Associate Professor at the Chinese University of Hong Kong. He conducts research in Information Systems and Operations Management. His research articles have appeared in

journals including Annals of Operations Research, Expert Systems, Expert Systems with Applications, IEEE Transactions on Man, Systems, and Cybernetics, IIE Transactions, International Journal of Production Research, Operations Research, etc.

![](/api/attachments/SPWCQACG/fulltext/images/3218782dfdcb7159b8bd20ad00a9db564bc95644dc9ec53ece292f95105bc454.jpg)

Jaydeep Balakrishnan is currently Associate Professor of Operations Management in the Faculty of Management at the University of Calgary. He has a Ph.D. from Indiana University and an MBA from the University of Georgia, both in Operations Management. His undergraduate degree is in Mechanical Engineering from Nagpur University in India. He has also worked for the

automobile industry in India. Dr. Balakrishnan's research interests include facility layout. He has published in journals including Management Science, The European Journal of Operational Research, and OMEGA. He has also presented papers at various international conferences. During 1995–96 he was a Visiting Scholar at the Chinese University of Hong Kong.
