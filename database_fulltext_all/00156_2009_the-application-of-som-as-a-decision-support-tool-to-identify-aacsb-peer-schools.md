---
otero_id: 156
otero_key: "TUREXYCQ"
title: "The application of SOM as a decision support tool to identify AACSB peer schools"
authors: "Melody Y. Kiang; Dorothy M. Fisher; Jeng-Chung Victor Chen; Steven A. Fisher; Robert T. Chi"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.12.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The application of SOM as a decision support tool to identify AACSB peer schools

Melody Y. Kiang <sup>a,e,</sup>⁎, Dorothy M. Fisher <sup>b</sup>, Jeng-Chung Victor Chen <sup>c</sup>, Steven A. Fisher <sup>d</sup>, Robert T. Chi <sup>a</sup>

<sup>a</sup> Department of Information Systems, College of Business Administration, California State University, Long Beach, United States <sup>b</sup> Department of Information Systems and Operations Management, College of Business Administration and Public Policy, California State University, Dominguez Hills, United States S Denartment of Transnortation and Communication Management Science, National Cheng Kung University Taiwar

Department of Transportation and Communication Management Science, National Cheng Kung University, Taiwan

<sup>d</sup> Department of Accountancy, College of Business Administration, California State University, Long Beach, United States

<sup>e</sup> School of Management, Harbin Institute of Technology, Heilongjiang, China

## a r t i c l e i n f o

Article history: Received 6 March 2008 Received in revised form 29 September 2008 Accepted 28 December 2008 Available online 12 January 2009

Keywords: Kohonen SOM networks Cluster analysis AACSB accreditation Data mining

## a b s t r a c t

For a business school, the selection of its peer schools is an important component of its International Association for Management Education (AACSB) (re)accreditation process. A school typically compares itself with other institutions having similar structural and identity-based attributes. The identification of peer schools is critical and can have a signi<sup>fi</sup>cant impact on a business school's accreditation efforts. For many schools the selection of comparable peer schools is a judgmental process. This study offers an alternative means for selection; a quantitative technique called Kohonen's Self-Organizing Map (SOM) network for clustering. In this research, we <sup>fi</sup>rst demonstrate the capability of SOM as a clustering tool to visually uncover the relationships among AACSB-accredited schools. The results suggest that SOM is an effective and robust clustering method. Then, we compare the results of SOM with that of other clustering methods, such as K-means, Factor/K-means analysis, and kth nearest neighbor procedure. The objective of this study is to demonstrate that a two-dimensional SOM map can be used to integrate the results of various clustering methods and, thus, act as a visual decision support tool.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

AACSB accreditation is critical to the success of a collegiate business school. It gives the school prestige by placing it in an elite group of accredited institutions that meet strict quality standards. However, more tangible bene<sup>fi</sup>ts of accreditation include improved curriculum and operations, enhanced fund-raising, and the ability to attract and retain quality students and faculty. Accreditation is an arduous and costly process that requires a school to meet AACSB standards as well as to re<sup>fl</sup>ect on its own mission, operations, and direction.

A key dimension of a business school's (re)accreditation process is the selection of its comparable peer schools. For a self-analysis, a school typically compares itself to other institutions having similar structural and identity-based attributes such as size, degree-granting type, resources, etc. Comparison with peer schools is necessary for understanding and evaluating the business school's current performance and future goals. AACSB de<sup>fi</sup>nes comparable peers as “…schools who are considered to be similar in mission and are assumed to be appropriate for performance comparison” [5] (http://www.aacsb.edu/accreditation/glossary.asp). AACSB requires a business school to identify a minimum of six comparable schools.

The selection of comparable peers is a critical process and can have a signi<sup>fi</sup>cant impact on a school's accreditation efforts. For many schools the selection of comparable peers is a judgment made by a college committee. However, this can be a formidable task given the large number of business schools and the many relevant attributes. In this research, we <sup>fi</sup>rst introduce an alternative means for selection; a quantitative technique called Kohonen's SOM networks, an unsupervised learning neural network for clustering, to assist schools in identifying their “AACSB comparable peers”.

The Self-Organizing Map (SOM) network, a variation of neural computing networks, is a categorization network developed by Kohonen [14–16]. The SOM network was originally designed for solving problems that involve tasks such as clustering, visualization, and abstraction. The main function of SOM networks is to map the input data from an n-dimensional space to a lower dimensional (usually one or two-dimensional) plot while maintaining the original topological relations. The physical locations of points on the map show the relative similarity between the points in the multi-dimensional space. Each node on the map can be considered as a cluster by itself. An extension of SOM has been developed and tested by Kiang [9] to further group the nodes into smaller number of clusters. This is especially useful when the number of output nodes is more than the number of desired clusters. The purpose of maintaining a reasonable size output map is to help the decision maker visualize the relationship among the input data in a less abstract manner. The fewer nodes we have on the map, the more abstract the output. The extended

SOM technique enables the map to depict more detailed membership relationships between and within clusters while maintaining the capability of deriving any desired number of clusters.

In cluster analysis, we try to identify similar elements by their attributes. We form groups, or clusters, that are homogeneous but are different from other groups. SOM networks combine competitive learning with dimensionality reduction by smoothing the clusters with respect to an a priori grid and provide a powerful tool for data visualization. Kohonen's SOM networks have been successfully applied to clustering problems such as gene research [6,7], text mining [2], market segmentation [11], MBA school selection [13] and web search tools [20].

In this research, we apply the clustering and visualization capabilities of SOM to plot the 229 AACSB accredited schools into a twodimensional map. We further apply the extended SOM feature to cluster the schools on the map into groups with desired number of data points. The map will assist a candidate school to properly identify its peer schools for comparison during the AACSB (re)accreditation process. Comparative analysis of the outputs from SOM with those from other popular clustering methods is also included in this study.

The main objective of this study is to introduce SOM as an integration tool to combine clustering results from different clustering approaches including traditional statistics and arti<sup>fi</sup>cial intelligence technique and present the results in a user-friendly format. The visual map generated by SOM is used as the basis for plotting the results from other clustering methods. It allows the decision maker to visualize the relationship among different clustering results to make informed decisions. Thus, both objective criteria from school pro<sup>fi</sup>le data and subjective criteria such as vicinity and familiarity of the schools can be taken into considerationwhen making the <sup>fi</sup>nal selection. We believe the same tool can be applied to other problem domains that involve clustering tasks.

The balance of the paper is organized as follows: Section 2 presents the basic concepts of SOM network and illustrates its use as a datareduction tool. This is followed by a discussion of the extended grouping capability. Section 3 describes the data sets, the experimental design and results from the extended SOM. Section 4 compares and integrates the results of the extended SOM with those of K-means cluster analysis, a twostep factor analysis plus K-means procedure, and kth nearest neighbor (kNN) procedure. The paper concludes with a summary of our <sup>fi</sup>ndings.

## 2. Self-Organizing Map (SOM) Networks

A SOM Network is a special type of neural network that can learn from complex, multi-dimensional data and transform them into visually decipherable clusters. The theory of the SOM network is motivated by observations of the operation of the brain. Various human sensory impressions are neurologically mapped into the brain such that spatial or other relations among stimuli correspond to spatial relations among the neurons organized into a two-dimensional map [15].

The SOM network typically has two layers of nodes, the input layer and the Kohonen layer. The input layer is fully connected to a twodimensional Kohonen layer. The network undergoes a self-organization process through a number of training cycles, starting with randomly chosen weights for the nodes in Kohonen layer. During each training cycle, every input vector is considered in turn and the winning node is determined based on the minimum Euclidean distance rule. The weight vectors of the winning node and the nodes in the neighborhood are updated using a weight adaptation function. For a two dimensional Kohonen layer, there are a total of eight neighboring nodes within 1 radius. The neighborhood size (r) changes over time. We started with a neighborhood that covers the whole network and reduce the size as the training progress. Reader may refer to Kiang [9] for detailed algorithm.

The learning algorithm we implemented is similar to the one implemented by Kiang [9]. The training is conducted in many stages; at each stage, we reduce neighborhood size r by one. Note that r affects the number of nodes in the set for weight adjustment. To determine the number of training cycles to be run at each stage, we use the index of disorder D proposed by Mitra and Pal [18]. Essentially, D measures the “improvement” in the “state” of the network at discrete time intervals. When this index falls below a certain threshold (Dbconvergence coef<sup>fi</sup>cient δ), the next stage of training begins with a reduced r value. Reader may refer to Mitra and Pal [18] for the detailed explanation of the algorithm.

The output from SOM networks is a two-dimensional map (Kohonen layer). Each node on the map may represent zero to many input data. The input data that are similar in higher dimension should be close to each other on the output map. Next, we applied the extended SOM network method developed by [9] to automate the segmentation process to <sup>fi</sup>nd the desired number of clusters. The method follows a hierarchical clustering approach and groups the output from SOM based on a minimal variance criterion to merge the neighboring nodes together. Readers should refer to Appendix A for the discussion of the detailed process.

## 3. Experimental design and results

In this study, we have identi<sup>fi</sup>ed eleven attributes from the AACSB database as input parameters to train the SOM network. The eleven attributes are the important structural and identity-based characteristic identi<sup>fi</sup>ed from the school pro<sup>fi</sup>le data collected by the AACSB. They are 1) Degree Offered (Undergraduate/Masters/Doctoral), 2) Private/Public and Commuter/Residential, 3) Carnegie Classi<sup>fi</sup>cation, 4) Endowment, 5) Ratio of Budget to Full Time Equivalent Faculty, 6) MBA Degree Con<sup>fi</sup>rmed, 7) Total Full Time Equivalent Faculty, 8) Ratio of Full Time Faculty Doctorate to Full Time Faculty, 9) Ratio of Full Time Equivalent Faculty to Full Time Faculty, 10) MBA tuition, and 11) GMAT score. Since SOM and most statistical clustering methods work better with numeric data values than with nominal data, we have applied the following encoding scheme to convert nominal variables to numeric values. Table 1 presents the encoding scheme used for the three nominal attributes:

After removing schools with missing data, there are a total of 229 schools (input vectors) with 11 attributes. The input values were preprocessed to reduce the impact of off-scaled attributes on the result of the output. The most commonly used input pre-processing function in SOM is implemented:

$$
\text { Input } _ {i, \text { new }} = \left(\text { Input } _ {i, \text { old }} - \text { Mean } _ {i}\right) / \text { Standard\_Deviation } _ {i},
$$

where i is the attribute number

After some preliminary runs, it shows that the network size has no signi<sup>fi</sup>cant effect on the performance of the network. Therefore we used network sizes of 11×11 for our experiments. We implemented the algorithm in C++ programming language. The output map of the 229 schools is shown in Fig. 1.

We note that the outcome of SOM groups somewhat matches the Carnegie Classi<sup>fi</sup>cation of institutions in Table 1. Unlike supervised training tasks, there is usually no known correct answer to unsupervised training such as clustering. In order to demonstrate that SOM can generate meaningful groupings, we compared the output map of SOM with the Carnegie Classi<sup>fi</sup>cation, a well known classi<sup>fi</sup>cation for schools of higher education. We applied the extended SOM method to further group the 229 schools into <sup>fi</sup>ve clusters based on their closeness on the output map. Since the purpose of the AACSB peer school clustering is not to reproduce the Carnegie Classi<sup>fi</sup>cation, we were not interested in knowing the exact matches of the two results. We manually compared the Carnegie Classi<sup>fi</sup>cation with the SOM output map and labeled the map roughly at the location where the corresponding Carnegie Classi<sup>fi</sup>cation school gathers. Fig. 2 shows the resulting 2-dimensional plot depicting the <sup>fi</sup>ve groups.

Table 1 Encoding scheme.

<table><tr><td colspan="2">Highest Degree Offered</td><td colspan="2">Private/Public &amp; Commuter/Residential</td><td colspan="2">Carnegie Classification</td></tr><tr><td rowspan="2">Under-graduate Masters</td><td>1</td><td>Public &amp; Commuter</td><td>1</td><td>Bachelor/Specialized Institution</td><td>1</td></tr><tr><td>2</td><td>Private &amp; Commuter</td><td>2</td><td>Master&#x27;s I</td><td>2</td></tr><tr><td rowspan="3">Doctoral</td><td>3</td><td>Public &amp; Residential</td><td>3</td><td>Master&#x27;s II</td><td>3</td></tr><tr><td></td><td>Private &amp; Residential</td><td>4</td><td>Doctoral – Intensive</td><td>4</td></tr><tr><td></td><td></td><td></td><td>Doctoral –Extensive</td><td>5</td></tr></table>

![](/api/attachments/TUREXYCQ/fulltext/images/bdaedad910a614a441e77ee65078a6b5bd44446610e26a4b32c78bc7ab53437a.jpg)  
Fig. 1. SOM output map of 229 schools.

A one-way analysis of variance (ANOVA) was conducted to test if there was signi<sup>fi</sup>cant difference in each attribute among the <sup>fi</sup>ve segments formed through SOM. The results are presented in Table 2. Statistically signi<sup>fi</sup>cant differences are detected for all attributes among <sup>fi</sup>ve clusters at pb0.0001. There is a good indication that the extended SOM method has correctly identi<sup>fi</sup>ed <sup>fi</sup>ve signi<sup>fi</sup>cantly different groups and is an effective decision support tool for clustering and visualization of AACSB business schools.

Since all F scores are statistically signi<sup>fi</sup>cant, we then compare sets of two means at a time for each attribute in order to determine where the signi<sup>fi</sup>cance difference lies. To answer the pair comparisons questions we run a series of Tukey's tests, which are similar to a series of t-tests. The results show that Endowment and Budget/Full\_Time\_Equivalent\_Faculty are the two most important attributes that differentiate schools into clusters shown in Fig. 2. Public/Private & Commuter/

Residential and Total Full Time Equivalent Facultyare the least important attributes.

In order to demonstrate the capability of SOM as a decision support tool for selecting peer schools for AACSB review, we selected California State University, Long Beach as an example. The process can be easily replicated using a different host school of your choice. The extended SOM technique can derive any number of clusters as speci<sup>fi</sup>ed by the user. It is a decision support tool that allows human agent interaction [17]. To better identify at least six peer schools as suggested by AACSB, we printed the clustering results of all clusters. The complete school list with corresponding cluster numbers is available upon request. The various clusters can help a candidate school to identify any number of peer schools according to its relative closeness on the map. As an example, the peer schools of California State University, Long Beach (CSULB) identified by the extended SOM are shown in Table 3.

The extended SOM clustering procedure starts with each node on the map representing one cluster. Then it gradually merges neighboring clusters based on a minimal variance criterion as described in Section 2. The school that most closely resembles CSULB based on the 11 input attributes is University of Houston–Clear Lake. For number of clusters from 63 to 100, University of Houston–Clear Lake was the only peer school identi<sup>fi</sup>ed. When the number of clusters is reduced to 62, SOM identi<sup>fi</sup>ed a total of seven peers for CSULB as shown in Table 3.

![](/api/attachments/TUREXYCQ/fulltext/images/7495d03e68176e92f9392d4d85919774b1047b9ad98cd9a7261691a1b2d88be8.jpg)  
Fig. 2. The SOM output map of the 229 schools grouped into <sup>fi</sup>ve clusters.

ANOVA was again conducted to test if there is a signi<sup>fi</sup>cant difference in each attribute among the 62 segments formed through SOM. The results are presented in Table 4. Statistically signi<sup>fi</sup>cant differences are detected for all attributes among all 62 clusters at pb0.0001. When we further reduce the number of clusters, there are more schools merged into the same cluster as CSULB. The decision maker can select any six peer schools from the above list by taking into consideration of other subjective criteria not included in the eleven attributes. In the following section, we compare the peer schools found by SOM with that of other popular clustering methods and demonstrate how SOM can be used as a decision support tool to integrate clustering results from other clustering methods.

Test of the signi<sup>fi</sup>cance of difference among the <sup>fi</sup>ve groups using SOM

<table><tr><td colspan="3">ANOVA</td></tr><tr><td></td><td> $F_{(4, 224)}$ </td><td>Sig.</td></tr><tr><td>Degree Offered</td><td>161.892</td><td>0.000</td></tr><tr><td>Public/Private &amp; Commuter/Residential</td><td>9.252</td><td>0.000</td></tr><tr><td>Carnegie Classification</td><td>84.967</td><td>0.000</td></tr><tr><td>Endowment</td><td>73.461</td><td>0.000</td></tr><tr><td>Budget/Full_Time_Equivalent_Faculty</td><td>138.415</td><td>0.000</td></tr><tr><td>MBA Degree Confirmed</td><td>48.141</td><td>0.000</td></tr><tr><td>Total Full Time Equivalent Faculty</td><td>23.822</td><td>0.000</td></tr><tr><td>Full_Time_Faculty_Doctorate/Total_Full_Time_Faculty</td><td>17.907</td><td>0.000</td></tr><tr><td>Total_Full_Time_Equivalent_Faculty/Total_Full_Time_Faculty</td><td>40.266</td><td>0.000</td></tr><tr><td>MBA Tuition</td><td>61.015</td><td>0.000</td></tr><tr><td>GMAT Score</td><td>51.639</td><td>0.000</td></tr></table>

Peer schools of California State University Long Beach identi<sup>fi</sup>ed by SOM.

<table><tr><td>School number</td><td>School name</td></tr><tr><td>38</td><td>California State University, San Bernardino</td></tr><tr><td>48</td><td>University of Colorado at Colorado Springs</td></tr><tr><td>76</td><td>Georgia Southern University</td></tr><tr><td>78</td><td>Grand Valley State University</td></tr><tr><td>83</td><td>University of Houston–Clear Lake</td></tr><tr><td>128</td><td>University of Nebraska at Omaha</td></tr><tr><td>141</td><td>University of Northern Iowa</td></tr></table>

Table 6  
Table 5  
Table 4 Test of the signi<sup>fi</sup>cance of difference among the 62 groups using SOM.

<table><tr><td colspan="3">ANOVA</td></tr><tr><td></td><td> $F_{(61, 167)}$ </td><td>Sig.</td></tr><tr><td>Degree Offered</td><td>77.962</td><td>0.000</td></tr><tr><td>Public/Private &amp; Commuter/Residential</td><td>27.831</td><td>0.000</td></tr><tr><td>Carnegie Classification</td><td>20.220</td><td>0.000</td></tr><tr><td>Endowment</td><td>25.595</td><td>0.000</td></tr><tr><td>Budget/Full_Time_Equivalent_Faculty</td><td>19.175</td><td>0.000</td></tr><tr><td>MBA Degree Confirmed</td><td>12.290</td><td>0.000</td></tr><tr><td>Total Full Time Equivalent Faculty</td><td>7.886</td><td>0.000</td></tr><tr><td>Full_Time_Faculty_Doctorate/Total_Full_Time_Faculty</td><td>11.882</td><td>0.000</td></tr><tr><td>Total_Full_Time_Equivalent_Faculty/Total_Full_Time_Faculty</td><td>7.909</td><td>0.000</td></tr><tr><td>MBA Tuition</td><td>13.247</td><td>0.000</td></tr><tr><td>GMAT Score</td><td>13.756</td><td>0.000</td></tr></table>

## 4. Comparative analysis and integration

K-means analysis is among the most popular clustering methods used in scienti<sup>fi</sup>c and business applications [4]. In this section we <sup>fi</sup>rst compared the extended SOM network solutions with K-means clustering method. Previous research has suggested that when using a statistical method, if signi<sup>fi</sup>cant correlation among the attributes is expected, such as Degree Offered and Carnegie Classi<sup>fi</sup>cation, a twostep approach typically is used [21]. Thus, we next compared the extended SOM network solutions to a two-step procedure that uses factor analysis to combine related variables to reduce the dimensions before subjecting the output factors to the K-means clustering method.

Another popular non-parametric (or distribution-free) clustering procedure, kth nearest neighbor (kNN) developed by Wong and Lane [23], is a density linkage clustering technique. kNN relaxes the normality assumption as well as eliminating the functional form required in most other statistical models. Using the nearest neighbor decision rule, an observation is assigned to the group to which the majority of its k nearest neighbors belongs. This method has the merits of better approximating the sample distribution by dividing the variable space into any arbitrary number of decision regions, with the maximum bounded by the total number of observations. A study by Wettschereck and Dietterich [22] shows that when applied to learning, kNN is a fairly robust and effective classi<sup>fi</sup>er compared with the nearesthyperrectangle algorithm, an inductive method based on the nested generalized exemplar (NGE) theory [19]. Previous research compares kNN with other statistical models such as discriminant analysis and suggests that kNN outperforms when normality, linearity, and identical covariance assumptions are not in place and/or when the data set is multi-modal. Moreover, the performance of kNN may improve when the sample size is increased [10]. In the following study, we use California State University, Long Beach as a case study to demonstrate how a school can use the two-dimensional SOM map as an integration tool to compare the results of the four methods and identify the six peer schools.

K-means identi<sup>fi</sup>es 7 peer schools for CSULB

<table><tr><td>School number</td><td>School name</td></tr><tr><td>7</td><td>University of Akron</td></tr><tr><td>61</td><td>East Tennessee State University</td></tr><tr><td>83</td><td>University of Houston-Clear Lake</td></tr><tr><td>92</td><td>Indiana State University</td></tr><tr><td>116</td><td>The University of Michigan-Flint</td></tr><tr><td>122</td><td>University of Missouri-Kansas City</td></tr><tr><td>144</td><td>Oakland University</td></tr></table>

Test of the signi<sup>fi</sup>cance of difference among the 55 groups using K-means analysis.

<table><tr><td colspan="3">ANOVA</td></tr><tr><td></td><td> $F_{(69, 259)}$ </td><td>Sig.</td></tr><tr><td>Degree Offered</td><td>2,655,427,742,144,430.000</td><td>0.000</td></tr><tr><td>Public/Private &amp; Commuter/Residential</td><td>31.933</td><td>0.000</td></tr><tr><td>Carnegie Classification</td><td>21.028</td><td>0.000</td></tr><tr><td>Endowment</td><td>62.945</td><td>0.000</td></tr><tr><td>Budget/Full_Time_Equivalent_Faculty</td><td>63.571</td><td>0.000</td></tr><tr><td>MBA Degree Confirmed</td><td>28.259</td><td>0.000</td></tr><tr><td>Total Full Time Equivalent Faculty</td><td>13.406</td><td>0.000</td></tr><tr><td>Full_Time_Faculty_Doctorate/</td><td>12.356</td><td>0.000</td></tr><tr><td>Total_Full_Time_Faculty</td><td></td><td></td></tr><tr><td>Total_Full_Time_Equivalent_Faculty/</td><td>15.370</td><td>0.000</td></tr><tr><td>Total_Full_Time_Faculty</td><td></td><td></td></tr><tr><td>MBA Tuition</td><td>15.151</td><td>0.000</td></tr><tr><td>GMAT Score</td><td>13.524</td><td>0.000</td></tr></table>

Version 15.0 for Windows of the SPSS Statistical package was used to perform the K-means clustering method as well as the Factor/ K-means procedure that uses the factor scores from factor analysis as inputs to K-means clustering method Unlike SOM, K-means requires that the number of clusters be determined at the outset. Since there are a total of 229 schools and we seek to identify at least six peers for CSULB, we believe that 70 clusters should be more than enough and, therefore, set it as our upper limit. We ran K-means cluster analysis starting at 5 clusters and increment the cluster numbers by 5 each run until there are 70 clusters. A total of 14 runs were performed. Unfortunately K-means analysis cannot derive exactly six peers for CSULB. Both the 55 and 70 clusters yielded the same set of seven peer schools for CSULB as shown in Table 5. The ANOVA results indicate that statistically there are signi<sup>fi</sup>cant differences for all attributes among all clusters at pb0.0001 for both the 55 and 70 clusters as shown in Table 6.

In the <sup>fi</sup>rst step of the Factor/K-means procedure factor analysis with varimax rotation was employed. The objective was to obtain fewer dimensions that re<sup>fl</sup>ect succinctly the relationships among these interrelated variables. The Kaiser's rule of “eigen-value greater than 1” was applied and results in three factors to be retained [3]. The total amount of variability accounted for by the three factors is 68.06%. The second step was to use the K-means clustering algorithm to group the 229 schools into segments with at least six other schools in the same segment as CSULB. We again ran 14 experiments starting with 5 clusters and increment by 5 each time until reached 70 clusters. However, none of the runs yielded a result with the number of peer schools of CSULB close to 6. Thus, additional 40 runs were made between 20 and 60 clusters. Finally, we were able to identify eight schools as CSULB's peers using 31 clusters as shown in Table 7. Again, the ANOVA results indicate that there are statistically signi<sup>fi</sup>cant differences for all attributes among all 31 clusters at pb0.0001 as shown in Table 8.

We noticed that there is signi<sup>fi</sup>cant overlapping between the results of K-means and Factor/K-means approaches. As shown in Tables 5 and 7, both methods identify East Tennessee State University,

Factor/K-means identi<sup>fi</sup>es 8 peer schools for CSULB

<table><tr><td>School number</td><td>School name</td></tr><tr><td>4</td><td>Arizona State University-West Campus</td></tr><tr><td>14</td><td>Auburn University Montgomery</td></tr><tr><td>23</td><td>Bowling Green State University</td></tr><tr><td>61</td><td>East Tennessee State University</td></tr><tr><td>83</td><td>University of Houston-Clear Lake</td></tr><tr><td>92</td><td>Indiana State University</td></tr><tr><td>116</td><td>The University of Michigan-Flint</td></tr><tr><td>122</td><td>University of Missouri-Kansas City</td></tr></table>

Table 11  
Table 8  
Test of the signi<sup>fi</sup>cance of difference among the 31 groups using Factor/K-means.

<table><tr><td colspan="3">ANOVA</td></tr><tr><td></td><td> $F_{(30, 198)}$ </td><td>Sig.</td></tr><tr><td>Degree Offered</td><td>33.198</td><td>0.000</td></tr><tr><td>Public/Private &amp; Commuter/Residential</td><td>10.516</td><td>0.000</td></tr><tr><td>Carnegie Classification</td><td>17.439</td><td>0.000</td></tr><tr><td>Endowment</td><td>55.588</td><td>0.000</td></tr><tr><td>Budget/Full_Time_Equivalent_Faculty</td><td>62.054</td><td>0.000</td></tr><tr><td>MBA Degree Confirmed</td><td>14.458</td><td>0.000</td></tr><tr><td>Total Full Time Equivalent Faculty</td><td>13.609</td><td>0.000</td></tr><tr><td>Full_Time_Faculty_Doctorate/Total_Full_Time_Faculty</td><td>20.897</td><td>0.000</td></tr><tr><td>Total_Full_Time_Equivalent_Faculty/Total_Full_Time_Faculty</td><td>34.213</td><td>0.000</td></tr><tr><td>MBA Tuition</td><td>14.244</td><td>0.000</td></tr><tr><td>GMAT Score</td><td>13.700</td><td>0.000</td></tr></table>

University of Houston–Clear Lake, Indiana State University, the University of Michigan–Flint, and University of Missouri–Kansas City as CSULB's peers.

SAS 9.1 statistical package was used to run the kNN method. To <sup>fi</sup>nd six peer schools for California State University Long Beach, we implemented the Ward clustering method [1] with k, the number of neighbor nodes, set to 5 to 12. The results of all eight runs (k=5 to 12) yield the same peer schools for CSULB. The Ward clustering method implemented a hierarchic agglomerative clustering algorithm to gradually merge nearby clusters to form the desired number of groups. However, the results did not provide the acceptable number of peer schools for CSULB. The closest we can get from kNN is a cluster with <sup>fi</sup>ve peer schools for CSULB when we reached 70 clusters. If we further merge this cluster, we will have a cluster with 30 peer schools for CSULB when there are 27 clusters and we feel that would be too many peer schools to be considered.

The <sup>fi</sup>ve peer schools identi<sup>fi</sup>ed by all eight runs (k=5 to 12) of kNN are the same and are shown in Table 9. ANOVA results for 70 clusters using kNN clustering method are presented in Table 10. It shows that there is signi<sup>fi</sup>cant difference in each attribute across the 70 clusters at pb0.0001.

## 4.1. Comparative analysis

Any metric developed to measure the goodness of a clustering design will, in general, <sup>fi</sup>nd that a clustering design with a large number of clusters to be a better design than that with a fewer number of clusters. This is because, for a given data set, a design with a larger number of clusters has fewer members in each cluster and, therefore, the members within a cluster are more likely to be closer to each other. A bias can be introduced in the metric to counter this effect in measurement, but this adjustment is always subjective. The desired number of clusters is problem-dependent. Therefore, it is fair to compare the performance of different clustering techniques with only equal number of clusters. For one technique to be judged better than another, it should perform consistently better than the others for all different clustering numbers.

One way to evaluate the performance of different clustering results is to compare the total within cluster variance. For the same number of clusters, the smaller the within cluster variance is, the more homogenous are the cluster members. Therefore, it is a good indication of the clustering performance. Table 11 and Fig. 3 compare the total variance of the four approaches based on 5, 10, 20, 40, 60, and 80 cluster results.

kNN identi<sup>fi</sup>es 5 peer schools for CSULB.

<table><tr><td>School number</td><td>School name</td></tr><tr><td>4</td><td>Arizona State University-West Campus</td></tr><tr><td>83</td><td>University of Houston-Clear Lake</td></tr><tr><td>92</td><td>Indiana State University</td></tr><tr><td>116</td><td>The University of Michigan-Flint</td></tr><tr><td>122</td><td>University of Missouri-Kansas City</td></tr></table>

Table 10  
Test of the signi<sup>fi</sup>cance of difference among the 70 clusters using kNN.

<table><tr><td colspan="3">ANOVA</td></tr><tr><td></td><td> $F_{(69, 159)}$ </td><td>Sig.</td></tr><tr><td>Degree Offered</td><td>234.410</td><td>0.000</td></tr><tr><td>Public/Private &amp; Commuter/Residential</td><td>53.333</td><td>0.000</td></tr><tr><td>Carnegie Classification</td><td>34.532</td><td>0.000</td></tr><tr><td>Endowment</td><td>50.110</td><td>0.000</td></tr><tr><td>Budget/Full_Time_Equivalent_Faculty</td><td>57.157</td><td>0.000</td></tr><tr><td>MBA Degree Confirmed</td><td>21.660</td><td>0.000</td></tr><tr><td>Total Full Time Equivalent Faculty</td><td>16.643</td><td>0.000</td></tr><tr><td>Full_Time_Faculty_Doctorate/Total_Full_Time_Faculty</td><td>11.685</td><td>0.000</td></tr><tr><td>Total_Full_Time_Equivalent_Faculty/Total_Full_Time_Faculty</td><td>17.608</td><td>0.000</td></tr><tr><td>MBA Tuition</td><td>16.160</td><td>0.000</td></tr><tr><td>GMAT Score</td><td>16.049</td><td>0.000</td></tr></table>

The results show that kNN consistently generates clustering results with the lowest total within cluster variance except when there are <sup>fi</sup>ve clusters. Factor/K-means tends to generate the highest total within cluster variances. We noticed that the differences in total within cluster variances among different methods increase as the number of clusters increases. This may due to uneven cluster sizes generated by the clustering methods.

Next, we focus on the one cluster with CSULB peer schools and evaluate the performance of the four methods based on the average Euclidean distance of the selected peers from CSULB. Table 13 rank orders the Euclidean distances of all the selected CSULB peer schools by the four methods. We also marked the schools selected by each method in the table. It is interesting to note that the results of SOM and the K-means analysis seem to complement each other. We also noticed that four out of the <sup>fi</sup>ve peer schools identi<sup>fi</sup>ed by kNN are the same as that of the K-means procedure and the peers identi<sup>fi</sup>ed by kNN is a subset of the peers identi<sup>fi</sup>ed by the Factor/K-means procedure. The only common peer school identi<sup>fi</sup>ed by all four methods is University of Houston–Clear Lake. Although kNN had the lowest total within cluster variance, the average Euclidean distance of the peer schools selected by kNN have the greatest distance from CSULB among all four methods. SOM selected peer schools with lowest average Euclidean distance among the four methods. Since it is favorable to the cluster with fewer schools when computing average distance, in Table 13 we calculated both the average of all peer schools and the average of only the closest <sup>fi</sup>ve peer schools to compare with kNN. Independent-samples t test is run for all combinations of the four methods to verify if there are signi<sup>fi</sup>cant differences among the average Euclidean distances of the four methods. No statistically signi<sup>fi</sup>cant difference is detected among the four methods at p=0.01.

## 4.2. SOM as an integration tool

Most clustering procedures are sensitive not only to the measurements being used but also to the objective functions and implementation of the algorithms. Among the four clustering techniques implemented in this study, all of them have been successfully applied to different problem domains and there is no de<sup>fi</sup>nite answer regarding which is the best clustering method. Previous studies have suggested that each clustering method has its strengths and weaknesses and that the effectiveness of a clustering technique is impacted by the characteristic of the data set [8]. Given the differences in the clustering methods, it is the reason why we believe the proposed system that combines results from heterogeneous clustering methods and presents them in an integrated manner can serve as a powerful and effective decision support tool. This is analogous to consulting experts with different backgrounds about the same problem and integrating their results. In this research we demonstrate the use of SOM visual map as a decision support tool to visualize and integrate the results from the four clustering methods.

Total within cluster variances.

<table><tr><td></td><td>80</td><td>60</td><td>40</td><td>20</td><td>10</td><td>5</td></tr><tr><td>kNN</td><td>179.23</td><td>259.58</td><td>390.24</td><td>653.31</td><td>968.33</td><td>1312.89</td></tr><tr><td>K-means</td><td>196.80</td><td>285.74</td><td>421.33</td><td>678.35</td><td>979.30</td><td>1,311.00</td></tr><tr><td>SOM</td><td>331.98</td><td>391.98</td><td>493.01</td><td>713.59</td><td>987.68</td><td>1,324.83</td></tr><tr><td>Factor/K-means</td><td>348.43</td><td>449.76</td><td>470.96</td><td>774.520</td><td>1,034.95</td><td>1,315.28</td></tr></table>

![](/api/attachments/TUREXYCQ/fulltext/images/7f39d9a5ae2b280311e68f757e401dc3b42cc72eacb1af22c6ffb76205e5bdfa.jpg)  
Fig. 3. Total within cluster variances of the four methods.

When looking closely at the resulting peer schools of the four methods as shown in Table 13, we notice substantial overlapping among the results. To demonstrate how SOM visual map can serve as a decision support tool to integrate the results from all four methods, we marked the peer schools of CSLUB identi<sup>fi</sup>ed by the four methods on SOM map as shown in Fig. 4.

The salient feature of the extended SOM network is its ability to reduce the input space to a one- or two-dimensional output map while maintaining the original topological relations. In other words, the data points that were close in the higher dimensional space should remain close in the reduced lower dimensional map. Therefore, when grouped into clusters, the schools that are close to the borderlines on the SOM map possess characteristics belonging to two or more groups. Besides providing the cluster membership information, the SOM visual map clearly depicts the actual relationship among the schools within and among different clusters. We believe the information revealed in the SOM visual map that is not available from other techniques is a valuable decision aid in addition to the cluster membership information.

Using SOM as a decision support tool to integrate cluster results from other clustering methods allows the decision maker to visualize the relationship of the peer schools selected by different clustering tools. The fact that all peer schools are within two radius of CSULB on SOM map further con<sup>fi</sup>rms that the visual map generated by SOM is consistent with the results of other traditional clustering methods. The decision maker can start identifying peer schools of CSULB from the schools within one radius of CSULB on the SOM map. Various selection criteria can be implemented in integrating the results to identify the <sup>fi</sup>nal set of peer schools. For example, we can select the schools within one radius with the most number of votes from all four methods. Alternatively, minimum Euclidean distance can be used as the selection criterion. If there is not enough number of peer schools within one radius, the decision maker can gradually increase the radius distance to increase the number of choices. In the means time, subjective criteria that were not included in the original eleven attributes, such as vicinity and familiarity of the school, can also be taken into consideration during the interactive selection process.

## 5. Limitations and conclusions

In this study, we <sup>fi</sup>rst applied the SOM network to identify peer schools for AACSB accreditation. We used a two-dimensional map, the most common Kohonen network, to capture the relationships among the 229 schools. We further applied the extended SOM method to group the 229 schools into <sup>fi</sup>ve clusters to compare with the Carnegie Classi<sup>fi</sup>cation. The output map of SOM provides a graphical interface to help candidate schools to visualize the relationship among the schools, thus, reducing the task from a multi-dimensional problem to a two-dimensional map.

Rank order of selected peer schools based on Euclidean distance from CSULB.

<table><tr><td>Rank</td><td>School number</td><td>School name</td><td>Euclidean distance</td><td>SOM</td><td>K-means</td><td>Factor/K-means</td><td>kNN</td></tr><tr><td>1</td><td>83</td><td>University of Houston-Clear Lake</td><td>1.0009</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>2</td><td>7</td><td>University of Akron</td><td>1.4581</td><td></td><td>√</td><td></td><td></td></tr><tr><td>3</td><td>61</td><td>East Tennessee State University</td><td>1.7249</td><td></td><td>√</td><td>√</td><td></td></tr><tr><td>4</td><td>141</td><td>University of Northern Iowa</td><td>1.7421</td><td>√</td><td></td><td></td><td></td></tr><tr><td>5</td><td>78</td><td>Grand Valley State University</td><td>1.7500</td><td>√</td><td></td><td></td><td></td></tr><tr><td>6</td><td>38</td><td>California State University, San Bernardino</td><td>1.8086</td><td>√</td><td></td><td></td><td></td></tr><tr><td>7</td><td>144</td><td>Oakland University</td><td>1.8784</td><td></td><td>√</td><td></td><td></td></tr><tr><td>8</td><td>128</td><td>University of Nebraska at Omaha</td><td>1.8848</td><td>√</td><td></td><td></td><td></td></tr><tr><td>9</td><td>48</td><td>University of Colorado at Colorado Springs</td><td>1.9750</td><td>√</td><td></td><td></td><td></td></tr><tr><td>10</td><td>76</td><td>Georgia Southern University</td><td>2.0458</td><td>√</td><td></td><td></td><td></td></tr><tr><td>11</td><td>92</td><td>Indiana State University</td><td>2.1154</td><td></td><td>√</td><td>√</td><td>√</td></tr><tr><td>12</td><td>14</td><td>Auburn University Montgomery</td><td>2.2291</td><td></td><td></td><td>√</td><td></td></tr><tr><td>13</td><td>116</td><td>The University of Michigan-Flint</td><td>2.2480</td><td></td><td>√</td><td>√</td><td>√</td></tr><tr><td>14</td><td>122</td><td>University of Missouri-Kansas City</td><td>2.3027</td><td></td><td>√</td><td>√</td><td>√</td></tr><tr><td>15</td><td>4</td><td>Arizona State University</td><td>2.4445</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>16</td><td>23</td><td>Bowling Green State University</td><td>2.4802</td><td></td><td></td><td>√</td><td></td></tr><tr><td colspan="4">Average Euclidean distance of all peer schools</td><td>1.74</td><td>1.82</td><td>2.068</td><td>2.02</td></tr><tr><td colspan="4">Average Euclidean distance of the closest 5 peer schools</td><td>1.64</td><td>1.64</td><td>1.86</td><td>2.02</td></tr></table>

![](/api/attachments/TUREXYCQ/fulltext/images/ee84684fdff3e89183e4e3d16aceede5ac4dccc271a4607c78802400fe274302.jpg)  
Fig. 4. Clustering results of the four methods plotted on SOM result map.

We then compared the result from SOM with that of K-means analysis, a two-step Factor/K-means process, and kth nearest neighbor method. The results show that the extended SOM method generates distinct groups similar to that of the K-means and Factor/K-means, and kNN approaches. The main advantage of using the extended SOM method over the other clustering approaches is the added visual map. Although kNN consistently generates lowest total within cluster variance among all four methods, we have a problem <sup>fi</sup>nding cluster results for the desired number of peer schools for CSULB.

Similar to other hierarchical clustering methods, kNN is somewhat rigid in terms of the composition of clusters (number of data points in each cluster) for a given number of clusters and input data set. This weakness may prevent it from generating clusters with desired number of data points. In our example, kNN generate clusters with either <sup>fi</sup>ve peers or thirty peers for CSULB. We have chosen to use the <sup>fi</sup>ve peer school result because thirty 30 peer schools are too many to be considered. In a problem situation that requires at least six peers, it could be quite a challenge to identify one additional peer school among the remaining 25 schools without other supporting tools.

The limitation of the two-step Factor/K-means approach is the common problem that faces most statistical methods. Clustering algorithms are not statistical in the sense that they do not rely on any distributional assumptions. However, statistical dimension reduction routines such as the factor analysis evolve around the Pearson's product moment correlation coef<sup>fi</sup>cient. Multivariate normality and linearity among the variables are the key assumptions underlying the use of correlation coef<sup>fi</sup>cient. Violations of the normality assumption may lead to bias and incorrect assignment of schools to the resulting segments and eventually lead to poor selection of peer schools using the two-step approach. Moreover, both K-means analysis and Factor/ K-means approach also have the same problem regarding arriving at the exact number of desired peer schools. Therefore, in our study numerous trial-and-error runs of both approaches have been conducted before we can arrive at the clustering results with the desired number of peer schools for CSULB. There are ways to <sup>fi</sup>ne tune the performance of each method. For example, trimming can be applied to K-means analysis to eliminate outliers and, hence, improve the balancing of cluster sizes and lower the total within cluster variance. A similar mechanism can be applied to SOM as well to improve the total within cluster variance. However, the purpose of this research is not to come up with the best performing method for a given data set, but to suggest a way to combine and present the results from different clustering methods in an integrated manner.

Although the extended SOM method also implements a hierarchical clustering algorithm to further group nodes on SOM map into desired number of cluster, it overcomes the weakness by providing the visual map to show the relationships of the data points both within its cluster and with their neighboring clusters. Therefore, the decisionmaker can interactively determine the composition of the clusters using the output map of SOM and incorporate subjective criteria when desired. The two-dimensional plot provides an easy-to-read graphical interface that does not require specialized analytical knowledge to interpret the results. It is a valuable decision support tool that helps the decision maker visualizes the relationships among inputs.

The SOM map can be used to integrate clustering results from any type of clustering methods. You simply mark the cluster members from all clustering methods on the SOM output map, similar to the SOM map in Fig. 4. You will be able to view the relationships among the cluster members for all methods. Additional mechanisms, such as the majority vote rule and the weighted vote rule, can be used to systematically combine the results to derive an integrated solution. Moreover, the integration capability of the SOM network allows applications of the peer selection process for performance review purpose other than AACSB. The same methodology can be applied in business process benchmarking, employee performance evaluation, competitive analysis of <sup>fi</sup>rms in various industries, etc. We believe the extended SOM method can be an effective tool to build decision support systems for other performance review tasks.

Appendix A. The contiguity-constrained clustering method (adopted from Kiang et al. [12])

Step 1. For each node , calculate the centroid (<sup>⇀</sup>c ) of node as

$$
\overrightarrow {c _ {i}} = \frac {1}{| n o d e _ {i} |} \sum_ {\overline {{x}} \in n o d e _ {i}} \overrightarrow {x}.
$$

where | node | is the number of input vectors associated with the node.

Step 2. Assign a group number $\left( G _ { k } \right)$ to each node if |node | N 0, and update the corresponding centroid value.

Step 3. Calculate the overall variance of the map:

Sum the square distance between input vector x and the group centroid $\scriptstyle { \overrightarrow { c _ { k } } }$ for all <sup>⇀</sup>x in $G _ { k } .$ Calculate for every group k.

$$
V _ {k} = \sum | | \vec {x} - \vec {c} _ {k} | |, \vec {x} \in G _ {k}.
$$

Total the variances from all groups. This will give us the global variance of the map:

$$
V _ {\text { Total }} = \sum V _ {k}.
$$

Step 4. For each pair of neighboring groups, calculate the total variance of the map if the two groups were merged. Merge the two groups that result in the minimum global variance.

Calculate the new centroid for $G _ { p q } { \mathrm { ~ i f ~ } } G _ { p }$ and $G _ { q }$ were merged:

$$
\vec {c} _ {p q} = \left(| n o d e _ {p} | ^ {*} \vec {c} _ {p} + | n o d e _ {q} | ^ {*} \vec {c} _ {q}\right) / \left(| n o d e _ {p} | + | n o d e _ {q} |\right).
$$

Calculate the new variance if $G _ { p }$ and $G _ { q }$ were merged (modi<sup>fi</sup>ed from Murtagh (1985)):

$V _ { p q } = \sum \mid \mid \overrightarrow { x } - \overrightarrow { c } _ { p q } \mid \mid$ ; for all $\vec { x } , \vec { x } \in G _ { p }$ or $\vec { x } \in G _ { q }$

Calculate the new global variance for merging $G _ { p }$ and $G _ { q } .$

$$
V _ {p q \mathrm{Total}} = V _ {\mathrm{Total}} + V _ {p q} - V _ {p} - V _ {q}.
$$

Calculate the $V _ { p q \mathrm { T o t a l } }$ for every pair of p and q on the map. For each iteration, groups p and q must be within a <sup>fi</sup>xed radius distance on the grid. We start with radius distance=1, hence, for each node there are eight neighboring nodes within that distance. We increase the radius distance by one each time if there is no neighboring group within current radius distance for all groups k. Finally, we merge the two groups that result in global minimal variance.

Update $V _ { \mathrm { T o t a l } }$ and the group number and group centroid of the two newly merged groups.

Step 5. Repeat step 4 until only one cluster or the pre-speci<sup>fi</sup>ed number of clusters has been reached.

## References

[1] M.R. Anderberg, Cluster Analysis for Applications, Academic Press, New York, 1973.

[2] K. Ciesielski, M. Dramiriski, M.A. Klopotek, On some clustering algorithms for document maps creation, Intelligent Information Processing and Web Mining, 2005.

[3] H.C. Co, E. Patuwo, M.Y. Hu, The human factor in advanced manufacturing technology adoption, International Journal of Operations & Production Management 18 (1) (1998) 87–106.

[4] I. Davison Understanding, K-means non-hierarchical clustering, SUNY Albany – Technical Report 02-2.2002 http://www.cs.albany.edu/\~davidson/courses/CSI635 UnderstandingK-MeansClustering,pdf.

[5] J.F. Fairbank, G. Labianca, Picking the Perfect Peers, BizEd, Novmber/December 2003, pp. 36–41.

[6] F.D. Gibbons, F.P. Roth, Judging the quality of gene expression-based clustering methods using gene annotation, Genome Research, Cold Spring Harbor Lab, 2002.

[7] J. Herrero, A. Valencia, J. Dopazo, A hierarchical unsupervised growing neural network for clustering gene expression patterns, Bioinformatics, Oxford Univ Press, 2001.

[8] A.K. Jain, M.N. Murty, P.J. Flynn, Data clustering: a review, ACM Computing Surveys (CSUR) 31 (3) (September 1999) 264–323

[9] M.Y. Kiang, Extending the Kohonen self-organizing map networks for clustering analysis, Journal of Computational Statistics and Data Analysis (2001).

[10] M.Y. Kiang, A comparative assessment of classi<sup>fi</sup>cation methods, Decision Support Systems 35 (4) (July 2003) 441–454.

[11] M.Y. Kiang, M.Y. Hu, D.M. Fisher, The effect of sample size on the extended selforganizing map network for market segmentation, Decision Support Systems 42 (1) (2006) 36–47 2006.

[12] M.Y. Kiang, D.M. Fisher, M.Y. Hu, R.T. Chi, Using an extended self-organizing map network to forecast market segment membership, in: G. Peter Zhang (Ed.), Neural Networks in Business Forecasting, Idea Group Inc. book, 2004, pp. 142–157

[13] M.Y. Kiang, D.M. Fisher. Selecting the right MBA schools — an application of selforganizing map networks. Expert Systems with Applications. 35, 3, 946–955.

[14] T. Kohonen, in: E.R. Caianiello, G. Musso (Eds.), Cybernetic Systems: Recognition, Learning, Self-Organization, Research Studies Press, Ltd., Letchworth, Herfordshire, UK, 1984.

[15] T. Kohonen, Self-Organization and Associative Memory, second ed.Springer–Verlag, 1989.

[16] T. Kohonen, Self-Organizing Maps, Springer, 1995.

[17] M. Lewis, Designing for human–agent interaction, AI Magazine, 1998.

[18] S. Mitra, S.K. Pal, Self-organizing neural network as a fuzzy classi<sup>fi</sup>er, IEEE Transactions on Systems, Man, and Cybernetics 24 (3) (March 1994) 385–399.

[19] S. Salzberg, A nearest hyperrectangle learning method, Machine Learning 6 (1991) 277–309.

[20] O. Turetken, R. Sharda, Clustering-based visual interfaces for presentation of web search results: an empirical investigation, Information Systems Frontiers 7 (3) (July 2005) 273–297.

[21] M. Wedel, W. Kamakura, Market Segmentation: Conceptual and Methodological Foundations, Kluwer Academic Publisher, 1999.

[22] D. Wettschereck, T.G. Dietterich, An experimental comparison of the nearestneighbor and nearest-hyperrectangle algorithms, Machine Learning 19 (1995).

[23] M.A. Wong, T. Lane, A kth nearest neighbour clustering procedure, Journal of Roya Statistical Society B 45 (3) (1983) 362–368.

Melody Y. Kiang is Professor of Computer Information Systems at California State University, Long Beach. She received her M.S. in MIS from the University of Wisconsin, Madison, and Ph.D. in MSIS from the University of Texas at Austin. Prior to join CSULB, she was Associate Professor at Arizona State University. Her research interests include the development and applications of arti<sup>fi</sup>cial intelligence techniques to a variety of business problems. Her research has appeared in Information Systems Research (ISR), Management Science, Journal of Management Information Systems, Decision Support Systems, IEEE Transactions on SMC. EIOR, and other professional journals. She is an Associate Editor of Decision Support Systems and Co-Editor of Journal of Electronic Commerce Research

Dorothy M. Fisher is a Professor of Information Systems at California State University, Dominguez Hills. She received a M.A. from Duke University and a Ph.D. from Kent State University. Dr. Fisher has had broad consulting experience with private <sup>fi</sup>rms as well as educational institutions. Her research emphasizes the applications of statistical and arti<sup>fi</sup>cial intelligence techniques to management problems. Dr. Fisher has published papers in the Journal of Computer Information Systems, the Journal of Systems Management, the Journal of Applied Business Research, and other academic and professional journals. Currently she is the managing editor of the Journal of Electronic Commerce Research.

Jengchung V. Chen (Ph.D., University of Hawaii) is Associate Professor in International Management at National Cheng Kung University, Taiwan, R.O.C. He has written articles about telecommunications, privacy, trust, and technology.

Steven A. Fisher is Chair and Professor of Accountancy at California State University, Long Beach. He holds a D.B.A. from Kent State University and is a CPA and a CMA.

Dr. Robert Chi is the chair and professor of Information Systems Department at California State University, Long Beach. He obtained his Ph.D. from University of Texas at Austin and his MS from University of Wisconsin at Madison. His teaching interests include E-commerce, Internet marketing, Data Base Management, Data Communication and Web Development. He has published research articles in Journal of Decision Support Systems, Journal of MIS and so on. He is the founder and co-editor of Journal of Electronic Commerce Research
